---
layout: post
title: "Describing a distribution in the exam's own words"
date: 2026-07-31
description: "The mean follows an outlier and the median refuses to. Push one value across a dotplot and watch which summaries move, which hold still, and which of two outlier rules fires first."
course: "AP Statistics"
read_time: "8 min read"
math: true
kind: foundations
sequence: 1
interactive: true
featured: true
blurb: "Push one value and watch which summaries move and which hold still"
---

The mean follows an outlier and the median refuses to. That is not a curiosity about two formulas; it is the reason the course asks which summary a distribution deserves, and grades the answer.

The framework's description of a distribution has four parts and one condition. Descriptions include shape, center, and variability, together with any unusual features such as outliers, gaps, or clusters — *in context*. Three of those words are quantities and the fourth is a catch-all, but the condition at the end is where most of the lost points are. A description with no units and no variable named is a description of nothing.

## Push one value

Eleven of the twelve values below are nailed down. The twelfth moves.

<div class="viz" markdown="0">
  <canvas id="dd-cv" width="700" height="286"></canvas>
  <div class="viz-controls">
    <label for="dd-r">The twelfth value</label>
    <input type="range" id="dd-r" min="40" max="130" step="1" value="80">
    <span class="viz-value" id="dd-flag"></span>
  </div>
  <div class="dd-read" id="dd-read"></div>
  <p class="viz-caption">Top: the twelve values as a dotplot, with the moving one hollow. Bottom: the boxplot of the same twelve, drawn against the same axis so the box and the dots line up. The two dashed verticals are the fences at 1.5 times the interquartile range beyond each quartile, and they are drawn rather than described because a boxplot's whiskers stop at the most extreme value inside them, not at the minimum and maximum. Push the moving value to the right and watch the readout: two of the four summaries chase it and two do not move at all.</p>
  <style>
    .dd-read{margin:.9rem 0 0;padding-top:.8rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .dd-read .dd-lab{color:var(--muted);display:inline-block;min-width:9rem}
    .dd-read .dd-val{font-weight:700;display:inline-block;min-width:5.5rem}
    .dd-read .dd-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv = document.getElementById('dd-cv'), c = cv.getContext('2d');
  var sl = document.getElementById('dd-r'), read = document.getElementById('dd-read');
  var flag = document.getElementById('dd-flag');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var INK = '#1f1f1f', MUTED = '#5c5c5c', LINE = '#e6e6e6', FAINT = '#9a9a97', PALE = '#c9c9c6';
  var FONT = 'Hanken Grotesk, sans-serif';
  var BASE = [52, 58, 61, 63, 64, 66, 67, 69, 72, 78, 84];
  var XLO = 35, XHI = 135, PADL = 30, PADR = 20;
  var DOTBASE = 132, AXIS = 140, BOXY = 196, BOXH = 34;

  function px(x){ return PADL + (x - XLO)/(XHI - XLO)*(W - PADL - PADR); }
  function med(v){
    var n = v.length;
    return n % 2 ? v[(n - 1)/2] : (v[n/2 - 1] + v[n/2])/2;
  }
  // quartiles the way the framework defines them: the median of each half,
  // with the middle value excluded when the count is odd
  function summarize(vals){
    var v = vals.slice().sort(function(a, b){ return a - b; }), n = v.length, i;
    var sum = 0; for(i = 0; i < n; i++) sum += v[i];
    var mean = sum/n, ss = 0;
    for(i = 0; i < n; i++) ss += (v[i] - mean)*(v[i] - mean);
    var s = Math.sqrt(ss/(n - 1));
    var q1 = med(v.slice(0, Math.floor(n/2))), q3 = med(v.slice(Math.ceil(n/2)));
    var iqr = q3 - q1;
    return { v: v, mean: mean, median: med(v), s: s, q1: q1, q3: q3, iqr: iqr,
             lo: q1 - 1.5*iqr, hi: q3 + 1.5*iqr };
  }

  function draw(){
    var r = +sl.value, all = BASE.concat([r]), st = summarize(all);
    c.clearRect(0, 0, W, H);

    // fences, drawn through both panels
    c.strokeStyle = PALE; c.lineWidth = 1; c.setLineDash([4, 3]);
    [st.lo, st.hi].forEach(function(f){
      if(f < XLO || f > XHI) return;
      c.beginPath(); c.moveTo(px(f), 18); c.lineTo(px(f), BOXY + BOXH/2 + 8); c.stroke();
    });
    c.setLineDash([]);
    c.fillStyle = FAINT; c.font = '700 10px ' + FONT; c.textAlign = 'center';
    if(st.hi <= XHI) c.fillText('FENCE', px(st.hi), 14);
    if(st.lo >= XLO) c.fillText('FENCE', px(st.lo), 14);

    // dotplot, stacking equal values
    var counts = {};
    all.forEach(function(x){
      var k = Math.round(px(x));
      counts[k] = (counts[k] || 0) + 1;
      var y = DOTBASE - (counts[k] - 1)*13;
      var isRover = (x === r) && (counts[k] === 1 || BASE.indexOf(x) < 0);
      c.beginPath(); c.arc(px(x), y, 5, 0, 7);
      if(x === r){ c.fillStyle = '#fff'; c.fill(); c.strokeStyle = INK; c.lineWidth = 2; c.stroke(); }
      else { c.fillStyle = INK; c.fill(); }
    });

    // axis
    c.strokeStyle = LINE; c.lineWidth = 1;
    c.beginPath(); c.moveTo(PADL, AXIS + 0.5); c.lineTo(W - PADR, AXIS + 0.5); c.stroke();
    c.fillStyle = MUTED; c.font = '700 10px ' + FONT; c.textAlign = 'center';
    for(var t = 40; t <= 130; t += 10){
      c.fillText(String(t), px(t), AXIS + 15);
      c.beginPath(); c.moveTo(px(t), AXIS); c.lineTo(px(t), AXIS + 4); c.stroke();
    }

    // boxplot: whiskers reach the most extreme value inside the fences
    var inside = st.v.filter(function(x){ return x >= st.lo && x <= st.hi; });
    var wlo = inside[0], whi = inside[inside.length - 1];
    var mid = BOXY, half = BOXH/2;
    c.strokeStyle = INK; c.lineWidth = 1.6;
    c.beginPath();
    c.moveTo(px(wlo), mid); c.lineTo(px(st.q1), mid);
    c.moveTo(px(st.q3), mid); c.lineTo(px(whi), mid);
    c.moveTo(px(wlo), mid - 7); c.lineTo(px(wlo), mid + 7);
    c.moveTo(px(whi), mid - 7); c.lineTo(px(whi), mid + 7);
    c.stroke();
    c.strokeRect(px(st.q1), mid - half, px(st.q3) - px(st.q1), BOXH);
    c.lineWidth = 2.4;
    c.beginPath(); c.moveTo(px(st.median), mid - half); c.lineTo(px(st.median), mid + half); c.stroke();
    // outliers as open squares
    st.v.forEach(function(x){
      if(x < st.lo || x > st.hi){
        c.strokeStyle = INK; c.lineWidth = 1.6; c.fillStyle = '#fff';
        c.beginPath(); c.rect(px(x) - 4, mid - 4, 8, 8); c.fill(); c.stroke();
      }
    });
    // the mean, marked separately, because a boxplot does not show it
    c.fillStyle = MUTED;
    c.beginPath();
    c.moveTo(px(st.mean), mid + half + 5);
    c.lineTo(px(st.mean) - 4, mid + half + 12);
    c.lineTo(px(st.mean) + 4, mid + half + 12);
    c.closePath(); c.fill();
    c.font = '700 9px ' + FONT; c.textAlign = 'left';
    c.fillText('MEAN', px(st.mean) + 7, mid + half + 12);

    var iqrOut = (r > st.hi || r < st.lo);
    var sdOut = Math.abs(r - st.mean) > 2*st.s;
    flag.textContent = iqrOut === sdOut
      ? (iqrOut ? 'both rules call it an outlier' : 'neither rule calls it an outlier')
      : (sdOut ? 'the two-deviation rule flags it; the 1.5 IQR rule does not'
               : 'the 1.5 IQR rule flags it; the two-deviation rule does not');

    read.innerHTML =
      '<div><span class="dd-lab">mean</span><span class="dd-val">' + st.mean.toFixed(2) +
        '</span><span class="dd-note">follows the moving value</span></div>' +
      '<div><span class="dd-lab">median</span><span class="dd-val">' + st.median.toFixed(2) +
        '</span><span class="dd-note">resistant</span></div>' +
      '<div><span class="dd-lab">standard deviation</span><span class="dd-val">' + st.s.toFixed(2) +
        '</span><span class="dd-note">follows the moving value</span></div>' +
      '<div><span class="dd-lab">interquartile range</span><span class="dd-val">' + st.iqr.toFixed(2) +
        '</span><span class="dd-note">resistant; fences at ' + st.lo.toFixed(1) + ' and ' + st.hi.toFixed(1) + '</span></div>';
  }
  sl.addEventListener('input', draw);
  draw();
})();
</script>

