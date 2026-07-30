# Claims ledger — What a p-value is, and what it is not

Article: `_posts/2026-07-30-what-a-p-value-is.md`
Session: 7A, 2026-07-30

Every checkable claim the article makes, one per line, tagged. `[COMPUTED]` entries name
the script that produced them; all scripts are reproducible from the code quoted below.

Verification scripts, run in this session:

- `verify.py` — Hart normal CDF against published values; the worked example; the
  binomial/normal comparison that drove the design decision; Monte Carlo convergence.
- `core.js` / `test-core.js` — the same functions as shipped in the article, tested under
  node with 400,000-draw Monte Carlo checks on every alternative.
- `harness.js` — a DOM stub that runs the article's own `<script>` verbatim and reads the
  numbers back out of the readout, so the prose is checked against the shipped code rather
  than against a reimplementation.

---

## Setup and definitions

`[STANDARD]` A p-value is the probability, computed under the null hypothesis, of a test
statistic at least as extreme as the observed one. This is the definition in any standard
treatment, and it is the AP framework's topic 3.6 (p-Values) in the course effective
2026-27.

`[STANDARD]` A quantity computed under the assumption that $H_0$ holds cannot report the
probability that $H_0$ holds. The p-value is $P(\text{data at least this extreme} \mid H_0)$;
the thing students want is $P(H_0 \mid \text{data})$. These are different conditionals, and
the second is not obtainable from the first without a prior.

`[STANDARD]` If the population is normal and $\sigma$ is known, the sampling distribution of
$\bar{x}$ is exactly normal with mean $\mu$ and standard deviation $\sigma/\sqrt{n}$ — no
approximation, at any $n$. This is what makes the article's simulation converge to the
theory curve's area exactly rather than approximately.

`[COMPUTED]` $\sigma/\sqrt{n} = 10/\sqrt{25} = 2$.

```
>>> 10/math.sqrt(25)
2.0
```

## The normal CDF used in the interactive

`[COMPUTED]` The shipped `Phi(z)` (Hart 1968 rational approximation) has absolute error
below $3 \times 10^{-16}$ against published standard-normal values.

```
=== JS Phi against published values ===
  Phi(0)                   err 0.00e+0        Phi(2)                   err 2.22e-16
  Phi(0.5)                 err 0.00e+0        Phi(2.3263478740408408)  err 0.00e+0
  Phi(1)                   err 0.00e+0        Phi(2.5758293035489004)  err 0.00e+0
  Phi(1.2815515655446004)  err 1.11e-16       Phi(3)                   err 1.11e-16
  Phi(1.6448536269514722)  err 0.00e+0        Phi(4)                   err 1.11e-16
  Phi(1.9599639845400545)  err 0.00e+0        Phi(5)                   err 1.11e-16
  worst absolute error: 2.220e-16
  Phi(z) + Phi(-z) = 1 to 1e-15 at z = 0.3, 1, 1.96, 2.5, 3.3
```

Reference values are from the standard normal distribution to 15 decimal places; the four
quantile-argument checks use full-precision quantiles, since truncating them to 12 digits
produces a spurious $7 \times 10^{-14}$ discrepancy that is in the argument, not the
algorithm.

## The worked example

All read back from the article's own shipped script via `harness.js`, not recomputed.

`[COMPUTED]` $z = (53.92 - 50)/2 = 1.96$.

`[COMPUTED]` $H_a: \mu > 50 \Rightarrow p = 0.0250$ (0.024997895148).

`[COMPUTED]` $H_a: \mu < 50 \Rightarrow p = 0.9750$ (0.975002104852).

`[COMPUTED]` $H_a: \mu \neq 50 \Rightarrow p = 0.0500$ (0.049995790296), and this equals
twice the one-tail area to machine precision.

`[COMPUTED]` The two-sided mirror bound is $50 - 3.92 = 46.08$.

```
  default z (xbar 53.92, n 25)   1.96     want 1.96
  default SE                     2        want 2
  p, mu > 50                     0.025    want 0.025
  p, mu < 50                     0.975    want 0.975
  p, mu != 50                    0.05     want 0.05
  two-sided = 2 x right tail              equal to 1e-15
```

`[COMPUTED]` The simulation's highlighted region matches the region the p-value integrates,
for all three alternatives. 400,000 draws each:

```
  simulated share, lt   0.975320   theory 0.975002   (within 4 standard errors)
  simulated share, gt   0.024960   theory 0.024998
  simulated share, ne   0.049733   theory 0.049996
  left  half of the two-sided region  0.024988   each tail 0.024998
  right half of the two-sided region  0.024825   each tail 0.024998
```

## Claims in "What the number does not say"

`[COMPUTED]` At an observed mean of 50.4 the p-value exceeds 0.4 (0.4207 one-sided,
0.8415 two-sided).

`[COMPUTED]` With the effect held at one point and the alternative two-sided, the p-value
falls 0.6171 → 0.3173 → 0.0455 at $n = 25, 100, 400$, and the verdict flips to reject at
$n = 400$.

```
  n =   25   SE = 2.0000   z = 0.500   two-sided p = 0.61707508
  n =  100   SE = 1.0000   z = 1.000   two-sided p = 0.31731051
  n =  400   SE = 0.5000   z = 2.000   two-sided p = 0.04550026
  verdict at n=400: p <= a = 0.05, so reject the null
```

