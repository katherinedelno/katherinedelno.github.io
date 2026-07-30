# Claims ledger — A distribution explorer

Article: `_posts/2026-07-30-distribution-explorer.md`
Session: 7B, 2026-07-30

Verification performed in this session:

- `dist.js` / `test-dist.js` — the distribution mathematics as shipped, 66 assertions under
  node against published table values and against closed forms.
- `jsdom-test.js` — the article's own `<script>` loaded into a real DOM (jsdom), driven
  through every distribution, both directions, all region modes, and presentation mode, with
  every readout compared against the independently tested `dist.js`.

---

## The mathematics

Every function is implemented directly, with no libraries, as the brief requires. Accuracy
against published values, all far inside the 1e-8 target:

| function | published values checked | worst absolute error | target |
|---|---|---|---|
| `normcdf` | 9 | 2.22e-16 | 1e-8 met |
| `norminv` | 8 | 9.33e-15 | 1e-8 met |
| `tcdf` | 6 | 2.22e-16 | 1e-8 met |
| `tinv` | 11 | 2.31e-12 | 1e-8 met |
| `chi2cdf` | 5 | 3.33e-16 | 1e-8 met |
| `chi2inv` | 10 | 1.42e-14 | 1e-8 met |
| `binompdf` | 6 | 5.72e-15 | vs integer coefficients |
| `binomcdf` | 6 | 8.00e-15 | vs integer coefficients |

`[COMPUTED]` Methods, as specified: normal cdf by the Hart 1968 rational approximation;
inverse normal by Acklam's rational approximation refined with two Newton steps against the
cdf; Student t by the regularized incomplete beta (Lentz continued fraction); chi-square by
the regularized lower incomplete gamma (series below the crossover, continued fraction
above); binomial exactly, with log-gamma coefficients so large `n` does not overflow.

`[COMPUTED]` Cross-family identities, all holding to 1e-13 or better: `chi2cdf(x,1)` equals
`2·Φ(√x) − 1`; `chi2cdf(x,2)` equals `1 − e^{−x/2}`; `tcdf` at df = 10⁷ agrees with the
standard normal to 1.4e-8; `tinv` and `chi2inv` invert their cdfs to 2e-16 and 6e-17.

### Two published reference values I had wrong

Both apparent test failures turned out to be errors in my reference values, not in the code.
Recording them because they are the reason to check against closed forms rather than
transcribed tables.

`[COMPUTED]` **t(0.975, df = 2).** For df = 2 the cdf has the closed form
$F(t) = \tfrac12 + t/(2\sqrt{2+t^2})$, so the exact quantile is $\sqrt{1.805/0.0975}$.
Computed in 50-digit decimal arithmetic: **4.30265272974946385**. The shipped `tinv` returns
4.302652729749465, off by 1.15e-15. The value I had transcribed, 4.302652729911275, is off
by 1.62e-10 and yields a cdf of 0.9750000000017 rather than 0.975.

`[COMPUTED]` **χ²(0.975, df = 1).** For df = 1 the quantile is $[\Phi^{-1}((1+p)/2)]^2$
exactly, giving **5.023886187314900**. The shipped `chi2inv` returns 5.023886187314891, off
by 8.88e-15; my transcribed 5.023886187150766 was off by 1.64e-10.

## The calculator line

`[EXAM]` Every command string and menu position below is verified against Texas Instruments'
own *Reference Guide for the TI-84 Plus CE*, Commands and Functions Listing. None was
written from memory.

| command | documented syntax | DISTR position |
|---|---|---|
| `normalpdf(` | `normalpdf(x[,μ,σ])` | 1 |
| `normalcdf(` | `normalcdf(lowerbound,upperbound[,μ,σ])` | 2 |
| `invNorm(` | `invNorm(area[,μ,σ,tail])`, tail ∈ LEFT, CENTER, RIGHT | 3 |
| `invT(` | `invT(area,df)` | 4 |
| `tpdf(` | `tpdf(x,df)` | 5 |
| `tcdf(` | `tcdf(lowerbound,upperbound,df)` | 6 |
| `χ²pdf(` | `χ²pdf(x,df)` | 7 |
| `χ²cdf(` | `χ²cdf(lowerbound,upperbound,df)` | 8 |
| `binompdf(` | `binompdf(numtrials,p[,x])` | A |
| `binomcdf(` | `binomcdf(numtrials,p[,x])` | B |

