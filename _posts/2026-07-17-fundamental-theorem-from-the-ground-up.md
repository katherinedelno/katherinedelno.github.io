---
layout: post
title: "The Fundamental Theorem of Calculus from first principles"
date: 2026-07-17
description: "Build an accumulation function from area, then differentiate it. The result is the original integrand."
course: "AP Calculus AB"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "10 min read"
math: true
kind: foundations
sequence: 22
interactive: true
blurb: "Build an accumulation function from area, then differentiate it. The result is the original integrand"
featured: true
image: "/assets/og/fundamental-theorem-from-the-ground-up.png"
---

Students often meet the Fundamental Theorem of Calculus as an evaluation rule:

$$\int_a^b f(x)\,dx = F(b)-F(a),$$

where $$F'=f$$.

That rule is important, but it is not the most revealing way to understand the theorem.

The deeper statement is that accumulation and differentiation are inverse operations.

## Build a function out of area

Let $$f$$ be continuous and define

$$A(x) = \int_0^x f(t)\,dt.$$

The variable $$t$$ belongs inside the integral because $$x$$ is already serving as the upper limit.

The function $$A$$ takes an input $$x$$ and returns the signed accumulation from 0 to $$x$$.

If $$f$$ is positive, $$A$$ increases.

If $$f$$ is negative, $$A$$ decreases.

And

$$A(0)=0.$$

## Watch the accumulation

<div class="viz" markdown="0">
  <canvas id="ftc-top" width="700" height="230"></canvas>
  <canvas id="ftc-bot" width="700" height="230" style="margin-top:10px"></canvas>
  <div class="viz-controls">
    <label for="ftc-x">Sweep&nbsp;x</label>
    <input type="range" id="ftc-x" min="0" max="1000" value="430">
    <span class="viz-value" id="ftc-read"></span>
  </div>
  <p class="viz-caption"><strong>Top:</strong> the rate function <em>f</em>, with the region from 0 to <em>x</em> shaded: dark where it counts positively, light where it counts negatively. <strong>Bottom:</strong> the accumulation function <em>A</em>(<em>x</em>), traced as far as the sweep has gone, with its tangent line drawn at the leading point. Watch three things. <em>A</em> rises while <em>f</em> is above the axis and falls while <em>f</em> is below. <em>A</em> peaks at the exact moment <em>f</em> crosses zero. And the slope of the tangent always matches the height of <em>f</em> in the top panel. That last observation is the Fundamental Theorem.</p>
</div>

