---
layout: post
title: "Integration by parts and partial fractions"
date: 2026-07-30
description: "Two integration techniques for expressions that do not yield directly to substitution. One reverses the product rule. The other rewrites a rational function into simpler pieces."
course: "AP Calculus BC"
read_time: "8 min read"
math: true
kind: mechanics
sequence: 23
interactive: true
blurb: "Two integration techniques for expressions that do not yield directly to substitution. One reverses the product rule. The other rewrites a rational function into simpler pieces"
image: "/assets/og/parts-and-partial-fractions.png"
---

Integration by parts and partial fractions solve different kinds of problems.

Integration by parts is useful when an integrand contains a product whose structure becomes simpler after one factor is differentiated.

Partial fractions is useful for rational functions that can be decomposed into simpler fractions.

The first step is recognizing which structure is present.

## Integration by parts

The product rule says

$$\frac{d}{dx}(uv) = u\frac{dv}{dx} + v\frac{du}{dx}.$$

Integrating both sides gives

$$uv = \int u\,dv + \int v\,du.$$

Rearranging,

$$\int u\,dv = uv-\int v\,du.$$

This is integration by parts.

The choice of $$u$$ matters. A useful choice is one whose derivative is simpler than the original factor.

Consider

$$\int xe^x\,dx.$$

Choose

$$u=x$$

and

$$dv=e^x\,dx.$$

Then

$$du=dx$$

and

$$v=e^x.$$

So

$$\int xe^x\,dx = xe^x-\int e^x\,dx = xe^x-e^x+C.$$

The remaining integral is simpler than the one we started with.

If instead we choose

$$u=e^x$$

and

$$dv=x\,dx,$$

the resulting integral becomes more complicated.

The formula is valid either way. The useful choice is the one that improves the problem.

## A function that looks like one factor

Integration by parts can also be used when there is no visible product.

For

$$\int \ln x\,dx,$$

write

$$\ln x = (\ln x)(1).$$

Choose

$$u=\ln x$$

and

$$dv=dx.$$

Then

$$du=\frac1x\,dx$$

and

$$v=x.$$

Therefore

$$\int \ln x\,dx = x\ln x-\int1\,dx = x\ln x-x+C.$$

The invisible factor of 1 is what makes the product-rule structure available.

## Partial fractions

Partial fractions begins with a rational function.

Suppose

$$\frac{1}{x^2-1} = \frac{1}{(x-1)(x+1)}.$$

We seek constants $$A$$ and $$B$$ such that

$$\frac{1}{(x-1)(x+1)} = \frac{A}{x-1} + \frac{B}{x+1}.$$

Multiplying through by the denominator gives

$$1 = A(x+1)+B(x-1).$$

Setting $$x=1$$ gives

$$A=\frac12.$$

Setting $$x=-1$$ gives

$$B=-\frac12.$$

So

$$\frac{1}{x^2-1} = \frac12\frac{1}{x-1} - \frac12\frac{1}{x+1}.$$

Now integrate term by term:

$$\int\frac{1}{x^2-1}\,dx = \frac12\ln\vert x-1\vert - \frac12\ln\vert x+1\vert + C.$$

The original rational function did not have an obvious antiderivative. After decomposition, each term does.

For the course-level problems considered here, the denominator factors into distinct linear factors. More general decompositions can involve repeated factors and irreducible quadratics, but those require additional forms.

## Check by differentiating

An [antiderivative](/2026/07/17/fundamental-theorem-from-the-ground-up.html) can be checked immediately.

Differentiate

$$\frac12\ln\vert x-1\vert - \frac12\ln\vert x+1\vert .$$

The result is

$$\frac{1}{2(x-1)} - \frac{1}{2(x+1)} = \frac{1}{x^2-1}.$$

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

This is a useful habit after any longer integration problem.

It is especially important with definite integrals because a wrong antiderivative can occasionally produce a plausible numerical answer for particular bounds.

A correct final value does not repair incorrect reasoning.

## Choosing the technique

A useful classification is:

- If the integrand contains a composite function and its derivative, try substitution.
- If it contains a product where differentiating one factor makes the expression simpler, consider integration by parts.
- If it is a rational function with a factorable denominator, consider partial fractions.

<div class="article-note" markdown="1">
These categories can overlap.

The goal is not to identify the most advanced available technique. It is to find the rewrite that makes the integral simpler.
</div>
