---
layout: post
title: "Invoking the Intermediate Value Theorem"
date: 2026-07-30
description: "An existence theorem promises that something happens without saying where. Check the hypotheses, state the conclusion in the theorem's own terms, and the point is earned."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "7 min read"
math: true
kind: mechanics
sequence: 6
interactive: true
blurb: "Something happens somewhere, and the theorem refuses to say where"
image: "/assets/og/intermediate-value-theorem.png"
---

The framework gathers a small family of results under one idea: existence theorems allow us to draw conclusions about a function's behavior on an interval without precisely locating that behavior. The Intermediate Value Theorem is the first of them, and that sentence is the whole shape of it. Something happens. The theorem declines to say where.

Stated in full: if $$f$$ is continuous on the closed interval $$[a,b]$$ and $$d$$ is a number between $$f(a)$$ and $$f(b)$$, then there is at least one number $$c$$ between $$a$$ and $$b$$ with $$f(c) = d$$.

Four things to notice, and the interactive below is built to make each of them visible.

## The statement, one clause at a time

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

The two hypotheses are checked separately because they fail separately. Drag the target above 5 or below 1 and the second one goes out while the first holds: the function is still continuous, the theorem has nothing to say, and the honest report is that it does not apply rather than that no crossing exists.

## "At least one" is not a hedge

Leave the target at 3 on the continuous function and count the marked crossings. There are three, at $$x = 2-\sqrt{3}$$, $$x = 2$$, and $$x = 2+\sqrt{3}$$, and the theorem promised one.

That gap is the point of an existence theorem. It is a lower bound on how much happens, obtained from almost no information — two endpoint values and continuity. It cannot be a count, because the same two endpoint values are consistent with one crossing or with a hundred.

So a conclusion that says "the function equals 3 exactly once" is not what the theorem gives you, and neither is "the function equals 3 at $$x = 2$$." Both are true here. Neither follows from the IVT.

## Continuity is not decoration

Switch to the jump and set the target to 3.5. The endpoints have not moved: $$f(0) = 1$$ and $$f(4) = 5$$, and 3.5 sits squarely between them. The second hypothesis is satisfied and the first is not, and the readout reports what that costs — no crossing anywhere on the interval.

The left piece climbs from 1 to just under 3; the right piece starts at 4 and climbs to 5. Everything in $$[3, 4)$$ is stepped straight over. The bracket is a genuine bracket and it guarantees nothing, because the guarantee was never about the endpoints alone.

This is also why "continuous on the *closed* interval" is written the way it is. The endpoints are where $$f(a)$$ and $$f(b)$$ are read, so continuity has to reach them.

## The sentence that earns the point

The suggested skill attached to this topic is providing reasons or rationales for a conclusion, which is a fair warning that the writing is the assessed part. A complete invocation has four moves, in this order:

1. Name the function and assert continuity, with a reason. Polynomials are continuous everywhere; a quotient is [continuous on its domain](/2026/07/30/continuity-three-conditions.html); a function given as continuous in the stem is continuous because you were told.
2. Evaluate at both endpoints and state the two values.
3. Observe that the target lies between them.
4. Conclude, in the theorem's own words, that there is at least one $$c$$ in the open interval with $$f(c) = d$$, and name the theorem.

Written out for the function above:

> $$f$$ is a polynomial, so it is continuous on $$[0,4]$$. Since $$f(0) = 1$$ and $$f(4) = 5$$, and $$1 < 3 < 5$$, the Intermediate Value Theorem guarantees there is at least one $$c$$ in $$(0,4)$$ with $$f(c) = 3$$.

The two failures worth naming are skipping step 1, which is the one graders are actually checking, and overclaiming in step 4 — writing "exactly one" or naming a location. The theorem is being invoked precisely because you cannot locate anything, so a conclusion that locates something is not a conclusion the theorem supports.

<div class="article-note" markdown="1">
A self-test at the jump: drag the target slowly from 2 up to 5 and watch the crossing count. It reads one, then none, then one again, while the verdict never moves — the theorem has said "does not apply" for the whole drag. Account for that in one sentence. A theorem that is silent across the entire range is still telling you something true at every point of it, and saying what is the difference between having learned the statement and being able to use it.
</div>
