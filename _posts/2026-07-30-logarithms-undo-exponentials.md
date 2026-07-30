---
layout: post
title: "Logarithms undo exponentials"
date: 2026-07-30
description: "A logarithm is an exponent: the two notations state one fact, the graphs mirror across y = x, and every log law is an exponent law read backward."
course: "AP Precalculus"
read_time: "7 min read"
math: true
kind: mechanics
sequence: 3
interactive: true
blurb: "Slide the base and watch b^x and its logarithm mirror across y = x"
---

Most difficulty with logarithms comes from treating them as a new species of object with its own arbitrary rulebook. They are not. A logarithm is an exponent — $$\log_b y$$ is the answer to one question: *b raised to what power gives y?* Hold onto that sentence and every rule in this article becomes something you can rederive in a line rather than memorize.

The graphs below stay locked in a mirror. Slide the exponent to move the point along $$y = b^x$$; its reflection across the line $$y = x$$ rides the logarithm's graph, because the two curves are the same relationship read in opposite directions.

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
  <p class="viz-caption">The solid curve is y = b^x; the lighter curve is its inverse, the logarithm base b; the dashed diagonal is y = x. The two marked points are reflections of each other: if b^a = y, then the logarithm of y is a — one fact, plotted twice, as the panels on either side of the graph spell out. Slide the base through e &#8776; 2.718; nothing dramatic marks it, and that is rather the point. Push the base higher and the exponential steepens while the logarithm flattens.</p>
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

## The same fact, written twice

Every logarithmic statement is an exponential statement wearing different clothes:

$$b^a = y \quad\Longleftrightarrow\quad \log_b y = a.$$

So $$2^5 = 32$$ and $$\log_2 32 = 5$$ are not two facts; they are one fact. When a logarithm looks opaque, convert it. Asked for $$\log_5 125$$, do not reach for a rule — ask the question the notation asks: *5 to what power is 125?* Three. Asked to solve $$\log_x 49 = 2$$, rewrite it as $$x^2 = 49$$ and it stops being a logarithm problem at all.

The graphs say the same thing geometrically. Reflecting a point across the line $$y = x$$ swaps its coordinates, and swapping coordinates is exactly what the equivalence above does: the point $$(a, y)$$ sits on the exponential precisely when $$(y, a)$$ sits on the logarithm. That is what it means for two functions to be inverses, and it is why the logarithm's graph inherits everything about the exponential's, sideways: the exponential's horizontal asymptote becomes the logarithm's vertical one, and the exponential's refusal to output negative numbers becomes the logarithm's refusal to accept them.

## The laws are exponent laws, read backward

Exponents turn multiplication into addition: $$b^m \cdot b^n = b^{m+n}$$. Since logarithms *are* exponents, they inherit this directly. If $$m = \log_b x$$ and $$n = \log_b y$$, then $$xy = b^m b^n = b^{m+n}$$, and reading off the exponent of the product gives

$$\log_b(xy) = \log_b x + \log_b y.$$

The other two laws arrive the same way, each from its exponent-law parent: $$\log_b\!\left(\tfrac{x}{y}\right) = \log_b x - \log_b y$$ comes from $$b^m / b^n = b^{m-n}$$, and $$\log_b(x^k) = k \log_b x$$ comes from $$(b^m)^k = b^{mk}$$. Three laws, zero new memorization — each is a sentence about exponents you already believe.

The errors worth naming are the laws that do not exist. $$\log_b(x + y)$$ is not $$\log_b x + \log_b y$$ — logarithms convert *multiplication* to addition, and they do nothing tidy to sums. And $$(\log_b x)^2$$ is not $$\log_b(x^2)$$: the first squares an exponent after the fact, the second doubles it. Writing the parentheses deliberately is not pedantry; it is the whole meaning.

## Solving equations: undo in the right order

To solve an exponential equation, take a logarithm; to solve a logarithmic equation, exponentiate. The only technique is deciding [what to undo first](/2026/07/30/functions-inside-functions.html). Solve

$$5 \cdot 3^t = 40.$$

Isolate the exponential before touching a logarithm: $$3^t = 8$$. Now the equation says, in exponential form, exactly what $$t = \log_3 8$$ says in logarithmic form — and the change-of-base formula turns that into something a calculator accepts: $$t = \frac{\ln 8}{\ln 3} \approx 1.893$$. Check it forward: $$3^{1.893} \approx 8.00$$, and $$5 \cdot 8 = 40$$.

The order matters. Taking a log of both sides of $$5 \cdot 3^t = 40$$ first is legal but produces $$\log 5 + t\log 3 = \log 40$$, an extra step that exists only to undo the 5 you could have divided away at the start. Isolate, then invert.

## The base e

Among all possible bases, one is special enough to own a key on the calculator: $$e \approx 2.718$$, with its logarithm written $$\ln x$$. In precalculus, $$e$$ earns its place through continuous growth — compounding a rate more and more often walks the growth factor toward $$e$$, which is why continuously compounded models are written $$A(t) = A_0 e^{rt}$$. Press "set base to e" above and look at the pair of curves; nothing visually dramatic marks the spot, and that is rather the point: $$e$$ is not a strange base, just the natural one, and $$\ln$$ obeys every law in this article with no special cases.

For those continuing to calculus: that course runs almost entirely on base $$e$$, and it will assume the equivalence $$b^a = y \Leftrightarrow \log_b y = a$$, the three laws, and clean parenthesizing as reflexes rather than topics. The reflexes are built here.

<div class="article-note" markdown="1">
A self-test at the slider: push the base down toward its lower limit and watch both curves at once. The exponential flattens toward the horizontal line $$y = 1$$, and its mirror steepens toward the vertical. At $$b = 1$$ exactly, $$b^x$$ would be the constant function 1, which fails the horizontal line test and therefore has no inverse. The rule that a logarithm requires $$b \neq 1$$ is that collapse, caught one step before it happens.
</div>
