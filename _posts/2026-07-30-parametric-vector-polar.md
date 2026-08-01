---
layout: post
title: "Parametric, vector, and polar: three systems, one calculus"
date: 2026-07-30
description: "Unit 9 introduces three new ways to describe a curve and no new calculus. The framework says so three times, and everything in the unit follows from dividing one derivative by another."
course: "AP Calculus BC"
read_time: "9 min read"
math: true
kind: foundations
sequence: 28
interactive: true
blurb: "Three notations, one chain rule, and one thing to watch"
---

The last unit of BC looks like three new topics. Read its essential knowledge and the same sentence appears three times in slightly different clothes: methods for calculating derivatives of real-valued functions can be extended to parametric functions, methods for calculating derivatives of real-valued functions can be extended to functions in polar coordinates, and the concept of calculating areas in rectangular coordinates can be extended to polar coordinates.

Three statements of the same claim. There is no new calculus in Unit 9. There is new bookkeeping, and it is worth being careful about.

## Everything is parametric

A parametric curve is a pair of functions $$x(t)$$ and $$y(t)$$. A vector-valued function $$\langle x(t), y(t)\rangle$$ is the same pair with different notation. And a polar curve $$r = f(\theta)$$ becomes the pair

$$x = f(\theta)\cos\theta, \qquad y = f(\theta)\sin\theta,$$

which is parametric with $$\theta$$ as the parameter. So one set of rules covers all three, and the rest of this article is that set.

The slope of the tangent line comes from [the chain rule](/2026/07/30/chain-rule-reading-the-layers.html), and the framework states it with its hypothesis attached: $$\tfrac{dy}{dx}$$ can be determined by dividing $$\tfrac{dy}{dt}$$ by $$\tfrac{dx}{dt}$$, provided $$\tfrac{dx}{dt}$$ does not equal zero.

$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt}.$$

The velocity of a particle following the curve is the vector $$\langle x'(t), y'(t)\rangle$$, and its speed is the length of that vector:

$$\text{speed} = \sqrt{\big(x'(t)\big)^2 + \big(y'(t)\big)^2}.$$

Distance travelled is the accumulated speed, $$\textstyle\int_a^b \sqrt{(x')^2+(y')^2}\,dt$$, which is also the arc length of the curve when the particle does not retrace its path.

The framework introduces this by pointing back: as with [particle motion on a line](/2026/07/30/particle-motion.html), the work is deciding which procedure a scenario needs. The distinctions carry over unchanged and gain a dimension. Velocity is a vector and speed is its length, so speed is again the unsigned quantity. Displacement over $$[a,b]$$ is the vector $$\langle x(b)-x(a),\, y(b)-y(a)\rangle$$ and needs only the endpoints; distance travelled is the integral above and needs the whole path. A particle that returns to where it started has zero displacement and a positive distance, in the plane exactly as on the line.

## The one that catches people

The second derivative is where the bookkeeping bites, and the framework's own guidance says why: $$\tfrac{dy}{dx}$$ is in terms of $$t$$, so students must be particularly careful when determining $$\tfrac{d^2y}{dx^2}$$.

It is not $$\tfrac{y''(t)}{x''(t)}$$. It is the derivative of the slope with respect to $$x$$, and the slope is a function of $$t$$, so the same division has to happen again:

$$\frac{d^2y}{dx^2} = \frac{\dfrac{d}{dt}\!\left[\dfrac{dy}{dx}\right]}{\dfrac{dx}{dt}}.$$

Differentiate the slope with respect to the parameter, then divide by $$\tfrac{dx}{dt}$$ one more time. On the circle $$x = 3\cos t$$, $$y = 3\sin t$$ the slope is $$-\cot t$$ and the second derivative works out to $$-\tfrac{1}{3\sin^3 t}$$, which is $$-\tfrac{9}{y^3}$$ — exactly what [implicit differentiation](/2026/07/30/implicit-differentiation.html) gives for $$x^2+y^2=9$$. Two routes, one curve, one answer.

## One tool for all three

