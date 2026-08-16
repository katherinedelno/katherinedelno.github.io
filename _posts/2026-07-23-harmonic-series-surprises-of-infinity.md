---
layout: post
title: "The harmonic series and conditional convergence"
date: 2026-07-23
description: "Terms can approach zero while their series diverges. Alternating signs can restore convergence, and conditional convergence makes the order of terms matter."
course: "AP Calculus BC"
read_time: "12 min read"
math: true
kind: foundations
sequence: 29
interactive: true
blurb: "Terms can approach zero while their series diverges. Alternating signs can restore convergence, and conditional convergence makes the order of terms matter"
image: "/assets/og/harmonic-series-surprises-of-infinity.png"
---

Infinite series force a distinction between the behavior of individual terms and the behavior of their accumulated sum.

The harmonic series is the standard example.

Its terms approach zero, but the series diverges.

Changing only the signs produces a convergent series.

That difference explains several of the [convergence tests](/2026/07/24/which-convergence-test-field-guide.html) used in BC.

## Terms can vanish while the sum diverges

The harmonic series is

$$1+\frac12+\frac13+\frac14+\frac15+\cdots.$$

Its terms approach zero.

The series nevertheless diverges.

A classical proof groups the terms:

$$1+\frac12 + \left(\frac13+\frac14\right) + \left(\frac15+\frac16+\frac17+\frac18\right) +\cdots.$$

In the first displayed group,

$$\frac13+\frac14>\frac12.$$

In the next,

$$\frac15+\frac16+\frac17+\frac18 > 4\left(\frac18\right) = \frac12.$$

Each new block contains twice as many terms, and every block contributes more than $$1/2$$.

With infinitely many such blocks, the partial sums grow without bound.

So

$$\sum_{n=1}^{\infty}\frac1n$$

diverges even though

$$\frac1n\to0.$$

This is why the $$n$$-th term test can prove divergence but cannot prove convergence.

If the terms do not approach zero, the series diverges.

If they do approach zero, more information is needed.

## Divergence can be extremely slow

The partial sums of the harmonic series grow roughly like

$$\ln n.$$

That growth is very slow.

The series can appear numerically stable for a long time while continuing to diverge.

This is one reason numerical evidence is not enough to establish convergence.

A test has to address the infinite tail.

