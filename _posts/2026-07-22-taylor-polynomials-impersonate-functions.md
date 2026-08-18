---
layout: post
title: "Approximation by Taylor polynomials"
date: 2026-07-22
description: "A Taylor polynomial matches a function and its derivatives at one point. Increasing the degree improves the local approximation, while convergence determines how far that approximation extends."
course: "AP Calculus BC"
read_time: "8 min read"
math: true
kind: foundations
sequence: 31
interactive: true
blurb: "A Taylor polynomial matches a function and its derivatives at one point. Increasing the degree improves the local approximation, while convergence determines how far that approximation extends"
featured: true
image: "/assets/og/taylor-polynomials-impersonate-functions.png"
---

A Taylor polynomial approximates a function near a chosen center by matching its derivatives there, and the degree determines how many derivatives are matched. This gives a systematic way to replace a function with a polynomial whose local behavior is easier to compute.

## Matching derivatives

Suppose we want a polynomial to approximate $$\sin x$$ near $$x=0$$. We require the polynomial to match the function value and successive derivatives at the center. For sine, $$\sin0=0,\; \cos0=1,\; -\sin0=0,\; -\cos0=-1$$.

In general, the degree-$$n$$ Taylor polynomial for $$f$$ centered at $$c$$ is

$$T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(c)}{k!} (x-c)^k$$

When the center is 0, this is called a Maclaurin polynomial, and for sine, $$T_n(x) = x-\tfrac{x^3}{3!}+\tfrac{x^5}{5!}-\tfrac{x^7}{7!}+\cdots$$.

The factorial has a specific role. Differentiating $$(x-c)^k$$ exactly $$k$$ times produces a factor of $$k!$$, and dividing by $$k!$$ makes the $$k$$-th derivative of the polynomial match the $$k$$-th derivative of the function at the center.

## The tangent line is the first case

The degree-1 Taylor polynomial is $$T_1(x) = f(c)+f'(c)(x-c)$$, which is the linearization of $$f$$ at $$c$$. So Taylor polynomials extend the same idea. A tangent line matches the function's value and first derivative. A quadratic Taylor polynomial also matches the second derivative, and a cubic also matches the third, and so on.

<div class="viz" markdown="0">
  <canvas id="tay-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="tay-n">Degree</label>
    <input type="range" id="tay-n" min="0" max="6" step="1" value="1">
    <span class="viz-value" id="tay-read"></span>
  </div>
  <p class="viz-caption">Two things to watch. Near the center, each new degree fits the polynomial to the curve for another stretch; by degree 7 the match is essentially perfect across a full period. Far from the center, every polynomial eventually pulls away and heads to plus or minus infinity, because that is what polynomials do. A Taylor polynomial is a local approximation: excellent where it is anchored, useless far away. Much of the unit comes down to knowing the size of "where it is anchored."</p>
</div>

