---
layout: post
title: "Logarithms undo exponentials"
date: 2026-07-30
description: "A logarithm is an exponent. Exponential and logarithmic statements describe the same relationship in opposite directions."
course: "AP Precalculus"
read_time: "5 min read"
math: true
kind: mechanics
sequence: 5
interactive: true
blurb: "A logarithm is an exponent. Exponential and logarithmic statements describe the same relationship in opposite directions"
image: "/assets/og/logarithms-undo-exponentials.png"
---

A logarithm answers an exponent question. The statement $$\log_b y=a$$ means exactly the same thing as $$b^a=y$$, and keeping those two forms connected makes most logarithm rules easier to understand.

## The same relationship in two directions

<div class="viz" markdown="0">
  <canvas id="el-cv" width="700" height="360"></canvas>
  <div class="viz-controls">
    <label for="el-b">base b</label>
    <input type="range" id="el-b" min="1.2" max="8" step="0.001" value="2">
    <button type="button" id="el-e" class="res-filter" style="font-size:.72rem">set base to e</button>
  </div>
  <div class="viz-controls">
    <label for="el-a">exponent a</label>
    <input type="range" id="el-a" min="-2" max="3" step="0.05" value="1.5">
    <span class="viz-value" id="el-read"></span>
  </div>
  <p class="viz-caption">The solid curve is y = b^x; the lighter curve is its inverse, the logarithm base b; the dashed diagonal is y = x. The two marked points are reflections of each other: if b^a = y, then the logarithm of y is a. One fact, plotted twice, as the panels on either side of the graph spell out. Slide the base through e &#8776; 2.718; nothing dramatic marks it, and that is rather the point. Push the base higher and the exponential steepens while the logarithm flattens.</p>
</div>

<script>
(function(){
  'use strict';
  var cv = document.getElementById('el-cv'), c = cv.getContext('2d');
  var sb = document.getElementById('el-b'), sa = document.getElementById('el-a');
  var eBtn = document.getElementById('el-e'), read = document.getElementById('el-read');

  var W = 700, H = 360;
  (function crisp(){
    var d = Math.min(window.devicePixelRatio || 1, 2);
    cv.width = W*d; cv.height = H*d; c.setTransform(d,0,0,d,0,0);
  })();

  var FONT = '"Hanken Grotesk",-apple-system,sans-serif';
  var INK = '#1f1f1f', MUTED = '#5c5c5c', LINE = '#e6e6e6', FAINT = '#9a9a97';

  // square plot region so the mirror is geometrically honest
  var PL = 195, PR = 515, PT = 15, PB = 335;   // 320 x 320 px
  var LO = -2, HI = 8;                          // same units both axes
  function px(x){ return PL + (x - LO)/(HI - LO)*(PR - PL); }
  function py(y){ return PB - (y - LO)/(HI - LO)*(PB - PT); }

  function plot(fun, color, width){
    c.save();
    c.beginPath(); c.rect(PL, PT, PR - PL, PB - PT); c.clip();
    c.strokeStyle = color; c.lineWidth = width; c.setLineDash([]);
    c.beginPath();
    var pen = false;
    for(var i = 0; i <= 640; i++){
      var x = LO + (HI - LO)*i/640;
      var y = fun(x);
      if(y === null || !isFinite(y) || y < LO - 8 || y > HI + 8){ pen = false; continue; }
      if(pen) c.lineTo(px(x), py(y)); else { c.moveTo(px(x), py(y)); pen = true; }
    }
    c.stroke(); c.restore();
  }

  function fmt(v, d){ return Number(v).toFixed(d === undefined ? 2 : d).replace('-', '−'); }

  function draw(){
    var b = parseFloat(sb.value), a = parseFloat(sa.value);
    var yv = Math.pow(b, a);
    c.clearRect(0, 0, W, H);

    // frame + axes
    c.strokeStyle = LINE; c.lineWidth = 1;
    c.strokeRect(PL + .5, PT + .5, PR - PL, PB - PT);
    c.beginPath(); c.moveTo(px(0), PT); c.lineTo(px(0), PB); c.stroke();
    c.beginPath(); c.moveTo(PL, py(0)); c.lineTo(PR, py(0)); c.stroke();
    c.font = '10px ' + FONT; c.fillStyle = MUTED;
    c.textAlign = 'center'; c.textBaseline = 'top';
    for(var t = -2; t <= 8; t += 2){ c.fillText(String(t), px(t), PB + 5); }
    c.textAlign = 'right'; c.textBaseline = 'middle';
    for(t = -2; t <= 8; t += 2){ c.fillText(String(t), PL - 6, py(t)); }

    // mirror line y = x
    c.save();
    c.beginPath(); c.rect(PL, PT, PR - PL, PB - PT); c.clip();
    c.strokeStyle = LINE; c.setLineDash([6,5]); c.lineWidth = 1.5;
    c.beginPath(); c.moveTo(px(LO), py(LO)); c.lineTo(px(HI), py(HI)); c.stroke();
    c.restore();

    plot(function(x){ return Math.pow(b, x); }, INK, 2.2);
    plot(function(x){ return x > 0 ? Math.log(x)/Math.log(b) : null; }, FAINT, 2);

    // the mirrored pair
    function dot(x, y, fill){
      if(x < LO || x > HI || y < LO || y > HI) return false;
      c.beginPath(); c.arc(px(x), py(y), 5, 0, 7);
      c.fillStyle = fill; c.fill();
      return true;
    }
    var p1 = dot(a, yv, INK);
    var p2 = dot(yv, a, MUTED);
    if(p1 && p2){
      c.save();
      c.strokeStyle = FAINT; c.setLineDash([3,4]); c.lineWidth = 1;
      c.beginPath(); c.moveTo(px(a), py(yv)); c.lineTo(px(yv), py(a)); c.stroke();
      c.restore();
    }

    // left margin: the exponential statement
    c.textAlign = 'left'; c.textBaseline = 'alphabetic';
    c.fillStyle = FAINT; c.font = '600 9px ' + FONT;
    c.fillText('EXPONENTIAL FORM', 12, 110);
    c.fillStyle = INK; c.font = '15px ' + FONT;
    c.fillText(fmt(b) + ' ^ ' + fmt(a) + ' = ' + fmt(yv), 12, 132);
    // right margin: the logarithmic statement
    c.fillStyle = FAINT; c.font = '600 9px ' + FONT;
    c.fillText('LOGARITHMIC FORM', 528, 110);
    c.fillStyle = MUTED; c.font = '15px ' + FONT;
    c.fillText('log' + fmt(b) + '(' + fmt(yv) + ')', 528, 132);
    c.fillText('= ' + fmt(a), 528, 152);
    c.fillStyle = FAINT; c.font = '10px ' + FONT;
    c.fillText('one fact,', 528, 180);
    c.fillText('written twice', 528, 194);

    read.textContent = fmt(b) + '^' + fmt(a) + ' = ' + fmt(yv);
  }

  eBtn.addEventListener('click', function(){ sb.value = Math.E.toFixed(3); draw(); });
  sb.addEventListener('input', draw);
  sa.addEventListener('input', draw);
  draw();
})();
</script>

