---
layout: post
title: "Indeterminate forms and the algebra that resolves them"
date: 2026-07-30
description: "0/0 is not a value. It is a report that substitution failed, and it carries no information about the answer. Three ways to rewrite the expression, two standard limits, and the squeeze theorem for what is left."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: mechanics
sequence: 3
interactive: false
blurb: "0/0 is a verdict on your method, not an answer"
image: "/assets/og/indeterminate-forms.png"
---

Substituting into $$\tfrac{x^2 - 9}{x - 3}$$ at $$x = 3$$ gives $$\tfrac{0}{0}$$, and the limit is 6. Substituting into $$\tfrac{x - 3}{x^2 - 9}$$ at $$x = 3$$ gives $$\tfrac{0}{0}$$, and the limit is $$\tfrac16$$. Substituting into $$\tfrac{x-3}{(x-3)^2}$$ gives $$\tfrac{0}{0}$$, and the limit does not exist.

Three expressions, one symbol, three different answers. That is what "indeterminate" means: the form $$\tfrac00$$ is not a number and it is not a verdict on the limit. It is a report that substitution failed, and it carries no information about what the limit actually is.

The work, therefore, is to stop substituting and start rewriting. The framework says so directly: it may be necessary to rearrange expressions into equivalent forms before evaluating limits.

## Substitution first, and when it is legal

Try substitution before anything else, because when it works it is finished. It works precisely when the function is [continuous at the point](/2026/07/30/continuity-three-conditions.html), and the standard families — polynomial, rational, power, exponential, logarithmic, trigonometric — are continuous everywhere in their domains. For those, substitution *is* the evaluation.

Limits also distribute over sums, differences, products, quotients, and composites, so a complicated expression built from continuous pieces can be taken apart and substituted piece by piece. The quotient rule for limits carries the obvious caveat, and it is the caveat that produces this article: it applies when the limit of the denominator is not zero.

So the algebra below is for one situation only. Substitution returned $$\tfrac00$$, which means the numerator and denominator share a root at the point, and the shared factor is what has to come out.

## Factor and cancel

The first move whenever both parts are polynomials. Factor, cancel the common factor, then substitute into what is left.

$$\lim_{x \to 3} \frac{x^2-9}{x-3} = \lim_{x \to 3} \frac{(x-3)(x+3)}{x-3} = \lim_{x \to 3} (x+3) = 6.$$

The cancellation is legal because the limit never evaluates the function at $$x = 3$$. On every $$x$$ the limit does look at, $$x - 3 \neq 0$$ and the division is ordinary arithmetic. This is the same fact that makes $$\lim$$ indifferent to the hole it leaves behind, and it is worth saying aloud once: you are not simplifying the function, you are replacing it with a different function that agrees with it everywhere the limit cares about.

Higher degrees need the harder factorizations. A difference of cubes:

$$\lim_{x \to 2} \frac{x^3-8}{x^2-4} = \lim_{x \to 2} \frac{(x-2)(x^2+2x+4)}{(x-2)(x+2)} = \frac{4+4+4}{4} = 3.$$

## Multiply by the conjugate

When a radical is involved, factoring has nothing to grip. Multiplying by the conjugate does, because it converts a difference of square roots into a difference of squares and the radical disappears from the part that matters.

$$\lim_{x \to 0} \frac{\sqrt{x+4}-2}{x} = \lim_{x \to 0} \frac{\sqrt{x+4}-2}{x}\cdot\frac{\sqrt{x+4}+2}{\sqrt{x+4}+2} = \lim_{x \to 0} \frac{x}{x\left(\sqrt{x+4}+2\right)} = \frac{1}{4}.$$

The middle step is where the technique earns itself: the numerator becomes $$(x+4) - 4 = x$$, which cancels the $$x$$ downstairs. Multiply the denominator out and you have gained nothing, so leave it factored.

## Clear the compound fraction

A fraction inside a fraction is not indeterminate in a new way, only in an inconvenient form. Combine the inner fractions over a common denominator, then divide.

$$\lim_{x \to 0} \frac{\tfrac{1}{x+2} - \tfrac{1}{2}}{x} = \lim_{x \to 0} \frac{\tfrac{2 - (x+2)}{2(x+2)}}{x} = \lim_{x \to 0} \frac{-x}{2x(x+2)} = -\frac{1}{4}.$$

This form appears constantly once the derivative arrives, because the difference quotient of $$1/x$$ looks exactly like this. Getting fluent now pays later.

## The two limits you are expected to know

Some limits yield to none of the above, and two of them are standard enough that the framework names both:

$$\lim_{x \to 0} \frac{\sin x}{x} = 1, \qquad \lim_{x \to 0} \frac{1 - \cos x}{x} = 0.$$

A third technique the framework names alongside factoring and conjugates is using alternate forms of trigonometric functions, and it is usually a matter of rewriting everything as sine and cosine. For instance

$$\lim_{x \to 0} \frac{\tan x}{x} = \lim_{x \to 0} \frac{\sin x}{x}\cdot\frac{1}{\cos x} = 1 \cdot 1 = 1,$$

where the whole move was refusing to leave $$\tan$$ in place.

Both standard limits are $$\tfrac00$$ by substitution and neither factors. They are established by the squeeze theorem, which is the other tool listed under the same objective as algebraic rearrangement: if $$g(x) \le f(x) \le h(x)$$ near the point and $$g$$ and $$h$$ share a limit there, $$f$$ is trapped into having it too.

The squeeze theorem also handles the oscillating cases that defeat everything else. The function $$x^2\sin\!\left(\tfrac1x\right)$$ has no limit-friendly rewriting, but $$\left\vert\sin\frac1x\right\vert \le 1$$ forces

$$-x^2 \le x^2\sin\!\left(\frac1x\right) \le x^2,$$

and both bounds go to 0, so the middle does as well. Note what had to be checked: the inequality has to hold near the point, and the outer limits have to be equal. Naming the theorem without confirming both is not a justification.

## Choosing among them

Selecting the procedure is its own listed skill, which is a fair signal that it is the part worth practicing. The classification is quick:

- Both parts polynomial, sharing a root: *factor and cancel*.
- A square root in the numerator or denominator: *conjugate*.
- A fraction stacked inside a fraction: *common denominator, then divide*.
- Sine or cosine over $$x$$ near zero: *the two standard limits*.
- Any other trigonometric function: *rewrite it as sine and cosine first*.
- Bounded oscillation multiplied by something vanishing: *squeeze*.

Work the classification before the algebra. A student who starts multiplying by conjugates on a polynomial quotient has not made an arithmetic error; they have skipped the step where the expression is read.

<div class="article-note" markdown="1">
A drill worth doing without solving anything: take twenty limits and, for each one, write only the substitution result and the technique it calls for. No answers. The skill being tested is classification, and separating it from the algebra is the fastest way to find out whether you have it. The tell that you do not is reaching for the same technique twice in a row without checking.
</div>