<div class="viz" markdown="0">
  <div class="viz-controls" id="pv-fns"></div>
  <canvas id="pv-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <label for="pv-t" id="pv-tlab">t</label>
    <input type="range" id="pv-t" min="0" max="1200" step="1" value="180">
  </div>
  <div class="pv-read" id="pv-read"></div>
  <p class="viz-caption">Five curves, the last two given in polar form and converted to a parameter pair before anything is computed. The arrow at the moving point is the velocity vector; its length is the speed, drawn to scale, and its direction is the direction of travel. The pale line through the point is the tangent, whose slope is the panel's dy/dx. Where the arrow points straight up or down the tangent is vertical and dx/dt is zero, and the panel refuses to divide rather than printing a number.</p>
  <style>
    .pv-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .pv-read .pv-lab{color:var(--muted);display:inline-block;min-width:12.5rem}
    .pv-read .pv-val{font-weight:700;display:inline-block;min-width:8rem}
    .pv-read .pv-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('pv-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var SIDE=286, TOPP=18, CX0=(W-SIDE)/2;
  var sin=Math.sin, cos=Math.cos, PI=Math.PI;

  // Polar entries carry r(θ); the pair (x, y) is built from it, so nothing in
  // the panel is computed by a rule specific to polar coordinates.
  // Ranges put every parameter the article names on an integer slider step:
  // t = 0, π/2, π at 0, 300, 600 on the circle; t = −1, 0, 1 at 200, 600, 1000
  // on the cubic.
  var E=[
    { n:'x = 3cos t,  y = 3sin t', lab:'t', lo:0, hi:2*PI, w:4.2,
      x:function(t){ return 3*cos(t); }, y:function(t){ return 3*sin(t); },
      note:'a circle traced at constant speed 3' },
    { n:'x = 3cos t,  y = 2sin t', lab:'t', lo:0, hi:2*PI, w:4.2,
      x:function(t){ return 3*cos(t); }, y:function(t){ return 2*sin(t); },
      note:'an ellipse: same path shape, speed no longer constant' },
    { n:'x = t² − 1,  y = t³ − t', lab:'t', lo:-1.5, hi:1.5, w:2.4,
      x:function(t){ return t*t-1; }, y:function(t){ return t*t*t-t; },
      note:'passes through the origin twice, at t = −1 and t = 1, with different slopes' },
    { n:'r = 1 + cos θ', lab:'θ', lo:0, hi:2*PI, w:2.6, polar:true,
      r:function(a){ return 1+cos(a); },
      note:'a cardioid; area (1/2)∫r²dθ = 3π/2 and total length 8' },
    { n:'r = 2cos 3θ', lab:'θ', lo:0, hi:PI, w:2.6, polar:true,
      r:function(a){ return 2*cos(3*a); },
      note:'a three-petalled rose, traced once as θ runs from 0 to π' }
  ];
  E.forEach(function(e){
    if(e.polar){ e.x=function(a){ return e.r(a)*cos(a); };
                 e.y=function(a){ return e.r(a)*sin(a); }; }
  });
  var k=0;
  function G(){ return E[k]; }
  function px(u){ return CX0+(u+G().w)/(2*G().w)*SIDE; }
  function py(v){ return TOPP+SIDE-(v+G().w)/(2*G().w)*SIDE; }
  function fmt(v){ if(!isFinite(v)) return '—';
    var a=Math.abs(v); if(a<1e-12) return (0).toFixed(4);
    if(a>=1e5) return v.toExponential(4); return v.toFixed(4); }
  // central differences on the parameter, so every quantity below comes from
  // the same two functions x(t) and y(t) and nothing else
  function d1(f,t){ var h=1e-5; return (f(t+h)-f(t-h))/(2*h); }
  function slope(t){ var g=G(); return d1(g.y,t)/d1(g.x,t); }

  var bar=$('pv-fns');
  E.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  function draw(){
    var g=G(), t=g.lo+(+$('pv-t').value)/1200*(g.hi-g.lo);
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    $('pv-tlab').textContent=g.lab;
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(CX0,TOPP,SIDE,SIDE); c.clip();

    c.strokeStyle=LINE; c.lineWidth=1;
    var i;
    for(i=Math.ceil(-g.w);i<=g.w;i++){
      c.beginPath(); c.moveTo(px(i),TOPP); c.lineTo(px(i),TOPP+SIDE); c.stroke();
      c.beginPath(); c.moveTo(CX0,py(i)); c.lineTo(CX0+SIDE,py(i)); c.stroke(); }
    c.strokeStyle=PALE; c.lineWidth=1.4;
    c.beginPath(); c.moveTo(px(0),TOPP); c.lineTo(px(0),TOPP+SIDE); c.stroke();
    c.beginPath(); c.moveTo(CX0,py(0)); c.lineTo(CX0+SIDE,py(0)); c.stroke();

    c.strokeStyle=INK; c.lineWidth=2.2; c.beginPath();
    for(i=0;i<=900;i++){ var u=g.lo+(g.hi-g.lo)*i/900;
      if(i===0) c.moveTo(px(g.x(u)),py(g.y(u))); else c.lineTo(px(g.x(u)),py(g.y(u))); }
    c.stroke();

    var X=g.x(t), Y=g.y(t), vx=d1(g.x,t), vy=d1(g.y,t), sp=Math.hypot(vx,vy);
    // the ray from the origin, for the polar entries
    if(g.polar){ c.strokeStyle=PALE; c.lineWidth=1.2; c.setLineDash([4,3]);
      c.beginPath(); c.moveTo(px(0),py(0)); c.lineTo(px(X),py(Y)); c.stroke(); c.setLineDash([]); }
    // the tangent line
    if(sp>1e-9){ var ux=vx/sp, uy=vy/sp, R=0.7*g.w;
      c.strokeStyle=FAINT; c.lineWidth=1.4; c.setLineDash([5,4]);
      c.beginPath(); c.moveTo(px(X-R*ux),py(Y-R*uy)); c.lineTo(px(X+R*ux),py(Y+R*uy));
      c.stroke(); c.setLineDash([]); }
    // the velocity vector, to scale
    var s=0.22;
    c.strokeStyle=INK; c.lineWidth=2.2;
    c.beginPath(); c.moveTo(px(X),py(Y)); c.lineTo(px(X+s*vx),py(Y+s*vy)); c.stroke();
    if(sp>1e-9){ var a=Math.atan2(py(Y+s*vy)-py(Y), px(X+s*vx)-px(X)), L=8;
      c.beginPath();
      c.moveTo(px(X+s*vx),py(Y+s*vy));
      c.lineTo(px(X+s*vx)-L*Math.cos(a-0.4), py(Y+s*vy)-L*Math.sin(a-0.4));
      c.moveTo(px(X+s*vx),py(Y+s*vy));
      c.lineTo(px(X+s*vx)-L*Math.cos(a+0.4), py(Y+s*vy)-L*Math.sin(a+0.4));
      c.stroke(); }
    c.fillStyle=INK; c.beginPath(); c.arc(px(X),py(Y),4.5,0,6.284); c.fill();
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText(g.n, CX0, TOPP-6);

    var vert = Math.abs(vx) < 1e-9*(Math.abs(vx)+Math.abs(vy));
    var m = vert ? null : vy/vx;
    var m2 = vert ? null : d1(slope,t)/vx;
    function row(l,v,n){ return '<div><span class="pv-lab">'+l+'</span>'+
      '<span class="pv-val">'+v+'</span>'+(n?'<span class="pv-note">'+n+'</span>':'')+'</div>'; }
    $('pv-read').innerHTML =
      row(g.lab, fmt(t), g.polar ? 'r = '+fmt(g.r(t)) : '') +
      row('(x, y)', '('+fmt(X)+', '+fmt(Y)+')', '') +
      row('dx/d'+g.lab+',  dy/d'+g.lab, fmt(vx)+',  '+fmt(vy), '') +
      row('dy/dx', vert ? '—' : fmt(m),
          vert ? 'undefined, because dx/d'+g.lab+' is zero: the tangent is vertical' : '') +
      row('d²y/dx²', vert ? '—' : fmt(m2),
          vert ? 'undefined for the same reason' : (m2>0?'concave up here':'concave down here')) +
      row('speed', fmt(sp), g.note);
  }
  $('pv-t').addEventListener('input',draw);
  draw();
})();
</script>

