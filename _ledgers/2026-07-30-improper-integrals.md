# Claims ledger — Improper integrals, and the exponent that decides

Article: `_posts/2026-07-30-improper-integrals.md`
Session: 7D article 19, 2026-07-30. AP Calculus **BC only**, sequence 24, Unit 6 topic 6.13, with
a forward reference to Unit 10.

Verification: `t.js` loads the shipped script in jsdom with a stubbed canvas context and sweeps a
grid of $(p, d)$ pairs — 93 values of $p$ against 42 values of $d$ — comparing both partial
integrals against independently written closed forms, then checks the convergence verdicts at
every one of the 1201 positions of $p$. Symbolic results from SymPy.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **Enduring understanding LIM-6**, quoted in the opening: "The use of limits allows us to
show that the areas of unbounded regions may be finite." The article's remark that this states a
result rather than a technique is an observation about the sentence, which is unusual among the
enduring understandings for exactly that reason.

`[EXAM]` **LIM-6.A.1**, the definition, paraphrased closely in the second section: "An improper
integral is an integral that has one or both limits infinite or has an integrand that is
unbounded in the interval of integration."

`[EXAM]` **LIM-6.A.2**: "Improper integrals can be determined using limits of definite
integrals." That is the whole procedure and the article says so.

`[EXAM]` Learning objective **LIM-6.A**: "Evaluate an improper integral **or determine that the
integral diverges**." Both outcomes are named in the objective, which is why the tool's panel
prints "diverges" rather than a number when it should.

`[EXAM]` Topic 6.13 is "Evaluating Improper Integrals", marked bc only, suggested skill 1.E.

`[EXAM]` **The forward reference to Unit 10 is the framework's own recommendation.** Unit 10's
overview: "Students should build connections to past learning, such as how evaluating improper
integrals relates to the integral test." Topic 10.4 is "Integral Test for Convergence"
(LIM-7.A.6, bc only) and topic 10.5 is "Harmonic Series and p-Series", so both halves of the
connection the article draws are course content.

`[STANDARD]` The $p$-series threshold — $\sum n^{-p}$ converges exactly when $p > 1$ — is
standard and is topic 10.5's content. SymPy confirms the sums at $p = 1$ (diverges),
$p = \tfrac32$ ($\zeta(3/2)$), and $p = 2$ ($\pi^2/6$); at $p = \tfrac12$ it declines to evaluate
and returns the sum unchanged, so that case rests on the standard theorem rather than on a
computation.

## Computed results

`[COMPUTED]` **The $p$-integral at infinity**, from SymPy:

```
  p = 1/2   ∫₁^∞ x^-p dx = ∞
  p = 1                  = ∞
  p = 3/2                = 2      = 1/(p−1)
  p = 2                  = 1      = 1/(p−1)
  p = 3                  = 1/2    = 1/(p−1)
```

`[COMPUTED]` **The $p$-integral at zero**, the mirror image:

```
  p = 1/2   ∫₀¹ x^-p dx  = 2      = 1/(1−p)
  p = 1                  = ∞
  p = 3/2                = ∞
  p = 2                  = ∞
  p = 3                  = ∞
```

Converges exactly when $p < 1$, diverges exactly when $p \geq 1$. The two thresholds are
opposite and both are strict, which is the article's central claim and the reason no $p$ makes
$\int_0^\infty x^{-p}dx$ finite.

`[COMPUTED]` **The panel matches independently written closed forms** at every $(p,d)$ pair on a
93 by 42 grid — 3906 pairs — with worst relative discrepancy $5.0\times10^{-5}$, exactly half the
last displayed digit on both curves.

`[COMPUTED]` **The verdicts flip at $p = 1$ and both fail there.** Checked at
$p = 0.5,\ 0.9975,\ 1,\ 1.0025,\ 2$: the outer integral converges only for $p > 1$ and the inner
only for $p < 1$, including one slider step either side of 1. At $p = 1$ both notes read
"diverges". Sweeping all 1201 values of $p$, the full-range row reads "diverges" every time —
zero exceptions.

