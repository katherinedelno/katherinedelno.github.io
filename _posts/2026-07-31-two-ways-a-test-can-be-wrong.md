---
layout: post
title: "The two ways a test can be wrong"
date: 2026-07-31
description: "A Type I error is a risk chosen before the data arrive. A Type II error is inherited, and four separate things move it. Two curves and one cut make the difference visible."
course: "AP Statistics"
read_time: "9 min read"
math: true
kind: foundations
sequence: 14
interactive: true
blurb: "One error is chosen in advance; the other is inherited"
image: "/assets/og/two-ways-a-test-can-be-wrong.png"
---

The probability of a Type I error is a number chosen in advance. The probability of a Type II error is inherited from the situation, and in a real study it is never observed at all. That asymmetry is the whole of this topic, and it accounts for a lopsidedness students notice without being able to name: $$\alpha$$ is announced before the data are collected, and its counterpart usually is not announced anywhere.

## Two errors, named for what they get wrong

The framework defines both by the verdict rather than by the arithmetic. A Type I error occurs when there is convincing statistical evidence that the alternative hypothesis is true, on the strength of a small p-value, but it is not. A Type II error occurs when there is not convincing evidence that the alternative is true, on the strength of a large p-value, but it is.

Each error pairs a verdict with a truth, and the two are the only ways that pair can disagree. A test that rejects a true null has raised a false alarm; a test that fails to reject a false null has missed something real.

A third definition completes the set: the power of a test is the probability that it correctly rejects a false null hypothesis. Power and the Type II error are complements, and the framework states the relationship as a formula rather than as a picture:

$$P(\text{Type II error}) = 1 - \text{power}.$$

## One cut, two curves

A production line is treated as in control when at most 10% of parts need rework. An inspector draws a random sample and tests $$H_0: p = 0.10$$ against $$H_a: p > 0.10$$, rejecting when the sample proportion lands far enough above 0.10.

Both panels below show the same cut, drawn in the same place. What changes between them is which world the sample was drawn from. Move the true rate and watch only the lower panel respond.

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

## What each control moves, and what it leaves alone

The framework lists four things that raise power, and attaches the same clause to all four: *provided the others do not change*. The three controls above are those four factors, because sample size and standard error are one lever rather than two.

Raise $$n$$ from 200 to 400 and power climbs from 0.7252 to 0.9220. Both curves narrow, the cut slides left, and the top panel's dark area stays at 0.05 throughout. That is the first thing worth watching. The significance level is a constraint the cut is built to satisfy, so it cannot drift; everything else on screen is free to move.

Drag the true rate from 0.15 out to 0.20 and power runs to 0.9893, with nothing about the test changed. A test is not powerful or weak on its own, only powerful against a particular alternative, and a discrepancy far from the null is easier to see than one nearby. Drag the other way, to 0.12, and power falls to 0.2585 — the same test, now missing a real problem three times in four.

Loosening $$\alpha$$ to 0.10 raises power to 0.8169, and tightening it to 0.01 drops power to 0.5103. This is the only one of the four that is a trade rather than a gain. The others buy power with sample size or receive it as a gift from the truth; this one buys it by accepting more false alarms.

## Power at the null

Slide the true rate all the way down to 0.10, so the two panels show the same curve. The readout stops calling the lower area power in any useful sense and reports a number equal to $$\alpha$$ exactly — 0.0500 at the default setting, 0.0100 if the level is tightened.

The coincidence is not a coincidence. Power is the probability of rejecting, evaluated at whatever the truth is; at the null value that is the probability of rejecting a true null, which is the definition of $$\alpha$$. So $$\alpha$$ is the beginning of the power curve rather than a separate quantity, and the two errors are measured on one continuum instead of belonging to different worlds.

## What the exam asks of this

Less arithmetic than the picture suggests. The relationship $$P(\text{Type II error}) = 1 - \text{power}$$ is the calculation, so a question supplying a power of 0.80 is asking for 0.20 and nothing more. Nothing on the exam requires shading a normal curve to produce $$\beta$$ from scratch.

What is assessed is identification, the four factors, and consequences. Consequences are where the two errors stop being symmetric: halting a line that is running properly costs production, while letting a faulty line run costs the parts that reach customers, and the framework asks which is worse to be settled before the study rather than after. That judgment sets $$\alpha$$, because $$\alpha$$ is the probability of a Type I error, and it sets $$n$$, because sample size drives the probability of the other. Neither number is chosen for a statistical reason, and both are fixed before any data exist — the same discipline that makes [a p-value interpretable at all](/2026/07/30/what-a-p-value-is.html) once it arrives.

<div class="article-note" markdown="1">
A prediction to test against the interactive: set the true rate to 0.15 and the level to 0.05, then find the smallest sample size that lifts power to the 0.80 benchmark. Guess first, nearer 250 or nearer 500. It is 253. Now ask what that number becomes if the inspector cares about a rate of 0.12 instead, and notice the question cannot be answered without naming an alternative. Power is never a property of a test alone, which is why a study reporting it always reports the discrepancy it was built to catch.
</div>
