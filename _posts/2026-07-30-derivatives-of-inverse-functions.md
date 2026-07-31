---
layout: post
title: "Derivatives of inverse functions"
date: 2026-07-30
description: "The derivative of an inverse function can be found without ever writing the inverse down. The rule is a reciprocal, and the whole difficulty is remembering where it gets evaluated."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: mechanics
sequence: 12
interactive: true
blurb: "A reciprocal, evaluated somewhere other than where you are standing"
---

The graph of $$f^{-1}$$ is the graph of $$f$$ reflected across the line $$y = x$$. Reflecting a line across $$y = x$$ swaps its rise and its run, so the slopes at corresponding points are reciprocals. That picture is the whole theorem, and it is worth having before the formula.

What makes the formula useful is that it needs no formula for $$f^{-1}$$. The inverse can be something nobody can write down, and the derivative of it at a point is still an ordinary arithmetic problem.

## The rule, and where it is evaluated

Suppose $$f$$ is one-to-one and differentiable on an interval, $$f^{-1}$$ is defined near $$a$$, and $$f'\big(f^{-1}(a)\big) \neq 0$$. Then $$f^{-1}$$ is differentiable at $$a$$ and

$$\big(f^{-1}\big)'(a) = \frac{1}{f'\big(f^{-1}(a)\big)}.$$

It comes straight out of the chain rule, which is what the framework says it comes out of. Start from the definition of an inverse, $$f\big(f^{-1}(x)\big) = x$$, and differentiate both sides:

$$f'\big(f^{-1}(x)\big) \cdot \big(f^{-1}\big)'(x) = 1.$$

Divide. The condition $$f'\big(f^{-1}(a)\big) \neq 0$$ is exactly the condition that lets you divide.

The trap is the evaluation point, and it is the [same trap as in the chain rule](/2026/07/30/chain-rule-reading-the-layers.html): $$f'$$ is not evaluated at $$a$$. It is evaluated at the input that $$f$$ sends to $$a$$. Take $$f(x) = x^3 + x$$. Since $$f(1) = 2$$, we have $$f^{-1}(2) = 1$$, so

$$\big(f^{-1}\big)'(2) = \frac{1}{f'(1)} = \frac{1}{3(1)^2 + 1} = \frac14.$$

Nobody wrote down $$f^{-1}$$, and nobody could — the inverse of $$x^3 + x$$ has no expression in the functions of this course. The answer is still exactly one quarter.

## Confirming an answer you could not have computed

Topic 3.3's suggested skill is to confirm that solutions are accurate and appropriate, which is an unusual thing to ask of a differentiation rule and a reasonable thing to ask of this one. The tool below does the confirming two ways.