The exponential and logarithmic graphs are reflections across $$y=x$$. If $$b^a=y$$, then the point $$(a,y)$$ lies on the exponential graph, and the reflected point $$(y,a)$$ lies on the logarithmic graph because $$\log_b y=a$$. This is what it means for the two functions to be inverses.

For example, $$2^5=32$$ and $$\log_2 32=5$$ are two forms of the same fact. When a logarithmic expression looks unfamiliar, rewriting it exponentially is often the cleanest first move.

## The domain and asymptote also reverse

For $$b>0,\; b\neq1$$, the exponential function $$b^x$$ always produces positive outputs, so its range is $$(0,\infty)$$. The logarithm reverses inputs and outputs, so its domain is $$(0,\infty)$$. The horizontal asymptote $$y=0$$ of the exponential becomes the vertical asymptote $$x=0$$ of the logarithm, and the geometry and the algebra say the same thing.

## Logarithm laws come from exponent laws

Suppose $$m=\log_b x$$ and $$n=\log_b y$$, so that $$x=b^m$$ and $$y=b^n$$. Since $$b^m b^n=b^{m+n}$$, we get $$\log_b(xy) = \log_b x+\log_b y$$. Similarly,

$$\log_b\left(\frac{x}{y}\right) = \log_b x-\log_b y \qquad\text{and}\qquad \log_b(x^k) = k\log_b x$$

These are exponent laws translated into logarithmic form. There is no corresponding rule for sums, and in general $$\log_b(x+y) \neq \log_b x+\log_b y$$. Logarithms turn multiplication into addition, and they do not turn addition into anything similarly simple.

## Solving exponential equations

Consider $$5\cdot3^t=40$$. First isolate the exponential, $$3^t=8$$, and then write the equivalent logarithmic statement, $$t=\log_3 8$$. Using change of base,

$$t = \frac{\ln8}{\ln3} \approx1.893$$

The reverse process solves logarithmic equations. If $$\log_2 x=5$$, then $$x=2^5=32$$. The useful principle is to [isolate the invertible function first](/2026/07/30/functions-inside-functions.html), then apply its inverse.

## The base $$e$$

The number $$e\approx2.718$$ is the standard base for continuous exponential growth. The logarithm base $$e$$ is written $$\ln x$$, and it follows all the same logarithm laws. Its importance becomes greater in calculus because $$e^x$$ has especially simple derivative and integral behavior. For precalculus, it is enough to treat $$e$$ as a particular exponential base and $$\ln$$ as its inverse.

<div class="article-note" markdown="1">
The restrictions on logarithmic bases also make sense from invertibility. At $$b=1$$, the exponential function would be $$1^x=1$$, a constant function. It is not one-to-one and therefore has no inverse function.
</div>
