---
layout: post
title: "The chain rule, layer by layer"
date: 2026-07-30
description: "Composite functions are differentiated one layer at a time, with each layer contributing a factor."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "6 min read"
math: true
kind: mechanics
sequence: 10
interactive: true
blurb: "Composite functions are differentiated one layer at a time, with each layer contributing a factor"
featured: true
image: "/assets/og/chain-rule-reading-the-layers.png"
---

The chain rule is simple once a composite function has been read correctly. Most mistakes happen before the differentiation begins. A student sees several operations in one expression but does not identify [which function is inside which](/2026/07/30/functions-inside-functions.html), and the useful habit is to read the layers first.

## The rule

Suppose $$g$$ is differentiable at $$x$$, and $$h$$ is differentiable at $$g(x)$$. Then

$$(h\circ g)'(x) = h'(g(x))g'(x)$$

The two derivatives are evaluated at different inputs. The inner derivative $$g'(x)$$ is evaluated at $$x$$, and the outer derivative $$h'$$ is evaluated at the value produced by the inner function, $$g(x)$$.

In Leibniz notation, if $$u=g(x)$$, then $$\tfrac{dy}{dx} = \tfrac{dy}{du}\,\tfrac{du}{dx}$$. This notation is useful, but the symbols should not be treated as ordinary fractions. The underlying statement is the composition rule above.

For example, consider $$(3x+1)^5$$. The outer function is $$h(u)=u^5$$ and the inner function is $$g(x)=3x+1$$, so $$h'(u)=5u^4$$ and $$g'(x)=3$$, which gives

$$\frac{d}{dx}(3x+1)^5 = 5(3x+1)^4\cdot3 = 15(3x+1)^4$$

The final answer must be written back in terms of $$x$$.

## Reading the layers

The visualization below lists the layers of several composite functions from outside to inside.

<div class="viz" markdown="0">
  <div class="viz-controls" id="cl-fns"></div>
  <div class="cl-fx" id="cl-fx"></div>
  <div class="viz-controls">
    <label for="cl-x">x</label>
    <input type="range" id="cl-x" min="-150" max="150" step="1" value="80">
    <span class="viz-value" id="cl-xv"></span>
  </div>
  <div class="cl-stack" id="cl-stack"></div>
  <div class="cl-check" id="cl-check"></div>
  <p class="viz-caption">Seven composites. The stack lists the layers from the outside in; each row shows the factor that layer contributes and its value at the chosen x. The product row is the chain rule's answer, and the line beneath compares it against a slope measured directly from the function by a symmetric difference with a step of one hundred-thousandth. The two agree to four decimals at every position on the slider, for all seven functions, which is the point: the chain rule is not a mnemonic, it is a true statement about a number you could have measured instead.</p>
  <style>
    .cl-fx{font-size:1.6rem;font-weight:700;letter-spacing:-.02em;color:var(--ink);
      text-align:center;padding:14px 0 6px}
    .cl-stack{border-top:1px solid var(--line);margin-top:.5rem}
    .cl-row{display:flex;align-items:baseline;gap:.6rem;padding:7px 0;
      border-bottom:1px solid var(--line);font-size:.9rem}
    .cl-row .cl-tag{flex:0 0 5.4rem;color:var(--muted);font-size:.74rem;
      text-transform:uppercase;letter-spacing:.06em}
    .cl-row .cl-sym{flex:1 1 auto;color:var(--ink)}
    .cl-row .cl-num{flex:0 0 7.5rem;text-align:right;font-variant-numeric:tabular-nums;
      color:var(--ink);font-weight:700}
    .cl-prod{display:flex;align-items:baseline;gap:.6rem;padding:9px 0;font-size:.9rem}
    .cl-prod .cl-tag{flex:0 0 5.4rem;color:var(--muted);font-size:.74rem;
      text-transform:uppercase;letter-spacing:.06em}
    .cl-prod .cl-sym{flex:1 1 auto;color:var(--ink)}
    .cl-prod .cl-num{flex:0 0 7.5rem;text-align:right;font-variant-numeric:tabular-nums;
      font-weight:700;color:var(--ink)}
    .cl-check{font-size:.85rem;color:var(--muted);padding-top:2px}
  </style>
</div>

