---
layout: post
title: "Integration by parts and partial fractions"
date: 2026-07-30
description: "Two BC-only techniques with narrow scopes. One turns on a choice, the other on a restriction the course states explicitly, and both are verified the same way."
course: "AP Calculus BC"
read_time: "8 min read"
math: true
kind: mechanics
sequence: 23
interactive: true
blurb: "Choose u, factor the denominator, then differentiate your answer"
---

Two of BC's integration techniques are procedures rather than ideas. Integration by parts undoes the product rule; partial fractions splits a rational function into pieces that basic techniques already handle. Neither is difficult once started. The difficulty is in starting the right one, and in knowing how narrow each one's scope is.

## The two formulas, and what they require

Integration by parts is the product rule read backwards. From $$(uv)' = u'v + uv'$$, integrating both sides and rearranging,

$$\int u \,dv = uv - \int v\,du.$$

The framework says only that it is a technique for finding antiderivatives, which is honest: the formula does not evaluate anything, it trades one integral for another. Whether that is progress depends entirely on the choice.

Partial fractions comes with a restriction stated in the framework's own words: *some* rational functions can be decomposed into sums of ratios of *linear, nonrepeating* factors. Three conditions, and all three are load-bearing. The denominator must factor, the factors must be linear, and no factor may repeat.

## Choosing u is the whole of integration by parts

Take $$\textstyle\int x e^x\,dx$$. There are two ways to assign the pieces.

Choosing $$u = x$$ and $$dv = e^x dx$$ gives $$du = dx$$ and $$v = e^x$$, so the formula produces $$x e^x - \textstyle\int e^x dx$$, and the remaining integral is one you know. The answer is $$(x-1)e^x$$.

Choosing $$u = e^x$$ and $$dv = x\,dx$$ gives $$du = e^x dx$$ and $$v = \tfrac{x^2}{2}$$, so the formula produces $$\tfrac{x^2}{2}e^x - \textstyle\int \tfrac{x^2}{2}e^x\,dx$$. That is also true, and it is worse: the polynomial's degree went from one to two, and repeating the move will take it to three.

So the test for the choice is not a rule to memorise but a question to ask: does $$\textstyle\int v\,du$$ look easier than what I started with? If the polynomial factor gets differentiated it shrinks toward a constant, and if it gets integrated it grows. That is the reason $$u$$ is usually the polynomial, and it is also the reason the rule breaks for $$\textstyle\int \ln x\,dx$$, where there is no polynomial and only one choice available: $$u = \ln x$$, $$dv = dx$$, giving $$x\ln x - \textstyle\int 1\,dx = x\ln x - x$$.

## Linear and nonrepeating, and what that rules out

To integrate $$\tfrac{1}{x^2-1}$$, factor the denominator and write

$$\frac{1}{(x-1)(x+1)} = \frac{A}{x-1} + \frac{B}{x+1}.$$

Clearing denominators gives $$A(x+1) + B(x-1) = 1$$, and substituting $$x = 1$$ and $$x = -1$$ gives $$A = \tfrac12$$ and $$B = -\tfrac12$$ immediately. Each piece is now a logarithm:

$$\int \frac{dx}{x^2-1} = \tfrac12\ln\vert x-1\vert - \tfrac12\ln\vert x+1\vert + C.$$

The restriction is what makes this reliable. A repeated factor such as $$(x-1)^2$$ needs a second term with the square in its denominator, and an irreducible quadratic such as $$x^2+1$$ needs a linear numerator — both are standard, and neither is in this course. If the denominator does not factor into distinct linear pieces, the problem is not asking for partial fractions.

## Differentiate to check

Every [antiderivative](/2026/07/17/fundamental-theorem-from-the-ground-up.html) carries its own answer key. If $$F$$ is claimed to be an antiderivative of $$f$$, then $$F'$$ must equal $$f$$ everywhere on the interval, and that is a check you can run without knowing whether the original work was right — or whose work it was.

