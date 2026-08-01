# Claims ledger — What the factored form tells you

Article: `_posts/2026-07-31-what-the-factored-form-tells-you.md`
Session: P1, 2026-07-31. AP Precalculus sequence 1, Unit 1 topics 1.5, 1.7, 1.9, 1.10.

Source: `ap-precalculus-course-and-exam-description.pdf` via `pdftotext -layout`.

Verification: the article's `roots`, `features`, and `f` functions were extracted from its
own `<script>` and run under node across all four presets at the positions the prose
quotes. The multiplicity bookkeeping is symbolic rather than numerical — the tool cancels
factors before evaluating — so a hole never produces $0/0$ and the classification never
depends on inspecting pixels.

---

## Why this article exists

AP Precalculus Unit 1 is **30–40% of the exam** and had no coverage on the site. This is the
single largest weighting gap in the corpus.

## Zeros and factors

`[EXAM]` The equivalence the article opens on, from EK 1.5.A.1: "If $a$ is a real number,
then $(x - a)$ is a linear factor of $p$ if and only if $a$ is a zero of $p$." The
biconditional is the article's premise and is quoted as one.

`[EXAM]` Multiplicity and the degree count, from EK 1.5.A.2: "If a linear factor $(x - a)$
is repeated $n$ times, the corresponding zero of the polynomial function has a multiplicity
$n$. A polynomial function of degree $n$ has exactly $n$ complex zeros when counting
multiplicities."

`[EXAM]` Tangency, quoted closely from EK 1.5.A.5: "If the real zero, $a$, of a polynomial
function has even multiplicity, then the signs of the output values are the same for input
values near $x = a$. For these polynomial functions, the graph will be tangent to the
$x$-axis at $x = a$."

`[SCOPE]` The framework states the **even** case and is silent on odd multiplicity above
one. The article's claim that a triple root "crosses lazily" is therefore presented as an
observation about the picture and about sign, not attributed to the framework. The sign
argument the article gives — that a factor changes sign exactly when its multiplicity is
odd, while every distant factor holds its sign across the crossing — is a proof rather than
a quotation, and it covers both parities from one idea.

## Asymptote or hole

`[EXAM]` Vertical asymptotes, quoted from EK 1.9.A.1: "If the value $a$ is a real zero of
the polynomial function in the denominator of a rational function and is not also a real
zero of the polynomial function in the numerator, then the graph of the rational function
has a vertical asymptote at $x = a$. Furthermore, a vertical asymptote also occurs at
$x = a$ if the multiplicity of $a$ as a real zero in the denominator is greater than its
multiplicity as a real zero in the numerator."

`[EXAM]` Holes, quoted from EK 1.10.A.1: "If the multiplicity of a real zero in the
numerator is greater than or equal to its multiplicity in the denominator, then the graph of
the rational function has a hole at the corresponding input value."

These two statements together are the article's central claim, and the emphasis is the
framework's own: **neither statement mentions cancelling.** Both compare multiplicities.
The usual classroom shortcut — a common factor cancels and leaves a hole — agrees with the
framework whenever the multiplicities happen to tie and disagrees whenever the denominator's
is larger, which is precisely the case the third and fourth presets are built to separate.

`[EXAM]` Locating a hole, from EK 1.10.A.2: "If the graph of a rational function $r$ has a
hole at $x = c$, then the location of the hole can be determined by examining the output
values corresponding to input values sufficiently close to $c$." The tool does exactly this,
evaluating the reduced form a hair to the right of the hole.

## End behaviour

`[EXAM]` From EK 1.7.A.2: "For input values of large magnitude, a polynomial is dominated by
its leading term. Therefore, the end behavior of a rational function can be understood by
examining the corresponding quotient of the leading terms."

`[EXAM]` The slant case, from EK 1.7.A.3: "If the polynomial in the numerator dominates the
polynomial in the denominator ... the quotient of the leading terms is a nonconstant
polynomial, and the original rational function has the end behavior of that polynomial. If
that polynomial is linear, then the graph of the rational function has a slant asymptote
parallel to the graph of the line."

The article's three-outcome summary is a restatement of these two, organised by which
polynomial dominates, which is the framework's own organising idea rather than the more
common "compare the degrees" phrasing.

## Computed results

Read out of the shipped classifier, which works from multiplicities rather than from the
rendered curve.

```
  preset                         a       features found
  (x−a)(x+1)(x−3)             −0.5      zeros at −1, −0.5, 3, all multiplicity 1
  (x−a)(x+1)(x−3)             −1.0      zero at −1 multiplicity 2, zero at 3
  (x−a)(x+1)²(x−3)            −0.5      zero at −1 multiplicity 2, zeros at −0.5 and 3
  (x−a)(x+1)²(x−3)            −1.0      zero at −1 multiplicity 3, zero at 3
  (x−1)(x+2)/((x−a)(x−4))      2.0      zeros at −2 and 1, asymptotes at 2 and 4
  (x−1)(x+2)/((x−a)(x−4))      1.0      zero at −2, HOLE at 1, asymptote at 4
  (x−1)(x+2)/((x−a)²(x−4))     2.0      zeros at −2 and 1, asymptotes at 2 and 4
  (x−1)(x+2)/((x−a)²(x−4))     1.0      zero at −2, ASYMPTOTE at 1, asymptote at 4
```

`[COMPUTED]` The two rational presets differ only in one exponent and diverge exactly as the
framework predicts. At $a = 1$ the third has multiplicity 1 above and 1 below, ties, and
produces a hole; the fourth has 1 above and 2 below, the denominator wins, and the asymptote
survives even though a factor of $(x-1)$ has cancelled. This is the article's argument for
preferring the comparison to the cancellation, and it is a computed result rather than an
assertion.

`[COMPUTED]` The hole in the third preset sits at $(1, -1)$. Checked independently: the
reduced function is $(x+2)/(x-4)$, which at $x = 1$ is $3/(-3) = -1$. The tool reports
$-1.0000$.

`[COMPUTED]` The first preset's merge is a genuine change of multiplicity, not an
appearance: at $a = -0.5$ the classifier reports three simple zeros, and at $a = -1$ it
reports a single zero of multiplicity 2. The second preset makes the same move from
multiplicity 2 to multiplicity 3.

## Placement

Sequence 1, ahead of the transformations article. Transformations is topic 1.12 and this is
topics 1.5 through 1.10, so under the ordering policy agreed on 2026-07-31 content order
decides and the whole band shifts by one.

The featured card followed the rule rather than the content. With five articles in the band,
featuring the unit-circle article alone at display position 5 is an **exact** fit at both
breakpoints — two full rows on desktop, three on mobile, no holes and no trailing cells. So
the transformations feature, which had only ever been added to close a gap, came off, and
the unit-circle feature that Katherine originally set is restored as the band's sole card.
This is the first band placement where the arithmetic and the original editorial choice
agreed without compromise.
