#!/usr/bin/env node
/* Runs every article's interactive against a stand-in DOM and canvas, then
 * exercises every control it registered. Catches the class of defect that
 * check.py cannot see and a reader finds immediately:
 *
 *   - the script throws, on load or on interaction
 *   - the canvas backing store grows after setup (the doubling bug)
 *   - NaN or Infinity reaches a drawing call, so nothing appears
 *   - getElementById returns null for an id the script relies on
 *
 * Usage:  node _style/runtime-check.js [FILE ...]
 * Exit status is 1 if anything is reported.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const NUMERIC_CANVAS_METHODS = new Set([
  'moveTo','lineTo','arc','arcTo','rect','fillRect','strokeRect','clearRect',
  'bezierCurveTo','quadraticCurveTo','fillText','strokeText','translate',
  'scale','rotate','setTransform','transform','ellipse','createLinearGradient'
]);

function makeHarness(html, report){
  // ---- what elements does the markup actually declare? ----
  const ids = new Map();
  const idRe = /<(\w+)([^>]*\bid="([^"]+)"[^>]*)>/g;
  let m;
  while((m = idRe.exec(html))){
    ids.set(m[3], { tag: m[1].toLowerCase(), attrs: m[2] });
  }
  // a <select> reports the value of its selected <option>, or of the first one
  const selectValue = new Map();
  const selRe = /<select[^>]*\bid="([^"]+)"[^>]*>([\s\S]*?)<\/select>/g;
  while((m = selRe.exec(html))){
    const opts = [...m[2].matchAll(/<option([^>]*)>/g)].map(o => o[1]);
    if(!opts.length) continue;
    const chosen = opts.find(o => /\bselected\b/.test(o)) || opts[0];
    const v = /value="([^"]*)"/.exec(chosen);
    selectValue.set(m[1], v ? v[1] : '');
  }
  const attr = (s, name) => {
    const r = new RegExp(name + '="([^"]*)"').exec(s || '');
    return r ? r[1] : null;
  };

  const allElements = [];
  function makeEl(tag, attrs, id){
    const cls = new Set((attr(attrs, 'class') || '').split(/\s+/).filter(Boolean));
    const el = {
      tagName: (tag || 'div').toUpperCase(),
      _id: id || null,
      _attrs: {},
      _listeners: {},
      children: [],
      style: {},
      textContent: '',
      innerHTML: '',
      hidden: false,
      value: attr(attrs, 'value') || '',
      min: attr(attrs, 'min'),
      max: attr(attrs, 'max'),
      step: attr(attrs, 'step'),
      type: attr(attrs, 'type'),
      classList: {
        add: c => cls.add(c),
        remove: c => cls.delete(c),
        toggle: (c, on) => { on === undefined ? (cls.has(c) ? cls.delete(c) : cls.add(c)) : (on ? cls.add(c) : cls.delete(c)); },
        contains: c => cls.has(c)
      },
      _classes: cls,
      addEventListener(t, fn){ (this._listeners[t] = this._listeners[t] || []).push(fn); },
      removeEventListener(){},
      setAttribute(k, v){ this._attrs[k] = String(v); if(k === 'class') { cls.clear(); String(v).split(/\s+/).filter(Boolean).forEach(x => cls.add(x)); } },
      getAttribute(k){ return k === 'class' ? Array.from(cls).join(' ') : (this._attrs[k] !== undefined ? this._attrs[k] : null); },
      appendChild(c){ this.children.push(c); return c; },
      removeChild(){},
      closest(){ return makeEl('div', ''); },
      querySelector(){ return null; },
      querySelectorAll(){ return []; },
      focus(){},
      getBoundingClientRect(){ return { left:0, top:0, width:700, height:300 }; },
      dispatchEvent(){ return true; }
    };
    (attr(attrs, 'data-k') || attr(attrs, 'data-a') || attr(attrs, 'data-d') ||
     attr(attrs, 'data-dir') || attr(attrs, 'data-target') || attr(attrs, 'data-preset'));
    ['data-k','data-a','data-d','data-dir','data-target','data-preset','data-cat'].forEach(k => {
      const v = attr(attrs, k); if(v !== null) el._attrs[k] = v;
    });
    if(tag === 'canvas'){
      el._w = +(attr(attrs, 'width') || 700);
      el._h = +(attr(attrs, 'height') || 300);
      el._initial = null;
      Object.defineProperty(el, 'width', {
        get(){ return el._w; },
        set(v){
          el._w = v;
          if(el._initial === null) el._initial = v;
          else if(v !== el._initial) report('canvas backing store changed after setup',
                                            `#${el._id}: ${el._initial} -> ${v}`);
        }
      });
      Object.defineProperty(el, 'height', { get(){ return el._h; }, set(v){ el._h = v; } });
      const ctx = new Proxy({}, {
        get(t, k){
          if(k === 'canvas') return el;
          if(typeof k !== 'string') return undefined;
          if(['fillStyle','strokeStyle','lineWidth','font','textAlign','textBaseline',
              'globalAlpha','lineCap','lineJoin'].includes(k)) return t[k];
          return function(...args){
            if(NUMERIC_CANVAS_METHODS.has(k)){
              for(const a of args){
                if(typeof a === 'number' && !Number.isFinite(a)){
                  report('non-finite value reaching the canvas', `${k}(${args.join(', ')})`);
                  break;
                }
              }
            }
            return k === 'measureText' ? { width: 10 } : undefined;
          };
        },
        set(t, k, v){ t[k] = v; return true; }
      });
      el.getContext = () => ctx;
    }
    allElements.push(el);
    return el;
  }

  const registry = new Map();
  for(const [id, info] of ids){
    const el = makeEl(info.tag, info.attrs, id);
    if(selectValue.has(id)) el.value = selectValue.get(id);
    registry.set(id, el);
  }
  // elements carrying only a class are still reachable by querySelector, so
  // build them too rather than letting a lookup return null and look like a bug
  const clsRe = /<(\w+)([^>]*\bclass="[^"]+"[^>]*)>/g;
  let cm;
  while((cm = clsRe.exec(html))){
    if(/\bid="/.test(cm[2])) continue;
    makeEl(cm[1].toLowerCase(), cm[2], null);
  }
  // scripts that build their own controls look them up again afterwards, so an
  // element becomes findable the moment it is given an id
  for(const el of allElements) registerById(el);
  function registerById(el){
    let v = el._id;
    Object.defineProperty(el, 'id', {
      get(){ return v || ''; },
      set(x){ v = x; el._id = x; registry.set(x, el); },
      configurable: true
    });
    const setAttr = el.setAttribute.bind(el);
    el.setAttribute = (k, val) => { setAttr(k, val); if(k === 'id'){ v = String(val); el._id = v; registry.set(v, el); } };
    // Several tools build their controls by assigning an HTML string and then
    // look the new ids up. Parse what was assigned so those lookups resolve.
    let markup = '';
    Object.defineProperty(el, 'innerHTML', {
      get(){ return markup; },
      set(x){
        markup = String(x);
        const re = /<(\w+)([^>]*\bid="([^"]+)"[^>]*)>/g;
        let mm;
        while((mm = re.exec(markup))){
          if(registry.has(mm[3])) continue;
          const child = makeEl(mm[1].toLowerCase(), mm[2], mm[3]);
          registerById(child);
          registry.set(mm[3], child);
          el.children.push(child);
        }
      },
      configurable: true
    });
  }

  const doc = {
    getElementById(id){
      if(registry.has(id)) return registry.get(id);
      report('getElementById returned null', `no element with id "${id}" in the markup`);
      return null;
    },
    createElement(tag){ const e = makeEl(tag, ''); registerById(e); return e; },
    querySelectorAll(sel){
      const cls = sel.replace(/^\./, '').split(/[ ,]/)[0];
      return allElements.filter(e => e._classes.has(cls));
    },
    querySelector(sel){ return this.querySelectorAll(sel)[0] || null; },
    addEventListener(){},
    createElementNS(){ return makeEl('div',''); },
    body: makeEl('body','')
  };
  const win = {
    devicePixelRatio: 2,
    matchMedia: () => ({ matches: false, addEventListener(){}, addListener(){} }),
    addEventListener(){},
    requestAnimationFrame(){ return 0; },
    cancelAnimationFrame(){},
    scrollTo(){},
    location: { hash: '', pathname: '/', search: '' },
    history: { pushState(){} },
    getComputedStyle: () => ({ getPropertyValue: () => '' })
  };
  return { doc, win, registry, allElements };
}

function run(file){
  const src = fs.readFileSync(file, 'utf8');
  let body = src.split(/^---\s*$/m).slice(2).join('---');
  // pull in the one Liquid include that carries an interactive
  if(/\{%\s*include interactive-regression\.html\s*%\}/.test(body)){
    const inc = path.join(path.dirname(file), '..', '_includes', 'interactive-regression.html');
    if(fs.existsSync(inc)) body += '\n' + fs.readFileSync(inc, 'utf8');
  }
  const scripts = [...body.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
  if(!scripts.length) return [];

  const findings = [];
  const seen = new Set();
  const report = (kind, detail) => {
    const key = kind + '|' + detail;
    if(seen.has(key)) return;           // one line per distinct problem
    seen.add(key);
    findings.push([kind, detail]);
  };

  const { doc, win, registry } = makeHarness(body, report);
  const sandbox = {
    document: doc, window: win, console: { log(){}, warn(){}, error(){} },
    Math, Number, String, Array, Object, JSON, Date, isFinite, isNaN,
    parseFloat, parseInt, Proxy, Set, Map, setTimeout(){}, clearTimeout(){},
    requestAnimationFrame(){ return 0; }
  };
  sandbox.globalThis = sandbox;
  const ctx = vm.createContext(sandbox);

  for(const js of scripts){
    try { vm.runInContext(js, ctx, { timeout: 5000 }); }
    catch(e){ report('threw on load', String(e.message).slice(0, 120)); return findings; }
  }

  // ---- exercise every control the script registered ----
  const fire = (el, type) => {
    for(const fn of (el._listeners[type] || [])){
      try { fn.call(el, { target: el, preventDefault(){}, stopPropagation(){} }); }
      catch(e){ report(`threw on ${type}`, `#${el._id || el.tagName}: ${String(e.message).slice(0, 100)}`); }
    }
  };
  for(const el of registry.values()){
    if(el._listeners.input){
      const lo = +(el.min !== null ? el.min : 0), hi = +(el.max !== null ? el.max : 100);
      for(let i = 0; i <= 12; i++){
        el.value = String(lo + (hi - lo) * i / 12);
        fire(el, 'input');
      }
      el.value = String(lo); fire(el, 'input');
      el.value = String(hi); fire(el, 'input');
    }
    if(el._listeners.change) fire(el, 'change');
  }
  // buttons, twice round so toggles get both states
  for(let pass = 0; pass < 2; pass++)
    for(const el of registry.values()) if(el._listeners.click) fire(el, 'click');
  // sliders again, now that presets have changed
  for(const el of registry.values()){
    if(!el._listeners.input) continue;
    const lo = +(el.min !== null ? el.min : 0), hi = +(el.max !== null ? el.max : 100);
    for(let i = 0; i <= 6; i++){ el.value = String(lo + (hi - lo) * i / 6); fire(el, 'input'); }
  }
  return findings;
}

function main(){
  const files = process.argv.length > 2
    ? process.argv.slice(2)
    : fs.readdirSync('_posts').filter(f => f.endsWith('.md')).map(f => path.join('_posts', f)).sort();
  let total = 0, withFindings = 0;
  for(const f of files){
    let findings;
    try { findings = run(f); }
    catch(e){ findings = [['harness error', String(e.message).slice(0, 120)]]; }
    if(findings.length){
      withFindings++;
      console.log('\n' + path.basename(f));
      for(const [k, d] of findings) console.log('   ' + k.padEnd(46) + ' ' + d);
      total += findings.length;
    }
  }
  console.log(`\n${files.length} files run, ${total} finding${total === 1 ? '' : 's'}` +
              (withFindings ? ` in ${withFindings} article${withFindings === 1 ? '' : 's'}` : ''));
  process.exit(total ? 1 : 0);
}
main();