<div class="viz" markdown="0">
  <div class="viz-controls" id="ip-fns"></div>
  <canvas id="ip-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <label for="ip-x">x</label>
    <input type="range" id="ip-x" min="0" max="1200" step="1" value="700">
  </div>
  <div class="ip-read" id="ip-read"></div>
  <p class="viz-caption">Top: the integrand f as a dark curve, with the measured derivative of the claimed antiderivative drawn over it as a pale one. When the antiderivative is right the pale curve is invisible, because it is exactly underneath. Bottom: the antiderivative itself. The last entry is the same integral as the second with the sign of one term flipped, which is the usual slip on that problem; its two curves come apart immediately and the panel prints the gap. Nothing here uses the derivation — the check only needs the claimed answer and the integrand.</p>
  <style>
    .ip-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .ip-read .ip-lab{color:var(--muted);display:inline-block;min-width:12rem}
    .ip-read .ip-val{font-weight:700;display:inline-block;min-width:7rem}
    .ip-read .ip-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('ip-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=44,PADR=18, T1=16,B1=150, T2=176,B2=H-24;
  var sin=Math.sin, cos=Math.cos, exp=Math.exp, log=Math.log;

  var E=[
    { n:'∫ x eˣ dx', lo:-3, hi:2, flo:-1.2, fhi:15.4, Flo:-1.6, Fhi:8.4,
      tech:'integration by parts',
      setup:'u = x,  dv = eˣ dx   →   du = dx,  v = eˣ',
      ans:'(x − 1)eˣ',
      f:function(x){ return x*exp(x); }, F:function(x){ return (x-1)*exp(x); } },
    { n:'∫ x sin x dx', lo:0, hi:2*Math.PI, flo:-6.6, fhi:2.4, Flo:-2.4, Fhi:7.0,
      tech:'integration by parts',
      setup:'u = x,  dv = sin x dx   →   du = dx,  v = −cos x',
      ans:'sin x − x cos x',
      f:function(x){ return x*sin(x); }, F:function(x){ return sin(x)-x*cos(x); } },
    { n:'∫ ln x dx', lo:0.05, hi:4, flo:-3.2, fhi:1.7, Flo:-1.3, Fhi:1.7,
      tech:'integration by parts, with only one choice available',
      setup:'u = ln x,  dv = dx   →   du = dx/x,  v = x',
      ans:'x ln x − x',
      f:function(x){ return log(x); }, F:function(x){ return x*log(x)-x; } },
    { n:'∫ dx/(x² − 1)', lo:1.15, hi:5, flo:-0.1, fhi:4.2, Flo:-1.3, Fhi:0.1,
      tech:'linear partial fractions',
      setup:'1/((x−1)(x+1)) = ½/(x−1) − ½/(x+1)',
      ans:'½ ln(x−1) − ½ ln(x+1)',
      f:function(x){ return 1/(x*x-1); },
      F:function(x){ return 0.5*log(x-1)-0.5*log(x+1); } },
    { n:'∫ x sin x dx, with the usual slip', lo:0, hi:2*Math.PI,
      flo:-6.6, fhi:2.4, Flo:-6.4, Fhi:6.4,
      tech:'integration by parts, second term signed wrongly',
      setup:'u = x,  dv = sin x dx   →   du = dx,  v = −cos x',
      ans:'−sin x − x cos x',
      f:function(x){ return x*sin(x); }, F:function(x){ return -sin(x)-x*cos(x); } }
  ];
  var k=0;
  function G(){ return E[k]; }
  function px(x){ var g=G(); return PADL+(x-g.lo)/(g.hi-g.lo)*(W-PADL-PADR); }
  function fy(v){ var g=G(); return B1-(v-g.flo)/(g.fhi-g.flo)*(B1-T1); }
  function Fy(v){ var g=G(); return B2-(v-g.Flo)/(g.Fhi-g.Flo)*(B2-T2); }
  function fmt(v){ if(!isFinite(v)) return '—';
    var a=Math.abs(v); if(a<1e-12) return (0).toFixed(4);
    if(a<1e-4||a>=1e5) return v.toExponential(3); return v.toFixed(4); }
  function slope(F,x){ var h=1e-5; return (F(x+h)-F(x-h))/(2*h); }

  var bar=$('ip-fns');
  E.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  function trace(h,ymap,style,width,dash){
    var g=G(), i, first=true;
    c.strokeStyle=style; c.lineWidth=width;
    if(dash) c.setLineDash(dash);
    c.beginPath();
    for(i=0;i<=800;i++){ var x=g.lo+(g.hi-g.lo)*i/800, y=h(x);
      if(!isFinite(y)){ first=true; continue; }
      if(first){ c.moveTo(px(x),ymap(y)); first=false; } else c.lineTo(px(x),ymap(y)); }
    c.stroke(); c.setLineDash([]);
  }

  function draw(){
    var g=G(), x=g.lo+(+$('ip-x').value)/1200*(g.hi-g.lo);
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(PADL-2,0,W-PADL-PADR+4,H); c.clip();

    c.strokeStyle=PALE; c.lineWidth=1.2;
    if(g.flo<0&&g.fhi>0){ c.beginPath(); c.moveTo(PADL,fy(0)); c.lineTo(W-PADR,fy(0)); c.stroke(); }
    if(g.Flo<0&&g.Fhi>0){ c.beginPath(); c.moveTo(PADL,Fy(0)); c.lineTo(W-PADR,Fy(0)); c.stroke(); }

    trace(g.f, fy, INK, 2.4);
    trace(function(u){ return slope(g.F,u); }, fy, FAINT, 1.8, [6,4]);
    trace(g.F, Fy, INK, 2);

    c.strokeStyle=LINE; c.lineWidth=1;
    c.beginPath(); c.moveTo(px(x),T1); c.lineTo(px(x),B2); c.stroke();
    if(isFinite(g.f(x))){ c.fillStyle=INK; c.beginPath(); c.arc(px(x),fy(g.f(x)),4,0,6.284); c.fill(); }
    if(isFinite(g.F(x))){ c.fillStyle=INK; c.beginPath(); c.arc(px(x),Fy(g.F(x)),4,0,6.284); c.fill(); }
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText('f, and the measured slope of F', 4, T1+9);
    c.fillText('F', 4, T2+9);

    var fx=g.f(x), Fp=slope(g.F,x), gap=Math.abs(Fp-fx);
    function row(l,v,n){ return '<div><span class="ip-lab">'+l+'</span>'+
      '<span class="ip-val">'+v+'</span>'+(n?'<span class="ip-note">'+n+'</span>':'')+'</div>'; }
    $('ip-read').innerHTML =
      row('technique', '', g.tech) +
      row('setup', '', g.setup) +
      row('claimed F(x)', fmt(g.F(x)), g.ans) +
      row('integrand f(x)', fmt(fx), '') +
      row('F&prime;(x), measured', fmt(Fp), '') +
      row('| F&prime;(x) − f(x) |',
          gap < 1e-6 ? gap.toExponential(1) : gap.toFixed(4),
          gap < 1e-4 ? 'the antiderivative checks out'
                     : 'the two disagree, so the antiderivative is wrong');
  }
  $('ip-x').addEventListener('input',draw);
  draw();
})();
</script>

