---
layout: post
title: "After BC: differential equations"
date: 2026-07-26
description: "Differential equations model systems by specifying how their state changes. The college course moves from single equations to systems, phase analysis, oscillation, and numerical solutions."
course: "AP Calculus BC"
section: beyond
read_time: "8 min read"
math: true
kind: beyond
sequence: 7
interactive: true
blurb: "Differential equations model systems by specifying how their state changes. The college course moves from single equations to systems, phase analysis, oscillation, and numerical solutions"
image: "/assets/og/beyond-bc-differential-equations.png"
---

A differential equation specifies how an unknown quantity changes, and that is often how scientific models are written. Newton's second law relates acceleration to force, population models describe growth through a rate equation, and heat transfer depends on temperature differences. In each case, the equation gives a rule for change and the solution describes the resulting behavior.

BC introduces several parts of this subject through separable equations, slope fields, logistic growth, and Euler's method, and a full differential equations course develops those ideas much further.

## From one equation to a system

The equations in BC usually involve one unknown function, but many models involve several quantities changing together. A standard example is an epidemic model. Divide a population into susceptible people $$S$$, infected people $$I$$, and recovered people $$R$$, and one version of the SIR model is

$$\begin{aligned}
\frac{dS}{dt} &= -\beta\frac{SI}{N}\\
\frac{dI}{dt} &= \beta\frac{SI}{N}-\gamma I\\
\frac{dR}{dt} &= \gamma I
\end{aligned}$$

The equations describe flows between the three groups. New infections move people from $$S$$ to $$I$$, and recoveries move people from $$I$$ to $$R$$. The variables are linked, so the equations have to be analyzed as a system.

## Steer an outbreak

The simulation starts with a population of 1,000 and 5 infected individuals, and the recovery rate is fixed at $$\gamma=0.1$$.