<script>
(function(){
  var cv = document.getElementById('tay-cv'), slider = document.getElementById('tay-n'), read = document.getElementById('tay-read');
  var c = cv.getContext('2d'), W = cv.width, H = cv.height, pad = 20;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var X0 = -9.4, X1 = 9.4, Y0 = -3.4, Y1 = 3.4;
  function px(x){ return pad + (x - X0)/(X1 - X0)*(W - 2*pad); }
  function py(y){ return H - pad - (y - Y0)/(Y1 - Y0)*(H - 2*pad); }
  function taylor(x, deg){
    var s = 0, term, k;
    for(k = 0; k <= deg; k++){
      term = Math.pow(-1, k) * Math.pow(x, 2*k+1);
      var f = 1, j; for(j = 2; j <= 2*k+1; j++) f *= j;
      s += term / f;
    }
    return s;
  }
  function plot(fn, color, wdt){
    c.strokeStyle = color; c.lineWidth = wdt; c.beginPath();
    var started = false;
    for(var i = 0; i <= 600; i++){
      var x = X0 + (X1 - X0)*i/600, y = fn(x);
      if(y < Y0 - 6 || y > Y1 + 6){ started = false; continue; }
      var X = px(x), Y = py(Math.max(Y0-1, Math.min(Y1+1, y)));
      started ? c.lineTo(X, Y) : c.moveTo(X, Y); started = true;
    }
    c.stroke();
  }
  function draw(){
    var n = +slider.value, deg = 2*n + 1;   // 1,3,5,...,13
    c.clearRect(0, 0, W, H);
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(px(X0), py(0)); c.lineTo(px(X1), py(0)); c.stroke();
    c.beginPath(); c.moveTo(px(0), py(Y0)); c.lineTo(px(0), py(Y1)); c.stroke();
    plot(Math.sin, '#c4c4c4', 2.5);
    plot(function(x){ return taylor(x, n); }, '#1f1f1f', 2);
    c.fillStyle = '#1f1f1f'; c.beginPath(); c.arc(px(0), py(0), 4, 0, 7); c.fill();
    var terms = ['x', 'x − x³/3!', 'x − x³/3! + x⁵/5!', '… − x⁷/7!', '… + x⁹/9!', '… − x¹¹/11!', '… + x¹³/13!'];
    read.textContent = 'T' + deg + '(x) = ' + terms[n];
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

The graph compares $$\sin x$$ with Taylor polynomials of increasing degree. Near the center, each additional nonzero term extends the region where the polynomial closely follows the function, and far enough away, any fixed polynomial eventually separates from the bounded sine curve. Taylor approximation is local unless the corresponding infinite series converges to the function on a larger domain.

## The alternating-series error bound

For a Taylor series that alternates with decreasing term magnitudes at the chosen $$x$$, the alternating-series error bound is often the simplest tool. For example, approximate $$\sin(0.5)$$ using $$T_3(0.5) = 0.5-\tfrac{0.5^3}{6}$$. The first omitted term has magnitude $$\tfrac{0.5^5}{120}$$, so the truncation error is no larger than that quantity. The bound comes from the same structure as the alternating series test. Successive partial sums trap the true value between them.

## The Lagrange error bound

A more general bound is

$$\vert f(x)-T_n(x)\vert \le \frac{M}{(n+1)!}\vert x-c\vert ^{n+1}$$

where $$M$$ is an upper bound for $$\vert f^{(n+1)}(z)\vert$$ between $$c$$ and $$x$$. The formula shows three things. The error depends on the first derivative that was not matched, it grows with the distance from the center, and it is divided by a factorial that grows rapidly with the degree. For sine and cosine, every derivative has magnitude at most 1, and that makes the Lagrange bound especially manageable.

## A series need not converge everywhere

Consider

$$\ln(1+x) = x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots$$

This power series converges on $$-1<x\le1$$, and at $$x=1.2$$, adding more terms does not make the polynomial approximations settle toward the function. The radius of convergence is 1.

For a real power series centered at $$c$$, convergence occurs on an interval centered at $$c$$. The ratio test usually determines the radius, and the endpoints then have to be checked separately. For the series above, the left endpoint produces the divergent [harmonic series](/2026/07/23/harmonic-series-surprises-of-infinity.html), the right endpoint produces the convergent alternating harmonic series, and so the interval is $$(-1,1]$$.

## Manipulating known series

Once a standard Taylor series is known, other series can be constructed through substitution, multiplication, differentiation, and integration within the interval where those operations are valid. For example, $$e^u = 1+u+\tfrac{u^2}{2!}+\tfrac{u^3}{3!}+\cdots$$. Substitute $$u=-x^2$$ to obtain a series for $$e^{-x^2}$$.

This is useful because $$e^{-x^2}$$ has no elementary antiderivative, even though its power series can be integrated term by term inside its interval of convergence. The connection is particularly relevant in probability and statistics, where the normal density contains the same exponential form.

## The recurring tasks

Taylor-series problems usually involve some combination of the following.

- Build terms from derivative values.
- Manipulate a known series.
- Approximate a function value.
- Bound the approximation error.
- Determine the radius and interval of convergence.

These are different questions about the same construction. The polynomial is built by matching derivatives at a center, the error measures how much information is lost by truncating, and the interval of convergence tells us where the infinite process actually recovers the function or a related analytic expression.

## A final point about the radius

<div class="article-note" markdown="1">
The function $$\tfrac{1}{1+x^2}$$ is smooth for every real $$x$$. Its Maclaurin series is $$1-x^2+x^4-x^6+\cdots$$, and that series has radius of convergence 1. The restriction comes from the complex singularities at $$x=\pm i$$. This lies beyond what is needed for BC, but it explains an otherwise puzzling fact. A Taylor series can stop converging even when the real-valued function itself remains perfectly well behaved.
</div>