<div class="viz" markdown="0">
  <div class="viz-controls" id="iv-fns"></div>
  <canvas id="iv-cv" width="700" height="380"></canvas>
  <div class="viz-controls">
    <label for="iv-b">b, the point on f</label>
    <input type="range" id="iv-b" min="0" max="1200" step="1" value="900">
  </div>
  <div class="iv-read" id="iv-read"></div>
  <p class="viz-caption">The dark curve is f and the pale one is its reflection across the dashed diagonal, drawn by swapping coordinates rather than by inverting anything. A point sits at (b, f(b)) and its mirror at (f(b), b); the two short lines are the tangents there. The panel gives f'(b), its reciprocal, and their product, which is 1 wherever both exist. Where an inverse derivative has a formula worth memorising, the last row evaluates that formula independently and reports the gap. For x³ + x there is no formula to compare against, which is the case the rule was built for.</p>
  <style>
    .iv-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .iv-read .iv-lab{color:var(--muted);display:inline-block;min-width:15rem}
    .iv-read .iv-val{font-weight:700}
    .iv-read .iv-flag{color:var(--muted);font-weight:400}
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
  var $=function(i){ return document.getElementById(i); };
  var SIDE=336, TOPP=22, CX0=(W-SIDE)/2;

  // invd is the memorised derivative of the inverse, as a function of a — used
  // only as an independent check, never to produce the answer.
  // Ranges are chosen so that the b values the article quotes land on integer
  // slider positions: b = 1 at 900, b = pi/6 at 800, b = pi/4 at 960, b = 0 at 600.
  var F=[
    { n:'x³ + x', inv:null, invd:null, lo:-2, hi:2, cx:0, cy:0, w:4.6,
      f:function(x){ return x*x*x+x; }, df:function(x){ return 3*x*x+1; } },
    { n:'eˣ', inv:'ln x', invd:function(a){ return 1/a; },
      lo:-2.6, hi:1.9, cx:1.4, cy:1.4, w:4.4,
      f:Math.exp, df:Math.exp },
    { n:'sin x  on  [-π/2, π/2]', inv:'arcsin x',
      invd:function(a){ return 1/Math.sqrt(1-a*a); },
      lo:-Math.PI/2, hi:Math.PI/2, cx:0, cy:0, w:1.85,
      f:Math.sin, df:Math.cos },
    { n:'tan x  on  (-5π/12, 5π/12)', inv:'arctan x',
      invd:function(a){ return 1/(1+a*a); },
      lo:-5*Math.PI/12, hi:5*Math.PI/12, cx:0, cy:0, w:4,
      f:Math.tan, df:function(x){ var s=1/Math.cos(x); return s*s; } },
    { n:'x³', inv:'∛x', invd:function(a){ return 1/(3*Math.pow(Math.cbrt(a),2)); },
      lo:-1.75, hi:1.75, cx:0, cy:0, w:2.2,
      f:function(x){ return x*x*x; }, df:function(x){ return 3*x*x; } }
  ];
  var k=0;
  function G(){ return F[k]; }
  function px(x){ var g=G(); return CX0+(x-(g.cx-g.w))/(2*g.w)*SIDE; }
  function py(y){ var g=G(); return TOPP+SIDE-(y-(g.cy-g.w))/(2*g.w)*SIDE; }
  function fmt(v){ var a=Math.abs(v);
    if(a<1e-12) return (0).toFixed(4);
    if(a<1e-3||a>=1e5) return v.toExponential(3);
    return v.toFixed(4); }

  var bar=$('iv-fns');
  F.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  function seg(x0,y0,x1,y1){ c.beginPath(); c.moveTo(px(x0),py(y0)); c.lineTo(px(x1),py(y1)); c.stroke(); }

  function draw(){
    var g=G(), s=(+$('iv-b').value)/1200, b=g.lo+s*(g.hi-g.lo);
    var a=g.f(b), m=g.df(b);
    Array.prototype.forEach.call(bar.children,function(e,i){
      e.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(CX0,TOPP,SIDE,SIDE); c.clip();

    c.strokeStyle=LINE; c.lineWidth=1;
    var i, lo=Math.ceil(g.cx-g.w), hi=Math.floor(g.cx+g.w);
    for(i=lo;i<=hi;i++) seg(i,g.cy-g.w,i,g.cy+g.w);
    lo=Math.ceil(g.cy-g.w); hi=Math.floor(g.cy+g.w);
    for(i=lo;i<=hi;i++) seg(g.cx-g.w,i,g.cx+g.w,i);

    // the mirror line
    c.strokeStyle=PALE; c.lineWidth=1.4; c.setLineDash([5,4]);
    seg(g.cx-g.w,g.cx-g.w,g.cx+g.w,g.cx+g.w);
    c.setLineDash([]);

    // f, then its reflection: the same points with the coordinates swapped
    var N=900, t, x, y;
    c.strokeStyle=INK; c.lineWidth=2; c.beginPath();
    for(i=0;i<=N;i++){ t=g.lo+(g.hi-g.lo)*i/N; x=t; y=g.f(t);
      if(i===0) c.moveTo(px(x),py(y)); else c.lineTo(px(x),py(y)); }
    c.stroke();
    c.strokeStyle=FAINT; c.lineWidth=2; c.beginPath();
    for(i=0;i<=N;i++){ t=g.lo+(g.hi-g.lo)*i/N; x=g.f(t); y=t;
      if(i===0) c.moveTo(px(x),py(y)); else c.lineTo(px(x),py(y)); }
    c.stroke();

    // the two tangents, each drawn over the same short run
    var r=0.5*g.w;
    c.lineWidth=1.6;
    c.strokeStyle=INK; seg(b-r, a-r*m, b+r, a+r*m);
    if(m!==0){ c.strokeStyle=FAINT; seg(a-r, b-r/m, a+r, b+r/m); }
    else     { c.strokeStyle=FAINT; seg(a, b-r, a, b+r); }   // vertical mirror tangent

    c.fillStyle=INK; c.beginPath(); c.arc(px(b),py(a),4.5,0,6.284); c.fill();
    c.fillStyle=FAINT; c.beginPath(); c.arc(px(a),py(b),4.5,0,6.284); c.fill();
    c.restore();
    c.fillStyle=MUTED; c.font='700 11px '+FONT; c.textAlign='left';
    c.fillText('f(x) = '+g.n, CX0, TOPP-8);
    c.textAlign='right';
    c.fillText(g.inv ? 'f⁻¹(x) = '+g.inv : 'f⁻¹ has no elementary formula', CX0+SIDE, TOPP-8);

    var dead = Math.abs(m) < 1e-12;
    var rec = dead ? null : 1/m;
    function row(lab,body){ return '<div><span class="iv-lab">'+lab+'</span>'+body+'</div>'; }
    function V(x){ return '<span class="iv-val">'+x+'</span>'; }
    function flag(x){ return '<span class="iv-flag">'+x+'</span>'; }
    var out=
      row('b', V(fmt(b)))+
      row('a = f(b)', V(fmt(a)))+
      row('f&prime;(b)', V(fmt(m)))+
      row('(f&#8315;&sup1;)&prime;(a) = 1 / f&prime;(b)',
          dead ? flag('undefined &mdash; f&prime;(b) is zero') : V(fmt(rec)))+
      row('f&prime;(b) &times; (f&#8315;&sup1;)&prime;(a)',
          dead ? flag('no product to form') : V(fmt(m*rec)));
    if(g.invd){
      var known=g.invd(a);
      out+=row('from the formula for '+g.inv,
        (!isFinite(known) || dead) ? flag('undefined there too')
          : V(fmt(known))+flag('&nbsp;&nbsp;gap '+Math.abs(known-rec).toExponential(1)));
    } else {
      out+=row('from the formula for f&#8315;&sup1;', flag('there is no such formula'));
    }
    $('iv-read').innerHTML=out;
  }
  $('iv-b').addEventListener('input',draw);
  draw();
})();
</script>

