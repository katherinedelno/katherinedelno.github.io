---
layout: post
title: "Two existence theorems, and what they refuse to tell you"
date: 2026-07-30
description: "The Mean Value Theorem and the Extreme Value Theorem both promise that something exists somewhere on an interval. Neither says where, and both stop promising the moment a hypothesis fails."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: mechanics
sequence: 18
interactive: true
blurb: "A guarantee that something exists, with no address attached"
---

The enduring understanding these two theorems sit under says what they are for in one sentence: existence theorems let us draw conclusions about a function's behaviour on an interval without precisely locating that behaviour. Both of them promise something exists. Neither tells you where it is.

That is the same bargain [the Intermediate Value Theorem](/2026/07/30/intermediate-value-theorem.html) offers, and these two are its neighbours in the framework — all three sit under FUN-1.

## The two statements

The Mean Value Theorem, with the hypotheses the framework gives it: if $$f$$ is continuous over $$[a,b]$$ and differentiable over $$(a,b)$$, then there is a point in that open interval where the instantaneous rate of change equals the average rate of change over the interval. That is,

$$f'(c) = \frac{f(b)-f(a)}{b-a} \quad \text{for some } c \text{ in } (a,b).$$

Note the asymmetry. Continuity is required on the closed interval because the average rate needs $$f(a)$$ and $$f(b)$$; differentiability is only required on the open one, because the guaranteed point is interior and no derivative at an endpoint is ever used.

The Extreme Value Theorem: if $$f$$ is continuous over $$[a,b]$$, then $$f$$ has at least one minimum value and at least one maximum value on $$[a,b]$$. Continuity on the closed interval, and that is the whole hypothesis. If you are working from an older printing of the framework, check the wording — this statement was corrected for fall 2026, and the interval in the hypothesis is the closed one.

Two supporting definitions come with it. A critical point is a point where the first derivative equals zero or [fails to exist](/2026/07/30/where-differentiability-fails.html) — both halves, and the second half is the one that gets forgotten. All local extrema occur at critical points, but not all critical points are local extrema, which is why finding them is a search and not an answer.

## Watching a guarantee disappear

Below, one interval and four functions on it. The first satisfies both theorems. The other three each break exactly one thing.

