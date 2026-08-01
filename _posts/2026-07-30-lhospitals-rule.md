---
layout: post
title: "Checking the form before L'Hospital's rule"
date: 2026-07-30
description: "The rule replaces a quotient of functions with a quotient of their derivatives. It has hypotheses, they have to be checked first, and the rule is silent more often than students expect."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: mechanics
sequence: 16
interactive: true
blurb: "The rule is silent more often than students expect"
---

L'Hospital's rule is a conditional, and almost every error with it comes from using the conclusion without having established the condition. It is easy to apply and easy to apply where it does not belong, and those are not separate facts about it.

The framework spells the name without a circumflex, and its enduring understanding for the topic is worth reading with attention to one word: the rule allows us to determine the limits of *some* indeterminate forms.

## What has to be true first

A form is indeterminate when the ratio of two functions tends to $$\tfrac00$$ or $$\tfrac{\infty}{\infty}$$ — the framework's definition, and the only two forms the AP exam will assess. The rule then says: if $$f$$ and $$g$$ are differentiable near $$a$$ with $$g' \neq 0$$ there, if the quotient is one of those two forms, and if $$\lim \tfrac{f'}{g'}$$ exists, then

$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}.$$

Three conditions, and the exam's guidance singles out the second: students must verify that the numerator and denominator both tend to zero, or that both tend to infinity, as a necessary first step. Not as a formality. As the thing that makes the next line true.

