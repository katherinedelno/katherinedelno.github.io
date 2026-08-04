---
layout: post
title: "Over or under: reading a linearization"
date: 2026-07-30
description: "The tangent line is the best straight-line stand-in for a function near a point. Deciding whether its value is an overestimate or an underestimate is a question about the whole interval, not about the point."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "9 min read"
math: true
kind: foundations
sequence: 15
interactive: true
blurb: "Concavity at the point of tangency is not the same as concavity in between"
image: "/assets/og/linearization.png"
---

Near the point of tangency, a curve and its tangent line are hard to tell apart. The course calls that local linearity, and it turns the tangent line into a calculator: an expression you can evaluate for a function value you cannot.

The formula takes one line. The interesting question is the one the framework attaches to it — whether the number you get is too big or too small.

## What the linearization is

Given a function $$f$$ differentiable at $$a$$, the linearization of $$f$$ at $$a$$ is the tangent line written as a function:

$$L(x) = f(a) + f'(a)(x - a).$$

The framework's phrasing is that the tangent line is the graph of a locally linear approximation of $$f$$ near the point of tangency, which is worth reading carefully — it is [the same line](/2026/07/30/derivative-as-a-limit.html) as always, given a new job.

The reason to bother is that $$f(a)$$ and $$f'(a)$$ can be easy where $$f(x)$$ is not. To approximate $$\sqrt{4.1}$$, take $$f(x) = \sqrt{x}$$ and $$a = 4$$. Then $$f(4) = 2$$ and $$f'(4) = \tfrac14$$, both exact and both mental arithmetic, so

$$L(4.1) = 2 + \tfrac14(0.1) = 2.025.$$

The true value is $$2.02484567\ldots$$, so the estimate is high by about 0.00015. Which raises the question of how anyone was supposed to know it would be high.

## Over or under is a question about the interval

A tangent line to a concave-up arc lies below it, and a tangent line to a concave-down arc lies above it. So [the sign of $$f''$$](/2026/07/21/reading-the-graph-of-f-prime.html) decides the direction of the error — but only where it holds. The framework is careful about this, saying that the behavior of $$f$$ near the point of tangency *may* determine whether the value is an underestimate or an overestimate.

That word is doing work. What guarantees the answer is the concavity on the entire interval between $$a$$ and $$x$$, not the concavity at $$a$$.

