---
layout: post
title: "The four parameters of transformation"
date: 2026-07-25
description: "In g(x) = a f(b(x - h)) + k, the outside parameters act on outputs and the inside parameters act on inputs. That distinction explains the direction and scale of each transformation."
course: "AP Precalculus"
read_time: "5 min read"
math: true
kind: foundations
sequence: 3
interactive: true
blurb: "In g(x) = a f(b(x - h)) + k, the outside parameters act on outputs and the inside parameters act on inputs. That distinction explains the direction and scale of each transformation"
image: "/assets/og/transformations-four-dials.png"
---

A large class of graph transformations can be written as

$$g(x)=a\,f\big(b(x-h)\big)+k$$

Each parameter has a different role. The outside parameters $$a$$ and $$k$$ act on outputs. The inside parameters $$b$$ and $$h$$ act on inputs. That distinction explains why horizontal transformations often appear to work in the opposite direction from the signs in the formula.

## Turn the four parameters

The parent function is $$f(x)=\sin x$$, and the transformed function is $$g(x)=a\sin\big(b(x-h)\big)+k$$.

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
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
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

Changing $$a$$ scales the output values. If $$\vert a\vert>1$$, the graph stretches vertically, and if $$0<\vert a\vert<1$$, it compresses vertically. If $$a<0$$, the graph is also reflected across the $$x$$-axis. Changing $$k$$ shifts every output vertically by the same amount, and those two parameters behave directly because they act after the parent function has produced an output.

## Why horizontal shifts look backward

Consider $$g(x)=f(x-3)$$. A feature of $$f$$ that occurred at input 0 now occurs where $$x-3=0$$, which means $$x=3$$, so the graph shifts right by 3. The minus sign does not mean “move left.” It tells us what new input is required to make the inside of the function equal the old input.

The same reasoning explains horizontal scaling. For $$g(x)=f(2x)$$, the input $$x=1$$ sends the parent function the value 2, so the parent function experiences its inputs twice as quickly. Its horizontal features therefore occur in half the original distance. For sine, $$\text{period}=\tfrac{2\pi}{\vert b\vert}$$, and a larger $$\vert b\vert$$ produces a shorter period.

## Factor the inside before reading a shift

Compare $$f(2x-6)$$ with $$f\big(2(x-3)\big)$$. These are the same expression, and the second form makes the shift visible. The horizontal shift is 3, not 6. So before reading $$h$$, factor the inside into the form $$b(x-h)$$, which avoids one of the most common transformation errors.

## Order outside the function

The outside operations also have an order. In $$-f(x)+2$$, the output of $$f$$ is first multiplied by $$-1$$, then 2 is added, so the graph is reflected across the $$x$$-axis and then shifted upward. When several transformations are combined, it is often cleaner to reason from the algebra than to memorize a verbal sequence.

## Sinusoidal models

For $$y=a\sin\big(b(x-h)\big)+k$$, the parameters have immediate [modeling interpretations](/2026/07/25/unit-circle-unrolled.html). Here $$\vert a\vert$$ is the amplitude, $$k$$ is the midline, the period is $$\tfrac{2\pi}{\vert b\vert}$$, and the value $$h$$ determines the horizontal shift. Those quantities often come directly from a physical setting such as a Ferris wheel, seasonal temperature, or daylight hours, and the model should be built from the situation rather than by filling four remembered slots.

<div class="article-note" markdown="1">
A useful test is to ask where a known feature of the parent graph should move. That usually determines the sign of the horizontal shift more reliably than memory.
</div>
