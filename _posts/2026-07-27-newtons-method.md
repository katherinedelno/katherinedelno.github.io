---
layout: post
title: "Newton's method and its basins of attraction"
date: 2026-07-27
description: "Newton's method turns tangent lines into an iterative root-finding algorithm. For functions with several roots, the starting value can determine which root the method finds."
course: "AP Calculus AB & BC"
read_time: "6 min read"
math: true
kind: beyond
sequence: 1
interactive: true
blurb: "Newton's method turns tangent lines into an iterative root-finding algorithm. For functions with several roots, the starting value can determine which root the method finds"
featured: true
image: "/assets/og/newtons-method.png"
---

A tangent line can do more than approximate a function near one point.

It can also be used to search for a root.

Newton's method begins with a guess $$x_0$$, draws the tangent line there, and uses the tangent line's $$x$$-intercept as the next guess.

The process repeats.

## From one guess to the next

For a differentiable function $$f$$, the tangent line at $$x_n$$ is

$$y = f(x_n)+f'(x_n)(x-x_n).$$

Set $$y=0$$ to find where that tangent line crosses the axis:

$$0 = f(x_n)+f'(x_n)(x_{n+1}-x_n).$$

Solving for the next guess gives

$$x_{n+1} = x_n-\frac{f(x_n)}{f'(x_n)}.$$

That is Newton's method.

The formula is simply a tangent-line calculation repeated.

## Try the iteration

Consider

$$f(x)=x^3-x.$$

Its roots are

$$-1,\quad0,\quad1.$$

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
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
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

The visualization shows each tangent line and the next $$x$$-intercept it produces.

For many starting values, the iterates settle quickly toward one of the three roots.

Near a root, the convergence can be extremely fast.

For a simple root $$r$$, and under the usual smoothness conditions, Newton's method has quadratic convergence once the guesses are sufficiently close.

Roughly, this means the number of correct digits can double from one iteration to the next.

## The starting value matters

With several roots, the method does not know which one you intend to find.

The starting value determines the path.

The strip below the graph colors each possible starting point according to the root reached by the iteration.

Large regions lead consistently to one root.

The boundaries between those regions are more complicated.

Move the starting value slowly across one of those boundaries.

A very small change can send the iteration to a different root.

This is not numerical randomness.

The algorithm is deterministic.

The sensitivity comes from the geometry of the tangent lines.

## What happens near a horizontal tangent

For

$$f(x)=x^3-x,$$

the derivative is

$$f'(x)=3x^2-1.$$

It is zero at

$$x=\pm\frac{1}{\sqrt3}.$$

Near those values, the denominator in

$$x_{n+1} = x_n-\frac{f(x_n)}{f'(x_n)}$$

is very small.

The next Newton step can therefore be very large.

At the exact points where $$f'(x)=0$$, the formula is undefined.

This explains much of the irregular behavior near the basin boundaries.

A nearly horizontal tangent can cross the $$x$$-axis very far from the current point.

The next guess may then land in a completely different part of the graph.

## Newton's method is not guaranteed to succeed

The method can fail in several ways.

The derivative can be zero.

The iterates can cycle rather than converge.

A poor starting value can send the sequence away from the root of interest.

For some functions, a root can have a very small basin of attraction.

So Newton's method is powerful, but it is not a theorem that every initial guess converges.

In numerical analysis, root-finding algorithms are studied partly by asking when convergence is guaranteed and how quickly it occurs.

## The complex plane

The basin picture becomes especially interesting when Newton's method is applied to complex numbers.

For

$$f(z)=z^3-1,$$

there are three complex roots of unity.

Every starting point in the complex plane can be colored according to which root Newton's method reaches.

The boundaries between the three basins form a fractal.

At every scale, points leading to different roots remain interwoven near the boundary.

These boundaries are related to Julia sets in complex dynamics.

The same one-line iteration therefore connects tangent-line approximation, numerical analysis, and dynamical systems.

None of that changes the basic mechanism.

At every step, the algorithm replaces the function locally with a tangent line and follows that line to the axis.

## A useful way to read the method

Newton's method is worth understanding even when a calculator or computer performs the iterations.

It shows how local information can drive a global search.

At one point, the derivative tells us only the slope of the function nearby.

Repeatedly updating that local approximation can nevertheless locate a root far from the original guess.

<div class="article-note" markdown="1">
The method also gives a useful warning. An algorithm can be deterministic and still be highly sensitive to where it starts.
</div>
