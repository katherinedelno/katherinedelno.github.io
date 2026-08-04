---
layout: post
title: "Where a function fails to be differentiable"
date: 2026-07-30
description: "The derivative is a limit, so it fails exactly where that limit fails. Four functions, four different failures, and the one-sided difference quotients showing which is which."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: foundations
sequence: 8
interactive: true
blurb: "Four ways for one limit to fail, and the number that tells them apart"
image: "/assets/og/where-differentiability-fails.png"
---

[The derivative at a point is a limit](/2026/07/30/derivative-as-a-limit.html). So it exists exactly when that limit exists, and it fails exactly when that limit fails — which means the ways a derivative can fail are the ways a limit can fail, inherited whole from Unit 1.

The two-sided limit of the difference quotient needs both one-sided quotients to exist and to agree. The framework states the consequence in one direction and denies it in the other: if a function is differentiable at a point then it is continuous there, and a continuous function may still fail to be differentiable at a point in its domain.

## Four ways to break it

Each function below is broken at $$x = 0$$ and unremarkable everywhere else. The two secants are drawn from the same anchor, one to the left and one to the right, and the panel reports what each one-sided quotient is doing as $$h$$ shrinks.

The framework's test is that pair of numbers, and nothing else. *Corner* and *cusp* are the conventional names for two of the outcomes, used in every textbook and review book; the buttons carry them because you will meet them, but the classification is settled by the quotients.

