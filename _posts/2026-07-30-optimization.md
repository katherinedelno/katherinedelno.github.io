---
layout: post
title: "Optimization, and the step that is not calculus"
date: 2026-07-30
description: "Optimization problems depend on a correct objective, constraint, and domain before the derivative is ever used."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "7 min read"
math: true
kind: mechanics
sequence: 19
interactive: true
blurb: "Optimization problems depend on a correct objective, constraint, and domain before the derivative is ever used"
image: "/assets/og/optimization.png"
---

Optimization problems often look different because the stories are different. A fence, an open box, and a shortest-distance problem can all have the same mathematical structure. The derivative usually comes late, and the setup comes first.

## The structure of an optimization problem

Most problems require four pieces.

1. A quantity to optimize.
2. A constraint relating the variables.
3. A domain for the remaining variable.
4. A method for locating and comparing candidate extrema.

The first three steps are usually where the real decisions are made. The domain is especially important because it often comes from the context rather than from the algebra alone.

## Three examples with the same structure

<div class="viz" markdown="0">
  <div class="viz-controls" id="op-fns"></div>
  <canvas id="op-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="op-x" id="op-xlab">x</label>
    <input type="range" id="op-x" min="0" max="1200" step="1" value="600">
  </div>
  <div class="op-read" id="op-read"></div>
  <p class="viz-caption">On the left, the situation, redrawn as the free variable moves. On the right, the quantity being optimized plotted against that variable, with the feasible domain shaded and the candidates marked: filled dots for critical points, bars at the ends for endpoints. The panel carries the constraint, the objective, the domain, and every candidate with its value, which together are the whole write-up. The third problem has no endpoints at all, and its panel says so.</p>
  <style>
    .op-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .op-read .op-lab{color:var(--muted);display:inline-block;min-width:11rem}
    .op-read .op-val{font-weight:700;display:inline-block;min-width:9rem}
    .op-read .op-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('op-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var LW=250, GX=LW+52, GR=W-18, TOP=22, BOT=H-30;   // left panel, then the graph

  var P=[
    { n:'a fence against a river', xlab:'x, the width in metres',
      lo:0, hi:50, plo:0, phi:50, ylo:-60, yhi:1420,
      obj:function(x){ return x*(100-2*x); },
      unit:'square metres', oname:'A(x) = x(100 − 2x)',
      cons:'2x + y = 100', other:function(x){ return 'y = '+(100-2*x).toFixed(4)+' m'; },
      crit:[25], ends:[0,50], dom:'0 ≤ x ≤ 50', endnote:'',
      draw:function(x){
        var y=100-2*x, s=170/100, ox=42, oy=210;
        c.strokeStyle=INK; c.lineWidth=3;                    // the river bank
        c.beginPath(); c.moveTo(ox-14,oy); c.lineTo(ox+120,oy); c.stroke();
        c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
        c.fillText('river', ox-14, oy+15);
        var wpx=y*s*0.72, hpx=x*s*0.9;
        c.strokeStyle=FAINT; c.lineWidth=2;
        c.beginPath();
        c.moveTo(ox,oy); c.lineTo(ox,oy-hpx); c.lineTo(ox+wpx,oy-hpx); c.lineTo(ox+wpx,oy);
        c.stroke();
        c.fillStyle=MUTED; c.font='700 10px '+FONT;
        c.textAlign='right'; c.fillText('x', ox-4, oy-hpx/2);
        c.textAlign='center'; c.fillText('y', ox+wpx/2, oy-hpx-6);
      } },
    { n:'a box from a 12 by 12 sheet', xlab:'x, the corner cut in inches',
      lo:0, hi:6, plo:0, phi:6, ylo:-8, yhi:145,
      obj:function(x){ return x*(12-2*x)*(12-2*x); },
      unit:'cubic inches', oname:'V(x) = x(12 − 2x)²',
      cons:'base side = 12 − 2x', other:function(x){ return 'base = '+(12-2*x).toFixed(4)+' in'; },
      crit:[2,6], ends:[0,6], dom:'0 ≤ x ≤ 6',
      endnote:'x = 6 is a critical point and an endpoint at once',
      draw:function(x){
        var s=13, ox=54, oy=48, side=12*s, cut=x*s;
        c.strokeStyle=FAINT; c.lineWidth=2;
        c.strokeRect(ox,oy,side,side);
        c.strokeStyle=PALE; c.lineWidth=1.4;
        [[0,0],[1,0],[0,1],[1,1]].forEach(function(q){
          var px=ox+q[0]*(side-cut), py=oy+q[1]*(side-cut);
          c.strokeRect(px,py,cut,cut); });
        c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
        c.fillText('12 in', ox+side/2, oy+side+14);
        c.textAlign='left'; c.fillText('x', ox+2, oy-4);
      } },
    { n:'the closest point on y = x²', xlab:'x, the point on the curve',
      lo:-2.2, hi:2.2, plo:-2.2, phi:2.2, ylo:1.1, yhi:5.4,
      obj:function(x){ return x*x+(x*x-2)*(x*x-2); },
      unit:'squared units', oname:'D²(x) = x² + (x² − 2)²',
      cons:'the point is (x, x²)', other:function(x){ return 'distance = '+Math.sqrt(x*x+(x*x-2)*(x*x-2)).toFixed(4); },
      crit:[-Math.sqrt(1.5),0,Math.sqrt(1.5)], ends:[], dom:'all real x',
      endnote:'no endpoints, so the Candidates Test does not apply',
      draw:function(x){
        var ox=128, oy=214, s=44;
        function qx(u){ return ox+u*s; } function qy(v){ return oy-v*s; }
        c.strokeStyle=LINE; c.lineWidth=1;
        c.beginPath(); c.moveTo(qx(-2.4),qy(0)); c.lineTo(qx(2.4),qy(0)); c.stroke();
        c.strokeStyle=FAINT; c.lineWidth=2; c.beginPath();
        for(var i=0;i<=200;i++){ var u=-2.2+4.4*i/200;
          if(i===0) c.moveTo(qx(u),qy(u*u)); else c.lineTo(qx(u),qy(u*u)); }
        c.stroke();
        c.strokeStyle=INK; c.lineWidth=1.6;
        c.beginPath(); c.moveTo(qx(0),qy(2)); c.lineTo(qx(x),qy(x*x)); c.stroke();
        c.fillStyle=INK;
        c.beginPath(); c.arc(qx(0),qy(2),4,0,6.284); c.fill();
        c.beginPath(); c.arc(qx(x),qy(x*x),4,0,6.284); c.fill();
        c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='right';
        c.fillText('(0, 2)', qx(0)-7, qy(2)+3);
      } }
  ];
  var k=0;
  function G(){ return P[k]; }
  function gx(x){ var g=G(); return GX+(x-g.plo)/(g.phi-g.plo)*(GR-GX); }
  function gy(y){ var g=G(); return BOT-(y-g.ylo)/(g.yhi-g.ylo)*(BOT-TOP); }
  function fmt(v){ return Math.abs(v)<1e-12 ? (0).toFixed(4) : v.toFixed(4); }

  var bar=$('op-fns');
  P.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  function draw(){
    var g=G(), x=g.lo+(+$('op-x').value)/1200*(g.hi-g.lo);
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    $('op-xlab').textContent=g.xlab;
    c.clearRect(0,0,W,H);

    c.save(); c.beginPath(); c.rect(0,0,LW,H); c.clip(); g.draw(x); c.restore();
    c.save(); c.beginPath(); c.rect(GX-24,TOP-8,GR-GX+30,BOT-TOP+16); c.clip();

    // the feasible domain, shaded
    c.fillStyle=LINE;
    c.fillRect(gx(g.lo),TOP,gx(g.hi)-gx(g.lo),BOT-TOP);
    c.strokeStyle=PALE; c.lineWidth=1;
    if(g.ylo<0&&g.yhi>0){ c.beginPath(); c.moveTo(GX,gy(0)); c.lineTo(GR,gy(0)); c.stroke(); }

    c.strokeStyle=INK; c.lineWidth=2; c.beginPath();
    for(var i=0;i<=600;i++){ var u=g.plo+(g.phi-g.plo)*i/600;
      if(i===0) c.moveTo(gx(u),gy(g.obj(u))); else c.lineTo(gx(u),gy(g.obj(u))); }
    c.stroke();

    g.ends.forEach(function(e){
      c.strokeStyle=INK; c.lineWidth=2.4;
      c.beginPath(); c.moveTo(gx(e),gy(g.obj(e))-7); c.lineTo(gx(e),gy(g.obj(e))+7); c.stroke(); });
    g.crit.forEach(function(cc){
      c.fillStyle=INK; c.beginPath(); c.arc(gx(cc),gy(g.obj(cc)),4.5,0,6.284); c.fill(); });

    c.strokeStyle=FAINT; c.lineWidth=1; c.setLineDash([4,3]);
    c.beginPath(); c.moveTo(gx(x),TOP); c.lineTo(gx(x),BOT); c.stroke(); c.setLineDash([]);
    c.fillStyle=FAINT; c.beginPath(); c.arc(gx(x),gy(g.obj(x)),4,0,6.284); c.fill();
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText(g.oname, GX-24, TOP-10);

    // candidates, in increasing x, tagged by what makes each one a candidate
    var cand=[];
    g.crit.forEach(function(v){ cand.push([v,'critical point']); });
    g.ends.forEach(function(v){ if(!g.crit.some(function(u){return Math.abs(u-v)<1e-9;}))
      cand.push([v,'endpoint']); });
    g.crit.forEach(function(v){ if(g.ends.some(function(u){return Math.abs(u-v)<1e-9;}))
      cand[cand.findIndex(function(p){return p[0]===v;})][1]='critical point and endpoint'; });
    cand.sort(function(a,b){ return a[0]-b[0]; });
    var best=null;
    cand.forEach(function(p){ var v=g.obj(p[0]);
      if(best===null || v>g.obj(best[0])) best=p; });
    var worst=null;
    cand.forEach(function(p){ var v=g.obj(p[0]);
      if(worst===null || v<g.obj(worst[0])) worst=p; });

    function row(l,v,n){ return '<div><span class="op-lab">'+l+'</span>'+
      '<span class="op-val">'+v+'</span>'+(n?'<span class="op-note">'+n+'</span>':'')+'</div>'; }
    var list=cand.map(function(p){
      return 'x = '+fmt(p[0])+' → '+fmt(g.obj(p[0]))+' ('+p[1]+')'; }).join('<br><span class="op-lab"></span>');
    $('op-read').innerHTML =
      row('the free variable', fmt(x), g.other(x)) +
      row('constraint', g.cons, '') +
      row('objective', fmt(g.obj(x)), g.unit) +
      row('domain', g.dom, g.endnote) +
      row('candidates', '', list) +
      row(k===2?'smallest candidate':'largest candidate',
          fmt(g.obj((k===2?worst:best)[0])),
          'at x = '+fmt((k===2?worst:best)[0]));
  }
  $('op-x').addEventListener('input',draw);
  draw();
})();
</script>

