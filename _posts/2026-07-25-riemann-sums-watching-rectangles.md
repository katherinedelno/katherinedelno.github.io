---
layout: post
title: "Riemann sums and the definition of the integral"
date: 2026-07-25
description: "A definite integral is the limit of approximating sums. Left, right, midpoint, and trapezoidal estimates differ only in how each slice is represented."
course: "AP Calculus AB"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "6 min read"
math: true
kind: foundations
sequence: 20
interactive: true
blurb: "A definite integral is the limit of approximating sums. Left, right, midpoint, and trapezoidal estimates differ only in how each slice is represented"
image: "/assets/og/riemann-sums-watching-rectangles.png"
---

Before the [Fundamental Theorem](/2026/07/17/fundamental-theorem-from-the-ground-up.html) gives a convenient way to evaluate many definite integrals, the integral has a definition.

Partition an interval into smaller pieces. Approximate the contribution from each piece. Add the contributions. Then let the partition become arbitrarily fine.

For a continuous function,

$$\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{k=1}^{n} f(x_k^*)\Delta x.$$

Here $$\Delta x$$ is the width of a subinterval and $$x_k^*$$ is the point used to choose the rectangle height.

## Watching the sums converge

Consider

$$f(x)=x^2+1$$

on

$$[0,3].$$

Its exact integral is

$$\int_0^3(x^2+1)\,dx = 12.$$

<div class="viz" markdown="0">
  <canvas id="rs-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="rs-n">Rectangles</label>
    <input type="range" id="rs-n" min="2" max="80" step="1" value="6">
    <button type="button" id="rs-left" class="res-filter is-active" style="font-size:.72rem">Left</button>
    <button type="button" id="rs-right" class="res-filter" style="font-size:.72rem">Right</button>
    <span class="viz-value" id="rs-read"></span>
  </div>
  <p class="viz-caption">With a handful of rectangles the error is visible as the white gaps (left sum) or the gray overhangs (right sum). By n = 80 the rectangles are nearly indistinguishable from the region itself, and the sum is within about two tenths of 12. The left sum reads 11.832 and the right 12.169, still bracketing the exact value from either side. The limit in the definition is this picture carried to completion.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('rs-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('rs-n'), read = document.getElementById('rs-read');
  var btnL = document.getElementById('rs-left'), btnR = document.getElementById('rs-right');
  var mode = 'left';
  var W = cv.width, H = cv.height, pad = 34;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var A = 0, B = 3, YMAX = 10.6;
  function f(x){ return x*x + 1; }
  function px(x){ return pad + (x - A)/(B - A)*(W - 2*pad); }
  function py(y){ return H - pad - (y/YMAX)*(H - 2*pad); }
  function draw(){
    var n = +slider.value, dx = (B - A)/n, sum = 0, k;
    c.clearRect(0, 0, W, H);
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(px(A), py(0)); c.lineTo(px(B), py(0)); c.stroke();
    c.beginPath(); c.moveTo(px(A), py(0)); c.lineTo(px(A), py(YMAX)); c.stroke();
    for(k = 0; k < n; k++){
      var x0 = A + k*dx, xs = (mode === 'left') ? x0 : x0 + dx, h = f(xs);
      sum += h*dx;
      c.fillStyle = '#dcdcd9';
      c.fillRect(px(x0), py(h), px(x0+dx)-px(x0), py(0)-py(h));
      c.strokeStyle = '#a7a7a3'; c.lineWidth = 1;
      c.strokeRect(px(x0), py(h), px(x0+dx)-px(x0), py(0)-py(h));
    }
    c.strokeStyle = '#1f1f1f'; c.lineWidth = 2.5; c.beginPath();
    for(k = 0; k <= 300; k++){
      var x = A + (B - A)*k/300, Y = py(f(x));
      k ? c.lineTo(px(x), Y) : c.moveTo(px(x), Y);
    }
    c.stroke();
    read.textContent = (mode === 'left' ? 'Left' : 'Right') + ' sum = ' + sum.toFixed(3) + '  (exact: 12)';
  }
  btnL.addEventListener('click', function(){ mode = 'left'; btnL.classList.add('is-active'); btnR.classList.remove('is-active'); draw(); });
  btnR.addEventListener('click', function(){ mode = 'right'; btnR.classList.add('is-active'); btnL.classList.remove('is-active'); draw(); });
  slider.addEventListener('input', draw);
  draw();
})();
</script>

With a small number of rectangles, the difference between the sum and the curved region is obvious.

As $$n$$ increases, the approximation improves.

For this increasing function, the left sum remains below the exact value and the right sum remains above it.

At $$n=80$$, the two estimates are already close to 12.

The limit in the definition is what happens as the number of subintervals continues without bound.

## Why left and right sums behave differently

On an interval where $$f$$ is increasing, the left endpoint gives the smallest function value on each subinterval.

So each left rectangle lies below the curve.

The left Riemann sum is therefore an underestimate.

The right endpoint gives the largest value on each subinterval, so the right sum is an overestimate.

If $$f$$ is decreasing, the roles reverse.

This reasoning is more useful than memorizing a table.

The direction of the error for left and right sums comes from whether the function is increasing or decreasing.

For midpoint and trapezoidal approximations, concavity becomes relevant instead.

## Riemann sums from a table

A formula for the function is not required.

Suppose a rate $$R(t)$$ is given by the table:

| $$t$$ (hours) | 0 | 2 | 5 | 8 | 9 |
|---|---|---|---|---|---|
| $$R(t)$$ (liters/hour) | 40 | 46 | 58 | 52 | 48 |

A left Riemann sum for

$$\int_0^9R(t)\,dt$$

uses the left value on each subinterval:

$$40(2)+46(3)+58(3)+52(1).$$

This gives

$$444$$

liters.

The widths are not equal, so each one must be read from the table.

The units also matter.

A rate measured in liters per hour multiplied by time in hours gives liters.

So the integral represents the accumulated quantity over the interval.

## Why the definition still matters

Antiderivatives provide an efficient evaluation method when they are available.

But many functions do not have elementary antiderivatives, and many datasets are given only numerically.

The Riemann-sum idea still applies in those settings.

Integration is fundamentally accumulation.

The antiderivative method is a theorem that connects that accumulation to differentiation.

<div class="article-note" markdown="1">
A useful check is to decide the direction of a trapezoidal approximation without computing it.

For

$$f(x)=x^2+1,$$

the function is concave up.

The line segment joining two points on a concave-up curve lies above the curve.

So a trapezoidal sum overestimates the integral.

That conclusion comes from the geometry of one subinterval. No chart is necessary.
</div>
