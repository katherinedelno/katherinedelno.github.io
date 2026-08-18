---
layout: post
title: "Area between curves and average value"
date: 2026-07-30
description: "Average value and area between curves both depend on setting up the correct integrand before evaluating the integral."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "6 min read"
math: true
kind: foundations
sequence: 27
interactive: true
blurb: "Average value and area between curves both depend on setting up the correct integrand before evaluating the integral"
image: "/assets/og/area-and-average-value.png"
---

Average value and area between curves are different applications of the definite integral, and both depend on setting up the integrand correctly. For average value, the integral is divided by the width of the interval, and for area between curves, the integrand is the difference between the relevant boundaries.

## Average value

The average value of $$f$$ on $$[a,b]$$ is

$$f_{\text{avg}} = \frac{1}{b-a} \int_a^b f(x)\,dx$$

Geometrically, this is the height of a rectangle with width $$b-a$$ and the same signed area as the integral, and its units are the same as the units of $$f$$. This is different from average rate of change, $$\tfrac{f(b)-f(a)}{b-a}$$. In fact,

$$\frac{f(b)-f(a)}{b-a} = \frac{1}{b-a} \int_a^b f'(x)\,dx$$

So the average rate of change of $$f$$ is the average value of $$f'$$, not the average value of $$f$$. For example, on $$[1,3]$$ with $$f(x)=x^2$$, the average rate of change is $$4$$ while the average value is $$\tfrac{13}{3}$$, and they are different quantities.

## Average value is not the midpoint of the range

On $$[0,1]$$, consider three functions that all range from 0 to 1. For $$f(x)=x,\; x^2,\; \sqrt{x}$$, the average values are $$\tfrac12,\; \tfrac13,\; \tfrac23$$. The midpoint of the output range is $$1/2$$ in all three cases, so the average value depends on how the function is distributed across the interval, not only on its minimum and maximum.

## Area between two curves

To find area between two graphs using vertical slices, integrate $$\text{top} - \text{bottom}$$. For $$y=x$$ and $$y=x^2$$ on $$[0,1]$$, we have $$x\ge x^2$$, so

$$A = \int_0^1(x-x^2)\,dx = \frac16$$

If the curves cross inside the interval, the integral may need to be split. A signed integral can cancel. Geometric area cannot.