<div class="viz" markdown="0">
  <canvas id="sir-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="sir-b">Transmission β</label>
    <input type="range" id="sir-b" min="5" max="50" step="1" value="25">
    <span class="viz-value" id="sir-read"></span>
  </div>
  <p class="viz-caption">Light gray: susceptible. Black: currently infected. Medium gray: recovered. Watch the quantity R&#8320; = β/γ, the average number of people each infected person infects. Below 1, the outbreak fizzles without ever taking off. Above 1, it grows into a wave, and the higher R&#8320; climbs, the taller and earlier the peak. Slide β down and watch the peak flatten: that phrase from recent memory is a statement about this exact curve. Notice also that the outbreak always ends before everyone is infected; it dies when S drops low enough that each case can no longer replace itself.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('sir-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('sir-b'), read = document.getElementById('sir-read');
  var W = cv.width, H = cv.height, pad = 34;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var N = 1000, GAMMA = 0.1, DAYS = 200, DT = 0.25;
  function px(t){ return pad + (t/DAYS)*(W - 2*pad); }
  function py(v){ return H - pad - (v/N)*(H - 2*pad); }
  function draw(){
    var beta = slider.value/100;
    c.clearRect(0, 0, W, H);
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(pad, py(0)); c.lineTo(W - pad, py(0)); c.stroke();
    c.beginPath(); c.moveTo(pad, py(0)); c.lineTo(pad, py(N)); c.stroke();
    var S = N - 5, I = 5, R = 0;
    var sPts = [], iPts = [], rPts = [], peak = I, peakT = 0;
    for(var t = 0; t <= DAYS; t += DT){
      sPts.push([t, S]); iPts.push([t, I]); rPts.push([t, R]);
      if(I > peak){ peak = I; peakT = t; }
      var newInf = beta*S*I/N*DT, newRec = GAMMA*I*DT;
      S -= newInf; I += newInf - newRec; R += newRec;
    }
    function plot(pts, color, wdt){
      c.strokeStyle = color; c.lineWidth = wdt; c.beginPath();
      for(var i = 0; i < pts.length; i++){
        i ? c.lineTo(px(pts[i][0]), py(pts[i][1])) : c.moveTo(px(pts[i][0]), py(pts[i][1]));
      }
      c.stroke();
    }
    plot(sPts, '#d0d0cd', 2);
    plot(rPts, '#9a9a97', 2);
    plot(iPts, '#1f1f1f', 2.5);
    var r0 = beta/GAMMA;
    read.textContent = 'R₀ = ' + r0.toFixed(1) + '   peak infected: ' + Math.round(peak) + (peak > 6 ? ' on day ' + Math.round(peakT) : ' (no outbreak)');
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

The curves show the susceptible, infected, and recovered populations over time. The ratio $$R_0=\tfrac{\beta}{\gamma}$$ describes the expected number of secondary infections produced by one infected individual in a fully susceptible population under this simplified model. When $$R_0<1$$, the infection cannot sustain initial exponential growth, and when $$R_0>1$$, an outbreak can grow. Increasing $$\beta$$ makes the infected curve rise earlier and reach a higher peak.

The simulation is computed numerically, and no closed-form solution is required to study the system's behavior.

## Qualitative analysis

A large part of differential equations is qualitative. Instead of asking only for an explicit formula, we ask:

- Where are the equilibria?
- Which equilibria are stable?
- Does a solution approach a steady state?
- Does it oscillate?
- How does changing a parameter alter the behavior?

BC already uses this kind of reasoning in logistic growth. If $$\tfrac{dP}{dt}=kP(K-P)$$, we can identify the equilibria and long-run behavior directly from the sign of the right-hand side, and a differential equations course turns that reasoning into a systematic method.

## Phase lines and phase planes

For one autonomous equation, a phase line shows the direction in which solutions move. For a system, the state has several coordinates, and a phase plane can plot one state variable against another. The trajectory then shows how the entire system evolves without using time as an axis.

Equilibria appear as fixed points, and nearby trajectories may move toward them, move away, or circulate around them. This geometric viewpoint is particularly useful for systems whose explicit solutions are difficult or unavailable.

## Why sine and cosine appear in physical models

Consider a mass attached to a spring. Under a simple restoring-force model,

$$\frac{d^2x}{dt^2} = -\omega^2x$$

We are looking for functions whose second derivative is the negative of the original function, up to a constant factor, and sine and cosine have exactly that property. The general solution is $$x(t) = A\cos(\omega t) + B\sin(\omega t)$$, so the oscillation is a consequence of the differential equation.

Adding a damping term produces oscillations whose amplitude decreases over time, and related equations appear in mechanics, circuits, acoustics, and many other physical systems.

## Numerical methods become central

Most differential equations do not have elementary closed-form solutions, but that does not make them unusable. Numerical methods approximate the solution directly, and [Euler's method](/2026/07/25/euler-method-step-size.html) is the simplest example. More accurate methods update the solution using additional information within each step.

The SIR simulation above uses numerical integration for exactly this reason. The important question becomes whether the numerical approximation is accurate and stable enough for the problem being studied.

## Sensitivity and chaos

Some nonlinear systems are extremely sensitive to their initial conditions, and two solutions that begin very close together can eventually separate dramatically. This phenomenon is one feature of deterministic chaos.

The Lorenz system is a classical example. Its equations are fully deterministic, and the unpredictability comes from sensitivity to initial conditions rather than from random input. This is one reason long-term prediction can be difficult even when the governing equations are known.

## What carries over from BC

Differential equations is one of the most direct continuations of BC. Separable equations, exponential and logistic models, Euler's method, slope fields, Taylor series, and integration techniques all return. Linear algebra also becomes increasingly important because systems of differential equations can often be understood through matrices and eigenvalues.

<div class="article-note" markdown="1">
A useful question in the epidemic simulation is to identify the moment when the infected population stops increasing, which is the point where $$\tfrac{dI}{dt}=0$$. Using the model equation shows that the turning point occurs when the susceptible fraction reaches a threshold determined by $$R_0$$, and the simulation makes that qualitative statement visible.
</div>
