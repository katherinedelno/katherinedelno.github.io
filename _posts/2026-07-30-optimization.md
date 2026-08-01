---
layout: post
title: "Optimization, and the step that is not calculus"
date: 2026-07-30
description: "Every optimization problem has the same skeleton underneath a different story. The calculus is the short part, and the domain is where the marks are lost."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: mechanics
sequence: 19
interactive: true
blurb: "Setting up the function and its domain is most of the work"
---

The framework's suggested skill for the introductory optimization topic is to identify common underlying structures in problems involving different contextual situations. That is an unusual thing to ask of a calculus topic, and it is the right thing to ask of this one. Fences, boxes, and distances are the same problem wearing different clothes.

## The skeleton

Every one of these problems has four parts, in this order.

A quantity to optimize, named as a function. A constraint relating the variables, used to eliminate all but one of them. A domain for the surviving variable, forced by the situation rather than by the algebra. And only then the derivative.

The framework's statement of the topic is deliberately plain: the derivative can be used to solve optimization problems, that is, finding a minimum or maximum value of a function on a given interval. The interval is given. Working out what it is, is the third step, and it is the step that gets skipped.

This is the same translation problem [related rates](/2026/07/20/related-rates-translation-problem.html) poses, one unit later and in the other direction. There the prose hands you rates and asks for a rate; here it hands you a constraint and asks for an extreme value. Both stand or fall on getting a picture and a variable list onto paper before any calculus starts.

## Three stories, one structure

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

The fence and the box are the same problem. Each has a constraint that turns two variables into one, each produces a function on a closed interval, and in each the domain comes from geometry rather than algebra.

Notice where the two endpoints come from, because they come from different places. The left end is $$x = 0$$ in both, because a width and a cut cannot be negative. The right end is whatever value collapses the other dimension: for the fence, $$y = 100 - 2x$$ reaches zero at $$x = 50$$; for the box, the base side $$12 - 2x$$ reaches zero at $$x = 6$$. Neither number appears anywhere in the algebra of the objective. Both have to be read off the picture.

For the fence, $$2x + y = 100$$ gives $$A(x) = x(100-2x)$$ on $$[0,50]$$, with $$A'(x) = 100 - 4x$$ zero at $$x = 25$$. The candidates are $$0$$, $$25$$, and $$50$$, with areas $$0$$, $$1250$$, and $$0$$. For the box, $$V(x) = x(12-2x)^2$$ on $$[0,6]$$, and $$V'(x) = 12(x-2)(x-6)$$ is zero at $$x = 2$$ and $$x = 6$$. The candidates are $$0$$, $$2$$, and $$6$$, with volumes $$0$$, $$128$$, and $$0$$ — and $$x = 6$$ arrives twice, once as a critical point and once as an endpoint.

## The Candidates Test, and when it does not apply

The framework states it in one line: absolute extrema of a function on a closed interval can only occur at critical points or at endpoints. So on a closed interval the whole method is to list those points, evaluate, and compare. No derivative test is needed, because comparing the values settles it directly — and [the Extreme Value Theorem](/2026/07/30/mean-value-and-extreme-value-theorems.html) is what guarantees there is something to find, provided the objective is continuous on that interval.

Both parts of the definition of a critical point matter here. A critical point is where the derivative is zero *or* [fails to exist](/2026/07/30/where-differentiability-fails.html), and objectives built from absolute values or roots can have the second kind without having the first.

The third problem is the one that breaks the habit. Minimising the distance from $$(0,2)$$ to the parabola $$y = x^2$$ gives

$$D^2(x) = x^2 + (x^2-2)^2 = x^4 - 3x^2 + 4,$$

whose derivative $$2x(2x^2-3)$$ vanishes at $$x = 0$$ and $$x = \pm\sqrt{3/2}$$. There is no closed interval and there are no endpoints, so there is nothing to compare against. Evaluating anyway: $$D^2 = 4$$ at $$x = 0$$ and $$D^2 = \tfrac74$$ at the other two, so the minimum distance is $$\tfrac{\sqrt7}{2} \approx 1.3229$$, attained twice.

And $$x = 0$$ is a critical point that is a local *maximum* of the distance. A student who finds one critical point and stops has a defensible-looking answer of 2, which is wrong. Without endpoints to compare, the justification has to come from a derivative test, and here the second derivative $$6(2x^2-1)$$ is $$-6$$ at $$x = 0$$ and $$+12$$ at $$x = \pm\sqrt{3/2}$$, which settles all three at once.

## Answering the question that was asked

The suggested skill for the second optimization topic is to explain the meaning of mathematical solutions in context, which mostly means noticing what was asked for.

The fence question asks for the largest area, which is $$1250$$ square metres, not $$x = 25$$. The box question asks for the volume, $$128$$ cubic inches, not the cut. And the distance question asks for a distance, so the answer is $$\tfrac{\sqrt7}{2}$$, not $$\tfrac74$$ — minimising $$D^2$$ instead of $$D$$ is a legitimate shortcut, because the square root is increasing and preserves the location of the minimum, but the shortcut has to be undone before the answer is written down.

<div class="article-note" markdown="1">
The setup is worth practising apart from the calculus. Take a page of optimization problems and, for each one, write only three lines: the quantity being optimized, the constraint, and the domain with a reason for each end of it. Do not differentiate any of them. The differentiating is the part that already works, and separating the two makes it obvious how much of the difficulty lives in the first three lines.
</div>
