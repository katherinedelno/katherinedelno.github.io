# Claims ledger — L'Hospital's rule, and the step before it

Article: `_posts/2026-07-30-lhospitals-rule.md`
Session: 7D article 14 (tier 4), 2026-07-30. AP Calculus sequence 16, Unit 4 topic 4.7.

Verification: `t.js` and `t2.js` load the shipped script in jsdom with a stubbed canvas context,
click each of the five limit buttons, and sweep all 1201 slider positions for each — 6005
evaluations — comparing both ratios against independently written formulas and reading every
panel row and note out of the live DOM. Limits confirmed symbolically in SymPy.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **The spelling.** The framework writes "L'Hospital's Rule" throughout, without a
circumflex. The article follows it and says so in the second paragraph. Your sequence proposal
used "L'Hôpital"; nothing else in the corpus mentions the name, so there is no inconsistency to
repair, but the file is named `lhospitals-rule` to match the framework.

`[EXAM]` **Enduring understanding LIM-4**: "L'Hospital's Rule allows us to determine the limits
of **some** indeterminate forms." The article italicises "some" and builds its fourth section on
it, the same way the linearization article was built on CHA-3.F.2's "may".

`[EXAM]` **LIM-4.A.1**: "When the ratio of two functions tends to $\tfrac00$ or
$\tfrac{\infty}{\infty}$ in the limit, such forms are said to be indeterminate." With an
**exclusion statement**: "There are many other indeterminate forms... but these will not be
assessed on either the AP Calculus AB or BC Exam." That is the source for the article's claim
that these are the only two forms the exam assesses.

`[EXAM]` **LIM-4.A.2**: "Limits of the indeterminate forms $\tfrac00$ or $\tfrac{\infty}{\infty}$
may be evaluated using L'Hospital's Rule."

`[EXAM]` **Topic 4.7's suggested skill is 3.D**, "Apply an appropriate mathematical definition,
theorem, or test" — quoted in the last section, and the reason that section is about what to
write rather than what to compute.

`[EXAM]` **Unit 4's exam guidance supplies three of the article's warnings, closely paraphrased:**
"students must verify that $\lim f(x) = \lim g(x) = 0$ (or that both approach infinity) as a
necessary first step"; "$\tfrac00$ or $\tfrac{\infty}{\infty}$ are appropriate labels for
indeterminate forms but do not represent values in an equation. Therefore, it is incorrect to
write $\lim \tfrac{f(x)}{g(x)} = \tfrac00$"; and "the conclusion of L'Hospital's rule features
the ratio of the derivatives of the numerator and denominator, respectively, rather than the
derivative of the ratio." It also notes that $\lim\tfrac{f}{g} \neq \tfrac{\lim f}{\lim g}$ when
$\lim g = 0$, which is the article's third notational point.

`[EXAM]` **The resource list, counted rather than characterised.** Topic 4.7 lists five
resources: two AP Online Teacher Community discussions, one titled "L'Hospital's Rule" and one
titled "Possible Inconsistent Language"; and three documents all for 2018 free-response question
5(d) — the Chief Reader Report, the Samples and Commentary, and the Scoring Guidelines. The
article states the count and the titles. It does **not** state what any of those documents say,
because I have not read them.

`[STANDARD]` The rule's three hypotheses as stated — differentiability near $a$ with $g' \neq 0$,
the indeterminate form, and the existence of $\lim f'/g'$ — are the standard statement. The CED
gives the form condition and the exam guidance gives the verification step; the differentiability
and $g' \neq 0$ conditions are standard analysis.

## Computed results

`[COMPUTED]` **All five limits, symbolically in SymPy.**

```
  sin x / x          x → 0    = 1
  (1 − cos x)/x²     x → 0    = 1/2      via sin x/(2x) → 1/2 and cos x/2 → 1/2
  x² / eˣ            x → ∞    = 0
  (x + 1)/(x² + 1)   x → 0    = 1        while 1/(2x) → +∞ from the right
  (x + sin x)/x      x → ∞    = 1        while 1 + cos x has no limit
```

For the last, SymPy returns `AccumBounds(0, 2)` for $\lim(1+\cos x)$ — the accumulation bounds,
which is its way of reporting that the limit does not exist and the values oscillate over
$[0,2]$. Exactly the article's claim.

