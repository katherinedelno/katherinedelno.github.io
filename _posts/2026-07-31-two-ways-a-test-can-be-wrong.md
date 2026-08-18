---
layout: post
title: "The two ways a test can be wrong"
date: 2026-07-31
description: "Type I error is a false rejection of the null. Type II error is a failure to detect a false null. Power is the probability of detecting the effect when it is real."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: foundations
sequence: 14
interactive: true
blurb: "Type I error is a false rejection of the null. Type II error is a failure to detect a false null. Power is the probability of detecting the effect when it is real"
image: "/assets/og/two-ways-a-test-can-be-wrong.png"
---

A hypothesis test can make two kinds of error. A Type I error occurs when the null hypothesis is true and the test rejects it, and a Type II error occurs when the null hypothesis is false and the test fails to reject it. The two errors arise from different parts of the testing procedure.

## Type I error

Suppose $$H_0:p=0.10$$ and $$H_a:p>0.10$$. A Type I error means concluding that the rework rate exceeds 10% when the true rate is actually 10%. This is a false positive. The significance level $$\alpha$$ is the probability of a Type I error when the null is true, and it is chosen before the data are observed.

## Type II error and power

A Type II error occurs when the true rework rate is greater than 10% but the study does not produce enough evidence to reject $$H_0$$. This is a missed detection, and its probability is often written $$\beta$$. Power is the probability that the test correctly rejects a false null, so $$\text{power}=1-\beta$$. Power depends on which alternative value is actually true, so there is not one universal power value for a test.

## One cutoff, two possible worlds

