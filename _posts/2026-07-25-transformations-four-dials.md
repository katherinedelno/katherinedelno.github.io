---
layout: post
title: "The four parameters of transformation"
date: 2026-07-25
description: "Every transformation question involves the same four parameters performing the same four roles, two of them in reverse. An interactive set of dials makes the structure visible."
course: "AP Precalculus"
read_time: "6 min read"
math: true
kind: foundations
sequence: 1
interactive: true
---

Every transformation question in AP Precalculus, and later in calculus, is built from one master form:

$$g(x) = a\,f\big(b(x-h)\big) + k.$$

Four numbers, four jobs. The outside pair $$a$$ and $$k$$ act on outputs, so they move the graph vertically and behave exactly as they read. The inside pair $$b$$ and $$h$$ act on inputs, so they move the graph horizontally and behave opposite to the way they read. That one sentence is the whole topic. The dials below let you verify it.

## Turn the dials

The gray curve is the parent function $$f(x) = \sin x$$. The black curve is $$g(x) = a\sin\big(b(x-h)\big) + k$$ with your dial settings.

<div class="viz" markdown="0">
  <canvas id="tf-cv" width="700" height="280"></canvas>
  <div class="viz-controls">
    <label for="tf-a">a</label><input type="range" id="tf-a" min="-30" max="30" step="1" value="10" style="min-width:90px">
    <label for="tf-b">b</label><input type="range" id="tf-b" min="2" max="40" step="1" value="10" style="min-width:90px">
    <label for="tf-h">h</label><input type="range" id="tf-h" min="-30" max="30" step="1" value="0" style="min-width:90px">
    <label for="tf-k">k</label><input type="range" id="tf-k" min="-15" max="15" step="1" value="0" style="min-width:90px">
  </div>
  <div class="viz-controls"><span class="viz-value" id="tf-read" style="min-width:100%"></span></div>
  <p class="viz-caption">Experiments worth running. Push a above 1 and watch the graph stretch tall without moving sideways; make a negative and it flips upside down. Push k and the whole graph rides up and down, midline included. Now the backward pair: increase b and the wave compresses horizontally, because a faster input completes its cycle sooner, so bigger b means a shorter period. Slide h positive and the graph moves right, even though the formula shows a minus sign. The inside always works in reverse.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('tf-cv'), c = cv.getContext('2d');
  var sa = document.getElementById('tf-a'), sb = document.getElementById('tf-b');
  var sh = document.getElementById('tf-h'), sk = document.getElementById('tf-k');
  var read = document.getElementById('tf-read');
  var W = cv.width, H = cv.height, pad = 24;
  var X0 = -7, X1 = 7, Y0 = -5, Y1 = 5;
  function px(x){ return pad + (x - X0)/(X1 - X0)*(W - 2*pad); }
  function py(y){ return H - pad - (y - Y0)/(Y1 - Y0)*(H - 2*pad); }
  function plot(fn, color, wdt){
    c.strokeStyle = color; c.lineWidth = wdt; c.beginPath();
    var started = false;
    for(var i = 0; i <= 500; i++){
      var x = X0 + (X1 - X0)*i/500, y = fn(x);
      if(y < Y0 - 2 || y > Y1 + 2){ started = false; continue; }
      started ? c.lineTo(px(x), py(y)) : c.moveTo(px(x), py(y));
      started = true;
    }
    c.stroke();
  }
  function fmt(v){ return (Math.round(v*10)/10).toString(); }
  function draw(){
    var a = sa.value/10, b = sb.value/10, h = sh.value/10, k = sk.value/5;
    c.clearRect(0, 0, W, H);
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(px(X0), py(0)); c.lineTo(px(X1), py(0)); c.stroke();
    c.beginPath(); c.moveTo(px(0), py(Y0)); c.lineTo(px(0), py(Y1)); c.stroke();
    // midline y=k
    c.strokeStyle = '#d0d0cd'; c.setLineDash([5,4]);
    c.beginPath(); c.moveTo(px(X0), py(k)); c.lineTo(px(X1), py(k)); c.stroke();
    c.setLineDash([]);
    plot(Math.sin, '#c9c9c6', 2);
    plot(function(x){ return a*Math.sin(b*(x - h)) + k; }, '#1f1f1f', 2.2);
    read.textContent = 'g(x) = ' + fmt(a) + ' sin( ' + fmt(b) + ' (x − ' + fmt(h) + ') ) + ' + fmt(k) +
      '    amplitude ' + fmt(Math.abs(a)) + ', period ' + fmt(2*Math.PI/Math.abs(b)) + ', midline y = ' + fmt(k);
  }
  [sa, sb, sh, sk].forEach(function(s){ s.addEventListener('input', draw); });
  draw();
})();
</script>