<div class="viz" markdown="0">
  <div class="viz-controls" id="lz-fns"></div>
  <canvas id="lz-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <label for="lz-x">x</label>
    <input type="range" id="lz-x" min="0" max="1200" step="1" value="410">
  </div>
  <div class="lz-read" id="lz-read"></div>
  <p class="viz-caption">The point of tangency is fixed and marked; the slider moves the point being estimated. The vertical bar between the curve and the line is the error, drawn to scale, so the way it opens up as x leaves a is the honest picture of what the approximation costs. The last row of the panel is the one that matters: it samples the second derivative strictly between a and x and reports whether the sign holds all the way across. When it does, the concavity settles the question. When it does not, the panel says so rather than guessing.</p>
  <style>
    .lz-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .lz-read .lz-lab{color:var(--muted);display:inline-block;min-width:14rem}
    .lz-read .lz-val{font-weight:700;display:inline-block;min-width:7rem}
    .lz-read .lz-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('lz-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=40,PADR=18,TOP=16,BOT=H-26;

  // Ranges are set so every x the article names lands on an integer slider step:
  // 4.05/4.1/4.2/9 at 405/410/420/900, 0.1 at 744, +-0.5 at 700/500, 0/2/3 at 480/960/1200.
  var F=[
    { n:'√x   at a = 4', a:4, lo:0, hi:12, ylo:-0.3, yhi:4.3,
      f:Math.sqrt,
      d:function(x){ return 0.5/Math.sqrt(x); },
      dd:function(x){ return -0.25/Math.pow(x,1.5); } },
    { n:'eˣ   at a = 0', a:0, lo:-3, hi:2, ylo:-1.2, yhi:7.8,
      f:Math.exp, d:Math.exp, dd:Math.exp },
    { n:'sin x   at a = 0', a:0, lo:-3, hi:3, ylo:-3.2, yhi:3.2,
      f:Math.sin,
      d:Math.cos,
      dd:function(x){ return -Math.sin(x); } },
    { n:'x³   at a = −1', a:-1, lo:-2, hi:3, ylo:-9, yhi:28,
      f:function(x){ return x*x*x; },
      d:function(x){ return 3*x*x; },
      dd:function(x){ return 6*x; } }
  ];
  var k=0;
  function G(){ return F[k]; }
  function px(x){ var g=G(); return PADL+(x-g.lo)/(g.hi-g.lo)*(W-PADL-PADR); }
  function py(y){ var g=G(); return BOT-(y-g.ylo)/(g.yhi-g.ylo)*(BOT-TOP); }
  function fmt(v){ var x=Math.abs(v);
    if(x<1e-12) return (0).toFixed(4);
    if(x<1e-4||x>=1e5) return v.toExponential(3);
    return v.toFixed(4); }
  // The error spans several orders of magnitude on one curve, and the article
  // makes a claim about how its ratio behaves, so it gets significant figures
  // rather than a fixed number of decimal places.
  function fmtErr(v){ return Math.abs(v)<1e-12 ? (0).toFixed(4) : v.toPrecision(5); }

  var bar=$('lz-fns');
  F.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  // Sample f'' strictly between a and x. Returns 'up', 'down', 'mixed', or 'none'
  // when a and x coincide. Endpoints excluded on purpose: a itself may be an
  // inflection point, and that is not what decides the comparison.
  function concavity(g,a,x){
    if(Math.abs(x-a)<1e-12) return 'none';
    var lo=Math.min(a,x), hi=Math.max(a,x), pos=false, neg=false, N=400;
    for(var i=1;i<N;i++){
      var v=g.dd(lo+(hi-lo)*i/N);
      if(v>1e-12) pos=true; else if(v<-1e-12) neg=true;
    }
    if(pos&&neg) return 'mixed';
    if(pos) return 'up';
    if(neg) return 'down';
    return 'flat';
  }

  function draw(){
    var g=G(), x=g.lo+(+$('lz-x').value)/1200*(g.hi-g.lo);
    var a=g.a, fa=g.f(a), ma=g.d(a);
    function L(t){ return fa+ma*(t-a); }
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(PADL-1,TOP-6,W-PADL-PADR+2,BOT-TOP+12); c.clip();

    c.strokeStyle=LINE; c.lineWidth=1;
    var i,t;
    for(i=Math.ceil(g.lo);i<=g.hi;i++){ c.beginPath(); c.moveTo(px(i),TOP); c.lineTo(px(i),BOT); c.stroke(); }
    if(g.ylo<0&&g.yhi>0){ c.strokeStyle=PALE; c.lineWidth=1.2;
      c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke(); }

    // the tangent line, then the curve on top of it
    c.strokeStyle=FAINT; c.lineWidth=1.6; c.setLineDash([6,4]);
    c.beginPath(); c.moveTo(px(g.lo),py(L(g.lo))); c.lineTo(px(g.hi),py(L(g.hi))); c.stroke();
    c.setLineDash([]);
    c.strokeStyle=INK; c.lineWidth=2; c.beginPath();
    for(i=0;i<=800;i++){ t=g.lo+(g.hi-g.lo)*i/800;
      if(i===0) c.moveTo(px(t),py(g.f(t))); else c.lineTo(px(t),py(g.f(t))); }
    c.stroke();

    // the error, drawn to scale
    c.strokeStyle=INK; c.lineWidth=3;
    c.beginPath(); c.moveTo(px(x),py(g.f(x))); c.lineTo(px(x),py(L(x))); c.stroke();
    c.fillStyle=INK; c.beginPath(); c.arc(px(a),py(fa),5,0,6.284); c.fill();
    c.fillStyle=FAINT; c.beginPath(); c.arc(px(x),py(L(x)),4,0,6.284); c.fill();
    c.fillStyle=INK;  c.beginPath(); c.arc(px(x),py(g.f(x)),4,0,6.284); c.fill();
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    c.fillText('a',px(a),BOT+14); c.fillText('x',px(x),BOT+14);

    var Lx=L(x), fx=g.f(x), err=Lx-fx, cc=concavity(g,a,x);
    var verdict = Math.abs(err)<1e-12 ? 'the line meets the curve here'
                : (err>0 ? 'overestimate' : 'underestimate');
    var ccnote = {
      up:   'positive throughout &mdash; concave up, so the line lies below',
      down: 'negative throughout &mdash; concave down, so the line lies above',
      mixed:'changes sign &mdash; concavity alone settles nothing here',
      flat: 'zero throughout &mdash; the function is its own tangent line',
      none: 'no interval yet'
    }[cc];
    function row(l,v,n){ return '<div><span class="lz-lab">'+l+'</span>'+
      '<span class="lz-val">'+v+'</span>'+(n?'<span class="lz-note">'+n+'</span>':'')+'</div>'; }
    $('lz-read').innerHTML =
      row('a, the point of tangency', fmt(a), '') +
      row('x', fmt(x), '') +
      row('L(x) = f(a) + f&prime;(a)(x &minus; a)', fmt(Lx), '') +
      row('f(x)', fmt(fx), '') +
      row('L(x) &minus; f(x)', fmtErr(err), verdict) +
      row('f&Prime; strictly between a and x', '', ccnote);
  }
  $('lz-x').addEventListener('input',draw);
  draw();
})();
</script>

