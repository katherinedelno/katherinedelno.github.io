---
layout: post
title: "Logistic growth, read without solving it"
date: 2026-07-30
description: "The framework says the logistic model can be interpreted without solving the differential equation. That is not a concession — it is the whole method, and everything the exam asks falls out of the equation itself."
course: "AP Calculus BC"
read_time: "9 min read"
math: true
kind: foundations
sequence: 26
interactive: true
blurb: "The carrying capacity and the fastest growth are both visible in the equation"
---

Exponential growth assumes nothing ever runs out. Logistic growth is what you write down when something does.

The framework builds the model from a sentence rather than from a formula: the rate of change of a quantity is jointly proportional to the size of the quantity and the difference between the quantity and the carrying capacity. Translated,

$$\frac{dy}{dt} = ky(a-y).$$

Two factors, each doing a job. The $$y$$ makes growth proportional to what is already there, which is the exponential part. The $$(a-y)$$ is the brake, and it tightens as $$y$$ approaches $$a$$.

## From the sentence to the equation

"Jointly proportional to" is the phrase carrying the structure, and it means proportional to a product, not to a sum. So the rate is $$k$$ times $$y$$ times $$(a - y)$$, and the two misreadings both come from mishandling that phrase.

The first is writing $$\tfrac{dy}{dt} = ky + (a-y)$$, which is proportional to nothing in particular and does not have $$y = a$$ as an equilibrium. The second is writing $$\tfrac{dy}{dt} = k(a-y)$$, dropping the size factor — that is a perfectly good model, but it is Newton's law of cooling rather than logistic growth, and its graph has no S-shape because nothing slows it down at the start.

The test for whether the equation is right is whether it has two constant solutions. Logistic growth stalls at the bottom as well as at the top, and both stalls have to be visible in the algebra.

## Everything without solving

The framework states, as its own piece of essential knowledge, that the logistic differential equation and initial conditions can be interpreted without solving the differential equation. That is the method, not a fallback. The exam does not ask for $$y(t)$$, and the two quantities it does ask for are both properties of the right-hand side.

**The carrying capacity.** Growth stops when $$\tfrac{dy}{dt} = 0$$, and $$ky(a-y) = 0$$ exactly when $$y = 0$$ or $$y = a$$. Those are the two constant solutions. Starting anywhere strictly between them, the rate is positive, so $$y$$ increases and cannot pass $$a$$ without the rate changing sign first. The limiting value is $$a$$, read straight off the factored form.

**Where growth is fastest.** As a function of $$y$$, the rate $$ky(a-y)$$ is a downward parabola with roots at $$0$$ and $$a$$, so it peaks halfway between them. The fastest growth happens at

$$y = \frac{a}{2}, \qquad \text{with rate} \quad \frac{ka^2}{4}.$$

No calculus was needed for that, only the symmetry of a parabola. Differentiating the rate with respect to $$y$$ gives $$k(a-2y)$$, which agrees.

## What that means for the shape

The value $$y = \tfrac{a}{2}$$ is also where the solution curve changes concavity, and the reason is the [chain rule](/2026/07/30/chain-rule-reading-the-layers.html) applied to the equation itself:

$$\frac{d^2y}{dt^2} = \frac{d}{dt}\Big[ky(a-y)\Big] = k(a-2y)\frac{dy}{dt} = k^2\,y\,(a-y)(a-2y).$$

For $$0 < y < a$$ the first two factors are positive, so the sign is the sign of $$a - 2y$$: concave up below half capacity, concave down above it. That is the S-shape, and it was derived without ever writing down a solution.

