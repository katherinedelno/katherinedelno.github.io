# Claims ledger — Parametric, vector, and polar: three systems, one calculus

Article: `_posts/2026-07-30-parametric-vector-polar.md`
Session: 7D article 22, 2026-07-30. AP Calculus **BC only**, sequence 28, Unit 9.
**This completes the 31-article sequence proposal.**

Verification: `t.js` loads the shipped script in jsdom with a stubbed canvas context, clicks each
of the five presets, and sweeps all 1201 slider positions for each — 6005 evaluations —
comparing the point, both parameter derivatives, the slope, the second derivative, and the speed
against independently written closed forms. Symbolic results from SymPy.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **The article's thesis is the framework repeating itself.** Three essential knowledge
statements, quoted in the opening paragraph:

- **CHA-3.G.1**: "Methods for calculating derivatives of real-valued functions can be extended to
  parametric functions."
- **FUN-3.G.1**: "Methods for calculating derivatives of real-valued functions can be extended to
  functions in polar coordinates."
- **CHA-5.D.1**: "The concept of calculating areas in rectangular coordinates can be extended to
  polar coordinates."

All three marked bc only. Three "can be extended to" claims in one unit is the framework saying
there is nothing new here, and the article takes it at its word.

`[EXAM]` **CHA-3.G.2**, quoted with its hypothesis: "$\frac{dy}{dx}$, the slope of the line
tangent to a curve defined using parametric equations, can be determined by dividing
$\frac{dy}{dt}$ by $\frac{dx}{dt}$, **provided $\frac{dx}{dt}$ does not equal zero**." The
interactive refuses to divide at exactly those points.

`[EXAM]` **FUN-3.G.2**: "For a curve given by a polar equation $r = f(\theta)$, derivatives of
$r$, $x$, and $y$ with respect to $\theta$, and first and second derivatives of $y$ with respect
to $x$ can provide information about the curve." That is the panel's row list.

`[EXAM]` **Unit 9's overview supplies both warnings the article ends on:** "Since $\frac{dy}{dx}$
is in terms of $t$, students must be particularly careful when determining
$\frac{d^2y}{dx^2}$"; and "Paying attention to subscripts in problems involving more than one
particle is essential to clear communication." It also frames the whole unit as a sequel: "As
with particle motion on a line, students learning to handle motion in the plane will need to
practice interpreting which procedure is needed for different scenarios."

`[EXAM]` Topic 9.2 is "Second Derivatives of Parametric Equations", skill 1.E. Topic 9.9 carries
skill 3.D. Unit 9 is titled "Parametric Equations, Polar Coordinates, and Vector-Valued
Functions".

## Computed results

`[COMPUTED]` **All five presets, every panel row, against closed forms.** Across 1201 slider
positions per preset, the worst discrepancies were $5\times10^{-5}$ on the point, $5\times10^{-5}$
relative on the two parameter derivatives, and $2.4\times10^{-5}$ relative on the speed — that is,
correct to the four decimals displayed. The panel uses central differences on $x(t)$ and $y(t)$
and nothing else, so this checks the whole chain.

`[COMPUTED]` **The second derivatives**, against SymPy's closed forms, over every position where
the value is finite and under $10^3$:

```
  circle       d²y/dx² = −1/(3sin³t)        worst 4.9e-5 over 1146 positions
  ellipse      d²y/dx² = −2/(9sin³t)        worst 5.0e-5 over 1154 positions
  nodal cubic  d²y/dx² = (3t²+1)/(4t³)      worst 5.0e-5 over 1162 positions
```

The tool computes these as $\frac{d}{dt}\!\left[\frac{dy}{dx}\right] \big/ \frac{dx}{dt}$ — a
numerical derivative of a numerical derivative — and it still agrees to display precision.

`[COMPUTED]` **The circle's two identities.** Speed reads exactly 3.0000 at all 1201 positions, a
single distinct string. And $-\frac{1}{3\sin^3 t}$ equals $-\frac{9}{y^3}$ with $y = 3\sin t$,
checked to $10^{-12}$ at three values of $t$ — so the parametric route and the implicit route
give the same second derivative for $x^2+y^2=9$, which is what the prose claims.

`[COMPUTED]` **Vertical tangents are exactly reachable and correctly refused.** On the circle,
sliders 0 and 600 give $t = 0$ and $t = \pi$, where $\frac{dx}{dt} = 0$; the panel prints an em
dash and says the tangent is vertical. Slider 300 gives $t = \pi/2$, point $(0, 3)$, slope
exactly 0, and $d^2y/dx^2 = -\tfrac13$.

