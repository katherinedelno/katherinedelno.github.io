# Claims ledger — Integration by parts, partial fractions, and the check that catches both

Article: `_posts/2026-07-30-parts-and-partial-fractions.md`
Session: 7D article 18, 2026-07-30. AP Calculus **BC only**, sequence 23, Unit 6 topics 6.11 and
6.12, with the selection skill from 6.14.

Verification: `t.js` loads the shipped script in jsdom with a stubbed canvas context, clicks each
of the five entries, and sweeps all 1201 slider positions for each — 6005 evaluations — comparing
the integrand, the claimed antiderivative, and the measured gap against independently written
formulas. Symbolic results from SymPy.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **FUN-6.E.1** (topic 6.11, marked bc only): "Integration by parts is a technique for
finding antiderivatives." That is the entire essential knowledge for the topic, which is why the
article's remark that the framework "says only" this is accurate rather than dismissive.

`[EXAM]` **FUN-6.F.1** (topic 6.12, marked bc only): "*Some* rational functions can be decomposed
into sums of ratios of *linear, nonrepeating* factors to which basic integration techniques can
be applied." Both italicised phrases are quoted from the framework, and the article's third
section is entirely about the restriction they impose. Topic title: "Integrating Using Linear
Partial Fractions".

`[EXAM]` **Both topics carry suggested skill 1.E**, "Apply appropriate mathematical rules or
procedures, with and without technology". Learning objectives FUN-6.E and FUN-6.F are each
phrased in two parts: determine indefinite integrals, evaluate definite integrals — which is why
the article treats the definite case separately at the end.

`[EXAM]` **Topic 6.14, "Selecting Techniques for Antidifferentiation", carries skill 1.C** —
"Identify an appropriate mathematical rule or procedure based on the classification of a given
expression." Quoted in the closing note. This is the third distinct topic in the framework built
on the identify-versus-apply distinction, after 2.10 (skill 1.D) and 3.1 (skill 1.C).

`[EXAM]` Enduring understanding **FUN-6**: "Recognizing opportunities to apply knowledge of
geometry and mathematical rules can simplify integration."

`[STANDARD]` The derivation of the parts formula from the product rule, and the statement that
repeated factors and irreducible quadratics need different forms, are standard and explicitly
outside this course's scope.

## Computed results

`[COMPUTED]` **All four correct antiderivatives verified symbolically**, `simplify(diff(F) - f)`
returning 0 in each case:

```
  ∫ x eˣ dx        F = (x − 1)eˣ
  ∫ x sin x dx     F = sin x − x cos x
  ∫ ln x dx        F = x ln x − x
  ∫ dx/(x² − 1)    F = ½ln(x−1) − ½ln(x+1)
```

`[COMPUTED]` **The fifth entry is wrong by exactly $-2\cos x$.** SymPy: the claimed
$-\sin x - x\cos x$ differentiates to $x\sin x - 2\cos x$. So the panel's gap should read
$2|\cos x|$, and over all 1201 slider positions it does, with zero disagreements. The largest
gap is exactly 2.000000 at $x = 0$, where $\cos x = 1$.

`[COMPUTED]` **The four correct entries hold up everywhere.** Worst $|F' - f|$ across all slider
positions: $6.3\times10^{-10}$, $2.9\times10^{-10}$, $6.7\times10^{-9}$, $5.0\times10^{-9}$ —
all of that being the symmetric difference's own truncation error, not disagreement.

`[COMPUTED]` **The by-parts comparison.** With $u = x$ the remaining integral is $\int e^x dx$,
integrand of degree 0. With $u = e^x$ it is $\int \tfrac{x^2}{2}e^x dx$, degree 2. The article's
claim that the degree "went from one to two" is the polynomial factor's degree in the remaining
integrand, and it is computed.

`[COMPUTED]` **The partial fraction constants.** $A(x+1) + B(x-1) = 1$ gives $A + B = 0$ and
$A - B = 1$, so $A = \tfrac12$, $B = -\tfrac12$. Confirmed independently by SymPy's `apart`,
which returns $\tfrac{1}{2(x-1)} - \tfrac{1}{2(x+1)}$.

`[COMPUTED]` **The panel matches independently written formulas** for both $f$ and $F$ at all
1201 positions on all five entries, to $5\times10^{-5}$ — exactly half the last displayed digit.

## Flags raised in this session

1. **A claim in my first draft was flatly false, and it turned into the best paragraph in the
   article.** I had written that the faulty antiderivative "would have given $-\pi$ instead" for
   $\int_0^\pi x\sin x\,dx$. It gives $\pi$ — the correct answer. The two antiderivatives differ
   by $-2\sin x$, which vanishes at every multiple of $\pi$, so on $[0,\pi]$ the error cancels
   exactly. SymPy confirms it, and also that on $[0, \tfrac{\pi}{2}]$ the correct value is 1 and
   the faulty one is $-1$.

   The article now says that: a definite integral can launder a mistake, which mistakes it
   launders depends on the limits, and differentiating the antiderivative does not depend on
   anything. That is a better argument for the check than the one I had, and I did not think of
   it — the test found the false claim and the correction wrote itself.

2. **Two style violations, both caught by the audit rather than by reading.** A mid-sentence bold
   on "linear, nonrepeating", converted to italics. And six inline integrals set as `\int`
   without `\textstyle`, against your rule about chunky inline math; all six now carry it, while
   the two display equations correctly do not. Worth noting that this is the first article in 7D
   with inline integrals at all, which is why the rule had not bitten before.

3. **The gap row's format was too coarse to check.** It printed `toExponential(1)` — two
   significant figures — so a gap of 1.2345 read as `1.2e+0` and could not be compared against
   $2|\cos x|$. It now prints exponential only below $10^{-6}$ and four decimals otherwise, which
   reads correctly at both ends. Third article in a row where a display format, not a value, was
   the defect; I am now checking the formatter against the article's own claims before writing
   the test.

4. **792 words**, four `##` headings, two italicised spans (both quoting the framework), two
   cross-links, both resolving. Inside the 650–950 target. First BC-only article of the run, so
   `course: "AP Calculus BC"` with no `courses` list, matching your three existing BC articles.

5. **The deliberately wrong entry is the design decision worth your view.** Putting a known-bad
   antiderivative in a student-facing tool is a risk: someone could copy it. It is labelled "with
   the usual slip" on the button, the technique row says "second term signed wrongly", and the
   check row says the antiderivative is wrong. If that is still too close to the line, removing
   it costs one array entry and two sentences of prose.
