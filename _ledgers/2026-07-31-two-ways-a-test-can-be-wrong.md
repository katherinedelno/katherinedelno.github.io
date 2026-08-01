# Claims ledger — The two ways a test can be wrong

Article: `_posts/2026-07-31-two-ways-a-test-can-be-wrong.md`
Session: S1, 2026-07-31. AP Statistics sequence 12, Unit 3 topic 3.8.

Source: `ap-statistics-course-and-exam-description-effective-fall-2026.pdf`, extracted with
`pdftotext -layout`. Topic 3.8 detail is at lines 4794–4895 of the extraction.

Verification: the article's own `<script>` was extracted, its two numeric functions (`se`
and `phi`) run under node against every setting the prose quotes, and the results compared
against `scipy.stats.norm` computed independently in Python. 12 cases, worst disagreement
$6.1 \times 10^{-8}$, against a display rounded to four decimals.

---

## Placement

`[EXAM]` Topic 3.8 is "Potential Errors When Performing Tests", sitting in Unit 3
(*Inference for Categorical Data: Proportions*) between 3.7, "Carrying Out a Test for a
Population Proportion", and 3.9, "Sampling Distributions for the Difference Between Two
Sample Proportions". The article is therefore built on a one-proportion test rather than a
mean, which is where the framework puts the topic. There is no parallel errors topic in
Unit 4.

`[EXAM]` The three skills attached to 3.8 are 2.D (identify types of errors and
relationships among components in statistical inference methods), 3.C (calculate and
estimate expected counts, percentages, probabilities, and intervals), and 4.D (interpret
statistical calculations and results to assess meaning or a claim). The article's three
sections after the interactive answer to those three skills in that order.

## The definitions

`[EXAM]` Type I error, quoted from EK 3.8.A.1: "A Type I error occurs when there is
convincing statistical evidence that the alternative hypothesis is true (due to the small
p-value), but it is not." The article paraphrases this closely and keeps the framework's
structure of pairing a verdict with a truth.

`[EXAM]` Type II error, quoted from EK 3.8.A.2: "A Type II error occurs when there is not
convincing statistical evidence that the alternative hypothesis is true (due to the large
p-value), but it is."

`[EXAM]` Power, quoted from EK 3.8.A.3: "The power of a hypothesis test is the probability
that a hypothesis test will correctly reject the false null hypothesis."

`[EXAM]` $$\alpha$$ as the probability of a Type I error, and its being set in advance,
from EK 3.8.B.1: "The probability of making a Type I error is defined as the significance
level, $\alpha$. For a given study and hypothesis test, the probability of making a Type I
error is typically set to a small value (e.g., 0.01, 0.05, 0.10) prior to collecting the
data." The three buttons in the interactive are exactly the framework's three examples.

`[EXAM]` The complement relation, from EK 3.8.B.2: "The probability of making a Type II
error is 1 − power." The article displays this as its only display equation in the opening
half, because it is the only calculation the topic actually requires.

`[EXAM]` The 0.80 benchmark, from EK 3.8.C.1: "the probability of a Type II error should
ideally be small, and thus, the power will be large (e.g., P(Type II error) = 0.20 and
power = 0.80)." The readout compares against 0.80 for this reason and names it as the
framework's benchmark rather than as a law.

## The four factors

`[EXAM]` Quoted in full from EK 3.8.C.1: "The probability of a Type II error decreases and
the power increases when any one of the following occurs, **provided the others do not
change**: (i) Sample size(s) increases. (ii) Standard error decreases. (iii) True parameter
value is farther from the null hypothesis. (iv) Significance level $\alpha$ of a test
increases."

The article's claim that three controls cover four factors rests on (i) and (ii) being one
lever here: for a one-proportion test the standard error is
$\sqrt{p_0(1-p_0)/n}$, so $n$ is the only thing on screen that moves it. This is stated in
the prose rather than left implicit.

The emphasised clause is the reason the interactive has separate controls at all. Each
factor is demonstrated by moving one control and reading that the other two quantities hold
still, which is a claim the prose could assert but not show.

## Consequences

`[EXAM]` Asymmetry of consequences, from EK 3.8.D.1: "In some studies, making a Type I
error may have more serious consequences than making a Type II error. In other studies,
making a Type II error may have more serious consequences than making a Type I error. The
consequences of each error should be considered prior to conducting the study."

`[EXAM]` Consequences setting $$\alpha$$, from EK 3.8.D.2: "Because the significance level,
$\alpha$, is the probability of making a Type I error, the consequences of a Type I error
influence decisions about a significance level."

