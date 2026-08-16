---
layout: post
title: "Euler's method and the effect of step size"
date: 2026-07-25
description: "Euler's method follows a differential equation one tangent-line step at a time. Smaller steps usually reduce the accumulated error."
course: "AP Calculus BC"
read_time: "6 min read"
math: true
kind: foundations
sequence: 25
interactive: true
blurb: "Euler's method follows a differential equation one tangent-line step at a time. Smaller steps usually reduce the accumulated error"
image: "/assets/og/euler-method-step-size.png"
---

A differential equation gives a slope.

Euler's method uses that slope to move a short distance, then recomputes the slope and moves again.

If

$$ \frac{dy}{dx}=F(x,y), $$

then one Euler step is

$$ y_{\text{new}} = y+F(x,y)\Delta x. $$

The method replaces a curve with a sequence of short tangent-line approximations.

## A first example

Consider

$$ \frac{dy}{dx}=y, \qquad y(0)=1. $$

The exact solution is

$$ y=e^x. $$

Suppose the step size is

$$ \Delta x=0.5. $$

At the starting point,

$$ (0,1), $$

the slope is

$$ y=1. $$

So

$$ y(0.5) \approx 1+1(0.5) = 1.5. $$

Now recompute the slope at the new approximate point.

The slope is approximately

$$ 1.5. $$

So

$$ y(1) \approx 1.5+1.5(0.5) = 2.25. $$

The exact value is

$$ e\approx2.718. $$

The approximation is low.

## Step size matters

<div class="viz" markdown="0">
  <canvas id="eu-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="eu-h">Step size</label>
    <input type="range" id="eu-h" min="1" max="40" step="1" value="4">
    <span class="viz-value" id="eu-read"></span>
  </div>
  <p class="viz-caption">With two big steps the path lands far below the curve, at 4 against a true 7.389. With forty small steps it closes most of that gap, reaching 7.040: the error has fallen from about 3.4 to about 0.35. Note that it is still short, and visibly so at the right-hand edge, because a twentyfold cut in step size buys only about a twentyfold cut in error. The dots mark the points Euler's method actually computes; the segments between them are the tangent lines it walks along. Notice that every path sits below the gray curve. That is not an accident, and the reason is a scoring point on the exam.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('eu-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('eu-h'), read = document.getElementById('eu-read');
  var W = cv.width, H = cv.height, pad = 34;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var X1 = 2, YMAX = 8.2;
  function px(x){ return pad + (x/X1)*(W - 2*pad); }
  function py(y){ return H - pad - (y/YMAX)*(H - 2*pad); }
  function draw(){
    var steps = +slider.value, h = X1/steps;
    c.clearRect(0, 0, W, H);
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(px(0), py(0)); c.lineTo(px(X1), py(0)); c.stroke();
    c.beginPath(); c.moveTo(px(0), py(0)); c.lineTo(px(0), py(YMAX)); c.stroke();
    // true solution e^x
    c.strokeStyle = '#c4c4c4'; c.lineWidth = 2.5; c.beginPath();
    for(var i = 0; i <= 300; i++){
      var x = X1*i/300, Y = py(Math.exp(x));
      i ? c.lineTo(px(x), Y) : c.moveTo(px(x), Y);
    }
    c.stroke();
    // Euler path
    var xs = 0, ys = 1;
    c.strokeStyle = '#1f1f1f'; c.lineWidth = 2; c.beginPath(); c.moveTo(px(0), py(1));
    var pts = [[0,1]];
    for(var k = 0; k < steps; k++){
      ys = ys + ys*h;    // dy/dx = y
      xs = xs + h;
      pts.push([xs, ys]);
      c.lineTo(px(xs), py(Math.min(ys, YMAX+1)));
    }
    c.stroke();
    c.fillStyle = '#1f1f1f';
    if(steps <= 20){
      for(var j = 0; j < pts.length; j++){
        c.beginPath(); c.arc(px(pts[j][0]), py(Math.min(pts[j][1], YMAX+1)), 3.5, 0, 7); c.fill();
      }
    }
    read.textContent = 'Euler y(2) = ' + ys.toFixed(3) + '  (true: ' + Math.exp(2).toFixed(3) + ')';
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

The visualization compares Euler approximations for the same differential equation using different step sizes.

With a large step, each tangent line is followed for a relatively long distance before the slope is updated.

With a smaller step, the slope is recomputed more often.

The approximation usually improves.

For this equation, the error is systematic. Since

$$ y''=y>0, $$

the solution is concave up.

A tangent line to a concave-up curve lies below the curve locally.

Euler's method therefore produces an underestimate as it moves to the right.

The sign of the error is not a universal feature of Euler's method. It depends on the concavity of the solution.

## Recompute every slope

A common mistake is to calculate the initial slope once and reuse it for every step.

That would produce one tangent line, not Euler's method.

Each new point gives a new value of

$$ F(x,y), $$

so the slope must be recomputed.

A table is often the cleanest way to organize the process.

| Step | $$x$$ | $$y$$ | slope $$F(x,y)$$ |
|---|---|---|---|
| 0 | 0 | 1 | 1 |
| 1 | 0.5 | 1.5 | 1.5 |
| 2 | 1.0 | 2.25 | 2.25 |

The value in one row becomes the starting point for the next.

## How quickly the error falls

Euler's method is a first-order method.

Over a fixed interval, halving the step size typically reduces the global error by roughly a factor of two when the solution is sufficiently smooth.

This is slower than higher-order numerical methods, but Euler's method has an important advantage for learning.

Its geometry is completely visible.

Each step says:

start at the current point, use the differential equation to find the tangent slope, and follow that tangent for a short distance.

## A useful self-test

Consider

$$ \frac{dy}{dx}=-y, \qquad y(0)=4. $$

With step size

$$ \Delta x=1, $$

Euler's method gives

$$ y(1) \approx 4+(-4)(1) = 0. $$

The exact solution is

$$ y=4e^{-x}, $$

so

$$ y(1)\approx1.47. $$

The Euler estimate is again low.

Here,

$$ y''=y>0, $$

so the exact solution is concave up even though it is decreasing.

<div class="article-note" markdown="1">
That is enough to explain the direction of the tangent-line error.
</div>
