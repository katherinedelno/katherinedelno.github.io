---
layout: post
title: "Buffon's needle and the estimation of pi"
date: 2026-07-27
description: "Drop needles on a lined floor and count the crossings, and the number pi emerges from pure chance. A 1777 problem that connects probability, geometry, and simulation."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: beyond
sequence: 61
interactive: true
---

In 1777, Georges-Louis Leclerc, Comte de Buffon, posed a question about a parlor game: if a needle is dropped at random onto a floor of parallel boards, what is the probability that it comes to rest crossing one of the cracks? The answer turned out to contain $$\pi$$, which means the game can be run in reverse. Drop many needles, count how often they cross a line, and the count estimates $$\pi$$ itself, extracted from randomness by nothing more than arithmetic.

The result is worth knowing for its own sake, and it is also a perfect miniature of an idea at the center of modern statistics: that simulation can compute quantities which have nothing visibly random about them.

## The setup and the answer

Rule a floor with parallel lines a distance $$d$$ apart, and drop a needle of length $$\ell$$, with $$\ell \le d$$, so that its position and angle are entirely random. Buffon showed that

$$P(\text{needle crosses a line}) = \frac{2\ell}{\pi d}$$

The appearance of $$\pi$$ is not mystical. A dropped needle has a random angle, angles live on a circle, and averaging over all angles drags the circle's constant into the answer. The derivation is a short exercise in a college probability course, and for BC students it is a pleasant surprise: the average of $$\sin\theta$$ over all angles is computed with an integral, so the formula is calculus and probability shaking hands.

If the needle's length is exactly half the spacing, so $$\ell = \tfrac{d}{2}$$, the formula collapses to $$P = \tfrac{1}{\pi}$$. A needle crosses a line about 31.8% of the time, and the estimate becomes

$$\pi \approx \frac{\text{number of drops}}{\text{number of crossings}}$$

## The experiment

The floor below uses that half-spacing needle. Drop them by the hundred and watch the estimate close in.

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

## Why a statistics student should care

The needle is the ancestor of the **Monte Carlo method**, the technique of computing a fixed, deterministic quantity by designing a random experiment whose long-run behavior encodes it. The Law of Large Numbers guarantees the convergence: the proportion of crossings must settle toward $$\tfrac{1}{\pi}$$, so the reciprocal must settle toward $$\pi$$. Every simulation in the AP course, from randomization distributions to simulated p-values, runs on exactly this engine, and the investigative-task questions that ask students to interpret a simulation are asking them to reason the way Buffon's floor does.

The slow convergence carries its own lesson. The estimate's error shrinks in proportion to $$\tfrac{1}{\sqrt{n}}$$, which is the same $$\sqrt{n}$$ that sits in the denominator of every standard error formula in the course. A political poll of 1,000 people and a floor of 1,000 needles are bound by the same arithmetic, and neither can be made ten times more precise without one hundred times the effort.

<div class="article-note" markdown="1">
A historical footnote with a caution attached: in 1901 the Italian mathematician Mario Lazzarini reported tossing a needle 3,408 times and obtaining pi to six decimal places, a result far too accurate for the number of trials. His needle-to-spacing ratio was chosen so that a particular lucky count would reproduce the famous fraction 355/113, and the trial count appears to have been chosen to stop at the right moment. The episode is now a standard example in the study of suspicious data, which makes it, fittingly, a statistics lesson twice over.
</div>