The visualization shows a physical or geometric setup beside the corresponding objective function. The feasible domain is marked, along with critical points and endpoints.

## A fenced region

Suppose three sides of a rectangle use 100 meters of fencing. Let $$x$$ be the width and $$y$$ the remaining side, so the constraint is $$2x+y=100$$ and $$y=100-2x$$. The area is

$$A(x)=x(100-2x)$$

The physical domain is $$0\le x\le50$$. Differentiating gives $$A'(x)=100-4x$$, so the interior critical point is $$x=25$$. Evaluating the area at the candidates gives $$A(0)=0,\; A(25)=1250,\; A(50)=0$$, so the maximum area is $$1250$$ square meters. The question asks for the area, not only the value of $$x$$.

## An open box

Suppose squares of side length $$x$$ are cut from the corners of a 12-by-12 sheet and the sides are folded upward. The volume is

$$V(x)=x(12-2x)^2$$

The geometry requires $$0\le x\le6$$. Differentiating gives $$V'(x)=12(x-2)(x-6)$$, so the candidates on the closed interval are $$x=0,\; x=2,\; x=6$$. The corresponding volumes are $$0,\; 128,\; 0$$, so the maximum volume is $$128$$.

## Distance to a curve

Now minimize the distance from $$(0,2)$$ to the parabola $$y=x^2$$. The squared distance is