<div class="viz" markdown="0">
  <canvas id="pw-cv" width="700" height="368"></canvas>
  <div class="viz-controls">
    <label for="pw-p">True rework rate</label>
    <input type="range" id="pw-p" min="100" max="250" step="1" value="150">
    <label for="pw-n">Sample size n</label>
    <input type="range" id="pw-n" min="50" max="800" step="1" value="200">
  </div>
  <div class="viz-controls">
    <label>Significance level &alpha;</label>
    <button type="button" class="res-filter pw-a" data-a="0.10" style="font-size:.72rem">0.10</button>
    <button type="button" class="res-filter pw-a is-active" data-a="0.05" style="font-size:.72rem">0.05</button>
    <button type="button" class="res-filter pw-a" data-a="0.01" style="font-size:.72rem">0.01</button>
  </div>
  <div class="pw-read" id="pw-read"></div>
  <p class="viz-caption">Dark shading is where the test rejects, and it is the same region in both panels, because the cut does not know which world it is in. Top: the line really is in control, so every dark outcome is a false alarm and the dark area is exactly the significance level. Bottom: the line really is running at the chosen rate, so the dark area is now the test working and the pale area is the failure to notice. Heights are scaled to fit; only the shaded areas are probabilities. Raise n and both curves narrow while the top area holds, which is the one thing on screen that never moves on its own.</p>
  <style>
    .pw-read{margin:.9rem 0 0;padding-top:.8rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .pw-read .pw-lab{color:var(--muted);display:inline-block;min-width:15.5rem}
    .pw-read .pw-val{font-weight:700;display:inline-block;min-width:6rem}
    .pw-read .pw-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv = document.getElementById('pw-cv'), c = cv.getContext('2d');
  var slP = document.getElementById('pw-p'), slN = document.getElementById('pw-n');
  var read = document.getElementById('pw-read');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var INK = '#1f1f1f', MUTED = '#5c5c5c', LINE = '#e6e6e6', FAINT = '#9a9a97';
  var DARK = 'rgba(31,31,31,0.62)', PALEFILL = 'rgba(31,31,31,0.10)';
  var FONT = 'Hanken Grotesk, sans-serif';
  var P0 = 0.10, XLO = 0.0, XHI = 0.30;
  var ZA = { '0.10': 1.2815515655446004, '0.05': 1.6448536269514722, '0.01': 2.3263478740408408 };
  var alpha = '0.05';
  var PADL = 20, PADR = 16, TOPA = 26, BASEA = 162, TOPB = 206, BASEB = 342;

  function px(x){ return PADL + (x - XLO)/(XHI - XLO)*(W - PADL - PADR); }
  function se(p, n){ return Math.sqrt(p*(1 - p)/n); }
  function dens(x, m, s){ return Math.exp(-0.5*Math.pow((x - m)/s, 2))/(s*Math.sqrt(2*Math.PI)); }
  // standard normal cdf, Abramowitz and Stegun 7.1.26 through erf; error under 1.5e-7
  function phi(z){
    var sgn = z < 0 ? -1 : 1, x = Math.abs(z)/Math.SQRT2;
    var t = 1/(1 + 0.3275911*x);
    var y = 1 - ((((1.061405429*t - 1.453152027)*t + 1.421413741)*t - 0.284496736)*t + 0.254829592)*t*Math.exp(-x*x);
    return 0.5*(1 + sgn*y);
  }

  function curve(m, s, base, scale, cut, lo, hi){
    // filled region between lo and hi, then the outline across the whole panel
    var x, i, N = 460;
    c.beginPath();
    c.moveTo(px(lo), base);
    for(i = 0; i <= N; i++){
      x = lo + (hi - lo)*i/N;
      c.lineTo(px(x), base - dens(x, m, s)*scale);
    }
    c.lineTo(px(hi), base);
    c.closePath();
    c.fill();
  }
  function outline(m, s, base, scale){
    var i, N = 700, x, started = false;
    c.beginPath();
    for(i = 0; i <= N; i++){
      x = XLO + (XHI - XLO)*i/N;
      var y = base - dens(x, m, s)*scale;
      started ? c.lineTo(px(x), y) : (c.moveTo(px(x), y), started = true);
    }
    c.stroke();
  }

  function draw(){
    var p = (+slP.value)/1000, n = +slN.value, a = +alpha, z = ZA[alpha];
    var s0 = se(P0, n), s1 = se(p, n);
    var cut = P0 + z*s0;
    var beta = phi((cut - p)/s1), power = 1 - beta;

    // one vertical scale for both panels, so relative heights stay honest
    var peak = Math.max(dens(P0, P0, s0), dens(p, p, s1));
    var scale = 128/peak;

    c.clearRect(0, 0, W, H);
    c.font = '700 10px ' + FONT; c.textAlign = 'left';

    [[TOPA, BASEA, 'IF THE LINE IS IN CONTROL,  p = 0.10'],
     [TOPB, BASEB, 'IF THE TRUE RATE IS ' + p.toFixed(3)]].forEach(function(pan){
      c.fillStyle = FAINT; c.fillText(pan[2], PADL, pan[0] - 8);
      c.strokeStyle = LINE; c.lineWidth = 1;
      c.beginPath(); c.moveTo(PADL, pan[1] + 0.5); c.lineTo(W - PADR, pan[1] + 0.5); c.stroke();
    });

    // shaded regions: dark is always "the test rejects"
    c.fillStyle = PALEFILL;
    curve(P0, s0, BASEA, scale, cut, XLO, cut);
    curve(p,  s1, BASEB, scale, cut, XLO, cut);
    c.fillStyle = DARK;
    curve(P0, s0, BASEA, scale, cut, cut, XHI);
    curve(p,  s1, BASEB, scale, cut, cut, XHI);

    c.strokeStyle = INK; c.lineWidth = 1.6;
    outline(P0, s0, BASEA, scale);
    outline(p,  s1, BASEB, scale);

    // the cut, one line through both panels
    c.strokeStyle = INK; c.lineWidth = 1.4; c.setLineDash([5, 3]);
    c.beginPath(); c.moveTo(px(cut), TOPA - 4); c.lineTo(px(cut), BASEB); c.stroke();
    c.setLineDash([]);
    c.fillStyle = INK; c.font = '700 11px ' + FONT; c.textAlign = 'center';
    c.fillText('reject above ' + cut.toFixed(4), px(cut), TOPA - 12);

    // axis
    c.fillStyle = MUTED; c.font = '700 10px ' + FONT; c.textAlign = 'center';
    for(var t = 0; t <= 0.30001; t += 0.05){
      c.fillText(t.toFixed(2), px(t), BASEB + 16);
      c.strokeStyle = LINE; c.beginPath();
      c.moveTo(px(t), BASEB); c.lineTo(px(t), BASEB + 4); c.stroke();
    }

    read.innerHTML =
      '<div><span class="pw-lab">significance level &alpha;</span><span class="pw-val">' + a.toFixed(2) +
        '</span><span class="pw-note">chosen in advance; the dark area of the top panel</span></div>' +
      '<div><span class="pw-lab">P(Type II error), &beta;</span><span class="pw-val">' + beta.toFixed(4) +
        '</span><span class="pw-note">the pale area of the lower panel</span></div>' +
      '<div><span class="pw-lab">power, 1 &minus; &beta;</span><span class="pw-val">' + power.toFixed(4) +
        '</span><span class="pw-note">' +
        (Math.abs(p - P0) < 1e-9
          ? 'the null is true here, so there is no false null to catch and this equals &alpha; exactly'
          : (power >= 0.8 ? 'at or above the 0.80 the framework uses as a benchmark'
                          : 'below the 0.80 the framework uses as a benchmark')) +
        '</span></div>';
  }

  function setAlpha(v){
    alpha = v;
    Array.prototype.forEach.call(document.querySelectorAll('.pw-a'), function(b){
      b.classList[b.getAttribute('data-a') === v ? 'add' : 'remove']('is-active');
    });
    draw();
  }
  Array.prototype.forEach.call(document.querySelectorAll('.pw-a'), function(b){
    b.addEventListener('click', function(){ setAlpha(b.getAttribute('data-a')); });
  });
  slP.addEventListener('input', draw);
  slN.addEventListener('input', draw);
  draw();
})();
</script>

The rejection cutoff is chosen so that the probability of entering the rejection region under the null equals $$\alpha$$. The lower curve represents a particular alternative value, and under that alternative the rejection region represents correct detection while the area outside it represents Type II error. The same cutoff is evaluated under two different distributions.

## What increases power

Power generally increases when:

- sample size increases
- the true parameter lies farther from the null value
- variability decreases
- $$\alpha$$ increases

The first three improve the ability to distinguish the null from the alternative. Changing $$\alpha$$ is different. Increasing $$\alpha$$ raises power by making rejection easier, but it also raises the Type I error rate, and that is a tradeoff.

## Sample size

Increasing $$n$$ reduces the standard error, so the null and alternative sampling distributions become narrower and a fixed difference between them is easier to detect. This increases power without changing the chosen significance level, which is one reason sample-size planning is done before a study begins.

## Effect size

A test has more power against alternatives far from the null than against alternatives very close to it. A true rework rate of 20% is easier to distinguish from 10% than a true rate of 12%, so a power statement should name the alternative effect size it refers to. Saying only that “the study has 80% power” is incomplete unless the target discrepancy is clear.

## Consequences matter

Type I and Type II errors may have very different practical costs. In one setting a false alarm may be more serious, and in another failing to detect a real effect may be worse. The choice of $$\alpha$$, sample size, and desired power should reflect those consequences before the data are analyzed.

<div class="article-note" markdown="1">
The statistical definitions are symmetric. The real-world costs often are not.
</div>
