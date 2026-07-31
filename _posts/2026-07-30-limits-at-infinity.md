---
layout: post
title: "Limits at infinity and end behavior"
date: 2026-07-30
description: "Infinite limits and limits at infinity are nearly the same phrase and opposite ideas. One describes a vertical asymptote, the other end behavior, and the three cases for a rational function follow from a single move."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "7 min read"
math: true
kind: mechanics
sequence: 5
interactive: true
blurb: "Two phrases one word apart, describing opposite things"
---

Two phrases in this unit are one word apart and mean opposite things.

An *infinite limit* is a limit whose output runs off: the input goes to a finite number and the function grows without bound. That is [a vertical asymptote](/2026/07/30/continuity-three-conditions.html), and the framework counts it among the ways continuity fails. A *limit at infinity* is the reverse: the input runs off and the output settles. That is end behavior, and where the output settles on a number, it is a horizontal asymptote.

The framework keeps them as separate topics for that reason. Limits at infinity describe end behavior, and the whole of this article is one question: for large $$x$$, what does the function look like?

## The three cases

For a rational function the answer depends only on which degree is larger. Set the two degrees below and zoom out.

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
    // vertical window: cover the asymptote and the visible values
    var ys=[], N=400;
    for(i=1;i<=N;i++){ y=f(xm*i/N); if(isFinite(y)) ys.push(y); }
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

Three cases, and the degrees decide which:

- **Denominator degree larger.** The limit is 0, and $$y = 0$$ is the horizontal asymptote.
- **Degrees equal.** The limit is the ratio of the leading coefficients — not of the whole expressions, and not of the constant terms.
- **Numerator degree larger.** There is no horizontal asymptote. The quotient grows without bound, and the honest answer names the direction rather than stopping at "does not exist."

Set the numerator to degree 3 and the denominator to degree 1, then zoom out, and watch the readout climb past anything the window can hold. Now set both degrees to 1, leaving $$a = 3$$ and $$b = 2$$, and the curve flattens onto $$y = 1.5$$ from below.

## The move that produces all three

There is one technique, and the three cases are what it returns. Divide numerator and denominator by the highest power of $$x$$ appearing in the *denominator*, then let every term of the form $$1/x^k$$ go to zero.

For $$\tfrac{3x + 2}{2x + 5}$$, divide top and bottom by $$x$$:

$$\frac{3x+2}{2x+5} = \frac{3 + \tfrac{2}{x}}{2 + \tfrac{5}{x}} \longrightarrow \frac{3 + 0}{2 + 0} = \frac{3}{2}.$$

The same division on $$\tfrac{3x+2}{2x^2+5x}$$ uses $$x^2$$ and sends the numerator's terms to zero while the denominator keeps its 2, giving 0. On $$\tfrac{3x^2+2x}{2x+5}$$ it leaves an $$x$$ upstairs that nothing cancels, and the expression grows.

Reading the degrees off is faster, and on a multiple-choice question that is what you should do. The division is what you write when a question asks you to justify, and it is the only version that survives a function that is not a quotient of polynomials.

## Beyond rational functions

Comparing relative magnitudes is its own listed skill, and outside rational functions the degree shortcut has nothing to say. Three facts carry most of it, in increasing order of growth: logarithms, then powers, then exponentials.

$$\lim_{x \to \infty} \frac{\ln x}{x} = 0, \qquad \lim_{x \to \infty} \frac{x^{100}}{e^x} = 0, \qquad \lim_{x \to \infty} \frac{e^x}{x^{100}} = \infty.$$

The exponent 100 is not a typo and not a special case: any fixed power loses to $$e^x$$ eventually. But "eventually" can be a long way off, and it is worth knowing how far. Differentiating $$100\ln x - x$$ shows that $$x^{100}/e^x$$ climbs until $$x = 100$$ exactly, where it peaks near $$3.7 \times 10^{156}$$, and it does not fall below 1 until about $$x = 647$$. A graphing window will tell you the opposite of the truth over that whole stretch, which is why the comparison is settled by a limit rather than by looking.

A useful sanity check when the function is not rational: ask which piece grows fastest, divide by it, and see what survives. That is the same move as before, with "highest power in the denominator" replaced by "fastest-growing term in sight."

<div class="article-note" markdown="1">
A self-test at the sliders: set both degrees to 2 with $$a = 3$$ and $$b = -6$$, and predict the horizontal asymptote before looking. Then set the numerator to degree 3 and, without changing anything else, say what happens to the answer and why the dashed line disappears. The second question is the one that separates students who read the rule from students who understand what the division does.
</div>
