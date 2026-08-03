---
layout: post
title: "The Fundamental Theorem of Calculus from first principles"
date: 2026-07-17
description: "An account of why an area function has a derivative, and of why that derivative recovers the original curve, with a dynamic illustration of the theorem at work."
course: "AP Calculus AB"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "10 min read"
math: true
kind: foundations
sequence: 22
interactive: true
blurb: "Why an area function has a derivative, and why it recovers the curve"
featured: true
---

The Fundamental Theorem of Calculus is the most important sentence in the course, and it is routinely memorized without ever being seen. Students learn to compute $$\textstyle \int_1^4 x^2\,dx$$ by antidifferentiating and subtracting, which works, but it hides the remarkable thing the theorem actually says: accumulating a quantity and differentiating are inverse operations. Area, of all things, undoes the derivative.

This piece builds the theorem the way I build it with students. Start with a machine that measures area, discover that the machine has a derivative, and then notice whose derivative it is.

## A function that measures area

Take any continuous function $$f$$. Do not antidifferentiate it; just watch it. Define a new function by asking, at each input $$x$$, how much area the graph of $$f$$ has swept out so far:

$$A(x) = \int_0^x f(t)\,dt.$$

Two notational points matter here, on the exam as much as in theory. First, the variable inside is $$t$$, not $$x$$. The letter $$x$$ is busy serving as the upper limit, and using it in two roles at once is exactly the kind of ambiguity graders penalize. Second, $$A$$ is a genuine function: feed it an input and it returns a number. $$A(2)$$ is the signed area from $$0$$ to $$2$$, and $$A(0) = 0$$, because no ground has been covered yet.

The word "signed" is doing real work in that sentence. Where $$f$$ is negative, the region between the graph and the axis counts against the total, so the accumulation function goes down while the curve is below the axis. Hold that thought, because it is about to become the whole theorem.

## Watching the accumulation happen

The picture below shows a function $$f$$ (top) and its accumulation function $$A$$ (bottom) being traced out as $$x$$ sweeps to the right. Drag the slider and watch both panels at once.

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

## Why the slope of A is the height of f

Here is the argument, and it fits in a paragraph. Ask how fast $$A$$ is growing at some moment $$x$$. Push the sweep line a small step $$h$$ further. The new area picked up, $$A(x+h) - A(x)$$, is a thin sliver, [very nearly a rectangle](/2026/07/25/riemann-sums-watching-rectangles.html) with width $$h$$ and height $$f(x)$$, because a continuous function barely moves over a small interval. So

$$\frac{A(x+h) - A(x)}{h} \approx \frac{f(x)\cdot h}{h} = f(x),$$

and the approximation sharpens to equality as $$h \to 0$$. Continuity of $$f$$ is what pays for that last step, via the Squeeze Theorem, since the sliver's height is trapped between the minimum and maximum of $$f$$ on the small interval. But the left side is the definition of the derivative of $$A$$. The conclusion:

$$A'(x) = f(x).$$

That is the first part of the Fundamental Theorem: every continuous function has an antiderivative, namely its own accumulation function. The rate at which area accumulates under a curve is the height of the curve. Once you see it in the animation, with a tall curve producing a steep accumulation and a below-axis curve producing a falling one, it stops being a formula and becomes something close to obvious.

## The evaluation shortcut is a corollary

The version everyone uses,

$$\int_a^b f(x)\,dx = F(b) - F(a) \quad\text{where } F' = f,$$

follows almost immediately. The accumulation function $$A$$ is an antiderivative of $$f$$, and your $$F$$ is another. Two antiderivatives of the same function differ by a constant, which is a Mean Value Theorem fact: a function with zero derivative is constant. So $$F = A + C$$, and

$$F(b) - F(a) = \big(A(b) + C\big) - \big(A(a) + C\big) = A(b) - A(a) = \int_a^b f(t)\,dt,$$

since $$A(a)$$ subtracts off the area before $$a$$. The constant cancels, which is also why the $$+C$$ never matters in a definite integral. The everyday computation is a corollary of the deeper statement, not the theorem itself.

## What this looks like on the exam

The FTC appears on the free-response section in three reliable costumes.

**The defined accumulation function.** You are given a graph of $$f$$ and the definition $$\textstyle g(x) = \int_2^x f(t)\,dt$$, then asked for $$g(0)$$, $$g'(3)$$, and $$g''(3)$$. Translate once and everything follows: $$g' = f$$ and $$g'' = f'$$. So $$g'(3)$$ is the height of the given graph at 3, and $$g''(3)$$ is its slope there. For $$\textstyle g(0) = \int_2^0 f(t)\,dt = -\int_0^2 f(t)\,dt$$, reverse the limits and read the geometric area off the graph, minding signs. Every question about $$g$$ is a question about the picture of $$f$$.

**The chain-rule hybrid.** If the upper limit is a function of $$x$$, the FTC peels off the integral and the chain rule handles the inner function:

$$\frac{d}{dx}\int_0^{x^2} \cos(t)\,dt = \cos\!\left(x^2\right)\cdot 2x.$$

Substitute into the integrand, then multiply by the derivative of the limit.

**Net change.** Since accumulating a rate gives total change, $$\textstyle f(b) = f(a) + \int_a^b f'(t)\,dt$$. This is the workhorse of every in-context FRQ: final amount equals starting amount plus accumulated rate. When a tank starts with 30 gallons and water flows in at rate $$R(t)$$, the amount at time 6 is $$\textstyle 30 + \int_0^6 R(t)\,dt$$. No antiderivative formula is needed, and on a calculator section, none is wanted.

## The sentence worth remembering

Differentiation asks how fast something is changing at this instant. Integration asks how much has accumulated in total. The Fundamental Theorem says these two questions are inverses of each other: "how much so far" is itself a quantity whose "how fast" is the original function. Newton and Leibniz are credited with calculus not because they computed areas (Archimedes did that) or slopes (Fermat did that), but because they saw that the two computations were secretly one.

<div class="article-note" markdown="1">
A good self-test: sketch any $$f$$ you like, then, without computing a single antiderivative, sketch $$\textstyle A(x) = \int_0^x f$$. Mark where $$A$$ rises, falls, peaks, and bends. If you can do that from the picture alone, you understand the theorem. The algebra is just bookkeeping.
</div>
