# Claims ledger — Expected value is not a value you expect

Article: `_posts/2026-07-31-expected-value.md`
Session: S4 (replacement), 2026-07-31. AP Statistics sequence 7, Unit 2 topics 2.8–2.10.

Source: `ap-statistics-course-and-exam-description-effective-fall-2026.pdf` via
`pdftotext -layout`, plus the formula sheet in the CED's own appendix.

Verification: the article's `binom`, `moments`, and preset array were extracted from its
`<script>` and run under node, then compared against an independent Python implementation
using `math.comb`. All four presets agree to six decimals on both parameters, and every
preset's probabilities sum to exactly 1.

---

## Why this article replaced the one originally proposed

The original S4 proposal was *combining random variables: means add, standard deviations do
not*. **That content is no longer in the course.** Searching the revised CED returns zero
hits for sums or differences of random variables, zero for linear combinations, and zero for
variances adding. The CED's own formula sheet carries no combining formula either. The
proposal was written from the pre-revision course and was withdrawn rather than built.

Topics 2.8–2.10 were uncovered and are current, so the slot went to them.

### A related finding about the materials folder

`AP Statistics/Admin/.../ap-statistics-exam-reference-sheet-2026.pdf` is the **pre-revision**
sheet. It is headed "2026 EXAM REFERENCE INFORMATION", which is the May 2026 administration
— the last sitting of the old course. Compared against the formula sheet in the revised
CED's appendix, the file in the folder lists the **geometric distribution** with its mean
$1/p$ and standard deviation $\sqrt{1-p}/p$, which the revised course has dropped.

The correct sheet for students starting Fall 2026 is the appendix of the revised CED, which
carries the binomial and not the geometric. Recorded here and in the audit report; the file
itself was left alone.

## The definitions

`[EXAM]` Random variable and probability distribution, from EK 2.8.A.1 and 2.8.A.2,
including that "the sum of the probabilities over all possible values of a discrete random
variable is 1" — checked in the verification for all four presets.

`[EXAM]` Expected value, quoted from EK 2.9.A.2: "The expected value (or mean) of a
probability distribution is a parameter and is denoted by $E(X)$ or $\mu_X$. For a discrete
random variable $X$, the expected value is calculated as $\mu_X = \sum x_i \cdot P(x_i)$
... The expected value **can be interpreted as the long-run average outcome** of the random
variable."

The emphasised clause is the article's whole thesis. The framework never claims the expected
value is a likely outcome or an attainable one.

`[EXAM]` Standard deviation, from EK 2.9.A.3, including its own long-run reading: "the
typical deviation of the values of the random variable from the mean value ... over the long
run."

`[EXAM]` Interpretation in context, from EK 2.9.B.1 and 2.10.C.1.

## The binomial

`[EXAM]` Definition, quoted from EK 2.10.A.1: "A binomial random variable, $X$, is a
discrete random variable that counts the number of successes in repeated independent trials,
$n$, that have only two possible outcomes (success or failure), with the probability of
success $p$ and the probability of failure $1-p$."

The article's "four conditions" are a reading of this one sentence: a fixed $n$, two
outcomes, a constant $p$, and independence. Justifying that a variable is binomial is LO
2.10.A in its own right, with skill 4.B attached, which is why the article treats it as a
sentence to write rather than a checklist.

`[EXAM]` The shortcut, from EK 2.10.B.1: mean $np$, standard deviation $\sqrt{np(1-p)}$.
Also on the revised formula sheet.

`[SCOPE]` The article's remark that counting trials until a first success is no longer part
of the course is the geometric-distribution removal, verified twice: zero occurrences in the
revised CED and absent from its formula sheet, while present on the older sheet in the
materials folder. The article mentions it because a student working from an older review
book will meet the distribution and needs to know where it went.

## Computed results

Both implementations, independently:

```
  preset                     mu          sigma       sum P    mu attainable
  fair die                 3.500000    1.707825      1.0       no
  binomial n=5,  p=0.5     2.500000    1.118034      1.0       no
  binomial n=10, p=0.3     3.000000    1.449138      1.0       yes
  raffle ticket            1.500000   10.136567      1.0       no
```

`[COMPUTED]` Three of the four expected values are unattainable, which is the article's
headline claim and the reason for these four presets rather than any others. The fair die
gives 3.5 with faces 1 through 6; five fair flips give 2.5 heads with counts 0 through 5;
the raffle gives 1.50 with payouts of 0, 10 or 100.

`[COMPUTED]` The binomial shortcut agrees with the term-by-term definition sums exactly, not
approximately. For $n = 10$, $p = 0.3$: the weighted sum over all eleven outcomes returns
$\mu = 3.000000$ against $np = 3.000000$, and $\sigma = 1.449138$ against
$\sqrt{np(1-p)} = \sqrt{2.1} = 1.449138$. Same for $n = 5$, $p = 0.5$.

`[COMPUTED]` The shipped binomial coefficient is built multiplicatively rather than from
factorials, which avoids overflow and rounding at the sizes used. Checked against
`math.comb` for both presets; the resulting probability vectors sum to 1.0 to full double
precision.

`[COMPUTED]` The raffle's standard deviation of 10.1366 against a mean of 1.50 is the
article's argument that expected value alone is a poor summary of a lottery. Its variance is
$105 - 1.5^2 = 102.75$, since $E(X^2) = 10000(0.01) + 100(0.05) = 105$.

`[SCOPE]` The closing note claims the running average often moves *away* from 1.50 before
returning. This is a property of the distribution rather than a scripted event: a single
prize of 100 arriving at trial $k$ lifts the running average by roughly $100/k$, which
exceeds the whole expected value for any $k$ below 67. The note describes what the reader
will usually see and explains it, rather than asserting it always happens.

## Placement

Sequence 7, between conditional probability and the Central Limit Theorem, which puts the
Statistics band in course order through Unit 2. Everything from the old sequence 7 upward
shifted by one; the band now runs 1–15 with no gaps.

Fifteen articles and one featured card is 16 grid cells: exact on mobile, two trailing cells
on desktop, no mid-grid holes at either breakpoint.