<script>
(function(){
  'use strict';
  var $=function(i){ return document.getElementById(i); };
  var sin=Math.sin, cos=Math.cos, exp=Math.exp, log=Math.log, pow=Math.pow;

  // Each entry: layers listed OUTSIDE IN. Every layer contributes one factor of x.
  var F=[
    { n:'(3x + 1)⁵', f:function(x){ return pow(3*x+1,5); },
      L:[ {t:'outer', s:'5(3x + 1)⁴', v:function(x){ return 5*pow(3*x+1,4); }},
          {t:'inner', s:'3',               v:function(x){ return 3; }} ] },
    { n:'sin(x²)', f:function(x){ return sin(x*x); },
      L:[ {t:'outer', s:'cos(x²)', v:function(x){ return cos(x*x); }},
          {t:'inner', s:'2x',         v:function(x){ return 2*x; }} ] },
    { n:'(sin x)²', f:function(x){ return pow(sin(x),2); },
      L:[ {t:'outer', s:'2 sin x', v:function(x){ return 2*sin(x); }},
          {t:'inner', s:'cos x',   v:function(x){ return cos(x); }} ] },
    { n:'e^(sin x)', f:function(x){ return exp(sin(x)); },
      L:[ {t:'outer', s:'e^(sin x)', v:function(x){ return exp(sin(x)); }},
          {t:'inner', s:'cos x',     v:function(x){ return cos(x); }} ] },
    { n:'ln(x² + 1)', f:function(x){ return log(x*x+1); },
      L:[ {t:'outer', s:'1 / (x² + 1)', v:function(x){ return 1/(x*x+1); }},
          {t:'inner', s:'2x',                v:function(x){ return 2*x; }} ] },
    { n:'sin(e^(x²))', f:function(x){ return sin(exp(x*x)); },
      L:[ {t:'outer',  s:'cos(e^(x²))', v:function(x){ return cos(exp(x*x)); }},
          {t:'middle', s:'e^(x²)',      v:function(x){ return exp(x*x); }},
          {t:'inner',  s:'2x',               v:function(x){ return 2*x; }} ] },
    { n:'(x²)³', f:function(x){ return pow(x*x,3); },
      L:[ {t:'outer', s:'3(x²)²', v:function(x){ return 3*pow(x*x,2); }},
          {t:'inner', s:'2x',               v:function(x){ return 2*x; }} ] }
  ];
  var cur=1;

  function fmt(v){
    var a=Math.abs(v);
    if(a!==0 && (a<1e-3 || a>=1e5)) return v.toExponential(3);
    return v.toFixed(4);
  }
  function slope(f,x){ var h=1e-5; return (f(x+h)-f(x-h))/(2*h); }

  var bar=$('cl-fns');
  F.forEach(function(e,k){
    var b=document.createElement('button');
    b.type='button'; b.className='res-filter'; b.style.fontSize='.72rem';
    b.textContent=e.n;
    b.addEventListener('click',function(){ cur=k; draw(); });
    bar.appendChild(b);
  });

  function draw(){
    var e=F[cur], x=(+$('cl-x').value)/100;
    Array.prototype.forEach.call(bar.children,function(b,k){
      b.classList[k===cur?'add':'remove']('is-active');
    });
    $('cl-fx').textContent='f(x) = '+e.n;
    $('cl-xv').textContent=x.toFixed(2);

    var prod=1, sym=[], html='';
    e.L.forEach(function(L){
      var v=L.v(x); prod*=v; sym.push(L.s);
      html+='<div class="cl-row"><span class="cl-tag">'+L.t+'</span>'+
            '<span class="cl-sym">'+L.s+'</span>'+
            '<span class="cl-num">'+fmt(v)+'</span></div>';
    });
    html+='<div class="cl-prod"><span class="cl-tag">product</span>'+
          '<span class="cl-sym">'+sym.join(' · ')+'</span>'+
          '<span class="cl-num">'+fmt(prod)+'</span></div>';
    $('cl-stack').innerHTML=html;

    var num=slope(e.f,x);
    $('cl-check').textContent='Slope measured from f directly: '+fmt(num)+
      '   —   difference: '+Math.abs(num-prod).toExponential(1);
  }
  $('cl-x').addEventListener('input',draw);
  draw();
})();
</script>

Each layer contributes one factor to the derivative. For a two-layer composition $$h(g(x))$$, the factors are $$h'(g(x))$$ and $$g'(x)$$. For a three-layer composition, the chain rule is simply applied again to the inner composition, and there is no separate three-layer rule.

The visualization also compares the chain-rule derivative with a numerically measured slope from the original function. The two values agree across the examples because the chain rule is describing the actual local rate of change, not merely a symbolic procedure.

## Order matters

The functions $$\sin(x^2)$$ and $$(\sin x)^2$$ contain the same two operations in opposite order, and their derivatives are different. For the first, $$\tfrac{d}{dx}\sin(x^2) = \cos(x^2)\cdot2x$$, and for the second, $$\tfrac{d}{dx}(\sin x)^2 = 2\sin x\cos x$$. The first function squares the input and then takes sine, while the second takes sine first and then squares the result.

A reliable way to identify the outermost operation is to ask what you would do last if you were evaluating the function at a number. For $$\sin(x^2)$$, you square first and take sine last, so sine is the outer function. For $$(\sin x)^2$$, you take sine first and square last, so squaring is the outer function.

## The missing inner factor

The most common chain-rule error is to differentiate the outer layer and stop. For $$\sin(x^2)$$, that produces $$\cos(x^2)$$, which is missing the derivative of the inner function, and the correct derivative is $$2x\cos(x^2)$$. The size of the error changes with $$x$$ because the missing factor is $$2x$$.

The pattern of the error is more important than its size. If the derivative of the inside never appears, one layer has been dropped.

## A rule can be valid without being useful

The chain rule applies to $$(x^2)^3$$, and using it gives $$3(x^2)^2\cdot2x = 6x^5$$. But the original expression is simply $$x^6$$, and the power rule gives $$6x^5$$ immediately. So before applying the chain rule, [simplify the expression](/2026/07/30/derivative-rules-and-choosing.html) if the composition can be collapsed cleanly.

<div class="article-note" markdown="1">
The best rule is not always the most sophisticated rule available. It is the one that makes the structure easiest to see and the work easiest to check.
</div>
