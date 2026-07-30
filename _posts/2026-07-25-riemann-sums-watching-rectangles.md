---
layout: post
title: "Riemann sums and the definition of the integral"
date: 2026-07-25
description: "The definite integral is defined by rectangles. This article watches the definition converge, and explains why left and right sums bracket the true value."
course: "AP Calculus AB"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "6 min read"
math: true
kind: foundations
sequence: 5
interactive: true
blurb: "Watch the definition converge, and see why left and right sums bracket it"
---

Before the Fundamental Theorem gives you a shortcut, the definite integral has a definition, and the definition is rectangles. To estimate the area under a curve, slice the interval into $$n$$ pieces, stand a rectangle on each piece, and add up the rectangle areas. The definite integral is what those sums approach as the slicing gets finer:

$$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{k=1}^{n} f\!\left(x_k^*\right)\Delta x.$$

The formula reads better as a recipe. $$\Delta x$$ is the width of each slice. The point $$x_k^*$$ is where you measure the height of the $$k$$-th rectangle: the left edge gives a left Riemann sum, and the right edge gives a right sum. The sigma adds the areas, and the limit sends the number of rectangles to infinity.

## Try it

The curve below is $$f(x) = x^2 + 1$$ on $$[0,3]$$, whose exact area is $$\int_0^3 (x^2+1)\,dx = 12$$. Slide $$n$$ and watch the rectangle total approach 12.

<div class="viz" markdown="0">
  <canvas id="rs-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="rs-n">Rectangles</label>
    <input type="range" id="rs-n" min="2" max="80" step="1" value="6">
    <button type="button" id="rs-left" class="res-filter is-active" style="font-size:.72rem">Left</button>
    <button type="button" id="rs-right" class="res-filter" style="font-size:.72rem">Right</button>
    <span class="viz-value" id="rs-read"></span>
  </div>
  <p class="viz-caption">With a handful of rectangles the error is visible as the white gaps (left sum) or the gray overhangs (right sum). By n = 80 the rectangles are nearly indistinguishable from the region itself, and the sum is within a few hundredths of 12. The limit in the definition is this picture carried to completion.</p>
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

## Why left and right sums bracket the truth

On this interval the function is increasing, and that single fact settles the direction of every error. A left rectangle measures its height at the left edge, where an increasing function is at its smallest on the slice, so each left rectangle sits below the curve and the left sum is an underestimate. A right rectangle measures where the function is largest on the slice, so the right sum is an overestimate. The exact area is trapped between them, and as $$n$$ grows the trap tightens.

The exam asks for exactly this reasoning, and it wants the hypothesis stated. The sentence that earns the point is: "the left Riemann sum is an underestimate because $$f$$ is increasing on the interval." For a decreasing function the roles flip. Note carefully which fact controls which method: increasing or decreasing controls left and right sums. Concavity controls two different methods, the midpoint sum and the trapezoidal sum. Students who memorize a four-way chart mix these up under pressure; students who picture one rectangle on one slice never do.

## Sums from tables

On the free-response section, Riemann sums usually arrive with a table instead of a formula, and with unequal widths:

| $$t$$ (hours) | 0 | 2 | 5 | 8 | 9 |
|---|---|---|---|---|---|
| $$R(t)$$ (liters/hour) | 40 | 46 | 58 | 52 | 48 |

A left Riemann sum for $$\int_0^9 R(t)\,dt$$ uses each subinterval's left value times its width:

$$40(2) + 46(3) + 58(3) + 52(1) = 444 \text{ liters}.$$

Two habits keep this clean. First, the widths come from the table and are not equal, so resist any formula with a single $$\Delta x$$. Second, the units of the answer are the product of the two axis units, here liters per hour times hours. Saying what the number means, the total liters that entered over the nine hours, is typically its own scoring point.

## The definition still matters after the shortcut

Once the Fundamental Theorem arrives, it is tempting to file rectangles away as scaffolding. The exam disagrees, for a reason worth respecting: many real functions have no antiderivative formula, and many real data sets have no formula at all, like the table above. Rectangle sums are not the primitive version of integration. They are what integration is, and the antiderivative shortcut is the special case that works when a formula happens to exist.

<div class="article-note" markdown="1">
A self-test: without computing either sum, decide whether the trapezoidal estimate of $$\int_0^3 (x^2+1)\,dx$$ is an overestimate or an underestimate. The answer depends on concavity alone. Since $$f$$ is concave up, each trapezoid's slanted top lies above the curve, so the trapezoidal sum overestimates. If that argument feels natural, the four-way chart is yours without memorizing it.
</div>
