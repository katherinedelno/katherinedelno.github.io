---
layout: post
title: "After AP Statistics: the upper division"
date: 2026-07-25
description: "Probability theory, mathematical statistics, regression, Bayesian inference, stochastic processes, and computation extend the ideas introduced in AP Statistics."
course: "AP Statistics"
section: beyond
read_time: "8 min read"
math: true
kind: beyond
sequence: 9
interactive: true
blurb: "Probability theory, mathematical statistics, regression, Bayesian inference, stochastic processes, and computation extend the ideas introduced in AP Statistics"
image: "/assets/og/beyond-ap-statistics.png"
---

AP Statistics introduces a carefully selected part of a much larger subject.

You learn how to design studies, describe variation, work with probability, fit a regression line, construct intervals, perform significance tests, and state conclusions in context.

Later statistics courses ask where those procedures come from and what happens when the standard formulas are no longer enough.

Calculus and linear algebra begin to appear more heavily.

So does computation.

## Probability theory

A first probability course gives a mathematical foundation to ideas that AP Statistics introduces through simulation and formulas.

Random variables become objects to study in their own right.

Expected values, variances, joint distributions, conditional distributions, and transformations are derived systematically.

The Law of Large Numbers explains why averages stabilize.

[The Central Limit Theorem](/2026/07/25/central-limit-theorem-watched-live.html) explains why normal approximations arise so often.

In an upper-division probability course, these results are proved rather than only observed.

## A random walk

A simple random walk begins at zero.

At each step, move up 1 with probability $$1/2$$ and down 1 with probability $$1/2$$.

<div class="viz" markdown="0">
  <canvas id="rw-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <button type="button" id="rw-go" class="res-filter" style="font-size:.72rem">Release 300 walkers</button>
    <button type="button" id="rw-clear" class="res-filter" style="font-size:.72rem">Clear</button>
    <span class="viz-value" id="rw-read"></span>
  </div>
  <p class="viz-caption">Each gray thread is one walker's fortune over 300 fair coin flips. Individually the paths are wild and unpredictable; collectively their endpoints pile into a bell centered at zero, with spread growing like the square root of the number of steps. One object, three upper-division courses: the settling is the Law of Large Numbers, the bell is the Central Limit Theorem, and the paths themselves are the subject of stochastic processes.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('rw-cv'), c = cv.getContext('2d');
  var read = document.getElementById('rw-read');
  var W = cv.width, H = cv.height, STEPS = 300, XEND = 540;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var ends = [], total = 0;
  function py(v){ return H/2 - v*3.2; }
  function drawHist(){
    c.clearRect(XEND + 2, 0, W - XEND - 2, H);
    var bins = {}, peak = 1;
    ends.forEach(function(e){ var b = Math.round(e/4); bins[b] = (bins[b]||0) + 1; peak = Math.max(peak, bins[b]); });
    for(var b in bins){
      var y = py(b*4), h = 12;
      var len = (W - XEND - 14)*bins[b]/peak;
      c.fillStyle = '#c9c9c6';
      c.fillRect(XEND + 6, y - h/2, len, h - 2);
    }
    c.strokeStyle = '#e0e0e0'; c.beginPath();
    c.moveTo(XEND + 3, 8); c.lineTo(XEND + 3, H - 8); c.stroke();
  }
  function release(){
    for(var w = 0; w < 300; w++){
      var v = 0;
      c.strokeStyle = 'rgba(31,31,31,0.05)'; c.lineWidth = 1;
      c.beginPath(); c.moveTo(0, py(0));
      for(var s = 1; s <= STEPS; s++){
        v += Math.random() < 0.5 ? 1 : -1;
        c.lineTo(XEND*s/STEPS, py(v));
      }
      c.stroke();
      ends.push(v);
    }
    total += 300;
    drawHist();
    read.textContent = total + ' walkers';
  }
  function clearAll(){
    c.clearRect(0, 0, W, H);
    c.strokeStyle = '#e0e0e0'; c.beginPath();
    c.moveTo(0, py(0)); c.lineTo(XEND, py(0)); c.stroke();
    ends = []; total = 0; read.textContent = '';
  }
  document.getElementById('rw-go').addEventListener('click', release);
  document.getElementById('rw-clear').addEventListener('click', clearAll);
  clearAll();
})();
</script>