On the first four the pale curve never separates from the dark one, and the gap stays at the level of the numerical differentiation's own error. On the fifth it does not: the claimed antiderivative $$-\sin x - x\cos x$$ differentiates to $$x\sin x - 2\cos x$$, so the gap is $$2\vert \cos x\vert$$ and reaches 2 wherever the cosine is $$\pm 1$$. That is a large, obvious, findable error, and finding it costs one differentiation.

There is a reason to run that check on the antiderivative rather than trusting the final number, and this example makes it uncomfortably clear. The two claimed antiderivatives differ by $$-2\sin x$$, which is zero at every multiple of $$\pi$$. So on $$[0,\pi]$$ both give the same answer:

$$\int_0^{\pi} x\sin x\,dx = \pi,$$

correct from the right antiderivative and correct from the wrong one. The error is real, the arithmetic is wrong, and the number is right. Shift the upper limit to $$\tfrac{\pi}{2}$$ and it surfaces: the correct antiderivative gives 1 and the faulty one gives $$-1$$.

A definite integral can launder a mistake, and which mistakes it launders depends on the limits. Differentiating the antiderivative does not depend on anything.

<div class="article-note" markdown="1">
The framework devotes a whole topic to choosing among antidifferentiation techniques, and its suggested skill there is to identify an appropriate procedure from the classification of the expression — the same skill the [derivative rules](/2026/07/30/derivative-rules-and-choosing.html) topic carries. The classification questions are short. Is there a composition with its inner derivative present? Substitute. Is it a product of two unrelated functions, one of which simplifies when differentiated? Parts. Is it a rational function whose denominator factors into distinct linear pieces? Partial fractions. Asking all three before writing anything is faster than restarting.
</div>
