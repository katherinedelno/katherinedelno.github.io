---
layout: post
title: "The Fundamental Theorem of Calculus, from the ground up"
date: 2026-07-17
description: "Why does an area function have a derivative, and why is that derivative the curve you started with? A guided tour of the accumulation function, with an interactive picture of the theorem at work."
course: "AP Calculus AB"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "9 min read"
math: true
---

The Fundamental Theorem of Calculus is the most important sentence in the course, and it is routinely memorized without ever being *seen*. Students learn to compute $$\int_1^4 x^2\,dx$$ by antidifferentiating and subtracting, which works, but hides the remarkable thing the theorem actually says: **accumulating a quantity and differentiating are inverse operations.** Area, of all things, undoes the derivative.

This piece builds the theorem the way I build it with students: start with a machine that measures area, discover that the machine has a derivative, and then notice — with some astonishment — whose derivative it is.

## A function that measures area

Take any continuous function $$f$$. Don't antidifferentiate it; just *watch* it. Define a new function by asking, at each input $$x$$, "how much area has the graph of $$f$$ swept out so far?"

$$A(x) = \int_0^x f(t)\,dt.$$

Two notational points that matter on the exam. First, the variable inside is $$t$$, not $$x$$ — $$x$$ is busy being the upper limit, and using it twice in two roles is exactly the kind of ambiguity graders penalize. Second, $$A$$ is a genuine function: feed it an input, it returns a number. $$A(2)$$ is the signed area from $$0$$ to $$2$$. $$A(0)$$ is $$0$$, because no ground has been covered yet.

"Signed" is doing real work in that sentence. Where $$f$$ is negative, the region between the graph and the axis counts *against* the total. The accumulation function goes down when the curve is below the axis. Hold that thought — it is about to become the whole theorem.

## Watching the accumulation happen

The picture below shows a function $$f$$ (top) and its accumulation function $$A$$ (bottom) being drawn in real time as $$x$$ sweeps to the right. Drag the slider and watch both panels at once.

<div class="viz" markdown="0">
  <canvas id="ftc-top" width="700" height="230"></canvas>
  <canvas id="ftc-bot" width="700" height="230" style="margin-top:10px"></canvas>
  <div class="viz-controls">
    <label for="ftc-x">Sweep&nbsp;x</label>
    <input type="range" id="ftc-x" min="0" max="1000" value="430">
    <span class="viz-value" id="ftc-read"></span>
  </div>
  <p class="viz-caption"><strong>Top:</strong> the rate function <em>f</em>, with the region from 0 to <em>x</em> shaded — dark where it counts positively, light where it counts negatively. <strong>Bottom:</strong> the accumulation function <em>A</em>(<em>x</em>), traced as far as the sweep has gone, with its tangent line drawn at the leading point. Watch three things: <em>A</em> rises while <em>f</em> is above the axis and falls while <em>f</em> is below; <em>A</em> peaks at the exact moment <em>f</em> crosses zero; and the slope of the tangent always matches the height of <em>f</em> in the top panel. That last observation <em>is</em> the Fundamental Theorem.</p>
</div>

