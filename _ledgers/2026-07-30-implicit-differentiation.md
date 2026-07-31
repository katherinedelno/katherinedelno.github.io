# Claims ledger — Implicit differentiation

Article: `_posts/2026-07-30-implicit-differentiation.md`
Session: 7D article 10 (tier 3), 2026-07-30. AP Calculus sequence 11, Unit 3 topic 3.2, with
supporting content from Unit 5 topic 5.12.

Verification: `t.js` and `t2.js` load the shipped script in jsdom with a stubbed canvas context,
click each curve button, and sweep all 1001 slider positions for each curve, reading the point,
the formula's numerator and denominator, and both slope figures back out of the live DOM.
Reference results computed independently in SymPy.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **FUN-3.D.1**, the article's second paragraph: "The chain rule is the basis for
implicit differentiation." One sentence, and it is the entire essential knowledge for topic 3.2.

`[EXAM]` **The exam guidance quoted in the first section is verbatim from Unit 3's Preparing for
the AP Exam:** "In expressions like $\frac{y}{3y^2 - x}$, students must recognize that the chain
rule applies to $y$ because $y$ depends on $x$." I kept the CED's own example expression rather
than substituting one of mine.

`[EXAM]` Topic 3.2 is titled "Implicit Differentiation" and carries suggested skill 1.E, "Apply
appropriate mathematical rules or procedures, with and without technology." Applying, not
identifying — which is why this article is a method article rather than a classification drill.

`[EXAM]` **FUN-4.D.1**, topic 5.12 (Exploring Behaviors of Implicit Relations): "A point on an
implicit relation where the first derivative equals zero or does not exist is a critical point of
the function." This is what licenses the article's claim that the vanishing denominator is course
content rather than an edge case. It sits in Unit 5, not Unit 3, and the article says so.

`[EXAM]` **FUN-4.E.2**: "Second derivatives involving implicit differentiation may be relations
of $x$, $y$, and $\frac{dy}{dx}$." Quoted almost verbatim to open the fourth section.

`[EXAM]` Unit 3's overview uses "outer" and "inner" in quotation marks for chain rule
decomposition, which is the vocabulary the previous article's layer stack uses. Noted here
because I had flagged in the tier-2 ledger that "cusp" and "corner" are *not* the CED's words;
"outer" and "inner" are.

## Computed results

`[COMPUTED]` **All four relations, symbolically.** For each, $-F_x/F_y$ was computed from the
defining equation and compared against the formula the tool displays. All four match exactly:

```
  x² + y² = 25         ->  -x / y
  x²/9 + y²/4 = 1      ->  -4x / 9y
  x² + xy + y² = 7     ->  -(2x + y) / (x + 2y)
  x³ + y³ = 6xy        ->  (2y - x²) / (y² - 2x)
```

`[COMPUTED]` **Every plotted point is on its curve.** Substituting the parametrisation back into
the defining relation and simplifying gives exactly 0 in SymPy for all four. Numerically, across
1001 slider positions per curve, the largest residual is $1.2\times10^{-3}$ on the folium, whose
coordinates run to about 3, so that is a relative error near $10^{-4}$ from `Math.tan` at the
far end of the parameter range.

`[COMPUTED]` **The formula agrees with an independent slope everywhere.** The tool computes
$dy/dx$ two ways — from the implicit formula, and as $(dy/dt)/(dx/dt)$ from the parametrisation,
which never uses the implicit formula. Over 4004 slider positions the two agreed to the printed
precision at every point, with zero disagreements about *which* points are undefined. SymPy
confirms the identity symbolically for all four curves.

`[COMPUTED]` **The worked example.** $x^2 + xy + y^2 = 7$ at $x = 1$ gives $y^2 + y - 6 = 0$, so
$y = 2$ or $y = -3$; both satisfy the relation ($1 + 2 + 4 = 7$ and $1 - 3 + 9 = 7$). The slopes
are $-(2+2)/(1+4) = -4/5$ and $-(2-3)/(1-6) = -1/5$. Read from the running tool at its nearest
slider positions to each point: $-0.80$ and $-0.20$.

`[COMPUTED]` **The circle's vertical tangents are exactly reachable.** Slider position 0 gives
$(5, 0)$ and position 500 gives $(-5, 0)$, both to the printed precision, and at both the
readout reports "undefined — vertical tangent" in the formula row and "undefined" in the measured
row. Positions 250 and 750 give $(0, 5)$ and $(0, -5)$ with slope exactly 0. The ellipse
behaves the same way at 0, 500, and 1000.

