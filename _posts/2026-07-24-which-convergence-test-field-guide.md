---
layout: post
title: "Which convergence test? A field guide"
date: 2026-07-24
description: "Ten seconds of looking should tell you which test to run. The decision sequence I teach, what each test can and cannot conclude, and the three traps the exam sets with them."
course: "AP Calculus BC"
read_time: "7 min read"
math: true
---

Students usually learn the convergence tests as a heap: seven tools, each with its own hypotheses and conclusion, in no particular order. Then a series appears on the page and the heap offers no advice about where to start. It helps to stop thinking of the tests as a toolbox and start thinking of them as a field guide. Series have visible features, and the features tell you which test to run. Worked in order, the first step that fits is almost always the intended test.

## The decision sequence

**Step 0: the divergence check, always first.** Look at the terms. If $$a_n$$ does not approach 0, the series diverges by the nth-term test, and you are done in one line. Try it on $$\sum \tfrac{3n}{n+1}$$: the terms head to 3, not 0, so the series diverges and no further analysis is needed. If the terms do go to 0, the test says nothing at all (the harmonic series is the standing counterexample), and you move on. This test can never prove convergence.

**Step 1: check for the two special families.** These have complete, exact theories, so look for them before doing any real work.

- Geometric, $$\sum a r^n$$: converges exactly when $$\vert r\vert < 1$$, and you even get the sum, $$\tfrac{\text{first term}}{1 - r}$$. The field mark: the index appears only as an exponent.
- p-series, $$\sum \tfrac{1}{n^p}$$: converges exactly when $$p > 1$$. The field mark: the index appears only as a base. Remember that $$p = 1$$ is the harmonic series, which diverges.

**Step 2: factorials or exponentials mean ratio test.** When $$n!$$, $$c^n$$, or $$n^n$$ appears, anything that grows multiplicatively, the ratio $$\left\vert\tfrac{a_{n+1}}{a_n}\right\vert$$ simplifies cleanly. If the limit $$L < 1$$ the series converges absolutely; if $$L > 1$$ it diverges; and if $$L = 1$$ the test has no opinion. Every p-series returns $$L = 1$$, convergent and divergent alike, which is exactly why the ratio test is the wrong tool for algebraic terms. A model computation:

$$\sum \frac{2^n}{n!}: \quad \frac{a_{n+1}}{a_n} = \frac{2}{n+1} \to 0 < 1, \text{ so the series converges.}$$

**Step 3: polynomial and root terms mean comparison.** For algebraic terms like $$\tfrac{n}{n^3 + 4}$$ or $$\tfrac{1}{\sqrt{n^2+1}}$$, keep only the dominant term of the top and bottom to find the benchmark: $$\tfrac{n}{n^3} = \tfrac{1}{n^2}$$ for the first (a convergent benchmark), $$\tfrac1n$$ for the second (a divergent one). Then make the comparison rigorous. Limit comparison is the workhorse: divide the series by its benchmark, and a positive finite limit means the two share a fate. Direct comparison is available when the inequality falls out cleanly, but the direction matters; see the traps below.

**Step 4: alternating signs. Check absolute convergence first, then the alternating series test.** For $$\sum (-1)^n b_n$$, first test the stripped series $$\sum b_n$$ using steps 1 through 3. If it converges, your series converges absolutely and you are finished. Only when the stripped series diverges do you turn to the alternating series test: if the $$b_n$$ are positive, decreasing, and have limit zero, the series converges, and the convergence is conditional. The order matters because absolute convergence is the stronger conclusion.

**Step 5: positive, decreasing, and easy to integrate means integral test.** The field mark is $$\ln n$$ in the denominator, as in $$\sum \tfrac{1}{n \ln n}$$ or $$\sum \tfrac{1}{n(\ln n)^2}$$. Nothing else handles these well: they match neither special family, the ratio test gives $$L = 1$$, and p-series comparisons straddle them awkwardly. But the substitution $$u = \ln x$$ settles the integral in two lines, and the series shares the integral's fate. The first example diverges, since $$\ln \ln x$$ grows without bound, though barely. The second converges.

## The three traps

**Trap 1: asking the alternating series test to prove divergence.** The AST has exactly one conclusion available: converges. If its hypotheses fail, the test simply does not apply; it does not declare divergence. The divergence verdict for $$\sum (-1)^n \tfrac{n}{n+1}$$ belongs to the nth-term test, since the terms hover near $$\pm 1$$ and never vanish. Writing "diverges by the AST" attaches a correct conclusion to a test that cannot produce it, and it earns nothing.

**Trap 2: reading $$L = 1$$ as a verdict.** When the ratio test returns 1, the correct next move is a different test, usually a comparison. Under time pressure it is tempting to convert "inconclusive" into whichever answer you were hoping for. The exam writes distractors for exactly this mistake.

**Trap 3: comparing in the useless direction.** Comparison only works one way: sitting below a convergent series proves convergence, and sitting above a divergent series proves divergence. Sitting below a divergent series, or above a convergent one, proves nothing. The inequality $$\tfrac{1}{n^2 + 1} < \tfrac{1}{n^2}$$ is useful; the term $$\tfrac{1}{n^2 - 0.5}$$ sits above the same benchmark, and the direct comparison stalls. When the inequality points the wrong way, do not wrestle with it. Switch to limit comparison, which does not care about direction and is usually the faster write-up anyway.

## Writing it up for points

A convergence justification has three required parts, and the scoring guidelines check all three: name the test, verify its hypotheses, and state the conclusion. For limit comparison, that means showing the limit, noting that it is positive and finite, and naming the fate of the benchmark series. For the alternating series test, it means stating positive, decreasing, and limit zero, in writing. "It converges by comparison" with no comparison shown is a claim, not a justification.

For interval-of-convergence problems, the whole guide compresses into a two-phase routine. First, the ratio test finds the radius: it produces an inequality of the form $$\vert x - c\vert < R$$. Second, check each endpoint by hand with the numeric tests, because at an endpoint the ratio test always returns $$L = 1$$ and steps aside. The endpoints usually split one each way, a harmonic-type divergence at one end and an alternating-type convergence at the other, and each endpoint's analysis is typically its own scoring point.

<div class="article-note" markdown="1">
A fluency drill worth trying: do not solve the problems, just classify them. Take twenty series and, for each one, say which test you would run and which feature of the series tells you so, out loud, ten seconds apiece. Selecting the test is the skill the exam is actually measuring. Executing it is mostly algebra.
</div>
