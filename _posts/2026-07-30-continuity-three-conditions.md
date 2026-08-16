---
layout: post
title: "Breaking continuity one condition at a time"
date: 2026-07-30
description: "Continuity has three conditions. Each type of discontinuity records which part of the definition failed."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "7 min read"
math: true
kind: foundations
sequence: 4
interactive: true
blurb: "Continuity has three conditions. Each type of discontinuity records which part of the definition failed"
image: "/assets/og/continuity-three-conditions.png"
---

A function $$f$$ is continuous at $$x=c$$ when three conditions hold.

First, $$f(c)$$ exists.

Second,

$$\lim_{x\to c}f(x)$$

exists.

Third,

$$\lim_{x\to c}f(x)=f(c).$$

These conditions are separate. A function can satisfy some while failing another.

The named discontinuities in AP Calculus are easiest to understand by asking which part of this definition failed.

## Break the conditions one at a time

The visualization below changes what happens at $$x=2$$ while leaving the surrounding curve fixed.

<div class="viz" markdown="0">
  <canvas id="ct-cv" width="700" height="290"></canvas>
  <div class="viz-controls">
    <button type="button" class="res-filter ct-b is-active" data-k="0" style="font-size:.72rem">Continuous</button>
    <button type="button" class="res-filter ct-b" data-k="1" style="font-size:.72rem">No value</button>
    <button type="button" class="res-filter ct-b" data-k="2" style="font-size:.72rem">Wrong value</button>
    <button type="button" class="res-filter ct-b" data-k="3" style="font-size:.72rem">Sides disagree</button>
    <button type="button" class="res-filter ct-b" data-k="4" style="font-size:.72rem">Unbounded</button>
    <button type="button" class="res-filter" id="ct-fix" style="font-size:.72rem">Repair it</button>
  </div>
  <div class="ct-panel">
    <div class="ct-cond" id="ct-c1"></div>
    <div class="ct-cond" id="ct-c2"></div>
    <div class="ct-cond" id="ct-c3"></div>
    <div class="ct-verdict" id="ct-v"></div>
  </div>
  <p class="viz-caption">Each button leaves the curve alone and changes only what happens at x = 2. "No value" removes the point; "wrong value" puts it somewhere the neighborhood does not point to; "sides disagree" and "unbounded" break the limit itself, in the two ways a limit can fail here. The checklist is the definition read one clause at a time, and the verdict is the name that clause pattern earns. Repair works on exactly the two cases where the limit exists, which is the whole content of what "removable" means.</p>
  <style>
    .ct-panel{margin:.9rem 0 0;padding-top:.8rem;border-top:1px solid var(--line)}
    .ct-cond{font-size:.95rem;line-height:1.75;color:var(--ink);font-variant-numeric:tabular-nums}
    .ct-cond .ct-mk{display:inline-block;width:1.4em;font-weight:700}
    .ct-cond.no{color:var(--muted)}
    .ct-verdict{margin-top:.6rem;font-size:1.35rem;font-weight:700;letter-spacing:-.02em;color:var(--ink)}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('ct-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97';
  var FONT='Hanken Grotesk, sans-serif';
  var C=2, kind=0, repaired=false;
  var PADL=42,PADR=22,TOP=14,AXIS=H-32;
  var XLO=0.2,XHI=3.8,YLO=-0.6,YHI=6.4;
  function px(x){ return PADL+(x-XLO)/(XHI-XLO)*(W-PADL-PADR); }
  function py(y){ return AXIS-(y-YLO)/(YHI-YLO)*(AXIS-TOP); }

  // Each case leaves the curve alone away from x = 2 and changes only the point.
  //   value: f(2), or null when undefined
  //   limit: the two-sided limit, or null when it does not exist
  var CASES=[
    { label:'Continuous',     f:function(x){ return x+2; },            value:4,    limit:4    },
    { label:'No value',       f:function(x){ return x+2; },            value:null, limit:4    },
    { label:'Wrong value',    f:function(x){ return x+2; },            value:1,    limit:4    },
    { label:'Sides disagree', f:function(x){ return x<C?x+2:x-1; },    value:1,    limit:null },
    { label:'Unbounded',      f:function(x){ return 1/((x-C)*(x-C)); },value:null, limit:null }
  ];
  function cur(){
    var k=CASES[kind];
    return { f:k.f, value:(repaired&&k.limit!==null)?k.limit:k.value, limit:k.limit, label:k.label };
  }
  function oneSided(){
    var k=CASES[kind];
    return [k.f(C-1e-7), k.f(C+1e-7)];
  }
  function name(s){
    if(s.limit!==null && s.value!==null && s.value===s.limit) return 'Continuous at x = 2';
    if(s.limit!==null) return 'Removable discontinuity';
    if(kind===4) return 'Discontinuity due to a vertical asymptote';
    return 'Jump discontinuity';
  }

  function draw(){
    var s=cur();
    c.clearRect(0,0,W,H);
    c.strokeStyle=LINE; c.lineWidth=1;
    c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    for(var t=1;t<=3;t++) c.fillText(String(t),px(t),AXIS+14);
    c.textAlign='right';
    for(var v=2;v<=6;v+=2) c.fillText(String(v),PADL-6,py(v)+3);
    // vertical asymptote guide
    if(kind===4){
      c.strokeStyle=FAINT; c.setLineDash([4,3]);
      c.beginPath(); c.moveTo(px(C),TOP); c.lineTo(px(C),AXIS); c.stroke(); c.setLineDash([]);
    }
    // curve, each side drawn separately so nothing bridges x = 2
    c.strokeStyle=INK; c.lineWidth=2;
    [[XLO,C],[C,XHI]].forEach(function(seg){
      c.beginPath(); var on=false;
      for(var i=0;i<=700;i++){
        var x=seg[0]+(seg[1]-seg[0])*i/700;
        if(Math.abs(x-C)<2e-3) continue;
        var y=s.f(x);
        if(!isFinite(y)||y<YLO-1||y>YHI+1){ on=false; continue; }
        on?c.lineTo(px(x),py(y)):(c.moveTo(px(x),py(y)),on=true);
      }
      c.stroke();
    });
    // open circles where the curve approaches but does not include
    function open(y){
      c.strokeStyle=INK; c.lineWidth=2; c.fillStyle='#fff';
      c.beginPath(); c.arc(px(C),py(y),4.3,0,7); c.fill(); c.stroke();
    }
    function dot(y){ c.fillStyle=INK; c.beginPath(); c.arc(px(C),py(y),4.3,0,7); c.fill(); }
    if(kind<=2){ if(s.value!==4) open(4); if(s.value!==null) dot(s.value); }
    else if(kind===3){ open(4); if(s.value!==null) dot(s.value); }
    render(s);
  }

  function render(s){
    var os=oneSided();
    function row(el,ok,txt){
      var e=document.getElementById(el);
      e.className='ct-cond'+(ok?'':' no');
      e.innerHTML='<span class="ct-mk">'+(ok?'&#10003;':'&#10007;')+'</span>'+txt;
    }
    row('ct-c1', s.value!==null,
      s.value!==null ? 'f(2) exists, and equals '+s.value
                     : 'f(2) does not exist');
    var lim2 = s.limit!==null;
    var lt = kind===4 ? 'unbounded' : os[0].toFixed(2);
    var rt = kind===4 ? 'unbounded' : os[1].toFixed(2);
    row('ct-c2', lim2,
      lim2 ? 'the limit exists, and equals '+s.limit
           : 'the limit does not exist. From the left, ' + lt + '; from the right, ' + rt);
    var third = lim2 && s.value!==null && s.value===s.limit;
    row('ct-c3', third,
      third ? 'the limit equals f(2)'
            : (lim2 && s.value!==null) ? 'the limit is '+s.limit+', but f(2) is '+s.value
            : 'nothing to compare, since one of the first two failed');
    document.getElementById('ct-v').textContent=name(s);
    var fix=document.getElementById('ct-fix');
    var fixable = s.limit!==null && !(s.value!==null && s.value===s.limit);
    fix.disabled=!fixable && !repaired;
    fix.style.opacity=(fixable||repaired)?'1':'.4';
    fix.textContent=repaired?'Undo the repair':'Repair it';
  }

  Array.prototype.forEach.call(document.querySelectorAll('.ct-b'),function(b){
    b.addEventListener('click',function(){
      kind=+b.getAttribute('data-k'); repaired=false;
      Array.prototype.forEach.call(document.querySelectorAll('.ct-b'),function(o){
        o.classList[o===b?'add':'remove']('is-active'); });
      draw();
    });
  });
  document.getElementById('ct-fix').addEventListener('click',function(){
    if(CASES[kind].limit===null) return;
    repaired=!repaired; draw();
  });
  draw();
})();
</script>

