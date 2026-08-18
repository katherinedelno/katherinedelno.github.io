---
layout: post
title: "Checking the form before L'Hospital's rule"
date: 2026-07-30
description: "L'Hospital's rule applies only after the quotient has been shown to have an appropriate indeterminate form."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "5 min read"
math: true
kind: mechanics
sequence: 16
interactive: true
blurb: "L'Hospital's rule applies only after the quotient has been shown to have an appropriate indeterminate form"
image: "/assets/og/lhospitals-rule.png"
---

L'Hospital's rule has hypotheses. The most common mistake is to differentiate the numerator and denominator before checking whether those hypotheses are satisfied. For AP Calculus, the relevant indeterminate quotient forms are $$\tfrac00$$ and $$\tfrac{\infty}{\infty}$$, and the form must be established before the rule is used.

## What the rule says

Suppose $$f$$ and $$g$$ are differentiable near $$a$$, with $$g'(x)\neq0$$ there. If $$\tfrac{f(x)}{g(x)}$$ has the indeterminate form $$0/0$$ or $$\infty/\infty$$, and if $$\lim_{x\to a}\tfrac{f'(x)}{g'(x)}$$ exists, then

$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$

Two notation points matter. The expression $$0/0$$ is not the value of the limit, and it labels an indeterminate form. The expression $$\tfrac{f'}{g'}$$ is the ratio of two derivatives, and it is not the derivative of the quotient $$f/g$$.

## Check the form first

<div class="viz" markdown="0">
  <div class="viz-controls" id="lh-fns"></div>
  <canvas id="lh-cv" width="700" height="320"></canvas>
  <div class="viz-controls">
    <label for="lh-x">x, moving toward the target</label>
    <input type="range" id="lh-x" min="0" max="1200" step="1" value="900">
  </div>
  <div class="lh-read" id="lh-read"></div>
  <p class="viz-caption">Five limits. The panel checks the form before it does anything else, and says in words what the check found. The dashed horizontal line is the true limit where one exists. On the first three the two curves converge on that line together, which is the rule working. On the fourth the form is not indeterminate at all and the derivative ratio runs off to infinity while the function ratio walks calmly to 1. On the fifth the form is genuinely infinity over infinity, the hypotheses about differentiability hold, and the derivative ratio still has no limit, so the rule concludes nothing, even though the original limit exists and equals 1.</p>
  <style>
    .lh-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .lh-read .lh-lab{color:var(--muted);display:inline-block;min-width:12.5rem}
    .lh-read .lh-val{font-weight:700;display:inline-block;min-width:7.5rem}
    .lh-read .lh-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('lh-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=42,PADR=18,TOP=28,BOT=H-24;
  var sin=Math.sin, cos=Math.cos, exp=Math.exp;

  // x runs over 10^(lo .. hi). Sliding right always moves toward the target,
  // whichever direction that is: for x -> 0 the exponent decreases, for
  // x -> infinity it increases. Slider 1200 is the closest approach in both cases.
  var E=[
    { n:'sin x / x   as x → 0', lo:-3, hi:Math.log10(2), rev:false,
      f:sin, g:function(x){return x;}, df:cos, dg:function(){return 1;},
      fl:'→ 0', gl:'→ 0', form:'0/0', L:1,
      fn:'indeterminate, so the rule applies',
      ln:'and f′/g′ arrives at the same value',
      ylo:-0.7, yhi:1.35 },
    { n:'(1 − cos x) / x²   as x → 0', lo:-3, hi:Math.log10(3), rev:false,
      f:function(x){return 1-cos(x);}, g:function(x){return x*x;},
      df:sin, dg:function(x){return 2*x;},
      fl:'→ 0', gl:'→ 0', form:'0/0', L:0.5,
      fn:'indeterminate, so the rule applies, and again after the first pass',
      ln:'and f′/g′ arrives at the same value',
      ylo:-0.08, yhi:0.62 },
    { n:'x² / eˣ   as x → ∞', lo:0, hi:Math.log10(30), rev:true,
      f:function(x){return x*x;}, g:exp,
      df:function(x){return 2*x;}, dg:exp,
      fl:'→ ∞', gl:'→ ∞', form:'∞/∞', L:0,
      fn:'indeterminate, so the rule applies',
      ln:'and f′/g′ arrives at the same value',
      ylo:-0.1, yhi:0.9 },
    { n:'(x + 1) / (x² + 1)   as x → 0', lo:-3, hi:Math.log10(2), rev:false,
      f:function(x){return x+1;}, g:function(x){return x*x+1;},
      df:function(){return 1;}, dg:function(x){return 2*x;},
      fl:'→ 1', gl:'→ 1', form:'1/1', L:1,
      fn:'not an indeterminate form, so the rule does not apply',
      ln:'found by evaluating the quotient, not by the rule',
      ylo:-0.2, yhi:3.2 },
    { n:'(x + sin x) / x   as x → ∞', lo:0, hi:Math.log10(40), rev:true,
      f:function(x){return x+sin(x);}, g:function(x){return x;},
      df:function(x){return 1+cos(x);}, dg:function(){return 1;},
      fl:'→ ∞', gl:'→ ∞', form:'∞/∞', L:1,
      fn:'indeterminate, so the form condition holds',
      ln:'but lim f′/g′ does not exist, so the rule concludes nothing',
      ylo:-0.25, yhi:2.35 }
  ];
  var k=0;
  function G(){ return E[k]; }
  function xat(s){ var g=G();
    return Math.pow(10, g.rev ? g.lo+(g.hi-g.lo)*s : g.hi-(g.hi-g.lo)*s); }
  function px(x){ var g=G(); return PADL+(Math.log10(x)-g.lo)/(g.hi-g.lo)*(W-PADL-PADR); }
  function py(y){ var g=G(); return BOT-(y-g.ylo)/(g.yhi-g.ylo)*(BOT-TOP); }
  // Every quantity here ranges over decades — x runs on a log slider and f′/g′
  // can pass 500 — so significant figures rather than decimal places, or the
  // printed x is too coarse to check the printed ratio against.
  function fmt(v){ if(!isFinite(v)) return v>0?'+∞':'−∞';
    var a=Math.abs(v);
    if(a<1e-12) return (0).toFixed(4);
    if(a<1e-4||a>=1e5) return v.toExponential(4);
    return v.toPrecision(5); }

  var bar=$('lh-fns');
  E.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  function curve(h,style,width){
    var g=G(), i, first=true;
    c.strokeStyle=style; c.lineWidth=width; c.beginPath();
    for(i=0;i<=900;i++){
      var x=Math.pow(10, g.lo+(g.hi-g.lo)*i/900), y=h(x);
      if(!isFinite(y) || y<g.ylo-8 || y>g.yhi+8){ first=true; continue; }
      if(first){ c.moveTo(px(x),py(y)); first=false; } else c.lineTo(px(x),py(y));
    }
    c.stroke();
  }

  function draw(){
    var g=G(), s=(+$('lh-x').value)/1200, x=xat(s);
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(PADL-1,TOP-10,W-PADL-PADR+2,BOT-TOP+16); c.clip();

    // decade gridlines, since the axis is logarithmic
    c.strokeStyle=LINE; c.lineWidth=1;
    for(var d=Math.ceil(g.lo); d<=g.hi; d++){
      c.beginPath(); c.moveTo(px(Math.pow(10,d)),TOP); c.lineTo(px(Math.pow(10,d)),BOT); c.stroke();
    }
    if(g.ylo<0&&g.yhi>0){ c.strokeStyle=PALE;
      c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke(); }

    // the true limit
    c.strokeStyle=PALE; c.lineWidth=1.4; c.setLineDash([6,4]);
    c.beginPath(); c.moveTo(PADL,py(g.L)); c.lineTo(W-PADR,py(g.L)); c.stroke();
    c.setLineDash([]);

    curve(function(x){ return g.df(x)/g.dg(x); }, FAINT, 2);
    curve(function(x){ return g.f(x)/g.g(x);   }, INK,   2);

    var q=g.f(x)/g.g(x), r=g.df(x)/g.dg(x);
    c.strokeStyle=LINE; c.lineWidth=1;
    c.beginPath(); c.moveTo(px(x),TOP); c.lineTo(px(x),BOT); c.stroke();
    if(isFinite(q)){ c.fillStyle=INK;   c.beginPath(); c.arc(px(x),py(q),4.5,0,6.284); c.fill(); }
    if(isFinite(r)&&r<g.yhi+8&&r>g.ylo-8){
      c.fillStyle=FAINT; c.beginPath(); c.arc(px(x),py(r),4.5,0,6.284); c.fill(); }
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText('f / g  and  f′ / g′        the target is at the '+
      (g.rev?'right':'left')+' edge', PADL, TOP-12);

    function row(l,v,n){ return '<div><span class="lh-lab">'+l+'</span>'+
      '<span class="lh-val">'+v+'</span>'+(n?'<span class="lh-note">'+n+'</span>':'')+'</div>'; }
    $('lh-read').innerHTML =
      row('x', fmt(x), '') +
      row('f(x)', fmt(g.f(x)), g.fl) +
      row('g(x)', fmt(g.g(x)), g.gl) +
      row('f(x) / g(x)', fmt(q), '') +
      row('f&prime;(x) / g&prime;(x)', fmt(r), '') +
      row('form check', g.form, g.fn) +
      row('the limit is', fmt(g.L), g.ln);
  }
  $('lh-x').addEventListener('input',draw);
  draw();
})();
</script>

