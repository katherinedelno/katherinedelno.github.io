---
layout: post
title: "Derivatives of inverse functions"
date: 2026-07-30
description: "Corresponding tangent slopes of a function and its inverse are reciprocals, with the derivative evaluated at the corresponding input."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: mechanics
sequence: 12
interactive: true
blurb: "Corresponding tangent slopes of a function and its inverse are reciprocals, with the derivative evaluated at the corresponding input"
image: "/assets/og/derivatives-of-inverse-functions.png"
---

The graph of $$f^{-1}$$ is the graph of $$f$$ reflected across the line $$y=x$$.

Reflection across $$y=x$$ swaps horizontal and vertical change. At corresponding points, tangent slopes are therefore reciprocals.

That geometric picture leads directly to the derivative formula.

## The rule and the evaluation point

Suppose $$f$$ is one-to-one and differentiable, and suppose

$$f'\big(f^{-1}(a)\big)\neq0.$$

Then

$$\big(f^{-1}\big)'(a) = \frac{1}{f'\big(f^{-1}(a)\big)}.$$

The formula follows from the identity

$$f\big(f^{-1}(x)\big)=x.$$

[Differentiate both sides](/2026/07/30/chain-rule-reading-the-layers.html):

$$f'\big(f^{-1}(x)\big) \cdot \big(f^{-1}\big)'(x) = 1.$$

Then solve for the inverse derivative.

The main difficulty is usually not the reciprocal. It is finding where $$f'$$ should be evaluated.

Suppose

$$f(x)=x^3+x.$$

Since

$$f(1)=2,$$

we know

$$f^{-1}(2)=1.$$

Therefore

$$\big(f^{-1}\big)'(2) = \frac{1}{f'(1)} = \frac{1}{3(1)^2+1} = \frac14.$$

We never needed a formula for $$f^{-1}$$.

## Matching corresponding points

