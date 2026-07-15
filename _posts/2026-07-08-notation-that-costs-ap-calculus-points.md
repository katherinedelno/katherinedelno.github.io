---
layout: post
title: "The notation that quietly costs AP Calculus points"
date: 2026-07-08
description: "Strong calculus students often lose free-response points on notation and justification rather than on ideas. Here are the habits that keep the credit you've earned."
read_time: "5 min read"
math: true
---

Most of the free-response points I see students lose in AP Calculus aren't lost on ideas. They're lost on notation and justification. The student knows how to solve the problem, does the real work correctly, and then leaves credit behind in how it's written. Graders reward reasoning that is communicated clearly, and calculus has a handful of conventions that are easy to drop under time pressure.

## Keep the differential

An integral needs its $$dx$$. Write $$\int f(x)\,dx$$, not just the integrand $$f(x)$$ on its own. The differential tells the reader which variable you're integrating with respect to, and it's part of the notation graders are looking for. The same goes for $$du$$ when you substitute; dropping it midway is a quiet way to lose a point on an otherwise perfect solution.

## Don't forget the constant

Every indefinite integral gets a $$+\,C$$. It looks small, but on a problem that asks you to find a particular solution to a differential equation, the constant is the entire point, and you need it there to solve for the initial condition.

## Say what you're evaluating

$$f'(2)$$ means the derivative at $$2$$, not $$f(2)$$. Prime notation and $$\dfrac{dy}{dx}$$ express the same idea in two forms, and mixing them up, or writing $$f(2)$$ when you mean the rate of change, changes the mathematical claim. Be precise about whether you're reporting a value, a slope, or an accumulated amount.

## The equals sign means equal

One of the most common notation errors is stringing together things that aren't actually equal, such as writing a function and its derivative joined by an equals sign as you differentiate. Each line you write should be a true statement on its own. If you wouldn't defend it as an equation, it shouldn't have an equals sign in it.

For example, under time pressure a student who knows the calculus might write $$x^2 = 2x = 6$$ to mean "the derivative of $$x^2$$ at $$3$$ is $$6$$." Read literally, though, $$x^2 \neq 2x$$, and $$2x \neq 6$$. Written so that every line is true: $$f(x) = x^2$$, so $$f'(x) = 2x$$, and $$f'(3) = 6$$. Same answer, but now each statement holds and the reasoning is visible, which is what earns the point.

## Justify in words, not just symbols

When a problem asks you to justify, a sign chart by itself is not a justification; the sentence is. Write it out: "$$f$$ is increasing on this interval **because** $$f'(x) > 0$$ there." When a result depends on a theorem, name it: "**by the Fundamental Theorem of Calculus**," or "the **Mean Value Theorem** guarantees it," and confirm the hypotheses the theorem requires, such as continuity or differentiability.

## Carry the units and the meaning

A definite integral of a rate is an accumulated change, and it has units. If the problem is in context, say what your number *means*: not just "$$42$$," but "the tank gained 42 gallons between $$t = 0$$ and $$t = 6$$." Interpretation questions are among the most reliable points on the exam, and among the most reliably skipped.

## Don't drop the limit

The derivative is defined as a limit:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}.$$

Keep that $$\lim_{h \to 0}$$ attached at every step until you actually evaluate it. Writing the expression without the limit and then producing a number treats a process as if it were already finished.

<div class="article-note" markdown="1">
None of this is busywork. The notation is how you show that the reasoning is yours and that you know *why* each step is allowed, which is exactly what the free-response section is built to measure. Getting it right is a habit, and habits are built by doing the work yourself, one problem at a time.
</div>