## Why the inside works backward

The backward behavior of $$b$$ and $$h$$ is the part students distrust, so it deserves an actual reason rather than a mnemonic.

Consider $$g(x) = f(x - 3)$$. Ask: what input must $$g$$ receive to produce the value $$f(0)$$? It needs $$x - 3 = 0$$, so $$x = 3$$. The feature of $$f$$ that used to live at 0 now lives at 3. Every feature migrates the same way, three units right. The minus sign in the formula is not a direction; it is the price of admission. The graph moves right because the input must be larger to compensate for the subtraction.

The same logic runs the compression. In $$g(x) = f(2x)$$, the input $$x = 1$$ already delivers $$f(2)$$: the function experiences inputs twice as fast as you supply them, so everything $$f$$ does gets done in half the horizontal space. Bigger $$b$$, faster consumption, narrower graph. For sinusoids this becomes the period formula, period $$= \tfrac{2\pi}{\vert b\vert}$$, but the formula is just this paragraph compressed.

Outputs have no such reversal because they happen after the function has done its work. Multiply the result by $$a$$, add $$k$$: the graph's heights scale and slide exactly as written.

## The order of operations trap

When several dials are set at once, the order you narrate them matters in one specific place: the horizontal factor and shift must be read from the factored form. Compare

$$g(x) = f(2x - 6) \qquad \text{and} \qquad g(x) = f\big(2(x - 3)\big).$$

These are the same function, but only the second displays the true shift. Read the first one naively and you will report a shift of 6; factoring the 2 out first reveals the actual shift of 3. On multiple-choice questions this is the most reliable distractor in the topic, and the defense is mechanical: before naming any horizontal transformation, factor the inside so it reads $$b(x - h)$$.

A parallel trap lives outside: in $$-f(x) + 2$$, the reflection happens before the upward shift, so the graph flips about the $$x$$-axis and then rises. Reading transformations in the wrong order rarely changes horizontal-only or vertical-only answers, but it scrambles anything mixing a reflection with a shift in the same direction.

## One skill, three courses

This topic is a rare investment that pays in every course that follows. In AP Precalculus, it writes sinusoidal models directly: amplitude is $$\vert a\vert$$, midline is $$y = k$$, period comes from $$b$$, and the phase comes from $$h$$. In AP Calculus, the chain rule differentiates $$f\big(b(x-h)\big)$$ and the same four numbers reappear in every substitution. In AP Statistics, standardizing a score, $$z = \tfrac{x - \mu}{\sigma}$$, is precisely a shift by $$h = \mu$$ and a horizontal scale by $$\sigma$$, which is why the normal table only needs one curve. Four dials, learned once.

<div class="article-note" markdown="1">
A self-test at the dials: set the sliders to make the black curve have amplitude 2, period π, midline y = 1, and a peak on the y-axis. There are two honest solutions, one using a sine with a shift and one that would use a cosine with none, which is a good reminder that models are not unique. If your sine version needs h = π/4, you have understood the quarter-lap relationship between the two functions.
</div>
