---
layout: post
title: "Taylor polynomials: teaching a polynomial to impersonate a function"
date: 2026-07-22
description: "The whole of Unit 10 in one idea: match enough derivatives at a point and a polynomial becomes indistinguishable from the function — nearby. Watch the impersonation improve degree by degree, and see exactly where it fails."
course: "AP Calculus BC"
read_time: "9 min read"
math: true
---

Here is the idea behind the entire second half of BC, stated in one sentence: **polynomials are the functions we can actually compute, so we teach one to impersonate the function we care about.** Everything else — Maclaurin series, error bounds, radius of convergence — is the theory of how good that impersonation is and where it works.

## The impersonation strategy

How do you make a polynomial behave like $$\sin x$$ near $$x = 0$$? Force it to agree with $$\sin x$$ on everything a derivative can measure at that point.

- Agree on the **value**: $$p(0) = \sin 0 = 0$$.
- Agree on the **slope**: $$p'(0) = \cos 0 = 1$$.
- Agree on the **concavity**: $$p''(0) = -\sin 0 = 0$$.
- Agree on the third derivative: $$p'''(0) = -\cos 0 = -1$$. And so on.

A degree-$$n$$ polynomial has $$n+1$$ coefficients — that's $$n+1$$ dials to turn, enough to match $$n+1$$ derivatives. Turning the dials gives the **Taylor polynomial**:

$$T_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(0)}{k!}\,x^k.$$

The $$k!$$ in the denominator is not decoration: differentiating $$x^k$$ exactly $$k$$ times produces $$k!$$, so dividing by it in advance is what makes the $$k$$-th derivative of $$T_n$$ land exactly on $$f^{(k)}(0)$$. For sine, the even derivatives all vanish at 0 and the odd ones alternate between $$1$$ and $$-1$$:

$$T_n(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$$

$$T_1(x) = x$$ is an old friend — it's the tangent line, and "$$\sin x \approx x$$ for small $$x$$" is exactly the degree-1 impersonation. Every higher degree is the same move with more dials.

## Watch the impersonation improve

The canvas below shows $$\sin x$$ in light gray and its Taylor polynomial in black. Drag the slider.

<div class="viz" markdown="0">
  <canvas id="tay-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="tay-n">Degree</label>
    <input type="range" id="tay-n" min="0" max="6" step="1" value="1">
    <span class="viz-value" id="tay-read"></span>
  </div>
  <p class="viz-caption">Two things to watch. Near the center, each new degree snaps the polynomial onto the curve for another stretch — by degree 7 the impersonation is essentially perfect on a full period. Far from the center, every polynomial eventually tears away and flies off to ±∞, because that is what polynomials do. A Taylor polynomial is a <em>local</em> impersonation: flawless where it's anchored, hopeless far away, and the whole game is knowing the size of "where it's anchored."</p>
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

## How wrong is the impersonation? Two rulers

BC gives you two instruments for measuring the gap $$\left|f(x) - T_n(x)\right|$$, and knowing which one a problem wants is half the battle.

**Ruler 1 — the alternating series error bound.** If, at your particular $$x$$, the series alternates with terms shrinking in size, the truncation error is at most the first term you left out. Approximate $$\sin(0.5)$$ by $$T_3 = 0.5 - \tfrac{0.5^3}{6} \approx 0.479$$; the error is at most the next term, $$\tfrac{0.5^5}{120} \approx 0.00026$$. Cheap and astonishingly tight.

**Ruler 2 — the Lagrange error bound.** In general,

$$\left|f(x) - T_n(x)\right| \;\le\; \frac{M}{(n+1)!}\,|x - c|^{\,n+1},$$

where $$M$$ bounds the *next* derivative, $$\left|f^{(n+1)}\right|$$, between the center $$c$$ and $$x$$. Read it as a story: the error is controlled by the first derivative you *failed* to match — the first dial you didn't get to turn — scaled by how far you've wandered from the anchor point ($$|x-c|^{n+1}$$) and tamed by the factorial. The factorial is why the impersonation improves so fast: $$(n+1)!$$ grows quicker than any power, so for functions like sine (all derivatives bounded by 1) the bound collapses to zero at every single $$x$$. That is the precise sense in which $$\sin x$$ *equals* its series everywhere.

## Where impersonations fail: the invisible wall

Sine is the best-case client. Now try $$\ln(1+x)$$:

$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$$

This series only converges for $$-1 < x \le 1$$. No matter how many terms you take, at $$x = 1.2$$ the polynomials don't settle down — they oscillate with growing violence. The impersonation has a **radius of convergence** of exactly 1, and there's a good reason for the wall's location: $$\ln(1+x)$$ itself blows up at $$x = -1$$. The polynomial impersonators, anchored at 0, can feel that singularity a distance 1 away, and the damage is symmetric — the series fails at $$x = -1$$ *and* beyond $$x = +1$$, even though $$\ln(1+x)$$ is perfectly healthy at $$x = 2$$. A power series always works on an interval centered at its anchor, with a radius set by the distance to the nearest trouble.

That's the mental model behind the exam's interval-of-convergence routine: ratio test to find the radius (the wall's distance), then hand-check each endpoint (the wall itself), where the ratio test goes silent and a numeric series test — often the alternating series test on one end, harmonic divergence on the other — settles the boundary. For $$\ln(1+x)$$ the interval comes out $$(-1, 1]$$: divergent at $$-1$$, conditionally convergent at $$1$$.

## What BC actually asks

Nearly every Taylor FRQ is assembled from five moves, and all five are visible from the impersonation idea:

1. **Build terms** from given derivative values with $$\tfrac{f^{(k)}(c)}{k!}$$ — turning the dials by hand.
2. **Manipulate a known series** — substitute $$-x^2$$ for $$u$$ in $$e^u$$, multiply by $$x$$, differentiate or integrate term by term. (Impersonators compose: the series for $$e^{-x^2}$$, key to statistics, is one substitution away, even though the function has no elementary antiderivative.)
3. **Approximate a value** with the first few terms.
4. **Bound the error** with the right ruler.
5. **Find where the impersonation holds** — radius and interval of convergence.

If you can narrate *why* each move works in impersonation language — matching dials, feeling for the nearest wall, measuring the first unmatched term — the unit stops being twelve formulas and becomes one idea with twelve outfits.

<div class="article-note" markdown="1">
A puzzle to take with you: the function $$\tfrac{1}{1+x^2}$$ is smooth and perfectly finite for every real $$x$$ — no blow-up anywhere on the real line. Yet its Maclaurin series $$1 - x^2 + x^4 - \cdots$$ stubbornly refuses to converge past $$|x| = 1$$. Where's the wall? (Hint: try $$x = i$$. The nearest trouble isn't always on the real line — a fact that delighted mathematicians into inventing complex analysis.)
</div>