## What resists, and what does not

Take the moving value from 80 out to 130 and read the four numbers. The mean climbs from 67.83 to 72.00 and the standard deviation more than doubles, from 9.38 to 20.17. The median reads 66.50 at both ends. So does the interquartile range, at 13.00, and so do both quartiles.

The reason is worth stating as arithmetic rather than as a slogan. The mean and the standard deviation are computed from every value, so every value has a vote proportional to its distance. The median and the quartiles are computed from *positions*, and moving the largest value further right does not change which value sits in the middle. A resistant statistic is one that a single observation cannot move far, and resistance is a structural property of how the statistic is defined.

That settles the choice the exam grades. A skewed distribution or one with an outlier is summarized by the median and the interquartile range, because the alternative reports a center that no observation is near. A roughly symmetric distribution is summarized by the mean and the standard deviation, which use more of the data and are more stable from sample to sample. The framework supplies the diagnostic: in a right-skewed distribution the mean is usually larger than the median, in a left-skewed one usually smaller, and in a symmetric one the two sit close together. Comparing them is a one-line test for skew that needs no picture.

## Two rules for one word

The framework names two methods for identifying an outlier, and they are not equivalent. One flags a value more than $$1.5 \times \text{IQR}$$ beyond a quartile. The other flags a value more than two standard deviations from the mean.

