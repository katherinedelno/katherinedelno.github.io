---
layout: post
title: "The Central Limit Theorem in simulation"
date: 2026-07-25
description: "Sample means from a skewed population become increasingly normal as sample size grows, while their spread decreases according to 1/√n."
course: "AP Statistics"
read_time: "5 min read"
math: true
kind: foundations
sequence: 8
interactive: true
blurb: "Sample means from a skewed population become increasingly normal as sample size grows, while their spread decreases according to 1/√n"
image: "/assets/og/central-limit-theorem-watched-live.png"
---

The Central Limit Theorem explains why normal distributions appear throughout inference even when the population itself is not normal. Take repeated random samples from a population and compute a mean from each sample. As the sample size grows, the distribution of those sample means becomes approximately normal under broad conditions, and the center and spread also follow specific rules.

## The simulator

The upper panel shows a strongly right-skewed population with mean $$\mu=20$$, and the lower panel collects sample means.

<div class="viz" markdown="0">
  <canvas id="clt-pop" width="700" height="150"></canvas>
  <canvas id="clt-means" width="700" height="190" style="margin-top:10px"></canvas>
  <div class="viz-controls">
    <label for="clt-n">n</label>
    <input type="range" id="clt-n" min="1" max="60" step="1" value="1">
    <button type="button" id="clt-one" class="res-filter" style="font-size:.72rem">Draw 1 sample</button>
    <button type="button" id="clt-many" class="res-filter" style="font-size:.72rem">Draw 500</button>
    <button type="button" id="clt-clear" class="res-filter" style="font-size:.72rem">Clear</button>
    <span class="viz-value" id="clt-read"></span>
  </div>
  <p class="viz-caption"><strong>Top:</strong> the population of individual values, skewed hard to the right. <strong>Bottom:</strong> the distribution of sample means. Three experiments to run. First, set n = 1 and draw 500: the bottom panel just reproduces the population, skew and all. Second, set n = 5 and draw 500: the skew is already fading. Third, set n = 30 and draw 500: the means pile into a tight, nearly symmetric bell centered at the population mean, even though no individual value was drawn from anything bell-shaped. Also watch the width: each fourfold increase in n cuts the spread of the bell in half.</p>
</div>

