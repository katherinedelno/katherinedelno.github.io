---
layout: post
title: "After BC: differential equations"
date: 2026-07-26
description: "Laws of nature specify change and leave the rest to be deduced. Systems, qualitative analysis, and an epidemic to steer."
course: "AP Calculus BC"
section: beyond
read_time: "8 min read"
math: true
kind: beyond
sequence: 6
interactive: true
blurb: "Laws of nature specify change; systems, phase lines, and an epidemic to steer"
---

Most laws of nature do not tell you what happens. They tell you how things are changing, and leave you to work out what happens. Newton's second law relates acceleration, a second derivative, to force. Populations grow in proportion to their size. Heat flows in proportion to temperature differences. Each of these is a differential equation, and the college course by that name is where calculus stops being a subject and starts being the operating system of physics, biology, engineering, and economics.

BC gives you the two keys: separable equations solved exactly, and Euler's method when exactness is out of reach. The full course is what those keys open.

## From one equation to a system

The BC equations involve one unknown function. The world usually involves several, tangled together. The famous first example is an epidemic. Divide a population into susceptible people $$S$$, infected people $$I$$, and recovered people $$R$$, and write down how each group changes:

$$\frac{dS}{dt} = -\beta \frac{SI}{N}, \qquad \frac{dI}{dt} = \beta \frac{SI}{N} - \gamma I, \qquad \frac{dR}{dt} = \gamma I.$$

Read them as sentences. New infections happen when susceptible and infected people meet, at a rate set by the transmission parameter $$\beta$$, so $$S$$ falls and $$I$$ rises by the same amount. Infected people recover at rate $$\gamma$$, draining $$I$$ into $$R$$. That is the whole model, three sentences long, and it is a direct ancestor of the models used in real public health.

No formula solves this system exactly. But Euler's method, the humble two-step tool from BC, handles it numerically without complaint, and that is exactly what the simulation below is doing behind the scenes.

## Steer an outbreak

A town of 1{,}000 people starts with 5 infected. Recovery takes about ten days ($$\gamma = 0.1$$). The slider controls the transmission rate $$\beta$$: how easily the infection spreads.

<div class="viz" markdown="0">
  <canvas id="sir-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="sir-b">Transmission β</label>
    <input type="range" id="sir-b" min="5" max="50" step="1" value="25">
    <span class="viz-value" id="sir-read"></span>
  </div>
  <p class="viz-caption">Light gray: susceptible. Black: currently infected. Medium gray: recovered. Watch the quantity R&#8320; = β/γ, the average number of people each infected person infects. Below 1, the outbreak fizzles without ever taking off. Above 1, it grows into a wave, and the higher R&#8320; climbs, the taller and earlier the peak. Slide β down and watch the peak flatten: that phrase from recent memory is a statement about this exact curve. Notice also that the outbreak always ends before everyone is infected; it dies when S drops low enough that each case can no longer replace itself.</p>
</div>

