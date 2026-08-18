---
layout: post
title: "The derivative as a limit"
date: 2026-07-30
description: "A derivative is the limit of secant slopes as the second point approaches the first."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "6 min read"
math: true
kind: foundations
sequence: 7
interactive: true
blurb: "A derivative is the limit of secant slopes as the second point approaches the first"
image: "/assets/og/derivative-as-a-limit.png"
---

An average rate of change needs two points. For a function $$f$$, the average rate of change from $$x=a$$ to $$x=a+h$$ is $$\tfrac{f(a+h)-f(a)}{h}$$, and at $$h=0$$ the two points coincide and the denominator is zero. The derivative solves this by using a limit. We let the second point approach the first and ask whether the secant slopes approach a finite number, and if they do, that number is the instantaneous rate of change.

## Move the second point toward the first

The anchor point stays fixed. The second point moves with $$h$$.

<div class="viz" markdown="0">
  <canvas id="dv-cv" width="700" height="320"></canvas>
  <div class="viz-controls">
    <button type="button" class="res-filter dv-f is-active" data-k="0" style="font-size:.72rem">x&sup2; at a = 1</button>
    <button type="button" class="res-filter dv-f" data-k="1" style="font-size:.72rem">x&sup3; at a = 1</button>
    <button type="button" class="res-filter dv-f" data-k="2" style="font-size:.72rem">sin x at a = 0</button>
    <label for="dv-h">h</label>
    <input type="range" id="dv-h" min="-301" max="301" step="1" value="201">
  </div>
  <div class="dv-panel">
    <div class="dv-line" id="dv-hform"></div>
    <div class="dv-line" id="dv-2form"></div>
    <div class="dv-gap" id="dv-gap"></div>
  </div>
  <p class="viz-caption">The faint line is the tangent at the anchor, drawn as the destination rather than as an answer. The dark line is the secant through the anchor and the moving point, and it is the only line the definition actually constructs. Push h toward zero from either side and the secant rotates onto the tangent; the two readouts are the same quotient written the two ways the course writes it, and they agree at every h because they are the same fraction. For x² at a = 1 the quotient is exactly 2 + h, so the convergence is visible as arithmetic as well as geometry.</p>
  <style>
    .dv-panel{margin:.9rem 0 0;padding-top:.8rem;border-top:1px solid var(--line)}
    .dv-line{font-size:1rem;line-height:1.85;color:var(--ink);font-variant-numeric:tabular-nums}
    .dv-gap{font-size:.9rem;color:var(--muted);margin-top:.3rem}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('dv-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var PADL=46,PADR=22,TOP=16,AXIS=H-30;
  var $=function(i){ return document.getElementById(i); };

  var FN=[
    { name:'x²',    f:function(x){ return x*x; },   d:function(x){ return 2*x; },
      a:1, xlo:-0.6, xhi:2.6, ylo:-0.8, yhi:6.2, exact:'2 + h' },
    { name:'x³',    f:function(x){ return x*x*x; }, d:function(x){ return 3*x*x; },
      a:1, xlo:-0.6, xhi:2.3, ylo:-1.2, yhi:8.2, exact:'3 + 3h + h²' },
    { name:'sin x', f:Math.sin,                     d:Math.cos,
      a:0, xlo:-2.2, xhi:2.2, ylo:-1.6, yhi:1.6, exact:'sin(h)/h' }
  ];
  var k=0;
  function F(){ return FN[k]; }
  // |v| = 1 is h = 0.001 and |v| = 301 is h = 1, so every power of ten is
  // reachable exactly on both sides. v = 0 is treated as +0.001; h is never 0.
  function Hval(){
    var v=+$('dv-h').value;
    var mag=Math.pow(10, Math.max(Math.abs(v)-1,0)/100 - 3);
    return (v<0?-1:1)*mag;
  }
  function px(x){ var g=F(); return PADL+(x-g.xlo)/(g.xhi-g.xlo)*(W-PADL-PADR); }
  function py(y){ var g=F(); return AXIS-(y-g.ylo)/(g.yhi-g.ylo)*(AXIS-TOP); }

  function draw(){
    var g=F(), h=Hval(), a=g.a, fa=g.f(a), fb=g.f(a+h);
    var q=(fb-fa)/h, dtrue=g.d(a);
    c.clearRect(0,0,W,H);
    // axes
    c.strokeStyle=LINE; c.lineWidth=1;
    if(g.ylo<=0&&g.yhi>=0){ c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke(); }
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    for(var t=Math.ceil(g.xlo); t<=Math.floor(g.xhi); t++){
      if(t===0 && g.ylo<=0 && g.yhi>=0) continue;
      c.fillText(String(t),px(t),AXIS+13);
    }
    // tangent at the anchor, as the destination
    c.strokeStyle=PALE; c.lineWidth=1.6; c.setLineDash([5,4]);
    c.beginPath();
    c.moveTo(px(g.xlo), py(fa+dtrue*(g.xlo-a)));
    c.lineTo(px(g.xhi), py(fa+dtrue*(g.xhi-a)));
    c.stroke(); c.setLineDash([]);
    // the curve
    c.strokeStyle=INK; c.lineWidth=2; c.beginPath();
    for(var i=0;i<=700;i++){
      var x=g.xlo+(g.xhi-g.xlo)*i/700, y=g.f(x);
      if(y<g.ylo-2||y>g.yhi+2){ continue; }
      i?c.lineTo(px(x),py(y)):c.moveTo(px(x),py(y));
    }
    c.stroke();
    // the secant, which is the line the definition actually builds
    c.strokeStyle=MUTED; c.lineWidth=1.8;
    c.beginPath();
    c.moveTo(px(g.xlo), py(fa+q*(g.xlo-a)));
    c.lineTo(px(g.xhi), py(fa+q*(g.xhi-a)));
    c.stroke();
    // the two points
    c.fillStyle=INK; c.beginPath(); c.arc(px(a),py(fa),4.6,0,7); c.fill();
    c.fillStyle='#fff'; c.strokeStyle=INK; c.lineWidth=2.2;
    c.beginPath(); c.arc(px(a+h),py(fb),4.6,0,7); c.fill(); c.stroke();
    // labels
    c.fillStyle=INK; c.font='700 11px '+FONT; c.textAlign='left';
    c.fillText('a = '+a, px(a)+8, py(fa)+16);
    c.fillStyle=MUTED;
    c.fillText('a + h = '+(a+h).toFixed(4), px(a+h)+8, py(fb)-8);
    c.fillStyle=FAINT; c.font='700 10px '+FONT; c.textAlign='right';
    c.fillText('tangent, slope '+dtrue, W-PADR, TOP+10);
    render(h,q,dtrue,a,fa,fb);
  }

  function render(h,q,dtrue,a,fa,fb){
    var g=F();
    var hs=(h>0?'+':'')+h.toFixed(4).replace(/0+$/,'').replace(/\.$/,'');
    $('dv-hform').innerHTML =
      '<strong>[ f(a+h) &minus; f(a) ] / h</strong> &nbsp;=&nbsp; [ ' + fb.toFixed(6) +
      ' &minus; ' + fa.toFixed(6) + ' ] / ' + hs + ' &nbsp;=&nbsp; <strong>' + q.toFixed(6) + '</strong>';
    $('dv-2form').innerHTML =
      '<strong>[ f(x) &minus; f(a) ] / (x &minus; a)</strong> &nbsp;=&nbsp; [ ' + fb.toFixed(6) +
      ' &minus; ' + fa.toFixed(6) + ' ] / ( ' + (a+h).toFixed(4) + ' &minus; ' + a +
      ' ) &nbsp;=&nbsp; <strong>' + q.toFixed(6) + '</strong>';
    $('dv-gap').textContent =
      'h = ' + hs + '.  In closed form the quotient is ' + g.exact +
      '.  It is ' + Math.abs(q-dtrue).toFixed(6) + ' away from f′(' + a + ') = ' + dtrue + '.';
  }
  Array.prototype.forEach.call(document.querySelectorAll('.dv-f'),function(b){
    b.addEventListener('click',function(){
      k=+b.getAttribute('data-k');
      Array.prototype.forEach.call(document.querySelectorAll('.dv-f'),function(o){
        o.classList[o===b?'add':'remove']('is-active'); });
      draw();
    });
  });
  $('dv-h').addEventListener('input',draw);
  draw();
})();
</script>

