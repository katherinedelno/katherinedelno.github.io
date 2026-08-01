# Claims ledger — Which inference procedure?

Article: `_posts/2026-07-31-which-inference-procedure.md`
Session: S2, 2026-07-31. AP Statistics sequence 14, spanning Units 3 and 4.

Source: `ap-statistics-course-and-exam-description-effective-fall-2026.pdf` via
`pdftotext -layout`.

Verification: the twelve scenarios were extracted from the article's own `Q` array and
their answer keys tabulated. All six families appear exactly twice; the purpose split is
five intervals to seven tests. The scoring path was smoke-tested under node.

---

## The inventory

`[EXAM]` The claim that twelve procedures survive was built by walking the revised unit
guides rather than assumed. Unit 3 supplies topics 3.3 (one-proportion interval), 3.5 and
3.7 (one-proportion test), 3.10 (two-proportion interval), 3.12 and 3.13 (two-proportion
test), 3.14 and 3.15 (chi-square for homogeneity or independence). Unit 4 supplies 4.2
(interval for a mean *or a mean difference*), 4.4 and 4.5 (test for the same), 4.7
(interval for a difference of two means), 4.9 and 4.10 (test for the same).

`[EXAM]` **Unit 5, Regression Analysis, contains no inference.** Its five topics run from
graphical representations through least-squares regression and stop. Inference for a
regression slope was removed in the revision, so no scenario in the drill involves it and
the article's count of six families is complete.

`[EXAM]` Chi-square appears only as a test. There is no chi-square interval in the course,
which is why two of the twelve scenarios are chi-square and both are tests.

`[EXAM]` The selection skill, 2.C, "Identify appropriate statistical inference methods", is
attached to eleven separate topics across Units 3 and 4 — every "constructing", "setting
up", and "identify an appropriate procedure" topic. That density is the article's
justification for treating selection as a topic in its own right.

## Paired versus two-sample

`[EXAM]` Quoted from EK 4.2.B.2: "For a matched pairs design with two dependent samples,
the appropriate analysis calculates differences between pairs of values to produce one
sample of differences. The confidence interval procedure for the matched pairs design is a
one-sample $t$-interval for a population mean difference."

This is the article's central classification claim and it is a quotation, not an inference.
A paired design is not a seventh family; it is converted to a one-sample problem before any
formula appears, and the parameter changes from $\mu_1 - \mu_2$ to $\mu_d$ with it.

`[EXAM]` The design itself, from EK 1.13.B.4: "A matched pairs design is a randomized block
design with only two treatments. Experimental units are arranged in pairs by matching on one
or more extraneous sources of variation ... Alternatively, each experimental unit may get
both treatments while the order of the treatments is randomized."

Both halves of that definition are represented in the drill: scenario three is the same
individuals measured twice, scenario eight is the same components measured by two
instruments. Neither is two samples.

## Independence versus homogeneity

`[EXAM]` The design distinction and the differently worded randomisation conditions are
sourced in the ledger for `which-chi-square-test` and are cited here rather than repeated.
The relevant point for this article is EK 3.14.D.1.i, where the randomisation condition is
stated separately for the two tests — a procedure whose arithmetic is identical and whose
conditions differ is a procedure that is really two, which is the article's phrasing.

## Scenario design

`[COMPUTED]` The twelve scenarios and their keys:

```
   1  p1  interval   one sample, categorical, plausible values requested
   2  p2  test       two randomly assigned groups, categorical
   3  md  test       same forty runners, before and after
   4  m2  test       two separate groups of employees, quantitative
   5  chi test       one sample cross-classified: independence
   6  chi test       three separate samples, one variable: homogeneity
   7  m1  interval   one sample, quantitative, 500 mL is context not a claim
   8  md  test       same twenty-five components, two gauges
   9  p1  interval   counts supplied, still one proportion
  10  p2  interval   two samples, categorical, size of a difference
  11  m1  test       one sample, quantitative, 600 is a hypothesised value
  12  m2  interval   two samples, quantitative, size of a difference
```

All six families appear exactly twice. Four scenarios are built as confusable pairs:

- **3 and 4** are the paired-versus-two-sample trap, with equal group sizes in the
  two-sample case so that matching counts cannot be mistaken for matching individuals.
- **5 and 6** are independence versus homogeneity, which produce identical tables.
- **7 and 11** are the interval-versus-test trap: both are one-sample means, both mention a
  specific number, and only in 11 is that number a claim to be judged.
- **10 and 12** ask the same question — how large is the difference — of a categorical and a
  quantitative response, so the family changes while the purpose does not.

`[SCOPE]` No scenario supplies any data. This is deliberate: every claim the feedback makes
is about the design, so none of it can be checked or short-circuited by arithmetic. A
student who reaches the right answer from numbers has not practised the skill the topic
assesses.

`[SCOPE]` A reader can select Chi-square together with Confidence interval, which is never
a correct pairing in this course. The tool marks it wrong and the feedback names the correct
answer, but it does not explain that chi-square has no interval. That is a deliberate
omission rather than an oversight — the article says elsewhere that chi-square appears only
as a test, and cluttering the feedback with the general rule would dilute the
design-feature-only discipline the drill is built on.

## Placement

Sequence 14, at the end of the Statistics band, because the article presumes every procedure
it sorts. `which-chi-square-test` sits at 13 immediately before it, which is the right
neighbour: the narrow decision, then the wide one.

Statistics now holds 14 articles and one featured card, which is 15 grid cells — an exact
three-column fit on desktop with one trailing cell on mobile. No mid-grid holes at either
breakpoint.