<script>
(function(){
  var cv = document.getElementById('sir-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('sir-b'), read = document.getElementById('sir-read');
  var W = cv.width, H = cv.height, pad = 34;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  var N = 1000, GAMMA = 0.1, DAYS = 200, DT = 0.25;
  function px(t){ return pad + (t/DAYS)*(W - 2*pad); }
  function py(v){ return H - pad - (v/N)*(H - 2*pad); }
  function draw(){
    var beta = slider.value/100;
    c.clearRect(0, 0, W, H);
    c.strokeStyle = '#e0e0e0'; c.lineWidth = 1;
    c.beginPath(); c.moveTo(pad, py(0)); c.lineTo(W - pad, py(0)); c.stroke();
    c.beginPath(); c.moveTo(pad, py(0)); c.lineTo(pad, py(N)); c.stroke();
    var S = N - 5, I = 5, R = 0;
    var sPts = [], iPts = [], rPts = [], peak = I, peakT = 0;
    for(var t = 0; t <= DAYS; t += DT){
      sPts.push([t, S]); iPts.push([t, I]); rPts.push([t, R]);
      if(I > peak){ peak = I; peakT = t; }
      var newInf = beta*S*I/N*DT, newRec = GAMMA*I*DT;
      S -= newInf; I += newInf - newRec; R += newRec;
    }
    function plot(pts, color, wdt){
      c.strokeStyle = color; c.lineWidth = wdt; c.beginPath();
      for(var i = 0; i < pts.length; i++){
        i ? c.lineTo(px(pts[i][0]), py(pts[i][1])) : c.moveTo(px(pts[i][0]), py(pts[i][1]));
      }
      c.stroke();
    }
    plot(sPts, '#d0d0cd', 2);
    plot(rPts, '#9a9a97', 2);
    plot(iPts, '#1f1f1f', 2.5);
    var r0 = beta/GAMMA;
    read.textContent = 'R₀ = ' + r0.toFixed(1) + '   peak infected: ' + Math.round(peak) + (peak > 6 ? ' on day ' + Math.round(peakT) : ' (no outbreak)');
  }
  slider.addEventListener('input', draw);
  draw();
})();
</script>

## The qualitative revolution

Here is the surprise at the heart of the modern course: for most differential equations, nobody solves for a formula at all, and it turns out not to matter. The important questions are qualitative. Does the system settle to an equilibrium? Oscillate forever? Blow up? You learned the first version of this thinking in BC without the name: when you argued that a logistic population levels off at carrying capacity because $$\tfrac{dP}{dt}$$ shrinks to zero, you did a qualitative analysis. Slope fields are the same idea drawn as a picture.

The college course builds this into a toolkit called phase analysis. For a system like the epidemic, you stop plotting against time and instead plot the state itself, $$S$$ against $$I$$, watching the system trace a curve through its space of possibilities. Equilibria become points that attract or repel trajectories, oscillations become closed loops, and the entire long-run fate of a system becomes visible geometry. A pendulum, a predator-prey ecosystem, and a national economy all get analyzed with the same pictures.

## Springs, and why sine appears everywhere

The single most important equation in physics is BC-sized. A mass on a spring feels a restoring force proportional to displacement, so Newton's law reads

$$\frac{d^2x}{dt^2} = -\omega^2 x.$$

Ask the BC question: what function is its own second derivative, negated? Sine and cosine. The solution is $$x = A\cos(\omega t) + B\sin(\omega t)$$: oscillation is not assumed, it is forced by the equation. This is the honest answer to a question students ask in Precalculus: why do sinusoids model springs, tides, sound, and circuits? Because those systems all obey this equation, and this equation's solutions are sinusoids. The same analysis with a damping term explains why a struck guitar string rings at a definite frequency and dies away exponentially, and the whole package, called the harmonic oscillator, reappears in every physics course through quantum mechanics.

## Chaos: the honest limit

The course ends with one of the great discoveries of twentieth-century mathematics. Some systems, though completely deterministic, are unpredictable in practice. In the 1960s the meteorologist Edward Lorenz found that in his three-equation weather model, two starting points differing by less than a rounding error produced completely different weather within weeks. Nothing was random; the equations amplify tiny differences exponentially. This is chaos, the reason weather forecasts are honest for about ten days and dishonest beyond, and it was found not in exotic mathematics but in a small system of differential equations that a student one course past BC can read.

## What to bring

Differential equations is the most direct sequel to BC. Separable equations, exponential and logistic models, Euler's method, slope fields, and the Taylor series all reappear as first-class citizens (series solutions are a whole chapter). If integration technique is sharp and the logistic story genuinely made sense, the course opens easily, and it pairs naturally with linear algebra, whose eigenvalues turn out to be the key that unlocks systems.

<div class="article-note" markdown="1">
A question to take with you: in the simulator, set β so that R&#8320; is just above 1 and note how many people are still susceptible when the outbreak dies. Herd immunity has a formula: the epidemic turns around exactly when the susceptible fraction falls to 1/R&#8320;. Check it against the curves. A threshold that important, derivable from three one-line equations, is a fair advertisement for the whole subject.
</div>
