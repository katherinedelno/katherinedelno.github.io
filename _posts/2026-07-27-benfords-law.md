---
layout: post
title: "Benford's law and the distribution of first digits"
date: 2026-07-27
description: "In many datasets spanning several orders of magnitude, smaller leading digits occur more often than larger ones. The pattern is logarithmic rather than uniform."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: beyond
sequence: 4
interactive: true
blurb: "In many datasets spanning several orders of magnitude, smaller leading digits occur more often than larger ones. The pattern is logarithmic rather than uniform"
image: "/assets/og/benfords-law.png"
---

If the leading digit of a number could be treated as uniformly random, each digit from 1 through 9 would appear about one ninth of the time.

Many real datasets do not behave that way.

The leading digit 1 often appears much more frequently than 9.

Benford's law gives the probability

$$ P(D=d) = \log_{10}\left(1+\frac1d\right), \qquad d=1,\ldots,9. $$

## The distribution

The probabilities are approximately:

| Leading digit | Probability |
|---|---|
| 1 | 30.1% |
| 2 | 17.6% |
| 3 | 12.5% |
| 4 | 9.7% |
| 5 | 7.9% |
| 6 | 6.7% |
| 7 | 5.8% |
| 8 | 5.1% |
| 9 | 4.6% |

So a leading 1 is expected almost one third of the time.

A leading 9 appears less than 5% of the time.

<div class="viz" markdown="0">
  <canvas id="bf-cv" width="700" height="280"></canvas>
  <div class="viz-controls">
    <button type="button" id="bf-pow" class="res-filter" style="font-size:.72rem">Powers of 2</button>
    <button type="button" id="bf-fib" class="res-filter" style="font-size:.72rem">Fibonacci numbers</button>
    <button type="button" id="bf-pop" class="res-filter" style="font-size:.72rem">Simulated city populations</button>
    <button type="button" id="bf-uni" class="res-filter" style="font-size:.72rem">Uniform random numbers</button>
    <span class="viz-value" id="bf-read"></span>
  </div>
  <p class="viz-caption">The first three datasets hug the predicted markers closely; the powers of 2 and the Fibonacci numbers follow the law essentially exactly, a theorem rather than a tendency. The uniform random numbers refuse: their digits are flat at about 11% each, because a uniform sample does not span many orders of magnitude, and spanning orders of magnitude is the engine of the law. Data that grows multiplicatively, or that mixes many scales, spends more of its life with a leading 1 than a leading 9, for the same reason a number must pass through the 100s before it reaches the 900s.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('bf-cv'), c = cv.getContext('2d');
  var read = document.getElementById('bf-read');
  var W = cv.width, H = cv.height, pad = 44;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  function firstDigitFromLog(lg){
    var frac = lg - Math.floor(lg);
    return Math.floor(Math.pow(10, frac));
  }
  function tallyLogs(logs){
    var t = [0,0,0,0,0,0,0,0,0,0];
    logs.forEach(function(lg){ var d = firstDigitFromLog(lg); if(d >= 1 && d <= 9) t[d]++; });
    return t;
  }
  function datasets(name){
    var logs = [], i;
    if(name === 'pow'){
      for(i = 1; i <= 600; i++) logs.push(i*Math.log10(2));
      return ['first 600 powers of 2', tallyLogs(logs)];
    }
    if(name === 'fib'){
      var phi = (1 + Math.sqrt(5))/2, lphi = Math.log10(phi), l5 = Math.log10(Math.sqrt(5));
      for(i = 1; i <= 600; i++) logs.push(i*lphi - l5);
      return ['first 600 Fibonacci numbers', tallyLogs(logs)];
    }
    if(name === 'pop'){
      for(i = 0; i < 2000; i++){
        var z = 0;
        for(var k = 0; k < 12; k++) z += Math.random();
        z = (z - 6)/1;  // approximately standard normal
        logs.push(4 + 0.9*z);  // lognormal populations, median 10,000
      }
      return ['2,000 simulated city populations', tallyLogs(logs)];
    }
    var t = [0,0,0,0,0,0,0,0,0,0];
    for(i = 0; i < 2000; i++){
      var x = 1 + Math.random()*999;
      var d = parseInt(String(Math.floor(x)).charAt(0), 10);
      t[d]++;
    }
    return ['2,000 uniform random numbers from 1 to 1,000', t];
  }
  function draw(name){
    var res = datasets(name), label = res[0], t = res[1];
    var total = t.reduce(function(a, b){ return a + b; }, 0);
    c.clearRect(0, 0, W, H);
    var bw = (W - 2*pad)/9;
    c.strokeStyle = '#e0e0e0'; c.beginPath();
    c.moveTo(pad, H - 36); c.lineTo(W - pad, H - 36); c.stroke();
    for(var d = 1; d <= 9; d++){
      var f = t[d]/total;
      var x = pad + (d - 1)*bw;
      var h = f*(H - 90)/0.35;
      c.fillStyle = '#c9c9c6';
      c.fillRect(x + bw*0.18, H - 36 - h, bw*0.64, h);
      var bp = Math.log10(1 + 1/d);
      var by = H - 36 - bp*(H - 90)/0.35;
      c.strokeStyle = '#1f1f1f'; c.lineWidth = 2;
      c.beginPath(); c.moveTo(x + bw*0.12, by); c.lineTo(x + bw*0.88, by); c.stroke();
      c.fillStyle = '#5c5c5c'; c.font = '12px Hanken Grotesk, sans-serif';
      c.fillText(String(d), x + bw/2 - 3, H - 18);
      c.fillStyle = '#9a9a97'; c.font = '10px Hanken Grotesk, sans-serif';
      c.fillText((f*100).toFixed(1), x + bw*0.2, H - 42 - h);
    }
    read.textContent = label + '; markers show Benford’s predictions';
  }
  document.getElementById('bf-pow').addEventListener('click', function(){ draw('pow'); });
  document.getElementById('bf-fib').addEventListener('click', function(){ draw('fib'); });
  document.getElementById('bf-pop').addEventListener('click', function(){ draw('pop'); });
  document.getElementById('bf-uni').addEventListener('click', function(){ draw('uni'); });
  draw('pow');
})();
</script>