`[COMPUTED]` **The panel matches independently written formulas at all 6005 positions.** Largest
relative discrepancies, computed by recomputing both ratios from the displayed $x$: below
$10^{-4}$ on all five, with the single worst at $5\times10^{-4}$ on $(x+\sin x)/x$, which is
display rounding rather than disagreement.

`[COMPUTED]` **What the panel prints at the closest approach**, read from the running tool:

```
  sin x / x        x = 0.0010000   f/g = 1.0000      f′/g′ = 1.0000
  (1−cos x)/x²     x = 0.0010000   f/g = 0.50000     f′/g′ = 0.50000
  x²/eˣ            x = 30.000      f/g = 8.42e-11    f′/g′ = 5.61e-12
  (x+1)/(x²+1)     x = 0.0010000   f/g = 1.0010      f′/g′ = 500.00
  (x+sin x)/x      x = 40.000      f/g = 1.0186      f′/g′ = 0.33306
```

The fourth row is the article's central demonstration: the function ratio is within a thousandth
of 1 while the derivative ratio has reached 500 and is climbing.

`[COMPUTED]` **The fifth limit's oscillation, measured.** Sweeping the slider, $f'/g' = 1+\cos x$
takes values across the full range $[0.0000, 2.0000]$, while over the near half of the sweep
$f/g$ stays inside $[0.9087, 1.1284]$. One quantity is settling and the other is not, which is
the whole point.

`[COMPUTED]` **The slider direction.** For all five entries, slider 1200 is the closest approach
to the target — decreasing $x$ for the three $x\to 0$ limits and increasing it for the two
$x\to\infty$ limits. Verified by comparing the endpoints on every entry.

## Judgment claims

`[JUDGMENT]` "Easy to apply and easy to apply where it does not belong, and those are not
separate facts about it." An editorial framing of why the verification step gets skipped.

`[JUDGMENT]` "Three documents and a warning about wording, for one part of one problem." The
count and titles are verified; the inference that this signals where marks are lost is mine, and
the sentence is written as an observation about the resource list rather than as a claim about
its contents.

`[JUDGMENT]` The closing note's advice to try algebra before the rule. Defensible on its own
terms and consistent with the indeterminate forms article it links to.

---

## Flags raised in this session

1. **The slider ran backwards on every one of the five limits.** My `xat` function had a single
   `rev` branch that made slider 0 the closest approach in all cases, while the control is
   labelled "x, moving toward the target" and the default sat at the far end. So sliding right —
   the natural reading — moved *away* from the limit everywhere. The mapping now decreases the
   exponent for $x\to 0$ and increases it for $x\to\infty$, so right is always toward the target.
   Caught by a test I added on a hunch about the comment I had written, which itself described
   the wrong behaviour.

2. **The panel's $x$ was too coarse to check the panel's own $f'/g'$.** With four decimal places,
   $x = 0.001$ printed as `0.0010` — two significant figures — from which $1/(2x)$ cannot be
   recovered to better than a few percent. Every quantity in this tool ranges over decades, so
   the formatter now uses five significant figures throughout. This is the second consecutive
   article where a display format, rather than a value, was the defect; both times the harness
   found it because the harness reads what a reader would read.

3. **Two claims cut for being unverifiable.** I had written that L'Hospital's rule is "the
   shortest theorem in the course to state", which I cannot defend against the power rule, and
   that the chief reader report shows the recurring loss is the missing justification line — a
   claim about the contents of a document I have not read. The first is gone; the second is
   replaced by the count of resources, which is verifiable from the CED page.

4. **The verdict messaging was derived and therefore wrong on the fifth case.** A single
   `applies` boolean made the form-check row say "the rule applies" for $(x+\sin x)/x$, where the
   *form* condition holds but the rule still concludes nothing. Each entry now carries its own
   form note and limit note, so the panel distinguishes "the form condition holds" from "the rule
   applies" — a distinction the article is entirely about.

5. **838 words**, four `##` headings, two italicised spans (both the framework's "some"), three
   cross-links, all resolving. Inside the 650–950 target.

6. **Unit 4 is complete except for related rates**, which you already have from 20 July at
   sequence 14. Topics 4.1, 4.2, 4.6, and 4.7 are now covered; 4.3 (rates of change in contexts
   other than motion) and 4.4–4.5 (related rates) are the remainder, and only 4.3 has no article.
   It is not in the approved plan. Worth a decision before Unit 5 begins at sequence 17.
