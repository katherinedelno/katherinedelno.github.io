---
layout: post
title: "The meaning of 95% confidence"
date: 2026-07-25
description: "A confidence level describes the long-run success rate of the interval-producing method, not a probability attached to one finished interval."
course: "AP Statistics"
read_time: "5 min read"
math: true
kind: foundations
sequence: 11
interactive: true
blurb: "A confidence level describes the long-run success rate of the interval-producing method, not a probability attached to one finished interval"
featured: true
image: "/assets/og/what-95-percent-confident-means.png"
---

A 95% confidence interval does not mean that there is a 95% probability the fixed population parameter lies inside one particular interval. The 95% describes the method used to generate intervals, and under repeated sampling, that method captures the true parameter about 95% of the time.

## Build one hundred intervals

Each row below represents a new random sample of size 25 from a population with $$\mu=50$$, and a 95% confidence interval is constructed from each sample.

<div class="viz" markdown="0">
  <canvas id="ci-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <button type="button" id="ci-go" class="res-filter" style="font-size:.72rem">Run 100 new studies</button>
    <span class="viz-value" id="ci-read"></span>
  </div>
  <p class="viz-caption">Each horizontal segment is one study's interval, with a dot at its sample mean. Run the studies a few times. The capture count hovers near 95 out of 100, sometimes 92, sometimes 98, and the misses land on both sides. No single interval knows whether it is a gray one or a black one. That ignorance is exactly what the phrase "95% confident" is compensating for.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('ci-cv'), c = cv.getContext('2d');
  var read = document.getElementById('ci-read');
  var W = cv.width, H = cv.height, pad = 40;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var MU = 50, SIGMA = 10, N = 25, Z = 1.96;
  var XLO = 42, XHI = 58;
  function px(x){ return pad + (x - XLO)/(XHI - XLO)*(W - 2*pad); }
  function gauss(){
    var u = 1 - Math.random(), v = Math.random();
    return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);
  }
  function run(){
    c.clearRect(0, 0, W, H);
    var mx = px(MU);
    c.strokeStyle = '#5c5c5c'; c.setLineDash([4,3]); c.beginPath();
    c.moveTo(mx, 8); c.lineTo(mx, H - 8); c.stroke(); c.setLineDash([]);
    c.fillStyle = '#5c5c5c'; c.font = '700 12px Hanken Grotesk, sans-serif';
    c.fillText('μ = 50', mx + 6, 16);
    var hits = 0, rows = 100, half = Z*SIGMA/Math.sqrt(N);
    for(var i = 0; i < rows; i++){
      var sum = 0;
      for(var k = 0; k < N; k++) sum += MU + SIGMA*gauss();
      var xbar = sum/N, lo = xbar - half, hi = xbar + half;
      var captured = (lo <= MU && MU <= hi);
      if(captured) hits++;
      var y = 24 + (H - 36)*i/rows;
      c.strokeStyle = captured ? '#c9c9c6' : '#1f1f1f';
      c.lineWidth = captured ? 1.6 : 2.4;
      c.beginPath(); c.moveTo(px(lo), y); c.lineTo(px(hi), y); c.stroke();
      c.fillStyle = captured ? '#a9a9a5' : '#1f1f1f';
      c.beginPath(); c.arc(px(xbar), y, 1.8, 0, 7); c.fill();
    }
    read.textContent = hits + ' of 100 captured μ';
  }
  document.getElementById('ci-go').addEventListener('click', run);
  run();
})();
</script>

The dashed vertical line marks the true mean, and intervals that contain $$\mu$$ are distinguished from those that miss. Run the simulation several times. The number of successful intervals varies from run to run, but it tends to stay near 95 out of 100, and that is the confidence level in repeated use.

## The probability belongs to the procedure

Before a sample is drawn, the interval is random because the sample is random. A procedure such as $$\bar x \pm 1.96\tfrac{\sigma}{\sqrt n}$$ has a 95% long-run capture rate under its assumptions. After the sample is drawn, the interval endpoints are fixed, and the parameter is also fixed. For that particular interval, the parameter is either inside or outside, and the frequentist confidence statement does not assign a 95% probability to that fixed event.

A correct contextual interpretation is: “We are 95% confident that the true mean commute time for students at this school lies between 47.1 and 54.9 minutes.” An interpretation of the confidence level is: “If this sampling process were repeated many times, about 95% of the intervals produced would contain the true mean commute time.”

## Three common misinterpretations

## “There is a 95% probability that $$\mu$$ is in this interval.”

In the frequentist framework used in AP Statistics, $$\mu$$ is fixed. The probability statement applies to the random interval-producing process before the sample is observed.

## “95% of the data are in the interval.”

A confidence interval for a mean estimates the population mean. It does not describe the range containing 95% of individual observations.

## “95% of sample means fall in this interval.”

The interval is centered on one observed sample statistic, and it is not a fixed reference range for all possible sample means. The [sampling distribution](/2026/07/25/central-limit-theorem-watched-live.html) of $$\bar X$$ is centered at $$\mu$$, not at the particular $$\bar x$$ observed in one sample.

## Confidence level and width

A higher confidence level requires a larger critical value, and that produces a wider interval. So increasing confidence generally reduces the chance of missing the parameter by accepting less precision. A 99% interval is wider than a 95% interval based on the same data and method, and this tradeoff is part of what a confidence level means.

## What changes with $$t$$

<div class="article-note" markdown="1">
The simulation treats the population standard deviation as known so that all intervals have the same width. For inference about a mean in AP Statistics, $$\sigma$$ is typically unknown, so we estimate it with $$s$$ and use a $$t$$-distribution. The interval widths then vary because $$s$$ varies from sample to sample, and the interpretation of confidence does not change.
</div>