The bars compare the first digits in each dataset with the Benford probabilities.

Some datasets follow the pattern closely.

Others do not.

## Why a logarithm appears

Consider the numbers with leading digit 1.

On [a logarithmic scale](/2026/07/30/logarithms-undo-exponentials.html), those numbers occupy intervals such as

$$ [1,2),\quad[10,20),\quad[100,200), $$

and so on.

The width of each interval on a base-10 logarithmic scale is

$$ \log_{10}2-\log_{10}1 = \log_{10}2. $$

For leading digit $$d$$, the corresponding width is

$$ \log_{10}(d+1)-\log_{10}d = \log_{10}\left(1+\frac1d\right). $$

If the fractional parts of the logarithms are approximately uniform, the first digits follow Benford's law.

This is why the pattern is natural for data spread across several orders of magnitude.

## When Benford's law is plausible

The law often appears in datasets produced by multiplicative processes or by combining measurements across a wide range of scales.

Examples can include populations, financial quantities, physical measurements, and sequences that grow roughly exponentially.

It is usually a poor model for:

- assigned numbers such as ZIP codes or identification numbers
- data restricted to a narrow interval
- quantities with a built-in minimum or maximum
- numbers generated uniformly over a short range

A dataset does not become suspicious merely because it fails to follow Benford's law.

The law has to be plausible for that particular data-generating process first.

## Scale invariance

One important property of Benford's law is scale invariance.

If a Benford-distributed dataset measured in dollars is converted to euros by multiplying every value by a positive constant, the first-digit distribution remains Benford.

A law for first digits that depended strongly on the choice of units would be difficult to treat as a general empirical pattern.

The logarithmic form avoids that problem.

## Auditing and screening

Benford's law is sometimes used as a screening tool in forensic accounting and data auditing.

A large departure from the expected first-digit distribution can motivate closer inspection.

It is not proof of fraud.

There are many legitimate reasons for a dataset not to follow Benford's law.

Conversely, manipulated data can still resemble the Benford distribution.

A statistical discrepancy is evidence about a model, not a verdict about intent.

That distinction is especially important when a method is used outside the classroom.

## A goodness-of-fit connection

One way to compare observed first-digit counts with the Benford probabilities is a [chi-square goodness-of-fit statistic](/2026/07/15/which-chi-square-test.html).

The expected count for digit $$d$$ is

$$ nP(D=d). $$

Then observed and expected counts can be compared across the nine categories.

The calculation is a useful example of how a theoretical probability model can be checked against empirical frequencies.

It also illustrates a broader principle.

<div class="article-note" markdown="1">
Before testing fit, decide whether the model itself makes sense for the data.
</div>