Nothing in that panel is computed by a rule belonging to any one system. Every row comes from $$x(t)$$ and $$y(t)$$ and their derivatives, and the polar curves reach it by being converted first.

Two things repay watching. On the circle the arrow has constant length and the speed reads 3 at every position, while on the ellipse the same-looking path has an arrow that stretches and shrinks — a reminder that a parametrisation carries more information than a curve does. And on the third preset the point passes through the origin twice, at $$t = -1$$ and $$t = 1$$, with slopes $$-1$$ and $$+1$$. One point of the plane, two tangent lines, because they happen at different times.

## Polar area is the extension the framework promised

The area formula for a polar region is the one genuinely new-looking result, and the framework files it under the same heading as everything else: the concept of calculating areas in rectangular coordinates can be extended to polar coordinates.

$$A = \frac12\int_{\alpha}^{\beta} \big(f(\theta)\big)^2\,d\theta.$$

The $$\tfrac12 r^2$$ is the area of a circular sector of angle $$d\theta$$, so the integral is a sum of thin wedges in exactly the way an ordinary area integral is a sum of thin rectangles. For the cardioid $$r = 1+\cos\theta$$ over a full turn it gives $$\tfrac{3\pi}{2}$$, and for the three-petalled rose $$r = 2\cos 3\theta$$ over $$[0,\pi]$$ it gives $$\pi$$.

Arc length behaves the same way. Substituting the conversion into $$\sqrt{(x')^2+(y')^2}$$ and simplifying leaves $$\sqrt{r^2 + (r')^2}$$, which is the polar arc length formula and is not a separate fact. The cardioid's total length is exactly 8.

<div class="article-note" markdown="1">
The framework's warning for this unit is about notation, and it is specific: be careful about the variable of differentiation, and pay attention to subscripts when a problem involves more than one particle. Both are bookkeeping failures rather than calculus failures, which is the theme of the whole unit. Write the parameter on every derivative — $$\tfrac{dx}{dt}$$ and not $$x'$$ — and the second-derivative mistake becomes hard to make, because $$\tfrac{d}{dt}$$ and $$\tfrac{d}{dx}$$ stop looking alike.
</div>
