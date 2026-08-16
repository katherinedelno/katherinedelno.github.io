---
layout: post
title: "Invoking the Intermediate Value Theorem"
date: 2026-07-30
description: "The theorem guarantees that a value is reached somewhere on an interval. It does not tell you where or how many times."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "7 min read"
math: true
kind: mechanics
sequence: 6
interactive: true
blurb: "The theorem guarantees that a value is reached somewhere on an interval. It does not tell you where or how many times"
image: "/assets/og/intermediate-value-theorem.png"
---

The Intermediate Value Theorem is an existence theorem.

It allows us to conclude that a continuous function reaches a particular value somewhere on an interval without locating the point where that happens.

In full, suppose $$f$$ is continuous on the closed interval $$[a,b]$$. If $$d$$ lies between $$f(a)$$ and $$f(b)$$, then there is at least one $$c\in(a,b)$$ such that

$$f(c)=d.$$

The hypotheses and the conclusion are all worth reading carefully.

## The statement one condition at a time

<div class="viz" markdown="0">
  <canvas id="iv-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <button type="button" id="iv-c" class="res-filter is-active" style="font-size:.72rem">Continuous on [0, 4]</button>
    <button type="button" id="iv-j" class="res-filter" style="font-size:.72rem">With a jump at x = 2</button>
    <label for="iv-d">Target d</label>
    <input type="range" id="iv-d" min="0" max="600" step="1" value="300">
  </div>
  <div class="iv-panel">
    <div class="iv-row" id="iv-h1"></div>
    <div class="iv-row" id="iv-h2"></div>
    <div class="iv-verdict" id="iv-v"></div>
    <div class="iv-truth" id="iv-t"></div>
  </div>
  <p class="viz-caption">Both functions run from f(0) = 1 to f(4) = 5, so the bracket the theorem checks is identical in the two modes and only continuity differs. Drag the target. Where the theorem applies it promises at least one crossing, and every place the function actually meets the target is marked and counted underneath — three, whenever the theorem has anything to say, which is the gap between what is guaranteed and what is true. Switch to the jump and drag the target between 3 and 4: the bracket still holds, the theorem no longer applies, and there is genuinely no crossing to find.</p>
  <style>
    .iv-panel{margin:.9rem 0 0;padding-top:.8rem;border-top:1px solid var(--line)}
    .iv-row{font-size:.95rem;line-height:1.7;color:var(--ink)}
    .iv-row .iv-mk{display:inline-block;width:1.4em;font-weight:700}
    .iv-row.no{color:var(--muted)}
    .iv-verdict{margin-top:.5rem;font-size:1.2rem;font-weight:700;letter-spacing:-.02em;color:var(--ink)}
    .iv-truth{font-size:.9rem;color:var(--muted);margin-top:.2rem}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('iv-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var A=0,B=4, cont=true;
  var PADL=44,PADR=24,TOP=16,AXIS=H-32;
  var YLO=0,YHI=6.4;
  function px(x){ return PADL+(x-A)/(B-A)*(W-PADL-PADR); }
  function py(y){ return AXIS-(y-YLO)/(YHI-YLO)*(AXIS-TOP); }
  function D(){ return (+document.getElementById('iv-d').value)/100; }

  // continuous: x^3 - 6x^2 + 9x + 1.  f(0)=1, f(1)=5, f(3)=1, f(4)=5.
  function fc(x){ return x*x*x-6*x*x+9*x+1; }
  // jump: same endpoints, values in [3,4) never attained
  function fj(x){ return x<2 ? 1+x : 0.5*x+3; }
  function f(x){ return cont?fc(x):fj(x); }

  // Every place where f attains d, not only the sign changes. A turning point
  // that sits exactly on d — d = 1 and d = 5 here — is attained without any
  // change of sign, and counting only sign changes would miss it.
  function crossings(d){
    var out=[], N=200000, prev=f(A)-d, prev2=null, x, v, i;
    for(i=1;i<=N;i++){
      x=A+(B-A)*i/N; v=f(x)-d;
      if(prev===0){ out.push(A+(B-A)*(i-1)/N); }
      else if(prev*v<0){
        var lo=A+(B-A)*(i-1)/N, hi=x;
        if(cont || !(lo<2 && hi>=2)){                     // the jump is not a crossing
          for(var k=0;k<60;k++){ var m=(lo+hi)/2; if((f(lo)-d)*(f(m)-d)<=0) hi=m; else lo=m; }
          out.push((lo+hi)/2);
        }
      } else if(prev2!==null && (prev-prev2)*(v-prev)<0 && Math.abs(prev)<1e-6){
        out.push(A+(B-A)*(i-1)/N);                        // a turning point resting on d
      }
      prev2=prev; prev=v;
    }
    if(Math.abs(f(B)-d)<1e-12) out.push(B);
    return out;
  }

  function draw(){
    var d=D(), fa=f(A), fb=f(B);
    var between = d>Math.min(fa,fb) && d<Math.max(fa,fb);
    var xs=crossings(d);
    c.clearRect(0,0,W,H);
    // axes
    c.strokeStyle=LINE; c.lineWidth=1;
    c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    for(var t=0;t<=4;t++) c.fillText(String(t),px(t),AXIS+14);
    c.textAlign='right';
    for(var v=2;v<=6;v+=2) c.fillText(String(v),PADL-6,py(v)+3);
    // bracket: f(a) and f(b)
    [[A,fa],[B,fb]].forEach(function(p){
      c.strokeStyle=PALE; c.setLineDash([3,3]); c.lineWidth=1;
      c.beginPath(); c.moveTo(PADL,py(p[1])); c.lineTo(W-PADR,py(p[1])); c.stroke(); c.setLineDash([]);
    });
    c.fillStyle=FAINT; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText('f(0) = 1', W-PADR-52, py(fa)-5);
    c.fillText('f(4) = 5', W-PADR-52, py(fb)-5);
    // target line
    c.strokeStyle=between?INK:FAINT; c.lineWidth=1.6; c.setLineDash([6,4]);
    c.beginPath(); c.moveTo(PADL,py(d)); c.lineTo(W-PADR,py(d)); c.stroke(); c.setLineDash([]);
    c.fillStyle=between?INK:FAINT; c.font='700 11px '+FONT;
    c.fillText('d = '+d.toFixed(2), PADL+4, py(d)-6);
    // curve
    c.strokeStyle=INK; c.lineWidth=2;
    (cont?[[A,B]]:[[A,2],[2,B]]).forEach(function(seg){
      c.beginPath(); var on=false;
      for(var i=0;i<=800;i++){
        var x=seg[0]+(seg[1]-seg[0])*i/800;
        if(!cont && seg[0]===A && x>=2) continue;
        var y=f(x);
        if(y<YLO-1||y>YHI+1){ on=false; continue; }
        on?c.lineTo(px(x),py(y)):(c.moveTo(px(x),py(y)),on=true);
      }
      c.stroke();
    });
    if(!cont){
      c.strokeStyle=INK; c.lineWidth=2; c.fillStyle='#fff';
      c.beginPath(); c.arc(px(2),py(3),4.2,0,7); c.fill(); c.stroke();
      c.fillStyle=INK; c.beginPath(); c.arc(px(2),py(4),4.2,0,7); c.fill();
    }
    // crossings
    xs.forEach(function(x){
      c.fillStyle=INK; c.beginPath(); c.arc(px(x),py(d),5,0,7); c.fill();
      c.strokeStyle='#fff'; c.lineWidth=1.6; c.stroke();
    });
    render(between,xs,d);
  }

  function render(between,xs,d){
    function row(id,ok,txt){
      var e=document.getElementById(id);
      e.className='iv-row'+(ok?'':' no');
      e.innerHTML='<span class="iv-mk">'+(ok?'&#10003;':'&#10007;')+'</span>'+txt;
    }
    row('iv-h1', cont, cont ? 'f is continuous on the closed interval [0, 4]'
                            : 'f is not continuous on [0, 4] &mdash; it jumps at x = 2');
    row('iv-h2', between, between ? 'd = '+d.toFixed(2)+' lies between f(0) = 1 and f(4) = 5'
                                  : 'd = '+d.toFixed(2)+' does not lie between f(0) = 1 and f(4) = 5');
    var applies = cont && between;
    document.getElementById('iv-v').textContent = applies
      ? 'The theorem applies: there is at least one c in (0, 4) with f(c) = ' + d.toFixed(2)
      : 'The theorem does not apply, so it promises nothing';
    var n=xs.length;
    document.getElementById('iv-t').textContent =
      'In fact this function meets d ' + (n===0?'nowhere':(n===1?'once':n===2?'twice':n+' times')) +
      (n?' — at x = '+xs.map(function(x){return x.toFixed(4);}).join(', '):'') + '.';
  }
  document.getElementById('iv-c').addEventListener('click',function(){
    cont=true; this.classList.add('is-active');
    document.getElementById('iv-j').classList.remove('is-active'); draw();
  });
  document.getElementById('iv-j').addEventListener('click',function(){
    cont=false; this.classList.add('is-active');
    document.getElementById('iv-c').classList.remove('is-active'); draw();
  });
  document.getElementById('iv-d').addEventListener('input',draw);
  draw();
})();
</script>