<script>
(function(){
  var popCv = document.getElementById('clt-pop'), mCv = document.getElementById('clt-means');
  var pc = popCv.getContext('2d'), mc = mCv.getContext('2d');
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  [popCv, mCv].forEach(function(k){ k.width *= d__; k.height *= d__; });
  var nSl = document.getElementById('clt-n'), read = document.getElementById('clt-read');
  var LO = 0, HI = 80, BINS = 60;
  // Right-skewed population: exponential with mean exactly 20. The values are
  // deliberately not clipped at the right edge of the histogram — clipping would
  // pile the tail into the last bin and drag the true mean down to 19.63, below
  // the 20 the marker claims. The thin tail past 80 simply falls outside the
  // bins, which is a fact about the drawing rather than about the population.
  function drawValue(){
    return -20*Math.log(1 - Math.random());
  }
  var means = [];
  function hist(canvas, ctx, data, label, maxBarsNorm){
    var W = canvas.width/d__, H = canvas.height/d__, pad = 30;
    ctx.setTransform(d__, 0, 0, d__, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ctx.strokeStyle = '#e0e0e0'; ctx.beginPath();
    ctx.moveTo(pad, H - 22); ctx.lineTo(W - pad, H - 22); ctx.stroke();
    var bins = new Array(BINS).fill(0), i;
    for(i = 0; i < data.length; i++){
      var b = Math.floor((data[i] - LO)/(HI - LO)*BINS);
      if(b >= 0 && b < BINS) bins[b]++;
    }
    var peak = Math.max.apply(null, bins) || 1;
    for(i = 0; i < BINS; i++){
      var x0 = pad + (W - 2*pad)*i/BINS, w = (W - 2*pad)/BINS - 1;
      var h = (H - 40)*bins[i]/peak;
      ctx.fillStyle = '#d6d6d3';
      ctx.fillRect(x0, H - 22 - h, w, h);
    }
    // mu marker at 20
    var mx = pad + (W - 2*pad)*(20 - LO)/(HI - LO);
    ctx.strokeStyle = '#1f1f1f'; ctx.setLineDash([4,3]); ctx.beginPath();
    ctx.moveTo(mx, 12); ctx.lineTo(mx, H - 22); ctx.stroke(); ctx.setLineDash([]);
    ctx.fillStyle = '#5c5c5c'; ctx.font = '700 12px Hanken Grotesk, sans-serif';
    ctx.fillText(label, pad + 4, 16);
    ctx.fillText('μ = 20', mx + 6, 16);
  }
  var popData = [];
  for(var i = 0; i < 8000; i++) popData.push(drawValue());
  function refresh(){
    hist(popCv, pc, popData, 'Population (individuals)');
    hist(mCv, mc, means, 'Sample means (n = ' + nSl.value + ')');
    read.textContent = means.length + ' means';
  }
  function drawSamples(count){
    var n = +nSl.value;
    for(var s = 0; s < count; s++){
      var sum = 0;
      for(var k = 0; k < n; k++) sum += drawValue();
      means.push(sum/n);
    }
    refresh();
  }
  document.getElementById('clt-one').addEventListener('click', function(){ drawSamples(1); });
  document.getElementById('clt-many').addEventListener('click', function(){ drawSamples(500); });
  document.getElementById('clt-clear').addEventListener('click', function(){ means = []; refresh(); });
  nSl.addEventListener('input', function(){ means = []; refresh(); });
  refresh();
})();
</script>

Set $$n=1$$. Each sample mean is just one observation, so the lower distribution reproduces the skew of the population. Increase $$n$$ to 5 and the distribution of sample means becomes less skewed. At $$n=30$$, it is much closer to a normal shape, and at the same time, the distribution becomes narrower.

## Center

For a random sample, $$\mu_{\bar X}=\mu$$, so the sampling distribution of the sample mean is centered at the population mean. This is true regardless of the sample size, and the sample mean is an unbiased estimator of the population mean under the random-sampling setup.

## Spread

The standard deviation of the sampling distribution is $$\sigma_{\bar X} = \tfrac{\sigma}{\sqrt{n}}$$, assuming the observations are independent or the sampling fraction is sufficiently small. As $$n$$ increases, sample means vary less from sample to sample. The square root matters, and to cut the standard deviation in half, the sample size must be multiplied by four. That same relationship appears later in standard errors and [margins of error](/2026/07/25/what-95-percent-confident-means.html).

## Shape

If the population is normal, the sampling distribution of $$\bar X$$ is normal for every sample size. If the population is not normal, the Central Limit Theorem tells us that the sampling distribution becomes approximately normal as $$n$$ grows, provided the usual conditions are met. The amount of sample size needed depends on the population shape, and a strongly skewed population generally requires a larger $$n$$ than a roughly symmetric one. The common $$n\ge30$$ rule is a course-level guideline, not a universal mathematical boundary.

## What becomes normal

The Central Limit Theorem is about a sampling distribution. It does not say that a large random sample makes the population values themselves normally distributed, and the individual observations can remain strongly skewed. What becomes approximately normal is the statistic $$\bar X$$.

This distinction matters when choosing a probability model. A probability question about one individual from a skewed population may not be suitable for a normal approximation, while a question about the mean of a sufficiently large random sample may be.

## A square-root experiment

<div class="article-note" markdown="1">
Compare sample sizes 4 and 16. Since $$\sqrt{16}=2\sqrt4$$, the sampling distribution at $$n=16$$ should have half the standard deviation of the one at $$n=4$$. The simulation shows that narrowing directly, and the fourfold increase in sample size buys a twofold reduction in sampling variability.
</div>
