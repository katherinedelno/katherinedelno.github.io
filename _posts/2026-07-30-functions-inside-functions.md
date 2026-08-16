---
layout: post
title: "Functions inside functions"
date: 2026-07-30
description: "Composition sends the output of one function into another. Order matters, and the domain of the composite has to satisfy both functions."
course: "AP Precalculus"
read_time: "6 min read"
math: true
kind: foundations
sequence: 4
interactive: true
blurb: "Composition sends the output of one function into another. Order matters, and the domain of the composite has to satisfy both functions"
image: "/assets/og/functions-inside-functions.png"
---

Function composition connects two functions in sequence.

In

$$f(g(x)),$$

the input goes into $$g$$ first.

The output of $$g$$ then becomes the input of $$f$$.

The inside function acts first.

The outside function acts last.

## Follow the pipeline

<div class="viz" markdown="0">
  <canvas id="cf-cv" width="700" height="320"></canvas>
  <div class="viz-controls">
    <label for="cf-g">g, first</label>
    <select id="cf-g" class="cf-sel">
      <option value="lin" selected>2x + 1</option>
      <option value="sq">x&#178;</option>
      <option value="sqrt">&#8730;x</option>
      <option value="abs">|x|</option>
    </select>
    <label for="cf-f">f, second</label>
    <select id="cf-f" class="cf-sel">
      <option value="sq" selected>x&#178;</option>
      <option value="lin">2x + 1</option>
      <option value="sqrt">&#8730;x</option>
      <option value="abs">|x|</option>
    </select>
    <button type="button" id="cf-swap" class="res-filter" style="font-size:.72rem">swap f and g</button>
  </div>
  <div class="viz-controls">
    <label for="cf-x">input x</label>
    <input type="range" id="cf-x" min="-4" max="4" step="0.1" value="3">
    <span class="viz-value" id="cf-read"></span>
  </div>
  <p class="viz-caption">The upper band is the pipeline: x enters g, and g's output enters f. The graph below it draws the composite f(g(x)) in ink, with g dashed and f dotted for reference. Where the composite line breaks, the first machine has produced a value the second cannot accept. Swap the order and the composite changes shape. Composition is not commutative, and the graph shows it immediately.</p>
  <style>
    .viz .cf-sel{font:inherit;font-size:.9rem;padding:4px 8px;border:1px solid var(--line);border-radius:8px;background:#fff;color:var(--ink)}
    .viz .cf-sel:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv = document.getElementById('cf-cv'), c = cv.getContext('2d');
  var selF = document.getElementById('cf-f'), selG = document.getElementById('cf-g');
  var swap = document.getElementById('cf-swap');
  var slider = document.getElementById('cf-x'), read = document.getElementById('cf-read');

  var W = 700, H = 320;
  (function crisp(){
    var d = Math.min(window.devicePixelRatio || 1, 2);
    cv.width = W*d; cv.height = H*d; c.setTransform(d,0,0,d,0,0);
  })();

  var FNS = {
    lin:  { label: '2x + 1', fn: function(x){ return 2*x + 1; }, dom: function(){ return true; } },
    sq:   { label: 'x²', fn: function(x){ return x*x; }, dom: function(){ return true; } },
    sqrt: { label: '√x', fn: function(x){ return Math.sqrt(x); }, dom: function(x){ return x >= 0; } },
    abs:  { label: '|x|', fn: function(x){ return Math.abs(x); }, dom: function(){ return true; } }
  };
  var FONT = '"Hanken Grotesk",-apple-system,sans-serif';
  var INK = '#1f1f1f', MUTED = '#5c5c5c', LINE = '#e6e6e6', FAINT = '#9a9a97';

  // pipeline band: y 0..96; graph: y 104..312
  var GL = 46, GR = 688, GT = 112, GB = 300;
  var XLO = -4, XHI = 4, YLO = -4, YHI = 8;
  function px(x){ return GL + (x - XLO)/(XHI - XLO)*(GR - GL); }
  function py(y){ return GB - (y - YLO)/(YHI - YLO)*(GB - GT); }

  function evalChain(g, f, x){
    if(!g.dom(x)) return { gx: null, fgx: null };
    var gx = g.fn(x);
    if(!f.dom(gx)) return { gx: gx, fgx: null };
    return { gx: gx, fgx: f.fn(gx) };
  }
  function fmt(v){ return v === null ? 'undefined' : (Math.round(v*100)/100).toString(); }

  function box(cx, w, label, value, strong){
    c.strokeStyle = strong ? INK : LINE; c.lineWidth = strong ? 1.5 : 1;
    c.fillStyle = '#ffffff';
    var x0 = cx - w/2;
    c.beginPath();
    if(c.roundRect) c.roundRect(x0, 22, w, 52, 8); else c.rect(x0, 22, w, 52);
    c.fill(); c.stroke();
    c.fillStyle = FAINT; c.font = '600 9px ' + FONT; c.textAlign = 'center';
    c.fillText(label.toUpperCase(), cx, 36);
    c.fillStyle = INK; c.font = '15px ' + FONT;
    c.fillText(value, cx, 60);
  }
  function arrow(x0, x1, y){
    c.strokeStyle = MUTED; c.lineWidth = 1;
    c.beginPath(); c.moveTo(x0, y); c.lineTo(x1 - 5, y); c.stroke();
    c.beginPath(); c.moveTo(x1, y); c.lineTo(x1 - 7, y - 4); c.lineTo(x1 - 7, y + 4);
    c.fillStyle = MUTED; c.fill();
  }

  function plot(fun, color, width, dash){
    c.save();
    c.beginPath(); c.rect(GL, GT, GR - GL, GB - GT); c.clip();
    c.strokeStyle = color; c.lineWidth = width; c.setLineDash(dash || []);
    c.beginPath();
    var pen = false;
    for(var i = 0; i <= 560; i++){
      var x = XLO + (XHI - XLO)*i/560;
      var y = fun(x);
      if(y === null || !isFinite(y) || y < YLO - 6 || y > YHI + 6){ pen = false; continue; }
      if(pen) c.lineTo(px(x), py(y)); else { c.moveTo(px(x), py(y)); pen = true; }
    }
    c.stroke(); c.restore();
  }

  function draw(){
    var g = FNS[selG.value], f = FNS[selF.value];
    var x = parseFloat(slider.value);
    var r = evalChain(g, f, x);
    c.clearRect(0, 0, W, H);

    // pipeline
    box(90, 96, 'input x', fmt(x), false);
    arrow(140, 202, 48);
    box(258, 110, 'g: ' + g.label, r.gx === null ? 'undefined' : fmt(r.gx), false);
    arrow(315, 377, 48);
    box(433, 110, 'f: ' + f.label, r.fgx === null ? 'undefined' : fmt(r.fgx), false);
    arrow(490, 552, 48);
    box(613, 130, 'f(g(x))', fmt(r.fgx), true);

    // graph frame
    c.strokeStyle = LINE; c.lineWidth = 1;
    c.strokeRect(GL + .5, GT + .5, GR - GL, GB - GT);
    c.font = '10px ' + FONT; c.fillStyle = MUTED;
    c.textAlign = 'center'; c.textBaseline = 'top';
    for(var xt = XLO; xt <= XHI; xt += 2){ c.fillText(String(xt), px(xt), GB + 5); }
    c.textAlign = 'right'; c.textBaseline = 'middle';
    for(var yt = YLO; yt <= YHI; yt += 4){ c.fillText(String(yt), GL - 6, py(yt)); }
    // axes through 0
    c.strokeStyle = LINE;
    c.beginPath(); c.moveTo(px(0), GT); c.lineTo(px(0), GB); c.stroke();
    c.beginPath(); c.moveTo(GL, py(0)); c.lineTo(GR, py(0)); c.stroke();

    plot(function(x){ return g.dom(x) ? g.fn(x) : null; }, FAINT, 1.5, [6,5]);
    plot(function(x){ return f.dom(x) ? f.fn(x) : null; }, FAINT, 1.5, [2,4]);
    plot(function(x){ return evalChain(g, f, x).fgx; }, INK, 2.2);

    // moving point on the composite
    if(r.fgx !== null && r.fgx >= YLO && r.fgx <= YHI){
      c.beginPath(); c.arc(px(x), py(r.fgx), 5, 0, 7);
      c.fillStyle = INK; c.fill();
    }
    // legend
    c.textAlign = 'left'; c.textBaseline = 'alphabetic';
    c.fillStyle = INK; c.font = '600 10px ' + FONT;
    c.fillText('f(g(x))', GL + 8, GT + 16);
    c.fillStyle = FAINT; c.font = '10px ' + FONT;
    c.fillText('g dashed · f dotted', GL + 60, GT + 16);

    read.textContent = r.fgx === null
      ? 'f(g(' + fmt(x) + ')) is undefined'
      : 'f(g(' + fmt(x) + ')) = ' + fmt(r.fgx);
  }

  swap.addEventListener('click', function(){
    var t = selF.value; selF.value = selG.value; selG.value = t; draw();
  });
  [selF, selG].forEach(function(s){ s.addEventListener('change', draw); });
  slider.addEventListener('input', draw);
  draw();
})();
</script>