<div class="viz" markdown="0">
  <canvas id="nd-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <button type="button" class="res-filter nd-f is-active" data-k="0" style="font-size:.72rem">Corner</button>
    <button type="button" class="res-filter nd-f" data-k="1" style="font-size:.72rem">Cusp</button>
    <button type="button" class="res-filter nd-f" data-k="2" style="font-size:.72rem">Vertical tangent</button>
    <button type="button" class="res-filter nd-f" data-k="3" style="font-size:.72rem">Discontinuity</button>
    <label for="nd-h">h</label>
    <input type="range" id="nd-h" min="0" max="400" step="1" value="300">
  </div>
  <div class="nd-panel">
    <div class="nd-row"><span class="nd-k">from the left</span><span class="nd-v" id="nd-l"></span></div>
    <div class="nd-row"><span class="nd-k">from the right</span><span class="nd-v" id="nd-r"></span></div>
    <div class="nd-verdict" id="nd-v2"></div>
    <div class="nd-note" id="nd-n"></div>
  </div>
  <p class="viz-caption">Both secants share the anchor, so the two numbers are the one-sided difference quotients at the same h. Shrink h and watch them. A corner sends them to two different finite numbers. A cusp sends them to infinities of opposite sign. A vertical tangent sends them to the same infinity, which is still not a number. A discontinuity is the odd one out: the function itself has a gap, one quotient stays put while the other runs away, and no repair to the slope is possible because the failure is not about slope at all.</p>
  <style>
    .nd-panel{margin:.9rem 0 0;padding-top:.8rem;border-top:1px solid var(--line)}
    .nd-row{display:flex;align-items:baseline;gap:14px;line-height:1.9}
    .nd-k{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
      color:var(--muted);min-width:13ch}
    .nd-v{font-size:1.15rem;font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums}
    .nd-verdict{margin-top:.5rem;font-size:1.15rem;font-weight:700;letter-spacing:-.02em;color:var(--ink)}
    .nd-note{font-size:.9rem;color:var(--muted);margin-top:.2rem;line-height:1.55}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('nd-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var PADL=44,PADR=22,TOP=16,AXIS=H-30;
  var $=function(i){ return document.getElementById(i); };
  function cbrt(x){ return x<0 ? -Math.pow(-x,1/3) : Math.pow(x,1/3); }

  var FN=[
    { label:'Corner',           f:function(x){ return Math.abs(x); },
      cont:true,  ylo:-0.7, yhi:1.6,
      verdict:'The one-sided slopes are −1 and +1: both exist, and they disagree.',
      note:'Continuous at 0, and still not differentiable. A two-sided limit needs the sides to agree, and finite disagreement is enough to destroy it.' },
    { label:'Cusp',             f:function(x){ return Math.pow(Math.abs(x),2/3); },
      cont:true,  ylo:-0.7, yhi:1.6,
      verdict:'The one-sided slopes run to −∞ and +∞: opposite infinities.',
      note:'Continuous at 0. The curve comes to a point, and the two branches turn vertical in opposite directions.' },
    { label:'Vertical tangent', f:cbrt,
      cont:true,  ylo:-1.4, yhi:1.4,
      verdict:'Both one-sided slopes run to +∞: the same infinity, from both sides.',
      note:'Continuous at 0, and the sides do agree, in a manner of speaking. They agree on something that is not a number, so the limit still does not exist.' },
    { label:'Discontinuity',    f:function(x){ return x<0 ? x : x+1; },
      cont:false, ylo:-1.2, yhi:2.2,
      verdict:'One quotient sits at +1 while the other runs to +∞.',
      note:'The function is not continuous at 0, and that alone rules out a derivative. Differentiability implies continuity, so the failure of continuity settles it before any slope is computed.' }
  ];
  var k=0;
  function F(){ return FN[k]; }
  function Hval(){ return Math.pow(10, (+$('nd-h').value)/100 - 4); }
  var XLO=-1.3, XHI=1.3;
  function px(x){ return PADL+(x-XLO)/(XHI-XLO)*(W-PADL-PADR); }
  function py(y){ var g=F(); return AXIS-(y-g.ylo)/(g.yhi-g.ylo)*(AXIS-TOP); }

  function fmt(v){
    if(!isFinite(v)) return '—';
    if(Math.abs(v)>=1e5) return (v>0?'+':'−')+Math.abs(v).toExponential(2);
    return (v>=0?'+':'−')+Math.abs(v).toFixed(Math.abs(v)>=100?1:4);
  }

  function draw(){
    var g=F(), h=Hval(), f0=g.f(0);
    var qr=(g.f(h)-f0)/h, ql=(g.f(-h)-f0)/(-h);
    c.clearRect(0,0,W,H);
    c.strokeStyle=LINE; c.lineWidth=1;
    c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke();
    c.beginPath(); c.moveTo(px(0),TOP); c.lineTo(px(0),AXIS); c.stroke();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    c.fillText('−1',px(-1),AXIS+13); c.fillText('1',px(1),AXIS+13);
    // the two secants
    [[ -h, ql ],[ h, qr ]].forEach(function(p){
      if(!isFinite(p[1])) return;
      c.strokeStyle=PALE; c.lineWidth=1.6;
      c.beginPath();
      c.moveTo(px(XLO), py(f0+p[1]*(XLO-0)));
      c.lineTo(px(XHI), py(f0+p[1]*(XHI-0)));
      c.stroke();
    });
    // the curve, split at 0 so a jump is not bridged
    c.strokeStyle=INK; c.lineWidth=2;
    [[XLO,0],[0,XHI]].forEach(function(seg){
      c.beginPath(); var on=false;
      for(var i=0;i<=600;i++){
        var x=seg[0]+(seg[1]-seg[0])*i/600;
        if(seg[1]===0 && x>=-1e-9) continue;
        if(seg[0]===0 && x<=1e-9) continue;
        var y=g.f(x);
        if(y<g.ylo-1||y>g.yhi+1){ on=false; continue; }
        on?c.lineTo(px(x),py(y)):(c.moveTo(px(x),py(y)),on=true);
      }
      c.stroke();
    });
    // the anchor, and the two moving points
    if(k===3){
      c.strokeStyle=INK; c.lineWidth=2; c.fillStyle='#fff';
      c.beginPath(); c.arc(px(0),py(0),4.2,0,7); c.fill(); c.stroke();
    }
    c.fillStyle=INK; c.beginPath(); c.arc(px(0),py(f0),4.6,0,7); c.fill();
    [-h,h].forEach(function(t){
      var y=g.f(t);
      if(y<g.ylo-1||y>g.yhi+1) return;
      c.fillStyle='#fff'; c.strokeStyle=MUTED; c.lineWidth=2;
      c.beginPath(); c.arc(px(t),py(y),4,0,7); c.fill(); c.stroke();
    });
    c.fillStyle=FAINT; c.font='700 10px '+FONT; c.textAlign='right';
    c.fillText('h = '+h.toExponential(1), W-PADR, TOP+10);

    $('nd-l').textContent=fmt(ql);
    $('nd-r').textContent=fmt(qr);
    $('nd-v2').textContent=g.verdict;
    $('nd-n').textContent=g.note;
  }
  Array.prototype.forEach.call(document.querySelectorAll('.nd-f'),function(b){
    b.addEventListener('click',function(){
      k=+b.getAttribute('data-k');
      Array.prototype.forEach.call(document.querySelectorAll('.nd-f'),function(o){
        o.classList[o===b?'add':'remove']('is-active'); });
      draw();
    });
  });
  $('nd-h').addEventListener('input',draw);
  draw();
})();
</script>