`[COMPUTED]` **The values the prose quotes**, read from the running panel:

```
  p = 2,   d = 3   outer 0.9990  → 1/(p−1) = 1        inner 999.0000, diverging
  p = 0.5, d = 3   inner 1.9368  → 1/(1−p) = 2        outer 61.2456, diverging
  p = 1,   d = 3   outer = inner = 6.9078 = 3 ln 10, both linear in d
```

The symmetry at $p = 1$ is exact: both partial integrals equal $d\ln 10$.

`[COMPUTED]` **The two worked examples.** $\int_1^T x^{-2}dx = 1 - \tfrac1T \to 1$ and
$\int_s^1 x^{-1/2}dx = 2 - 2\sqrt{s} \to 2$, both from SymPy.

`[COMPUTED]` **The interior blow-up.** The naive evaluation $\left[-\tfrac1x\right]_{-1}^{1}$
gives exactly $-2$. SymPy returns $\infty$ for $\int_0^1 x^{-2}dx$ and for $\int_{-1}^0 x^{-2}dx$
separately, so the split integral diverges on both halves. The integrand is positive wherever
defined, so $-2$ is not merely wrong but impossible, which is the article's point.

`[COMPUTED]` **Slider resolution.** $p$ runs 0 to 3 in 1200 steps and $d$ runs 0 to 6 in 1200
steps, so $p = 0.5, 1, 1.5, 2$ land on positions 200, 400, 600, 800 and $d = 1, 3, 6$ on 200,
600, 1200. All verified in the harness.

## Judgment claims

`[JUDGMENT]` "Everything hard about improper integrals is in deciding which ones are finite."
A framing claim the article then supports with the $p$ dichotomy.

`[JUDGMENT]` "The absurd answer is the useful part." An argument about how to read an impossible
result, not a claim about frequency.

`[JUDGMENT]` The closing note's two habits — write the limit every time, scan the integrand
before starting — are teaching advice offered as such.

---

## Flags raised in this session

1. **Zero cross-links on the first pass again**, the second time in three articles. Three added,
   and the best of them was worth the article's only new paragraph: the $p$-integral threshold and
   the $p$-series threshold are the same number, and the framework explicitly recommends building
   that connection. It links to your harmonic series article, which is the $p = 1$ case, and it
   turns an isolated Unit 6 fact into the thing Unit 10 will spend three topics on.

2. **A display-format issue caught before it mattered.** Values above $10^5$ printed with three
   exponential decimals — four significant figures — so at $p = 0.1625$, $d = 5.95$ the panel's
   reading was $4\times10^{-4}$ off in relative terms from the true value. Raised to five
   significant figures. Fourth article running where the formatter, not the mathematics, was the
   loose end; I have started checking the formatter against the tightest claim in the article
   before writing the test.

3. **A verification I could not complete.** SymPy declines to evaluate $\sum n^{-1/2}$ and
   returns it unchanged. The $p$-series result is standard and is Unit 10 content, so the article
   states it, but the ledger records that this one case rests on the theorem rather than on
   something I executed.

4. **805 words**, four `##` headings, no italics, three cross-links, all resolving. Inside the
   650–950 target.

5. **The log-log panel is a design choice worth your eye.** Drawing $y = x^{-p}$ on logarithmic
   axes turns every power function into a straight line of slope $-p$ and turns the $p = 1$
   threshold into a fixed diagonal, so the dichotomy becomes a line crossing a line. That is a
   representation students will not have seen in this course, and it is the only place in the
   corpus using log axes. If it reads as unfamiliar rather than clarifying, the alternative is
   ordinary axes with a much narrower window and no visible threshold.

6. **Unit 6 is now complete** except topics 6.1–6.3 and 6.8–6.10, which are Riemann sums,
   antiderivative basics, and substitution. Your 25 July Riemann sums article covers 6.2–6.3.
   Substitution has no article and is the technique the closing note of the previous article
   names first. It is not in the approved plan.
