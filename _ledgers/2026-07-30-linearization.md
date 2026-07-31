# Claims ledger — Linearization, and whether the answer is too big

Article: `_posts/2026-07-30-linearization.md`
Session: 7D article 13 (tier 4), 2026-07-30. AP Calculus sequence 15, Unit 4 topic 4.6.

Verification: `t.js` loads the shipped script in jsdom with a stubbed canvas context, clicks each
of the four function buttons, and sweeps all 1201 slider positions for each — 4804 evaluations —
comparing $L$, $f$, the error, the over/under verdict, and the concavity row against
independently written reference formulas and an independent sign sweep. Symbolic results from
SymPy.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **CHA-3.F.1**: "The tangent line is the graph of a locally linear approximation of the
function near the point of tangency." Paraphrased almost verbatim in the first section.

`[EXAM]` **CHA-3.F.2**, and the whole reason this article has a third section: "For a tangent
line approximation, the function's behavior near the point of tangency **may** determine whether
a tangent line value is an underestimate or an overestimate of the corresponding function value."
The framework's "may" is quoted and italicised, and the article's argument is that the hedge is
load-bearing.

`[EXAM]` **Topic 4.6's suggested skill is 1.F**, "Explain how an approximated value relates to
the actual value" — the only 1.F in Unit 4, and the reason the fourth section is about the size
of the error rather than only its sign.

`[EXAM]` Topic title, verbatim: "Approximating Values of a Function Using Local Linearity and
Linearization". Enduring understanding CHA-3: "Derivatives allow us to solve real-world problems
involving rates of change."

`[EXAM]` Unit 4's overview supplies the article's motivation: "Students may not understand why
they would use a tangent line approximation (i.e., linearization) rather than simply evaluating a
function. Expose them to scenarios where an exact function value can't be calculated, and then
ask them to determine whether a particular approximation is an overestimate or an underestimate."
That is the $\sqrt{4.1}$ example and the over/under question, in that order.

`[STANDARD]` A tangent line to a concave-up arc lies below it and to a concave-down arc lies
above it, on any interval where the concavity is constant. Standard, and the article states the
interval condition rather than the pointwise one.

## Computed results

`[COMPUTED]` **The panel matches independently written formulas at all 4804 positions.** Largest
discrepancies: $L$ to $4.4\times10^{-16}$, $f$ to $5\times10^{-5}$ (exactly half of the last
displayed decimal), error to $5\times10^{-5}$ relative. Zero verdict errors — the over/under
label agrees with the sign of $L - f$ everywhere.

`[COMPUTED]` **The concavity row matches an independent sign sweep at all 4804 positions**, with
zero mismatches on all four functions. The row samples $f''$ at 399 interior points strictly
between $a$ and $x$; the harness repeats that with separately written second derivatives.

`[COMPUTED]` **The square root at $a = 4$.** $f(4) = 2$, $f'(4) = \tfrac14$, $f''(4) = -\tfrac1{32}$.
$L(4.1) = 2.025$ against $\sqrt{4.1} = 2.02484567313\ldots$

```
  x       L        f (true)          L - f          ratio to previous
  4.05    2.0125   2.012461179750    3.8820e-05
  4.1     2.025    2.024845673132    1.5433e-04     3.9755
  4.2     2.05     2.049390153192    6.0985e-04     3.9516
  9       3.25     3                 2.5000e-01
```

Both doubling ratios are within 0.05 of 4, which is the article's "very nearly four". All four
$x$ values are exactly reachable at slider positions 405, 410, 420, 900.

`[COMPUTED]` **The quadratic estimate.** $\tfrac12 f''(4)(0.1)^2 = -\tfrac1{6400} = -0.00015625$
in magnitude, against a true error of $0.00015433$. Both figures are quoted in the article and
both are exact to the digits shown.

`[COMPUTED]` **The sine at $a = 0$.** $f''(0) = 0$, so the pointwise test says nothing. At
$x = 0.5$ the tool reports an overestimate with $f''$ negative throughout; at $x = -0.5$ it
reports an underestimate with $f''$ positive throughout. $L - f$ is $+0.020574$ and $-0.020574$
respectively — the same magnitude, opposite signs, one tangent line.

`[COMPUTED]` **The cubic at $a = -1$, which is the article's centrepiece.** $L(x) = 3x + 2$ and

$$L(x) - f(x) = 3x + 2 - x^3 = -(x-2)(x+1)^2,$$

