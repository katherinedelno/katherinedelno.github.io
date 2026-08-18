---
layout: post
title: "What a limit claims, and what it does not"
date: 2026-07-30
description: "A limit describes what happens near a point, not necessarily what happens at the point itself."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: foundations
sequence: 1
interactive: true
blurb: "A limit describes what happens near a point, not necessarily what happens at the point itself"
featured: true
image: "/assets/og/what-a-limit-claims.png"
---

A limit describes what a function does near a point. It does not, by itself, say what happens at the point.

That distinction is fundamental to calculus. A derivative is defined through a quotient that is not evaluated at the point where the two inputs coincide. A definite integral is defined through [a limit of approximating sums](/2026/07/25/riemann-sums-watching-rectangles.html). In both cases, we need language for describing what a quantity approaches without requiring it to reach that value during the approximation.

## Narrow the window

Choose a point $$a$$ and a width $$\delta$$. Look at every input within $$\delta$$ of $$a$$, except $$a$$ itself, and collect the corresponding outputs, then make $$\delta$$ smaller. If those outputs become arbitrarily close to a single number $$L$$, then

$$\lim_{x\to a} f(x)=L$$

The value $$f(a)$$ is not part of this test.

<div class="viz" markdown="0">
  <canvas id="lm-cv" width="700" height="330"></canvas>
  <div class="viz-controls">
    <button type="button" id="lm-f0" class="res-filter is-active" style="font-size:.72rem">A hole</button>
    <button type="button" id="lm-f1" class="res-filter" style="font-size:.72rem">A jump</button>
    <button type="button" id="lm-f2" class="res-filter" style="font-size:.72rem">Endless oscillation</button>
  </div>
  <div class="viz-controls">
    <label for="lm-d">Window &delta;</label>
    <input type="range" id="lm-d" min="-400" max="0" step="1" value="0">
    <span id="lm-vwrap"><label for="lm-v">Value at x = 2</label>
    <button type="button" id="lm-vu" class="res-filter is-active" style="font-size:.72rem">undefined</button>
    <button type="button" id="lm-v4" class="res-filter" style="font-size:.72rem">4</button>
    <button type="button" id="lm-v1" class="res-filter" style="font-size:.72rem">1</button></span>
  </div>
  <div class="viz-controls">
    <span class="viz-value" id="lm-read" style="min-width:100%"></span>
  </div>
  <p class="viz-caption">The shaded band is the window: every input within &delta; of 2, with the center itself punched out. The bar on the right is the set of outputs the function takes on that band, and its height is the number to watch. For the hole, the bar collapses toward a point at height 4 however small &delta; gets, and the marker at x = 2 can be set to 4, to 1, or removed entirely without the bar noticing. For the jump it sits at 3, the size of the gap, and never shrinks. For the oscillation it holds at 2 forever, because every window, however narrow, contains inputs sending the output to every value between −1 and 1.</p>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('lm-cv'), c=cv.getContext('2d');
  var read=document.getElementById('lm-read'), slD=document.getElementById('lm-d');
  var W=cv.width, H=cv.height;
  var d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f', MUTED='#5c5c5c', LINE='#e6e6e6', FAINT='#9a9a97', PALE='#d6d6d3',
      BAND='rgba(31,31,31,0.08)';
  var FONT='Hanken Grotesk, sans-serif';
  var A=2, mode=0, atPoint='u';
  var PADL=44, PADR=118, TOP=16, AXIS=H-40;
  var XLO=0.6, XHI=3.4, YLO=-1.6, YHI=5.8;
  function px(x){ return PADL+(x-XLO)/(XHI-XLO)*(W-PADL-PADR); }
  function py(y){ return AXIS-(y-YLO)/(YHI-YLO)*(AXIS-TOP); }
  function delta(){ return Math.pow(10, (+slD.value)/100); }

  // f(x) for x != 2 in each mode; the limit is a claim about these values only.
  function f(x){
    if(mode===0) return x+2;                      // (x^2-4)/(x-2) reduced
    if(mode===1) return x<A ? x+2 : x-1;          // left limit 4, right limit 1
    return Math.sin(1/(x-A));                     // no limit at all
  }
  var LIMIT=[4,null,null];

  // range of f on the punctured window, computed by sampling
  function outputRange(d){
    var lo=Infinity, hi=-Infinity, N=4000, i, x, y;
    for(i=1;i<=N;i++){
      x = A - d + (d)*(i/(N+1));                  // left half, excluding A
      y = f(x); if(y<lo) lo=y; if(y>hi) hi=y;
      x = A + d*(i/(N+1));                        // right half, excluding A
      y = f(x); if(y<lo) lo=y; if(y>hi) hi=y;
    }
    if(mode===2){ lo=-1; hi=1; }                  // exact: sin(1/u) fills [-1,1]
    return [lo,hi];
  }

  function draw(){
    var d=delta(), r=outputRange(d);
    c.clearRect(0,0,W,H);
    // window band
    c.fillStyle=BAND;
    c.fillRect(px(A-d), TOP, Math.max(1.2, px(A+d)-px(A-d)), AXIS-TOP);
    // axes
    c.strokeStyle=LINE; c.lineWidth=1;
    c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    for(var t=1;t<=3;t++){ c.fillText(String(t), px(t), AXIS+14); }
    c.textAlign='right';
    for(var v=0;v<=4;v+=2){ if(v) c.fillText(String(v), PADL-6, py(v)+3); }
    // the curve, drawn on each side separately so nothing is joined across x = 2
    c.strokeStyle=INK; c.lineWidth=2;
    [[XLO,A],[A,XHI]].forEach(function(seg){
      c.beginPath(); var started=false;
      var steps=mode===2?4000:600;
      for(var i=0;i<=steps;i++){
        var x=seg[0]+(seg[1]-seg[0])*i/steps;
        if(Math.abs(x-A)<1e-9) continue;
        var y=f(x);
        if(y<YLO-1||y>YHI+1){ started=false; continue; }
        started ? c.lineTo(px(x),py(y)) : (c.moveTo(px(x),py(y)), started=true);
      }
      c.stroke();
    });
    // the point itself
    if(mode===0){
      var yv = atPoint==='u' ? null : (atPoint==='4' ? 4 : 1);
      if(yv===null){
        c.strokeStyle=INK; c.lineWidth=2; c.fillStyle='#fff';
        c.beginPath(); c.arc(px(A),py(4),4.2,0,7); c.fill(); c.stroke();
      } else {
        c.fillStyle=INK; c.beginPath(); c.arc(px(A),py(yv),4.2,0,7); c.fill();
        if(yv!==4){
          c.strokeStyle=INK; c.lineWidth=2; c.fillStyle='#fff';
          c.beginPath(); c.arc(px(A),py(4),4.2,0,7); c.fill(); c.stroke();
        }
      }
    }
    // dashed line at the limit, where there is one
    if(LIMIT[mode]!==null){
      c.strokeStyle=FAINT; c.setLineDash([4,3]); c.lineWidth=1;
      c.beginPath(); c.moveTo(PADL,py(LIMIT[mode])); c.lineTo(W-PADR,py(LIMIT[mode])); c.stroke();
      c.setLineDash([]);
    }
    // the output bar
    var bx=W-PADR+30, w=16;
    c.fillStyle=FAINT; c.font='700 10px '+FONT; c.textAlign='center';
    c.fillText('OUTPUTS', bx+w/2, TOP+9);
    c.strokeStyle=LINE; c.strokeRect(bx+0.5, TOP+16.5, w, AXIS-TOP-16);
    var y1=py(Math.max(YLO,Math.min(YHI,r[1]))), y2=py(Math.max(YLO,Math.min(YHI,r[0])));
    c.fillStyle=INK; c.fillRect(bx, y1, w, Math.max(1.5, y2-y1));
    c.textAlign='left'; c.fillStyle=MUTED; c.font='700 10px '+FONT;
    c.fillText('height', bx+w+7, (y1+y2)/2-4);
    c.fillStyle=INK; c.font='700 12px '+FONT;
    c.fillText((r[1]-r[0]).toFixed(3), bx+w+7, (y1+y2)/2+10);

    var fmt = d<0.001 ? d.toExponential(1) : d.toFixed(4).replace(/0+$/,'').replace(/\.$/,'');
    var txt='window δ = '+fmt+'   outputs span ['+r[0].toFixed(4)+', '+r[1].toFixed(4)+
            '],  a height of '+(r[1]-r[0]).toFixed(4)+'.  ';
    txt += mode===0 ? 'Narrow it further and the height keeps falling: the limit is 4.'
         : mode===1 ? 'The height stalls at 3, the size of the jump. No single number is being approached.'
         : 'The height stays at 2 forever. No limit exists.';
    read.textContent=txt;
  }
  function setMode(m){
    mode=m;
    [0,1,2].forEach(function(i){
      document.getElementById('lm-f'+i).classList[i===m?'add':'remove']('is-active');
    });
    document.getElementById('lm-vwrap').style.visibility = m===0 ? 'visible' : 'hidden';
    draw();
  }
  function setAt(v){
    atPoint=v;
    [['u','lm-vu'],['4','lm-v4'],['1','lm-v1']].forEach(function(p){
      document.getElementById(p[1]).classList[p[0]===v?'add':'remove']('is-active');
    });
    draw();
  }
  document.getElementById('lm-f0').addEventListener('click',function(){ setMode(0); });
  document.getElementById('lm-f1').addEventListener('click',function(){ setMode(1); });
  document.getElementById('lm-f2').addEventListener('click',function(){ setMode(2); });
  document.getElementById('lm-vu').addEventListener('click',function(){ setAt('u'); });
  document.getElementById('lm-v4').addEventListener('click',function(){ setAt('4'); });
  document.getElementById('lm-v1').addEventListener('click',function(){ setAt('1'); });
  slD.addEventListener('input', draw);
  setMode(0);
})();
</script>

