---
layout: post
title: "Simpson's paradox and the lurking variable"
date: 2026-07-27
description: "An overall association can reverse after data are separated into meaningful subgroups. The reversal comes from unequal weighting across those groups."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: foundations
sequence: 3
interactive: true
blurb: "An overall association can reverse after data are separated into meaningful subgroups. The reversal comes from unequal weighting across those groups"
image: "/assets/og/simpsons-paradox.png"
---

An association observed in combined data can reverse after the data are separated into relevant groups, and this is Simpson's paradox. A well-known example comes from a comparison of two treatments for kidney stones. Overall, the less invasive treatment had a higher success rate, but within both small-stone and large-stone groups, open surgery had the higher success rate. The reversal came from the way patients were distributed between the treatments.

## The kidney-stone example

Open surgery succeeded in about 93% of small-stone cases and 73% of large-stone cases, and the less invasive procedure succeeded in about 87% of small-stone cases and 69% of large-stone cases. So open surgery had the higher success rate in both subgroups, yet the combined success rates favored the less invasive procedure. Why?

The treatments did not receive the same mix of patients. Surgeons were more likely to use open surgery for difficult large stones, and the less invasive treatment received more of the easier small-stone cases. An overall success rate is a weighted average of subgroup rates, and different weights can therefore reverse the comparison.

## Change only the case mix

<div class="viz" markdown="0">
  <canvas id="sx-cv" width="700" height="290"></canvas>
  <div class="viz-controls">
    <label for="sx-mix">Share of large stones treated by surgery</label>
    <input type="range" id="sx-mix" min="0" max="100" step="1" value="77">
    <span class="viz-value" id="sx-read"></span>
  </div>
  <p class="viz-caption">Each column is one treatment; the darker band is its large-stone caseload and the lighter band its small-stone caseload, with the marker showing the resulting overall success rate against the percentage scale at the left. Band heights are case counts, not rates. The two quantities share a frame because the point is how the first one drags the second. The subgroup rates printed beside the bands never change. At an even case mix the overall comparison agrees with the subgroups, and surgery leads. Drag the slider toward the historical value of about 77% and the marker order reverses while every printed rate stands still. The paradox is not in the treatments; it is in the weighting, and the slider is the lurking variable made into a physical object.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('sx-cv'), c = cv.getContext('2d');
  var sl = document.getElementById('sx-mix'), read = document.getElementById('sx-read');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  // published subgroup success rates (Charig et al., 1986)
  var S_SMALL = 0.93, S_LARGE = 0.73;   // open surgery
  var P_SMALL = 0.87, P_LARGE = 0.69;   // percutaneous procedure
  var N_LARGE = 350, N_SMALL = 350;     // difficult and easy cases to allocate
  function bar(x, label, nLarge, nSmall, rLarge, rSmall){
    var total = nLarge + nSmall;
    var overall = total > 0 ? (nLarge*rLarge + nSmall*rSmall)/total : 0;
    var bw = 120, top = 38, bh = H - 92;
    var hL = total > 0 ? bh*nLarge/420 : 0;
    var hS = total > 0 ? bh*nSmall/420 : 0;
    c.fillStyle = '#8a8a87';
    c.fillRect(x, top + bh - hL, bw, hL);
    c.fillStyle = '#e0e0dd';
    c.fillRect(x, top + bh - hL - hS, bw, hS);
    c.strokeStyle = '#c9c9c6'; c.strokeRect(x + 0.5, top + 0.5, bw, bh);
    // overall marker
    var my = top + bh - bh*overall;
    c.strokeStyle = '#1f1f1f'; c.lineWidth = 2.4;
    c.beginPath(); c.moveTo(x - 8, my); c.lineTo(x + bw + 8, my); c.stroke();
    c.lineWidth = 1;
    c.fillStyle = '#1f1f1f'; c.font = '700 12px Hanken Grotesk, sans-serif';
    c.fillText((overall*100).toFixed(1) + '%', x + bw + 14, my + 4);
    c.font = '700 13px Hanken Grotesk, sans-serif';
    c.fillText(label, x, H - 34);
    c.fillStyle = '#5c5c5c'; c.font = '11px Hanken Grotesk, sans-serif';
    c.fillText('large: ' + nLarge + ' cases at ' + Math.round(rLarge*100) + '%', x, H - 18);
    c.fillText('small: ' + nSmall + ' cases at ' + Math.round(rSmall*100) + '%', x, H - 5);
    return overall;
  }
  // The band heights are case counts and the marker is a success rate, so the
  // rate scale is drawn explicitly rather than left to be guessed at.
  function rateAxis(){
    var top = 38, bh = H - 92;
    c.strokeStyle = '#efefed'; c.lineWidth = 1;
    c.fillStyle = '#9a9a97'; c.font = '700 10px Hanken Grotesk, sans-serif';
    for(var p = 0; p <= 100; p += 25){
      var y = top + bh - bh*p/100;
      c.beginPath(); c.moveTo(100, y); c.lineTo(W - 24, y); c.stroke();
      c.textAlign = 'right'; c.fillText(p + '%', 94, y + 3);
    }
    c.textAlign = 'left'; c.fillText('SUCCESS RATE', 8, top - 10);
  }
  function draw(){
    var t = sl.value/100;
    var sL = Math.round(N_LARGE*t), pL = N_LARGE - sL;
    var sS = N_SMALL - Math.round(N_SMALL*t), pS = N_SMALL - sS;
    c.clearRect(0, 0, W, H);
    rateAxis();
    var o1 = bar(110, 'Open surgery', sL, sS, S_LARGE, S_SMALL);
    var o2 = bar(410, 'New procedure', pL, pS, P_LARGE, P_SMALL);
    var flipped = o2 > o1;
    read.textContent = 'overall: surgery ' + (o1*100).toFixed(1) + '%, new procedure ' + (o2*100).toFixed(1) + '%' + (flipped ? '  (reversed: the subgroup loser leads overall)' : '  (consistent with the subgroups)');
  }
  sl.addEventListener('input', draw);
  draw();
})();
</script>

The subgroup success rates remain fixed, and only the fraction of difficult cases assigned to each treatment changes. At an even case mix, the overall comparison agrees with the subgroup comparisons, and as the treatment groups become more imbalanced in stone severity, the aggregate rates can reverse.

Nothing about the treatment-specific subgroup rates changed. Only the weights changed.

## The lurking variable

Stone size is related to the treatment received, and it is also related to the probability of success. That makes it a confounding variable in the treatment-outcome association. The aggregate comparison mixes together the effect of treatment and the effect of severity, and stratifying by stone size compares more similar patients and exposes the reversal. This is why study design matters before any calculation is interpreted.

## Random assignment and confounding

Random assignment is designed to break systematic relationships between treatment assignment and pre-existing characteristics. If patients are assigned to treatment at random, variables such as disease severity should be balanced between groups apart from chance variation.

In an observational study, treatment choice may depend on prognosis, physician preference, patient characteristics, or other factors, and those variables can then confound the observed treatment-outcome relationship. An observational association can therefore be real without being causal.

## Aggregated data are not always wrong

Simpson's paradox does not mean that subgroup analysis is automatically better. The relevant level of analysis depends on the causal structure, and conditioning on a variable caused by the treatment can itself introduce bias. The important question is why the groups differ and where the third variable sits in the sequence of events.

<div class="article-note" markdown="1">
For AP Statistics, the practical lesson is simpler. Before making a causal claim, identify the study design and consider whether a lurking or confounding variable could explain the association.
</div>
