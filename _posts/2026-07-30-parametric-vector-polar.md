---
layout: post
title: "Parametric, vector, and polar: three systems, one calculus"
date: 2026-07-30
description: "Parametric, vector-valued, and polar curves use familiar derivative and integral ideas with a different way of describing position."
course: "AP Calculus BC"
read_time: "6 min read"
math: true
kind: foundations
sequence: 28
interactive: true
blurb: "Parametric, vector-valued, and polar curves use familiar derivative and integral ideas with a different way of describing position"
image: "/assets/og/parametric-vector-polar.png"
---

Parametric, vector-valued, and polar curves look like three separate topics, but they are closely related. In each case, a point in the plane is described by two coordinates that depend on another variable, and once that representation is clear, the usual ideas of derivative, speed, distance, area, and arc length continue to apply.

## Everything can be written parametrically

A parametric curve is given by $$x=x(t),\; y=y(t)$$, and a vector-valued function $$\langle x(t),y(t)\rangle$$ contains the same coordinate functions in vector notation. A polar curve $$r=f(\theta)$$ can be converted to $$x=f(\theta)\cos\theta,\; y=f(\theta)\sin\theta$$, so polar curves can also be treated parametrically, with $$\theta$$ as the parameter.

## Slope and motion

If $$\tfrac{dx}{dt}\neq0$$, then $$\tfrac{dy}{dx} = \tfrac{dy/dt}{dx/dt}$$. The velocity vector is $$\left\langle \tfrac{dx}{dt}, \tfrac{dy}{dt} \right\rangle$$, and its magnitude is the speed: $$\text{speed} = \sqrt{ \left(\tfrac{dx}{dt}\right)^2 + \left(\tfrac{dy}{dt}\right)^2 }$$. Distance traveled over $$[a,b]$$ is

$$\int_a^b \sqrt{ \left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 } \,dt$$

This is also the arc-length formula when the path is not retraced. Displacement depends only on the endpoints, $$\left\langle x(b)-x(a), y(b)-y(a) \right\rangle$$, and a particle can therefore [return to its starting point with zero displacement](/2026/07/30/particle-motion.html) while traveling a positive distance.

## The second derivative

The second derivative requires extra care because $$\tfrac{dy}{dx}$$ is still expressed as a function of the parameter. It is not $$\tfrac{y''(t)}{x''(t)}$$. Instead,

$$\frac{d^2y}{dx^2} = \frac{ \dfrac{d}{dt}\left(\dfrac{dy}{dx}\right) }{ \dfrac{dx}{dt} }$$

[Differentiate the first derivative with respect to the parameter](/2026/07/30/chain-rule-reading-the-layers.html), then divide by $$dx/dt$$ again. For the circle $$x=3\cos t,\; y=3\sin t$$, the first derivative is $$\tfrac{dy}{dx} = -\cot t$$ and the second derivative is $$-\tfrac{1}{3\sin^3t}$$. Since $$y=3\sin t$$, this can also be written as $$-\tfrac{9}{y^3}$$. [Implicit differentiation](/2026/07/30/implicit-differentiation.html) of $$x^2+y^2=9$$ gives the same result.

## One visualization, several coordinate systems

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

The panel shows several curves, including polar curves converted to coordinate pairs before the derivatives are computed. The arrow at the moving point is the velocity vector, whose length is the speed, and the tangent line uses $$dy/dx$$. Where $$dx/dt=0$$, the quotient for the slope is undefined and the tangent may be vertical.

The same point in the plane can also occur at more than one parameter value. If the curve passes through that point in different directions, the two visits can have different tangent lines, and a parametrization therefore contains information about how a curve is traversed, not only about the geometric path.

## Polar area

For a polar curve $$r=f(\theta)$$, the area swept from $$\alpha$$ to $$\beta$$ is

$$A = \frac12 \int_{\alpha}^{\beta} \big(f(\theta)\big)^2\,d\theta$$

The factor $$\tfrac12r^2$$ comes from the area of a thin circular sector, so the integral can be understood as a sum of narrow wedges, just as an ordinary area integral is built from narrow rectangles. For the cardioid $$r=1+\cos\theta$$ over a full revolution, the area is $$\tfrac{3\pi}{2}$$, and for the three-petalled rose $$r=2\cos3\theta$$ over $$[0,\pi]$$, the area is $$\pi$$.

## Polar arc length

Start with the parametric arc-length formula and substitute $$x=r\cos\theta,\; y=r\sin\theta$$, so that after simplification,

$$L = \int_{\alpha}^{\beta} \sqrt{ r^2+ \left(\frac{dr}{d\theta}\right)^2 } \,d\theta$$

For the cardioid $$r=1+\cos\theta$$, the total arc length is $$8$$. The formula is not disconnected from the parametric one, and it follows from it.

<div class="article-note" markdown="1">
The main practical issue in this unit is notation. Write the variable of differentiation explicitly when several variables are present, because the difference between $$\tfrac{d}{dt}$$ and $$\tfrac{d}{dx}$$ is doing real mathematical work.
</div>
