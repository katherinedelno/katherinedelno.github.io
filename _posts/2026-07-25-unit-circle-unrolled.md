---
layout: post
title: "The unit circle and the sine curve"
date: 2026-07-25
description: "The sine curve records the circle's height as the angle turns, and every feature of the wave can be read directly from the circle. An animation traces the correspondence."
course: "AP Precalculus"
read_time: "6 min read"
math: true
kind: foundations
sequence: 6
interactive: true
blurb: "Turn the angle and watch the circle's height become the sine curve"
featured: true
---

Students usually meet the unit circle and the sine graph as two separate things to memorize: a circle full of special angles, and a wavy graph with [amplitude and period](/2026/07/25/transformations-four-dials.html). They are not two things. The sine graph is what the circle writes down when you track one number, the height of a point traveling around it, while the angle grows. Once you watch the unrolling happen, the graph's features stop being facts and start being consequences.

## Watch the circle write the wave

On the left, a point sits on the unit circle at angle $$\theta$$, measured counterclockwise from the positive $$x$$-axis. Its height is $$\sin\theta$$. On the right, that height is being recorded as the angle grows. Drag the slider.

<div class="viz" markdown="0">
  <canvas id="uc-cv" width="700" height="260"></canvas>
  <div class="viz-controls">
    <label for="uc-th">Angle θ</label>
    <input type="range" id="uc-th" min="0" max="1000" step="1" value="130">
    <span class="viz-value" id="uc-read"></span>
  </div>
  <p class="viz-caption">The horizontal dashed line is the live connection: the height of the point on the circle is the height of the graph at that angle. Watch the wave's landmarks appear as circle events. The peak at θ = π/2 is the point reaching the top of the circle. The zero at θ = π is the point crossing the left side, at height 0. The trough at 3π/2 is the bottom of the circle. And the wave repeats after 2π because the point is back where it started. Period is not a formula; it is one full lap.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('uc-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('uc-th'), read = document.getElementById('uc-read');
  var W = cv.width, H = cv.height;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var CX = 110, CY = 130, R = 85;
  var GX0 = 250, GX1 = 680, GY = 130, GR = 85;
  var TMAX = 2*Math.PI;
  function gx(t){ return GX0 + (t/TMAX)*(GX1 - GX0); }
  function gy(v){ return GY - v*GR; }
  function draw(){
    var th = (slider.value/1000)*TMAX;
    c.clearRect(0, 0, W, H);
    // circle + axes
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(CX - R - 12, CY); c.lineTo(CX + R + 12, CY); c.stroke();
    c.beginPath(); c.moveTo(CX, CY - R - 12); c.lineTo(CX, CY + R + 12); c.stroke();
    c.beginPath(); c.moveTo(GX0, GY); c.lineTo(GX1, GY); c.stroke();
    // pi ticks on the graph axis
    c.fillStyle = '#8a8a8a'; c.font = '12px Hanken Grotesk, sans-serif';
    var labels = ['π/2', 'π', '3π/2', '2π'];
    for(var q = 1; q <= 4; q++){
      var tx = gx(q*Math.PI/2);
      c.beginPath(); c.moveTo(tx, GY - 4); c.lineTo(tx, GY + 4);
      c.strokeStyle = '#c0c0bc'; c.stroke();
      c.fillText(labels[q-1], tx - 9, GY + 18);
    }
    c.strokeStyle = '#b9b9b6'; c.lineWidth = 2;
    c.beginPath(); c.arc(CX, CY, R, 0, 2*Math.PI); c.stroke();
    // swept arc
    c.strokeStyle = '#1f1f1f'; c.lineWidth = 2.5;
    c.beginPath(); c.arc(CX, CY, R, 0, -th, true); c.stroke();
    // radius + point
    var pxc = CX + R*Math.cos(th), pyc = CY - R*Math.sin(th);
    c.strokeStyle = '#6b6b6b'; c.lineWidth = 1.5;
    c.beginPath(); c.moveTo(CX, CY); c.lineTo(pxc, pyc); c.stroke();
    // height segment
    c.strokeStyle = '#1f1f1f'; c.lineWidth = 2;
    c.beginPath(); c.moveTo(pxc, CY); c.lineTo(pxc, pyc); c.stroke();
    // sine curve traced so far
    c.strokeStyle = '#1f1f1f'; c.lineWidth = 2; c.beginPath();
    var steps = Math.max(2, Math.floor(300*th/TMAX));
    for(var i = 0; i <= steps; i++){
      var t = th*i/steps, Y = gy(Math.sin(t));
      i ? c.lineTo(gx(t), Y) : c.moveTo(gx(t), Y);
    }
    c.stroke();
    // ghost of the full curve
    c.strokeStyle = '#e2e2df'; c.lineWidth = 1.5; c.beginPath();
    for(var j = 0; j <= 300; j++){
      var t2 = TMAX*j/300, Y2 = gy(Math.sin(t2));
      j ? c.lineTo(gx(t2), Y2) : c.moveTo(gx(t2), Y2);
    }
    c.stroke();
    // connecting dashed line
    c.strokeStyle = '#8a8a8a'; c.setLineDash([4,4]); c.lineWidth = 1;
    c.beginPath(); c.moveTo(pxc, pyc); c.lineTo(gx(th), gy(Math.sin(th))); c.stroke();
    c.setLineDash([]);
    // dots
    c.fillStyle = '#1f1f1f';
    c.beginPath(); c.arc(pxc, pyc, 4.5, 0, 7); c.fill();
    c.beginPath(); c.arc(gx(th), gy(Math.sin(th)), 4.5, 0, 7); c.fill();
    read.textContent = 'sin(' + th.toFixed(2) + ') = ' + Math.sin(th).toFixed(3);
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

## Reading the wave's features off the circle

Every property of $$y = \sin\theta$$ that the course asks about is a circle fact in disguise.

**Amplitude 1.** The point lives on a circle of radius 1, so its height is trapped between $$-1$$ and $$1$$. The wave can never leave that band, and the maximum height 1 is reached exactly when the point is at the top of the circle.

**Period $$2\pi$$.** One full lap returns the point to its starting position, so the height record must repeat. The period of sine is the circumference of the trip in angle terms, nothing more. When a function is written $$\sin(b\theta)$$, the point travels $$b$$ times as fast, laps in $$\tfrac{2\pi}{b}$$, and the period shrinks accordingly.

**The zeros at $$0, \pi, 2\pi$$.** These are the two moments per lap when the point crosses the horizontal axis, where its height is zero. Between consecutive zeros the point is entirely above or entirely below the axis, which is why the wave alternates arches and troughs.

**Symmetry.** Walking the circle backward, $$\sin(-\theta) = -\sin\theta$$: an angle swept clockwise puts the point at the mirror-image height. The sine graph's odd symmetry is the circle's up-down mirror.

Cosine is the same story told about the other coordinate. The point's horizontal position, $$\cos\theta$$, starts at 1, hits 0 at the top of the circle, and reaches $$-1$$ at the far left. That is why the cosine wave is the sine wave shifted left by $$\tfrac{\pi}{2}$$: the horizontal coordinate is a quarter-lap ahead of the vertical one, always.

## Why radians are the natural unit here

The unrolling picture also explains why the course insists on radians. A radian measures the angle by the arc length walked along a unit circle, so the horizontal axis of the wave is literally the distance the point has traveled. Angle in, distance out, same number: the input axis and the circle's edge are the same ruler. In degrees, one lap is 360 of something arbitrary; in radians, one lap is $$2\pi$$ because the unit circle's circumference is $$2\pi$$. Every clean fact about sinusoids, from the period $$2\pi$$ to the calculus that waits in AP Calculus, depends on that ruler agreeing with itself.

## Where the exam takes this

AP Precalculus builds sinusoidal models: Ferris wheels, tides, daylight hours. Every one of those problems is the animation above with the circle resized and relocated. A wheel of radius 20 meters centered 22 meters up is the unit circle stretched by 20 and shifted by 22, which is exactly how the model $$h(t) = -20\cos\left(\tfrac{\pi t}{30}\right) + 22$$ earns each of its numbers: amplitude from the radius, midline from the center height, period from the rotation time, and the leading sign from where the ride starts. Students who can narrate that correspondence write these models in a minute. Students who memorized $$a$$, $$b$$, $$h$$, $$k$$ as slots tend to fill the slots with the wrong circle facts.

<div class="article-note" markdown="1">
A self-test with the slider: before dragging, predict the two angles in one lap where $$\sin\theta = \tfrac12$$, then drag and check where the dashed line sits at height one half. The answers, $$\tfrac{\pi}{6}$$ and $$\tfrac{5\pi}{6}$$, are mirror images across the top of the circle, and seeing that symmetry once is worth a page of reference-angle drills.
</div>