`[COMPUTED]` **The self-intersection.** For $x = t^2-1$, $y = t^3-t$, both $t = -1$ and $t = 1$
give the point $(0,0)$, with slopes $\frac{3t^2-1}{2t}$ equal to $-1$ and $+1$ respectively. Both
read from the panel at sliders 200 and 1000. One point of the plane, two tangent lines. At
$t = 0$, $\frac{dx}{dt} = 0$ and the panel refuses to divide.

`[COMPUTED]` **The polar entries are genuinely built from $r$.** The tool stores only
$r(\theta)$ and constructs $x = r\cos\theta$, $y = r\sin\theta$; nothing downstream knows the
curve is polar. As a consequence its speed should equal $\sqrt{r^2 + (r')^2}$ without that
formula ever being coded, and it does — worst relative gap $5\times10^{-5}$ on the cardioid and
$2.4\times10^{-5}$ on the rose, across all positions. SymPy confirms the identity symbolically
for both.

`[COMPUTED]` **The polar numbers the prose quotes.** Cardioid $r = 1+\cos\theta$: area
$\frac12\int_0^{2\pi} r^2 d\theta = \frac{3\pi}{2}$ exactly, and total arc length exactly 8.
Rose $r = 2\cos 3\theta$ over $[0,\pi]$: area exactly $\pi$. All three from SymPy and confirmed
by high-resolution Simpson.

`[COMPUTED]` **Slider resolution.** Ranges chosen so every parameter the article names lands on
an integer step: on the circle $t = 0,\ \pi/2,\ \pi$ at 0, 300, 600; on the cubic
$t = -1,\ 0,\ 1$ at 200, 600, 1000.

## Judgment claims

`[JUDGMENT]` "There is no new calculus in Unit 9. There is new bookkeeping." The article's
organising claim, supported by the three quoted extension statements.

`[JUDGMENT]` "A parametrisation carries more information than a curve does." An observation about
the circle-versus-ellipse comparison, made visible by the velocity arrow.

`[JUDGMENT]` The closing note's advice to write the parameter on every derivative. A habit,
offered as one, and aimed at the framework's own stated warning.

---

## Flags raised in this session

1. **The seventh slider-reachability failure of 7D, and the last.** The nodal cubic ran over
   $[-1.9, 1.9]$, so $t = \pm 1$ — the two parameters the prose names by number — landed at
   slider positions 284.21 and 915.79. Changed the range to $[-1.5, 1.5]$, which puts them at
   200 and 1000 exactly, and narrowed the window to match. Seven instances across twenty-two
   articles; the pattern is always the same and the fix is always to choose the range from the
   prose rather than from the picture.

2. **The tool's polar handling is the design decision I would most like your eye on.** Polar
   presets store only $r(\theta)$, and everything else — the point, both derivatives, the slope,
   the second derivative, the speed — is computed by the parametric code with no special case.
   That makes the article's thesis structural rather than asserted: if polar needed its own rules,
   the tool would not work. The check that it does work is the speed agreeing with
   $\sqrt{r^2+(r')^2}$, a formula that appears nowhere in the code.

3. **One cross-link on the first pass again.** Three now, and the added paragraph on displacement
   versus distance in the plane is the framework's own framing of the unit as a sequel to
   straight-line motion. That paragraph also took the article from 724 to 820 words.

4. **820 words**, four `##` headings, five display equations, no italics, three cross-links, all
   resolving. Inside the 650–950 target.

5. **Unit 9 coverage.** This article takes 9.1, 9.2, 9.4, 9.6, 9.7, and 9.8 at least in part, and
   states the arc length result from 9.3. Topic 9.5 (integrating vector-valued functions) and
   topic 9.9 (area between two polar curves) are named only in passing. Neither is in the
   approved plan, and 9.9 in particular is a standard free-response setup.

6. **The plan is complete.** All 31 rows of `_style/CALCULUS-SEQUENCE-PROPOSAL.md` are now
   written: nine existing articles renumbered, twenty-two new ones. The gaps I have flagged along
   the way and would put in priority order are: **volumes** (Unit 8 topics 8.7–8.12, the largest
   single hole), **concavity and the second derivative test** (Unit 5 topics 5.6–5.7, now assumed
   by four articles), **substitution** (Unit 6), and **separation of variables** (Unit 7). None
   of the four is in the approved sequence, and each would need a number inserted.
