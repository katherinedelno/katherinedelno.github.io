---
layout: post
title: "When an unbounded region has finite area"
date: 2026-07-30
description: "An improper integral is defined through a limit. An infinite interval or an unbounded integrand does not by itself determine whether the integral converges."
course: "AP Calculus BC"
read_time: "8 min read"
math: true
kind: mechanics
sequence: 24
interactive: true
blurb: "An improper integral is defined through a limit. An infinite interval or an unbounded integrand does not by itself determine whether the integral converges"
image: "/assets/og/improper-integrals.png"
---

A definite integral becomes improper when the interval is unbounded or the integrand becomes unbounded somewhere on the interval.

In either case, the integral is [defined through a limit](/2026/07/30/what-a-limit-claims.html).

The geometric region may extend infinitely far or rise without bound and still have finite area.

## An infinite interval

Consider

$$\int_1^\infty \frac{1}{x^2}\,dx.$$

The infinity symbol is not an endpoint at which an antiderivative can be evaluated.

Instead, write

$$\int_1^\infty \frac{1}{x^2}\,dx = \lim_{T\to\infty} \int_1^T \frac{1}{x^2}\,dx.$$

Then

$$= \lim_{T\to\infty} \left[-\frac1x\right]_1^T = \lim_{T\to\infty} \left(1-\frac1T\right) = 1.$$

The interval has infinite length, but the area is finite.

The integral converges.

## An unbounded integrand

Now consider

$$\int_0^1\frac{1}{\sqrt{x}}\,dx.$$

The interval is finite, but the integrand grows without bound as $$x\to0^+$$.

So write

$$\int_0^1\frac{1}{\sqrt{x}}\,dx = \lim_{s\to0^+} \int_s^1 x^{-1/2}\,dx.$$

Then

$$= \lim_{s\to0^+} \left[2\sqrt{x}\right]_s^1 = \lim_{s\to0^+} \left(2-2\sqrt{s}\right) = 2.$$

Again, the integral converges.

The vertical asymptote does not force the area to be infinite.

## The $$p$$-integral thresholds