The checklist reports the three conditions separately.

Start with the continuous case. The function value exists, the limit exists, and the two are equal.

Now choose “No value.”

[The nearby graph has not changed](/2026/07/30/what-a-limit-claims.html), so the limit is still 4. But $$f(2)$$ is undefined.

The first condition fails.

Choose “Wrong value.”

Now $$f(2)=1$$, while the nearby values still approach 4.

The function value exists and the limit exists. They simply are not equal.

The third condition fails.

Both of these are removable discontinuities.

The reason they are removable is that the limit exists. If we define or redefine the function value to equal that limit, continuity is restored.

The repair button does exactly that.

## When the limit fails

The last two cases break the second condition.

Choose “Sides disagree.”

The left-hand limit is 4 and the right-hand limit is 1.

Both one-sided limits exist, but they are unequal. Therefore the two-sided limit does not exist.

This is a jump discontinuity.

No single value assigned to $$f(2)$$ can repair it because there is no one limit value for $$f(2)$$ to match.

Now choose “Unbounded.”

The example uses

$$\frac{1}{(x-2)^2},$$

which grows without bound from both sides of $$x=2$$.

The finite two-sided limit does not exist, and the graph has a vertical asymptote.

Again, assigning a value at $$x=2$$ cannot repair the discontinuity.