Both functions in the visualization have the same endpoint values,

$$f(0)=1 \quad\text{and}\quad f(4)=5.$$

The only difference is continuity.

For the continuous function, any target $$d$$ between 1 and 5 satisfies the conditions of the theorem. At least one crossing is guaranteed.

The graph may cross the target more than once. The theorem does not count the crossings.

Switch to the function with a jump and choose a target between 3 and 4.

The endpoint condition still holds. The target lies between $$f(0)$$ and $$f(4)$$.

But the function is not continuous on the interval, so the theorem no longer applies.

In this example, there is also no crossing.

Now move the target above 5 or below 1 while keeping the continuous function.

Continuity still holds, but the target is no longer between the endpoint values. Again, the theorem does not apply.

This does not mean the function cannot equal that target somewhere. It means the theorem gives no guarantee.

## What “at least one” means

Set the target to 3 on the continuous function.

The graph crosses $$y=3$$ three times.

The Intermediate Value Theorem guarantees only one or more.

That is all an existence theorem can conclude from the information it uses. Continuity and two endpoint values are enough to guarantee a crossing, but not enough to determine the number or location of crossings.

So the theorem does not justify either of these claims:

- $$f(x)=3$$ exactly once.
- $$f(2)=3$$.

Those statements may happen to be true for a particular function. They do not follow from the theorem.

