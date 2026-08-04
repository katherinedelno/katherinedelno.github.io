---
layout: post
title: "Reading an accumulation function off the graph of its integrand"
date: 2026-07-30
description: "When a function is defined as an integral, every question about it is a question about the picture of the integrand. Increasing, concave, extreme, and inflected all translate, and only one thing depends on the lower limit."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "9 min read"
math: true
kind: foundations
sequence: 21
interactive: true
blurb: "Every question about g is a question about the picture of f"
image: "/assets/og/accumulation-functions.png"
---

A function can be defined by an integral. Given a continuous $$f$$ and a number $$a$$ in its interval, set

$$g(x) = \int_a^x f(t)\,dt,$$

and $$g$$ is a perfectly ordinary function with a graph, a derivative, and extrema. The framework calls it an accumulation function and states plainly what makes it usable: graphical, numerical, analytical, and verbal representations of $$f$$ provide information about $$g$$.

[Why $$g' = f$$](/2026/07/17/fundamental-theorem-from-the-ground-up.html) is the Fundamental Theorem and is argued elsewhere. This article is about the consequence: the translation from a picture of $$f$$ to the behavior of $$g$$.

## The translation

Two lines do all the work. The Fundamental Theorem gives $$g'(x) = f(x)$$, and differentiating again gives $$g''(x) = f'(x)$$. Everything follows by applying the usual derivative tests to those.

| about $$g$$ | read from $$f$$ |
|---|---|
| $$g$$ is increasing | $$f$$ is above the axis |
| $$g$$ is decreasing | $$f$$ is below the axis |
| $$g$$ has a local maximum | $$f$$ crosses from above to below |
| $$g$$ has a local minimum | $$f$$ crosses from below to above |
| $$g$$ is concave up | $$f$$ is increasing |
| $$g$$ is concave down | $$f$$ is decreasing |
| $$g$$ has an inflection point | $$f$$ has a local extremum or a corner |
| $$g(x) = 0$$ | the signed area from $$a$$ to $$x$$ cancels out |

This is [reading the graph of a derivative](/2026/07/21/reading-the-graph-of-f-prime.html) with the labels shifted one place: $$f$$ plays for $$g$$ the role $$f'$$ plays for $$f$$. The skill is the same one and the table is the same table.

## The picture, and the lower limit

<div class="viz" markdown="0">
  <canvas id="ac-cv" width="700" height="360"></canvas>
  <div class="viz-controls">
    <label for="ac-a">lower limit a</label>
    <input type="range" id="ac-a" min="0" max="1600" step="1" value="0">
    <label for="ac-x">upper limit x</label>
    <input type="range" id="ac-x" min="0" max="1600" step="1" value="700">
  </div>
  <div class="ac-read" id="ac-read"></div>
  <p class="viz-caption">Top: a piecewise linear f, the format these questions arrive in, with the region between a and x shaded — dark where it counts positively, light where it counts negatively. Bottom: the graph of g for the current lower limit, with hollow dots at its local extrema and bars at its inflection points. Move x and watch g trace out. Then move a and watch the whole curve slide vertically while every marker stays exactly where it was, because changing the lower limit changes g by a constant and a constant has no effect on any derivative.</p>
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

The integrand crosses the axis at $$x = 0.5$$, $$3.5$$, and $$7.25$$, and those are exactly where $$g$$ turns: down to up at the first, up to down at the second, down to up again at the third. It has corners at $$x = 2$$ and $$x = 5$$, where its slope jumps from $$+2$$ to $$-2$$ and from $$-2$$ to $$+\tfrac43$$, and those are exactly where $$g$$ changes concavity.

Values of $$g$$ come from geometry, not from an antiderivative — the framework says as much, that a definite integral can sometimes be evaluated using areas. To get $$g(3.5)$$ with $$a = 0$$, cut the region at every axis crossing and add the pieces with their signs. From $$0$$ to $$0.5$$ the graph is a triangle below the axis with base $$0.5$$ and height $$1$$, contributing $$-\tfrac14$$. From $$0.5$$ to $$2$$ it is a triangle above the axis with base $$1.5$$ and height $$3$$, contributing $$\tfrac94$$. From $$2$$ to $$3.5$$ it is a triangle above the axis with base $$1.5$$ and height $$3$$ again, contributing another $$\tfrac94$$. Altogether

$$g(3.5) = -\tfrac14 + \tfrac94 + \tfrac94 = \tfrac{17}{4},$$

and no antiderivative of $$f$$ was ever written down. Cutting at the crossings is the part that gets skipped, and skipping it turns the first triangle from $$-\tfrac14$$ into $$+\tfrac14$$.

The signed areas of the three linear pieces are $$2$$, $$0$$, and $$-3$$. The middle one being zero is worth pausing on: $$f$$ is not zero on $$[2,5]$$ and $$g$$ is certainly not constant there, but the positive and negative parts cancel exactly, so $$g(5) = g(2)$$. A definite integral of zero says the accumulation returned to where it started, not that nothing happened.

## What the lower limit does, and does not do

Move $$a$$ and the entire graph of $$g$$ slides vertically. Not one marker moves.

The reason is one line of the framework's own properties of definite integrals — the integral over adjacent intervals adds:

$$\int_{a_2}^{x} f = \int_{a_2}^{a_1} f + \int_{a_1}^{x} f.$$

The first term on the right does not involve $$x$$. So changing the lower limit from $$a_1$$ to $$a_2$$ adds a constant to $$g$$, and a constant has no derivative, which is why $$g'$$, $$g''$$, and every feature they control are untouched.

One thing does change: the value. With $$a = 0$$ the maximum of $$g$$ is $$\tfrac{17}{4}$$ at $$x = 3.5$$; with $$a = 2$$ the same maximum, at the same place, is $$\tfrac94$$. And $$g(a) = 0$$ always, because the integral from a point to itself is zero — which also means the zeros of $$g$$ move when $$a$$ does, while its extrema do not.

## Below the lower limit

If $$x < a$$ the integral runs backwards, and reversing the limits reverses the sign:

$$\int_a^x f = -\int_x^a f.$$

So $$g$$ is defined to the left of $$a$$ too, and the translation table still holds there without modification — $$g$$ still rises where $$f$$ is positive. It is worth checking that on the tool by putting $$a$$ to the right of $$x$$, because the sign flip feels as though it ought to reverse something, and it does not.

<div class="article-note" markdown="1">
On a free-response question the graph of $$f$$ is given and $$g$$ is defined in the stem, and the parts almost always run in this order: a value of $$g$$, then $$g'$$ or a statement about increase, then $$g''$$ or a statement about concavity, then a justification. Each part is one line of the table above. Write $$g' = f$$ and $$g'' = f'$$ at the top of the page before reading part (a), and the rest of the question is arithmetic on a picture.
</div>