The three named categories in the course are therefore:

- removable discontinuities
- jump discontinuities
- discontinuities associated with vertical asymptotes

They do not need to be memorized as unrelated cases. Each follows from the three-part definition of continuity.

## Continuity on an interval

A function is continuous on an interval if it is continuous at every point of that interval.

For the standard families, you are allowed to use a useful shortcut.

Polynomials, rational functions, power functions, exponentials, logarithms, and trigonometric functions are continuous throughout their domains.

The phrase “throughout their domains” matters.

A rational function such as

$$\frac{1}{x-2}$$

is continuous everywhere it is defined. The point $$x=2$$ is not in its domain.

So it is incorrect to say that every rational function is continuous everywhere. It is equally incorrect to say that the presence of one discontinuity means the function is not continuous anywhere else.

## Piecewise functions

Piecewise functions make the three conditions especially visible.

Suppose two formulas meet at $$x=c$$.

For the function to be continuous there, the left-hand expression must approach the same value as the right-hand expression, and the actual function value at $$c$$ must equal that common limit.

If a parameter appears in one of the pieces, the usual strategy is to evaluate the relevant expressions at the boundary, set the required values equal, and solve for the parameter.

This is not a separate continuity rule. It is the same definition written in a form that matches a piecewise function.

<div class="article-note" markdown="1">
A useful self-test is to use the buttons and predict which cases allow the repair button to activate.

The correct rule is not simply that “removable discontinuities can be repaired.” The deeper reason is that repair is possible exactly when the limit already exists.
</div>