The first two functions never make trouble. The square root is concave down on its whole domain, so its tangent line is above the curve everywhere and the estimate is high no matter where you evaluate it. The exponential is concave up everywhere, so its tangent is below and the estimate is low. In both cases the concavity at $$a$$ and the concavity across the interval are the same fact.

The sine is the first case where the point is not enough. At $$a = 0$$ the second derivative is zero, so the sign of $$f''(0)$$ predicts nothing at all. Move right and the interval is concave down, so $$L$$ is high; move left and it is concave up, so $$L$$ is low. The same tangent line overestimates on one side and underestimates on the other.

## Where the guarantee runs out

Take $$f(x) = x^3$$ at $$a = -1$$. Then $$f(-1) = -1$$ and $$f'(-1) = 3$$, so $$L(x) = 3x + 2$$, and $$f''(-1) = -6$$ is comfortably negative. Concave down at the point of tangency, so the line is above the curve — and for a while it is.

The difference factors:

$$L(x) - f(x) = 3x + 2 - x^3 = -(x-2)(x+1)^2.$$

The squared factor at $$x = -1$$ is the tangency itself. The other root is $$x = 2$$, and beyond it the whole expression changes sign. At $$x = 1$$ the line is high by 4; at $$x = 3$$ it is low by 16. Nothing about $$f''(-1)$$ hinted at that, because the inflection point at $$x = 0$$ sits between the point of tangency and every $$x$$ on the far side of it.

So the justification that works is about the interval: *$$f$$ is concave down on $$[a, x]$$, therefore the tangent line lies above the curve there, therefore $$L(x)$$ overestimates $$f(x)$$*. Naming the sign of $$f''(a)$$ alone is a claim about one point being offered as a claim about a stretch.

## How fast the error grows

Skill 1.F for this topic is to explain how an approximated value relates to the actual value, and the size of the gap is half of that explanation. It grows like the square of the distance.

Estimating $$\sqrt{x}$$ from $$a = 4$$, the tangent line is high by 0.0000388 at $$x = 4.05$$, by 0.000154 at $$4.1$$, and by 0.000610 at $$4.2$$. Each doubling of the step multiplies the error by very nearly four. Push out to $$x = 9$$ and the same line gives 3.25 against a true value of 3 — still an overestimate, as the concavity promised, but no longer an approximation of anything.

That quadratic growth is not an accident of the square root. The linearization is the degree-one member of a family, and the next term in that family carries $$\tfrac12 f''(a)(x-a)^2$$ — for $$\sqrt{x}$$ at $$a = 4$$ that predicts an error of 0.00015625 at $$x = 4.1$$, against a true 0.00015433. Adding more terms is what [Taylor polynomials](/2026/07/22/taylor-polynomials-impersonate-functions.html) do, and the tangent line is where they start.

<div class="article-note" markdown="1">
Two habits make these questions quick. Choose $$a$$ to be the nearest point where $$f$$ and $$f'$$ are both easy, which for a root means the nearest perfect square or cube. Then, before deciding over or under, sketch the concavity across the whole gap rather than checking a sign at one end — that is the step the question is actually testing, and it is the one that gets skipped.
</div>