<div class="viz" markdown="0">
  <canvas id="im-cv" width="700" height="340"></canvas>
  <div class="viz-controls">
    <label for="im-p">p</label>
    <input type="range" id="im-p" min="0" max="1200" step="1" value="800">
    <label for="im-d">how far out, in decades</label>
    <input type="range" id="im-d" min="0" max="1200" step="1" value="600">
  </div>
  <div class="im-read" id="im-read"></div>
  <p class="viz-caption">Top: y = x⁻ᵖ drawn on logarithmic axes, where every power function is a straight line of slope −p. The dashed diagonal is p = 1, the dividing case. Bottom: the two partial integrals plotted against how far the cutoff has been pushed, in decades — outward toward infinity, and inward toward zero. Both start at zero and climb. A curve that flattens is converging to the value the panel names; a curve that keeps rising is diverging, and the panel says so rather than printing a number. Slide p through 1 and watch the two verdicts trade places.</p>
  <style>
    .im-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .im-read .im-lab{color:var(--muted);display:inline-block;min-width:13.5rem}
    .im-read .im-val{font-weight:700;display:inline-block;min-width:7.5rem}
    .im-read .im-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('im-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=44,PADR=18, T1=16,B1=158, T2=196,B2=H-26;
  var L10=Math.LN10, DMAX=6, YMAX=14;

  // p runs 0..3 in steps of 0.0025 and d runs 0..6 in steps of 0.005, so
  // p = 0.5, 1, 1.5, 2 land on 200, 400, 600, 800 and d = 1, 3 on 200, 600.
  function P(){ return (+$('im-p').value)/1200*3; }
  function D(){ return (+$('im-d').value)/1200*DMAX; }

  // exact partial integrals, as functions of how many decades out or in
  function outer(p,d){ return p===1 ? d*L10 : (Math.pow(10,d*(1-p))-1)/(1-p); }
  function inner(p,d){ return p===1 ? d*L10 : (1-Math.pow(10,-d*(1-p)))/(1-p); }

  function lx(u){ return PADL+(u+3)/6*(W-PADL-PADR); }          // log10 x from -3 to 3
  function ly(v){ return B1-(v+3)/9*(B1-T1); }                  // log10 y from -3 to 6
  function dx(u){ return PADL+u/DMAX*(W-PADL-PADR); }
  function dy(v){ return B2-Math.min(v,YMAX)/YMAX*(B2-T2); }
  function fmt(v){ var a=Math.abs(v); if(a<1e-12) return (0).toFixed(4);
    if(a>=1e5) return v.toExponential(4); return v.toFixed(4); }

  function draw(){
    var p=P(), d=D();
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(PADL-2,0,W-PADL-PADR+4,H); c.clip();

    // --- top: the power function on log-log axes
    c.strokeStyle=LINE; c.lineWidth=1;
    for(var k=-3;k<=3;k++){ c.beginPath(); c.moveTo(lx(k),T1); c.lineTo(lx(k),B1); c.stroke(); }
    for(k=-3;k<=6;k+=3){ c.beginPath(); c.moveTo(PADL,ly(k)); c.lineTo(W-PADR,ly(k)); c.stroke(); }
    c.strokeStyle=PALE; c.lineWidth=1.4; c.setLineDash([5,4]);
    c.beginPath(); c.moveTo(lx(-3),ly(3)); c.lineTo(lx(3),ly(-3)); c.stroke();   // slope -1
    c.beginPath(); c.moveTo(lx(0),T1); c.lineTo(lx(0),B1); c.stroke();           // x = 1
    c.setLineDash([]);
    c.strokeStyle=INK; c.lineWidth=2.4;
    c.beginPath(); c.moveTo(lx(-3),ly(3*p)); c.lineTo(lx(3),ly(-3*p)); c.stroke();
    // the two cutoffs currently in play
    c.strokeStyle=FAINT; c.lineWidth=1; c.setLineDash([3,3]);
    [d,-d].forEach(function(u){ c.beginPath(); c.moveTo(lx(u),T1); c.lineTo(lx(u),B1); c.stroke(); });
    c.setLineDash([]);
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    c.fillText('x = 1', lx(0), B1+13);
    c.fillText('10⁻ᵈ', lx(-d), B1+13); c.fillText('10ᵈ', lx(d), B1+13);
    c.textAlign='left'; c.fillText('y = x⁻ᵖ, on log axes', 4, T1+9);

    // --- bottom: the two running values against d
    c.strokeStyle=LINE; c.lineWidth=1;
    for(k=0;k<=DMAX;k++){ c.beginPath(); c.moveTo(dx(k),T2); c.lineTo(dx(k),B2); c.stroke(); }
    var i,u;
    [[outer,INK,2.4],[inner,FAINT,2.4]].forEach(function(q){
      c.strokeStyle=q[1]; c.lineWidth=q[2]; c.beginPath();
      var started=false;
      for(i=0;i<=600;i++){ u=DMAX*i/600; var v=q[0](p,u);
        if(v>YMAX){ if(started) c.lineTo(dx(u),dy(YMAX)); started=false; continue; }
        if(!started){ c.moveTo(dx(u),dy(v)); started=true; } else c.lineTo(dx(u),dy(v)); }
      c.stroke(); });
    c.strokeStyle=FAINT; c.lineWidth=1; c.setLineDash([3,3]);
    c.beginPath(); c.moveTo(dx(d),T2); c.lineTo(dx(d),B2); c.stroke(); c.setLineDash([]);
    [[outer,INK],[inner,FAINT]].forEach(function(q){
      var v=q[0](p,d); if(v<=YMAX){
        c.fillStyle=q[1]; c.beginPath(); c.arc(dx(d),dy(v),4.5,0,6.284); c.fill(); } });
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText('accumulated area against d', 4, T2+9);
    c.textAlign='center';
    for(k=0;k<=DMAX;k++) c.fillText(String(k), dx(k), B2+14);

    var oc = p>1, ic = p<1;
    function row(l,v,n){ return '<div><span class="im-lab">'+l+'</span>'+
      '<span class="im-val">'+v+'</span>'+(n?'<span class="im-note">'+n+'</span>':'')+'</div>'; }
    $('im-read').innerHTML =
      row('p', fmt(p), 'the line above has slope −p') +
      row('d, decades', fmt(d), 'cutoffs at 10⁻ᵈ and 10ᵈ') +
      row('∫ from 1 to 10ᵈ', fmt(outer(p,d)),
          oc ? 'converges to 1/(p − 1) = '+fmt(1/(p-1)) : 'diverges, since p ≤ 1') +
      row('∫ from 10⁻ᵈ to 1', fmt(inner(p,d)),
          ic ? 'converges to 1/(1 − p) = '+fmt(1/(1-p)) : 'diverges, since p ≥ 1') +
      row('∫ from 0 to ∞', (oc&&ic)?'—':'diverges',
          'no p makes both ends finite');
  }
  $('im-p').addEventListener('input',draw);
  $('im-d').addEventListener('input',draw);
  draw();
})();
</script>

Two standard families are worth knowing.

For the tail integral,

$$\int_1^\infty \frac{1}{x^p}\,dx,$$

the integral converges exactly when

$$p>1.$$

When it converges,

$$\int_1^\infty x^{-p}\,dx = \frac{1}{p-1}.$$

For the integral near zero,

$$\int_0^1\frac{1}{x^p}\,dx,$$

the condition reverses.

It converges exactly when

$$p<1.$$

When it converges,

$$\int_0^1 x^{-p}\,dx = \frac{1}{1-p}.$$

The boundary case

$$p=1$$

diverges in both settings.

The same expression,

$$\frac1x,$$

therefore sits at the convergence threshold both near zero and at infinity.

## A discontinuity inside the interval

Suppose

$$\int_{-1}^{1}\frac{1}{x^2}\,dx.$$

The integrand is unbounded at $$x=0$$, so the integral must be split there:

$$\int_{-1}^{1}\frac{1}{x^2}\,dx = \int_{-1}^{0}\frac{1}{x^2}\,dx + \int_{0}^{1}\frac{1}{x^2}\,dx.$$

Each piece is improper and needs its own limit.

Both diverge.

So the original integral diverges.

If we ignore the discontinuity and apply the Fundamental Theorem mechanically,

$$\left[-\frac1x\right]_{-1}^{1} = -2.$$

That answer is impossible as geometric area under a positive function.

The problem is not the antiderivative. [The Fundamental Theorem](/2026/07/17/fundamental-theorem-from-the-ground-up.html) was applied across a point where the hypotheses failed.

## Two habits that prevent most errors

First, inspect the interval and the integrand before integrating.

Look for infinite bounds, denominator zeros, logarithmic singularities, and endpoints where a root or power becomes unbounded.

Second, write the limit explicitly.

The limit is part of the definition of the improper integral.

<div class="article-note" markdown="1">
If the limit is finite, the integral converges.

If the limit is infinite or fails to exist, the integral diverges.
</div>
