---
layout: post
title: "Logistic growth, read without solving it"
date: 2026-07-30
description: "The logistic differential equation reveals its equilibria, carrying capacity, fastest growth, and concavity before the equation is solved."
course: "AP Calculus BC"
read_time: "6 min read"
math: true
kind: foundations
sequence: 26
interactive: true
blurb: "The logistic differential equation reveals its equilibria, carrying capacity, fastest growth, and concavity before the equation is solved"
image: "/assets/og/logistic-growth.png"
---

A logistic differential equation has the form

$$\frac{dy}{dt} = ky(a-y)$$

with $$k>0$$. The equation describes growth that is initially reinforced by the size of the population and eventually limited by a carrying capacity, and a surprising amount can be read directly from the differential equation without solving it.

## The two factors

The factor $$y$$ makes the growth rate proportional to the current population, and the factor $$a-y$$ slows the growth as the population approaches $$a$$. The equilibrium solutions occur where $$\tfrac{dy}{dt}=0$$, so $$y=0$$ and $$y=a$$ are equilibria.

For a population starting between them, $$0<y<a$$, both factors are positive and the population increases. As $$y$$ approaches $$a$$, the factor $$a-y$$ approaches zero and the growth slows, and the value $$a$$ is the carrying capacity.

## Growth is fastest halfway up

The growth rate can be viewed as a function of $$y$$, namely $$R(y) = ky(a-y) = k(ay-y^2)$$, which is a downward-opening parabola. Its maximum occurs at $$y=\tfrac a2$$, and at that point, $$R\left(\tfrac a2\right) = \tfrac{ka^2}{4}$$. So a logistic population grows fastest when it reaches half its carrying capacity, and that same point is the inflection point of the solution curve.

## Concavity from the equation

Differentiate the differential equation with respect to time and substitute $$y'=ky(a-y)$$:

$$\begin{aligned}
y'' &= k y'(a-2y)\\
&= k^2y(a-y)(a-2y)
\end{aligned}$$

For a solution with $$0<y<a$$, the first three factors except $$a-2y$$ are positive, so the sign of $$y''$$ is determined by $$a-2y$$. When $$y<\tfrac a2$$, the solution is concave up, and when $$y>\tfrac a2$$, it is concave down. The change occurs at half the carrying capacity, exactly where the growth rate is largest.

<div class="viz" markdown="0">
  <canvas id="lg-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <label for="lg-y0">y₀</label>
    <input type="range" id="lg-y0" min="0" max="1200" step="1" value="75">
    <label for="lg-k">k</label>
    <input type="range" id="lg-k" min="0" max="1200" step="1" value="400">
  </div>
  <div class="lg-read" id="lg-read"></div>
  <p class="viz-caption">The carrying capacity is fixed at 100. Short strokes give the slope field for dy/dt = ky(100 − y); the pale curves are solutions from a spread of starting values and the dark one is the solution from the chosen y₀. Every curve is computed by stepping the differential equation numerically, never from a formula for y, which is the point of the topic. The two dashed lines are the equilibria at 0 and 100; the dotted line at 50 is where every curve has its steepest point and its inflection, whichever side it starts on.</p>
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
      var ux=(px(1)-px(0))/n*L, uy=(py(0)-py(m))/n*L;
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

The visualization fixes the carrying capacity at 100 and lets the initial value and growth constant vary. Changing $$k$$ changes the time scale, and a larger $$k$$ makes the population move through the same stages more quickly. It does not change the carrying capacity or the population size at which growth is fastest.

## Reading an expanded equation

A logistic equation may not be presented in factored form. Suppose $$\tfrac{dP}{dt} = 2P-0.02P^2$$, which factors as $$\tfrac{dP}{dt} = 0.02P(100-P)$$, and now the structure is visible.

The carrying capacity is $$100$$, the fastest growth occurs at $$P=50$$, and the maximum growth rate is $$0.02(50)(50)=50$$. If $$P$$ is measured in thousands of fish and $$t$$ in years, that means the population grows fastest at 50 thousand fish, at a rate of 50 thousand fish per year. The units come from the context, not from the algebra alone.

## Initial values outside the usual range

Most population examples begin with $$0<y_0<a$$. The differential equation also tells us what happens outside that range. If $$y>a$$, then $$a-y<0$$, so $$y'<0$$ and the solution decreases toward the carrying capacity. If $$y=0$$ or $$y=a$$, the solution remains constant, and these conclusions come from the sign of the differential equation itself.

<div class="article-note" markdown="1">
Before solving a logistic equation, factor it and identify:

- the equilibrium values
- the carrying capacity
- the sign of the growth rate
- the point of fastest growth
- the concavity change

Often that is most of what the problem is asking for.
</div>