<div class="viz" markdown="0">
  <div class="viz-controls" id="ar-fns"></div>
  <canvas id="ar-cv" width="700" height="310"></canvas>
  <div class="ar-read" id="ar-read"></div>
  <p class="viz-caption">Five regions. Dark shading is where the first named boundary is ahead of the second and the difference counts positively; pale shading is where they have swapped and it counts negatively. The panel gives both the signed integral and the total area, which are the same number only when the boundaries never cross in between. The first two presets are average value in disguise: the constant is chosen so the signed integral is exactly zero, which is what makes it the average, and the two shaded pieces then have equal area.</p>
  <style>
    .ar-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .ar-read .ar-lab{color:var(--muted);display:inline-block;min-width:13rem}
    .ar-read .ar-val{font-weight:700;display:inline-block;min-width:7rem}
    .ar-read .ar-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('ar-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3',
      POS='#c9c9c9',NEG='#efefef';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=44,PADR=18,TOP=16,BOT=H-26;

  // "in" is the variable of integration: 'x' means vertical strips, 'y' horizontal.
  var E=[
    { n:'x² and its average value', v:'x', a:0, b:1, lo:-0.15, hi:1.15, wlo:-0.15, whi:1.15,
      f1:function(t){ return 1/3; }, f2:function(t){ return t*t; },
      s1:'y = 1/3', s2:'y = x²',
      note:'the constant is the average value, so the signed integral is zero' },
    { n:'√x and its average value', v:'x', a:0, b:1, lo:-0.15, hi:1.15, wlo:-0.15, whi:1.15,
      f1:function(t){ return 2/3; }, f2:function(t){ return Math.sqrt(t); },
      s1:'y = 2/3', s2:'y = √x',
      note:'again zero, and here the average sits above the midpoint of the range' },
    { n:'y = x and y = x²', v:'x', a:0, b:1, lo:-0.15, hi:1.15, wlo:-0.15, whi:1.15,
      f1:function(t){ return t; }, f2:function(t){ return t*t; },
      s1:'y = x', s2:'y = x²',
      note:'one boundary stays above the other, so the two numbers agree' },
    { n:'y = x and y = x³', v:'x', a:-1, b:1, lo:-1.25, hi:1.25, wlo:-1.25, whi:1.25,
      f1:function(t){ return t; }, f2:function(t){ return t*t*t; },
      s1:'y = x', s2:'y = x³',
      note:'they swap at x = 0, so the signed integral cancels and the area does not' },
    { n:'x = y + 2 and x = y²', v:'y', a:-1, b:2, lo:-1.6, hi:2.6, wlo:-0.4, whi:4.4,
      f1:function(t){ return t+2; }, f2:function(t){ return t*t; },
      s1:'x = y + 2', s2:'x = y²',
      note:'horizontal strips, so the integration is with respect to y' }
  ];
  var k=0;
  function G(){ return E[k]; }
  // For 'x' presets the plot axes are (t, value); for 'y' presets they are (value, t).
  function ax(t,v){ var g=G();
    return g.v==='x' ? PADL+(t-g.lo)/(g.hi-g.lo)*(W-PADL-PADR)
                     : PADL+(v-g.wlo)/(g.whi-g.wlo)*(W-PADL-PADR); }
  function ay(t,v){ var g=G();
    return g.v==='x' ? BOT-(v-g.wlo)/(g.whi-g.wlo)*(BOT-TOP)
                     : BOT-(t-g.lo)/(g.hi-g.lo)*(BOT-TOP); }
  function fmt(v){ var a=Math.abs(v); if(a<1e-12) return (0).toFixed(4); return v.toFixed(4); }

  // composite Simpson on the difference, and on its absolute value
  function simpson(h,a,b,n){
    var s=h(a)+h(b), i;
    for(i=1;i<n;i++) s += (i%2 ? 4 : 2)*h(a+(b-a)*i/n);
    return s*(b-a)/(3*n);
  }

  var bar=$('ar-fns');
  E.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  function draw(){
    var g=G();
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(PADL-2,TOP-6,W-PADL-PADR+4,BOT-TOP+12); c.clip();

    c.strokeStyle=LINE; c.lineWidth=1;
    var i,t;
    for(i=Math.ceil(g.lo);i<=g.hi;i++){
      if(g.v==='x'){ c.beginPath(); c.moveTo(ax(i,0),TOP); c.lineTo(ax(i,0),BOT); c.stroke(); }
      else { c.beginPath(); c.moveTo(PADL,ay(i,0)); c.lineTo(W-PADR,ay(i,0)); c.stroke(); } }

    // the region, strip by strip, colored by which boundary is ahead
    var N=440;
    for(i=0;i<N;i++){
      var t0=g.a+(g.b-g.a)*i/N, t1=g.a+(g.b-g.a)*(i+1)/N, tm=(t0+t1)/2;
      c.fillStyle = (g.f1(tm)-g.f2(tm))>=0 ? POS : NEG;
      c.beginPath();
      c.moveTo(ax(t0,g.f1(t0)),ay(t0,g.f1(t0)));
      c.lineTo(ax(t1,g.f1(t1)),ay(t1,g.f1(t1)));
      c.lineTo(ax(t1,g.f2(t1)),ay(t1,g.f2(t1)));
      c.lineTo(ax(t0,g.f2(t0)),ay(t0,g.f2(t0)));
      c.closePath(); c.fill();
    }
    [[g.f1,INK],[g.f2,FAINT]].forEach(function(q){
      c.strokeStyle=q[1]; c.lineWidth=2.2; c.beginPath();
      for(i=0;i<=500;i++){ t=g.lo+(g.hi-g.lo)*i/500;
        var v=q[0](t); if(!isFinite(v)) continue;
        if(i===0) c.moveTo(ax(t,v),ay(t,v)); else c.lineTo(ax(t,v),ay(t,v)); }
      c.stroke(); });
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText(g.s1+'   (dark)      '+g.s2+'   (pale)', 4, TOP-4);

    var diff=function(t){ return g.f1(t)-g.f2(t); };
    var signed=simpson(diff,g.a,g.b,2000);
    var total =simpson(function(t){ return Math.abs(diff(t)); },g.a,g.b,4000);
    function row(l,v,n){ return '<div><span class="ar-lab">'+l+'</span>'+
      '<span class="ar-val">'+v+'</span>'+(n?'<span class="ar-note">'+n+'</span>':'')+'</div>'; }
    $('ar-read').innerHTML =
      row('integrating in', g.v, 'from '+fmt(g.a)+' to '+fmt(g.b)) +
      row('integrand', '', '('+g.s1.replace(/^[xy] = /,'')+') − ('+g.s2.replace(/^[xy] = /,'')+')') +
      row('signed integral', fmt(signed), '') +
      row('total area', fmt(total),
          Math.abs(total-Math.abs(signed))<1e-6 ? 'equal to the signed value here'
                                                : 'larger, because the boundaries swap') +
      row('', '', g.note);
  }
  draw();
})();
</script>

The visualization distinguishes [signed accumulation](/2026/07/30/accumulation-functions.html) from total area. When one boundary crosses the other, the sign of their difference changes, and if the goal is geometric area, split the integral at the crossing and keep each piece positive.

## Integrating with respect to $$y$$

Vertical slices are not always the easiest choice. Suppose a region is bounded by $$x=y^2$$ and $$x=y+2$$. The curves meet where $$y^2=y+2$$, so $$y=-1$$ and $$y=2$$. Using horizontal slices,

$$A = \int_{-1}^{2} \left((y+2)-y^2\right)\,dy = \frac92$$

The same region can be described using $$x$$, but the setup becomes less direct, and choosing the variable is part of the problem.

## Curves that cross more than once

Consider $$y=x$$ and $$y=x^3$$ on $$[-1,1]$$. The curves meet at $$-1,\; 0,\; 1$$. On the left half, $$x^3$$ lies above $$x$$, and on the right half, $$x$$ lies above $$x^3$$.

The signed integral $$\textstyle\int_{-1}^{1}(x-x^3)\,dx = 0$$ is correct as a net signed quantity, but it is not the geometric area. For area, split at $$x=0$$ and add the magnitudes of the two regions.

<div class="article-note" markdown="1">
Before integrating a difference, ask whether cancellation is appropriate. For average value, signed accumulation is part of the definition, and for geometric area, cancellation is not.
</div>
