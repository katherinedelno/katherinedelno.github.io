---
layout: post
title: "What a limit claims, and what it does not"
date: 2026-07-30
description: "A limit is a claim about the neighbourhood of a point, not about the point. Narrow the window by hand and watch the outputs close in on a number the function may never actually take."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: foundations
sequence: 2
interactive: true
blurb: "Narrow the window and watch the outputs close in on a value the function skips"
featured: true
---

A limit says nothing about what happens at the point. It is a claim about every point nearby, and the value at the centre is deliberately excluded from the question.

That exclusion is not a technicality to be tolerated until the real material arrives. It is the entire reason limits exist. A derivative is a limit of quotients that are undefined at the point of interest, and a definite integral is [a limit of sums](/2026/07/25/riemann-sums-watching-rectangles.html) that never equal the area. Both need a way to say "the outputs are closing in on this number" without ever asking the function to reach it.

## Narrow the window

Pick a point $$a$$ and a width $$\delta$$, look at every input within $$\delta$$ of $$a$$ except $$a$$ itself, and collect the outputs. Narrowing $$\delta$$ either drives that collection down to a single number or it does not. That is the whole test.

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
  <p class="viz-caption">The shaded band is the window: every input within &delta; of 2, with the centre itself punched out. The bar on the right is the set of outputs the function takes on that band, and its height is the number to watch. For the hole, the bar collapses toward a point at height 4 however small &delta; gets, and the marker at x = 2 can be set to 4, to 1, or removed entirely without the bar noticing. For the jump it sits at 3, the size of the gap, and never shrinks. For the oscillation it holds at 2 forever, because every window, however narrow, contains inputs sending the output to every value between −1 and 1.</p>
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

Start with the hole. The function is

$$f(x) = \frac{x^2 - 4}{x - 2},$$

which equals $$x + 2$$ everywhere except at $$x = 2$$, where the formula reads $$0/0$$ and defines nothing. Drag $$\delta$$ down. The output bar closes steadily toward height zero around the value 4, and it does so no matter how far you push: at $$\delta = 0.01$$ the outputs span a height of 0.02, at $$\delta = 0.0001$$ a height of 0.0002. The limit is 4.

Now set the value at $$x = 2$$ to 4, then to 1, then remove it again. The bar does not move. It cannot: the window has the centre punched out, so the marker at $$x = 2$$ is not among the outputs being collected. This is what "a limit is about the neighbourhood" means operationally, and it is why $$\lim_{x \to 2} f(x) = 4$$ is true for all three versions of the function even though only one of them is continuous there.

## The claim requires both sides to agree

Switch to the jump. Approaching 2 from the left the outputs head for 4; from the right they head for 1. Each side settles on its own destination, but the bar collects both, so its height sits at 3, exactly the size of the jump, however far you narrow the window.

Two one-sided limits exist, and they disagree:

$$\lim_{x \to 2^-} f(x) = 4, \qquad \lim_{x \to 2^+} f(x) = 1.$$

Because they disagree, $$\lim_{x \to 2} f(x)$$ does not exist. The two-sided limit exists exactly when both one-sided limits exist and are equal, and that is worth stating as a biconditional rather than a rule, since exam questions run it in both directions: sometimes you are given the two one-sided limits and asked about the limit, sometimes given continuity and asked what a parameter must be for the sides to match.

## Failing without a jump

Endless oscillation is the case that stops the pattern-matching. The function $$\sin\!\left(\tfrac{1}{x-2}\right)$$ has no jump, no break you could point at, and no vertical asymptote. It is perfectly finite everywhere near 2, trapped between $$-1$$ and 1.

It still has no limit, and the bar says why: the height stays at 2 for every $$\delta$$ you can reach. As $$x$$ closes on 2 the quantity $$1/(x-2)$$ runs off to infinity, so the sine completes infinitely many full cycles inside any window you choose. Every window, however narrow, contains inputs where the function is 1 and inputs where it is $$-1$$.

That is the honest content of "the outputs must close in on a single number." Not "the graph must be unbroken," and not "the function must be defined." Those are different claims, and separating them is what [continuity's three conditions](/2026/07/30/continuity-three-conditions.html) does.

## Reading a limit off a graph

Everything above turns into a single reading habit: cover the centre with a finger and look only at what is on either side of it.

If the two sides go to the same place, that place is the limit, whatever the graph does at the point itself — an open circle there, a filled dot at some unrelated height, or nothing at all. If they go to different places, the limit does not exist. If either side fails to settle anywhere, the limit does not exist either, and for a different reason, which is why the oscillation is worth having seen once.

The value at the point is a separate question with a separate answer, and a graph can be built so that the two answers differ. Asking them one at a time is the discipline; the finger is how it is enforced.

<div class="article-note" markdown="1">
A self-test at the window: set the function to the jump and predict, before dragging, what the output bar's height will do as $$\delta$$ falls from 1 to 0.001. Then check. Now do the same for the oscillation, and account for the difference in one sentence that mentions the word *cycles*. A student who can write that sentence understands limits better than one who can compute twenty of them.
</div>
