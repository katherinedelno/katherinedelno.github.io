---
layout: post
title: "The chain rule, layer by layer"
date: 2026-07-30
description: "The chain rule is a single line, and applying it is mechanical. The difficulty is that most functions do not arrive labeled as compositions, so the first task is seeing the layers at all."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: mechanics
sequence: 10
interactive: true
blurb: "Every layer contributes one factor, and the missing factor is always the inner one"
featured: true
image: "/assets/og/chain-rule-reading-the-layers.png"
---

The chain rule is one line long, and once an expression has been broken into layers, applying it is bookkeeping. Almost every mistake made with it happens before that point.

The course names this directly. Topic 3.1's suggested skill is to identify an appropriate rule based on the classification of a given expression, and the framework's own parenthetical example is the chain rule for a composite function. The rule is not the skill. Classifying the expression is.

## What the rule says

Suppose $$g$$ is differentiable at $$x$$ and $$h$$ is differentiable at $$g(x)$$. Then the composition $$h \circ g$$ is differentiable at $$x$$, and

$$(h \circ g)'(x) = h'\big(g(x)\big) \cdot g'(x).$$

Both hypotheses matter, and they are evaluated at different points: $$g$$ at $$x$$, and $$h$$ at the value $$g$$ produced. That mismatch is the whole content of the rule, and it is what the notation is trying to warn you about.

In Leibniz notation, writing $$u = g(x)$$,

$$\frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dx},$$

which is easier to remember and easier to misread, because it suggests two fractions cancelling. They are not fractions. What is true is the statement above.

Applied once, on $$(3x+1)^5$$: the outer function is $$h(u) = u^5$$ and the inner is $$g(x) = 3x+1$$, so $$h'(u) = 5u^4$$ and $$g'(x) = 3$$. Substituting $$u = g(x)$$ into $$h'$$ and multiplying,

$$\frac{d}{dx}(3x+1)^5 = 5(3x+1)^4 \cdot 3 = 15(3x+1)^4.$$

Notice what would go wrong with $$5u^4$$ left as it stands: the answer would be in terms of a variable the question never mentioned. Substituting $$g(x)$$ back in is not cosmetic. It is the half of the rule that says where $$h'$$ is being evaluated.

## Reading the layers

The tool below lays a composite out in layers, outermost first. Each layer contributes exactly one factor, and the derivative is the product of those factors — a product of ordinary numbers, once $$x$$ is fixed.

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

Two things are worth watching as the slider moves. The factors change independently — the inner one can be small while the outer one is large, and the product is neither. And the measured slope tracks the product everywhere, including at the values of $$x$$ where the function is steep enough that a graph would be no help.

The three-layer case is the same rule applied twice. There is no separate rule for three layers; the middle factor is what appears when the inner function of the outer function is itself a composition.

## Two functions that look alike

$$\sin(x^2)$$ and $$(\sin x)^2$$ are built from the same two ingredients in opposite order, and their derivatives have nothing in common:

$$\frac{d}{dx}\sin(x^2) = 2x\cos(x^2), \qquad \frac{d}{dx}(\sin x)^2 = 2\sin x \cos x = \sin(2x).$$

At $$x = 0.8$$ the first is 1.2834 and the second is 0.9996. Switch between them in the tool and the stack rearranges: what was the outer factor becomes the inner one. Neither function is harder than the other. Reading which is which is the entire task, and it is the same reading problem as [composing functions in the first place](/2026/07/30/functions-inside-functions.html).

## The factor that goes missing

The characteristic chain rule error is writing $$\cos(x^2)$$ for the derivative of $$\sin(x^2)$$ — differentiating the outer layer and stopping. In the stack that is visible as dropping a row. At $$x = 0.8$$ the outer factor is 0.8021 and the true derivative is 1.2834, so the omission costs a factor of $$2x = 1.6$$, and at $$x = 0.05$$ it would cost a factor of $$0.1$$ in the other direction. The error does not have a characteristic size; it has a characteristic shape.

The last function in the tool is a reminder from [the previous article](/2026/07/30/derivative-rules-and-choosing.html). The chain rule handles $$(x^2)^3$$ correctly and returns $$3(x^2)^2 \cdot 2x = 6x^5$$, but the expression is $$x^6$$, and the power rule gives $$6x^5$$ in one step. A rule being applicable is not the same as it being the right one.

<div class="article-note" markdown="1">
Before differentiating a composite, say out loud what the outermost operation is — the last thing you would do if you were evaluating the function at a number. For $$\sin(x^2)$$ you would square first and take the sine last, so the sine is outermost. That test costs a few seconds and settles the layer order before any writing starts, which is where the order needs to be settled.
</div>