The shaded band shows every input within $$\delta$$ of 2, with the center removed. The bar on the right shows the range of output values over that band.

For the hole, the output range collapses toward 4 as the window narrows, and the value at $$x=2$$ can be 4, 1, or undefined without changing that behavior. For the jump, the output range never collapses to a single value because the two sides approach different heights. For the oscillating example, every sufficiently small window still produces outputs throughout the interval from $$-1$$ to $$1$$.

Start with the hole. The function is $$f(x)=\tfrac{x^2-4}{x-2}$$, which simplifies to $$x+2$$ for every $$x\neq2$$, and at $$x=2$$ the original expression is undefined. As $$\delta$$ decreases, the nearby outputs become increasingly concentrated around 4. For example, when $$\delta=0.01$$, the outputs occupy an interval of width 0.02, and when $$\delta=0.0001$$, that width is 0.0002. So $$\lim_{x\to2}f(x)=4$$.

Now change the value at $$x=2$$. Set it to 4, then to 1, then leave it undefined. The limit does not change.

The reason is simple. The definition of the limit excludes the point itself, and the nearby behavior is identical in all three cases. Only one of those versions is continuous at $$x=2$$, but all three have the same limit there.

## Both sides have to agree

Now switch to the jump. As $$x$$ approaches 2 from the left, the outputs approach 4, and from the right, they approach 1, so