## Why continuity matters

Return to the function with a jump and set the target to 3.5.

The endpoint values remain 1 and 5, so

$$1<3.5<5.$$

But the left piece approaches values below 3 while the right piece begins at 4.

The graph skips the entire interval of outputs between 3 and 4.

Without continuity, the endpoint bracket alone guarantees nothing.

This is why the theorem requires continuity on the entire closed interval $$[a,b]$$. The conclusion depends on the function being unable to jump over intermediate values.

## Writing a complete IVT justification

A strong written justification has four parts.

1. State that the function is [continuous on the relevant closed interval](/2026/07/30/continuity-three-conditions.html) and give a reason.
2. Evaluate the function at both endpoints.
3. Show that the target value lies between those endpoint values.
4. Invoke the Intermediate Value Theorem and state the existence conclusion.

For example:

> “$$f$$ is a polynomial, so it is continuous on $$[0,4]$$. Since $$f(0)=1$$ and $$f(4)=5$$, and $$1<3<5$$, the Intermediate Value Theorem guarantees that there is at least one $$c\in(0,4)$$ such that $$f(c)=3$$.”

Two common errors are easy to avoid.

The first is skipping the continuity statement.

The second is claiming more than the theorem gives. Do not say “exactly one” unless you have additional information that proves uniqueness. Do not name the location unless you obtained it by some other method.

<div class="article-note" markdown="1">
A useful self-test is to use the discontinuous function and drag the target from 2 to 5.

The number of actual crossings changes. The theorem's verdict does not. It remains silent because one of its hypotheses is false.

That distinction is the point.
</div>