<div class="viz" markdown="0">
  <div class="viz-controls" id="mv-fns"></div>
  <canvas id="mv-cv" width="700" height="330"></canvas>
  <div class="mv-read" id="mv-read"></div>
  <p class="viz-caption">The interval is [0, 3] throughout. The dashed line is the secant joining the endpoints, and any tangent drawn parallel to it marks a point the Mean Value Theorem promised. Squares mark the maximum and the minimum where they are attained; an open circle marks a value the function approaches on the interval but never reaches, which is what it looks like when the Extreme Value Theorem has nothing to promise. The panel checks each hypothesis separately before reporting each conclusion, because those are separate questions.</p>
  <style>
    .mv-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .mv-read .mv-lab{color:var(--muted);display:inline-block;min-width:16.5rem}
    .mv-read .mv-val{font-weight:700;display:inline-block;min-width:5.5rem}
    .mv-read .mv-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('mv-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=44,PADR=20,TOP=18,BOT=H-26, A=0, B=3;

  function cube(x){ return x*x*x - 4.5*x*x + 6*x; }
  function dcube(x){ return 3*x*x - 9*x + 6; }
  var F=[
    { n:'a smooth cubic', ylo:-1.1, yhi:5.4,
      f:cube, d:dcube,
      cont:'yes', diff:'yes', breaks:[],
      // max, min: [value, location] or null when not attained
      mx:[4.5,3], mn:[0,0], open:[] },
    { n:'a corner at x = 1.5', ylo:0.2, yhi:3.1,
      f:function(x){ return Math.abs(x-1.5)+1; },
      d:function(x){ return x<1.5?-1:1; },
      cont:'yes', diff:'no, at x = 1.5', breaks:[1.5],
      mx:[2.5,3], mn:[1,1.5], open:[] },
    { n:'a jump at x = 1.5', ylo:-1.1, yhi:2.1,
      f:function(x){ return x<1.5 ? x : x-2; },
      d:function(){ return 1; },
      cont:'no, at x = 1.5', diff:'no, at x = 1.5', breaks:[1.5],
      mx:null, mn:[-0.5,1.5], open:[[1.5,1.5]] },
    { n:'a gap at the left endpoint', ylo:-0.6, yhi:5.4,
      f:function(x){ return x===0 ? 3 : cube(x); }, d:dcube,
      cont:'no, at x = 0', diff:'no, at x = 0', breaks:[0],
      mx:[4.5,3], mn:null, open:[[0,0]] }
  ];
  var k=0;
  function G(){ return F[k]; }
  function px(x){ return PADL+(x-A)/(B-A)*(W-PADL-PADR); }
  function py(y){ var g=G(); return BOT-(y-g.ylo)/(g.yhi-g.ylo)*(BOT-TOP); }
  function fmt(v){ return Math.abs(v)<1e-12 ? (0).toFixed(4) : v.toFixed(4); }

  var bar=$('mv-fns');
  F.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  // every c in (A,B) with f'(c) equal to the secant slope, by sign change
  function mvtPoints(g,m){
    var out=[], N=4000, prev=null, x0=null;
    for(var i=0;i<=N;i++){
      var x=A+(B-A)*i/N;
      if(g.breaks.some(function(b){ return Math.abs(x-b)<1e-9; })) { prev=null; continue; }
      var v=g.d(x)-m;
      if(prev!==null && prev*v<0){
        var lo=x0, hi=x;
        for(var j=0;j<80;j++){ var mid=(lo+hi)/2;
          if((g.d(lo)-m)*(g.d(mid)-m)<=0) hi=mid; else lo=mid; }
        out.push((lo+hi)/2);
      }
      prev=v; x0=x;
    }
    return out;
  }

  function draw(){
    var g=G();
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(PADL-2,TOP-8,W-PADL-PADR+4,BOT-TOP+14); c.clip();

    c.strokeStyle=LINE; c.lineWidth=1;
    for(var t=0;t<=3;t++){ c.beginPath(); c.moveTo(px(t),TOP); c.lineTo(px(t),BOT); c.stroke(); }
    if(g.ylo<0&&g.yhi>0){ c.strokeStyle=PALE;
      c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke(); }

    var fa=g.f(A), fb=g.f(B), m=(fb-fa)/(B-A);

    // the secant
    c.strokeStyle=PALE; c.lineWidth=1.6; c.setLineDash([6,4]);
    c.beginPath(); c.moveTo(px(A),py(fa)); c.lineTo(px(B),py(fb)); c.stroke();
    c.setLineDash([]);

    // the function, lifting the pen at each break
    c.strokeStyle=INK; c.lineWidth=2; c.beginPath();
    var first=true;
    for(var i=0;i<=1200;i++){
      var x=A+(B-A)*i/1200;
      if(g.breaks.some(function(b){ return Math.abs(x-b)<0.0016 && b>A && b<B; })){ first=true; continue; }
      var y=g.f(x);
      if(first){ c.moveTo(px(x),py(y)); first=false; } else c.lineTo(px(x),py(y));
    }
    c.stroke();

    // tangents parallel to the secant
    var cs=mvtPoints(g,m);
    c.strokeStyle=FAINT; c.lineWidth=1.6;
    cs.forEach(function(cc){
      var y=g.f(cc), r=0.55;
      c.beginPath(); c.moveTo(px(cc-r),py(y-r*m)); c.lineTo(px(cc+r),py(y+r*m)); c.stroke();
      c.fillStyle=FAINT; c.beginPath(); c.arc(px(cc),py(y),3.6,0,6.284); c.fill();
    });

    // attained extrema as filled squares
    c.fillStyle=INK;
    [g.mx,g.mn].forEach(function(e){ if(e) c.fillRect(px(e[1])-4,py(e[0])-4,8,8); });
    // approached-but-not-attained values as open circles
    c.strokeStyle=INK; c.lineWidth=1.8;
    g.open.forEach(function(o){
      c.beginPath(); c.arc(px(o[0]),py(o[1]),4.5,0,6.284); c.stroke(); });
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    c.fillText('0',px(0),BOT+14); c.fillText('3',px(3),BOT+14);

    function row(l,v,n){ return '<div><span class="mv-lab">'+l+'</span>'+
      '<span class="mv-val">'+v+'</span>'+(n?'<span class="mv-note">'+n+'</span>':'')+'</div>'; }
    var mvtOK = g.cont==='yes' && g.diff==='yes';
    $('mv-read').innerHTML =
      row('continuous on [0, 3]', g.cont==='yes'?'yes':'no', g.cont==='yes'?'':g.cont.slice(4)) +
      row('differentiable on (0, 3)', g.diff==='yes'?'yes':'no', g.diff==='yes'?'':g.diff.slice(4)) +
      row('average rate of change', fmt(m), '') +
      row('points c with f&prime;(c) = that rate', String(cs.length),
          cs.length ? 'c = '+cs.map(fmt).join(',&nbsp; ')
                    : (mvtOK ? '' : 'and the theorem no longer promises one')) +
      row('maximum on [0, 3]', g.mx?fmt(g.mx[0]):'none',
          g.mx?'at x = '+g.mx[1]:'the values approach a bound they never reach') +
      row('minimum on [0, 3]', g.mn?fmt(g.mn[0]):'none',
          g.mn?'at x = '+g.mn[1]:'the values approach a bound they never reach');
  }
  draw();
})();
</script>

