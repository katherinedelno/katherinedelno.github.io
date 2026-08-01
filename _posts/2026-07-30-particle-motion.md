---
layout: post
title: "Particle motion, and the two signs that decide everything"
date: 2026-07-30
description: "Position, velocity, and acceleration are one function and its first two derivatives. Speed is the one that is not a derivative, and it is where most of the errors are."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: foundations
sequence: 13
interactive: true
blurb: "Negative acceleration does not mean slowing down"
---

A particle moving on a line has a position $$s(t)$$, and everything else in the topic is a derivative of it. The course lists four quantities — position, speed, velocity, acceleration — and three of them are derivatives or the function itself. Speed is the odd one out, and that is where the errors are.

## One function and its first two derivatives

Velocity is the derivative of position, and acceleration is the derivative of velocity:

$$v(t) = s'(t), \qquad a(t) = v'(t) = s''(t).$$

Velocity is signed. Its sign is the direction of travel: positive means moving in the positive direction, negative means the other way, zero means momentarily at rest. Speed discards that information:

$$\text{speed} = \vert v(t)\vert.$$

Units follow the rule the framework states for every derivative — the unit of $$f'$$ is the unit of $$f$$ divided by the unit of its input. Position in metres and time in seconds gives velocity in metres per second, and differentiating again gives acceleration in metres per second per second. Nothing about motion is special here; it is [the same reading](/2026/07/21/reading-the-graph-of-f-prime.html) that any rate of change gets.

## Speeding up is a statement about two signs

Speeding up means the speed is increasing, so it is a question about the derivative of $$\vert v\vert$$. Wherever $$v(t) \neq 0$$, [the chain rule](/2026/07/30/chain-rule-reading-the-layers.html) gives

$$\frac{d}{dt}\,\vert v\vert = \frac{v}{\vert v\vert}\cdot a = \operatorname{sign}(v)\cdot a.$$

So the speed is increasing exactly when $$\operatorname{sign}(v)$$ and $$a$$ have the same sign — which is to say, when $$v$$ and $$a$$ do. That is the whole rule, and it is a one-line consequence rather than something to memorise. It is also why "the acceleration is negative, so it is slowing down" is wrong: negative acceleration slows a particle that is moving forward and speeds up one that is moving backward.

At $$v = 0$$ the derivative above does not exist, because $$\vert v\vert$$ has [a corner wherever $$v$$ crosses zero](/2026/07/30/where-differentiability-fails.html). At such an instant the particle is neither speeding up nor slowing down; it is turning around.

