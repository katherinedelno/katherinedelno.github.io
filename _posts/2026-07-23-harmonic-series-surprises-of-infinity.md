---
layout: post
title: "The harmonic series diverges, and other honest surprises of infinity"
date: 2026-07-23
description: "A series whose terms vanish can still blow up; a convergent series can change its sum if you shuffle it. The strangest true facts in BC, with proofs you can actually follow."
course: "AP Calculus BC"
read_time: "9 min read"
math: true
---

Unit 10 is where calculus stops feeling like a faster version of algebra and starts producing results that sound false. This piece collects the three best examples — each one a true statement that reads like a mistake — with real proofs, not incantations. If infinite series ever feel like arbitrary rules, this is the antidote: the rules exist *because* infinity behaves this strangely.

## Surprise 1: terms that vanish, a sum that doesn't

The harmonic series adds up the reciprocals:

$$1 + \frac12 + \frac13 + \frac14 + \frac15 + \cdots$$

The terms shrink to zero. Surely the sum settles down? It does not — and the proof, due to Nicole Oresme around 1350, fits in three lines. Group the terms:

$$1 + \frac12 + \underbrace{\left(\frac13 + \frac14\right)}_{>\,\frac14 + \frac14\, =\, \frac12} + \underbrace{\left(\frac15 + \frac16 + \frac17 + \frac18\right)}_{>\,4\,\cdot\,\frac18\, =\, \frac12} + \underbrace{\left(\frac19 + \cdots + \frac1{16}\right)}_{>\,8\,\cdot\,\frac1{16}\, =\, \frac12} + \cdots$$

Every group beats $$\tfrac12$$, and there are infinitely many groups. The partial sums pass any number you name. Divergence — from terms that go to zero.

What makes this genuinely strange is *how slowly* it happens. The sum of the first $$n$$ terms grows like $$\ln n$$: to push the total past 10 you need about 12,367 terms; to pass 100, you need more terms than there are atoms in the observable universe. The series diverges in theory and looks convergent on every calculator ever built. This is exactly why the exam insists on *tests* rather than numerical vibes, and why "the terms go to zero" earns nothing as a justification — the harmonic series is the standing counterexample. The nth-term test is a one-way instrument: it can convict a series of divergence, never acquit one into convergence.

And the boundary is razor thin. Raise the exponent by any amount at all and the sum tames: $$\sum \tfrac{1}{n^{1.0001}}$$ converges. The $$p$$-series test's sharp cutoff at $$p = 1$$ isn't bureaucracy — it marks a real cliff edge, and the harmonic series sits exactly on the lip.

## Surprise 2: alternate the signs and order suddenly matters

Flip every other sign and the harmonic series calms down completely:

$$1 - \frac12 + \frac13 - \frac14 + \frac15 - \cdots = \ln 2 \approx 0.693.$$

Convergence here is easy to *see*: the partial sums hop right, then left, each hop smaller than the last, closing in like a pendulum losing energy. That picture is the entire content of the alternating series test — terms decreasing in size to zero force the hops to trap a limit — and it also hands you the famous error bound for free: the truth is always trapped between consecutive partial sums, so you're never further from the limit than the size of the next hop. The first omitted term bounds the error. That's not a formula to memorize; it's the pendulum picture written down.

But this series converges *only because* of the cancellation — take absolute values and you're back to the divergent harmonic series. BC calls this **conditional convergence**, and the name is a warning label. Here is what the condition is.

**Watch what shuffling does.** Take the same numbers — every positive term $$1, \tfrac13, \tfrac15, \ldots$$ and every negative term $$-\tfrac12, -\tfrac14, \ldots$$, each used exactly once — but deal them in a different order: two positives, then one negative, repeat:

$$1 + \frac13 - \frac12 + \frac15 + \frac17 - \frac14 + \cdots = \frac{3}{2}\ln 2.$$

Same terms. Different order. **Different sum** — half again as large. Addition of infinitely many things is not commutative.

The reason is almost visible once you see the two halves separately: the positive terms alone sum to $$+\infty$$, the negatives alone to $$-\infty$$. The ordinary order drains the two infinite reservoirs in careful balance. A shuffle that draws faster from the positive reservoir tilts the balance forever. Riemann proved the ultimate version in 1854: a conditionally convergent series can be rearranged to sum to *any number you choose* — $$\pi$$, $$-1{,}000{,}000$$, anything — or to diverge. Pick a target; greedily draw positives until you cross it, negatives until you cross back; repeat. Since each reservoir is infinite you never run dry, and since the terms shrink to zero, the overshoots shrink too.

Absolutely convergent series — those that survive with all signs stripped, like $$\sum \tfrac{(-1)^n}{n^2}$$ — have no such pathology; shuffle them all you like, the sum holds. This is why BC bothers distinguishing absolute from conditional convergence: it is the difference between a sum that is a fact about the *set* of terms and a sum that is a fact about the *sequence* of them.

## Surprise 3: the one that converges has a beautiful secret

The near-twin of the harmonic series, with squares,

$$1 + \frac14 + \frac19 + \frac1{16} + \cdots$$

does converge ($$p = 2 > 1$$ — or compare with the telescoping $$\sum \tfrac{1}{n(n-1)}$$ if you want it barehanded). Its value stumped the Bernoullis for decades — the *Basel problem* — until Euler, in 1734, produced one of the most celebrated answers in mathematics:

$$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}.$$

A sum built from nothing but whole numbers, and out falls $$\pi$$ — the circle constant, arriving uninvited in a problem with no circle anywhere in sight. Euler's original argument treated $$\tfrac{\sin x}{x}$$ as an infinite polynomial and factored it by its roots, exactly the way you'd factor a quadratic — a gloriously reckless move that took another century to make rigorous, and a preview of how the Taylor-series worldview (functions *are* their series) pays off. Change the exponent to 3 and the sum, $$\sum \tfrac{1}{n^3}$$, has no known closed form; it wasn't even proved irrational until 1978. The frontier of mathematics runs directly through a BC homework problem.

## What this buys you on the exam

None of the above is on the test directly — but all of it is *behind* the test, and the strangeness is the reason the rules are what they are:

- The nth-term test only ever proves divergence **because of Surprise 1** — vanishing terms guarantee nothing.
- Justifications must name a test and verify its hypotheses **because** numerical evidence is provably worthless here (12,367 terms to reach 10).
- Absolute versus conditional convergence is worth classifying **because of Surprise 2** — the two kinds of convergence are different in kind, not degree.
- The alternating series error bound is the pendulum picture, and remembering the picture beats remembering the formula.

<div class="article-note" markdown="1">
Something to try at a whiteboard: use the greedy rearrangement idea to start steering the alternating harmonic series toward 1.2 — positives until you pass it, negatives until you drop below, repeat. Watching the overshoots shrink term by term is the fastest way I know to believe Riemann's theorem in your bones.
</div>
