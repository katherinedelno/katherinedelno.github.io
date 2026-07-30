# Claims ledger — Limits at infinity and end behavior

Article: `_posts/2026-07-30-limits-at-infinity.md`
Session: 7D article 3 (tier 1), 2026-07-30. AP Calculus sequence 5, Unit 1.

Verification: `t.js` drives the shipped script in jsdom across every degree combination and
zoom level, reading the limit and the edge value back out of the readout. All assertions
pass.

---

## Framework grounding

`[EXAM]` Infinite limits, from LIM-2.D.1 and LIM-2.D.2 (topic 1.14, Connecting Infinite
Limits and Vertical Asymptotes): "The concept of a limit can be extended to include infinite
limits" and "Asymptotic and unbounded behavior of functions can be described and explained
using limits."

`[EXAM]` Limits at infinity, from LIM-2.D.3 and LIM-2.D.4 (topic 1.15, Connecting Limits at
Infinity and Horizontal Asymptotes): "The concept of a limit can be extended to include
limits at infinity" and, quoted almost verbatim in the article, "Limits at infinity describe
end behavior."

`[EXAM]` Relative magnitudes, from LIM-2.D.5: "Relative magnitudes of functions and their
rates of change can be compared using limits." This is the listed skill the article's final
section serves, and it is why that section exists at all.

`[EXAM]` The two are separate topics — 1.14 and 1.15 — under the same learning objective
LIM-2.D. The article's opening claim that the framework "keeps them as separate topics" is
literally true and is the reason for the article's framing.

## Computed results

`[COMPUTED]` The three cases, read out of the shipped tool:

```
  numerator deg 1, denominator deg 2            limit 0
  numerator deg 1, denominator deg 1, a=3 b=2   limit 1.5
  numerator deg 3, denominator deg 1, a=3 b=2   limit +infinity
  numerator deg 3, denominator deg 1, a=-3 b=2  limit -infinity
  numerator deg 2, denominator deg 2, a=3 b=-6  limit -0.5   (the closing note)
```

`[COMPUTED]` The worked quotients:

```
  (3x+2)/(2x+5)        at x = 1e2, 1e4, 1e6:  1.473171, 1.499725, 1.499997   -> 3/2
  (3x+2)/(2x^2+5x)     at x = 1e2, 1e4, 1e6:  0.014732, 0.000150, 0.000001   -> 0
  (3x^2+2x)/(2x+5)     at x = 1e2, 1e4, 1e6:  147.3, 14997.3, 1499997.3      -> unbounded
```

`[COMPUTED]` With equal degrees, $a = 3$, $b = 2$, the approach is from below. At
$x = 10^4$ the tool reports 1.499725 against a limit of 1.5. Algebraically
$f - \tfrac{a}{b} = x^{p-1}(2b - 5a)/(b \cdot \text{den})$, and $2(2) - 5(3) = -11 < 0$, so
this holds for every equal-degree setting with these coefficients, not just the one shown.

`[COMPUTED]` **The growth-rate passage, which a draft got wrong.** I wrote that
$x^{100}/e^x$ "does not begin its collapse until $x$ is past a few hundred." It begins at
exactly $x = 100$: differentiating $100\ln x - x$ gives $100/x - 1$, zero at $x = 100$. The
corrected prose states the peak, its height, and the crossing:

```
  x =   50   ratio 1.52e+148
  x =  100   ratio 3.72e+156     <- maximum, exactly at the exponent
  x =  200   ratio 1.75e+143
  x =  400   ratio 3.08e+86
  x =  600   ratio 1.73e+17
  x =  800   ratio 7.47e-58
  ratio falls below 1 at x = 647.3   (bisection on 100 ln x - x)
```

`[STANDARD]` $\lim_{x\to\infty} \ln x / x = 0$; $\lim_{x\to\infty} x^{100}/e^x = 0$;
$\lim_{x\to\infty} e^x/x^{100} = \infty$. The middle one follows from
$\ln(x^{100}/e^x) = 100\ln x - x \to -\infty$.

`[STANDARD]` The general fact behind the corrected passage: $x^n/e^x$ peaks at $x = n$ for
every positive $n$, by the same derivative. Stated in the article only for $n = 100$.

`[STANDARD]` Dividing numerator and denominator by the highest power in the denominator, then
sending each $1/x^k$ to zero, produces all three cases. Worked in the article for the
equal-degree example.

## Judgment claims

`[JUDGMENT]` Reading the degrees off is the right move under multiple-choice time pressure,
and the division is what to write when justification is asked for. A teaching preference,
though it is consistent with the framework pairing topic 1.15 with skill 2.D (connecting
representations) rather than with a computation skill.

`[JUDGMENT]` "A graphing window will tell you the opposite of the truth over that whole
stretch." Supported by the computed table above: the ratio really is increasing on any
window ending before $x = 100$, and still above 1 out to 647.

---

## Flags raised in this session

1. **A wrong claim about where $x^{100}/e^x$ turns over**, caught by computing it rather
   than by reasoning about it. The corrected version is better material than the original —
   the maximum sits exactly at the exponent, which is memorable and checkable — but the
   draft would have shipped a false statement about "a few hundred". This is the second time
   in 7D that a numerical claim I was confident about was wrong.

2. **The article is short: 667 words**, against a corpus median of 730 and a minimum of 539.
   It is a single-idea mechanics piece and I would rather it stayed tight than padded, but
   if you want it fuller, the natural addition is a worked non-rational example — something
   like $\lim (\sqrt{x^2+3x} - x)$, which needs conjugate multiplication and is a standard
   exam trap that the current article does not touch.

3. **Slant asymptotes are absent.** When the numerator's degree exceeds the denominator's by
   exactly one, there is an oblique asymptote. The framework's essential knowledge for topic
   1.15 does not mention it, so I left it out, and the interactive reports only "no
   horizontal asymptote" in that case, which is true but incomplete if your students have
   met slant asymptotes in precalculus.

4. **The interactive forbids a zero leading coefficient.** Sliding $a$ or $b$ to 0 would
   silently change the degree and make the labels lie, so the code substitutes 1. That is
   defensible but invisible to the reader, who may wonder why 0 behaves like 1.
