---
layout: post
title: "Reading an accumulation function off the graph of its integrand"
date: 2026-07-30
description: "If g(x) = ∫ₐˣ f(t) dt, then the graph of f tells you the slope and concavity of g, while signed area determines its values."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "9 min read"
math: true
kind: foundations
sequence: 21
interactive: true
blurb: "If g(x) = ∫ₐˣ f(t) dt, then the graph of f tells you the slope and concavity of g, while signed area determines its values"
image: "/assets/og/accumulation-functions.png"
---

A function can be defined by an integral.

Let

$$g(x) = \int_a^x f(t)\,dt,$$

where $$f$$ is continuous.

[The Fundamental Theorem](/2026/07/17/fundamental-theorem-from-the-ground-up.html) gives

$$g'(x)=f(x).$$

Differentiating again gives

$$g''(x)=f'(x).$$

Those two equations turn a graph of $$f$$ into information about the behavior of $$g$$.

## The translation

| About $$g$$ | Read from $$f$$ |
|---|---|
| $$g$$ is increasing | $$f>0$$ |
| $$g$$ is decreasing | $$f<0$$ |
| $$g$$ has a local maximum | $$f$$ crosses from positive to negative |
| $$g$$ has a local minimum | $$f$$ crosses from negative to positive |
| $$g$$ is concave up | $$f$$ is increasing |
| $$g$$ is concave down | $$f$$ is decreasing |
| $$g$$ changes concavity | $$f'$$ changes sign |
| $$g(x)=0$$ | the signed area from $$a$$ to $$x$$ is zero |

This is the same reasoning used when [reading the graph of a derivative](/2026/07/21/reading-the-graph-of-f-prime.html).

Here $$f$$ plays the role of $$g'$$.

## Reading values from geometry