<div class="viz" markdown="0">
  <div class="viz-controls" id="iv-fns"></div>
  <canvas id="iv-cv" width="700" height="380"></canvas>
  <div class="viz-controls">
    <label for="iv-b">b, the point on f</label>
    <input type="range" id="iv-b" min="0" max="1200" step="1" value="900">
  </div>
  <div class="iv-read" id="iv-read"></div>
  <p class="viz-caption">The dark curve is f and the pale one is its reflection across the dashed diagonal, drawn by swapping coordinates rather than by inverting anything. A point sits at (b, f(b)) and its mirror at (f(b), b); the two short lines are the tangents there. The panel gives f'(b), its reciprocal, and their product, which is 1 wherever both exist. Where an inverse derivative has a formula worth memorizing, the last row evaluates that formula independently and reports the gap. For x³ + x there is no formula to compare against, which is the case the rule was built for.</p>
  <style>
    .iv-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .iv-read .iv-lab{color:var(--muted);display:inline-block;min-width:15rem}
    .iv-read .iv-val{font-weight:700}
    .iv-read .iv-flag{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('iv-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var SIDE=336, TOPP=22, CX0=(W-SIDE)/2;

  // invd is the memorized derivative of the inverse, as a function of a — used
  // only as an independent check, never to produce the answer.
  // Ranges are chosen so that the b values the article quotes land on integer
  // slider positions: b = 1 at 900, b = pi/6 at 800, b = pi/4 at 960, b = 0 at 600.
  var F=[
    { n:'x³ + x', inv:null, invd:null, lo:-2, hi:2, cx:0, cy:0, w:4.6,
      f:function(x){ return x*x*x+x; }, df:function(x){ return 3*x*x+1; } },
    { n:'eˣ', inv:'ln x', invd:function(a){ return 1/a; },
      lo:-2.6, hi:1.9, cx:1.4, cy:1.4, w:4.4,
      f:Math.exp, df:Math.exp },
    { n:'sin x  on  [-π/2, π/2]', inv:'arcsin x',
      invd:function(a){ return 1/Math.sqrt(1-a*a); },
      lo:-Math.PI/2, hi:Math.PI/2, cx:0, cy:0, w:1.85,
      f:Math.sin, df:Math.cos },
    { n:'tan x  on  (-5π/12, 5π/12)', inv:'arctan x',
      invd:function(a){ return 1/(1+a*a); },
      lo:-5*Math.PI/12, hi:5*Math.PI/12, cx:0, cy:0, w:4,
      f:Math.tan, df:function(x){ var s=1/Math.cos(x); return s*s; } },
    { n:'x³', inv:'∛x', invd:function(a){ return 1/(3*Math.pow(Math.cbrt(a),2)); },
      lo:-1.75, hi:1.75, cx:0, cy:0, w:2.2,
      f:function(x){ return x*x*x; }, df:function(x){ return 3*x*x; } }
  ];
  var k=0;
  function G(){ return F[k]; }
  function px(x){ var g=G(); return CX0+(x-(g.cx-g.w))/(2*g.w)*SIDE; }
  function py(y){ var g=G(); return TOPP+SIDE-(y-(g.cy-g.w))/(2*g.w)*SIDE; }
  function fmt(v){ var a=Math.abs(v);
    if(a<1e-12) return (0).toFixed(4);
    if(a<1e-3||a>=1e5) return v.toExponential(3);
    return v.toFixed(4); }

  var bar=$('iv-fns');
  F.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  function seg(x0,y0,x1,y1){ c.beginPath(); c.moveTo(px(x0),py(y0)); c.lineTo(px(x1),py(y1)); c.stroke(); }

  function draw(){
    var g=G(), s=(+$('iv-b').value)/1200, b=g.lo+s*(g.hi-g.lo);
    var a=g.f(b), m=g.df(b);
    Array.prototype.forEach.call(bar.children,function(e,i){
      e.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(CX0,TOPP,SIDE,SIDE); c.clip();

    c.strokeStyle=LINE; c.lineWidth=1;
    var i, lo=Math.ceil(g.cx-g.w), hi=Math.floor(g.cx+g.w);
    for(i=lo;i<=hi;i++) seg(i,g.cy-g.w,i,g.cy+g.w);
    lo=Math.ceil(g.cy-g.w); hi=Math.floor(g.cy+g.w);
    for(i=lo;i<=hi;i++) seg(g.cx-g.w,i,g.cx+g.w,i);

    // the mirror line
    c.strokeStyle=PALE; c.lineWidth=1.4; c.setLineDash([5,4]);
    seg(g.cx-g.w,g.cx-g.w,g.cx+g.w,g.cx+g.w);
    c.setLineDash([]);

    // f, then its reflection: the same points with the coordinates swapped
    var N=900, t, x, y;
    c.strokeStyle=INK; c.lineWidth=2; c.beginPath();
    for(i=0;i<=N;i++){ t=g.lo+(g.hi-g.lo)*i/N; x=t; y=g.f(t);
      if(i===0) c.moveTo(px(x),py(y)); else c.lineTo(px(x),py(y)); }
    c.stroke();
    c.strokeStyle=FAINT; c.lineWidth=2; c.beginPath();
    for(i=0;i<=N;i++){ t=g.lo+(g.hi-g.lo)*i/N; x=g.f(t); y=t;
      if(i===0) c.moveTo(px(x),py(y)); else c.lineTo(px(x),py(y)); }
    c.stroke();

    // the two tangents, each drawn over the same short run
    var r=0.5*g.w;
    c.lineWidth=1.6;
    c.strokeStyle=INK; seg(b-r, a-r*m, b+r, a+r*m);
    if(m!==0){ c.strokeStyle=FAINT; seg(a-r, b-r/m, a+r, b+r/m); }
    else     { c.strokeStyle=FAINT; seg(a, b-r, a, b+r); }   // vertical mirror tangent

    c.fillStyle=INK; c.beginPath(); c.arc(px(b),py(a),4.5,0,6.284); c.fill();
    c.fillStyle=FAINT; c.beginPath(); c.arc(px(a),py(b),4.5,0,6.284); c.fill();
    c.restore();
    c.fillStyle=MUTED; c.font='700 11px '+FONT; c.textAlign='left';
    c.fillText('f(x) = '+g.n, CX0, TOPP-8);
    c.textAlign='right';
    c.fillText(g.inv ? 'f⁻¹(x) = '+g.inv : 'f⁻¹ has no elementary formula', CX0+SIDE, TOPP-8);

    var dead = Math.abs(m) < 1e-12;
    var rec = dead ? null : 1/m;
    function row(lab,body){ return '<div><span class="iv-lab">'+lab+'</span>'+body+'</div>'; }
    function V(x){ return '<span class="iv-val">'+x+'</span>'; }
    function flag(x){ return '<span class="iv-flag">'+x+'</span>'; }
    var out=
      row('b', V(fmt(b)))+
      row('a = f(b)', V(fmt(a)))+
      row('f&prime;(b)', V(fmt(m)))+
      row('(f&#8315;&sup1;)&prime;(a) = 1 / f&prime;(b)',
          dead ? flag('undefined &mdash; f&prime;(b) is zero') : V(fmt(rec)))+
      row('f&prime;(b) &times; (f&#8315;&sup1;)&prime;(a)',
          dead ? flag('no product to form') : V(fmt(m*rec)));
    if(g.invd){
      var known=g.invd(a);
      out+=row('from the formula for '+g.inv,
        (!isFinite(known) || dead) ? flag('undefined there too')
          : V(fmt(known))+flag('&nbsp;&nbsp;gap '+Math.abs(known-rec).toExponential(1)));
    } else {
      out+=row('from the formula for f&#8315;&sup1;', flag('there is no such formula'));
    }
    $('iv-read').innerHTML=out;
  }
  $('iv-b').addEventListener('input',draw);
  draw();
})();
</script>

The visualization shows $$f$$ and its reflection across $$y=x$$.

A point $$(b,f(b))$$ on the original graph corresponds to

$$(f(b),b)$$

on the inverse.

The tangent slopes at those two points are reciprocals wherever both derivatives exist.

This is useful when a problem provides a table rather than a formula.

If you are asked for

$$\big(f^{-1}\big)'(4),$$

look for the row where

$$f(x)=4.$$

That row gives $$f^{-1}(4)$$. The derivative $$f'$$ must be evaluated at that input.

Looking for $$x=4$$ instead is the common mistake.

## Inverse trigonometric derivatives

The inverse trigonometric derivative formulas can be derived from the same rule.

For $$f=\sin$$ on the interval where sine is one-to-one,

$$(\arcsin)'(a) = \frac{1}{\cos(\arcsin a)}.$$

Using the Pythagorean identity,

$$\cos(\arcsin a) = \sqrt{1-a^2},$$

so

$$(\arcsin)'(a) = \frac{1}{\sqrt{1-a^2}}.$$

For tangent,

$$(\arctan)'(a) = \frac{1}{\sec^2(\arctan a)}.$$

Since

$$\sec^2\theta=1+\tan^2\theta,$$

we get

$$(\arctan)'(a) = \frac{1}{1+a^2}.$$

These formulas are consequences of the inverse-function rule and [trigonometric identities](/2026/07/30/derivative-rules-and-choosing.html).

## When the reciprocal does not exist

Take

$$f(x)=x^3.$$

Its inverse is

$$f^{-1}(x)=x^{1/3}.$$

At the origin,

$$f'(0)=0.$$

So the reciprocal formula would require division by zero.

The graph explains why. The tangent to $$x^3$$ at the origin is horizontal. Reflecting that tangent across $$y=x$$ produces a vertical line.

The inverse therefore has a [vertical tangent](/2026/07/30/where-differentiability-fails.html) at the corresponding point, not a finite derivative.

<div class="article-note" markdown="1">
The condition

$$f'\big(f^{-1}(a)\big)\neq0$$

is part of the theorem for a reason.
</div>