<div class="viz" markdown="0">
  <canvas id="lg-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <label for="lg-y0">y₀</label>
    <input type="range" id="lg-y0" min="0" max="1200" step="1" value="75">
    <label for="lg-k">k</label>
    <input type="range" id="lg-k" min="0" max="1200" step="1" value="400">
  </div>
  <div class="lg-read" id="lg-read"></div>
  <p class="viz-caption">The carrying capacity is fixed at 100. Short strokes give the slope field for dy/dt = ky(100 − y); the pale curves are solutions from a spread of starting values and the dark one is the solution from the chosen y₀. Every curve is computed by stepping the differential equation numerically, never from a formula for y — which is the point of the topic. The two dashed lines are the equilibria at 0 and 100; the dotted line at 50 is where every curve has its steepest point and its inflection, whichever side it starts on.</p>
  <style>
    .lg-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .lg-read .lg-lab{color:var(--muted);display:inline-block;min-width:13rem}
    .lg-read .lg-val{font-weight:700;display:inline-block;min-width:7rem}
    .lg-read .lg-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('lg-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=44,PADR=18,TOP=16,BOT=H-26;
  var A=100, TMAX=5, YLO=-8, YHI=168;

  // y0 runs 0..160 in steps of 2/15 and k runs 0..0.06 in steps of 0.00005,
  // so y0 = 10, 50, 100, 150 land on 75, 375, 750, 1125 and k = 0.02 on 400.
  function Y0(){ return (+$('lg-y0').value)/1200*160; }
  function K(){  return (+$('lg-k').value)/1200*0.06; }
  function rate(k,y){ return k*y*(A-y); }

  function px(t){ return PADL+t/TMAX*(W-PADL-PADR); }
  function py(y){ return BOT-(y-YLO)/(YHI-YLO)*(BOT-TOP); }
  function fmt(v){ var a=Math.abs(v); if(a<1e-12) return (0).toFixed(4);
    if(a>=1e5) return v.toExponential(4); return v.toFixed(4); }

  // classical fourth-order Runge-Kutta, so the curve comes from the equation
  // and not from the closed-form solution
  function solve(k,y0,n){
    var h=TMAX/n, y=y0, out=[[0,y0]], i;
    for(i=0;i<n;i++){
      var k1=rate(k,y), k2=rate(k,y+h*k1/2), k3=rate(k,y+h*k2/2), k4=rate(k,y+h*k3);
      y=y+h*(k1+2*k2+2*k3+k4)/6;
      out.push([(i+1)*h,y]);
    }
    return out;
  }
  function at(path,t){
    var n=path.length-1, i=Math.min(n, Math.max(0, Math.floor(t/TMAX*n)));
    if(i>=n) return path[n][1];
    var f=(t-path[i][0])/(path[i+1][0]-path[i][0]);
    return path[i][1]+f*(path[i+1][1]-path[i][1]);
  }

  function draw(){
    var y0=Y0(), k=K();
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(PADL-2,TOP-6,W-PADL-PADR+4,BOT-TOP+12); c.clip();

    // slope field
    c.strokeStyle=LINE; c.lineWidth=1.4;
    for(var i=0;i<=16;i++) for(var j=0;j<=13;j++){
      var t=TMAX*i/16, y=YLO+(YHI-YLO)*j/13;
      var m=rate(k,y), L=9;
      var dt=1, dy=m, n=Math.hypot(px(1)-px(0), py(0)-py(m));
      if(n===0) continue;
      var ux=(px(1)-px(0))/n*L, uy=-(py(0)-py(m))/n*L;
      c.beginPath(); c.moveTo(px(t)-ux,py(y)+uy); c.lineTo(px(t)+ux,py(y)-uy); c.stroke();
    }
    // equilibria and the half-capacity line
    c.strokeStyle=PALE; c.lineWidth=1.4; c.setLineDash([6,4]);
    [0,A].forEach(function(v){ c.beginPath(); c.moveTo(PADL,py(v)); c.lineTo(W-PADR,py(v)); c.stroke(); });
    c.setLineDash([2,4]);
    c.beginPath(); c.moveTo(PADL,py(A/2)); c.lineTo(W-PADR,py(A/2)); c.stroke();
    c.setLineDash([]);

    // a family of solutions, then the chosen one
    c.strokeStyle=PALE; c.lineWidth=1.4;
    [5,20,40,60,80,120,150].forEach(function(s){
      var p=solve(k,s,400); c.beginPath();
      p.forEach(function(q,n){ if(n===0) c.moveTo(px(q[0]),py(q[1])); else c.lineTo(px(q[0]),py(q[1])); });
      c.stroke(); });
    var path=solve(k,y0,800);
    c.strokeStyle=INK; c.lineWidth=2.4; c.beginPath();
    path.forEach(function(q,n){ if(n===0) c.moveTo(px(q[0]),py(q[1])); else c.lineTo(px(q[0]),py(q[1])); });
    c.stroke();
    c.fillStyle=INK; c.beginPath(); c.arc(px(0),py(y0),4.5,0,6.284); c.fill();
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='right';
    [0,50,100,150].forEach(function(v){ c.fillText(String(v), PADL-6, py(v)+3); });
    c.textAlign='center';
    for(i=0;i<=5;i++) c.fillText(String(i), px(i), BOT+14);

    var yEnd=at(path,TMAX), r0=rate(k,y0), maxRate=k*A*A/4;
    var fate = y0===0 ? 'stays at 0 forever, an equilibrium'
             : (Math.abs(y0-A)<1e-9 ? 'stays at 100 forever, the other equilibrium'
             : (y0<A ? 'rises toward 100' : 'falls toward 100'));
    function row(l,v,n){ return '<div><span class="lg-lab">'+l+'</span>'+
      '<span class="lg-val">'+v+'</span>'+(n?'<span class="lg-note">'+n+'</span>':'')+'</div>'; }
    $('lg-read').innerHTML =
      row('k', fmt(k), 'carrying capacity a = 100, fixed') +
      row('y₀', fmt(y0), fate) +
      row('dy/dt at t = 0', fmt(r0), r0>0?'growing':(r0<0?'shrinking':'not changing')) +
      row('y at t = 5', fmt(yEnd), 'by Runge–Kutta on the equation itself') +
      row('fastest growth at y', fmt(A/2), 'always a/2, whatever k and y₀ are') +
      row('and the rate there', fmt(maxRate), 'ka²/4');
  }
  $('lg-y0').addEventListener('input',draw);
  $('lg-k').addEventListener('input',draw);
  draw();
})();
</script>

