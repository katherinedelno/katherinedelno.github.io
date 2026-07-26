---
layout: post
title: "Which convergence test? A field guide"
date: 2026-07-24
description: "Ten seconds of looking should tell you which test to run. The decision sequence I teach, what each test can and cannot conclude, and the three traps the exam sets with them."
course: "AP Calculus BC"
read_time: "7 min read"
math: true
---

Students usually learn the convergence tests as a heap: seven tools, each with hypotheses and a conclusion, no order. Then a series appears and the heap offers no advice about where to start. The fix is to stop thinking *toolbox* and start thinking *field guide* — series have visible field marks, and the marks tell you which test wants the job. Worked in order, the first step that fits is almost always the intended test.

## The decision sequence

**Step 0 — the divergence check, always first.** Look at the terms. If $$a_n \not\to 0$$, the series diverges by the **nth-term test**, and you are done in one line. Try it on $$\sum \tfrac{3n}{n+1}$$: the terms head to 3, not 0 — diverges, no further analysis. If the terms *do* go to 0, the test says nothing at all (the harmonic series is the eternal counterexample), and you move on. This test can never, under any circumstances, prove convergence.

**Step 1 — recognize royalty.** Two families have complete, exact theories, so check for them before doing any work:

- **Geometric** $$\sum a r^n$$: converges exactly when $$|r| < 1$$, and you even get the sum, $$\tfrac{\text{first term}}{1 - r}$$. Field mark: the index appears only as an *exponent*.
- **p-series** $$\sum \tfrac{1}{n^p}$$: converges exactly when $$p > 1$$. Field mark: the index appears only as a *base*. Remember the cliff edge: $$p = 1$$ (harmonic) diverges.

**Step 2 — factorials or exponentials? Ratio test.** When $$n!$$, $$c^n$$, or $$n^n$$ appear — anything that grows multiplicatively — the ratio $$\left|\tfrac{a_{n+1}}{a_n}\right|$$ collapses beautifully. $$L < 1$$ converges (absolutely), $$L > 1$$ diverges, and $$L = 1$$ means the test *has no opinion* — every p-series returns $$L = 1$$, convergent and divergent alike, which is exactly why the ratio test is the wrong tool for algebraic-looking terms.

$$\sum \frac{2^n}{n!}: \quad \frac{a_{n+1}}{a_n} = \frac{2}{n+1} \to 0 < 1 \;\Rightarrow\; \text{converges.}$$

**Step 3 — polynomial-and-root terms? Compare.** For algebraic terms like $$\tfrac{n}{n^3 + 4}$$ or $$\tfrac{1}{\sqrt{n^2+1}}$$, keep only the dominant term of top and bottom to find the benchmark: $$\tfrac{n}{n^3} = \tfrac{1}{n^2}$$ for the first (convergent benchmark), $$\tfrac1n$$ for the second (divergent). Then make it rigorous with a comparison. **Limit comparison** is the workhorse: divide the series by its benchmark, and a positive finite limit means they share a fate. **Direct comparison** is available when the inequality is clean, but mind the direction — see the traps.

**Step 4 — alternating signs? Absolute first, then AST.** For $$\sum (-1)^n b_n$$, check the stripped series $$\sum b_n$$ first, using steps 1–3: if it converges, your series converges **absolutely** and you're done, full stop. Only when the stripped series diverges do you reach for the **alternating series test**: $$b_n$$ positive, decreasing, limit zero gives convergence — now merely **conditional**. The order matters because absolute convergence is the stronger, cleaner verdict, and because the AST's conclusion can't be upgraded afterward.

**Step 5 — positive, decreasing, and built for a u-sub? Integral test.** The field mark is $$\ln n$$ in the denominator: $$\sum \tfrac{1}{n \ln n}$$, $$\sum \tfrac{1}{n(\ln n)^2}$$. Nothing else touches these — the geometric/p-series forms don't match, ratios give $$L = 1$$, comparisons with p-series straddle awkwardly — but the substitution $$u = \ln x$$ dispatches the integral in two lines. The first diverges ($$\ln \ln x \to \infty$$, barely); the second converges. The series inherits the integral's verdict.

## The three traps

**Trap 1 — asking the AST to prove divergence.** The alternating series test has exactly one conclusion available: *converges*. If its hypotheses fail — say the terms don't shrink to zero — the AST doesn't declare divergence; it simply walks off the job. The divergence verdict for $$\sum (-1)^n \tfrac{n}{n+1}$$ belongs to the nth-term test (the terms bounce between values near $$\pm 1$$ and never vanish). Citing "diverges by AST" is a scoring-guideline classic — the right conclusion attributed to a test that cannot produce it earns nothing.

**Trap 2 — reading $$L = 1$$ as a verdict.** Ratio test returns 1: the correct next move is a different test, usually a comparison. Students under time pressure convert "inconclusive" into whichever answer they were hoping for. The exam knows this and provides candidates generously.

**Trap 3 — comparing in the useless direction.** Comparison is one-way glass: being **below a convergent** series proves convergence; being **above a divergent** series proves divergence. Below a divergent series, or above a convergent one, proves precisely nothing. When the inequality points the wrong way — $$\tfrac{1}{n^2 + 1} < \tfrac{1}{n^2}$$ works, but $$\tfrac{1}{n^2 - 0.5}$$ sits *above* the benchmark — don't wrestle with it; switch to limit comparison, which is direction-blind and almost always the faster write-up anyway.

## Writing it up for points

A convergence justification has three mandatory parts, and the scoring guidelines check all three: **name the test, verify its hypotheses, state the conclusion.** For limit comparison, that means exhibiting the limit and noting it is positive and finite *and* naming the fate of the benchmark. For the AST: positive, decreasing, limit zero — all three, in writing. "It converges by comparison" with no comparison shown is a claim, not a justification.

For interval-of-convergence problems, the whole guide compresses into a two-phase routine: **ratio test for the radius** (it will happily produce $$|x - c| < R$$), then **hand-check each endpoint** with the numeric tests — the ratio test always returns $$L = 1$$ at an endpoint, which is it formally recusing itself. Endpoints are usually one harmonic-type divergence and one alternating-type convergence, and each endpoint's analysis is typically its own scoring point.

<div class="article-note" markdown="1">
Fluency drill: don't do the problems — just *classify* them. Take twenty series and, for each, say only which test you'd run and why the field marks say so, out loud, ten seconds apiece. Selection is the skill the exam is actually testing; execution is Unit 6 algebra wearing a costume.
</div>