<div class="viz" markdown="0">
  <canvas id="ac-cv" width="700" height="360"></canvas>
  <div class="viz-controls">
    <label for="ac-a">lower limit a</label>
    <input type="range" id="ac-a" min="0" max="1600" step="1" value="0">
    <label for="ac-x">upper limit x</label>
    <input type="range" id="ac-x" min="0" max="1600" step="1" value="700">
  </div>
  <div class="ac-read" id="ac-read"></div>
  <p class="viz-caption">Top: a piecewise linear f, the format these questions arrive in, with the region between a and x shaded, dark where it counts positively, light where it counts negatively. Bottom: the graph of g for the current lower limit, with hollow dots at its local extrema and bars at its inflection points. Move x and watch g trace out. Then move a and watch the whole curve slide vertically while every marker stays exactly where it was, because changing the lower limit changes g by a constant and a constant has no effect on any derivative.</p>
  <style>
    .ac-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .ac-read .ac-lab{color:var(--muted);display:inline-block;min-width:13.5rem}
    .ac-read .ac-val{font-weight:700;display:inline-block;min-width:6.5rem}
    .ac-read .ac-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('ac-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3',
      POS='#c9c9c9',NEG='#efefef';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=40,PADR=18, T1=16,B1=158, T2=196,B2=H-26;
  var X0=0, X1=8;

  // f is piecewise linear through these vertices. Slopes 2, -2, 4/3; zeros at
  // 0.5, 3.5, 7.25; the three segment areas are exactly 2, 0, and -3.
  var V=[[0,-1],[2,3],[5,-3],[8,1]];
  function f(u){
    for(var i=0;i<V.length-1;i++){
      if(u>=V[i][0] && u<=V[i+1][0]){
        var t=(u-V[i][0])/(V[i+1][0]-V[i][0]);
        return V[i][1]+t*(V[i+1][1]-V[i][1]);
      }
    }
    return u<X0 ? V[0][1] : V[V.length-1][1];
  }
  function slope(u){
    for(var i=0;i<V.length-1;i++){
      if(u>=V[i][0] && u<V[i+1][0])
        return (V[i+1][1]-V[i][1])/(V[i+1][0]-V[i][0]);
    }
    return (V[V.length-1][1]-V[V.length-2][1])/(V[V.length-1][0]-V[V.length-2][0]);
  }
  // exact integral from 0 to u: trapezoids are exact on a linear piece
  function G0(u){
    var tot=0;
    for(var i=0;i<V.length-1;i++){
      if(u<=V[i][0]) break;
      var r=Math.min(u,V[i+1][0]);
      tot += (f(V[i][0])+f(r))/2*(r-V[i][0]);
    }
    return tot;
  }
  var ZEROS=[0.5,3.5,7.25], CORNERS=[2,5];
  var FLO=-3.6, FHI=3.6, GLO=-6.4, GHI=5.4;

  function px(u){ return PADL+(u-X0)/(X1-X0)*(W-PADL-PADR); }
  function fy(v){ return B1-(v-FLO)/(FHI-FLO)*(B1-T1); }
  function gy(v){ return B2-(v-GLO)/(GHI-GLO)*(B2-T2); }
  function fmt(v){ return Math.abs(v)<1e-12 ? (0).toFixed(4) : v.toFixed(4); }

  function draw(){
    var a=X0+(+$('ac-a').value)/1600*(X1-X0);
    var x=X0+(+$('ac-x').value)/1600*(X1-X0);
    var g=function(u){ return G0(u)-G0(a); };
    c.clearRect(0,0,W,H);

    // ---- top: f, with the region between a and x shaded by sign
    var lo=Math.min(a,x), hi=Math.max(a,x), i, u;
    for(i=0;i<420;i++){
      var u0=lo+(hi-lo)*i/420, u1=lo+(hi-lo)*(i+1)/420, mid=(u0+u1)/2;
      c.fillStyle = f(mid)>=0 ? POS : NEG;
      c.beginPath();
      c.moveTo(px(u0),fy(0)); c.lineTo(px(u0),fy(f(u0)));
      c.lineTo(px(u1),fy(f(u1))); c.lineTo(px(u1),fy(0));
      c.closePath(); c.fill();
    }
    c.strokeStyle=LINE; c.lineWidth=1;
    for(i=0;i<=8;i++){ c.beginPath(); c.moveTo(px(i),T1); c.lineTo(px(i),B1); c.stroke(); }
    c.strokeStyle=PALE; c.lineWidth=1.2;
    c.beginPath(); c.moveTo(PADL,fy(0)); c.lineTo(W-PADR,fy(0)); c.stroke();
    c.strokeStyle=INK; c.lineWidth=2; c.beginPath();
    V.forEach(function(p,j){ if(j===0) c.moveTo(px(p[0]),fy(p[1])); else c.lineTo(px(p[0]),fy(p[1])); });
    c.stroke();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText('f', 6, T1+10);

    // ---- bottom: g for this lower limit
    c.strokeStyle=LINE; c.lineWidth=1;
    for(i=0;i<=8;i++){ c.beginPath(); c.moveTo(px(i),T2); c.lineTo(px(i),B2); c.stroke(); }
    c.strokeStyle=PALE; c.lineWidth=1.2;
    c.beginPath(); c.moveTo(PADL,gy(0)); c.lineTo(W-PADR,gy(0)); c.stroke();
    c.strokeStyle=PALE; c.lineWidth=2; c.beginPath();
    for(i=0;i<=640;i++){ u=X0+(X1-X0)*i/640;
      if(i===0) c.moveTo(px(u),gy(g(u))); else c.lineTo(px(u),gy(g(u))); }
    c.stroke();
    c.strokeStyle=INK; c.lineWidth=2.4; c.beginPath();
    for(i=0;i<=640;i++){ u=X0+(X1-X0)*i/640;
      if(u<lo||u>hi){ continue; }
      if(Math.abs(u-lo)<(X1-X0)/640) c.moveTo(px(u),gy(g(u))); else c.lineTo(px(u),gy(g(u))); }
    c.stroke();

    c.lineWidth=1.8;
    ZEROS.forEach(function(z){
      c.strokeStyle=INK; c.beginPath(); c.arc(px(z),gy(g(z)),4.5,0,6.284); c.stroke(); });
    CORNERS.forEach(function(z){
      c.strokeStyle=FAINT; c.beginPath();
      c.moveTo(px(z),gy(g(z))-6); c.lineTo(px(z),gy(g(z))+6); c.stroke(); });

    [[a,'a'],[x,'x']].forEach(function(p){
      c.strokeStyle=FAINT; c.lineWidth=1; c.setLineDash([4,3]);
      c.beginPath(); c.moveTo(px(p[0]),T1); c.lineTo(px(p[0]),B2); c.stroke(); c.setLineDash([]);
      c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
      c.fillText(p[1],px(p[0]),B2+14); });
    c.fillStyle=INK; c.beginPath(); c.arc(px(x),gy(g(x)),4.5,0,6.284); c.fill();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText('g', 6, T2+10);

    var fx=f(x), sx=slope(x);
    var mono = Math.abs(fx)<1e-9 ? 'neither, momentarily'
             : (fx>0 ? 'g is increasing here' : 'g is decreasing here');
    var conc = sx>0 ? 'g is concave up here' : (sx<0 ? 'g is concave down here' : 'g is linear here');
    function row(l,v,n){ return '<div><span class="ac-lab">'+l+'</span>'+
      '<span class="ac-val">'+v+'</span>'+(n?'<span class="ac-note">'+n+'</span>':'')+'</div>'; }
    $('ac-read').innerHTML =
      row('lower limit  a', fmt(a), 'g(a) = 0, always') +
      row('upper limit  x', fmt(x), '') +
      row('g(x)', fmt(g(x)), 'the signed area from a to x') +
      row('g&prime;(x) = f(x)', fmt(fx), mono) +
      row('g&Prime;(x) = f&prime;(x)', fmt(sx), conc);
  }
  $('ac-a').addEventListener('input',draw);
  $('ac-x').addEventListener('input',draw);
  draw();
})();
</script>