The visualization compares $$\tfrac{f}{g}$$ with $$\tfrac{f'}{g'}$$. For limits where the rule applies, the two expressions approach the same value. For example, $$\lim_{x\to0}\tfrac{\sin x}{x}$$ has form $$0/0$$, and L'Hospital's rule gives $$\lim_{x\to0}\tfrac{\cos x}{1} = 1$$.

For $$\lim_{x\to0}\tfrac{1-\cos x}{x^2}$$, the first application gives $$\lim_{x\to0}\tfrac{\sin x}{2x}$$. That new quotient is still $$0/0$$, so the form must be checked again before applying the rule a second time, and then $$\lim_{x\to0}\tfrac{\cos x}{2} = \tfrac12$$. Each application requires its own justification.

## When the rule does not apply

Consider $$\lim_{x\to0}\tfrac{x+1}{x^2+1}$$. Direct substitution gives $$\tfrac11=1$$, so the form is not indeterminate and there is no reason to use L'Hospital's rule. If you differentiate numerator and denominator anyway, you get $$\tfrac{1}{2x}$$, which does not approach 1. The rule did not fail, and its hypotheses were never satisfied.

There is another way the method can become unhelpful. Consider $$\lim_{x\to\infty} \tfrac{x+\sin x}{x}$$, where the original quotient has form $$\tfrac{\infty}{\infty}$$. Differentiating numerator and denominator gives $$1+\cos x$$, which has no limit, and L'Hospital's rule therefore gives no conclusion.

But the original limit still exists because $$\tfrac{x+\sin x}{x} = 1+\tfrac{\sin x}{x}$$ and $$\tfrac{\sin x}{x}\to0$$, so the original limit is 1. Failure of the derivative ratio to converge does not imply that the original limit fails. It only means this theorem does not determine it.

## What to write

A clean solution should establish the form before differentiating. For example, since $$\lim_{x\to0}(1-\cos x)=0$$ and $$\lim_{x\to0}x^2=0$$, the quotient has indeterminate form $$0/0$$, so L'Hospital's rule applies. Then differentiate, and if the new quotient is still indeterminate, state that before applying the rule again.

<div class="article-note" markdown="1">
Also check whether [ordinary algebra](/2026/07/30/indeterminate-forms.html) is simpler. Factoring, rationalizing, or [dividing by the dominant power](/2026/07/30/limits-at-infinity.html) often resolves $$0/0$$ and $$\infty/\infty$$ limits without L'Hospital's rule. The theorem is useful, but it should not replace reading the expression first.
</div>
