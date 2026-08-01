# Claims ledger — One template for every interval

Article: `_posts/2026-07-31-one-template.md`
Session: S5, 2026-07-31. AP Statistics sequence 12, spanning Units 3 and 4.

Source: the **formula sheet in the revised CED's own appendix**, section III, extracted with
`pdftotext -layout` and read line by line. This is the sheet students will be handed; the
copy in the materials folder is the pre-revision one, recorded separately in the audit
report.

Verification: the article's `T` table was extracted from its `<script>` and every standard
error compared against the sheet. Structural claims about the sheet were checked by regular
expression against the extracted section III rather than from memory.

---

## The claim the article is built on

`[EXAM]` Section III of the revised formula sheet prints exactly three things before its
tables, and they are quoted verbatim in the article:

- "Standardized test statistic: $\dfrac{\text{statistic} - \text{parameter}}{\text{standard error of the statistic}}$"
- "Confidence interval: $\text{statistic} \pm (\text{critical value})(\text{standard error of the statistic})$"
- "Chi-square statistic: $\chi^2 = \sum \dfrac{(\text{Observed Count} - \text{Expected Count})^2}{\text{Expected Count}}$"

All three confirmed present by search. **No procedure-specific interval or test formula
appears anywhere on the sheet.** There is no one-proportion interval formula, no two-sample
$t$ formula, nothing of that kind. The article's thesis is a description of the sheet's
layout rather than an interpretation of it.

`[EXAM]` What follows is two tables headed *Sampling Distributions for Proportions* and
*Sampling Distributions for Means*, each with rows for one population and two populations,
and each with three columns: **Mean**, **Standard Deviation**, **Standard Error**.

## The three-column structure, which is the article's second point

`[EXAM]` The Standard Deviation column is built from the *parameter* and the Standard Error
column from the *statistic*. Confirmed on both tables:

- proportions: $\sigma_{\hat p} = \sqrt{p(1-p)/n}$ against $SE_{\hat p} = \sqrt{\hat p(1-\hat p)/n}$
- means: $\sigma_{\bar x} = \sigma/\sqrt{n}$ against $SE_{\bar x} = s/\sqrt{n}$

This is the sheet's own encoding of the interval-versus-test distinction, and it produces
the article's answer to why proportions take $z$ and means take $t$. A null hypothesis
supplies a value for $p$, which determines a proportion's spread completely, so a test can
use the Standard Deviation column exactly. Nothing ever supplies $\sigma$, so a mean must
use the Standard Error column in both purposes, and the extra uncertainty in substituting
$s$ for $\sigma$ is what $t$ accounts for.

`[EXAM]` The pooled standard error, from the same table: "When $p_1 = p_2$ is assumed:
$SE_{\hat p_1 - \hat p_2} = \sqrt{\hat p_c(1 - \hat p_c)\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}$,
where $\hat p_c = \frac{n_1 \hat p_1 + n_2 \hat p_2}{n_1 + n_2}$." Confirmed present. The
conditional phrasing is the point: the pooled form is available only because the null
asserts equality, which is why the two-proportion interval does not use it.

`[EXAM]` The two-population means row gives
$SE_{\bar x_1 - \bar x_2} = \sqrt{s_1^2/n_1 + s_2^2/n_2}$ — variances under the root,
which is where the article's remark that standard deviations never add is sourced.

## Computed results

The article's table of standard errors, checked entry by entry against the sheet:

```
  family              interval standard error            test standard error              same?
  one proportion      sqrt( p̂(1−p̂)/n )                  sqrt( p₀(1−p₀)/n )               DIFFERS
  two proportions     sqrt( p̂₁(1−p̂₁)/n₁ + p̂₂(1−p̂₂)/n₂ ) sqrt( p̂_c(1−p̂_c)(1/n₁+1/n₂) )   DIFFERS
  one mean            s/sqrt(n)                          s/sqrt(n)                        same
  paired difference   s_d/sqrt(n)                        s_d/sqrt(n)                      same
  two means           sqrt( s₁²/n₁ + s₂²/n₂ )            sqrt( s₁²/n₁ + s₂²/n₂ )          same
  chi-square          no interval exists                 sum over cells                   n/a
```

`[COMPUTED]` The two purposes differ in the standard error for exactly the two proportion
families and for neither mean family. That asymmetry is the article's third section and it
is a result of the check rather than an assumption going in.

`[SCOPE]` The paired row is the one-mean row with $n$ counting pairs, following EK 4.2.B.2
as sourced in the `which-inference-procedure` ledger. The tool lists it separately because
students look for it separately, and the note says explicitly that it is not a seventh
formula.

`[SCOPE]` Degrees of freedom for the two-sample $t$ are described as supplied by technology
rather than given a formula, which is how the course treats them. The sheet prints no
degrees-of-freedom formula for that case.

`[SCOPE]` The article does not claim the sheet is the only thing a student needs. Conditions,
parameter definitions, and conclusions are all unsourced by the sheet and are covered in
other articles, two of which it links to by way of the surrounding sequence rather than
inline.

## A note on extraction

Two regular-expression checks initially reported the one-proportion standard error and the
pooled estimate as absent. Both were false negatives: `pdftotext` drops the hat diacritic,
so $SE_{\hat p}$ extracts as `SEp`, and the pooled estimate's subscripts are lost entirely.
Confirmed by reading the surrounding lines directly. The column headers and the distinct
entries under each are present, which is what the article's claim rests on.

## Placement

Sequence 12, after *Writing parameters* and before *What a p-value cannot tell you*. The
order it sits in now reads: what a confidence interval means, the distribution tool, define
the parameter, assemble the formula, what a p-value is, the two errors, which chi-square
test, which procedure.

**This completes the Statistics batch.** The band holds 16 articles numbered 1–16 with no
gaps, in course order through Unit 4. With one featured card that is 17 cells and no
mid-grid holes at either breakpoint; the featured set should now be re-solved in one pass,
and the arithmetic for doing so is in the audit report.