$$\lim_{x\to2^-}f(x)=4, \qquad \lim_{x\to2^+}f(x)=1$$

Both one-sided limits exist, but they are not equal, so the two-sided limit does not exist. In general, $$\lim_{x\to a}f(x)=L$$ exists exactly when both one-sided limits exist and equal $$L$$. This matters in both directions. Sometimes you are given the one-sided limits and asked for the two-sided limit, and other times, especially in continuity problems, you are asked to choose a parameter so that the two sides agree.

## A limit can fail without a jump

The function $$\sin\left(\tfrac{1}{x-2}\right)$$ shows a different kind of failure. There is no jump and no vertical asymptote, and the function stays between $$-1$$ and $$1$$ near $$x=2$$, but it still has no limit.

As $$x$$ approaches 2, the quantity $$1/(x-2)$$ grows without bound in magnitude, so the sine function completes infinitely many oscillations inside every neighborhood of 2. No matter how small the window becomes, it still contains inputs where the output is near 1 and others where the output is near $$-1$$, and the outputs never settle near one number.

This is why a limit cannot be read simply as “the graph is unbroken.” [Continuity](/2026/07/30/continuity-three-conditions.html), existence of the function value, and existence of the limit are separate questions.

## Reading a limit from a graph

A useful habit is to ignore the point itself at first. Look at what the graph does as you approach from the left and from the right. If both sides approach the same value, that value is the limit, and it does not matter whether the graph has an open circle there, a filled point somewhere else, or no defined point at all.

If the two sides approach different values, the two-sided limit does not exist, and if either side fails to settle to a finite value, the two-sided limit also does not exist. Only after answering the limit question should you look at the actual value of the function.

<div class="article-note" markdown="1">
A quick self-test is to use the visualization without dragging the slider first. Choose the jump and predict what happens to the output range as $$\delta$$ falls from 1 to 0.001. Then do the same for the oscillating function. The important distinction is why the range refuses to collapse in each case.
</div>
