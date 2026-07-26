---
layout: post
title: "The harmonic series diverges, and other honest surprises of infinity"
date: 2026-07-23
description: "A series whose terms vanish can still blow up, and a convergent series can change its sum if you shuffle it. The strangest true facts in BC, with proofs you can actually follow."
course: "AP Calculus BC"
read_time: "9 min read"
math: true
---

Unit 10 is where calculus stops feeling like a faster version of algebra and starts producing results that sound false. This piece collects three of the best examples, each one a true statement that reads like a mistake, together with real proofs rather than incantations. If infinite series ever feel like a list of arbitrary rules, this is the antidote. The rules exist because infinity really does behave this strangely.

## Surprise 1: terms that vanish, a sum that does not

The harmonic series adds up the reciprocals:

$$1 + \frac12 + \frac13 + \frac14 + \frac15 + \cdots$$

The terms shrink to zero, so it seems the sum should settle down. It does not, and the proof, due to Nicole Oresme around 1350, fits in three lines. Group the terms:

$$1 + \frac12 + \underbrace{\left(\frac13 + \frac14\right)}_{>\,\frac14 + \frac14\, =\, \frac12} + \underbrace{\left(\frac15 + \frac16 + \frac17 + \frac18\right)}_{>\,4\,\cdot\,\frac18\, =\, \frac12} + \underbrace{\left(\frac19 + \cdots + \frac1{16}\right)}_{>\,8\,\cdot\,\frac1{16}\, =\, \frac12} + \cdots$$

Every group contributes more than $$\tfrac12$$, and there are infinitely many groups, so the partial sums eventually pass any number you name. The series diverges even though its terms go to zero.

What makes this genuinely strange is how slowly the divergence happens. The sum of the first $$n$$ terms grows like $$\ln n$$. To push the total past 10 you need about 12,367 terms. To pass 100, you would need more terms than there are atoms in the observable universe. The series diverges in theory and looks convergent on every calculator ever built. This is exactly why the exam insists on tests rather than numerical evidence, and why "the terms go to zero" earns no credit as a justification. The harmonic series is the standing counterexample: the nth-term test can convict a series of divergence, but it can never acquit one into convergence.

The boundary here is razor thin. Raise the exponent by any amount at all and the sum tames itself: $$\sum \tfrac{1}{n^{1.0001}}$$ converges. The sharp cutoff at $$p = 1$$ in the p-series test is not bureaucratic tidiness. It marks a real cliff edge, and the harmonic series sits exactly on the lip.

## Surprise 2: alternate the signs, and order suddenly matters

Flip every other sign and the harmonic series calms down completely:

$$1 - \frac12 + \frac13 - \frac14 + \frac15 - \cdots = \ln 2 \approx 0.693.$$

Convergence here is easy to see. The partial sums hop right, then left, each hop smaller than the last, closing in like a pendulum losing energy. That picture is the entire content of the alternating series test: terms decreasing in size to zero force the hops to trap a limit. The picture also hands you the famous error bound for free. The true sum is always trapped between consecutive partial sums, so you are never farther from the limit than the size of the next hop. In other words, the first omitted term bounds the error. That is not a formula to memorize so much as the pendulum picture written down.

But this series converges only because of the cancellation. Take absolute values and you are back to the divergent harmonic series. BC calls this situation conditional convergence, and the name is a warning label. Here is what the condition is.

Consider what shuffling does. Take the same numbers, every positive term $$1, \tfrac13, \tfrac15, \ldots$$ and every negative term $$-\tfrac12, -\tfrac14, \ldots$$, each used exactly once, but deal them in a different order: two positives, then one negative, and repeat.

$$1 + \frac13 - \frac12 + \frac15 + \frac17 - \frac14 + \cdots = \frac{3}{2}\ln 2.$$

Same terms, different order, different sum, half again as large. Addition of infinitely many things is not commutative.

The reason becomes visible once you look at the two halves separately. The positive terms alone sum to $$+\infty$$, and the negative terms alone sum to $$-\infty$$. The ordinary order drains the two infinite reservoirs in careful balance. A shuffle that draws faster from the positive reservoir tilts the balance forever. Riemann proved the ultimate version of this in 1854: a conditionally convergent series can be rearranged to sum to any number you choose, or to diverge. The recipe is greedy. Pick a target; draw positive terms until you cross it, then negative terms until you cross back, and repeat. Each reservoir is infinite, so you never run out, and since the terms shrink to zero, the overshoots shrink too.

Absolutely convergent series, the ones that survive with all signs stripped, such as $$\sum \tfrac{(-1)^n}{n^2}$$, have no such pathology. Shuffle them however you like and the sum holds. This is why BC bothers to distinguish absolute from conditional convergence. It is the difference between a sum that depends only on the set of terms and a sum that depends on their order.

## Surprise 3: the convergent twin has a beautiful secret

The near-twin of the harmonic series, built from squares,

$$1 + \frac14 + \frac19 + \frac1{16} + \cdots$$

does converge, since $$p = 2 > 1$$. Its exact value stumped the Bernoullis for decades. The question became known as the Basel problem, and Euler answered it in 1734 with one of the most celebrated results in mathematics:

$$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}.$$

A sum built from nothing but whole numbers, and $$\pi$$ appears, the circle constant arriving uninvited in a problem with no circle in sight. Euler's original argument treated $$\tfrac{\sin x}{x}$$ as an infinite polynomial and factored it by its roots, exactly the way you would factor a quadratic. It was a gloriously reckless move that took another century to justify rigorously, and it previews the Taylor-series worldview in which functions really are their series. Change the exponent to 3, though, and the sum $$\sum \tfrac{1}{n^3}$$ has no known closed form; it was not even proved irrational until 1978. The frontier of mathematics runs directly through what looks like a BC homework problem.

## What this buys you on the exam

None of the above appears on the test directly, but all of it stands behind the test, and the strangeness explains why the rules are what they are.

- The nth-term test only proves divergence because of Surprise 1: vanishing terms guarantee nothing.
- Justifications must name a test and verify its hypotheses because numerical evidence is provably worthless here. Recall the 12,367 terms needed just to reach 10.
- Absolute versus conditional convergence is worth classifying because of Surprise 2. The two kinds of convergence differ in kind, not merely in degree.
- The alternating series error bound is the pendulum picture, and remembering the picture is more reliable than remembering the formula.

<div class="article-note" markdown="1">
Something to try at a whiteboard: use the greedy rearrangement recipe to steer the alternating harmonic series toward 1.2. Take positive terms until you pass it, then negative terms until you drop below, and repeat. Watching the overshoots shrink term by term is the fastest way I know to believe Riemann's theorem in your bones.
</div>
