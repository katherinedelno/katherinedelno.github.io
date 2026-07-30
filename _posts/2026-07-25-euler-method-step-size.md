---
layout: post
title: "Euler's method and the effect of step size"
date: 2026-07-25
description: "The method advances along tangent lines. This article examines what a smaller step purchases, why the path undershoots a concave-up solution, and what the exam asks of the technique."
course: "AP Calculus BC"
read_time: "6 min read"
math: true
kind: foundations
sequence: 7
interactive: true
blurb: "What a smaller step purchases, and why the path undershoots a concave-up solution"
---

A differential equation tells you the slope of a solution curve at every point, but not the curve itself. Euler's method turns that slope information into a curve the most direct way imaginable: stand at the initial point, walk a short distance along the tangent line, look up the new slope where you land, and repeat. Each step uses the update

$$y_{\text{new}} = y + \frac{dy}{dx}\cdot \Delta x,$$

where the slope $$\tfrac{dy}{dx}$$ is computed from the differential equation at the current point. The result is a broken-line path that approximates the true solution, and the quality of the approximation is controlled by one number: the step size.

## Try it

The differential equation below is $$\tfrac{dy}{dx} = y$$ with $$y(0) = 1$$, whose exact solution is $$y = e^x$$. The gray curve is the truth. The black path is Euler's method from $$x = 0$$ to $$x = 2$$. Slide the step size and watch the path bend toward the curve.

<div class="viz" markdown="0">
  <canvas id="eu-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="eu-h">Step size</label>
    <input type="range" id="eu-h" min="1" max="40" step="1" value="4">
    <span class="viz-value" id="eu-read"></span>
  </div>
  <p class="viz-caption">With two big steps the path lands far below the curve. With forty small steps it hugs the curve almost perfectly. The dots mark the points Euler's method actually computes; the segments between them are the tangent lines it walks along. Notice that every path sits below the gray curve. That is not an accident, and the reason is a scoring point on the exam.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('eu-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('eu-h'), read = document.getElementById('eu-read');
  var W = cv.width, H = cv.height, pad = 34;
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

## The computation, by hand

The exam version uses two or three steps and asks you to show the arithmetic. Approximating $$y(1)$$ for $$\tfrac{dy}{dx} = y$$, $$y(0) = 1$$, with two steps of size $$0.5$$:

At $$(0, 1)$$: the slope is $$y = 1$$, so $$y(0.5) \approx 1 + (1)(0.5) = 1.5$$.

At $$(0.5, 1.5)$$: the slope is $$y = 1.5$$, so $$y(1) \approx 1.5 + (1.5)(0.5) = 2.25$$.

The true value is $$e \approx 2.718$$, so two big steps landed well short. A table with columns for the point, the slope there, and the new value keeps the bookkeeping honest, and it shows the grader every number the rubric is looking for. The most common arithmetic slip is reusing the old slope for the second step: the slope must be recomputed at each new point, because that is the entire content of the method.

## Why the path undershoots here

The exam's favorite follow-up: is the Euler approximation an overestimate or an underestimate? The answer comes from concavity. For this equation,

$$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{dy}{dx} = y > 0,$$

so the solution curve is concave up. A tangent line to a concave-up curve lies below the curve, and Euler's method walks along tangent lines, so every step starts on or below the truth and lands further below it. The approximation is an underestimate, which is exactly what the picture shows at every step size.

The justification sentence has the same three-part shape the rest of the course uses: the claim (underestimate), the reason (tangent lines lie below the curve), and the calculus fact that licenses it (the solution is concave up because $$y'' > 0$$). For a concave-down solution the conclusion flips. No memorized rule is needed, only the picture of a tangent line hugging a curve from one side.

## Halving the step, quartering nothing

One more observation the slider makes visible. Euler's method is a first-order method: cutting the step size in half roughly cuts the error in half, no better. Forty steps get close to the curve, but "close" is earned linearly, one halving at a time. This is why real numerical solvers use more sophisticated updates, and why the exam keeps the step count at two or three: the method's value in BC is conceptual. It is the differential equation's slope field made into a walking path, and it is the simplest possible answer to the question of how a computer solves an equation that has no formula solution.

<div class="article-note" markdown="1">
A self-test: run Euler's method for $$\tfrac{dy}{dx} = -y$$ with $$y(0) = 4$$ and one step of size 1. The update gives $$y(1) \approx 4 + (-4)(1) = 0$$. The true value is $$4e^{-1} \approx 1.47$$. Then explain the undershoot: this solution is concave up too, since $$y'' = -y' = y > 0$$, so the tangent line again dives below the curve. If you can produce both the number and the sentence, the Euler point pair on the exam is yours.
</div>
