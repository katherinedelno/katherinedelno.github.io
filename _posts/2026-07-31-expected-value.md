---
layout: post
title: "Expected value is not a value you expect"
date: 2026-07-31
description: "The expected value of a fair die is 3.5, which is not a face the die has. It is a long-run average, and watching one settle explains why the binomial gets a shortcut."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: foundations
sequence: 7
interactive: true
blurb: "A long-run average, and often a number no outcome can produce"
image: "/assets/og/expected-value.png"
---

The expected value of a fair die is 3.5, which is not a face the die has. Nothing has gone wrong. The name is misleading in a way the definition is not, and unpicking the difference is most of what the topic asks.

The framework defines the quantity as a weighted sum, $$\mu_X = \textstyle\sum x_i \cdot P(x_i)$$, and then supplies the reading that makes it usable: the expected value can be interpreted as the *long-run average outcome* of the random variable. Not the likeliest outcome, not a typical outcome, not an outcome at all. An average, of a great many results, none of which need resemble it.

## Watch one settle

Each preset below is a probability distribution. The bars are the probabilities and the vertical line is $$\mu_X$$, computed from the definition rather than from the simulation.

<div class="viz" markdown="0">
  <div class="viz-controls" id="ev-modes"></div>
  <canvas id="ev-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <button type="button" class="res-filter" id="ev-100" style="font-size:.72rem">Draw 100</button>
    <button type="button" class="res-filter" id="ev-1k" style="font-size:.72rem">Draw 1,000</button>
    <button type="button" class="res-filter" id="ev-clr" style="font-size:.72rem">Reset</button>
    <span class="viz-value" id="ev-read" style="min-width:100%"></span>
  </div>
  <div class="ev-read" id="ev-panel"></div>
  <p class="viz-caption">Top: the probability distribution, with a dashed vertical at the expected value and short marks one standard deviation either side. Bottom: the running average of the outcomes drawn so far, against the number of trials, with the same expected value as a dashed target. The scale is logarithmic in the number of trials, because the interesting behavior is the settling and it happens over orders of magnitude. On three of the four presets the dashed vertical falls in the gap between two bars, so the running average converges to a number that no single trial can ever produce.</p>
  <style>
    .ev-read{margin:.9rem 0 0;padding-top:.8rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .ev-read .ev-lab{color:var(--muted);display:inline-block;min-width:16rem}
    .ev-read .ev-val{font-weight:700;display:inline-block;min-width:7rem}
    .ev-read .ev-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv = document.getElementById('ev-cv'), c = cv.getContext('2d');
  var read = document.getElementById('ev-read'), panel = document.getElementById('ev-panel');
  var modes = document.getElementById('ev-modes');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var INK = '#1f1f1f', MUTED = '#5c5c5c', LINE = '#e6e6e6', FAINT = '#9a9a97', PALE = '#c9c9c6';
  var FONT = 'Hanken Grotesk, sans-serif';
  var PADL = 44, PADR = 16, TOPA = 22, BASEA = 150, TOPB = 196, BASEB = 300;

  function binom(n, p){
    var vals = [], probs = [], k, lc = 0;
    for(k = 0; k <= n; k++){
      // log-factorial free: build the coefficient multiplicatively
      var cf = 1, j;
      for(j = 0; j < k; j++) cf = cf*(n - j)/(j + 1);
      vals.push(k); probs.push(cf*Math.pow(p, k)*Math.pow(1 - p, n - k));
    }
    return { vals: vals, probs: probs };
  }
  var P = [
    { lab: 'fair die', vals: [1,2,3,4,5,6], probs: [1/6,1/6,1/6,1/6,1/6,1/6],
      note: 'six equally likely faces' },
    { lab: 'binomial n = 5, p = 0.5', d: binom(5, 0.5), note: 'five fair coin flips, counting heads' },
    { lab: 'binomial n = 10, p = 0.3', d: binom(10, 0.3), note: 'ten trials, success rate 0.3' },
    { lab: 'raffle ticket', vals: [0,10,100], probs: [0.94,0.05,0.01],
      note: 'a prize of 100 with probability 0.01, a prize of 10 with probability 0.05' }
  ];
  P.forEach(function(p){ if(p.d){ p.vals = p.d.vals; p.probs = p.d.probs; } });
  var mode = 0, run = [], total = 0, count = 0;

  function moments(p){
    var m = 0, i;
    for(i = 0; i < p.vals.length; i++) m += p.vals[i]*p.probs[i];
    var v = 0;
    for(i = 0; i < p.vals.length; i++) v += (p.vals[i] - m)*(p.vals[i] - m)*p.probs[i];
    return { mu: m, sd: Math.sqrt(v) };
  }
  function drawOne(p){
    var u = Math.random(), acc = 0, i;
    for(i = 0; i < p.vals.length; i++){ acc += p.probs[i]; if(u <= acc) return p.vals[i]; }
    return p.vals[p.vals.length - 1];
  }
  function simulate(k){
    var p = P[mode], i;
    for(i = 0; i < k; i++){
      total += drawOne(p); count++;
      if(count <= 40 || count % Math.ceil(count/240) === 0) run.push([count, total/count]);
    }
    draw();
  }

  function draw(){
    var p = P[mode], mo = moments(p), i;
    var lo = p.vals[0] - 0.8, hi = p.vals[p.vals.length - 1] + 0.8;
    function px(x){ return PADL + (x - lo)/(hi - lo)*(W - PADL - PADR); }
    var pmax = Math.max.apply(null, p.probs);

    c.clearRect(0, 0, W, H);
    c.font = '700 10px ' + FONT;

    // distribution
    var bw = Math.min(46, (W - PADL - PADR)/(p.vals.length*1.7));
    for(i = 0; i < p.vals.length; i++){
      var h = (p.probs[i]/pmax)*(BASEA - TOPA - 12);
      c.fillStyle = '#d8d8d5';
      c.fillRect(px(p.vals[i]) - bw/2, BASEA - h, bw, h);
    }
    c.strokeStyle = LINE; c.lineWidth = 1;
    c.beginPath(); c.moveTo(PADL, BASEA + 0.5); c.lineTo(W - PADR, BASEA + 0.5); c.stroke();
    c.fillStyle = MUTED; c.textAlign = 'center';
    for(i = 0; i < p.vals.length; i++){
      if(p.vals.length <= 12 || i % 2 === 0) c.fillText(String(p.vals[i]), px(p.vals[i]), BASEA + 14);
    }
    // one standard deviation either side
    c.strokeStyle = PALE; c.lineWidth = 1.4;
    [mo.mu - mo.sd, mo.mu + mo.sd].forEach(function(x){
      if(x < lo || x > hi) return;
      c.beginPath(); c.moveTo(px(x), BASEA - 6); c.lineTo(px(x), BASEA + 6); c.stroke();
    });
    // the expected value
    c.strokeStyle = INK; c.lineWidth = 1.6; c.setLineDash([5, 3]);
    c.beginPath(); c.moveTo(px(mo.mu), TOPA - 4); c.lineTo(px(mo.mu), BASEA); c.stroke();
    c.setLineDash([]);
    c.fillStyle = INK; c.font = '700 11px ' + FONT;
    c.fillText('μ = ' + mo.mu.toFixed(2), px(mo.mu), TOPA - 9);

    // running average, logarithmic in trial number
    c.strokeStyle = LINE; c.lineWidth = 1;
    c.beginPath(); c.moveTo(PADL, BASEB + 0.5); c.lineTo(W - PADR, BASEB + 0.5); c.stroke();
    var YLO = mo.mu - 2.2*mo.sd, YHI = mo.mu + 2.2*mo.sd;
    function qy(y){ return BASEB - (y - YLO)/(YHI - YLO)*(BASEB - TOPB); }
    function qx(n){ return PADL + Math.log10(Math.max(n,1))/3*(W - PADL - PADR); }
    c.strokeStyle = FAINT; c.setLineDash([4, 3]); c.lineWidth = 1.2;
    c.beginPath(); c.moveTo(PADL, qy(mo.mu)); c.lineTo(W - PADR, qy(mo.mu)); c.stroke();
    c.setLineDash([]);
    c.fillStyle = MUTED; c.font = '700 10px ' + FONT; c.textAlign = 'center';
    [1, 10, 100, 1000].forEach(function(n){ c.fillText(n.toLocaleString(), qx(n), BASEB + 14); });
    c.textAlign = 'right'; c.fillText('trials', W - PADR, TOPB - 6);
    if(run.length > 1){
      c.strokeStyle = INK; c.lineWidth = 1.8; c.beginPath();
      run.forEach(function(pt, i){
        var y = Math.max(YLO, Math.min(YHI, pt[1]));
        i ? c.lineTo(qx(pt[0]), qy(y)) : c.moveTo(qx(pt[0]), qy(y));
      });
      c.stroke();
    }

    var attain = p.vals.some(function(v){ return Math.abs(v - mo.mu) < 1e-9; });
    read.textContent = count
      ? count.toLocaleString() + ' trials drawn, running average ' + (total/count).toFixed(4)
      : 'no trials drawn yet';
    panel.innerHTML =
      '<div><span class="ev-lab">expected value &mu;</span><span class="ev-val">' + mo.mu.toFixed(4) +
        '</span><span class="ev-note">' + (attain
          ? 'a value the variable can actually take'
          : 'no outcome of this variable equals it') + '</span></div>' +
      '<div><span class="ev-lab">standard deviation &sigma;</span><span class="ev-val">' + mo.sd.toFixed(4) +
        '</span><span class="ev-note">' + p.note + '</span></div>';
  }

  P.forEach(function(p, i){
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'res-filter' + (i === 0 ? ' is-active' : '');
    b.style.fontSize = '.72rem'; b.textContent = p.lab;
    b.addEventListener('click', function(){
      mode = i; run = []; total = 0; count = 0;
      Array.prototype.forEach.call(modes.children, function(o, j){
        o.classList[j === i ? 'add' : 'remove']('is-active');
      });
      draw();
    });
    modes.appendChild(b);
  });
  document.getElementById('ev-100').addEventListener('click', function(){ simulate(100); });
  document.getElementById('ev-1k').addEventListener('click', function(){ simulate(1000); });
  document.getElementById('ev-clr').addEventListener('click', function(){
    run = []; total = 0; count = 0; draw();
  });
  draw();
})();
</script>

