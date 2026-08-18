---
layout: post
title: "Describing a distribution in the exam's own words"
date: 2026-07-31
description: "Shape, center, variability, and unusual features should be described in context. The choice of summary statistics depends on the shape of the distribution."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: foundations
sequence: 1
interactive: true
featured: true
blurb: "Shape, center, variability, and unusual features should be described in context. The choice of summary statistics depends on the shape of the distribution"
image: "/assets/og/describing-a-distribution.png"
---

A statistical description should tell the reader what the distribution looks like and what its values mean. For a quantitative variable, the main features are shape, center, variability, and unusual features such as outliers, gaps, or clusters. The description also needs context, and a statement about a median of 66.5 is incomplete until the variable, units, and population are clear.

## Move one observation

Eleven of the twelve values below stay fixed, and the twelfth moves.

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

    // dotplot, stacking equal values. The mover is the last entry, so it is
    // identified by index: comparing values would also hollow out a fixed value
    // that the slider happens to be sitting on.
    var counts = {}, ROVER = all.length - 1;
    all.forEach(function(x, idx){
      var k = Math.round(px(x));
      counts[k] = (counts[k] || 0) + 1;
      var y = DOTBASE - (counts[k] - 1)*13;
      c.beginPath(); c.arc(px(x), y, 5, 0, 7);
      if(idx === ROVER){ c.fillStyle = '#fff'; c.fill(); c.strokeStyle = INK; c.lineWidth = 2; c.stroke(); }
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

The dotplot and boxplot show the same data, and the dashed lines mark the usual $$1.5\times\text{IQR}$$ fences. As the moving value travels farther from the rest of the data, compare the mean, median, standard deviation, and interquartile range. The mean and standard deviation respond strongly, and the median and IQR may not move at all.

## Resistant and nonresistant summaries

When the moving value changes from 80 to 130, the mean rises from 67.83 to 72.00 and the standard deviation rises from 9.38 to 20.17. The median remains 66.50 and the IQR remains 13.00.

The difference comes from how the summaries are defined. The mean and standard deviation use the numerical size of every observation, and an extreme value therefore has direct influence on both. The median and quartiles depend primarily on order and position, and moving the largest observation farther right does not change which observations occupy the middle positions. That makes the median and IQR resistant to extreme values.

For a roughly symmetric distribution without strong outliers, the mean and standard deviation are usually appropriate summaries. For a skewed distribution or one with influential outliers, the median and IQR are often more representative.

## Shape matters

For a right-skewed distribution, the long right tail tends to pull the mean above the median, and for a left-skewed distribution, the long left tail tends to pull the mean below the median. For a roughly symmetric distribution, the two are often close.

This relationship can support a description, but it does not replace looking at the distribution itself. A distribution can also be bimodal, clustered, or otherwise unusual in ways that a single pair of summary statistics cannot show.

## Two outlier rules

Two common rules can identify different observations as unusual. The $$1.5\times\text{IQR}$$ rule flags observations below $$Q_1-1.5(\text{IQR})$$ or above $$Q_3+1.5(\text{IQR})$$, and another rule considers observations more than two standard deviations from the mean. These rules need not agree, and in the visualization, the two-standard-deviation rule begins flagging the moving value before the IQR rule does.

That disagreement is not a contradiction. The rules use different centers and measures of spread, and the mean and standard deviation are themselves affected by the candidate outlier, while the quartiles are much more resistant. So when a problem asks whether an observation is an outlier, state which rule is being used.

## Reading a boxplot correctly

A standard modified boxplot does not extend its whiskers automatically to the minimum and maximum. The whiskers stop at the most extreme observations that remain within the $$1.5\times\text{IQR}$$ fences, and observations beyond the fences are shown separately.

A boxplot is useful for comparing center, spread, skew, and possible outliers. It cannot show every feature of the raw distribution, and two different datasets can have similar boxplots while having very different modality or clustering.

## Comparing two distributions

A comparison should actually compare. Instead of writing one paragraph about Group A and another about Group B, use comparative language. For example:

“Group A has a higher median score and less variability than Group B. Group B is more strongly right-skewed and contains one high outlier.”

The same four features still organize the response:

- shape
- center
- variability
- unusual features

<div class="article-note" markdown="1">
But each statement should relate the groups directly and remain in context.
</div>
