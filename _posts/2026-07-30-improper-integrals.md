---
layout: post
title: "Improper integrals, and the exponent that decides"
date: 2026-07-30
description: "An integral is improper when a limit is infinite or the integrand blows up. Both cases are handled the same way, and for the power functions the verdict turns on a single number."
course: "AP Calculus BC"
read_time: "8 min read"
math: true
kind: mechanics
sequence: 24
interactive: true
blurb: "The exponent that saves you at infinity is the one that ruins you at zero"
---

The framework's enduring understanding for this topic is worth reading twice, because it states a result rather than a technique: the use of limits allows us to show that the areas of unbounded regions may be finite.

Unbounded regions with finite area are not intuitive, and the machinery that establishes them is short. Everything hard about improper integrals is in deciding which ones are finite.

## Two ways to be improper

The framework's definition names both: an improper integral is one that has one or both limits infinite, or has an integrand that is unbounded in the interval of integration.

The first kind is visible in the notation. The second is not, and that is what makes it dangerous — $$\textstyle\int_0^1 \tfrac{dx}{\sqrt{x}}$$ looks like an ordinary definite integral and is not one, because the integrand has no value at the left endpoint. Before evaluating anything, check the integrand at both endpoints and everywhere between.

## Rewrite as a limit

The procedure is one line of the framework: improper integrals are determined using limits of definite integrals. Replace the offending endpoint with a variable, integrate properly, and take the limit.

$$\int_1^{\infty} \frac{dx}{x^2} = \lim_{T\to\infty}\int_1^{T}\frac{dx}{x^2} = \lim_{T\to\infty}\left(1 - \frac1T\right) = 1.$$

An unbounded region with area exactly 1. The same move handles the other kind:

$$\int_0^{1} \frac{dx}{\sqrt{x}} = \lim_{s\to 0^+}\int_s^{1}\frac{dx}{\sqrt{x}} = \lim_{s\to 0^+}\big(2 - 2\sqrt{s}\big) = 2.$$

Notice that the limit is [one-sided](/2026/07/30/what-a-limit-claims.html), and that it approaches the bad endpoint from inside the interval. Writing the limit is not decoration; a divergent integral looks exactly like a convergent one until the limit is taken, and there is nowhere else for the word "diverges" to come from.

## The same exponent, opposite verdicts

Both of the integrals above are $$x^{-p}$$ for some $$p$$, and both converged. That is a coincidence of which $$p$$ went with which end.

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

The pattern is exact and it is a reversal. For the tail out to infinity, $$\textstyle\int_1^{\infty} x^{-p}dx$$ converges precisely when $$p > 1$$, to $$\tfrac{1}{p-1}$$. For the spike at the origin, $$\textstyle\int_0^{1} x^{-p}dx$$ converges precisely when $$p < 1$$, to $$\tfrac{1}{1-p}$$.

The reason is the same in both cases and it is worth saying once. Convergence at infinity needs the function to fall off quickly, and a large $$p$$ does that. Convergence at zero needs the function to blow up slowly, and a large $$p$$ does the opposite. One exponent cannot do both, which is why $$\textstyle\int_0^{\infty} x^{-p}dx$$ diverges for every $$p$$ whatsoever.

At $$p = 1$$ both fail. That is the case the log-log picture makes obvious: $$y = x^{-p}$$ is a straight line of slope $$-p$$ on those axes, and $$p = 1$$ is the dashed diagonal that separates the two behaviours. It is on the wrong side of both boundaries at once, because both are strict.

That threshold is going to appear again. The series $$\textstyle\sum n^{-p}$$ converges under exactly the condition that $$\textstyle\int_1^{\infty}x^{-p}dx$$ does, and the case $$p = 1$$ — [the harmonic series](/2026/07/23/harmonic-series-surprises-of-infinity.html) — is on the divergent side of both. That is not a coincidence, and Unit 10 gives it a name and a theorem. The framework recommends making the connection in the other direction as well, from the integral test back to this topic.

## The blow-up you did not look for

Here is the one that catches people, and it catches them because it does not look improper:

$$\int_{-1}^{1}\frac{dx}{x^2}.$$

Both limits are finite. Antidifferentiate and evaluate and you get $$\left[-\tfrac1x\right]_{-1}^{1} = -1 - 1 = -2$$, which is a confident, wrong, and impossible answer — the integrand is positive wherever it is defined, so no correct value can be negative.

The integrand is unbounded at $$x = 0$$, which is inside the interval. The integral has to be split there, and each half evaluated as its own limit. Each half is $$\textstyle\int x^{-2}$$ against the origin with $$p = 2 > 1$$, so each half diverges, and so does the whole thing.

The absurd answer is the useful part. An integral of a positive function that returns a negative number is telling you that [the Fundamental Theorem](/2026/07/17/fundamental-theorem-from-the-ground-up.html) was applied across a point where its hypotheses fail — it wants an integrand that is continuous on the closed interval, and this one is not defined at the middle of it.

<div class="article-note" markdown="1">
Two habits close most of the gap on this topic. Write the limit every time, even when you are sure it converges, because the notation is the argument and a value with no limit attached has not been justified. And before starting, look at the integrand at both endpoints and at any zero of a denominator inside the interval — that scan takes five seconds and is the only defence against the case that does not announce itself.
</div>
