---
layout: post
title: "Where a function fails to be differentiable"
date: 2026-07-30
description: "Corners, cusps, vertical tangents, and discontinuities can all prevent a two-sided derivative from existing."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "6 min read"
math: true
kind: foundations
sequence: 8
interactive: true
blurb: "Corners, cusps, vertical tangents, and discontinuities can all prevent a two-sided derivative from existing"
image: "/assets/og/where-differentiability-fails.png"
---

[The derivative at a point is a limit](/2026/07/30/derivative-as-a-limit.html), so a derivative fails to exist when the corresponding limit of difference quotients fails to exist as a finite two-sided limit. That gives several familiar cases. A function may have a corner, a cusp, a vertical tangent, or a discontinuity, and the graphs look different, but the underlying question is the same. What do the one-sided difference quotients do?

## Four ways differentiability can fail

Each function in the visualization has a problem at $$x=0$$.

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

The two reported values are one-sided difference quotients at the same distance from the point. Shrink $$h$$ and compare them.

## Corner

For $$f(x)=\vert x\vert$$, the left-hand difference quotient is $$-1$$ and the right-hand difference quotient is $$1$$. Both are finite, and they simply disagree, so the two-sided derivative does not exist. Graphically, this produces a sharp corner.

## Cusp

For $$f(x)=x^{2/3}$$, the one-sided difference quotients grow without bound with opposite signs. One side tends toward $$-\infty$$ and the other toward $$+\infty$$. The curve narrows into a cusp, and there is no finite derivative.

## Vertical tangent

For $$f(x)=x^{1/3}$$, the one-sided difference quotients both tend toward $$+\infty$$. The two sides agree in direction, but they do not approach a finite number. The graph has a vertical tangent line, and a vertical line has undefined slope, so the ordinary derivative does not exist there.

## Discontinuity

The last case fails even earlier. If the function is [not continuous at the point](/2026/07/30/continuity-three-conditions.html), it cannot be differentiable there, and there is no need to continue to the difference quotient once continuity has already failed.

## Differentiability implies continuity

If a function is differentiable at $$x=c$$, then it is continuous at $$x=c$$. The contrapositive is often the useful version: if a function is not continuous at $$c$$, then it is not differentiable at $$c$$.

The converse is false. A function may be continuous but not differentiable, and the corner, cusp, and vertical-tangent examples are all continuous at the point where the derivative fails. So the relationship is

$$\text{differentiable at }c \Longrightarrow \text{continuous at }c$$

but in general $$\text{continuous at }c \not\Longrightarrow \text{differentiable at }c$$. It is also useful to remember that if $$c$$ is not in the domain of $$f$$, then $$c$$ cannot be in the domain of $$f'$$.

## Testing a piecewise join

For a piecewise function, check continuity before checking derivatives. Consider

$$f(x) = \begin{cases} x^2, & x\le1,\\ 2x-5, & x>1 \end{cases}$$

The derivative of the first expression at $$x=1$$ is 2, and the derivative of the second expression is also 2, so the one-sided slopes match. But the function values do not. From the left, $$f(1)=1$$, and from the right, the expression approaches $$2(1)-5=-3$$. The function is not continuous at $$x=1$$, so it is not differentiable there, regardless of the matching derivative formulas.

The correct order is:

1. Check continuity at the join.
2. If continuity holds, compare the one-sided derivatives.

Matching slopes across a jump does not produce differentiability.

<div class="article-note" markdown="1">
A useful self-test is to compare the cusp and vertical tangent in the visualization. Both involve unbounded one-sided quotients, and the difference is the sign pattern. Then ask what happens for $$-x^{2/3}$$ and for $$\sqrt{\vert x\vert}$$. The classification comes from the behavior of the two one-sided difference quotients.
</div>
