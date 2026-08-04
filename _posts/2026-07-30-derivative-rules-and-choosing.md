---
layout: post
title: "Choosing a differentiation rule"
date: 2026-07-30
description: "There are only a handful of differentiation rules and they are quickly memorized. The work is reading an expression and knowing which one it wants, including the times when the answer is to rewrite it first."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "9 min read"
math: true
kind: mechanics
sequence: 9
interactive: true
blurb: "The rules are the easy part; reading the expression is the skill"
image: "/assets/og/derivative-rules-and-choosing.png"
---

The differentiation rules in this unit fit on an index card, and memorizing them is a week's work at most. Almost none of the difficulty in Unit 2 lives there.

The difficulty is in the step before: looking at an expression and knowing which rule it wants. That step has no formula and is rarely written down, but it is not an afterthought in the course either. The enduring understanding these topics sit under says it outright — recognizing opportunities to apply derivative rules can simplify differentiation — and where topics 2.5 through 2.9 ask you to *apply* an appropriate rule, topic 2.10 asks you to *identify* one. Those are different skills, and only one of them is memorization.

## The rules, briefly

The framework groups them by what they act on. For a power, $$\tfrac{d}{dx}x^r = rx^{r-1}$$ for real $$r$$, at every $$x$$ where both sides are defined. Sums, differences, and constant multiples pass straight through, so a polynomial is differentiated term by term. Four specific functions have rules of their own: sine, cosine, the exponential, and the natural logarithm.

$$\frac{d}{dx}\sin x = \cos x, \qquad \frac{d}{dx}\cos x = -\sin x, \qquad \frac{d}{dx}e^x = e^x, \qquad \frac{d}{dx}\ln x = \frac1x.$$

Then two rules for expressions built from others. If $$f$$ and $$g$$ are both differentiable at $$x$$, then

$$(fg)'(x) = f'(x)g(x) + f(x)g'(x),$$

and if in addition $$g(x) \neq 0$$, then

$$\left(\frac{f}{g}\right)'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}.$$

That is the whole card. Both rules require the pieces to be differentiable, and that hypothesis is doing work: when a factor fails it, the rule is silent rather than negative. The function $$\vert x\vert \cdot 1$$ has no derivative at 0, and $$\vert x\vert \cdot \vert x\vert = x^2$$ has one, so a [point where differentiability fails](/2026/07/30/where-differentiability-fails.html) inside a product has to be examined directly.

## Two rules that get reached for too early

The product and quotient rules are correct whenever they apply, and they apply more often than they are needed. An expression can be a product and still not want the product rule, because multiplying it out first is less work and less error-prone.

Below is a classification drill. No differentiating — just name the first move.

<div class="viz" markdown="0">
  <div class="rc-expr" id="rc-e"></div>
  <div class="viz-controls">
    <button type="button" class="res-filter rc-a" data-a="basic" style="font-size:.72rem">Power / sum / constant multiple</button>
    <button type="button" class="res-filter rc-a" data-a="product" style="font-size:.72rem">Product rule</button>
    <button type="button" class="res-filter rc-a" data-a="quotient" style="font-size:.72rem">Quotient rule</button>
    <button type="button" class="res-filter rc-a" data-a="rewrite" style="font-size:.72rem">Rewrite it first</button>
  </div>
  <div class="rc-fb" id="rc-fb"></div>
  <div class="viz-controls">
    <button type="button" class="res-filter" id="rc-next" style="font-size:.72rem">Next expression</button>
    <span class="viz-value" id="rc-score"></span>
  </div>
  <p class="viz-caption">Ten expressions, cycling. Five of them want a rewrite, and those are the ones worth arguing about: two products that collapse to a single power, one quotient that is really a division, and the two trigonometric functions the framework says to rearrange rather than memorize. The product and quotient rules would give the right answer on all five; they are just the long way round, and the long way is where sign errors live.</p>
  <style>
    .rc-expr{font-size:1.9rem;font-weight:700;letter-spacing:-.02em;color:var(--ink);
      text-align:center;padding:18px 0 14px;min-height:2.6em}
    .rc-fb{font-size:.95rem;line-height:1.6;color:var(--ink);min-height:3.4em;
      padding:10px 0 4px;border-top:1px solid var(--line);margin-top:.4rem}
    .rc-fb .rc-ok{font-weight:700}
    .rc-fb .rc-no{font-weight:700;color:var(--muted)}
  </style>
</div>

