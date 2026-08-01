# Claims ledger — Describing a distribution in the exam's own words

Article: `_posts/2026-07-31-describing-a-distribution.md`
Session: S3, 2026-07-31. AP Statistics sequence 1, Unit 1 topics 1.6–1.9.

Source: `ap-statistics-course-and-exam-description-effective-fall-2026.pdf` via
`pdftotext -layout`. Topics 1.5–1.9 run from roughly line 1790 to line 2300 of the
extraction.

Verification: the article's own `med` and `summarize` functions were extracted from its
`<script>`, run under node at **every one of the 91 slider positions**, and compared against
an independent Python implementation of the same statistics. Worst disagreement
$4.7 \times 10^{-7}$ across mean, median, standard deviation, both quartiles, the
interquartile range, both fences, both whisker endpoints, and both outlier verdicts. No
mismatches.

---

## The four parts of a description

`[EXAM]` Quoted from EK 1.6.A.1: "Descriptions of the distribution of one quantitative
variable include shape, center, and variability (spread) as well as any unusual features
such as outliers, gaps, or clusters in context." The article treats the closing phrase as
load-bearing rather than decorative, which is where it puts the emphasis.

`[EXAM]` Skew, from EK 1.6.A.2: skewed right when "the right tail (toward larger values) is
longer than the left", skewed left when the left tail is longer, approximately symmetric
when "the left half is approximately the mirror image of the right half." The article does
not restate this at length because the interactive does not vary shape; it is cited only
through the mean-median diagnostic below.

`[EXAM]` The mean-median relationship, quoted from EK 1.8.B.1: "If a distribution is
relatively symmetric, then the values of the mean and median are relatively close to each
other. If a distribution is skewed right, then the value of the mean is usually larger than
the median. If the distribution is skewed left, then the value of the mean is usually
smaller than the median." Note *usually* — the article preserves the hedge.

## Summary statistics

`[EXAM]` Centre and position, from EK 1.7.A.1–1.7.A.6: mean and median as the two common
measures of centre; minimum and maximum; and the quartile definition the interactive
implements, EK 1.7.A.5: "The first quartile, denoted by $Q_1$, is the median value of the
lower half of the ordered data set from the minimum value to the position of the median."

This wording is why the shipped code computes quartiles as the median of each half with the
middle value excluded when the count is odd, rather than by any interpolation rule. It is
*not* what `numpy.percentile` returns by default, so the Python check reimplements the
framework's method rather than calling a library. Getting this wrong would have shifted
every fence in the article.

`[EXAM]` Variability, from EK 1.7.B.1–1.7.B.4: range, interquartile range as $Q_3 - Q_1$,
and the sample standard deviation with its $n-1$ denominator. The interactive uses $n-1$.

`[EXAM]` The five-number summary and the boxplot, from EK 1.8.A.1–1.8.A.2. The whisker rule
is quoted almost verbatim in the caption and the closing note: "If there are outliers in the
data, the whiskers extend to the most extreme data values that are not outliers, and
outliers are usually denoted with an asterisk or other symbol." The interactive draws
outliers as open squares and stops the whiskers at the extreme values inside the fences,
which is the behaviour the closing note asks the reader to account for.

## Two outlier rules

`[EXAM]` Both quoted from EK 1.7.D.1, which opens "There are many methods for determining
potential outliers. Two methods frequently used are as follows":

- 1.7.D.1.i — "An outlier is a value located more than $1.5 \times \text{IQR}$ above the
  third quartile or more than $1.5 \times \text{IQR}$ below the first quartile."
- 1.7.D.1.ii — "An outlier is a value located more than 2 standard deviations above, or
  below, the mean."

That the framework names two and that they disagree on ordinary data is the article's
sharpest claim, and it is the framework's own text rather than an outside observation. The
article does not assert that either rule is correct, only that the quartile rule is built
from statistics a candidate outlier cannot move and the deviation rule is not.

## Comparison

`[EXAM]` From EK 1.9.A.1: "Boxplots may be used to compare center, variability, outliers,
and skewness (or symmetry)." The article cites this exactly, and the omission of *shape*
beyond skewness from that list is the reason it notes that a bimodal distribution can hide
inside an ordinary-looking box.

`[EXAM]` Topic 1.9 carries skill 4.A, "Describe and **compare** tabular and graphical
representations". The article's claim that describing two distributions separately does not
answer a comparison question rests on that skill wording plus EK 1.9.B.1.

## Computed results

Base data, fixed: 52, 58, 61, 63, 64, 66, 67, 69, 72, 78, 84. Twelfth value roves from 40
to 130. Quartiles by the framework's method throughout.

```
  rover    mean   median      s     Q1    Q3    IQR   lower    upper
     40   64.50    65.00  11.52   62.0  73.0   11.0    45.5     89.5
     80   67.83    66.50   9.38   62.0  75.0   13.0    42.5     94.5
     90   68.67    66.50  10.88   62.0  75.0   13.0    42.5     94.5
    100   69.50    66.50  12.87   62.0  75.0   13.0    42.5     94.5
    130   72.00    66.50  20.17   62.0  75.0   13.0    42.5     94.5
```

`[COMPUTED]` Between rover 80 and rover 130 the mean moves 67.83 → 72.00 and the standard
deviation 9.38 → 20.17, while the median holds at 66.50 and the interquartile range at
13.00 — both to every digit displayed. Both quartiles are also unchanged. These are the four
figures the prose quotes.

`[COMPUTED]` The upper fence is constant at 94.5 for every rover position from 84 to 130,
confirmed by checking all 47 of them. This is the article's claim that the quartile rule's
threshold "holds still" while the deviation rule's runs away.

`[COMPUTED]` The two rules first fire at different places, scanning upward from 66:

- the two-deviation rule at rover **91**, where $\bar{x} + 2s = 90.9$
- the $1.5 \times \text{IQR}$ rule at rover **95**, where the fence is 94.5

A four-unit gap, which is the number the prose quotes. The direction of the disagreement —
the deviation rule firing first here — is a consequence of the suspect value inflating $s$
faster than it moves $\bar{x}$; the article explains the mechanism rather than generalising
the direction, since the ordering is data-dependent.

`[COMPUTED]` At rover 40 the value falls below the lower fence of 45.5 and is flagged, which
is the configuration the closing note sends the reader to. The left whisker then stops at 52,
the smallest value inside the fence, rather than at 40. Verified from the shipped code's own
whisker endpoints.

## Placement

Sequence 1, ahead of the regression article that previously opened the band. Under the
ordering policy agreed on 2026-07-31, content order takes precedence over featured-card
placement, so:

- Statistics renumbered 1–13 with no gaps for the first time. The long-standing hole at
  sequence 6 is now filled by the conditional-probability article.
- *The meaning of 95% confidence* lost its `featured` flag. Inserting any article ahead of it
  moved it from display position 7 to 8, and position 8 can never carry a band's first
  featured card: mobile requires an even number of ordinary cards before a full-width one,
  which puts the first featured card at an odd position. Rather than reorder content to
  protect the card, the card yielded. This article carries the band's feature in the interim.
- Statistics featuring should be re-solved in one pass when S2, S4, and S5 land, at which
  point the band reaches 16 articles and 5 featured cards is an exact 21-cell fit.