<script>
(function(){
  var f = function(t){ return 2*Math.sin(t) + 0.6; };
  var A = function(x){ return 2*(1 - Math.cos(x)) + 0.6*x; };   // exact: ∫0..x f
  var X0 = 0, X1 = 2*Math.PI;
  var top = document.getElementById('ftc-top'), bot = document.getElementById('ftc-bot');
  var slider = document.getElementById('ftc-x'), read = document.getElementById('ftc-read');
  var INK = '#1f1f1f', MUTED = '#8a8a8a', LINE = '#e0e0e0', POS = '#c9c9c9', NEG = '#efefef';

  // Resize the backing store exactly once per canvas. Doing this inside draw()
  // re-reads a width that was already scaled and multiplies it again, so the
  // canvas doubles on every slider event.
  function prepare(cv){
    var c = cv.getContext('2d'), W = cv.width, H = cv.height;
    var d__ = Math.min(window.devicePixelRatio || 1, 2);
    cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
    return { c:c, W:W, H:H };
  }
  var CT = prepare(top), CB = prepare(bot);

  function setup(base, lo, hi){
    var W = base.W, H = base.H, pad = 34;
    return {
      c:base.c, W:W, H:H, pad:pad, lo:lo, hi:hi,
      px:function(x){ return pad + (x - X0)/(X1 - X0)*(W - 2*pad); },
      py:function(y){ return H - pad - (y - lo)/(hi - lo)*(H - 2*pad); }
    };
  }
  function axes(g, label){
    var c = g.c;
    c.clearRect(0,0,g.W,g.H);
    c.strokeStyle = LINE; c.lineWidth = 1;
    c.beginPath(); c.moveTo(g.px(X0), g.py(0)); c.lineTo(g.px(X1), g.py(0)); c.stroke();
    c.beginPath(); c.moveTo(g.px(X0), g.py(g.lo)); c.lineTo(g.px(X0), g.py(g.hi)); c.stroke();
    c.fillStyle = MUTED; c.font = '700 12px Hanken Grotesk, sans-serif';
    c.fillText(label, g.px(X0) + 6, g.py(g.hi) + 14);
  }
  function draw(){
    var x = X0 + (slider.value/1000)*(X1 - X0);
    var gT = setup(CT, -1.9, 3.1), gB = setup(CB, -0.6, 8.2);

    axes(gT, 'f  (the rate)');
    // shaded region 0..x
    var c = gT.c, n = 300, i, t;
    for(i = 0; i < n; i++){
      var t0 = X0 + (x - X0)*i/n, t1 = X0 + (x - X0)*(i+1)/n, ym = f((t0+t1)/2);
      c.fillStyle = ym >= 0 ? POS : NEG;
      c.fillRect(gT.px(t0), Math.min(gT.py(0), gT.py(ym)), gT.px(t1)-gT.px(t0)+0.6, Math.abs(gT.py(ym)-gT.py(0)));
    }
    // curve
    c.strokeStyle = INK; c.lineWidth = 2; c.beginPath();
    for(i = 0; i <= 320; i++){ t = X0 + (X1-X0)*i/320; var Y = gT.py(f(t)); i ? c.lineTo(gT.px(t), Y) : c.moveTo(gT.px(t), Y); }
    c.stroke();
    // marker at x
    c.strokeStyle = MUTED; c.setLineDash([4,4]); c.beginPath();
    c.moveTo(gT.px(x), gT.py(gT.lo)); c.lineTo(gT.px(x), gT.py(gT.hi)); c.stroke(); c.setLineDash([]);
    c.fillStyle = INK; c.beginPath(); c.arc(gT.px(x), gT.py(f(x)), 4, 0, 7); c.fill();

    axes(gB, 'A  (area so far)');
    c = gB.c;
    // traced A curve up to x
    c.strokeStyle = INK; c.lineWidth = 2; c.beginPath();
    var steps = Math.max(2, Math.floor(320*(x - X0)/(X1 - X0)));
    for(i = 0; i <= steps; i++){ t = X0 + (x - X0)*i/steps; var Y2 = gB.py(A(t)); i ? c.lineTo(gB.px(t), Y2) : c.moveTo(gB.px(t), Y2); }
    c.stroke();
    // ghost of the full curve
    c.strokeStyle = LINE; c.lineWidth = 1.5; c.beginPath();
    for(i = 0; i <= 320; i++){ t = X0 + (X1-X0)*i/320; var Y3 = gB.py(A(t)); i ? c.lineTo(gB.px(t), Y3) : c.moveTo(gB.px(t), Y3); }
    c.stroke();
    // tangent segment at leading point, slope = f(x)
    var m = f(x), dx = 0.55;
    c.strokeStyle = '#6b6b6b'; c.lineWidth = 2; c.beginPath();
    c.moveTo(gB.px(x - dx), gB.py(A(x) - m*dx));
    c.lineTo(gB.px(x + dx), gB.py(A(x) + m*dx)); c.stroke();
    c.fillStyle = INK; c.beginPath(); c.arc(gB.px(x), gB.py(A(x)), 4.5, 0, 7); c.fill();

    read.textContent = 'slope of A = ' + m.toFixed(2) + ' = height of f';
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

The upper graph shows $$f$$.

The lower graph shows $$A$$.

As $$x$$ moves to the right, the shaded region in the upper panel records the signed area accumulated so far.

At the same time, the lower graph traces the value of $$A(x)$$.

Three things are worth watching.

When $$f$$ is above the axis, $$A$$ rises.

When $$f$$ is below the axis, $$A$$ falls.

And the slope of $$A$$ at each point matches the height of $$f$$ there.

That last observation is the first part of the Fundamental Theorem.

## Why $$A'(x)=f(x)$$

Consider a small increase from $$x$$ to $$x+h$$.

The change in accumulated area is

$$A(x+h)-A(x).$$

For small $$h$$, this additional region is [close to a rectangle](/2026/07/25/riemann-sums-watching-rectangles.html) with width $$h$$ and height $$f(x)$$.

So

$$A(x+h)-A(x) \approx f(x)h.$$

Divide by $$h$$:

$$\frac{A(x+h)-A(x)}{h} \approx f(x).$$

As $$h\to0$$, continuity makes the approximation exact.

Therefore

$$A'(x) = f(x).$$

The rate at which signed area accumulates is the value of the function being accumulated.

That is the central connection between integration and differentiation.

## The evaluation rule follows

Now suppose $$F$$ is any antiderivative of $$f$$.

Then $$A$$ and $$F$$ have the same derivative:

$$A'=F'=f.$$

So they differ by a constant.

Write

$$F(x)=A(x)+C.$$

Then

$$F(b)-F(a) = A(b)-A(a).$$

But

$$A(b)-A(a) = \int_a^b f(t)\,dt.$$

Therefore

$$\int_a^b f(x)\,dx = F(b)-F(a).$$

The familiar evaluation rule follows from the accumulation-function statement.

The constant disappears because subtraction removes it.

## Three common forms

### An accumulation function

Suppose

$$g(x) = \int_2^x f(t)\,dt.$$

Then

$$g'(x)=f(x).$$

And, where $$f$$ is differentiable,

$$g''(x)=f'(x).$$

Values of $$g$$ come from signed area.

Derivatives of $$g$$ come from the graph of $$f$$.

### A variable upper limit

If the upper limit is itself a function of $$x$$, use the chain rule.

For example,

$$\frac{d}{dx} \int_0^{x^2}\cos(t)\,dt = \cos(x^2)\cdot2x.$$

The Fundamental Theorem evaluates the integrand at the upper limit. The chain rule contributes the derivative of that upper limit.

### Net change

If $$f'$$ is a rate of change, then

$$f(b) = f(a) + \int_a^b f'(t)\,dt.$$

This is the net change form.

A starting amount plus accumulated rate gives the final amount.

If a tank begins with 30 gallons and water enters at rate $$R(t)$$, then after 6 units of time the amount is

$$30+\int_0^6R(t)\,dt.$$

No antiderivative formula is required if the integral is evaluated numerically.

## A useful self-test

<div class="article-note" markdown="1">
Sketch any continuous function $$f$$.

Then sketch

$$A(x) = \int_0^x f(t)\,dt$$

without finding an antiderivative.

Use only the graph of $$f$$.

Where $$f$$ is positive, $$A$$ should rise.

Where $$f$$ is negative, $$A$$ should fall.

Where $$f=0$$, $$A$$ may have an extremum.

Where $$f$$ is increasing, $$A$$ should be concave up.

If you can build that second graph from the first, the theorem is doing more than supplying an integration shortcut.
</div>