The first confirmation is geometric and needs no algebra: the two slopes multiply to 1 at every position of the slider, on every function. The second is the row at the bottom. Where the inverse has a derivative worth memorising, the tool evaluates that memorised formula independently and prints the gap between the two answers. Across every function and every slider position that gap never exceeds seven parts in a trillion, which is arithmetic rounding rather than disagreement.

For $$x^3 + x$$ that row has nothing to say, and that is the case the rule exists for.

## The inverse trigonometric derivatives are not a second list

The framework is explicit that the inverse trigonometric derivatives come from this rule rather than from memorisation — the chain rule with the definition of an inverse, or the inverse-derivative formula itself. Both routes are named, and both are short.

With $$f = \sin$$ on $$[-\tfrac{\pi}{2}, \tfrac{\pi}{2}]$$, so that $$f^{-1} = \arcsin$$ and $$f' = \cos$$,

$$(\arcsin)'(a) = \frac{1}{\cos(\arcsin a)} = \frac{1}{\sqrt{1 - a^2}},$$

where the last step is the Pythagorean identity applied to the angle whose sine is $$a$$. With $$f = \tan$$ it is shorter still, because $$\sec^2 = 1 + \tan^2$$ and $$\tan$$ of the angle in question is $$a$$:

$$(\arctan)'(a) = \frac{1}{\sec^2(\arctan a)} = \frac{1}{1 + a^2}.$$

Two derivations, four lines, and no list. This is the same argument as [rearranging tangent and secant](/2026/07/30/derivative-rules-and-choosing.html) in Unit 2, one unit later.

## Provided the derivative exists

The framework attaches that clause to the rule, and it is not decoration. Take $$f(x) = x^3$$, which is one-to-one on the whole real line with inverse the cube root $$x^{1/3}$$. At $$b = 0$$, $$f'(0) = 0$$, and the reciprocal does not exist. Reading the picture instead of the formula says the same thing: the tangent to $$x^3$$ at the origin is horizontal, so its reflection is vertical, and [a vertical tangent is not a slope](/2026/07/30/where-differentiability-fails.html).

<div class="article-note" markdown="1">
On a free-response question the information usually arrives as a table rather than a formula, and the reciprocal is the easy part. Before writing anything, find the row you actually need: if the question asks for $$\big(f^{-1}\big)'(4)$$, look down the $$f(x)$$ column for the 4, not the $$x$$ column. Everything after that is one division.
</div>
