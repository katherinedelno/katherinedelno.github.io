---
layout: post
title: "The meaning of 95% confidence"
date: 2026-07-25
description: "A confidence level describes the method rather than any single interval. One hundred simulated studies make the distinction visible."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: foundations
sequence: 9
interactive: true
blurb: "Run a hundred studies and count which intervals capture the truth"
---

The most commonly missed interpretation question in AP Statistics is also the most commonly asked: what does "95% confident" mean? Students want it to mean "there is a 95% chance the true mean is in my interval." It does not mean that, the exam knows students want it to mean that, and the scoring guidelines are written to catch it. The distinction is easier to see than to say, so the simulation comes first.

## Build a hundred intervals

Each row below is a complete, honest study: a random sample of size 25 drawn from a population with true mean $$\mu = 50$$, followed by a 95% confidence interval computed from that sample alone. The dashed line marks the truth, which in real life nobody gets to see. Intervals that capture $$\mu$$ are gray; intervals that miss are black.

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

## The method has the probability, not the interval

Before you draw the sample, the process is random and probability applies: the procedure "sample, then build $$\bar{x} \pm 1.96\,\tfrac{\sigma}{\sqrt{n}}$$" will capture $$\mu$$ in 95% of its uses. That is a fact about the method, verified by the simulation above.

After you draw the sample, the randomness is spent. Your interval is now a fixed pair of numbers, say $$(47.1, 54.9)$$, and $$\mu$$ is a fixed number too. Either it is inside or it is not; there is no 95% about it, only our ignorance of which case we are in. What you are entitled to say is that you used a method that succeeds 95% of the time, and this interval is one of its outputs.

The AP-credited interpretation of the interval says exactly that, in context: "We are 95% confident that the true mean commute time for students at this school is between 47.1 and 54.9 minutes." The AP-credited interpretation of the level says what the simulation shows: "If we repeated this sampling process many times, about 95% of the intervals produced would capture the true mean."

## The wordings that lose the point

Each of the following appears on real student papers every year, and each earns zero for a specific reason.

"There is a 95% probability that $$\mu$$ is between 47.1 and 54.9." This assigns randomness to $$\mu$$, which is a fixed number. The probability belonged to the sampling process, and that process is over.

"95% of the data are in the interval." A confidence interval for a mean estimates where the mean is, not where individual observations fall. In the simulation, the population values spread from roughly 20 to 80, while the intervals are only a few units wide. An interval that contained 95% of individual values would be a different object entirely.

"95% of sample means fall in this interval." Close enough to sound right, and still wrong: [the reference distribution of sample means](/2026/07/25/central-limit-theorem-watched-live.html) is centered at $$\mu$$, not at your particular $$\bar{x}$$. Your interval is one draw, not the yardstick.

The interpretation that survives grading mentions repeated sampling, attaches the 95% to the method, and states the parameter in context. Three ingredients, one sentence.

## Why this is worth internalizing beyond the exam

Nearly every statistical claim you will meet in the wild, from polling margins to clinical trial results, arrives as a confidence interval. Reading one correctly means holding two thoughts at once: this particular range may well be wrong, and the process that produced it is reliable at a known rate. That is a genuinely useful way to hold beliefs, and the hundred little studies above are the entire argument for it.

<div class="article-note" markdown="1">
An exercise for the simulator: the intervals here all have the same width, since the population standard deviation is treated as known and the sample size is fixed. That is a teaching simplification — on the exam a mean is estimated with $$t$$, because $$\sigma$$ never is known, and the intervals then vary in width from sample to sample. Nothing about the interpretation changes; only the reference curve does. Now predict what changing the confidence level to 99% would do to the picture, then check your prediction against the formula. Wider intervals, fewer misses: confidence is purchased with width, which is why 100% confidence is available and useless.
</div>