All three values are reachable on the shipped control: the sample-size slider runs 4 to 400.
An earlier draft cited $n = 1600$ against a slider that stopped at 200, which the harness
caught.

`[STANDARD]` A large p-value is not evidence for $H_0$, because a result unsurprising under
$H_0$ is also unsurprising under many nearby alternatives. Stated in the article with a
worked instance rather than as an assertion.

`[STANDARD]` The p-value is not the probability that the test has erred. Whether an error
occurred depends on the unknown true $\mu$. The Type I error rate is a property of the
procedure, fixed in advance at $\alpha$; the p-value is a function of the data.

`[STANDARD]` $\alpha$ is fixed before the data are seen.

`[EXAM]` The AP framework retains a topic on errors in testing: topic 3.8, "Potential Errors
When Performing Tests," in the course effective 2026-27. Supported by the College Board
Course and Exam Description, Course at a Glance. The article deliberately does not use the
phrase "Type I error," because I verified that the topic exists but not that the CED's
essential-knowledge statements still use that term. See the flag below.

## Claims about the conclusion sentence

`[EXAM]` A complete conclusion links the p-value to $\alpha$, gives the decision, and states
what it means about the alternative in context. Supported by College Board scoring
guidelines language: where no $\alpha$ is given, "the solution must be explicit about the
linkage by giving a correct interpretation of the p-value or explaining how the conclusion
follows from the p-value."

`[EXAM]` A conclusion equivalent to accepting the null is not credited. Supported directly:
"If the response includes a statement that is equivalent to accepting the null hypothesis
… then component 2 is not satisfied."

`[EXAM]` A conclusion must be in context — naming the variable and the population. Supported
by the same scoring guidelines, which require the conclusion "in the context of the
problem."

`[EXAM]` An explicit "reject / fail to reject" is not strictly required if the decision is
implied by "convincing evidence" wording. Verified but **not used in the article**, because
it is a permission rather than a requirement and would muddy the advice. Recorded here so
the omission is deliberate.

## Claims in the closing note

`[COMPUTED]` Dragging the observed mean under a two-sided alternative until $p = 0.0500$
stops at 53.92.

`[COMPUTED]` The 95% interval $53.92 \pm 1.96(2)$ has lower end 50.00.

```
  two-sided p hits 0.0500 at xbar   53.92
  95% CI lower bound there          50.000072   (exact knife edge: xbar = 50 + 1.96*SE
                                                 = 53.9199279691, p = 0.0500000000,
                                                 CI lower bound = 50.0000000000)
```

`[STANDARD]` The duality is exact for a z-test with known $\sigma$: the two-sided test
rejects $H_0: \mu = \mu_0$ at level $\alpha$ if and only if $\mu_0$ falls outside the
$(1-\alpha)$ confidence interval.

## Judgment claims

`[JUDGMENT]` Students want the p-value to mean the probability that $H_0$ is true. Widely
reported as the dominant misinterpretation, and the premise of the article brief.

`[JUDGMENT]` Reporting one tail for a two-sided test is a standing error in this topic. The
article carries an inline `<!-- VERIFY -->` at this sentence. I softened the brief's "most
common error" to "a standing error," which I can support; the stronger claim I cannot.

---

## Flags raised in this session

1. **"Type I error" as exam vocabulary.** Topic 3.8 exists and is called "Potential Errors
   When Performing Tests." I could not retrieve the CED's essential-knowledge statements for
   Unit 3 — the fetch of the 4 MB PDF truncated before them — so I do not know whether the
   revised framework still uses the phrases "Type I error" and "power." The article makes
   the statistical point without the vocabulary. If you confirm the terms are still in use,
   the sentence "It is not the probability that this test has made an error" can name them.

2. **The known-$\sigma$ z-test is an idealization.** AP tests a mean with $t$, since
   $\sigma$ is never known. The article uses known $\sigma$ so the sampling distribution is
   exactly normal and the simulation converges to the theory area exactly. This follows the
   precedent your 95% confidence article sets, which makes the same idealization and flags
   it in its closing note. This article does not currently flag it. Worth deciding.

3. **Unit context.** p-values are introduced in Unit 3 (proportions) in the revised
   framework, and this article uses a mean. The concept is identical and the picture is
   cleaner with a mean, but a student reading alongside the course will meet p-values first
   with $\hat{p}$. The article does not mention units at all, which sidesteps it.

4. **Length. Corrected 2026-07-30, later the same session.** This ledger first recorded
   1060 words against a stated corpus median of 802. Both figures were wrong: the measuring
   script removed the `viz` block with a non-greedy `.*?</div>`, which stops at the first
   nested `viz-controls` close and leaves every button label counted as prose. Measured
   properly, by `<div>` depth, this article is **952 words** against a corpus median of
   **714** and a maximum of 1128. It sits seventh of thirty-two, which is a comfortable
   place for a dense interactive piece and needs no trimming. The style sheet's length
   table and measurement notes have been corrected.

5. **A design decision worth recording.** The first design used a sample proportion, which
   matches where the course introduces p-values. I abandoned it: at $n = 50$ the exact
   binomial tail is 0.0595 while the normal approximation gives 0.0448, a 25% relative gap
   that never closes (still 8% at $n = 1000$). The simulation would visibly fail to converge
   to the computed p-value, contradicting the article's central claim. The mean setup has no
   approximation anywhere.