Three notational points the framework also makes explicitly. Writing $$\lim \tfrac{f}{g} = \tfrac00$$ is incorrect, because $$\tfrac00$$ is a label for a situation rather than a value in an equation. The limit of a quotient is not the quotient of the limits when the denominator's limit is zero — [that rule has a hypothesis too](/2026/07/30/what-a-limit-claims.html), and this is precisely the case it excludes. And the conclusion is the ratio of the two derivatives, $$\tfrac{f'}{g'}$$, which is not the derivative of the ratio.

## Two curves, and whether they meet

Below, the dark curve is $$\tfrac{f}{g}$$ and the pale one is $$\tfrac{f'}{g'}$$. When the rule applies, they arrive at the same height at the target. When it does not, watching them is more instructive than any warning.

<div class="viz" markdown="0">
  <div class="viz-controls" id="lh-fns"></div>
  <canvas id="lh-cv" width="700" height="320"></canvas>
  <div class="viz-controls">
    <label for="lh-x">x, moving toward the target</label>
    <input type="range" id="lh-x" min="0" max="1200" step="1" value="900">
  </div>
  <div class="lh-read" id="lh-read"></div>
  <p class="viz-caption">Five limits. The panel checks the form before it does anything else, and says in words what the check found. The dashed horizontal line is the true limit where one exists. On the first three the two curves converge on that line together, which is the rule working. On the fourth the form is not indeterminate at all and the derivative ratio runs off to infinity while the function ratio walks calmly to 1. On the fifth the form is genuinely infinity over infinity, the hypotheses about differentiability hold, and the derivative ratio still has no limit — so the rule concludes nothing, even though the original limit exists and equals 1.</p>
  <style>
    .lh-read{margin:.7rem 0 0;padding-top:.7rem;border-top:1px solid var(--line);
      font-size:.95rem;line-height:1.9;color:var(--ink);font-variant-numeric:tabular-nums}
    .lh-read .lh-lab{color:var(--muted);display:inline-block;min-width:12.5rem}
    .lh-read .lh-val{font-weight:700;display:inline-block;min-width:7.5rem}
    .lh-read .lh-note{color:var(--muted);font-weight:400}
  </style>
</div>

<script>
(function(){
  'use strict';
  var cv=document.getElementById('lh-cv'), c=cv.getContext('2d');
  var W=cv.width,H=cv.height, d__=Math.min(window.devicePixelRatio||1,2);
  cv.width=W*d__; cv.height=H*d__; c.setTransform(d__,0,0,d__,0,0);
  var INK='#1f1f1f',MUTED='#5c5c5c',LINE='#e6e6e6',FAINT='#9a9a97',PALE='#d6d6d3';
  var FONT='Hanken Grotesk, sans-serif';
  var $=function(i){ return document.getElementById(i); };
  var PADL=42,PADR=18,TOP=28,BOT=H-24;
  var sin=Math.sin, cos=Math.cos, exp=Math.exp;

  // x runs over 10^(lo .. hi). Sliding right always moves toward the target,
  // whichever direction that is: for x -> 0 the exponent decreases, for
  // x -> infinity it increases. Slider 1200 is the closest approach in both cases.
  var E=[
    { n:'sin x / x   as x → 0', lo:-3, hi:Math.log10(2), rev:false,
      f:sin, g:function(x){return x;}, df:cos, dg:function(){return 1;},
      fl:'→ 0', gl:'→ 0', form:'0/0', L:1,
      fn:'indeterminate, so the rule applies',
      ln:'and f′/g′ arrives at the same value',
      ylo:-0.7, yhi:1.35 },
    { n:'(1 − cos x) / x²   as x → 0', lo:-3, hi:Math.log10(3), rev:false,
      f:function(x){return 1-cos(x);}, g:function(x){return x*x;},
      df:sin, dg:function(x){return 2*x;},
      fl:'→ 0', gl:'→ 0', form:'0/0', L:0.5,
      fn:'indeterminate, so the rule applies &mdash; and again after the first pass',
      ln:'and f′/g′ arrives at the same value',
      ylo:-0.08, yhi:0.62 },
    { n:'x² / eˣ   as x → ∞', lo:0, hi:Math.log10(30), rev:true,
      f:function(x){return x*x;}, g:exp,
      df:function(x){return 2*x;}, dg:exp,
      fl:'→ ∞', gl:'→ ∞', form:'∞/∞', L:0,
      fn:'indeterminate, so the rule applies',
      ln:'and f′/g′ arrives at the same value',
      ylo:-0.1, yhi:0.9 },
    { n:'(x + 1) / (x² + 1)   as x → 0', lo:-3, hi:Math.log10(2), rev:false,
      f:function(x){return x+1;}, g:function(x){return x*x+1;},
      df:function(){return 1;}, dg:function(x){return 2*x;},
      fl:'→ 1', gl:'→ 1', form:'1/1', L:1,
      fn:'not an indeterminate form &mdash; the rule does not apply',
      ln:'found by evaluating the quotient, not by the rule',
      ylo:-0.2, yhi:3.2 },
    { n:'(x + sin x) / x   as x → ∞', lo:0, hi:Math.log10(40), rev:true,
      f:function(x){return x+sin(x);}, g:function(x){return x;},
      df:function(x){return 1+cos(x);}, dg:function(){return 1;},
      fl:'→ ∞', gl:'→ ∞', form:'∞/∞', L:1,
      fn:'indeterminate, so the form condition holds',
      ln:'but lim f′/g′ does not exist, so the rule concludes nothing',
      ylo:-0.25, yhi:2.35 }
  ];
  var k=0;
  function G(){ return E[k]; }
  function xat(s){ var g=G();
    return Math.pow(10, g.rev ? g.lo+(g.hi-g.lo)*s : g.hi-(g.hi-g.lo)*s); }
  function px(x){ var g=G(); return PADL+(Math.log10(x)-g.lo)/(g.hi-g.lo)*(W-PADL-PADR); }
  function py(y){ var g=G(); return BOT-(y-g.ylo)/(g.yhi-g.ylo)*(BOT-TOP); }
  // Every quantity here ranges over decades — x runs on a log slider and f′/g′
  // can pass 500 — so significant figures rather than decimal places, or the
  // printed x is too coarse to check the printed ratio against.
  function fmt(v){ if(!isFinite(v)) return v>0?'+∞':'−∞';
    var a=Math.abs(v);
    if(a<1e-12) return (0).toFixed(4);
    if(a<1e-4||a>=1e5) return v.toExponential(4);
    return v.toPrecision(5); }

  var bar=$('lh-fns');
  E.forEach(function(e,i){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ k=i; draw(); });
    bar.appendChild(b);
  });

  function curve(h,style,width){
    var g=G(), i, first=true;
    c.strokeStyle=style; c.lineWidth=width; c.beginPath();
    for(i=0;i<=900;i++){
      var x=Math.pow(10, g.lo+(g.hi-g.lo)*i/900), y=h(x);
      if(!isFinite(y) || y<g.ylo-8 || y>g.yhi+8){ first=true; continue; }
      if(first){ c.moveTo(px(x),py(y)); first=false; } else c.lineTo(px(x),py(y));
    }
    c.stroke();
  }

  function draw(){
    var g=G(), s=(+$('lh-x').value)/1200, x=xat(s);
    Array.prototype.forEach.call(bar.children,function(b,i){
      b.classList[i===k?'add':'remove']('is-active');
    });
    c.clearRect(0,0,W,H);
    c.save(); c.beginPath(); c.rect(PADL-1,TOP-10,W-PADL-PADR+2,BOT-TOP+16); c.clip();

    // decade gridlines, since the axis is logarithmic
    c.strokeStyle=LINE; c.lineWidth=1;
    for(var d=Math.ceil(g.lo); d<=g.hi; d++){
      c.beginPath(); c.moveTo(px(Math.pow(10,d)),TOP); c.lineTo(px(Math.pow(10,d)),BOT); c.stroke();
    }
    if(g.ylo<0&&g.yhi>0){ c.strokeStyle=PALE;
      c.beginPath(); c.moveTo(PADL,py(0)); c.lineTo(W-PADR,py(0)); c.stroke(); }

    // the true limit
    c.strokeStyle=PALE; c.lineWidth=1.4; c.setLineDash([6,4]);
    c.beginPath(); c.moveTo(PADL,py(g.L)); c.lineTo(W-PADR,py(g.L)); c.stroke();
    c.setLineDash([]);

    curve(function(x){ return g.df(x)/g.dg(x); }, FAINT, 2);
    curve(function(x){ return g.f(x)/g.g(x);   }, INK,   2);

    var q=g.f(x)/g.g(x), r=g.df(x)/g.dg(x);
    c.strokeStyle=LINE; c.lineWidth=1;
    c.beginPath(); c.moveTo(px(x),TOP); c.lineTo(px(x),BOT); c.stroke();
    if(isFinite(q)){ c.fillStyle=INK;   c.beginPath(); c.arc(px(x),py(q),4.5,0,6.284); c.fill(); }
    if(isFinite(r)&&r<g.yhi+8&&r>g.ylo-8){
      c.fillStyle=FAINT; c.beginPath(); c.arc(px(x),py(r),4.5,0,6.284); c.fill(); }
    c.restore();
    c.fillStyle=MUTED; c.font='700 10px '+FONT; c.textAlign='left';
    c.fillText('f / g  and  f′ / g′        the target is at the '+
      (g.rev?'right':'left')+' edge', PADL, TOP-12);

    function row(l,v,n){ return '<div><span class="lh-lab">'+l+'</span>'+
      '<span class="lh-val">'+v+'</span>'+(n?'<span class="lh-note">'+n+'</span>':'')+'</div>'; }
    $('lh-read').innerHTML =
      row('x', fmt(x), '') +
      row('f(x)', fmt(g.f(x)), g.fl) +
      row('g(x)', fmt(g.g(x)), g.gl) +
      row('f(x) / g(x)', fmt(q), '') +
      row('f&prime;(x) / g&prime;(x)', fmt(r), '') +
      row('form check', g.form, g.fn) +
      row('the limit is', fmt(g.L), g.ln);
  }
  $('lh-x').addEventListener('input',draw);
  draw();
})();
</script>

