---
layout: post
title: "Expected value is not a value you expect"
date: 2026-07-31
description: "Expected value is a probability-weighted long-run average. It need not be a possible outcome of a single trial."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: foundations
sequence: 7
interactive: true
blurb: "Expected value is a probability-weighted long-run average. It need not be a possible outcome of a single trial"
image: "/assets/og/expected-value.png"
---

The expected value of a fair six-sided die is $$3.5$$, and no roll can produce 3.5. That is not a problem with the definition. Expected value is a long-run average, not a prediction of the next outcome.

## The definition

For a discrete random variable $$X$$,

$$\mu_X = E(X) = \sum x_iP(X=x_i)$$

Each possible value is weighted by its probability, and the result describes where the average of many independent repetitions will tend over the long run. It does not have to be one of the values the random variable can actually take.

## Watch the average settle

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

The upper panel shows the probability distribution, and the dashed vertical line marks the theoretical expected value. The lower panel shows the running average of simulated outcomes, and with more trials, the running average tends to move toward the theoretical mean.

For several presets, the expected value lies between possible outcomes. The running average can still converge to that value because an average is not itself required to be an observed outcome.

## Examples

For a fair die, $$E(X) = \tfrac{1+2+3+4+5+6}{6} = 3.5$$, and for the number of heads in five fair coin flips, $$E(X)=2.5$$. Again, 2.5 heads is impossible in one repetition.

A raffle can have an expected value of \$1.50 even if no ticket pays \$1.50. The mean describes the probability distribution as a whole, and it does not identify the most likely outcome.

## Standard deviation matters too

Expected value alone can hide substantial risk or variability. The standard deviation of a random variable describes the typical distance of outcomes from the mean over repeated trials, and a lottery may have a small positive expected value but a large standard deviation because almost every outcome is near zero and a very small fraction are extremely large.

Two random variables with the same expected value can therefore behave very differently. The mean describes location, and the standard deviation describes spread.

## The binomial shortcuts

For a binomial random variable with $$n$$ trials and success probability $$p$$,

$$\mu_X=np \qquad\text{and}\qquad \sigma_X = \sqrt{np(1-p)}$$

For example, if $$n=10$$ and $$p=0.3$$, then $$\mu_X=3\;\text{and}\;\sigma_X = \sqrt{2.1} \approx1.449$$. These formulas are exact for a binomial distribution, and they are not approximations.

## When a variable is binomial

A binomial random variable counts successes across a fixed number of trials. The usual conditions are:

- a fixed number of trials
- two possible outcomes on each trial
- a constant probability of success
- independence between trials

If the number of trials continues until the first success, the variable is not binomial because the number of trials is not fixed. Drawing without replacement from a small finite population can also violate the constant-probability and independence conditions. The formulas $$np$$ and $$\sqrt{np(1-p)}$$ should be used only after the binomial model is justified.

## Long run does not mean smooth

<div class="article-note" markdown="1">
A running average can move away from the expected value before moving back toward it, and this is especially visible for skewed distributions with rare large outcomes. The law of large numbers is a statement about long-run behavior, and it does not require the average to improve monotonically after every additional trial.
</div>
