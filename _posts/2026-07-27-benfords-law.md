---
layout: post
title: "Benford's law and the distribution of first digits"
date: 2026-07-27
description: "In a surprising range of real datasets, the leading digit 1 appears about 30% of the time. The logarithmic law behind the pattern, and its use in the detection of fraud."
course: "AP Statistics"
read_time: "7 min read"
math: true
---

Collect the populations of every county in the United States, or the lengths of the world's rivers, or the line items of a corporate ledger, and tally the first digit of each number. Intuition expects the nine digits to appear roughly equally, about 11% each. What actually happens is one of the strangest reliable facts in statistics: the digit 1 leads about 30% of the time, 2 about 18%, and the frequencies fall steadily until 9, which leads barely 5% of entries.

The pattern is called Benford's law, after the physicist Frank Benford, who documented it in 1938 across twenty unrelated datasets, from atomic weights to street addresses, though the astronomer Simon Newcomb had noticed it fifty years earlier in the worn early pages of logarithm tables. The law states that the probability of leading digit $$d$$ is

$$P(d) = \log_{10}\!\left(1 + \frac{1}{d}\right)$$

which gives the sequence 30.1%, 17.6%, 12.5%, 9.7%, 7.9%, 6.7%, 5.8%, 5.1%, 4.6%.

## Watching datasets obey, and disobey

The tally below computes first digits for several datasets. The dark bars are the observed frequencies; the small markers are Benford's predictions.

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

## Why the logarithm appears

The cleanest explanation runs through growth. A quantity that grows by a fixed percentage, an investment, a bacterial colony, a city, spends unequal time in the territory of each leading digit. Growing from 1,000 to 2,000 requires doubling, while growing from 8,000 to 9,000 requires an increase of merely 12.5%, so the quantity lingers among the low leading digits and hurries through the high ones. On a logarithmic scale, the intervals belonging to each digit have exactly the widths that Benford's formula assigns, and any dataset that is spread smoothly across several orders of magnitude inherits those proportions.

The law also has a characterization with real mathematical depth: it is the only first-digit distribution that is invariant under changes of unit. Convert river lengths from miles to kilometers, or a ledger from dollars to euros, and every entry is multiplied by a constant, yet the first-digit pattern of a Benford dataset is undisturbed. A distribution that survives every rescaling must be uniform in the logarithm, and Benford's formula is what uniform-in-the-logarithm looks like in ordinary digits.

## The forensic application

The law's fame rests on its use in auditing. Invented numbers do not obey it. People fabricating expenses, tax figures, or trial data tend to distribute first digits far too evenly, overusing middle digits and avoiding the repetition of leading 1s that honest data exhibits. Auditors and forensic accountants therefore run first-digit tests on ledgers, and a chi-square comparison of observed digit counts against Benford's expected proportions, exactly the goodness-of-fit machinery of a statistics course, flags accounts deserving a closer look. Benford analysis has appeared in tax-fraud prosecutions, in the auditing of election returns, and in the detection of manipulated scientific data.

Two cautions complete the picture, and both are good statistical sense. A Benford violation is a screen rather than a verdict: some honest datasets fail the law for structural reasons, as when a price list clusters at 4.99. And datasets confined to a narrow range, human heights, exam scores, temperatures, never obeyed the law in the first place, since they lack the multi-scale spread that generates it. Knowing when a tool applies is the tool.

<div class="article-note" markdown="1">
A prediction to test against the interactive: the law extends to second digits, with a flatter but still unequal distribution, and by the fourth digit the frequencies are essentially uniform. Forensic tests use the first two digits jointly for exactly this reason, giving 90 categories instead of 9 and a far sharper screen. The pattern of decreasing information as one moves rightward through the digits is itself the logarithm at work.
</div>