The visualization shows the intermediate value between the two functions.

It also graphs the composite.

If the first function produces an output that the second function cannot accept, the composite is undefined there.

Swapping the order generally changes the result.

## Order matters

Let

$$g(x)=2x+1$$

and

$$f(x)=x^2.$$

At $$x=3$$,

$$g(3)=7,$$

so

$$f(g(3)) = f(7) = 49.$$

Reverse the order.

First,

$$f(3)=9.$$

Then

$$g(f(3)) = g(9) = 19.$$

Thus

$$f\circ g$$

and

$$g\circ f$$

are different functions.

Composition is not commutative.

## Reading a composite from the outside

Suppose

$$h(x)=\sqrt{3x+1}.$$

To decompose it, ask what operation happens last.

The final operation is a square root.

So a natural choice is

$$f(u)=\sqrt{u}$$

and

$$g(x)=3x+1.$$

Then

$$h(x)=f(g(x)).$$

Giving the inside expression a temporary name often makes the structure easier to see.

Write

$$u=3x+1.$$

Then

$$h=\sqrt{u}.$$

The decomposition is not always unique.

For

$$(x+2)^6,$$

one valid decomposition is a sixth power applied to $$x+2$$.

Another is a cube applied to $$(x+2)^2$$.

A useful decomposition is usually the one that makes the relevant operation easiest to analyze.

