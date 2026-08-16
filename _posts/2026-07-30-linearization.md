---
layout: post
title: "Over or under: reading a linearization"
date: 2026-07-30
description: "A linearization uses the tangent line to approximate a nearby function value. Concavity determines whether the estimate is high or low."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "9 min read"
math: true
kind: foundations
sequence: 15
interactive: true
blurb: "A linearization uses the tangent line to approximate a nearby function value. Concavity determines whether the estimate is high or low"
image: "/assets/og/linearization.png"
---

Near a point of tangency, a differentiable function and its tangent line can be very close.

Linearization uses that local agreement to approximate nearby function values.

The formula is simple. The more interesting question is whether the approximation is above or below the true value.

## The linearization

For a function $$f$$ differentiable at $$a$$, the linearization at $$a$$ is

$$ L(x) = f(a)+f'(a)(x-a). $$

This is [the tangent line](/2026/07/30/derivative-as-a-limit.html) written as a function.

Suppose we want to approximate

$$ \sqrt{4.1}. $$

Take

$$ f(x)=\sqrt{x} $$

and choose $$a=4$$, where both the function and derivative are easy to evaluate.

Since

$$ f(4)=2 $$

and

$$ f'(4)=\frac14, $$

the linearization is

$$ L(x) = 2+\frac14(x-4). $$

Then

$$ L(4.1) = 2.025. $$

The true value is approximately

$$ 2.02484567. $$

The tangent-line estimate is slightly high.

## Concavity determines the direction

A tangent line to a concave-up function lies below the curve locally.

A tangent line to a concave-down function lies above it locally.

So [the sign of the second derivative](/2026/07/21/reading-the-graph-of-f-prime.html) can tell us whether a linear approximation is an underestimate or overestimate.

But the concavity must hold across the interval between the point of tangency $$a$$ and the point being estimated.

Checking $$f''(a)$$ alone is not always enough.

<div class="viz" markdown="0">
  <div class="viz-controls" id="lz-fns"></div>
  <canvas id="lz-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <label for="lz-x">x</label>
    <input type="range" id="lz-x" min="0" max="1200" step="1" value="410">
  </div>
  <div class="lz-read" id="lz-read"></div>
  <p class="viz-caption">The point of tangency is fixed and marked; the slider moves the point being estimated. The vertical bar between the curve and the line is the error, drawn to scale, so the way it opens up as x leaves a is the honest picture of what the approximation costs. The last row of the panel is the one that matters: it samples the second derivative strictly between a and x and reports whether the sign holds all the way across. When it does, the concavity settles the question. When it does not, the panel says so rather than guessing.</p>
  <style>
    .lz-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .lz-read .lz-lab{color:var(--muted);display:inline-block;min-width:14rem}
    .lz-read .lz-val{font-weight:700;display:inline-block;min-width:7rem}
    .lz-read .lz-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('lz-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=40,PADR=18,TOP=16,BOT=H-26;

  // Ranges are set so every x the article names lands on an integer slider step:
  // 4.05/4.1/4.2/9 at 405/410/420/900, 0.1 at 744, +-0.5 at 700/500, 0/2/3 at 480/960/1200.
  var F=[
    { n:'√x   at a = 4', a:4, lo:0, hi:12, ylo:-0.3, yhi:4.3,
      f:Math.sqrt,
      d:function(x){ return 0.5/Math.sqrt(x); },
      dd:function(x){ return -0.25/Math.pow(x,1.5); } },
    { n:'eˣ   at a = 0', a:0, lo:-3, hi:2, ylo:-1.2, yhi:7.8,
      f:Math.exp, d:Math.exp, dd:Math.exp },
    { n:'sin x   at a = 0', a:0, lo:-3, hi:3, ylo:-3.2, yhi:3.2,
      f:Math.sin,
      d:Math.cos,
      dd:function(x){ return -Math.sin(x); } },
    { n:'x³   at a = −1', a:-1, lo:-2, hi:3, ylo:-9, yhi:28,
      f:function(x){ return x*x*x; },
      d:function(x){ return 3*x*x; },
      dd:function(x){ return 6*x; } }
  ];
  var k=0;
  function G(){ return F[k]; }
  function px(x){ var g=G(); return PADL+(x-g.lo)/(g.hi-g.lo)*(W-PADL-PADR); }
  function py(y){ var g=G(); return BOT-(y-g.ylo)/(g.yhi-g.ylo)*(BOT-TOP); }
  function fmt(v){ var x=Math.abs(v);
    if(x<1e-12) return (0).toFixed(4);
    if(x<1e-4||x>=1e5) return v.toExponential(3);
    return v.toFixed(4); }
  // The error spans several orders of magnitude on one curve, and the article
  // makes a claim about how its ratio behaves, so it gets significant figures
  // rather than a fixed number of decimal places.
  function fmtErr(v){ return Math.abs(v)<1e-12 ? (0).toFixed(4) : v.toPrecision(5); }

  var bar=$('lz-fns');
  F.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  // Sample f'' strictly between a and x. Returns 'up', 'down', 'mixed', or 'none'
  // when a and x coincide. Endpoints excluded on purpose: a itself may be an
  // inflection point, and that is not what decides the comparison.
  function concavity(g,a,x){
    if(Math.abs(x-a)<1e-12) return 'none';
    var lo=Math.min(a,x), hi=Math.max(a,x), pos=false, neg=false, N=400;
    for(var i=1;i<N;i++){
      var v=g.dd(lo+(hi-lo)*i/N);
      if(v>1e-12) pos=true; else if(v<-1e-12) neg=true;
    }
    if(pos&&neg) return 'mixed';
    if(pos) return 'up';
    if(neg) return 'down';
    return 'flat';
  }

  function draw(){
    var g=G(), x=g.lo+(+$('lz-x').value)/1200*(g.hi-g.lo);
    var a=g.a, fa=g.f(a), ma=g.d(a);
    function L(t){ return fa+ma*(t-a); }
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(PADL-1,TOP-6,W-PADL-PADR+2,BOT-TOP+12); c.clip();

    c.strokeStyle=LINE; c.lineWidth=1;
    var i,t;
    for(i=Math.ceil(g.lo);i<=g.hi;i++){ c.beginPath(); c.moveTo(px(i),TOP); c.lineTo(px(i),BOT); c.stroke(); }
    if(g.ylo<0&&g.yhi>0){ c.strokeStyle=PALE; c.lineWidth=1.2;
      c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke(); }

    // the tangent line, then the curve on top of it
    c.strokeStyle=FAINT; c.lineWidth=1.6; c.setLineDash([6,4]);
    c.beginPath(); c.moveTo(px(g.lo),py(L(g.lo))); c.lineTo(px(g.hi),py(L(g.hi))); c.stroke();
    c.setLineDash([]);
    c.strokeStyle=INK; c.lineWidth=2; c.beginPath();
    for(i=0;i<=800;i++){ t=g.lo+(g.hi-g.lo)*i/800;
      if(i===0) c.moveTo(px(t),py(g.f(t))); else c.lineTo(px(t),py(g.f(t))); }
    c.stroke();

    // the error, drawn to scale
    c.strokeStyle=INK; c.lineWidth=3;
    c.beginPath(); c.moveTo(px(x),py(g.f(x))); c.lineTo(px(x),py(L(x))); c.stroke();
    c.fillStyle=INK; c.beginPath(); c.arc(px(a),py(fa),5,0,6.284); c.fill();
    c.fillStyle=FAINT; c.beginPath(); c.arc(px(x),py(L(x)),4,0,6.284); c.fill();
    c.fillStyle=INK;  c.beginPath(); c.arc(px(x),py(g.f(x)),4,0,6.284); c.fill();
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    c.fillText('a',px(a),BOT+14); c.fillText('x',px(x),BOT+14);

    var Lx=L(x), fx=g.f(x), err=Lx-fx, cc=concavity(g,a,x);
    var verdict = Math.abs(err)<1e-12 ? 'the line meets the curve here'
                : (err>0 ? 'overestimate' : 'underestimate');
    var ccnote = {
      up:   'positive throughout. Concave up, so the line lies below',
      down: 'negative throughout. Concave down, so the line lies above',
      mixed:'changes sign. Concavity alone settles nothing here',
      flat: 'zero throughout. The function is its own tangent line',
      none: 'no interval yet'
    }[cc];
    function row(l,v,n){ return '<div><span class="lz-lab">'+l+'</span>'+
      '<span class="lz-val">'+v+'</span>'+(n?'<span class="lz-note">'+n+'</span>':'')+'</div>'; }
    $('lz-read').innerHTML =
      row('a, the point of tangency', fmt(a), '') +
      row('x', fmt(x), '') +
      row('L(x) = f(a) + f&prime;(a)(x &minus; a)', fmt(Lx), '') +
      row('f(x)', fmt(fx), '') +
      row('L(x) &minus; f(x)', fmtErr(err), verdict) +
      row('f&Prime; strictly between a and x', '', ccnote);
  }
  $('lz-x').addEventListener('input',draw);
  draw();
})();
</script>