Each path is unpredictable.

Across many walkers, the distribution of endpoints develops a recognizable shape.

After $$n$$ steps, the standard deviation of the endpoint is proportional to

$$\sqrt n.$$

That square-root scaling is related to the same probabilistic structure behind the Central Limit Theorem.

Random walks are also a starting point for stochastic processes, where randomness evolves over time rather than appearing as isolated independent events.

## Frequentist and Bayesian inference

AP Statistics is largely frequentist.

Parameters are treated as fixed.

Probability describes the sampling process.

That is why [a 95% confidence interval](/2026/07/25/what-95-percent-confident-means.html) is interpreted through the long-run behavior of the procedure rather than as a 95% probability that a fixed parameter lies in one finished interval.

Bayesian statistics uses a different probability model.

Unknown parameters are represented with probability distributions.

A prior distribution is updated with observed data to produce a posterior distribution.

The two frameworks answer uncertainty questions in different ways.

Upper-division study makes those assumptions explicit and allows the methods to be compared rather than treating one framework as the only form of inference.

## Regression becomes much larger

[Simple linear regression](/2026/07/30/least-squares-regression-influence.html) is the beginning of a broad family of models.

Multiple regression uses several predictors at once.

Logistic regression models the probability of a categorical outcome.

Generalized linear models extend the same framework to other response distributions.

Mixed models handle dependence created by repeated measurements or clustered observations.

Regularization methods such as ridge and lasso regression add penalties that can improve prediction and stabilize high-dimensional models.

Many ideas in machine learning develop naturally from this progression.

Trees, random forests, boosting, and neural networks use different model structures, but the same statistical questions remain.

How well does the method generalize?

What is the uncertainty?

Which features are informative?

What assumptions are being made?

## Mathematical statistics

Mathematical statistics studies the theory behind estimation and testing.

Instead of taking formulas for granted, it asks why an estimator has a particular sampling distribution and what properties make one estimator preferable to another.

Concepts such as bias, consistency, efficiency, sufficiency, likelihood, and asymptotic distribution become central.

The $$t$$-distribution and chi-square distribution are derived rather than supplied.

Critical values and standard errors become consequences of probability models.

The conditions taught in introductory statistics are then seen as practical versions of deeper mathematical assumptions.

## Randomness with memory

AP probability focuses heavily on independent events.

Many real systems have dependence over time.

Stochastic-process courses study models in which the next state depends on the current state or on the history of the process.

Markov chains are one example.

Queues, inventory systems, epidemic models, financial prices, and reliability processes provide others.

Brownian motion is a continuous stochastic process closely related to a scaled limit of random walks.

It plays an important role in probability theory and mathematical finance.

## Computation changes what can be done

Modern statistics uses computation alongside analytic theory.

The bootstrap estimates uncertainty by repeatedly resampling the observed data.

Permutation tests construct reference distributions by rearranging labels or residuals under a null hypothesis.

Monte Carlo methods approximate expectations and probabilities through simulation.

These approaches become especially useful when a clean formula is unavailable.

The randomization logic in introductory statistics is therefore not merely pedagogical.

It is part of a large class of computational methods used in modern research.

## What to bring with you

Two kinds of preparation matter.

The first is mathematical.

Calculus is needed for continuous probability distributions, likelihoods, optimization, and asymptotic theory.

Linear algebra is fundamental to regression, multivariate methods, and machine learning.

The second is statistical.

Study design, context, assumptions, and careful interpretation remain important even when the mathematics becomes more advanced.

<div class="article-note" markdown="1">
A technically sophisticated model cannot recover information the design never supplied. It also cannot turn an association into a causal effect without the assumptions needed for causal identification. That discipline carries directly from AP Statistics into the upper division.
</div>