Every curve is produced by stepping the differential equation forward numerically, in the same spirit as [Euler's method](/2026/07/25/euler-method-step-size.html) but with a more accurate step. That is deliberate: nothing in the picture comes from a formula for $$y$$, because the topic does not have one.

Three things are worth watching. Every curve starting strictly between 0 and 100 ends at 100, and so does every curve starting above it — the approach is from below or from above, and the destination does not care. The two flat lines are genuine solutions, not artifacts. And $$k$$ changes how fast the whole thing happens without moving the carrying capacity or the half-capacity line by a single unit.

That last point is the one to hold onto. The framework asks for the carrying capacity and for the value where the quantity is changing fastest, and neither depends on $$k$$ or on where you started.

Reasoning about a differential equation's long-run behaviour without solving it has a name in the courses that follow this one, and [it is most of what they do](/2026/07/26/beyond-bc-differential-equations.html). The logistic model is where it starts.

## Saying it in context

The suggested skill for this topic is to explain the meaning of mathematical solutions in context, which for a logistic model means three sentences and no formulas.

Take a fish population modelled by $$\tfrac{dP}{dt} = 0.02P(100-P)$$, with $$P$$ in thousands and $$t$$ in years, starting at 10 thousand. The population approaches 100 thousand in the long run, because that is the value making the rate zero from a start below it. It is growing fastest when it reaches 50 thousand, half the carrying capacity. At that moment it is growing at $$\tfrac{ka^2}{4} = 50$$ thousand per year.

Every one of those came from the equation. The one thing they do not tell you is *when* the population reaches 50 thousand, and that is the question the exam does not ask, because answering it needs the solution.

<div class="article-note" markdown="1">
A quick sanity check on any logistic answer: the carrying capacity is the number in the parentheses when the equation is written as $$\tfrac{dy}{dt} = ky(a-y)$$, and half of it is where growth peaks. If the equation arrives in the expanded form $$\tfrac{dy}{dt} = 0.5y - 0.001y^2$$, factor first — that is $$0.001y(500-y)$$, so the capacity is 500 and not 0.5 or 0.001. Reading a capacity off an unfactored equation is the most common way to lose the point.
</div>