The visualization fixes the point of tangency and moves the point being approximated.

For

$$ f(x)=\sqrt{x}, $$

the function is concave down throughout its domain. Its tangent line therefore lies above the curve, so the linearization is an overestimate.

For

$$ f(x)=e^x, $$

the function is concave up everywhere. The tangent line lies below the curve, so the estimate is low.

Sine is more subtle.

At $$a=0$$,

$$ f''(0)=0. $$

That value alone does not determine the direction.

To the right of the origin, sine is concave down for a while, so the tangent line is above the curve.

To the left, it is concave up, so the same tangent line is below.

The interval matters.

## When the guarantee changes

Consider

$$ f(x)=x^3 $$

at $$a=-1$$.

Then

$$ f(-1)=-1 $$

and

$$ f'(-1)=3, $$

so

$$ L(x)=3x+2. $$

At the point of tangency,

$$ f''(-1)=-6, $$

so the function is concave down there.

Near $$a=-1$$, the tangent line lies above the curve.

But

$$ L(x)-f(x) = 3x+2-x^3 = -(x-2)(x+1)^2. $$

At $$x=2$$, the sign changes.

Beyond that point, the same tangent line lies below the function.

The concavity also changes at the inflection point $$x=0$$.

So a justification about overestimation or underestimation should refer to the concavity on the interval between $$a$$ and the target value, not only at $$a$$.

## Approximation error

The farther $$x$$ moves from $$a$$, the less reliable a linear approximation usually becomes.

For $$\sqrt{x}$$ linearized at $$a=4$$, the error is very small near 4 and grows as the target moves away.

The leading error behaves quadratically in the distance from the point of tangency.

[The next Taylor term](/2026/07/22/taylor-polynomials-impersonate-functions.html) is

$$ \frac12f''(a)(x-a)^2. $$

That helps explain why doubling the distance from $$a$$ roughly multiplies the linearization error by four when higher-order effects remain small.

Linearization is therefore local in a meaningful sense.

A tangent line can remain on the correct side of a curve far from the point of tangency and still be a poor numerical approximation.

<div class="article-note" markdown="1">
Two habits are useful.

Choose $$a$$ near the target where $$f(a)$$ and $$f'(a)$$ are easy to compute.

Then inspect the concavity across the interval before deciding whether the estimate is high or low.
</div>