Push the moving value slowly upward through the nineties and the readout under the slider changes twice. At 91 the two-deviation rule fires. The $$1.5 \times \text{IQR}$$ rule does not fire until 95. Four whole units separate two rules from the same page of the same framework.

The disagreement has a direction, and it is the direction resistance predicts. The two-deviation rule is built from the mean and the standard deviation, both of which the suspect value has already inflated, so the threshold runs away from the value that is chasing it. The quartile rule is built from statistics the suspect value cannot move, so its fence holds still — at 94.5, unchanged for every position past 84. A rule that a candidate outlier can dilute is a weaker rule than one it cannot.

The practical consequence is small and worth knowing: a question about outliers has to say which rule it means, and an answer has to name the rule it used.

## Compare, do not describe

The comparison topic is where descriptions are actually assessed, and it fails in a way that has nothing to do with statistics. Asked to compare two distributions, students describe each one in turn and stop. Two accurate paragraphs, no comparison, no credit.

A comparison needs comparative words — *higher*, *more variable*, *more strongly skewed* — attached to each of the features, and the features come from the same list as before. Center, then variability, then shape, then unusual features, each one naming both groups and both contexts. The boxplot is built for exactly this, which is why the framework says boxplots may be used to compare center, variability, outliers, and skewness. What the boxplot cannot show is the mean, which is why the marker under the box above is drawn separately, and why a bimodal distribution can hide inside a perfectly ordinary-looking box.

<div class="article-note" markdown="1">
A self-test at the slider: put the moving value at 40 and read the boxplot rather than the numbers. The left whisker does not reach it, because a whisker stops at the most extreme value that is not an outlier and the point beyond it is drawn as its own marker. Now account for a whisker's length in one sentence that does not use the word minimum. A student who can write that sentence will never again read the ends of a boxplot as the ends of the data, which is the most common misreading of the display in the course.
</div>
