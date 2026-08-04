---
layout: post
title: "The derivative as a limit"
date: 2026-07-30
description: "An average rate of change needs two points, and at a single instant there is only one. Drag the second point in and watch the secant line become the tangent, with the quotient converging as it goes."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: foundations
sequence: 7
interactive: true
blurb: "Drag the second point in until the secant has nowhere left to go"
image: "/assets/og/derivative-as-a-limit.png"
---

An average rate of change divides a change in one variable by a change in another, so it needs two points. At a single instant there is only one, the denominator would be zero, and the quotient is undefined. The framework states the obstacle in exactly those terms, and then states the way past it: the limit concept allows us to define instantaneous rate of change in terms of average rates of change.

That is the whole of the derivative. Not a new operation, but an old one — slope between two points — put under a limit so that the second point can be sent away without ever arriving.

## Drag the second point in

The anchor stays put. The second point moves, and with it the secant line through the pair. Watch the number, not just the picture.

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

Start with $$x^2$$ at $$a = 1$$ and push $$h$$ down. At $$h = 1$$ the quotient reads 3; at $$h = 0.1$$ it reads 2.1; at $$0.01$$, 2.01; at $$0.001$$, 2.001. The reason is printed alongside: for this function the difference quotient is exactly $$2 + h$$. Every bit of the algebra is

$$\frac{(1+h)^2 - 1^2}{h} = \frac{2h + h^2}{h} = 2 + h,$$

and the cancellation of $$h$$ is legal for the same reason cancellation was legal in the [indeterminate forms](/2026/07/30/indeterminate-forms.html) work: the limit never evaluates at $$h = 0$$, so $$h \neq 0$$ on every input it inspects.

Then take $$h$$ negative. The second point crosses to the other side, the secant approaches from below instead of above, and the quotient reads 1.9, 1.99, 1.999. Both one-sided approaches land on 2, which is what makes the two-sided limit exist at all. A function whose secants converge from one side and not the other has no derivative there.

## Two ways to write it, one limit

The course writes the definition in two forms, and students sometimes learn them as two facts.

$$f'(a) = \lim_{h \to 0}\frac{f(a+h) - f(a)}{h} = \lim_{x \to a}\frac{f(x) - f(a)}{x - a}.$$

They are the same quotient. Put $$x = a + h$$ and the second becomes the first: the numerators match, and the denominator $$x - a$$ *is* $$h$$. The readouts print both at every setting and the values never differ, because there is nothing to differ about.

What does change is which one is convenient. The $$h$$-form is easier to compute with, since $$h$$ is the thing you are sending to zero and it appears by itself. The $$x$$-form is easier to *recognize*, because exam questions hand you a limit and ask what derivative it represents, and they hand it to you in whichever form makes it least obvious.

## The notation, and what each piece of it says

The framework asks for a derivative to be represented three ways, and the reason is that they emphasize different things.

$$f'(a) \qquad \left.\frac{dy}{dx}\right\vert_{x=a} \qquad y'$$

Prime notation names the function and is compact. Leibniz notation, $$\tfrac{dy}{dx}$$, keeps both variables visible, which matters the moment there is more than one thing changing — it is the notation that survives into related rates and the chain rule, where you need to know what is being differentiated with respect to what. Its evaluation bar is not decoration: $$\tfrac{dy}{dx}$$ is a function and $$\left.\tfrac{dy}{dx}\right\vert_{x=a}$$ is a number, and writing the first when you mean the second is the kind of thing [notation in AP Calculus](/2026/07/08/notation-that-costs-ap-calculus-points.html) is about.

## What the tangent line has to do with it

The faint line in the picture is the tangent, and it is drawn as the destination rather than as a definition. That order matters. A tangent line is not defined first and its slope measured afterwards; the limit is computed first and *then* the line with that slope through that point is called the tangent.

This is why "the tangent touches at one point" is a description rather than a definition, and a poor one — the tangent to $$\sin x$$ at the origin crosses the curve and meets it again infinitely often. Switch to the third function and look. The line is tangent because its slope is the limit of the secant slopes, and for no other reason.

<div class="article-note" markdown="1">
A self-test at the slider: choose $$\sin x$$ at $$a = 0$$ and read the quotient at $$h = 0.1$$, then at $$h = 0.01$$. The values are $$\sin(h)/h$$, which you have met before as a limit that resists algebra and yields to the squeeze theorem. So the derivative of $$\sin x$$ at 0 is not a new fact obtained by a new method; it is a limit you already knew, wearing the definition as a costume. Ask yourself which other derivative rules are limits you have already computed.
</div>
