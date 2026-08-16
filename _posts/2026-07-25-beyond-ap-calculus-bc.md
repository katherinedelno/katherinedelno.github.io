---
layout: post
title: "After BC: multivariable calculus"
date: 2026-07-25
description: "Functions become surfaces, derivatives become directional, and integrals extend over regions and volumes. Much of BC reappears in a higher-dimensional setting."
course: "AP Calculus BC"
section: beyond
read_time: "9 min read"
math: true
kind: beyond
sequence: 6
interactive: true
blurb: "Functions become surfaces, derivatives become directional, and integrals extend over regions and volumes. Much of BC reappears in a higher-dimensional setting"
featured: true
image: "/assets/og/beyond-ap-calculus-bc.png"
---

AP Calculus studies functions of one variable.

A function such as

$$y=f(x)$$

takes one input and produces one output, so its graph is a curve.

Multivariable calculus begins by allowing more than one input.

For example,

$$z=f(x,y)$$

takes a point in the plane and assigns it a height.

The graph is now a surface.

Many of the ideas from BC remain recognizable, but they have to account for the additional directions.

## Functions become surfaces

Consider

$$f(x,y)=\sin x\cos y.$$

<div class="viz" markdown="0">
  <canvas id="s3-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <label for="s3-rot">Rotate</label>
    <input type="range" id="s3-rot" min="0" max="1000" value="140">
  </div>
  <p class="viz-caption">The graph of z = sin x cos y, a function of two variables. Peaks, valleys, and mountain passes replace the maxima and minima of BC. Walking east-west changes the height at one rate, walking north-south at another, and that observation is the whole idea of partial derivatives.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('s3-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('s3-rot');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var N = 28, LO = -3.6, HI = 3.6;
  function f(x, y){ return Math.sin(x)*Math.cos(y); }
  function draw(){
    var th = (slider.value/1000)*2*Math.PI, tilt = 0.42;
    var ct = Math.cos(th), st = Math.sin(th);
    c.clearRect(0, 0, W, H);
    function proj(x, y, z){
      var X = x*ct - y*st, Y = x*st + y*ct;
      return [W/2 + X*62, H/2 + 26 - z*74 + Y*62*tilt];
    }
    var i, j;
    c.lineWidth = 1;
    for(i = 0; i <= N; i++){
      var x = LO + (HI - LO)*i/N;
      c.strokeStyle = '#9a9a97'; c.beginPath();
      for(j = 0; j <= N; j++){
        var y = LO + (HI - LO)*j/N, p = proj(x, y, f(x, y));
        j ? c.lineTo(p[0], p[1]) : c.moveTo(p[0], p[1]);
      }
      c.stroke();
    }
    for(j = 0; j <= N; j++){
      var y2 = LO + (HI - LO)*j/N;
      c.strokeStyle = '#c9c9c6'; c.beginPath();
      for(i = 0; i <= N; i++){
        var x2 = LO + (HI - LO)*i/N, p2 = proj(x2, y2, f(x2, y2));
        i ? c.lineTo(p2[0], p2[1]) : c.moveTo(p2[0], p2[1]);
      }
      c.stroke();
    }
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

The graph rises and falls over the $$xy$$-plane.

A maximum is now a peak on a surface.

A minimum is a valley.

There can also be saddle points, where the surface rises in one direction and falls in another.

That additional geometry is the first major change.

With one input, there is essentially one axis along which to ask how the function changes.

With two inputs, there are infinitely many possible directions.

## Partial derivatives

Two directions are especially useful.

The partial derivative

$$\frac{\partial f}{\partial x}$$

measures the rate of change in the $$x$$-direction while $$y$$ is held fixed.

Similarly,

$$\frac{\partial f}{\partial y}$$

measures change in the $$y$$-direction while $$x$$ is held fixed.

The differentiation rules themselves are familiar.

For

$$f(x,y)=x^2y,$$

treat $$y$$ as constant when differentiating with respect to $$x$$:

$$\frac{\partial f}{\partial x}=2xy.$$

Treat $$x$$ as constant when differentiating with respect to $$y$$:

$$\frac{\partial f}{\partial y}=x^2.$$

The new notation records which input is changing.

## The gradient

The two partial derivatives can be collected into a vector:

$$\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right\rangle.$$

This is the gradient.

At a point where the gradient is nonzero, it points in the direction of steepest increase.

Its magnitude gives the rate of that steepest increase.

The directional derivative in any other direction can be obtained by projecting the gradient onto that direction.

This is one reason vectors become central in the course.

Optimization also changes.

For an interior critical point of a differentiable function of two variables, both partial derivatives must be zero.

Then second-derivative information is used to distinguish local maxima, minima, and saddle points.

## Integrals become double and triple integrals

In one variable,

$$\int_a^b f(x)\,dx$$

accumulates across an interval.

A double integral,

$$\iint_R f(x,y)\,dA,$$

accumulates across a region in the plane.

When $$f$$ represents height, the integral can compute volume under a surface.

The basic [Riemann-sum](/2026/07/25/riemann-sums-watching-rectangles.html) idea is the same.

Instead of dividing an interval into narrow subintervals, divide a region into small pieces and sum the contributions from each one.

Many double integrals can be evaluated as repeated one-variable integrals.

For example, integrate with respect to $$x$$ while treating $$y$$ as constant, then integrate the result with respect to $$y$$.

The BC integration rules are still doing the computational work.

## Coordinate systems matter more

Polar coordinates become especially useful for regions with circular symmetry.

The area element is

$$dA=r\,dr\,d\theta.$$

The factor $$r$$ accounts for the way polar coordinates stretch area.

This change-of-variables idea extends much further in multivariable calculus through Jacobian determinants.

A classical example is the Gaussian integral

$$\int_{-\infty}^{\infty}e^{-x^2}\,dx.$$

It has no elementary antiderivative.

By squaring the integral and interpreting the result as a double integral, the problem can be converted to polar coordinates.

The result is

$$\sqrt{\pi}.$$

The same calculation helps explain the normalization constant in the normal distribution.

## Vector fields and line integrals

A multivariable course eventually shifts from scalar functions to vector fields.

A vector field assigns an arrow to each point in space.

Examples include velocity fields, gravitational fields, and electric fields.

A line integral measures accumulation along a curve through such a field.

One interpretation is physical work.

The parametric curves from BC become useful again because a path can be written as

$$\mathbf r(t) = \langle x(t),y(t)\rangle.$$

Arc length, velocity vectors, and parameterized motion all carry directly into this setting.

## The Fundamental Theorem grows too

Later the course develops theorems such as Green's theorem and, in higher dimensions, Stokes' theorem and the divergence theorem.

These connect behavior on the boundary of a region with behavior throughout its interior.

The resemblance to the [Fundamental Theorem of Calculus](/2026/07/17/fundamental-theorem-from-the-ground-up.html) is structural.

In one dimension, integration of a derivative over an interval is determined by values at the endpoints.

In higher dimensions, related theorems connect integrals over a region with integrals over its boundary.

## What carries over from BC

The most useful preparation is still ordinary calculus done cleanly.

The chain rule, integration techniques, parametric curves, vectors, polar coordinates, and limits all return.

The new challenge is usually geometric.

There are more variables, more directions, and more coordinate systems, but the underlying operations remain recognizable.

<div class="article-note" markdown="1">
A good preview question is to look at the surface above and ask how its height changes if you move east, north, or along a diagonal.

Those are three different directional questions about the same function.

That is the shift from one-variable to multivariable calculus.
</div>