<div class="viz" markdown="0">
  <div class="viz-controls" id="pm-fns"></div>
  <canvas id="pm-cv" width="700" height="380"></canvas>
  <div class="viz-controls">
    <label for="pm-t">t</label>
    <input type="range" id="pm-t" min="0" max="1200" step="1" value="150">
  </div>
  <div class="pm-read" id="pm-read"></div>
  <p class="viz-caption">The bar at the top is the track: the dot is where the particle actually is, and the pale trail behind it is everywhere it has been up to the current time. Below are s, v, and a on a shared time axis with a cursor at the current instant. The panel gives all four quantities and then the verdict, which is decided by comparing two signs and nothing else. The first function visits all four combinations of those signs in four seconds, which is why it is the one every textbook uses.</p>
  <style>
    .pm-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .pm-read .pm-lab{color:var(--muted);display:inline-block;min-width:11rem}
    .pm-read .pm-val{font-weight:700;display:inline-block;min-width:6.5rem}
    .pm-read .pm-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('pm-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=44, PADR=16, TRK=40, P0=64, PH=98;   // three panes of height PH from y = P0

  // T is chosen so every time the article names lands on an integer slider step:
  // t = 1, 2, 3 at 300/600/900; t = 3 at 600 on the projectile; pi/6 at 100.
  var F=[
    { n:'s = t³ − 6t² + 9t', T:4, slo:-0.6, shi:4.6, vlo:-3.6, vhi:9.6, alo:-13, ahi:13,
      s:function(t){ return t*t*t-6*t*t+9*t; },
      v:function(t){ return 3*t*t-12*t+9; },
      a:function(t){ return 6*t-12; } },
    { n:'s = 30t − 5t²', T:6, slo:-4, shi:50, vlo:-32, vhi:32, alo:-14, ahi:14,
      s:function(t){ return 30*t-5*t*t; },
      v:function(t){ return 30-10*t; },
      a:function(t){ return -10; } },
    { n:'s = t + 2cos t', T:2*Math.PI, slo:-0.4, shi:8.6, vlo:-1.3, vhi:3.3, alo:-2.4, ahi:2.4,
      s:function(t){ return t+2*Math.cos(t); },
      v:function(t){ return 1-2*Math.sin(t); },
      a:function(t){ return -2*Math.cos(t); } }
  ];
  var k=0;
  function G(){ return F[k]; }
  function fmt(v){ var x=Math.abs(v);
    if(x<1e-12) return (0).toFixed(4);
    return v.toFixed(4); }
  function tx(t){ var g=G(); return PADL+t/g.T*(W-PADL-PADR); }
  function sx(v){ var g=G(); return PADL+(v-g.slo)/(g.shi-g.slo)*(W-PADL-PADR); }

  var bar=$('pm-fns');
  F.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  function pane(idx,f,lo,hi,label,tnow){
    var g=G(), y0=P0+idx*PH, y1=y0+PH-14;
    function py(u){ return y1-(u-lo)/(hi-lo)*(y1-y0); }
    c.strokeStyle=LINE; c.lineWidth=1;
    c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke();
    c.strokeStyle=INK; c.lineWidth=1.8; c.beginPath();
    for(var i=0;i<=700;i++){ var t=g.T*i/700, u=f(t);
      if(i===0) c.moveTo(tx(t),py(u)); else c.lineTo(tx(t),py(u)); }
    c.stroke();
    c.strokeStyle=FAINT; c.lineWidth=1.2; c.setLineDash([4,3]);
    c.beginPath(); c.moveTo(tx(tnow),y0); c.lineTo(tx(tnow),y1); c.stroke(); c.setLineDash([]);
    c.fillStyle=INK; c.beginPath(); c.arc(tx(tnow),py(f(tnow)),3.6,0,6.284); c.fill();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText(label,4,y0+9);
  }

  function draw(){
    var g=G(), t=(+$('pm-t').value)/1200*g.T;
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);

    // the track, with the trail of everywhere the particle has been
    c.strokeStyle=LINE; c.lineWidth=1;
    c.beginPath(); c.moveTo(PADL,TRK); c.lineTo(W-PADR,TRK); c.stroke();
    c.strokeStyle=PALE; c.lineWidth=5; c.lineCap='round';
    var N=600, i, u;
    for(i=0;i<N;i++){ var t0=t*i/N, t1=t*(i+1)/N;
      c.beginPath(); c.moveTo(sx(g.s(t0)),TRK); c.lineTo(sx(g.s(t1)),TRK); c.stroke(); }
    c.lineCap='butt';
    c.strokeStyle=FAINT; c.lineWidth=1;
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    var step = (g.shi-g.slo)>20 ? 10 : 1;
    for(u=Math.ceil(g.slo/step)*step; u<=g.shi; u+=step){
      c.beginPath(); c.moveTo(sx(u),TRK-4); c.lineTo(sx(u),TRK+4); c.stroke();
      c.fillText(String(u),sx(u),TRK+16);
    }
    c.fillStyle=INK; c.beginPath(); c.arc(sx(g.s(t)),TRK,6,0,6.284); c.fill();
    c.textAlign='left'; c.fillStyle=MUTED; c.font='700 10px '+FONT;
    c.fillText('position on the track',4,TRK-14);

    pane(0,g.s,g.slo,g.shi,'s',t);
    pane(1,g.v,g.vlo,g.vhi,'v',t);
    pane(2,g.a,g.alo,g.ahi,'a',t);

    var S=g.s(t), V=g.v(t), A=g.a(t), SP=Math.abs(V);
    var rest = Math.abs(V) < 1e-9;
    var dir  = rest ? 'momentarily at rest' : (V>0 ? 'moving in the positive direction'
                                                   : 'moving in the negative direction');
    var verdict;
    if(rest) verdict='turning around &mdash; speed is not differentiable here';
    else if(Math.abs(A)<1e-12) verdict='neither &mdash; the acceleration is zero';
    else if(V*A>0) verdict='speeding up &mdash; v and a have the same sign';
    else verdict='slowing down &mdash; v and a have opposite signs';

    function row(l,v,n){ return '<div><span class="pm-lab">'+l+'</span>'+
      '<span class="pm-val">'+v+'</span>'+(n?'<span class="pm-note">'+n+'</span>':'')+'</div>'; }
    $('pm-read').innerHTML =
      row('t', fmt(t), '') +
      row('position  s(t)', fmt(S), '') +
      row('velocity  v(t)', fmt(V), dir) +
      row('acceleration  a(t)', fmt(A), '') +
      row('speed  |v(t)|', fmt(SP), verdict);
  }
  $('pm-t').addEventListener('input',draw);
  draw();
})();
</script>

On the first function the velocity is $$3(t-1)(t-3)$$ and the acceleration is $$6t - 12$$, so the signs change at $$t = 1$$, $$t = 2$$, and $$t = 3$$. Those three instants cut $$[0,4]$$ into four intervals, and each one is a different combination: right and slowing, left and speeding up, left and slowing, right and speeding up. Watch the track rather than the graphs and the particle goes out to 4, back to 0, and out to 4 again.

## The case where physical intuition fails

A ball thrown straight up at 30 metres per second, with gravity rounded to 10 for clean numbers, has position $$s(t) = 30t - 5t^2$$ in metres. Its acceleration is $$-10$$ metres per second per second at every instant of the flight — constant, negative, never changing.

It is slowing down for the first three seconds and speeding up for the last three. Nothing about the acceleration changed; the velocity did. On the way up $$v > 0$$ and $$a < 0$$, so the signs disagree and the speed falls. At the apex $$v = 0$$. On the way down $$v < 0$$ and $$a < 0$$, the signs agree, and the speed climbs back. A single constant acceleration produced both answers, which is the clearest argument there is against reading the sign of $$a$$ on its own.

## Displacement is not distance

Over $$[0,4]$$ the first particle ends at $$s(4) = 4$$ having started at $$s(0) = 0$$, so its displacement is 4. That is not how far it travelled. It turns around at $$t = 1$$ and $$t = 3$$, and its positions at $$t = 0, 1, 3, 4$$ are $$0, 4, 0, 4$$, so the distance covered is $$4 + 4 + 4 = 12$$.

Displacement is the net change in $$s$$ and needs only the endpoints. Distance needs the turning points, which means it needs the zeros of $$v$$, which is the reason a question asking for total distance is really a question about the sign of the velocity.

<div class="article-note" markdown="1">
Sign charts earn no credit on their own. The framework's exam guidance is explicit that a justification has to connect the work to a definition or a theorem, so a chart showing $$v < 0$$ and $$a < 0$$ on an interval is the evidence, not the answer. The sentence that scores says what the signs mean: the velocity and the acceleration are both negative on that interval, so the speed is increasing and the particle is speeding up.
</div>