factored in SymPy, with roots at $x = -1$ (double, the tangency) and $x = 2$. Read from the tool:

```
  x = -2   L = -4    f = -8    error  +4      overestimate   f'' negative throughout
  x =  0   L =  2    f =  0    error  +2      overestimate   f'' changes sign
  x =  1   L =  5    f =  1    error  +4      overestimate   f'' changes sign
  x =  2   L =  8    f =  8    error   0      the line meets the curve
  x =  3   L = 11    f = 27    error -16      underestimate  f'' changes sign
```

$f''(-1) = -6 < 0$, so the pointwise test predicts an overestimate — correct at $x = -2$, $0$,
and $1$, and wrong at $x = 3$. The inflection at $x = 0$ lies strictly between $a$ and every
positive $x$, which is exactly when the guarantee lapses.

`[COMPUTED]` **Slider ranges.** 1201 positions, with per-function ranges chosen so that every $x$
the article names lands on an integer step: $4.05/4.1/4.2/9$ at 405/410/420/900; $\pm 0.5$ at
700/500; $-2/0/1/2/3$ at 0/480/720/960/1200. Verified in the harness, not by arithmetic.

## Judgment claims

`[JUDGMENT]` "No longer an approximation of anything" (of $L(9) = 3.25$ against 3). Editorial;
the numbers are computed.

`[JUDGMENT]` "Naming the sign of $f''(a)$ alone is a claim about one point being offered as a
claim about a stretch." The article's thesis, argued from the cubic rather than asserted.

`[JUDGMENT]` The closing note's two habits — choose $a$ at the nearest easy point, sketch
concavity across the whole gap — are teaching advice, offered as such.

---

## Flags raised in this session

1. **The panel's own display contradicted the article's numerical claim, and only the harness
   caught it.** The error row used four decimal places, so the three square-root errors printed as
   `3.882e-5`, `0.0002`, and `0.0006` — from which a reader computing the doubling ratios gets
   5.15 and 3.00, not 4. The article says "very nearly four". The error row now uses five
   significant figures, printing `0.000038820`, `0.00015433`, `0.00060985`, and the ratios read
   3.9755 and 3.9516. This is the first time a formatting choice, rather than a value, made the
   prose false; worth watching for wherever an article quotes a ratio.

2. **One of my test tolerances was wrong after that fix**, because five significant figures on a
   value near 16 leaves only three decimals. Changed to a relative tolerance. My error, not the
   tool's.

3. **The concavity row excludes the endpoints on purpose.** $a$ itself may be an inflection
   point — it is, for the sine — and the concavity *at* $a$ is precisely the thing the article
   argues is not the right question. Sampling the open interval is what makes the sine case read
   correctly on both sides. Noted in a code comment as well as here.

4. **859 words**, four `##` headings, two italicised spans, three cross-links, all resolving.
   Inside the 650–950 target and the longest of tier 4 so far.

5. **A forward reference I would like your view on.** The last section now points to the Taylor
   polynomials article, on the grounds that the linearization is the degree-one Taylor polynomial
   and the $\tfrac12 f''(a)(x-a)^2$ term is the next one. That is a BC article being linked from
   an AB article. It is a forward reference rather than a prerequisite, and the sentence stands
   without following the link, but say the word and I will drop it.

6. **I shipped the wrong sequence number and the wrong kind, and caught it after writing the
   ledger.** I had set `sequence: 14` and `kind: mechanics`. The approved plan puts linearization
   at **15** with `kind: foundations`; position 14 belongs to your existing related rates article
   from 20 July, which already carries that number. Two articles sharing a sequence within one
   band produces an arbitrary order, so this would have quietly scrambled the Unit 4 run. Fixed
   to 15 and foundations.

   I then audited every article in the repo against the banding rules: **no duplicate sequence
   numbers in any of the four bands.** AP Calculus now runs 1–31 with nine gaps at the positions
   still unwritten (16, 17, 19, 22, 23, 24, 26, 27, 28); Statistics has one gap at 6; Precalculus
   and Looking ahead are contiguous. From here I will check the plan's row before writing rather
   than after.

7. **A title deviation, noted rather than fixed.** The plan calls this article "Linearization and
   the tangent line as approximation"; I titled it "Linearization, and whether the answer is too
   big". I have been drifting from the plan's working titles for several articles now — particle
   motion is another — on the grounds that the plan fixed the sequence rather than the wording.
   If you would rather the titles match the plan exactly, that is a quick pass over the six
   articles from this session.