<div class="viz" markdown="0">
  <canvas id="hs-cv" width="700" height="280"></canvas>
  <div class="viz-controls">
    <label for="hs-n">Terms</label>
    <input type="range" id="hs-n" min="2" max="400" step="1" value="30">
    <span class="viz-value" id="hs-read"></span>
  </div>
  <p class="viz-caption">Top: harmonic partial sums, still climbing at 400 terms and never stopping, though ever more slowly (the growth is logarithmic). Bottom, on a vertical scale roughly ten times finer, because on the upper panel's scale it would be a flat line: the alternating harmonic series, hopping above and below the target in shrinking steps and trapping ln 2 between consecutive hops. Same ingredients, opposite fates. The gap between each hop and the dashed line is smaller than the next term, which is the alternating series error bound drawn in the air.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('hs-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('hs-n'), read = document.getElementById('hs-read');
  var W = cv.width, H = cv.height, pad = 36;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  // Two panels sharing one horizontal axis. A single vertical scale cannot show
  // both series: the harmonic sum passes 6.5 by 400 terms, and against that the
  // alternating one is a flat line a few pixels thick.
  var HTOP = 18, HBOT = 142, ATOP = 178, ABOT = 258;
  var HMAX = 7, ALO = 0.42, AHI = 1.06;
  var FONT = '700 11px Hanken Grotesk, sans-serif';
  function px(i, n){ return pad + (W - 2*pad)*i/n; }
  function hy(v){ return HBOT - (HBOT - HTOP)*v/HMAX; }
  function ay(v){ return ABOT - (ABOT - ATOP)*(v - ALO)/(AHI - ALO); }
  function draw(){
    var n = +slider.value, k, ln2 = Math.log(2);
    c.clearRect(0, 0, W, H);

    // upper panel: the harmonic partial sums
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(pad, hy(0)); c.lineTo(W - pad, hy(0)); c.stroke();
    c.font = FONT; c.fillStyle = '#9a9a97'; c.textAlign = 'right';
    for(var g = 2; g <= 6; g += 2){
      c.strokeStyle = '#f2f2f0';
      c.beginPath(); c.moveTo(pad, hy(g)); c.lineTo(W - pad, hy(g)); c.stroke();
      c.fillText(String(g), pad - 6, hy(g) + 4);
    }
    c.textAlign = 'left'; c.fillStyle = '#5c5c5c';
    c.fillText('harmonic partial sums', pad, HTOP + 2);
    var hSum = 0;
    c.strokeStyle = '#1f1f1f'; c.lineWidth = 2; c.beginPath();
    for(k = 1; k <= n; k++){
      hSum += 1/k;
      var Y2 = hy(Math.min(hSum, HMAX));
      k === 1 ? c.moveTo(px(k, n), Y2) : c.lineTo(px(k, n), Y2);
    }
    c.stroke();

    // lower panel: the alternating partial sums, on a scale ten times finer
    c.strokeStyle = '#8a8a8a'; c.lineWidth = 1; c.setLineDash([4,4]);
    c.beginPath(); c.moveTo(pad, ay(ln2)); c.lineTo(W - pad, ay(ln2)); c.stroke();
    c.setLineDash([]);
    c.fillStyle = '#5c5c5c'; c.font = FONT; c.textAlign = 'left';
    c.fillText('alternating partial sums', pad, ATOP - 8);
    c.fillText('ln 2', W - pad - 26, ay(ln2) - 6);
    var aSum = 0;
    c.strokeStyle = '#5c5c5c'; c.lineWidth = 1.6; c.beginPath();
    for(k = 1; k <= n; k++){
      aSum += (k % 2 ? 1 : -1)/k;
      var Y = ay(Math.max(ALO, Math.min(AHI, aSum)));
      k === 1 ? c.moveTo(px(k, n), Y) : c.lineTo(px(k, n), Y);
    }
    c.stroke();
    read.textContent = 'harmonic: ' + hSum.toFixed(3) + '   alternating: ' + aSum.toFixed(3);
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

The upper panel shows harmonic partial sums continuing upward.

The lower panel shows the alternating harmonic partial sums approaching a finite limit.

The ingredients are nearly the same. The signs change the outcome.

## Alternating signs

Now consider

$$1-\frac12+\frac13-\frac14+\frac15-\cdots.$$

This series converges to

$$\ln2.$$

The alternating series test explains why.

If the positive magnitudes $$b_n$$ decrease to zero, then

$$\sum(-1)^n b_n$$

converges.

The partial sums alternate above and below the limit with progressively smaller corrections.

That same structure gives the alternating-series error bound.

If the series satisfies the hypotheses of the test, the error after truncation is no larger than the magnitude of the first omitted term.

## Conditional convergence

The alternating harmonic series converges.

But its absolute-value series is

$$\sum_{n=1}^{\infty}\frac1n,$$

which diverges.

So the alternating harmonic series converges conditionally rather than absolutely.

This distinction has a real consequence.

A conditionally convergent series can change value when its terms are rearranged.

For example, taking two positive terms and then one negative term repeatedly gives a rearrangement of the alternating harmonic series with a different sum.

The positive terms by themselves diverge to $$+\infty$$.

The negative terms by themselves diverge to $$-\infty$$.

A rearrangement changes the balance between those two parts.

The Riemann rearrangement theorem goes further. A conditionally convergent series can be rearranged to converge to any chosen real number, or to diverge.

Absolutely convergent series do not have this behavior.

If

$$\sum \vert a_n\vert$$

converges, rearranging

$$\sum a_n$$

does not change its sum.

## The neighboring $$p$$-series

The harmonic series is the $$p=1$$ case of

$$\sum_{n=1}^{\infty}\frac{1}{n^p}.$$

This series converges when

$$p>1$$

and diverges when

$$p\le1.$$

For $$p=2$$,

$$\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}.$$

The appearance of $$\pi$$ in a series involving only reciprocals of squares is the classical Basel problem.

For $$p=3$$, the series also converges, but its value has no known comparably simple closed form.

The important course-level distinction is the threshold at $$p=1$$.

Even a very small change above 1 changes the convergence behavior.

## What to carry into convergence problems

Several practical rules follow from these examples.

- A term approaching zero is necessary for convergence, but not sufficient.
- Numerical partial sums cannot establish convergence.
- Absolute convergence is stronger than conditional convergence.
- For an alternating series that meets the hypotheses, the first omitted term bounds the truncation error.
- The $$p$$-series threshold at $$p=1$$ is exact.

<div class="article-note" markdown="1">
These are not unrelated rules.

They describe different ways that infinite accumulation can behave.
</div>