The top graph shows $$f$$, with the region between $$a$$ and $$x$$ shaded according to sign.

The lower graph shows the corresponding accumulation function.

Suppose $$a=0$$.

To compute

$$g(3.5) = \int_0^{3.5}f(t)\,dt,$$

add the signed areas.

In the displayed example, the first small triangle lies below the axis and contributes

$$-\frac14.$$

The next two triangles lie above the axis and each contribute

$$\frac94.$$

Therefore

$$g(3.5) = -\frac14+\frac94+\frac94 = \frac{17}{4}.$$

No antiderivative is needed.

The graph is enough.

A definite integral of zero also does not mean nothing happened.

If positive and negative areas cancel, the accumulation can return to an earlier value even while the function changes throughout the interval.

## What changing the lower limit does

Changing $$a$$ shifts the entire accumulation function vertically.

It does not change its derivative.

To see why, compare

$$g_1(x) = \int_{a_1}^{x}f(t)\,dt$$

with

$$g_2(x) = \int_{a_2}^{x}f(t)\,dt.$$

Using additivity,

$$\int_{a_2}^{x}f = \int_{a_2}^{a_1}f + \int_{a_1}^{x}f.$$

The first term is constant with respect to $$x$$.

So $$g_2$$ differs from $$g_1$$ by a constant.

That means the location of extrema and inflection points does not change.

The function values do change.

Also,

$$g(a)=0$$

for any lower limit $$a$$, because an integral from a point to itself is zero.

## What if $$x<a$$?

The accumulation function is still defined when the upper limit lies to the left of the lower limit.

Reversing the bounds changes the sign:

$$\int_a^x f(t)\,dt = -\int_x^a f(t)\,dt.$$

The derivative relationship remains

$$g'(x)=f(x).$$

So $$g$$ still increases wherever $$f$$ is positive and decreases wherever $$f$$ is negative, even to the left of $$a$$.

<div class="article-note" markdown="1">
A reliable setup on a free-response problem is to write

$$g'=f$$

and

$$g''=f'$$

before answering anything else.

Then separate two kinds of questions.

Questions about values of $$g$$ use signed area.

Questions about increase, decrease, extrema, and concavity use the derivative relationships.
</div>
