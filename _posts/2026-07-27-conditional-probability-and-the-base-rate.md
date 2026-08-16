---
layout: post
title: "Conditional probability and the base rate"
date: 2026-07-27
description: "Sensitivity and the probability of disease given a positive test are different conditional probabilities. Prevalence determines how far apart they can be."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: foundations
sequence: 6
interactive: true
blurb: "Sensitivity and the probability of disease given a positive test are different conditional probabilities. Prevalence determines how far apart they can be"
featured: true
image: "/assets/og/conditional-probability-and-the-base-rate.png"
---

Suppose a disease affects 1% of a population.

A screening test detects 99% of people who have the disease and correctly clears 95% of those who do not.

A person tests positive.

The probability that this person actually has the disease is about 17%, not 99%.

The difference comes from conditional probability and the low prevalence of the disease.

## Two conditional probabilities

Sensitivity is

$$P(\text{positive}\mid\text{disease}).$$

The question a patient usually wants answered is

$$P(\text{disease}\mid\text{positive}).$$

These probabilities reverse the condition.

They have different denominators and can have very different values.

Confusing them is an inverse-probability error.

## Draw the population

<div class="viz" markdown="0">
  <canvas id="br-cv" width="700" height="270"></canvas>
  <div class="viz-controls">
    <label for="br-prev">Prevalence</label>
    <input type="range" id="br-prev" min="1" max="100" step="1" value="10">
    <label for="br-sens">Sensitivity</label>
    <input type="range" id="br-sens" min="50" max="100" step="1" value="99">
    <label for="br-spec">Specificity</label>
    <input type="range" id="br-spec" min="50" max="100" step="1" value="95">
  </div>
  <div class="viz-controls"><span class="viz-value" id="br-read" style="min-width:100%"></span></div>
  <p class="viz-caption">Each square is one person in a population of 10,000. Black squares are true positives; gray squares are false positives; the faint field is everyone who tested negative. The readout computes the probability that a positive result is genuine, which is the black squares as a fraction of all shaded squares. At the default settings, gray squares outnumber black ones roughly five to one. Now raise the prevalence and watch the same test become trustworthy: the test never changed, only the population did. This is the base rate doing its quiet work.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('br-cv'), c = cv.getContext('2d');
  var sp = document.getElementById('br-prev'), ss = document.getElementById('br-sens'), sc = document.getElementById('br-spec');
  var read = document.getElementById('br-read');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var COLS = 125, ROWS = 80, N = COLS*ROWS;
  var cw = W/COLS, ch = H/ROWS;
  function draw(){
    var prev = sp.value/1000, sens = ss.value/100, spec = sc.value/100;
    var sick = Math.round(N*prev);
    var tp = Math.round(sick*sens);
    var fp = Math.round((N - sick)*(1 - spec));
    c.clearRect(0, 0, W, H);
    for(var i = 0; i < N; i++){
      var x = (i%COLS)*cw, y = Math.floor(i/COLS)*ch;
      if(i < tp) c.fillStyle = '#1f1f1f';
      else if(i < tp + fp) c.fillStyle = '#9a9a97';
      else c.fillStyle = '#f0f0ee';
      c.fillRect(x + 0.5, y + 0.5, cw - 1, ch - 1);
    }
    var ppv = tp + fp > 0 ? tp/(tp + fp) : 0;
    read.textContent = 'prevalence ' + (prev*100).toFixed(1) + '%   sensitivity ' + ss.value + '%   specificity ' + sc.value + '%   →   P(disease given positive) = ' + tp + '/' + (tp + fp) + ' ≈ ' + (ppv*100).toFixed(1) + '%';
  }
  [sp, ss, sc].forEach(function(s){ s.addEventListener('input', draw); });
  draw();
})();
</script>

The display represents 10,000 people.

At 1% prevalence, 100 people have the disease.

With 99% sensitivity, 99 of those people test positive.

The remaining 9,900 people do not have the disease.

With 95% specificity, 5% of that group tests positive incorrectly:

$$0.05(9900)=495.$$

So the positive group contains

$$99+495=594$$

people.

Only 99 actually have the disease.

Therefore

$$P(\text{disease}\mid\text{positive}) = \frac{99}{594} \approx0.167.$$

The calculation becomes much easier to reason about when the probabilities are converted into counts.

## Why prevalence matters

The test is good.

The disease is rare.

That means the healthy population is much larger than the diseased population.

A small false-positive rate applied to a very large group can therefore produce more false positives than a high sensitivity produces true positives.

Raise the prevalence while keeping the test characteristics fixed.

The probability that a positive result is genuine rises sharply.

The test did not improve.

The population changed.

This underlying prevalence is the base rate.

## Reading “given”

For a conditional probability,

$$P(A\mid B),$$

the event after the vertical bar is the condition.

It determines the denominator.

So

$$P(\text{disease}\mid\text{positive})$$

asks what fraction of positive tests come from people with the disease.

By contrast,

$$P(\text{positive}\mid\text{disease})$$

asks what fraction of diseased people receive positive tests.

A two-way table is often the safest way to keep those denominators separate.

## Bayes' theorem

<div class="article-note" markdown="1">
The same calculation can be written as

$$P(D\mid +) = \frac{P(+\mid D)P(D)} {P(+)}.$$

The denominator can be expanded as

$$P(+) = P(+\mid D)P(D) + P(+\mid D^c)P(D^c).$$

This is Bayes' theorem.

The population-count approach and the formula are doing the same calculation.

For many students, the count table is easier to interpret because each term corresponds to an actual subgroup.
</div>
