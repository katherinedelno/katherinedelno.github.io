---
layout: post
title: "Limits at infinity and end behavior"
date: 2026-07-30
description: "Limits at infinity describe end behavior. For rational functions, the leading terms determine what survives."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "7 min read"
math: true
kind: mechanics
sequence: 5
interactive: true
blurb: "Limits at infinity describe end behavior. For rational functions, the leading terms determine what survives"
image: "/assets/og/limits-at-infinity.png"
---

An infinite limit and a limit at infinity are different ideas.

In an infinite limit, the input approaches a finite number while the output grows without bound. This is the behavior associated with [a vertical asymptote](/2026/07/30/continuity-three-conditions.html).

In a limit at infinity, the input grows without bound and we ask what happens to the output.

That is a question about end behavior.

For example,

$$\lim_{x\to\infty}f(x)=L$$

means that $$f(x)$$ approaches $$L$$ as $$x$$ becomes arbitrarily large.

If $$L$$ is finite, then $$y=L$$ is a horizontal asymptote.

## Three cases for rational functions

For a rational function, the end behavior can be read from the degrees of the numerator and denominator.

Use the controls below to change those degrees and then zoom out.

<div class="viz" markdown="0">
  <canvas id="ei-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="ei-p">Numerator</label>
    <span class="viz-value" id="ei-nlab" style="min-width:9ch"></span>
    <input type="range" id="ei-p" min="0" max="3" step="1" value="1">
    <label for="ei-a">a</label>
    <input type="range" id="ei-a" min="-6" max="6" step="1" value="3">
  </div>
  <div class="viz-controls">
    <label for="ei-q">Denominator</label>
    <span class="viz-value" id="ei-dlab" style="min-width:9ch"></span>
    <input type="range" id="ei-q" min="0" max="3" step="1" value="1">
    <label for="ei-b">b</label>
    <input type="range" id="ei-b" min="-6" max="6" step="1" value="2">
  </div>
  <div class="viz-controls">
    <label for="ei-z">Zoom out to x =</label>
    <input type="range" id="ei-z" min="0" max="300" step="1" value="100">
    <span class="viz-value" id="ei-read" style="min-width:100%"></span>
  </div>
  <p class="viz-caption">The curve is drawn out to whatever x the zoom reaches, so the shape you see is the end behavior rather than the interesting part near the origin. Where a horizontal asymptote exists it is drawn as a dashed line, and the readout gives the function's value at the right edge of the window so the approach can be checked numerically as well as visually. Degrees equal: the ratio of leading coefficients. Denominator larger: zero. Numerator larger: no horizontal asymptote, and the readout says which way it goes.</p>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('ei-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97';
  var FONT='Hanken Grotesk, sans-serif';
  var PADL=48,PADR=20,TOP=16,AXIS=H-34;
  var $=function(i){ return document.getElementById(i); };

  function P(){ return +$('ei-p').value; }
  function Q(){ return +$('ei-q').value; }
  function A(){ var v=+$('ei-a').value; return v===0?1:v; }
  function B(){ var v=+$('ei-b').value; return v===0?1:v; }
  function XMAX(){ return Math.pow(10, 0.5 + (+$('ei-z').value)/100); }

  // numerator a x^p + 2 x^(p-1), denominator b x^q + 5 x^(q-1); degrees exactly p and q
  function num(x){ var p=P(); return p===0 ? A() : A()*Math.pow(x,p) + 2*Math.pow(x,p-1); }
  function den(x){ var q=Q(); return q===0 ? B() : B()*Math.pow(x,q) + 5*Math.pow(x,q-1); }
  function f(x){ var d=den(x); return d===0 ? NaN : num(x)/d; }

  function limitInfo(){
    var p=P(), q=Q(), a=A(), b=B();
    if(p<q)  return { kind:'zero', L:0,   text:'0' };
    if(p===q) return { kind:'ratio', L:a/b, text:(a/b).toFixed(4).replace(/0+$/,'').replace(/\.$/,'') };
    return { kind:'none', L:null, text:(a/b>0?'+∞':'−∞') };
  }
  function poly(deg, lead, second){
    if(deg===0) return String(lead);
    var s=(lead===1?'':lead===-1?'−':String(lead))+'x'+(deg>1?'^'+deg:'');
    if(deg-1===0) s+=' + '+second;
    else s+=' + '+second+'x'+(deg-1>1?'^'+(deg-1):'');
    return s;
  }

  function draw(){
    var xm=XMAX(), info=limitInfo(), i, x, y;
    // A negative b puts a zero of the denominator inside the window. That is a
    // vertical asymptote, which is the other topic entirely, and if its spike is
    // allowed to set the vertical scale then the horizontal asymptote and the
    // curve are squashed into one flat line. So find the poles first and keep a
    // margin around them out of the scaling.
    var N=400, poles=[], dprev=den(xm/N), dv;
    for(i=2;i<=N;i++){
      x=xm*i/N; dv=den(x);
      if(dv===0 || dprev*dv<0) poles.push(x);
      dprev=dv;
    }
    var guard=xm*0.06;
    // vertical window: cover the asymptote and the visible values
    var ys=[];
    for(i=1;i<=N;i++){
      x=xm*i/N;
      if(poles.some(function(p){ return Math.abs(x-p)<guard; })) continue;
      y=f(x); if(isFinite(y)) ys.push(y);
    }
    if(!ys.length) ys=[0,1];
    var lo=Math.min.apply(null,ys), hi=Math.max.apply(null,ys);
    if(info.L!==null){ lo=Math.min(lo,info.L); hi=Math.max(hi,info.L); }
    if(hi-lo<1e-9){ hi=lo+1; }
    var padY=(hi-lo)*0.18; lo-=padY; hi+=padY;
    function px(v){ return PADL+v/xm*(W-PADL-PADR); }
    function py(v){ return AXIS-(v-lo)/(hi-lo)*(AXIS-TOP); }
    c.clearRect(0,0,W,H);
    // axes
    c.strokeStyle=LINE; c.lineWidth=1;
    if(lo<=0&&hi>=0){ c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke(); }
    c.beginPath(); c.moveTo(PADL+0.5,TOP); c.lineTo(PADL+0.5,AXIS); c.stroke();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='center';
    for(i=0;i<=4;i++){
      var xv=xm*i/4;
      c.fillText(xv>=1000?xv.toExponential(0):String(Math.round(xv)), px(xv), AXIS+14);
    }
    c.textAlign='right';
    [lo+ (hi-lo)*0.02, (lo+hi)/2, hi-(hi-lo)*0.02].forEach(function(v){
      c.fillText(v.toFixed(2), PADL-6, py(v)+3);
    });
    // horizontal asymptote
    if(info.L!==null){
      c.strokeStyle=FAINT; c.setLineDash([5,4]); c.lineWidth=1.5;
      c.beginPath(); c.moveTo(PADL,py(info.L)); c.lineTo(W-PADR,py(info.L)); c.stroke();
      c.setLineDash([]);
      c.fillStyle=FAINT; c.font='700 11px '+FONT; c.textAlign='left';
      c.fillText('y = '+info.text, PADL+6, py(info.L)-6);
    }
    // curve
    c.strokeStyle=INK; c.lineWidth=2; c.beginPath();
    var on=false;
    for(i=1;i<=1400;i++){
      x=xm*i/1400; y=f(x);
      if(!isFinite(y)||y<lo-(hi-lo)||y>hi+(hi-lo)){ on=false; continue; }
      on?c.lineTo(px(x),py(y)):(c.moveTo(px(x),py(y)),on=true);
    }
    c.stroke();
    $('ei-nlab').textContent=poly(P(),A(),2);
    $('ei-dlab').textContent=poly(Q(),B(),5);
    var edge=f(xm);
    var why = info.kind==='zero'
        ? 'the denominator has the higher degree, so the quotient is driven to 0'
      : info.kind==='ratio'
        ? 'the degrees match, so the limit is the ratio of leading coefficients, '+A()+'/'+B()
        : 'the numerator has the higher degree, so the quotient grows without bound and there is no horizontal asymptote';
    $('ei-read').textContent='at x = '+(xm>=1000?xm.toExponential(1):xm.toFixed(0))+
      ',  f(x) = '+(isFinite(edge)?edge.toFixed(6):'—')+
      '.   Limit as x → ∞ is '+info.text+': '+why+'.';
  }
  ['ei-p','ei-q','ei-a','ei-b','ei-z'].forEach(function(i){
    $(i).addEventListener('input',draw);
  });
  draw();
})();
</script>

