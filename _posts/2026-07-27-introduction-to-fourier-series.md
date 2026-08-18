---
layout: post
title: "An introduction to Fourier series"
date: 2026-07-27
description: "A periodic function can be represented by a sum of sine and cosine waves. Adding harmonics shows how increasingly complex shapes can be built from simple frequencies."
course: "All courses"
courses: [AP Calculus BC, AP Precalculus]
section: beyond
read_time: "7 min read"
math: true
kind: beyond
sequence: 5
interactive: true
blurb: "A periodic function can be represented by a sum of sine and cosine waves. Adding harmonics shows how increasingly complex shapes can be built from simple frequencies"
image: "/assets/og/introduction-to-fourier-series.png"
---

[Sine and cosine functions](/2026/07/25/unit-circle-unrolled.html) are simple. By adding enough of them at different frequencies and amplitudes, we can represent much more complicated periodic functions, and a Fourier series writes a periodic function as a sum of these harmonic components.

## Building a square wave

A standard example is the square wave, and one representation is

$$f(x) = \frac4\pi \left( \sin x + \frac{\sin3x}{3} + \frac{\sin5x}{5} + \frac{\sin7x}{7} +\cdots \right)$$

Only odd harmonics appear, and their amplitudes decrease as the reciprocal of the frequency.

<div class="viz" markdown="0">
  <canvas id="fs-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="fs-n">Harmonics</label>
    <input type="range" id="fs-n" min="1" max="40" step="1" value="1">
    <span class="viz-value" id="fs-read"></span>
  </div>
  <p class="viz-caption">The faint square wave is the target; the dark curve is the sum of the first several harmonics. One sine wave is a poor imitation. Three begin to square the shoulders; ten are recognizably the signal; forty are nearly indistinguishable from it. Two details reward a closer look. Every added harmonic is smooth, yet the sum marches toward a shape with jumps, which is the fact that so unsettled Fourier's contemporaries. And the small horns that persist beside each jump never entirely flatten, however many terms are added: this is the Gibbs phenomenon, discovered when physicists noticed their measuring device drawing the same stubborn overshoot.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('fs-cv'), c = cv.getContext('2d');
  var sl = document.getElementById('fs-n'), read = document.getElementById('fs-read');
  var W = cv.width, H = cv.height, pad = 16;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var XMIN = -Math.PI*1.5, XMAX = Math.PI*1.5;
  function px(x){ return pad + (x - XMIN)/(XMAX - XMIN)*(W - 2*pad); }
  function py(y){ return H/2 - y*(H/2 - pad)/1.6; }
  function square(x){
    var m = ((x % (2*Math.PI)) + 2*Math.PI) % (2*Math.PI);
    return m < Math.PI ? 1 : -1;
  }
  function draw(){
    var n = parseInt(sl.value, 10);
    c.clearRect(0, 0, W, H);
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(pad, py(0)); c.lineTo(W - pad, py(0)); c.stroke();
    // target square wave
    c.strokeStyle = '#d0d0cd'; c.lineWidth = 1.6;
    c.beginPath();
    for(var x = XMIN; x <= XMAX; x += 0.004){
      var X = px(x), Y = py(square(x));
      x === XMIN ? c.moveTo(X, Y) : c.lineTo(X, Y);
    }
    c.stroke();
    // partial sum
    c.strokeStyle = '#1f1f1f'; c.lineWidth = 2;
    c.beginPath();
    for(x = XMIN; x <= XMAX; x += 0.004){
      var s = 0;
      for(var k = 0; k < n; k++){
        var m = 2*k + 1;
        s += Math.sin(m*x)/m;
      }
      s *= 4/Math.PI;
      X = px(x); Y = py(s);
      x === XMIN ? c.moveTo(X, Y) : c.lineTo(X, Y);
    }
    c.stroke();
    read.textContent = n + (n === 1 ? ' harmonic' : ' harmonics') + '  (frequencies 1, 3, 5, … up to ' + (2*n - 1) + ')';
  }
  sl.addEventListener('input', draw);
  draw();
})();
</script>

The faint graph shows the target square wave, and the dark graph shows the partial Fourier sum. With one term, the approximation is simply a sine wave. As more harmonics are added, the flat regions become flatter and the transitions become sharper, and the approximation is being built globally from smooth waves.

## Where the coefficients come from

The coefficients are determined by integrals. For a function with period $$2\pi$$, a Fourier series has the form

$$\frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n\cos nx+b_n\sin nx \right)$$

The coefficients are

$$a_n = \frac1\pi \int_{-\pi}^{\pi} f(x)\cos(nx)\,dx \qquad\text{and}\qquad b_n = \frac1\pi \int_{-\pi}^{\pi} f(x)\sin(nx)\,dx$$

These formulas work because the sine and cosine functions are orthogonal over a full period. Informally, the integral measures how much of a particular frequency is present in the function.

## The Gibbs phenomenon

Look near a jump in the square wave. Even after many harmonics are added, the Fourier approximation overshoots near the discontinuity. The oscillation becomes narrower as more terms are used, but the maximum overshoot does not disappear completely, and this is the Gibbs phenomenon.

It is a useful reminder that convergence can behave differently near discontinuities. A series can approximate a function extremely well across most of an interval while retaining a structured error near a jump.

## Frequency instead of position

Fourier analysis gives two ways to describe the same signal. The original function shows how the signal changes over time or position, and the Fourier coefficients show how much of each frequency is present. This second representation is often called the frequency domain.

For a musical note, the fundamental frequency determines the perceived pitch, and higher harmonics contribute to timbre. Two instruments can play the same note while producing very different mixtures of harmonics, and the waveform looks different because the frequency content is different.

## Applications

The same decomposition appears in audio processing, image compression, telecommunications, signal denoising, and the analysis of differential equations. Noise can sometimes be removed by suppressing unwanted frequency components, and compression can preserve the most important components while discarding smaller ones. Differential equations involving oscillation often become easier when expressed in a basis of sine and cosine functions, and the computational version of this idea is the Fourier transform.

## Fourier series and Taylor series

Fourier series and [Taylor series](/2026/07/22/taylor-polynomials-impersonate-functions.html) both approximate functions using simpler building blocks, but the constructions are different. A Taylor polynomial is organized around one center and matches derivatives there, and its basis functions are powers such as $$1,\; x,\; x^2,\; x^3,\ldots$$ A Fourier series is organized around frequency across an interval, and its basis functions are sine and cosine waves.

Taylor approximation is naturally local, while Fourier representation is naturally global and periodic. Both become much more systematic in later analysis courses, where the choice of basis is treated as a general mathematical idea.

## A useful way to see the square wave

<div class="article-note" markdown="1">
Move the harmonic slider slowly. Each new term has a higher frequency and a smaller amplitude, so the low-frequency terms determine the broad shape and the high-frequency terms refine the sharp transitions. That same separation between broad structure and fine detail is central to signal processing, and a complicated signal can often be understood by asking which scales or frequencies carry most of its energy.
</div>
