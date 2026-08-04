---
layout: post
title: "Functions inside functions"
date: 2026-07-30
description: "Composition runs one function's output into another's input, and the order changes everything. A pipeline to operate, and the skill of reading a composite from the outside in."
course: "AP Precalculus"
read_time: "6 min read"
math: true
kind: foundations
sequence: 4
interactive: true
blurb: "Feed one function through another and see why order matters"
image: "/assets/og/functions-inside-functions.png"
---

A function is a machine: a number goes in, a number comes out. Composition is what happens when two machines run in a row — the output of the first is fed directly into the second, no stops. We write the result as $$f(g(x))$$, and it is worth reading that notation aloud the way it actually operates: $$x$$ goes into $$g$$ first, and whatever $$g$$ produces goes into $$f$$. The function written on the outside acts last.

The pipeline below runs live. Choose the two machines, slide the input, and watch the intermediate value pass from one to the other.

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
  <p class="viz-caption">The upper band is the pipeline: x enters g, and g's output enters f. The graph below it draws the composite f(g(x)) in ink, with g dashed and f dotted for reference. Where the composite line breaks, the first machine has produced a value the second cannot accept. Swap the order and the composite changes shape — composition is not commutative, and the graph shows it immediately.</p>
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

## Order matters

Set the machines to $$g(x) = 2x + 1$$ first and $$f(x) = x^2$$ second, and read the pipeline at $$x = 3$$: the 3 becomes 7, and the 7 becomes 49. That is $$f(g(3)) = (2 \cdot 3 + 1)^2 = 49$$. Now press "swap f and g," so the squaring happens first: 3 becomes 9, and 9 becomes 19. That is $$g(f(3)) = 2 \cdot 3^2 + 1 = 19$$.

Same two machines, same input, different answers — because $$(2x+1)^2$$ and $$2x^2 + 1$$ are different functions. Composition is not commutative, and this is the single most common composition error: treating $$f(g(x))$$ and $$g(f(x))$$ as interchangeable because both "use $$f$$ and $$g$$." The graph makes the difference visible faster than the algebra does. Swap the order and the composite's whole shape changes.

## Reading a composite from the outside in

The harder skill, and the one exams reward, runs in reverse: you are handed the finished composite and asked to see the machines inside it. Take

$$h(x) = \sqrt{3x + 1}.$$

Nobody hands you $$f$$ and $$g$$; you have to find them. The reliable method is to ask what the function does to its input, *last*. Here, the last thing that happens is a square root — so the outside function is $$f(u) = \sqrt{u}$$, and everything under the root is the inside, $$g(x) = 3x + 1$$. Check by running the pipeline forward: $$x = 5$$ gives $$3(5) + 1 = 16$$, and $$\sqrt{16} = 4$$. The decomposition works when composing it back gives you the original function.

Two habits make this reliable. First, give the inside a name — writing $$u = 3x + 1$$, so that $$h = \sqrt{u}$$, turns a nested expression into two simple ones. Second, expect more than one right answer: $$h(x) = (x+2)^6$$ decomposes naturally as $$u = x + 2$$ inside the sixth power, but $$u = (x+2)^2$$ inside a cube is also correct. Decompositions are not unique; useful ones put the messy part inside and leave the outside simple.

## Domains travel through the pipeline

Set $$g(x) = 2x + 1$$ first and $$f(x) = \sqrt{x}$$ second, and slide the input left. The composite's graph stops abruptly — to the left of $$x = -\tfrac{1}{2}$$, the first machine produces negative outputs, and the second machine cannot accept them. The pipeline readout says so directly: $$g(x)$$ has a value, and $$f(g(x))$$ is undefined.

This is the general rule, and it is worth stating carefully: $$x$$ is in the domain of $$f \circ g$$ exactly when $$x$$ is in the domain of $$g$$ *and* $$g(x)$$ is in the domain of $$f$$. The domain of a composite is inherited from both machines, not read off the final simplified formula. Simplification can hide the restriction; the pipeline cannot.

## Why this skill compounds

Nearly everything built later in precalculus is a composition wearing a disguise. [A transformed graph](/2026/07/25/transformations-four-dials.html) like $$y = \sin(2x - \pi)$$ is a composition; [an exponential model](/2026/07/30/logarithms-undo-exponentials.html) like $$A(t) = 50e^{0.03t}$$ is a composition; inverting a function is running a pipeline backward, machine by machine, last one first. And for those continuing on: calculus differentiates composite functions by exactly the outside-in reading practiced here — the students who struggle there are almost never confused about the new rule, only about seeing which function is inside which. Learn to see the seams now and that course gets noticeably easier.

<div class="article-note" markdown="1">
A self-test at the pipeline: set $$g$$ to $$\sqrt{x}$$ and $$f$$ to $$x^2$$, then press swap and compare the two composites at $$x = -4$$. One returns 4 and the other is undefined, though both simplify to formulas that look harmless, $$x$$ and $$\vert x\vert$$. The order decided which restriction survived, and neither finished formula records it.
</div>