The graph extends to the selected scale so you can see the end behavior rather than only the local shape near the origin.

There are three cases.

- If the denominator has higher degree, the limit is 0.
- If the degrees are equal, the limit is the ratio of the leading coefficients.
- If the numerator has higher degree, there is no finite horizontal asymptote.

For example, if the numerator and denominator are both degree 1 with leading coefficients 3 and 2, then

$$\lim_{x\to\infty}f(x)=\frac32.$$

If the denominator has higher degree, the denominator eventually dominates and the quotient approaches 0.

If the numerator has higher degree, the quotient does not settle to a finite number. Its end behavior depends on the leading terms and on whether $$x\to\infty$$ or $$x\to-\infty$$.

## Why the degree rule works

The degree rule is a shortcut for an algebraic argument.

Consider

$$\frac{3x+2}{2x+5}.$$

Divide numerator and denominator by $$x$$:

$$\frac{3x+2}{2x+5} = \frac{3+\frac2x}{2+\frac5x}.$$

As $$x\to\infty$$,

$$\frac2x\to0 \quad\text{and}\quad \frac5x\to0.$$

Therefore

$$\lim_{x\to\infty} \frac{3x+2}{2x+5} = \frac32.$$

If the denominator instead has degree 2, dividing by $$x^2$$ sends every term in the numerator to 0 while the leading denominator coefficient remains.