`[COMPUTED]` **The folium's special points.** $\big(2^{5/3}, 2^{4/3}\big) = (3.1748, 2.5198)$
satisfies $x^3 + y^3 = 6xy$ to $10^{-9}$, and its denominator $y^2 - 2x$ is zero to $10^{-12}$.
The mirror point $\big(2^{4/3}, 2^{5/3}\big)$ zeroes the numerator $2y - x^2$. The slider does
not land exactly on either. Measured from the running tool: the steepest slope on the loop is
**501.6** at slider 429, and the flattest is $1.8\times10^{-3}$ at slider 576 — which is what
the prose now says, having previously claimed both were "visible" without saying how.

`[COMPUTED]` **The second derivative on the circle.** SymPy's implicit second derivative of
$x^2 + y^2 = 25$ is $-(x^2 + y^2)/y^3$, which on the curve is $-25/y^3$. The article's three
displayed steps reproduce that: quotient rule, substitute $dy/dx = -x/y$, then apply the
constraint last.

`[COMPUTED]` **The closing note's check.** $(3,3)$ is on the folium ($27 + 27 - 54 = 0$), and
$(2\cdot3 - 9)/(9 - 6) = -3/3 = -1$. The curve is symmetric in $x$ and $y$, so $y = x$ is an
axis of symmetry and $-1$ is the only slope consistent with it.

## Judgment claims

`[JUDGMENT]` "A formula for $y$ in terms of $x$ that anyone wants to differentiate." An
editorial characterisation of solving $x^2 + xy + y^2 = 7$ by the quadratic formula.

`[JUDGMENT]` "An answer of the form '$dy/dx$ at $x = 1$' is not a well-posed question here."
Follows from the two computed slopes at $x = 1$.

`[JUDGMENT]` "Substituting the constraint is the last step, not the first, and doing it early is
how the algebra usually goes wrong." A claim about method, supported by the worked derivation
where the collapse to $-25/y^3$ only becomes available after the quotient rule and the
substitution of $dy/dx$.

`[JUDGMENT]` "Most sign errors in implicit differentiation die at that test." Overstated as a
frequency claim; kept because the mechanism is demonstrated rather than asserted.

---

## Flags raised in this session

1. **Floating-point residue was printing as scientific notation.** At $(-5, 0)$ on the circle the
   $y$ coordinate came out as $6.12\times10^{-16}$ — `Math.sin(Math.PI)` — and the formatter's
   small-number branch rendered it in exponential form, so the readout said `6.123e-16` where it
   should say `0.0000`. Same for a slope of $-6.1\times10^{-17}$ at the top of the circle. The
   formatter now snaps magnitudes below $10^{-12}$ to zero, with a comment saying why. Caught by
   the harness comparing against exact strings, not by reading the code.

2. **A vague claim replaced by measured numbers.** I had written that the folium's vertical and
   horizontal tangents are "visible in the tool as the point rounds the loop." The slider does
   not actually land on either, so nothing ever reads "undefined" on that curve. The prose now
   reports what the tool really shows — 501.6 and 0.0018, both measured — and contrasts it with
   the circle, where the exact case *is* reachable. Showing both behaviours is better than the
   claim I originally made, but I did not choose it deliberately; the test found it.

3. **A mid-sentence bold slipped in.** I had emphasised "or does not exist" with `**`, which the
   style sheet forbids. Changed to italics, the corpus's one permitted emphasis. That is the
   first recurrence since the 44 were converted in session 1.

4. **Nested fractions in a display were full-size.** The second-derivative chain had
   `\frac{dy}{dx}` and `\frac{x^2}{y}` sitting inside the numerator of another `\frac`. Per your
   instruction about chunky inline math, the inner ones are now `\tfrac`. The outer ones stay
   `\frac`.

5. **730 words**, four `##` headings, one italicised span, two cross-links. Inside the 650–950
   target.

6. **A design choice worth naming.** The four curves are parametrised rather than contour-traced,
   which is what makes the independent slope check possible — $(dy/dt)/(dx/dt)$ never touches the
   implicit formula, so the two calculations share no code. The cost is that only curves with
   clean parametrisations can appear, which ruled out relations like $\sin(xy) = x$. If you want
   a curve the tool cannot currently draw, marching squares would open that up at the cost of the
   independent check.
