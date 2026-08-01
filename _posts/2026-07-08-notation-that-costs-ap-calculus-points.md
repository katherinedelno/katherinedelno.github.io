---
layout: post
title: "Notation in AP Calculus"
date: 2026-07-08
description: "Most lost free-response points are lost in the writing rather than the mathematics. This article sets out the conventions that protect earned credit, with examples of each."
course: "AP Calculus AB & BC"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "10 min read"
math: true
kind: mechanics
sequence: 2
interactive: false
blurb: "The writing conventions that protect earned credit"
---

Most of the free-response points I see students lose in AP Calculus are not lost on ideas. They are lost on notation and justification. The student knows how to solve the problem, does the real work correctly, and then leaves credit behind in how it is written. Graders reward reasoning that is communicated clearly, and calculus has a handful of conventions that are easy to drop under time pressure.

What follows is the list I wish every student had taped inside their binder: each habit, why it matters to a grader, and an example of the difference between work that earns the point and work that does not.

## Keep the differential

An integral needs its $$dx$$. Write $$\textstyle \int f(x)\,dx$$, not just the integrand $$f(x)$$ on its own. The differential tells the reader which variable you are integrating with respect to, and it is part of the notation graders are looking for.

This matters most during substitution, where the differential is doing real mathematical work. If $$u = x^2 + 1$$, then $$du = 2x\,dx$$, an actual equation you use to trade variables:

$$\int 2x\sqrt{x^2+1}\,dx = \int \sqrt{u}\,du = \frac{2}{3}u^{3/2} + C = \frac{2}{3}\left(x^2+1\right)^{3/2} + C.$$

Every integral in that chain carries its differential, and the substitution is visible and checkable. A student who writes $$\textstyle \int \sqrt{u}$$ midway has stopped saying what the variable of integration is, and on a definite integral, that ambiguity is exactly where forgotten limit conversions hide.

## Where the constant enters

Every indefinite integral gets a $$+\,C$$. It looks small, but on a problem that asks you to find a particular solution to a differential equation, the constant is the entire point, and you need it there to solve for the initial condition.

Watch where the constant enters. Solving $$\tfrac{dy}{dx} = 2xy$$ with $$y(0) = 3$$:

$$\int \frac{dy}{y} = \int 2x\,dx \quad\Longrightarrow\quad \ln\vert y\vert = x^2 + C.$$

The $$C$$ appears at the moment of integration, one constant, on one side. A student who omits it here and pastes it on later, after exponentiating, often ends up with $$y = e^{x^2} + C$$, which is a *different family of functions*, and the wrong one. Done in order: $$y = Ae^{x^2}$$, then $$A = 3$$, so $$y = 3e^{x^2}$$. The placement of the constant is not a formality. It changes the answer.

## Say what is being evaluated

$$f'(2)$$ means the derivative at $$2$$, not $$f(2)$$. Prime notation and $$\tfrac{dy}{dx}$$ express the same idea in two forms, and mixing them up, or writing $$f(2)$$ when you mean the rate of change, changes the mathematical claim. Be precise about whether you are reporting a value, a slope, or an accumulated amount.

The same discipline applies to evaluation bars. Writing $$\left.\tfrac{dy}{dx}\right\vert_{x=2}$$ says "the derivative, evaluated at 2." Writing $$\tfrac{dy}{dx} = 12$$ when the derivative is $$3x^2$$ and you mean its value at $$x=2$$ makes a false general claim; the bar makes it a true specific one.

## The equals sign means equal

One of the most common notation errors is stringing together things that are not actually equal, such as writing a function and its derivative joined by an equals sign as you differentiate. Each line you write should be a true statement on its own. If you would not defend it as an equation, it should not have an equals sign in it.