$$D^2(x) = x^2+(x^2-2)^2 = x^4-3x^2+4$$

Because square root is increasing, minimizing $$D^2$$ also minimizes $$D$$. Differentiating gives $$\tfrac{d}{dx}D^2(x) = 2x(2x^2-3)$$, so the critical points are $$x=0$$ and $$x=\pm\sqrt{\tfrac32}$$. There is no closed bounded interval here, so there are no endpoints to check.

At $$x=0$$, we get $$D^2=4$$. At $$x=\pm\sqrt{\tfrac32}$$, we get $$D^2=\tfrac74$$. Therefore the minimum distance is $$D=\tfrac{\sqrt7}{2}$$, and the square-root shortcut has to be undone in the final answer because the problem asks for a distance.

## The Candidates Test

[For a continuous function on a closed interval](/2026/07/30/mean-value-and-extreme-value-theorems.html), absolute extrema can occur at interior critical points or endpoints. So the standard procedure is:

- find the critical points
- include the endpoints
- evaluate the objective at every candidate
- compare

A critical point is a point where the derivative is zero or [fails to exist](/2026/07/30/where-differentiability-fails.html). Finding one critical point is not enough, because it may be a local maximum, local minimum, or neither. On an open or unbounded domain, endpoint comparison may not be available, and then a derivative test, global argument, or analysis of end behavior may be needed.

## Answer the quantity that was asked for

Optimization problems often ask for a quantity different from the variable used during the calculus. A problem may ask for maximum area but require solving first for a width. It may ask for volume but require finding the cut size, or it may ask for distance while the simpler objective is squared distance. So the last step should return to the original question and state the requested quantity with appropriate units.

<div class="article-note" markdown="1">
A useful practice exercise is to set up several optimization problems without differentiating them. For each one, write only:

- the objective
- the constraint
- the domain

If those three lines are correct, the calculus that follows is usually routine.
</div>