The limit is then 0.

If the numerator has higher degree, the same division leaves a positive power of $$x$$ in the numerator. That term does not disappear, so the quotient does not approach a finite horizontal asymptote.

On a multiple-choice problem, comparing degrees is usually the fastest method.

If a free-response problem asks for justification, the division makes the reasoning explicit.

## Beyond rational functions

The degree shortcut only applies to polynomial quotients.

For more general functions, compare their rates of growth.

A useful hierarchy is

$$\text{logarithms} < \text{powers} < \text{exponentials}.$$

For example,

$$\lim_{x\to\infty}\frac{\ln x}{x}=0,$$

$$\lim_{x\to\infty}\frac{x^{100}}{e^x}=0,$$

and

$$\lim_{x\to\infty}\frac{e^x}{x^{100}}=\infty.$$

The exponent 100 does not change the long-run ordering. Any fixed power of $$x$$ is eventually dominated by $$e^x$$.

The word “eventually” matters.

The function

$$\frac{x^{100}}{e^x}$$

actually increases until $$x=100$$. At that point it is extremely large. It does not fall below 1 until much later.

A graphing window over a moderate range can therefore suggest the wrong end behavior.

Limits describe what happens arbitrarily far out, not what happens on the portion of the graph that happens to fit on the screen.

## A useful comparison habit

When the function is not rational, ask which component grows fastest.

Then divide by that dominant term and see what remains.

This is the same logic used for rational functions. There, the dominant term is identified through polynomial degree. In a broader expression, you compare growth rates instead.

<div class="article-note" markdown="1">
A quick self-test is to set both degrees in the visualization to 2 with leading coefficients $$a=3$$ and $$b=-6$$.

Predict the horizontal asymptote before looking at the graph.

Then increase the numerator degree to 3 and explain why the finite horizontal asymptote disappears.

The useful question is not only which rule applies. It is what survives after the expression is scaled by its dominant term.
</div>
