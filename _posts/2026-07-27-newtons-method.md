---
layout: post
title: "Newton's method and its basins of attraction"
date: 2026-07-27
description: "Tangent lines turn a guess into a root with astonishing speed, until the starting point crosses an invisible boundary. An iteration to steer, and the fractal structure hiding in it."
course: "AP Calculus AB & BC"
read_time: "7 min read"
math: true
---

A tangent line is the best straight substitute for a curve at a point. Newton's method takes that sentence seriously and turns it into an algorithm: to solve $$f(x) = 0$$, make a guess, replace the curve by its tangent line at the guess, and solve the tangent line's root instead, which is easy because lines are easy. The answer becomes the next guess, and the process repeats. Algebraically, one step reads

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

The method is no longer tested on the AP exams, but it deserves a place in any calculus student's education for two reasons. It is the single most vivid application of the tangent-line idea, the same local linearity that underlies linearization in Unit 4. And it hides, just beneath a placid surface, one of the doorways into fractal geometry.

## The iteration, watched

The curve below is $$f(x) = x^3 - x$$, with roots at $$-1$$, $$0$$, and $$1$$. Choose a starting point and watch the tangent lines hunt.

<div class="viz" markdown="0">
  <canvas id="nm-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="nm-x0">Starting point</label>
    <input type="range" id="nm-x0" min="-200" max="200" step="1" value="130">
    <span class="viz-value" id="nm-read"></span>
  </div>
  <p class="viz-caption">Each gray segment is a tangent line; each drop to the axis is one iteration. From most starting points the method converges with remarkable speed, roughly doubling the number of correct decimal places at every step. The strip beneath the axis colors every starting point by the root it eventually finds: dark for the root at 1, medium for 0, light for the root at negative 1. Slide slowly through the region near 0.45 and watch the outcome flicker between distant roots as the strip's bands crowd together. Near the points where the tangent line goes horizontal, the method's first step is enormous, and the question of where a starting point ultimately lands becomes delicate without limit.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('nm-cv'), c = cv.getContext('2d');
  var sl = document.getElementById('nm-x0'), read = document.getElementById('nm-read');
  var W = cv.width, H = cv.height;
  var XMIN = -2, XMAX = 2, YMIN = -2.2, YMAX = 2.2;
  var AXH = H - 46;
  function px(x){ return (x - XMIN)/(XMAX - XMIN)*W; }
  function py(y){ return AXH/2 - y*(AXH/2 - 12)/Math.abs(YMIN); }
  function f(x){ return x*x*x - x; }
  function fp(x){ return 3*x*x - 1; }
  function rootOf(x0){
    var x = x0;
    for(var i = 0; i < 60; i++){
      var d = fp(x);
      if(Math.abs(d) < 1e-12) return null;
      x = x - f(x)/d;
      if(!isFinite(x) || Math.abs(x) > 1e6) return null;
    }
    if(Math.abs(x - 1) < 1e-3) return 1;
    if(Math.abs(x) < 1e-3) return 0;
    if(Math.abs(x + 1) < 1e-3) return -1;
    return null;
  }
  function basinColor(r){
    if(r === 1) return '#1f1f1f';
    if(r === 0) return '#8a8a87';
    if(r === -1) return '#d6d6d3';
    return '#ffffff';
  }
  function drawBasins(){
    for(var p = 0; p < W; p++){
      var x0 = XMIN + (XMAX - XMIN)*p/W;
      c.fillStyle = basinColor(rootOf(x0));
      c.fillRect(p, H - 30, 1, 18);
    }
    c.strokeStyle = '#e0e0e0'; c.strokeRect(0.5, H - 30.5, W - 1, 18);
  }
  function draw(){
    var x0 = sl.value/100;
    c.clearRect(0, 0, W, H - 34);
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(0, py(0)); c.lineTo(W, py(0)); c.stroke();
    c.strokeStyle = '#b5b5b2'; c.lineWidth = 2;
    c.beginPath();
    for(var x = XMIN; x <= XMAX; x += 0.005){
      var X = px(x), Y = py(Math.max(Math.min(f(x), 2.4), -2.4));
      x === XMIN ? c.moveTo(X, Y) : c.lineTo(X, Y);
    }
    c.stroke();
    var xn = x0, path = [xn];
    for(var i = 0; i < 12; i++){
      var d = fp(xn);
      if(Math.abs(d) < 1e-9) break;
      var next = xn - f(xn)/d;
      c.strokeStyle = 'rgba(31,31,31,0.45)'; c.lineWidth = 1.1;
      c.beginPath(); c.moveTo(px(xn), py(f(xn))); c.lineTo(px(next), py(0)); c.stroke();
      c.beginPath(); c.moveTo(px(next), py(0)); c.lineTo(px(next), py(f(next))); c.stroke();
      xn = next; path.push(xn);
      if(Math.abs(xn) > 2.6) break;
      if(Math.abs(f(xn)) < 1e-10) break;
    }
    c.fillStyle = '#1f1f1f';
    c.beginPath(); c.arc(px(x0), py(f(x0)), 3.4, 0, 7); c.fill();
    var r = rootOf(x0);
    read.textContent = 'start ' + x0.toFixed(2) + (r === null ? ':  no convergence within tolerance' : ':  converges to ' + r + ' after ' + Math.min(path.length - 1, 60) + ' visible steps');
  }
  drawBasins();
  sl.addEventListener('input', draw);
  draw();
})();
</script>

## Why the convergence is so fast

When Newton's method works, it works extravagantly well. Near a root where $$f'$$ is not zero, each iteration approximately squares the error: an answer correct to 3 decimal places becomes correct to 6, then to 12. This behavior, called quadratic convergence, is why the method and its descendants sit inside calculators, GPS receivers, and the training loops of machine learning, where some version of "follow the local linear approximation downhill" is executed billions of times a day. The tangent line is not merely a geometric ornament; it is the workhorse of numerical computation.

The failures are as instructive as the successes. If an iterate lands where $$f'(x) = 0$$, the tangent line is horizontal and never reaches the axis. Land merely near such a point, and the tangent line is nearly horizontal, catapulting the next guess far away, which is exactly the behavior visible near $$x = \pm 0.577$$ in the interactive. A method built on local information inherits local blind spots, and knowing an algorithm's failure modes is as much a part of numerical literacy as knowing its speed.

## The fractal at the boundary

The colored strip beneath the axis records, for every starting point, which root the method ultimately finds. Each root owns a large connected territory, its basin of attraction, but between territories the bands fragment: zoom toward a boundary and bands of all three shades reappear at every magnification, an infinite interleaving in which arbitrarily close starting points commit to different roots.

The full picture requires one more dimension. In 1879 Arthur Cayley asked the same question for complex starting points, and could not answer it for the cubic. The reason, invisible for another century, is that the basin boundaries in the complex plane are fractals: infinitely intricate filigrees, now called Julia sets, in which the three basins tangle so completely that every boundary point touches all three territories at once. Newton's method for $$z^3 - 1$$ produces one of the most reproduced mathematical images ever made, and it comes from nothing more exotic than the tangent-line formula above, applied honestly and asked a fair question.

<div class="article-note" markdown="1">
An experiment at the slider: start at 0.44 and then at 0.46, and note the destinations. Then find a pair of starting points, as close together as one slider step, that land at different roots. Sensitivity of outcomes to initial conditions, appearing in a deterministic formula built from a cubic polynomial, is the same phenomenon that limits weather prediction, met here in its most inspectable form.
</div>
