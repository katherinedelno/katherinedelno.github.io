---
layout: post
title: "Indeterminate forms and the algebra that resolves them"
date: 2026-07-30
description: "When substitution produces 0/0, the next step is to rewrite the expression rather than treat the form as an answer."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "6 min read"
math: true
kind: mechanics
sequence: 3
interactive: false
blurb: "When substitution produces 0/0, the next step is to rewrite the expression rather than treat the form as an answer"
image: "/assets/og/indeterminate-forms.png"
---

Substitution into $$\tfrac{x^2-9}{x-3}$$ at $$x=3$$ gives $$0/0$$, but the limit is 6. Substitution into $$\tfrac{x-3}{x^2-9}$$ also gives $$0/0$$, but the limit is $$1/6$$. And substitution into $$\tfrac{x-3}{(x-3)^2}$$ again gives $$0/0$$, while the two-sided limit does not exist.

The form $$0/0$$ therefore does not determine the value of the limit. It is an indeterminate form, and it tells you that direct substitution did not finish the problem. The next step is usually algebra.

## Start with substitution

Substitution should still be the first move. If the function is [continuous at the point](/2026/07/30/continuity-three-conditions.html), the limit equals the function value there, and polynomials, rational functions, power functions, exponentials, logarithms, and trigonometric functions are continuous throughout their domains. Limit laws also allow sums, products, quotients, and compositions of continuous pieces to be evaluated component by component, and the important exception for quotients is a denominator approaching zero.

When substitution produces $$0/0$$, both numerator and denominator vanish at the point. In many AP Calculus problems, that means there is algebraic structure to expose before trying again.

## Factor and cancel

If both numerator and denominator are polynomials, look for a common factor, as in

$$\lim_{x\to3}\frac{x^2-9}{x-3} = \lim_{x\to3}\frac{(x-3)(x+3)}{x-3} = \lim_{x\to3}(x+3) = 6$$

The cancellation is valid for the limit because the limit considers values near $$x=3$$, not the value at $$x=3$$ itself. For every nearby $$x\neq3$$, $$\tfrac{(x-3)(x+3)}{x-3}=x+3$$, and the simplified expression is a different function at $$x=3$$, but it agrees with the original function everywhere the limit is examining. Higher-degree expressions may require identities such as the difference of cubes, as in $$\lim_{x\to2}\tfrac{x^3-8}{x^2-4} = \lim_{x\to2}\tfrac{(x-2)(x^2+2x+4)}{(x-2)(x+2)} = 3$$.

## Multiply by the conjugate

When a radical produces $$0/0$$, multiplying by the conjugate often creates a factor that can be canceled. Consider $$\lim_{x\to0}\tfrac{\sqrt{x+4}-2}{x}$$ and multiply by $$\tfrac{\sqrt{x+4}+2}{\sqrt{x+4}+2}$$, so that

$$\lim_{x\to0} \frac{\sqrt{x+4}-2}{x} \cdot \frac{\sqrt{x+4}+2}{\sqrt{x+4}+2} = \lim_{x\to0} \frac{x}{x(\sqrt{x+4}+2)} = \frac14$$

The useful step is the difference of squares in the numerator. Do not expand the denominator unless there is a reason to, because leaving it factored keeps the cancellation visible.

## Clear a compound fraction

A fraction inside a fraction may only need ordinary algebra before the limit can be evaluated. Consider

$$\lim_{x\to0} \frac{\frac{1}{x+2}-\frac12}{x}$$

and combine the terms in the numerator, which gives $$\tfrac{1}{x+2}-\tfrac12 = \tfrac{2-(x+2)}{2(x+2)} = \tfrac{-x}{2(x+2)}$$, so the limit becomes $$\lim_{x\to0}\tfrac{-x}{2x(x+2)} = -\tfrac14$$. This structure becomes common when derivatives are introduced because difference quotients often create compound fractions.

## Two standard trigonometric limits

Two limits are especially important:

$$\lim_{x\to0}\frac{\sin x}{x}=1, \qquad \lim_{x\to0}\frac{1-\cos x}{x}=0$$

They also produce $$0/0$$ under substitution, but they are established from geometric arguments and the squeeze theorem rather than ordinary factoring. Other trigonometric limits can often be rewritten to use them, as in $$\lim_{x\to0}\tfrac{\tan x}{x} = \lim_{x\to0} \tfrac{\sin x}{x} \cdot \tfrac{1}{\cos x} = 1$$, where the important step is rewriting tangent in terms of sine and cosine.

## The squeeze theorem

The squeeze theorem handles limits where direct simplification is not the right tool. If $$g(x)\le f(x)\le h(x)$$ near a point, and $$\lim_{x\to a}g(x) = \lim_{x\to a}h(x) = L$$, then $$\lim_{x\to a}f(x)=L$$.

For example, $$x^2\sin\left(\tfrac1x\right)$$ oscillates as $$x\to0$$, but $$\left\vert \sin\left(\tfrac1x\right)\right\vert \le1$$, and therefore $$-x^2 \le x^2\sin\left(\tfrac1x\right) \le x^2$$. Both outer expressions approach 0, so the middle expression must also approach 0.

When using the theorem as a justification, state both pieces. The inequality has to hold near the point, and the two bounding functions have to approach the same limit.

## Choosing the technique

The algebra is usually easier once the expression has been classified. A useful first pass is:

- Polynomial numerator and denominator with a shared root: factor and cancel.
- Radical creating $$0/0$$: multiply by the conjugate.
- Fraction inside a fraction: combine the inner fractions first.
- Sine or cosine over $$x$$ near zero: use the standard trigonometric limits.
- Other trigonometric functions: rewrite in terms of sine and cosine.
- Bounded oscillation multiplied by something approaching zero: consider the squeeze theorem.

<div class="article-note" markdown="1">
It is worth practicing the classification separately from the computation. Take a set of limits and, before solving any of them, write only what substitution gives and which technique you would try next. That isolates the part of the problem that students often skip. The question is not only whether you can carry out the algebra. It is whether you can read the expression well enough to choose the right algebra.
</div>
