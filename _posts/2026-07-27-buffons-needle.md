---
layout: post
title: "Buffon's needle and the estimation of pi"
date: 2026-07-27
description: "Drop a needle across parallel lines, count the crossings, and a geometric probability produces an estimate of π."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: beyond
sequence: 3
interactive: true
blurb: "Drop a needle across parallel lines, count the crossings, and a geometric probability produces an estimate of π"
image: "/assets/og/buffons-needle.png"
---

A geometric probability experiment can be used to estimate $$\pi$$. Draw parallel lines a fixed distance apart, drop a needle at random, and record whether the needle crosses one of the lines. The long-run crossing proportion is related to $$\pi$$.

## The probability

Let the needle length be $$\ell$$ and let the distance between adjacent parallel lines be $$d$$, with $$\ell\le d$$. Under the usual random-position and random-angle assumptions,

$$P(\text{crossing}) = \frac{2\ell}{\pi d}$$

If we choose $$\ell=\tfrac d2$$, then $$P(\text{crossing}) = \tfrac1\pi$$. So after many drops, $$\tfrac{\text{crossings}}{\text{drops}} \approx \tfrac1\pi$$, and rearranging gives $$\pi \approx \tfrac{\text{drops}}{\text{crossings}}$$.

<div class="viz" markdown="0">
  <canvas id="bn-cv" width="700" height="280"></canvas>
  <div class="viz-controls">
    <button type="button" id="bn-100" class="res-filter" style="font-size:.72rem">Drop 100</button>
    <button type="button" id="bn-1000" class="res-filter" style="font-size:.72rem">Drop 1,000</button>
    <button type="button" id="bn-clear" class="res-filter" style="font-size:.72rem">Reset</button>
    <span class="viz-value" id="bn-read"></span>
  </div>
  <p class="viz-caption">Needles that cross a line are drawn dark; needles that land clear are faint. The readout divides drops by crossings to estimate pi. The first hundred needles usually land within a few tenths of the truth; ten thousand may get two decimal places, on a lucky day. Notice how slowly the precision improves. Cutting the error in half requires roughly four times the needles, the same square-root law that governs margins of error in polling, and a preview of why real surveys cannot buy accuracy cheaply.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('bn-cv'), c = cv.getContext('2d');
  var read = document.getElementById('bn-read');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var D = 56, L = D/2;
  var drops = 0, hits = 0;
  function lines(){
    c.strokeStyle = '#d8d8d5'; c.lineWidth = 1;
    for(var y = 0; y <= H; y += D){
      c.beginPath(); c.moveTo(0, y + 0.5); c.lineTo(W, y + 0.5); c.stroke();
    }
  }
  function drop(n){
    for(var i = 0; i < n; i++){
      var cx = Math.random()*W;
      var cy = Math.random()*H;
      var th = Math.random()*Math.PI;
      var dy = (L/2)*Math.sin(th), dx = (L/2)*Math.cos(th);
      var y1 = cy - dy, y2 = cy + dy;
      var crosses = Math.floor(y1/D) !== Math.floor(y2/D);
      if(crosses) hits++;
      drops++;
      c.strokeStyle = crosses ? 'rgba(31,31,31,0.75)' : 'rgba(31,31,31,0.14)';
      c.lineWidth = 1.2;
      c.beginPath(); c.moveTo(cx - dx, y1); c.lineTo(cx + dx, y2); c.stroke();
    }
    var est = hits > 0 ? drops/hits : 0;
    read.textContent = drops + ' drops, ' + hits + ' crossings' + (hits > 0 ? ',  estimate of pi: ' + est.toFixed(4) : '');
  }
  function reset(){
    c.clearRect(0, 0, W, H); lines();
    drops = 0; hits = 0; read.textContent = '';
  }
  document.getElementById('bn-100').addEventListener('click', function(){ drop(100); });
  document.getElementById('bn-1000').addEventListener('click', function(){ drop(1000); });
  document.getElementById('bn-clear').addEventListener('click', reset);
  reset();
})();
</script>

The dark needles cross a line, and the running estimate changes after every batch. With a small number of drops it can wander considerably, and with more drops it tends to settle closer to $$\pi$$.

## Why the formula contains $$\pi$$

Two random quantities determine whether a needle crosses a line. One is the distance from the needle's center to the nearest line, and the other is the angle of the needle. If the angle is $$\theta$$, half of the needle's vertical reach is $$\tfrac{\ell}{2}\vert\sin\theta\vert$$, and a crossing occurs when the center lies close enough to a line that this vertical reach can touch it.

Averaging that condition over all possible positions and angles produces the factor involving $$\pi$$. The constant appears because the experiment contains a uniformly random orientation.

## This is Monte Carlo estimation

The experiment is an early example of what is now called a Monte Carlo method. A quantity that is difficult to compute directly is expressed as a probability, and that probability is then estimated by repeated random trials. The law of large numbers explains why the empirical crossing proportion approaches the theoretical crossing probability.

The simulation does not derive $$\pi$$. It estimates a probability whose exact value happens to contain $$\pi$$.

## More trials help slowly

Random error usually decreases at a rate proportional to $$\tfrac1{\sqrt n}$$, and that square-root rate is important. To reduce the typical sampling error by a factor of ten, we need roughly one hundred times as many trials. A million simulated needles therefore gives a much more stable estimate than a hundred needles, but the improvement is not proportional to the increase in sample size. This is the same square-root behavior that appears in standard errors throughout statistics.

## A historical caution

Buffon's needle was proposed in the eighteenth century and has been physically performed many times since. One famous experiment was reported by Mario Lazzarini in 1901, and he claimed an estimate of $$\pi$$ correct to six decimal places after only a few thousand needle tosses. That accuracy is implausibly good for a random experiment of that size, and later discussions have noted that the reported counts appear unusually well chosen.

The episode is a useful statistical caution. Stopping rules, selective reporting, or choosing a favorable result after looking at the data can make an estimate appear much more precise than its sampling process justifies, and the mechanism matters as much as the final number.

## A useful comparison

Suppose you run the simulation twice with the same number of drops. The estimates will not be identical, and that variation is part of the experiment.

<div class="article-note" markdown="1">
The appropriate question is not whether one run reproduces $$\pi$$ to several decimal places. It is whether the estimator behaves as expected across repeated runs and becomes more stable as the number of trials increases, and that is the statistical content of the experiment.
</div>