The corner is $$\vert x\vert$$. Its one-sided quotients are $$-1$$ and $$+1$$ at every $$h$$, never converging on each other because there is nothing to converge — they were already constant. Two finite slopes that disagree is the cheapest way to have no derivative, and the graph shows it as a sharp turn.

The cusp is $$x^{2/3}$$. Push $$h$$ down and the quotients read $$\pm 2.15$$, then $$\pm 4.64$$, then $$\pm 10$$, then $$\pm 21.5$$, running to opposite infinities. The two branches both turn vertical, in opposite directions, and the curve is pinched to a point.

The vertical tangent is $$x^{1/3}$$. Here the quotients read $$+4.64$$, $$+21.5$$, $$+100$$, $$+464$$ — the same value from both sides, both running to $$+\infty$$. The sides agree, and the derivative still does not exist, because they agree on something that is not a number. The tangent line is genuinely there; it is just vertical, and vertical lines have no slope.

## Differentiable implies continuous

The fourth button is different in kind. The first three functions are all continuous at 0 — they fail on the slope alone. This one fails earlier: the function has [a gap](/2026/07/30/continuity-three-conditions.html), and no discussion of slopes is required.

That is the one-way implication the course states outright: if $$f$$ is differentiable at a point, then it is continuous at that point. The contrapositive is the usable form — *not continuous, therefore not differentiable* — and you can stop there. The framework adds a corollary worth having: if a point is not in the domain of $$f$$, it is not in the domain of $$f'$$ either.

The converse is false, and the framework says so in as many words: a continuous function may fail to be differentiable at a point in its domain. The first three buttons are that sentence made concrete — all continuous at 0, none with a derivative there. Two of them are the framework's own illustrative examples: $$\vert x\vert$$, where the one-sided difference quotients are unequal, and $$x^{1/3}$$, where the tangent line is vertical and has no slope. So "continuous" buys you nothing about differentiability, while "differentiable" buys you continuity for free.

Which makes the two claims worth keeping in the right order:

- Differentiable at $$c$$ $$\Rightarrow$$ continuous at $$c$$. Always.
- Continuous at $$c$$ $$\Rightarrow$$ differentiable at $$c$$. Not in general — the first three buttons are the counterexamples.

## Testing a piecewise join

Graphs are read by eye, but a piecewise function given algebraically has to be tested, and the test is two steps in a fixed order.

First check continuity at the join: the two expressions must agree there, and both must agree with the function's value. Second, and only if the first passes, check that the two one-sided derivatives agree there.

Both steps are needed, and a student who does only the second can be caught out. Take

$$f(x) = \begin{cases} x^2 & x \le 1 \\ 2x - 5 & x > 1 \end{cases}$$

The one-sided derivatives at $$x = 1$$ are $$2x$$ evaluated at 1, which is 2, and 2, which match perfectly. But the function values are $$1$$ and $$-3$$, so $$f$$ is not even continuous at 1, and there is no derivative regardless of how well the slopes agree. Matching slopes across a gap means nothing.

<div class="article-note" markdown="1">
A self-test at the slider: the vertical tangent and the cusp both send their quotients to infinity, so what distinguishes them, in one sentence, is the *sign*. Now predict what $$-x^{2/3}$$ would look like and which pair of infinities it would produce. Then say which of the four cases $$\sqrt{\vert x\vert}$$ belongs to. The classification is entirely a question about the two one-sided quotients, which is why the panel prints them separately and prints nothing else.
</div>
