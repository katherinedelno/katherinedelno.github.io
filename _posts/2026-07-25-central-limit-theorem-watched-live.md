---
layout: post
title: "The Central Limit Theorem in simulation"
date: 2026-07-25
description: "Samples drawn from a heavily skewed population produce means that organize themselves into a normal curve. A simulation makes visible what the theorem claims, and what it does not."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: foundations
sequence: 7
interactive: true
blurb: "Draw samples from a skewed population and watch the means organize"
---

The Central Limit Theorem is the load-bearing wall of inference. Every confidence interval for a mean and every t-test in the course leans on it. Yet the statement sounds like a riddle: take samples from almost any population, however lopsided, and the distribution of the sample means will be approximately normal, with the approximation improving as the sample size grows.

The best way I know to believe it is to watch it happen.

## The simulator

The top panel shows the population: a strongly right-skewed distribution of individual values, something like household incomes or hospital stay lengths, with mean $$\mu = 20$$. The bottom panel starts empty. Each click draws a random sample of size $$n$$ from the population, computes the sample mean $$\bar{x}$$, and drops it into the bottom histogram.

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
  // right-skewed population: exponential-like, mean 20, clipped at 80
  function drawValue(){
    var v = -20*Math.log(1 - Math.random());
    return Math.min(v, HI - 0.01);
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

## What the theorem actually claims

Three separate statements are bundled inside the CLT, and the exam tests all three.

**Center.** The sampling distribution of $$\bar{x}$$ is centered at the population mean: $$\mu_{\bar{x}} = \mu$$. Sample means do not drift high or low on average, no matter the shape of the population and no matter the sample size. In the simulator, the bell forms around the dashed line at 20 from the very first samples.

**Spread.** The standard deviation of the sampling distribution is

$$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}.$$

Averaging tames variability, and it tames it by the square root of the sample size. That square root is why quadrupling your sample only doubles your precision, and it is the reason margin-of-error formulas all carry a $$\sqrt{n}$$ in the denominator.

**Shape.** This is the part that deserves the name "theorem." If the population is normal, $$\bar{x}$$ is exactly normal for every $$n$$. If the population is not normal, the distribution of $$\bar{x}$$ becomes approximately normal anyway as $$n$$ grows. The course's working guideline is $$n \ge 30$$ for populations as skewed as this one, and the simulator shows the guideline being earned: at $$n = 5$$ a trace of right skew survives, and by $$n = 30$$ it is gone to the eye.

Keep the three claims separate when you write. Center and spread are exact facts that hold for every sample size. Shape is the approximation, and it is the only part that needs the large-sample condition.

## The mistake the exam is designed to catch

The CLT is about the distribution of sample means. It says nothing about the individuals. Drawing a bigger sample does not make incomes, or hospital stays, or the population itself any more normal; set $$n = 1$$ and draw all day, and the bottom panel stays as skewed as the top. What becomes normal is the average, a statistic computed from many individuals at once.

This is exactly the distinction the free-response section probes. A question describing a skewed population and a sample of size 40 may ask for the probability that one randomly chosen individual exceeds some value, and that question is unanswerable with a normal calculation, because the individuals are not normal. The companion question about the sample mean is answerable, by the CLT. Deciding which tool applies is the tested skill, and the sentence that earns the point names the theorem and the condition: "since $$n = 40 \ge 30$$, the sampling distribution of $$\bar{x}$$ is approximately normal by the Central Limit Theorem."

<div class="article-note" markdown="1">
One more experiment worth running: set n = 4, draw 500, and note the spread of the bell. Then set n = 16 and draw 500 more. The bell is half as wide. The fourfold sample bought a twofold improvement, which is the square-root law seen with your own eyes, and it is the single most useful piece of intuition to carry into the margin-of-error questions.
</div>