On the cubic both theorems deliver. The average rate over $$[0,3]$$ is $$\tfrac32$$, and there are two points where the derivative equals it, at $$\tfrac{3 \pm \sqrt3}{2}$$. The Mean Value Theorem promised one and there are two, which is allowed — it says *at least* one, the way the Extreme Value Theorem says *at least* one maximum.

The corner is the case worth sitting with. The function is continuous on the closed interval, so the Extreme Value Theorem still applies and still finds both extrema. But it has [a corner at $$x = 1.5$$](/2026/07/30/where-differentiability-fails.html) and is therefore not differentiable there, so the Mean Value Theorem does not apply — and its conclusion genuinely fails. The average rate is 0, and the derivative is $$-1$$ or $$+1$$ and never anything else. Two theorems, one function, different hypotheses, different fates.

## What failing a hypothesis does and does not mean

The fourth function is the subtle one. It is the cubic everywhere on $$(0,3]$$, but its value at $$x = 0$$ has been moved to 3, so it is not continuous at the left endpoint. The Extreme Value Theorem is void, and its conclusion fails: the function's values on $$(0,3]$$ get arbitrarily close to 0 without reaching it, so there is no minimum.

The Mean Value Theorem is void too. And yet its conclusion still holds — the average rate is now $$\tfrac12$$, and there are still two points where $$f'(c) = \tfrac12$$, at $$\tfrac32 \pm \tfrac{\sqrt{15}}{6}$$.

That is the thing to take away. A theorem whose hypotheses fail makes no claim; it does not make the opposite claim. Losing the guarantee is not the same as losing the conclusion, and an argument that says "the function is not differentiable, so there is no such point" is as unsupported as one that forgets to check.

## Where the extrema actually were

On the cubic, the maximum on $$[0,3]$$ is 4.5 at $$x = 3$$ and the minimum is 0 at $$x = 0$$ — both at endpoints, and neither at a critical point, since $$f'(0) = f'(3) = 6$$. The interior critical points at $$x = 1$$ and $$x = 2$$ give local extrema of 2.5 and 2, and neither is global.

So the Extreme Value Theorem guarantees the global extrema exist, the critical points supply the interior candidates, and the endpoints have to be added by hand. Missing the endpoints is the standard way to lose this question, and the theorem is partly to blame: it says the extrema are somewhere on $$[a,b]$$, and $$[a,b]$$ includes its ends.

<div class="article-note" markdown="1">
Both topics carry the same suggested skill — provide reasons or rationales for solutions and conclusions — and for an existence theorem that means naming the hypotheses before invoking the name. The sentence that scores looks like this: since $$f$$ is continuous on $$[0,3]$$ and differentiable on $$(0,3)$$, the Mean Value Theorem guarantees a $$c$$ in $$(0,3)$$ with $$f'(c) = \tfrac32$$. Everything in it is a hypothesis, a theorem, or a conclusion, and nothing in it is a calculation.
</div>