## Three of the four are unreachable

The die averages 3.5. Five fair coin flips average 2.5 heads. A raffle ticket that pays 100 one time in a hundred and 10 one time in twenty is worth 1.50, and no ticket has ever been worth 1.50. In each case the dashed line lands in the gap between two bars, and the running average underneath walks toward it anyway.

Only the third preset, ten trials at a success rate of 0.3, produces an expected value that an outcome can equal — and even there, three successes is merely the likeliest of eleven possibilities, not something to be expected in any ordinary sense.

The standard deviation is the companion measurement and the framework gives it the same long-run reading: a typical deviation of the values from the mean, over the long run. The two short marks beside the dashed line are one such deviation either side. On the raffle they are far outside the picture, because a distribution that is almost always zero and occasionally 100 has a standard deviation of about 10 against a mean of 1.50 — which is the honest description of a lottery, and the reason expected value alone is a poor summary of one.

## Why the binomial gets a shortcut

For most distributions, finding $$\mu_X$$ means doing the weighted sum term by term. The binomial is exempted, and the exemption is worth understanding rather than memorizing.

A binomial random variable counts successes in $$n$$ repeated independent trials, each with two outcomes and the same probability $$p$$ of success. Because the trials are identical and independent, each one contributes the same amount to the total on average, and the framework can state the result outright:

$$\mu_X = np, \qquad \sigma_X = \sqrt{np(1-p)}.$$

Check it against the tool. For ten trials at $$p = 0.3$$ the shortcut gives $$\mu = 3$$ and $$\sigma = \sqrt{2.1} \approx 1.4491$$, and the term-by-term sums over all eleven outcomes return the same two numbers. The shortcut is not an approximation.

## The four conditions, and what breaks them

The shortcut is available only when the variable really is binomial, and the definition carries four requirements: a fixed number of trials, two outcomes per trial, the same probability of success on every trial, and independence between trials.

Drawing cards without replacement breaks the third and fourth at once, since each draw changes what is left. Counting how many trials it takes to get a first success breaks the first, because the number of trials is not fixed in advance — and that variable, once part of this course, is no longer in it, which is worth knowing if you are working from an older review book. Asking each subject a question with three possible answers breaks the second until the categories are collapsed to two.

Justifying that a variable *is* binomial is its own learning objective, so the four conditions are a sentence to write rather than a box to tick.

<div class="article-note" markdown="1">
A check worth running on the raffle: draw a hundred trials, note the running average, then draw a thousand more and note it again. The number often moves *away* from 1.50 before it comes back, because a single hundred-pound prize arriving late in a short run drags the average up by a full point. That is not the law of large numbers failing. It is the law of large numbers being a statement about the long run only, and the reason a distribution this skewed needs both of its parameters reported rather than just the first.
</div>
