---
layout: post
title: "An introduction to Fourier series"
date: 2026-07-27
description: "Any repeating signal, however jagged, can be assembled from smooth sine waves. The theorem behind sound, signal processing, and data compression, built one harmonic at a time."
course: "All courses"
courses: [AP Calculus BC, AP Precalculus]
section: beyond
read_time: "7 min read"
math: true
kind: beyond
sequence: 96
interactive: true
---

Here is a claim that sounds impossible. Take the most abrupt periodic signal imaginable: a square wave, which sits at $$+1$$, drops instantly to $$-1$$, and repeats forever, all corners and jumps. Joseph Fourier asserted in 1807 that this signal, and essentially any repeating signal, can be built out of nothing but smooth sine waves, provided you are allowed to stack up enough of them. The claim scandalized the leading mathematicians of his day. It also turned out to be true, and the mathematics that grew from it now sits inside every phone call, streaming song, JPEG image, and MRI scan.

For a student finishing AP Precalculus or BC, Fourier series are the natural next chapter of two stories at once: the sinusoid chapter, since they promote sine waves from one function family among many to the universal alphabet of periodic behavior, and the Taylor series chapter, since they answer the same question with a different basis. Taylor asks how a function can be assembled from powers of $$x$$; Fourier asks how it can be assembled from frequencies.

## Building the square wave

For the square wave, the recipe turns out to use only odd multiples of the base frequency, each weighted by the reciprocal of its number:

$$f(x) = \frac{4}{\pi}\left(\sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \frac{\sin 7x}{7} + \cdots\right)$$

Each added term is called a harmonic, the same word music uses, and for the same reason. Watch the assembly happen.

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

## Where the coefficients come from

The weights in the recipe are not guessed; they are computed, and the computation is BC-sized. The coefficient of $$\sin(nx)$$ is an integral, of the target function multiplied by $$\sin(nx)$$, taken over one period. What makes the method work is a quiet miracle called orthogonality: the average of $$\sin(mx)\sin(nx)$$ over a period is zero whenever $$m \ne n$$, so the integral acts like a tuner, isolating the strength of one frequency while every other frequency averages itself away. A student who has computed integrals of trigonometric products in Unit 6 has already handled the machinery; Fourier's contribution was recognizing what the machinery could be aimed at.

That tuning interpretation is the modern one. The Fourier coefficients of a signal are its frequency content, and computing them is asking the signal what pitches it contains. When an audio format stores a song, a compression algorithm discards the frequencies your ear weights least; when a noise-cancelling headphone works, it is doing a Fourier analysis in real time and subtracting what it finds.

## The two series, side by side

The comparison with Taylor series is worth making precise, because it organizes both subjects. A Taylor series is local: it knows everything about the function at one point and approximates outward from it, superbly nearby and sometimes not at all far away. A Fourier series is global: it knows the function's average behavior over a whole period, converges in an averaged sense across the entire interval, and cheerfully handles the jumps and corners that no Taylor series can touch, since a function with a jump has no derivative there to match. The two are the first examples every mathematician meets of the same deep strategy, representing a complicated object as coordinates against a well-chosen family of simple ones, and that strategy, generalized, is much of applied mathematics.

<div class="article-note" markdown="1">
An experiment at the slider: set it to one harmonic and imagine hearing that pure tone; this is what a tuning fork sounds like. Forty harmonics of the same base note, in these exact proportions, is what the same pitch sounds like on a clarinet, roughly: the instrument's timbre lives in the coefficients. Two instruments playing the same note agree on the fundamental frequency and disagree in their Fourier series, which is the reason you can tell them apart with your eyes closed.
</div>