The dark line is the secant through the two points. The faint line is the tangent line corresponding to the limiting slope.

Start with $$f(x)=x^2$$ at $$a=1$$. The difference quotient is $$\tfrac{(1+h)^2-1}{h}$$, and expanding gives $$\tfrac{2h+h^2}{h}=2+h$$ for $$h\neq0$$, so as $$h\to0$$ the quotient approaches 2. Numerically, the secant slopes at $$h=1,\ 0.1,\ 0.01,\ 0.001$$ are 3, 2.1, 2.01, and 2.001, so the slope approaches 2. The [cancellation of $$h$$](/2026/07/30/indeterminate-forms.html) is valid because the limit never evaluates the quotient at $$h=0$$. It only examines values arbitrarily close to zero.

Now use negative values of $$h$$. The second point moves to the other side of the anchor, and the secant slopes approach 2 from that direction as well. A two-sided derivative exists only when the left-hand and right-hand difference quotients approach the same finite value.

## Two forms of the same definition

The derivative is commonly written in either of these forms:

$$f'(a) = \lim_{h\to0} \frac{f(a+h)-f(a)}{h}
\qquad\text{or}\qquad
f'(a) = \lim_{x\to a} \frac{f(x)-f(a)}{x-a}$$

These are the same limit. If $$x=a+h$$, then $$x-a=h$$, and the second quotient becomes the first. The $$h$$-form is often easier for computation because the quantity approaching zero appears directly, while the $$x$$-form is useful for recognition, since AP questions may present a limit and ask which derivative it represents. The main task is to recognize the structure of the difference quotient.

## Derivative notation

[Several notations](/2026/07/08/notation-that-costs-ap-calculus-points.html) describe the same derivative: $$f'(a),\; \left.\tfrac{dy}{dx}\right\vert_{x=a},\; y'$$. Prime notation is compact and keeps the function name visible, while Leibniz notation keeps the dependent and independent variables visible, which becomes especially useful in the chain rule, implicit differentiation, and related rates.

The evaluation bar also matters. On its own, $$\tfrac{dy}{dx}$$ is generally a function of $$x$$, while $$\left.\tfrac{dy}{dx}\right\vert_{x=a}$$ is the value of that derivative at one point.

## The tangent line

The tangent line is determined by the derivative. Once the limiting secant slope exists, the tangent line is the line through the point whose slope equals that limit. This is more precise than saying that a tangent line “touches the curve once.” A tangent line can cross the graph, and it can also meet the same curve again elsewhere. For example, the tangent to $$\sin x$$ at the origin is $$y=x$$, and it crosses the sine curve rather than merely touching it from one side. The defining feature is the limiting slope of the secants.

<div class="article-note" markdown="1">
Use the sine example in the visualization. At $$a=0$$ the difference quotient becomes $$\tfrac{\sin h}{h}$$, and as $$h\to0$$ this approaches 1, so $$\left.\tfrac{d}{dx}\sin x\right\vert_{x=0}=1$$. This connects the derivative directly back to a standard limit from the previous unit.
</div>
