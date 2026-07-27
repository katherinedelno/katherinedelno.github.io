---
layout: post
title: "Approximation by Taylor polynomials"
date: 2026-07-22
description: "A polynomial that matches enough derivatives becomes locally indistinguishable from the function it imitates. This article examines where the approximation holds, where it fails, and how the error is measured."
course: "AP Calculus BC"
read_time: "9 min read"
math: true
---

The second half of BC rests on one idea. Polynomials are the functions we can actually compute, so we build a polynomial that behaves like the function we care about. Everything else in the unit, from Maclaurin series to error bounds to the radius of convergence, is the theory of how good that approximation is and where it holds.

## The matching strategy

How do you make a polynomial behave like $$\sin x$$ near $$x = 0$$? Force it to agree with $$\sin x$$ on everything a derivative can measure at that point.

- Agree on the value: $$p(0) = \sin 0 = 0$$.
- Agree on the slope: $$p'(0) = \cos 0 = 1$$.
- Agree on the concavity: $$p''(0) = -\sin 0 = 0$$.
- Agree on the third derivative: $$p'''(0) = -\cos 0 = -1$$, and so on.

A polynomial of degree $$n$$ has $$n+1$$ coefficients, which is enough freedom to match $$n+1$$ derivatives. Carrying out the matching produces the Taylor polynomial:

$$T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(0)}{k!}\,x^k.$$

The $$k!$$ in the denominator has a job. Differentiating $$x^k$$ exactly $$k$$ times produces a factor of $$k!$$, so dividing by it in advance is what makes the $$k$$-th derivative of $$T_n$$ land exactly on $$f^{(k)}(0)$$. For sine, the even derivatives all vanish at 0 and the odd ones alternate between $$1$$ and $$-1$$, which gives

$$T_n(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$$

The first of these, $$T_1(x) = x$$, is an old friend: it is the tangent line, and the familiar fact that $$\sin x \approx x$$ for small $$x$$ is the degree-1 case of this whole construction. Each higher degree is the same move with more derivatives matched.

## Watch the approximation improve

The graph below shows $$\sin x$$ in light gray and its Taylor polynomial in black. Drag the slider to raise the degree.

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
    var terms = ['x', 'x − x³/3!', 'x − x³/3! + x⁵/5!', '… + x⁷/7!', '… − x⁹/9!', '… + x¹¹/11!', '… − x¹³/13!'];
    read.textContent = 'T' + deg + '(x) = ' + terms[n];
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

## Measuring the error

BC gives you two instruments for measuring the gap between $$f(x)$$ and $$T_n(x)$$, and knowing which one a problem wants is half the battle.

**The alternating series error bound.** If, at your particular $$x$$, the series alternates with terms shrinking in size, the truncation error is at most the first term you left out. Approximate $$\sin(0.5)$$ by $$T_3 = 0.5 - \tfrac{0.5^3}{6} \approx 0.479$$; the error is at most the next term, $$\tfrac{0.5^5}{120} \approx 0.00026$$. The bound costs almost nothing to compute and is remarkably tight.

**The Lagrange error bound.** In general,

$$\left\vert f(x) - T_n(x)\right\vert \;\le\; \frac{M}{(n+1)!}\,\vert x - c\vert^{\,n+1},$$

where $$M$$ bounds the next derivative, $$\left\vert f^{(n+1)}\right\vert$$, between the center $$c$$ and $$x$$. It helps to read the formula as a sentence: the error is controlled by the first derivative you failed to match, scaled by how far you have moved from the center, and divided down by the factorial. The factorial is why the approximation improves so quickly. Since $$(n+1)!$$ grows faster than any power, and every derivative of sine is bounded by 1, the bound goes to zero at every single $$x$$. That is the precise sense in which $$\sin x$$ equals its series everywhere.

## Where the approximation fails

Sine is the best possible case. Now consider $$\ln(1+x)$$:

$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$$

This series converges only for $$-1 < x \le 1$$. No matter how many terms you take, at $$x = 1.2$$ the polynomials never settle down; they oscillate more and more violently. The series has a radius of convergence of exactly 1, and the location of the wall is not an accident. The function $$\ln(1+x)$$ itself blows up at $$x = -1$$. A power series centered at 0 can only work out to the nearest point of trouble, and the damage is symmetric: the series fails at $$x = -1$$ and also beyond $$x = +1$$, even though $$\ln(1+x)$$ is perfectly well behaved at $$x = 2$$. A power series always converges on an interval centered at its anchor point, with a radius set by the distance to the nearest singularity.

This is the reasoning behind the exam's interval-of-convergence routine. The ratio test finds the radius, which is the distance to the wall. Then each endpoint must be checked by hand, because the ratio test returns $$L = 1$$ there and has nothing to say. The endpoint checks are ordinary numeric series tests. For $$\ln(1+x)$$ the interval comes out to $$(-1, 1]$$: divergent at $$-1$$ (harmonic series), conditionally convergent at $$1$$ (alternating harmonic series).

## What BC actually asks

Nearly every Taylor free-response question is assembled from five moves, and all five come straight from the ideas above.

1. Build terms from given derivative values using $$\tfrac{f^{(k)}(c)}{k!}$$.
2. Manipulate a known series: substitute $$-x^2$$ for $$u$$ in the series for $$e^u$$, multiply by $$x$$, or differentiate and integrate term by term. Series compose well. The series for $$e^{-x^2}$$, which matters in statistics, is one substitution away, even though the function has no elementary antiderivative.
3. Approximate a value with the first few terms.
4. Bound the error with the appropriate bound.
5. Find where the series converges, meaning the radius and the interval.

If you can explain why each move works in the language of matching derivatives and distance to the nearest wall, the unit stops being twelve separate formulas and becomes one idea used twelve ways.

<div class="article-note" markdown="1">
A puzzle to take with you: the function $$\tfrac{1}{1+x^2}$$ is smooth and finite for every real $$x$$, with no blow-up anywhere on the real line. Yet its Maclaurin series $$1 - x^2 + x^4 - \cdots$$ refuses to converge past $$\vert x\vert = 1$$. Where is the wall? Hint: try $$x = i$$. The nearest trouble is not always on the real line, a fact that helped push mathematicians toward inventing complex analysis.
</div>