<script>
(function(){
  var f = function(t){ return 2*Math.sin(t) + 0.6; };
  var A = function(x){ return 2*(1 - Math.cos(x)) + 0.6*x; };   // exact: ∫0..x f
  var X0 = 0, X1 = 2*Math.PI;
  var top = document.getElementById('ftc-top'), bot = document.getElementById('ftc-bot');
  var slider = document.getElementById('ftc-x'), read = document.getElementById('ftc-read');
  var INK = '#1f1f1f', MUTED = '#8a8a8a', LINE = '#e0e0e0', POS = '#c9c9c9', NEG = '#efefef';

  function setup(cv, lo, hi){
    var c = cv.getContext('2d'), W = cv.width, H = cv.height, pad = 34;
    return {
      c:c, W:W, H:H, pad:pad, lo:lo, hi:hi,
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
    var gT = setup(top, -1.9, 3.1), gB = setup(bot, -0.6, 8.2);

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

## Why the slope of A is the height of f

Here is the argument, and it fits in a paragraph. Ask how fast $$A$$ is growing at some moment $$x$$. Push the sweep line a tiny step $$h$$ further. The new area picked up, $$A(x+h) - A(x)$$, is a sliver — nearly a rectangle with width $$h$$ and height $$f(x)$$, because over a tiny interval a continuous function barely moves. So

$$\frac{A(x+h) - A(x)}{h} \approx \frac{f(x)\cdot h}{h} = f(x),$$

and the approximation sharpens to equality as $$h \to 0$$ (that is what continuity of $$f$$ buys, via the Squeeze Theorem, since the sliver's height is trapped between the min and max of $$f$$ on the tiny interval). But the left side is the definition of the derivative. Conclusion:

$$A'(x) = f(x).$$

That is the **first part of the Fundamental Theorem**: every continuous function has an antiderivative, namely its own accumulation function. The rate at which area accumulates under a curve *is the height of the curve*. Once you see it in the animation — tall curve, steep accumulation; curve below the axis, falling accumulation — it stops being a formula and becomes something closer to obvious.

## The evaluation shortcut is a corollary

The version everyone uses,

$$\int_a^b f(x)\,dx = F(b) - F(a) \quad\text{where } F' = f,$$

falls out almost immediately. The accumulation function $$A$$ is *an* antiderivative of $$f$$; your $$F$$ is another. Two antiderivatives of the same function differ by a constant (a Mean Value Theorem fact — a function with zero derivative is constant), so $$F = A + C$$. Then

$$F(b) - F(a) = \big(A(b) + C\big) - \big(A(a) + C\big) = A(b) - A(a) = \int_a^b f(t)\,dt,$$

since $$A(a)$$ subtracts off the area before $$a$$. The constant cancels — which is also why the $$+C$$ never matters in a definite integral. The everyday computation is a corollary of the deeper statement, not the theorem itself.

## What this looks like on the exam

The FTC appears on the free-response section in three reliable costumes.

**Costume 1: the defined accumulation function.** You're given a graph of $$f$$ and the definition $$g(x) = \int_2^x f(t)\,dt$$, then asked for $$g(0)$$, $$g'(3)$$, $$g''(3)$$. Translate once and everything follows: $$g' = f$$ and $$g'' = f'$$. So $$g'(3)$$ is the *height* of the given graph at 3, and $$g''(3)$$ is its *slope* there. For $$g(0) = \int_2^0 f(t)\,dt = -\int_0^2 f(t)\,dt$$, reverse the limits and read the geometric area off the graph, minding signs. Every question about $$g$$ is a question about the picture of $$f$$.

**Costume 2: the chain-rule hybrid.** If the upper limit is a function of $$x$$,

$$\frac{d}{dx}\int_0^{x^2} \cos(t)\,dt = \cos\!\left(x^2\right)\cdot 2x,$$

— FTC to peel off the integral, chain rule for the inner function. Substitute into the integrand, multiply by the derivative of the limit.

**Costume 3: net change.** Since a rate's accumulation is total change, $$f(b) = f(a) + \int_a^b f'(t)\,dt$$. This is the workhorse of every in-context FRQ: final amount equals starting amount plus accumulated rate. When a water tank starts at 30 gallons and water flows at rate $$R(t)$$, the amount at time 6 is $$30 + \int_0^6 R(t)\,dt$$ — no antiderivative formula needed, and on a calculator section, none wanted.

## The sentence worth remembering

Differentiation asks: *at this instant, how fast?* Integration asks: *in total, how much?* The Fundamental Theorem says these two questions are inverses of each other — that "how much, so far" is itself a quantity whose "how fast" is the original function. Newton and Leibniz are credited with calculus not because they computed areas (Archimedes did that) or slopes (Fermat did that), but because they saw that the two computations were secretly one.

<div class="article-note" markdown="1">
A good self-test: sketch any $$f$$ you like, then — without computing a single antiderivative — sketch $$A(x) = \int_0^x f$$. Mark where $$A$$ rises, falls, peaks, and bends. If you can do that from the picture alone, you understand the theorem; the algebra is just bookkeeping.
</div>