For example, under time pressure a student who knows the calculus might write $$x^2 = 2x = 6$$ to mean "the derivative of $$x^2$$ at $$3$$ is $$6$$." Read literally, though, $$x^2 \neq 2x$$, and $$2x \neq 6$$. Written so that every line is true: $$f(x) = x^2$$, so $$f'(x) = 2x$$, and $$f'(3) = 6$$. Same answer, but now each statement holds and the reasoning is visible, which is what earns the point.

The definite-integral version of this error is just as common:

$$\int_0^3 x^2\,dx = \frac{x^3}{3} = 9. \quad\text{(false in the middle)}$$

A definite integral is a *number*, while $$\tfrac{x^3}{3}$$ is a *function*. The honest chain uses the evaluation bar:

$$\int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = 9 - 0 = 9.$$

## Justify in words, not just symbols

When a problem asks you to justify, [a sign chart](/2026/07/21/reading-the-graph-of-f-prime.html) by itself is not a justification; the sentence is. Graders are instructed not to award justification points for a bare chart. The chart is your scratch work, and the sentence is your answer. Write it out: "$$f$$ is increasing on this interval *because* $$f'(x) > 0$$ there."

The reliable pattern is *claim, because, calculus fact*:

- "$$f$$ has a relative minimum at $$x = 2$$ *because* $$f'$$ changes from negative to positive at $$x = 2$$."
- "The graph of $$f$$ is concave down on $$(1, 4)$$ *because* $$f''(x) < 0$$ there."
- "The particle is slowing down at $$t = 3$$ *because* velocity and acceleration have opposite signs."

When a result depends on a theorem, name it and check its hypotheses in the same breath: "$$f$$ is continuous on $$[1,4]$$ and differentiable on $$(1,4)$$, so *by the Mean Value Theorem* there is a $$c$$ in $$(1,4)$$ with $$f'(c) = \tfrac{f(4)-f(1)}{3}$$." The hypothesis check is very often its own point; the conclusion alone collects half the credit.

## Carry the units and the meaning

A definite integral of a rate is an accumulated change, and it has units. If the problem is in context, say what your number *means*: not just "$$42$$," but "the tank gained 42 gallons between $$t = 0$$ and $$t = 6$$."

A complete interpretation touches four things: the *quantity*, its *units*, the *time or interval*, and the *direction of change*. Compare:

> "$$W'(5) = -2$$" *(no credit as an interpretation)*
>
> "At $$t = 5$$ hours, the temperature of the water is *decreasing* at a rate of *2 degrees Fahrenheit per hour*." *(all four elements: full credit)*

Interpretation questions are among the most reliable points on the exam, and among the most reliably skipped.

## Keep the limit attached

The derivative is defined as a limit:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}.$$

Keep that $$\lim_{h \to 0}$$ attached at every step until you actually evaluate it. Writing the expression without the limit and then producing a number treats a process as if it were already finished.

The same rule governs improper integrals in BC. The integral $$\textstyle \int_1^\infty \tfrac{1}{x^2}\,dx$$ is *defined* as $$\textstyle \lim_{b\to\infty}\int_1^b \tfrac{1}{x^2}\,dx$$, and the scoring guidelines award a point specifically for writing the limit. Evaluating straight to $$1$$ without it gets the number and misses the point.

## Calculator answers need setups

On the calculator-active questions, the number is only half the answer. Write the mathematical setup, meaning the integral, the equation, or the derivative, before you report what the calculator returned:

$$\int_0^8 \left(R(t) - P(t)\right)dt \approx 47.312.$$

A bare "$$47.312$$" with no setup can miss the setup point even when the value is perfect, and an answer of $$47.31$$ or $$47.3$$ misses the answer point: final numeric answers must be correct to *three decimal places*. Store intermediate values in the calculator rather than retyping rounded versions. A rounded intermediate is the most common source of a third-decimal error.

<div class="article-note" markdown="1">
None of this is busywork. The notation is how you show that the reasoning is yours and that you know *why* each step is allowed, which is exactly what the free-response section is built to measure. Getting it right is a habit, and habits are built by doing the work yourself, one problem at a time.
</div>