<script>
(function(){
  'use strict';
  var $=function(i){ return document.getElementById(i); };
  // answer: the first move, not the derivative
  var Q=[
    { e:'x⁵ − 3x² + 7', a:'basic',
      why:'A polynomial. Power rule on each term, with sum, difference, and constant multiple carrying through.' },
    { e:'x² · sin x', a:'product',
      why:'A genuine product of two functions with no simpler form. Product rule.' },
    { e:'(x² + 1) / (x − 3)', a:'quotient',
      why:'A genuine quotient. Nothing cancels, so the quotient rule is the shortest route.' },
    { e:'tan x', a:'rewrite',
      why:'Rewrite as sin x / cos x, then apply the quotient rule. The framework says the other four trigonometric derivatives come from rearranging with identities, not from four more memorized rules.' },
    { e:'(x³ + 2x) / x', a:'rewrite',
      why:'Divide first: this is x² + 2, whose derivative is 2x. The quotient rule gets there too, three steps later.' },
    { e:'5e^x', a:'basic',
      why:'A constant multiple of a function with its own rule. The 5 rides along.' },
    { e:'x² · x⁵', a:'rewrite',
      why:'Add the exponents: this is x⁷, derivative 7x⁶. It is a product, and the product rule is the wrong tool for it.' },
    { e:'sec x', a:'rewrite',
      why:'Rewrite as 1 / cos x, then quotient rule. Same instruction as tan x, same reason.' },
    { e:'(sin x) / x²', a:'quotient',
      why:'A genuine quotient: the numerator and denominator share nothing to cancel.' },
    { e:'√x · x', a:'rewrite',
      why:'x^(1/2) · x is x^(3/2), derivative (3/2)x^(1/2). Another product that is really a power.' }
  ];
  var LABEL={ basic:'Power / sum / constant multiple', product:'Product rule',
              quotient:'Quotient rule', rewrite:'Rewrite it first' };
  var i=0, asked=0, right=0, answered=false;

  function show(){
    $('rc-e').textContent=Q[i].e;
    $('rc-fb').innerHTML='&nbsp;';
    answered=false;
    score();
  }
  function score(){
    $('rc-score').textContent = asked ? (right+' of '+asked+' correct') : 'Name the first move.';
  }
  function answer(a){
    if(answered) return;
    answered=true; asked++;
    var ok = a===Q[i].a;
    if(ok) right++;
    $('rc-fb').innerHTML = (ok ? '<span class="rc-ok">Yes.</span> ' :
      '<span class="rc-no">No &mdash; ' + LABEL[Q[i].a] + '.</span> ') + Q[i].why;
    score();
  }
  Array.prototype.forEach.call(document.querySelectorAll('.rc-a'),function(b){
    b.addEventListener('click',function(){ answer(b.getAttribute('data-a')); });
  });
  $('rc-next').addEventListener('click',function(){ i=(i+1)%Q.length; show(); });
  show();
})();
</script>

Five of the ten want a rewrite, and they are the five worth slowing down for. Two are products that collapse to a single power, one is a quotient that is really a division, and two are the trigonometric functions the framework explicitly says to rearrange.

Take $$\tfrac{x^3 + 2x}{x}$$. The quotient rule gives

$$\frac{(3x^2+2)(x) - (x^3+2x)(1)}{x^2} = \frac{2x^3}{x^2} = 2x,$$

which is right, and which took three steps to reach a result that dividing through gives in one: the expression is $$x^2 + 2$$, so the derivative is $$2x$$. Nothing was learned by the longer route, and it carried a subtraction, two derivatives, and a squared denominator that the direct route never needed.

## The other four trigonometric functions are quotients

Among the trigonometric functions, the course states derivatives for sine and cosine only. Tangent, cotangent, secant, and cosecant are not a second list to memorize — the framework says that rearranging them with identities allows differentiation using the rules you already have.

$$\tan x = \frac{\sin x}{\cos x} \;\Longrightarrow\; (\tan x)' = \frac{\cos x \cos x - \sin x(-\sin x)}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} = \sec^2 x.$$

Four steps, using the quotient rule and one Pythagorean identity, and the result is the formula that usually gets memorized instead. Secant is the same move on $$1/\cos x$$, and gives $$\sec x \tan x$$. Deriving one of these a few times costs less than misremembering it once in May.

## A limit that is secretly a derivative

The recognition skill runs backwards too, and the framework lists it as its own objective: recognizing an expression as [the definition of a derivative](/2026/07/30/derivative-as-a-limit.html), for a function whose derivative you know, is a way of evaluating a limit.

$$\lim_{h \to 0} \frac{(2+h)^5 - 2^5}{h}$$

is a $$0/0$$ form, and the usual [algebra for resolving one](/2026/07/30/indeterminate-forms.html) is not worth attempting here — expanding the fifth power to cancel the $$h$$ is five terms of work for a number you already know. It is exactly $$f'(2)$$ for $$f(x) = x^5$$, so it equals $$5(2)^4 = 80$$. The whole problem is noticing the shape.

Two things give it away: a limit as $$h \to 0$$, and a numerator that is *something at a shifted input, minus the same thing at the input*. Once those register, the question is only which function and which point.

<div class="article-note" markdown="1">
A drill in the same spirit as the one above: take a page of derivative exercises and, without differentiating any of them, write next to each one only the first move. Then compare with a classmate. Disagreements will cluster on the expressions that could be done two ways, which are exactly the ones worth discussing, and the discussion is more useful than the derivatives would have been.
</div>