`[EXAM]` The guide's own worked example for `binomcdf(30,0.5,19)` gives approximately
0.9506314271. The shipped `binomcdf` returns 0.950631426647, agreeing to 4.5e-10 — the
guide's figure is rounded to ten places.

`[EXAM]` The TI-84 has **no inverse χ² command**. Verified by absence: the Reference Guide's
Commands and Functions Listing contains `χ²pdf(`, `χ²cdf(`, and `χ²Test(`, and no inverse.
The tool says so rather than inventing one, and offers the forward command instead.

**Not verified, and therefore stated loosely in the tool:** the exact keystroke that opens
the DISTR menu. Every distribution entry in the guide is preceded by a key glyph that the
PDF text layer renders as `y=`, which is not readable as a key pair. The tool says
"2nd DISTR", which is how TI names the menu and how the numbered positions are reached; it
does not claim which key DISTR sits above.

## Claims in the prose

`[STANDARD]` Forward commands take a region and return a probability; inverse commands take
a probability and return a boundary. This is the `normalcdf` / `invNorm` distinction, and
topic 3.6 (p-Values) and the Unit 3 confidence-interval topics both use it.

`[STANDARD]` `binompdf` gives $P(X = k)$; `binomcdf` gives $P(X \leq k)$. Documented syntax
above; the tool shows both simultaneously for the current $k$.

`[COMPUTED]` "At least 6" is $P(X \geq 6) = 1 - P(X \leq 5)$, written `1 - binomcdf(n,p,5)`.
Confirmed in the DOM: selecting "Right of a" with a = 6, n = 20, p = 0.3 produces exactly
the string `1 − binomcdf(20,0.3,5)` and the value 0.5836.

`[STANDARD]` For a sample proportion the normal curve approximates a binomial, and the
large-counts condition is $np \geq 10$ and $n(1-p) \geq 10$.

`[STANDARD]` For a sample mean the normal curve is exact if the population is normal, and
otherwise rests on the Central Limit Theorem with the course's $n \geq 30$ guideline. This
matches what the existing CLT article already states.

`[COMPUTED]` The closing note's three numbers, read out of the running tool:

```
  normal(0,1), between -1.96 and 1.96      0.9500
  t df=10,     between -1.96 and 1.96      0.9216
  t df=300,    between -1.96 and 1.96      0.9491
```

A draft said 0.9224 for df = 10. The DOM test caught it; the correct value is 0.9216.

## Judgment claims

`[JUDGMENT]` Students conflate the forward and inverse directions. The brief asserts it and
it matches the common `normalcdf`/`invNorm` confusion; no source is cited in the prose.

`[JUDGMENT]` `binompdf` and `binomcdf` are the pair most often swapped. Stated in the
caption. Same status: asserted from the brief, not from a source.

---

## Flags raised in this session

1. **A measurement bug in my own tooling, which affected the previous article too.** The
   script that measures article length removed the `viz` block with a non-greedy
   `.*?</div>`. That block contains nested `viz-controls` divs, so the match stopped at the
   first inner close and every button label counted as prose. Corrected by matching `<div>`
   depth. The corpus median falls from a reported 802 to a true **714**, the maximum from
   1202 to **1128**. The style sheet and the p-value ledger are both corrected. The p-value
   article is 952 words, not the 1060 I reported to you.

2. **This page is the shortest on the site at 567 words** (391 of prose). The previous
   minimum was 539. That seems right for a reference tool whose substance is the tool, but
   it is worth your eye — if you want it to read more like an article, the natural addition
   is a worked example carried through all three of its representations.

3. **Presentation mode breaks out of the article column** using `width:100vw` with a
   negative margin. It is the only place on the site that does this. It works within the
   restraint rules (no shadow, no gradient, palette unchanged) but it is a layout device
   nothing else uses, so you may want to see it on a projector before keeping it.

4. **The chi-square inverse is absent by design.** Because the TI-84 has no inverse χ²
   command, choosing "Probability → cutoff" with χ² selected shows a message rather than a
   number, even though the tool can compute the value. I chose to match the calculator
   rather than exceed it, on the grounds that this is a tool for a course whose students sit
   the exam with that calculator. Reversible if you would rather it show the value.

5. **Keyboard control is partial.** Every parameter, bound, and mode is reachable and
   operable by keyboard, because they are native `input` and `button` elements. Dragging a
   bound on the plot is mouse and touch only; the typed bound box is the keyboard
   equivalent, which satisfies "every plotted number also present as text" but is not the
   same as keyboard dragging.