The first three are the rule doing its job. On $$\tfrac{\sin x}{x}$$ one application gives $$\tfrac{\cos x}{1}$$, which walks straight to 1. On $$\tfrac{x^2}{e^x}$$ two applications reduce the numerator to a constant, and the limit is 0 — which is [the growth-rate comparison](/2026/07/30/limits-at-infinity.html) from Unit 1 arrived at by a different road.

The middle one shows the pattern that matters:

$$\lim_{x\to 0}\frac{1-\cos x}{x^2} \;\overset{\tfrac00}{=}\; \lim_{x\to 0}\frac{\sin x}{2x} \;\overset{\tfrac00}{=}\; \lim_{x\to 0}\frac{\cos x}{2} = \frac12.$$

The second quotient is indeterminate again, so the check has to be made a second time before the second application. Two uses of the rule means two verifications, not one.

## The two ways it goes wrong

The fourth limit is not indeterminate. Both $$x+1$$ and $$x^2+1$$ tend to 1, so the quotient tends to 1 and there is nothing to do. Apply the rule anyway and you get $$\tfrac{1}{2x}$$, which runs to infinity. The verification step is not bookkeeping; skipping it here turns a limit of 1 into a limit of $$\infty$$.

The fifth is subtler, and it is why the framework says *some*. The quotient $$\tfrac{x + \sin x}{x}$$ is honestly $$\tfrac{\infty}{\infty}$$, and $$f$$ and $$g$$ are differentiable everywhere, so the first two conditions hold. But $$\tfrac{f'}{g'} = 1 + \cos x$$ oscillates between 0 and 2 forever and has no limit, so the third condition fails and the rule says nothing at all.

That is not the same as saying the original limit fails to exist. It equals 1, which you can see by writing $$\tfrac{x+\sin x}{x} = 1 + \tfrac{\sin x}{x}$$ and letting the second term vanish. The rule is a one-way street: if $$\lim \tfrac{f'}{g'}$$ exists it tells you $$\lim \tfrac{f}{g}$$, and if it does not exist it tells you nothing.

## What to write down

The topic's suggested skill is to apply an appropriate definition, theorem, or test, and a theorem applied on paper looks like its hypotheses being checked. In practice that is one sentence before the work:

Since $$\lim_{x\to 0}(1-\cos x) = 0$$ and $$\lim_{x\to 0} x^2 = 0$$, the quotient has indeterminate form $$\tfrac00$$, so L'Hospital's rule applies.

Then the differentiation, and then — if the new quotient is still indeterminate — the same sentence again for the second application.

The framework treats this as more than a preference. Its resource list for the topic points three separate documents at a single released free-response part — the scoring guidelines, the samples and commentary, and the chief reader report, all for question 5(d) from 2018. It also lists two teacher discussions, one of them titled "Possible Inconsistent Language". Three documents and a warning about wording, for one part of one problem.

<div class="article-note" markdown="1">
Before reaching for the rule, check whether [ordinary algebra](/2026/07/30/indeterminate-forms.html) resolves the form. Factoring, rationalising, and dividing by the highest power all handle large families of $$\tfrac00$$ and $$\tfrac{\infty}{\infty}$$ limits without any theorem, and they never require you to argue that a hypothesis holds. The rule is worth saving for the quotients that algebra cannot reach.
</div>