`[EXAM]` Consequences setting $$n$$, from EK 3.8.D.3: "Because sample size influences the
probability of making a Type II error, the consequences of a Type II error influence
decisions about how large the sample size should be."

The production-line context was chosen so that both errors have real and opposed costs —
lost production against defective parts reaching customers — which is what 3.8.D.1 asks
students to weigh. No claim is made about which is worse.

## Scope, and what the article declines to teach

`[SCOPE]` The article states that nothing on the exam requires producing $$\beta$$ from a
normal curve. This is an inference from the framework rather than a quotation: EK 3.8.B.2
gives $$\beta$$ only as $$1 - \text{power}$$, and no essential knowledge statement in 3.8
describes computing either quantity from a sampling distribution. The interactive performs
that computation so the four factors of 3.8.C become visible, and the prose says so rather
than leaving a student to think the calculation is examinable.

`[SCOPE]` The critical-value construction $$p^* = p_0 + z^*\sqrt{p_0(1-p_0)/n}$$ uses the
null value in the standard error, which is the convention for a one-proportion test.
$$\beta$$ is then computed under the true $$p$$ with its own standard error
$$\sqrt{p(1-p)/n}$$. Both choices are standard and neither is examinable.

## Computed results

All independently recomputed in Python with `scipy.stats.norm`, not read off the tool.
$$p_0 = 0.10$$, right-tailed test throughout.

```
     p     n  alpha       p*      beta    power     quoted in prose
  0.15   200   0.05   0.1349   0.2748   0.7252     yes, base case
  0.15   200   0.10   0.1272   0.1831   0.8169     yes
  0.15   200   0.01   0.1493   0.4897   0.5103     yes
  0.15   400   0.05   0.1247   0.0780   0.9220     yes
  0.15   800   0.05   0.1174   0.0050   0.9950     no
  0.15   100   0.05   0.1493   0.4927   0.5073     no
  0.12   200   0.05   0.1349   0.7415   0.2585     yes
  0.20   200   0.05   0.1349   0.0107   0.9893     yes
  0.25   200   0.05   0.1349   0.0001   0.9999     no
  0.10   200   0.05   0.1349   0.9500   0.0500     yes, power = alpha
  0.10   200   0.01   0.1493   0.9900   0.0100     yes, power = alpha
  0.15   253   0.05   0.1310   0.1990   0.8010     yes, closing note
```

`[COMPUTED]` Power at the null equals $$\alpha$$ exactly, to every digit the readout shows,
at all three levels. This is not a numerical coincidence: power is the rejection
probability evaluated at the truth, and at $$p = p_0$$ that is the rejection probability
under a true null, which is the definition of $$\alpha$$. The article makes the argument
rather than resting on the arithmetic.

`[COMPUTED]` The smallest $$n$$ giving power at least 0.80 against $$p = 0.15$$ at
$$\alpha = 0.05$$ is **253**, at which power is 0.8010. Checked by scanning $$n$$ from 50
upward. This is the number the closing note asks the reader to guess.

`[COMPUTED]` The claim that $$\alpha$$ never moves when $$n$$ or the true rate moves is
exact by construction rather than approximate: the cut is defined as
$$p_0 + z^*\sqrt{p_0(1-p_0)/n}$$, so the null-curve tail area beyond it is $$\alpha$$ for
every $$n$$. The table confirms it — the top-panel area is 0.05 at $$n = 100$$, 200, 400
and 800 alike.

`[COMPUTED]` The normal CDF shipped in the article is Abramowitz and Stegun 7.1.26 through
`erf`, documented in a comment with its stated error bound of $$1.5 \times 10^{-7}$$.
Measured against `scipy` across the twelve cases above, the worst disagreement in any
printed quantity was $$6.1 \times 10^{-8}$$ — two orders of magnitude finer than the four
decimals displayed. The three $$z^*$$ values are hardcoded to 16 digits rather than
computed, so no inverse-normal approximation enters anywhere.

## Notes for a later session

- Statistics currently sits at 12 articles and one featured card, which is 13 grid cells
  against a 3-column grid and leaves two empty cells in the last row. It returns to exact at
  14 articles, and again at 16 articles with 5 featured, which is the end state of the
  proposal batch. No action needed in between.
- `which-chi-square-test` moved from sequence 12 to 13 to make room. The Statistics band
  still has an open slot at sequence 6.
