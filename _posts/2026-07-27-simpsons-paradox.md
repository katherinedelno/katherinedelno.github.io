---
layout: post
title: "Simpson's paradox and the lurking variable"
date: 2026-07-27
description: "A treatment can be superior in every subgroup and inferior overall. Real medical data, an adjustable case mix, and the reason observational comparisons require such care."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: foundations
sequence: 3
interactive: true
blurb: "Better in every subgroup, worse overall: the lurking variable at work"
image: "/assets/og/simpsons-paradox.png"
---

In 1986, researchers compared two treatments for kidney stones using the records of a British hospital group. Open surgery succeeded in 78% of its cases; the newer, less invasive procedure succeeded in 83%. The natural reading is that the newer procedure is better, and the natural reading is wrong. Split the patients by stone size and open surgery wins among small stones, 93% to 87%, and wins again among large stones, 73% to 69%. The treatment that is better for every patient is worse on paper.

This reversal, an association that holds in every subgroup yet flips when the subgroups are combined, is called Simpson's paradox, and it is not a curiosity. It is the sharpest available demonstration of why AP Statistics insists so firmly on the vocabulary of lurking variables, confounding, and the limits of observational data.

## How the reversal happens

Nothing in the arithmetic is exotic. An overall success rate is a weighted average of subgroup rates, weighted by how many patients each subgroup contributes. In the kidney-stone data, surgeons steered the difficult large stones toward open surgery and the easy small stones toward the new procedure. Open surgery's overall figure was therefore an average dominated by hard cases, and the new procedure's by easy ones. Each treatment's overall rate says as much about its caseload as about its quality.

The instrument below holds the four subgroup success rates fixed at their published values. The slider controls only the case mix: what fraction of the difficult cases each treatment receives.

<div class="viz" markdown="0">
  <canvas id="sx-cv" width="700" height="290"></canvas>
  <div class="viz-controls">
    <label for="sx-mix">Share of large stones treated by surgery</label>
    <input type="range" id="sx-mix" min="0" max="100" step="1" value="77">
    <span class="viz-value" id="sx-read"></span>
  </div>
  <p class="viz-caption">Each column is one treatment; the darker band is its large-stone caseload and the lighter band its small-stone caseload, with the marker showing the resulting overall success rate against the percentage scale at the left. Band heights are case counts, not rates — the two quantities share a frame because the point is how the first one drags the second. The subgroup rates printed beside the bands never change. At an even case mix the overall comparison agrees with the subgroups, and surgery leads. Drag the slider toward the historical value of about 77% and the marker order reverses while every printed rate stands still. The paradox is not in the treatments; it is in the weighting, and the slider is the lurking variable made into a physical object.</p>
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

## The statistical moral

The paradox settles a question students often ask about the design unit: why so much ceremony about random assignment? Because random assignment is precisely the device that severs the link the slider controls. When treatments are assigned by coin flip, difficult cases distribute themselves evenly, the case mixes match, and the overall comparison means what it appears to mean. When treatments are assigned by human judgment, as in any observational study, the assignment mechanism is free to correlate with severity, and the aggregate numbers inherit that correlation. The kidney-stone surgeons were making sensible medical decisions; the data recorded their sensible decisions as a statistical illusion.

The exam vocabulary maps onto the picture exactly. Stone size is a lurking variable, associated both with the treatment received and with the outcome, which is the definition of confounding. The corrected analysis, comparing like with like inside each subgroup, is stratification. And the one-sentence conclusion the rubric wants is a causal disclaimer: because this is an observational study, the overall association between treatment and success cannot support a causal claim.

A last caution keeps the lesson honest: the paradox does not say that subgroup rates are always the truth and aggregates always the lie. Splitting data by a variable that is a consequence of the treatment, rather than a pre-existing condition, can manufacture reversals just as spurious in the other direction. Which level of the data answers the question depends on what caused what, and that dependence, formalized, is the modern field of causal inference. The AP course's insistence on naming the study design before interpreting any number is the first chapter of that field.

<div class="article-note" markdown="1">
The reversal has appeared in consequential places: in the 1973 Berkeley graduate admissions data, where the university's overall admission rate appeared to favor men while most individual departments slightly favored women — the explanation being that women had applied disproportionately to the most competitive departments — and in batting averages, where one player can trail another in both halves of a season yet lead for the year. A worthwhile exercise with the slider: find the exact case mix at which the overall rates tie, and note that nothing medical happens there at all; the tie is a fact about arithmetic, which is the entire point.
</div>