## Domains pass through both functions

Suppose

$$g(x)=2x+1$$

and

$$f(x)=\sqrt{x}.$$

Then

$$f(g(x)) = \sqrt{2x+1}.$$

For the composite to exist, $$x$$ must be in the domain of $$g$$, and $$g(x)$$ must lie in the domain of $$f$$.

Here that means

$$2x+1\ge0,$$

so

$$x\ge-\frac12.$$

In general,

$$x\in\operatorname{dom}(f\circ g)$$

exactly when

$$x\in\operatorname{dom}(g)$$

and

$$g(x)\in\operatorname{dom}(f).$$

Simplifying an expression can sometimes hide an original restriction, so it is worth determining the domain from the composition itself.

## Composition appears everywhere later

[Graph transformations](/2026/07/25/transformations-four-dials.html) are compositions.

[Exponential and logarithmic models](/2026/07/30/logarithms-undo-exponentials.html) are compositions.

Inverse functions undo compositions in reverse order.

In calculus, the chain rule differentiates compositions by identifying the same inner and outer layers.

The notation becomes more elaborate later, but the underlying reading skill is the same.

<div class="article-note" markdown="1">
A useful self-test is to compare

$$(\sqrt{x})^2$$

with

$$\sqrt{x^2}.$$

The first is defined only for

$$x\ge0$$

and simplifies to $$x$$ on that domain.

The second is defined for every real $$x$$ and equals

$$\vert x\vert .$$

The operations look similar.

Their order changes both the output and the domain.
</div>
