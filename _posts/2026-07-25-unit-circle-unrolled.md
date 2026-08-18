---
layout: post
title: "The unit circle and the sine curve"
date: 2026-07-25
description: "The sine graph records the vertical coordinate of a point moving around the unit circle. Its amplitude, period, zeros, and symmetry all follow from that motion."
course: "AP Precalculus"
read_time: "6 min read"
math: true
kind: foundations
sequence: 6
interactive: true
blurb: "The sine graph records the vertical coordinate of a point moving around the unit circle. Its amplitude, period, zeros, and symmetry all follow from that motion"
featured: true
image: "/assets/og/unit-circle-unrolled.png"
---

The unit circle and the sine graph describe the same motion in two different ways. A point moves around the unit circle, and at each angle $$\theta$$, its vertical coordinate is $$\sin\theta$$. If that height is recorded as the angle increases, the result is the sine curve.

## Watch the height become the graph

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

On the circle, the point has coordinates $$(\cos\theta,\sin\theta)$$. On the graph, the horizontal coordinate is $$\theta$$ and the vertical coordinate is the same value $$\sin\theta$$. The dashed line in the visualization connects those two heights.

Several familiar points follow immediately. At $$\theta=0$$, the point is on the positive $$x$$-axis and has height 0, and at $$\theta=\tfrac{\pi}{2}$$, it reaches the top of the circle and the sine value is 1. At $$\theta=\pi$$, it returns to height 0, and at $$\theta=\tfrac{3\pi}{2}$$, it reaches height $$-1$$. After $$2\pi$$, the point completes one full revolution and returns to its starting position, so the sine graph repeats.

## Amplitude and period come from the circle

The unit circle has radius 1, so the vertical coordinate can never exceed 1 or fall below $$-1$$, and that gives sine an amplitude of 1. One full revolution takes an angle of $$2\pi$$, which gives sine its period. For $$\sin(bx)$$, the angle inside the sine function changes $$b$$ times as quickly, so the period becomes $$\tfrac{2\pi}{\vert b\vert}$$. The period formula is a statement about how quickly the point completes one full lap.

## Zeros and symmetry

Sine is zero whenever the point lies on the horizontal axis, and over one full revolution that occurs at $$0,\;\pi,\;2\pi$$. The sign of sine records whether the point lies above or below that axis. Sine also satisfies $$\sin(-\theta)=-\sin\theta$$, since moving clockwise by $$\theta$$ produces the opposite vertical coordinate from moving counterclockwise by the same amount. That is why sine is an odd function.

## Cosine records the other coordinate

Cosine records the horizontal coordinate of the same moving point. At $$\theta=0$$, cosine begins at 1. At $$\tfrac{\pi}{2}$$, it reaches 0, and at $$\pi$$, it reaches $$-1$$. The cosine curve is therefore the same circular motion recorded from the horizontal coordinate instead of the vertical one. Sine and cosine differ by a quarter-cycle shift, as in $$\cos x=\sin\left(x+\tfrac{\pi}{2}\right)$$.

## Why radians fit the geometry

On a unit circle, radian measure equals arc length, so an angle of $$\theta$$ radians cuts off an arc of length $$\theta$$. When the sine graph uses radians on its horizontal axis, the input therefore also measures the distance traveled around the unit circle. One full lap has length $$2\pi$$, which is why the period appears naturally as $$2\pi$$. Radians are not an arbitrary replacement for degrees, and they connect the angle directly to the geometry of the circle.

## From the circle to a sinusoidal model

[A sinusoidal model](/2026/07/25/transformations-four-dials.html) rescales and shifts this same motion. A Ferris wheel with radius 20 meters and center height 22 meters might be modeled with an amplitude of 20 and a midline of 22. The period comes from the time required for one revolution, and the phase shift depends on where the rider begins. The parameters should therefore be read from the physical motion.

<div class="article-note" markdown="1">
A useful self-test is to find the angles in one revolution where $$\sin\theta=\tfrac12$$. On the unit circle, the height $$1/2$$ occurs in Quadrants I and II, so the angles are $$\tfrac{\pi}{6}$$ and $$\tfrac{5\pi}{6}$$. The graph and the circle give the same answer.
</div>
