---
layout: post
title: "Choosing a differentiation rule"
date: 2026-07-30
description: "Differentiation is often easier once the expression has been classified and simplified before any rule is applied."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "9 min read"
math: true
kind: mechanics
sequence: 9
interactive: true
blurb: "Differentiation is often easier once the expression has been classified and simplified before any rule is applied"
image: "/assets/og/derivative-rules-and-choosing.png"
---

The basic differentiation rules are short.

The harder skill is deciding which rule fits the expression in front of you.

A product does not always need the product rule. A quotient does not always need the quotient rule. Some expressions are much easier after a small algebraic rewrite.

It is worth separating two questions.

First, what rule is valid?

Second, what approach is simplest?

## The core rules

For a power,

$$\frac{d}{dx}x^r=rx^{r-1},$$

where the expression is defined.

Sums, differences, and constant multiples can be differentiated term by term.

The basic trigonometric, exponential, and logarithmic derivatives include

$$\frac{d}{dx}\sin x=\cos x,$$

$$\frac{d}{dx}\cos x=-\sin x,$$

$$\frac{d}{dx}e^x=e^x,$$

and

$$\frac{d}{dx}\ln x=\frac1x.$$

For products,

$$(fg)'(x)=f'(x)g(x)+f(x)g'(x).$$

For quotients, when $$g(x)\neq0$$,

$$\left(\frac{f}{g}\right)'(x) = \frac{f'(x)g(x)-f(x)g'(x)}{[g(x)]^2}.$$

These rules assume the relevant component functions are [differentiable at the point](/2026/07/30/where-differentiability-fails.html).

If that condition fails, the rule cannot simply be applied mechanically.

## Rewrite before using a longer rule

The product and quotient rules are often correct even when they are unnecessary.

The drill below asks only for the first move.

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
      '<span class="rc-no">No. ' + LABEL[Q[i].a] + '.</span> ') + Q[i].why;
    score();
  }
  Array.prototype.forEach.call(document.querySelectorAll('.rc-a'),function(b){
    b.addEventListener('click',function(){ answer(b.getAttribute('data-a')); });
  });
  $('rc-next').addEventListener('click',function(){ i=(i+1)%Q.length; show(); });
  show();
})();
</script>

Consider

$$\frac{x^3+2x}{x}.$$

The quotient rule works, but simplifying first is much easier:

$$\frac{x^3+2x}{x}=x^2+2$$

for $$x\neq0$$.

Then

$$\frac{d}{dx}(x^2+2)=2x.$$

Using the quotient rule produces the same derivative with more algebra and more opportunities for error.

The same idea applies to products that collapse to a single power or rational expressions that simplify before differentiation.

Before choosing a rule, ask whether ordinary algebra makes the structure simpler.

## Deriving the other trigonometric rules

Sine and cosine are enough to derive the other standard trigonometric derivatives.

For example,

$$\tan x=\frac{\sin x}{\cos x}.$$

Using the quotient rule,

$$(\tan x)' = \frac{\cos^2x+\sin^2x}{\cos^2x} = \frac{1}{\cos^2x} = \sec^2x.$$

Likewise,

$$\sec x=\frac1{\cos x}$$

can be differentiated using the quotient rule or a negative power.

This is useful even if you eventually memorize the formulas. Knowing where they come from makes them easier to recover when memory fails.

## Recognizing a derivative inside a limit

The same classification skill can run in reverse.

Consider

$$\lim_{h\to0} \frac{(2+h)^5-2^5}{h}.$$

Direct substitution gives [$$0/0$$](/2026/07/30/indeterminate-forms.html).

You could expand $$(2+h)^5$$, cancel $$h$$, and then evaluate the limit.

But the expression is already [the definition of a derivative](/2026/07/30/derivative-as-a-limit.html).

If

$$f(x)=x^5,$$

then the limit is

$$f'(2).$$

Since

$$f'(x)=5x^4,$$

the answer is

$$f'(2)=5(2)^4=80.$$

Two features reveal the structure:

- the limit is taken as $$h\to0$$
- the numerator has the form $$f(a+h)-f(a)$$

Recognizing the form is the entire problem.

<div class="article-note" markdown="1">
A useful practice exercise is to take a page of derivative problems and write only the first move beside each one.

Do not differentiate yet.

For each expression, decide whether you would simplify, use a basic derivative, use the product rule, use the quotient rule, or use the chain rule.

That isolates the classification skill from the algebra that follows.
</div>
