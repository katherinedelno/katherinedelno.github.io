# Claims ledger — Reading an accumulation function off the graph of its integrand

Article: `_posts/2026-07-30-accumulation-functions.md`
Session: 7D article 17 (tier 5 territory, Unit 6), 2026-07-30. AP Calculus sequence 22, Unit 6
topics 6.5 and 6.6, resting on 6.4.

Verification: `t.js` loads the shipped script in jsdom with a stubbed canvas context and sweeps
both sliders — a 31 by 95 grid of $(a,x)$ pairs, plus every one of the 1601 positions of $x$ —
comparing the panel against an independently written trapezoid computation. Exact values from
SymPy and from `fractions.Fraction`.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **FUN-5.A.3** (topic 6.5), which is the article's whole premise: "Graphical, numerical,
analytical, and verbal representations of a function $f$ provide information about the function
$g$ defined as $g(x) = \int_a^x f(t)\,dt$." Paraphrased in the opening.

`[EXAM]` **Topic 6.5's suggested skill is 2.D**, "Identify how mathematical characteristics or
properties of functions are related in different representations" — which is the translation
table, and the same skill your "Reading the graph of f′" article is built on. Topic title:
"Interpreting the Behavior of Accumulation Functions Involving Area".

`[EXAM]` **FUN-5.A.1**: "The definite integral can be used to define new functions."
**FUN-5.A.2**: "If $f$ is a continuous function on an interval containing $a$, then
$\frac{d}{dx}\left[\int_a^x f(t)\,dt\right] = f(x)$, where $x$ is in the interval." The article
cites this and points at the existing FTC article for the argument rather than repeating it.

`[EXAM]` **FUN-6.A.1**: "In some cases, a definite integral can be evaluated by using geometry
and the connection between the definite integral and area." This licenses the worked triangle
computation.

`[EXAM]` **FUN-6.A.2**: "Properties of definite integrals include the integral of a constant
times a function, the integral of the sum of two functions, reversal of limits of integration,
and the integral of a function over adjacent intervals." The last two are the fourth and third
sections respectively.

`[EXAM]` Enduring understanding **FUN-5**: "The Fundamental Theorem of Calculus connects
differentiation and integration."

## Not duplicating the existing article

`[JUDGMENT]` Your FTC article of 17 July, at sequence 21, already covers why $A' = f$ with the
sliver argument, the evaluation shortcut as a corollary, and a two-panel sweep interactive on
$f(t) = 2\sin t + 0.6$. Its closing note asks the reader to sketch $f$ and then sketch $A$ from
the picture alone. **This article is that exercise made into the topic**, and it deliberately
does three things the existing one does not: it uses a piecewise linear $f$ with no formula,
which is the exam's format; it marks the features of $g$ rather than only tracing it; and it
makes the lower limit a control. The one-line derivation of $g' = f$ is not repeated — the
article links to it instead.

## Computed results

`[COMPUTED]` **The integrand.** Piecewise linear through $(0,-1)$, $(2,3)$, $(5,-3)$, $(8,1)$.
Slopes $2$, $-2$, $\tfrac43$. Zeros at $x = \tfrac12,\ \tfrac72,\ \tfrac{29}{4}$, that is
$0.5$, $3.5$, $7.25$. Corners at $x = 2$ and $x = 5$. Segment signed areas exactly $2$, $0$,
$-3$. All from SymPy.

`[COMPUTED]` **Every value the prose quotes, read from the running panel with $a = 0$:**

```
  x       g(x)        f(x)
  0        0.0000     -1
  0.5     -0.2500      0        local minimum of g
  2        2.0000      3        inflection of g (corner of f)
  3.5      4.2500      0        local maximum of g
  5        2.0000     -3        inflection of g (corner of f)
  7.25    -1.3750      0        local minimum of g
  8       -1.0000      1
```

`[COMPUTED]` **The worked geometry.** $g(3.5)$ by cutting at the axis crossing: triangle from
$0$ to $0.5$ with base $\tfrac12$ and height $1$, below the axis, $-\tfrac14$; triangle from
$0.5$ to $2$ with base $\tfrac32$ and height $3$, $+\tfrac94$; triangle from $2$ to $3.5$ with
base $\tfrac32$ and height $3$, $+\tfrac94$. Sum exactly $\tfrac{17}{4}$, matching the panel.
Failing to cut at the crossing gives $\tfrac{19}{4} = 4.75$ instead — the article names the
error and this is the number it would produce.

`[COMPUTED]` **The panel matches an independent trapezoid computation** across a 31 by 95 grid of
lower and upper limits — 2945 pairs — with worst discrepancy below $10^{-4}$, which is the
displayed precision.

`[COMPUTED]` **The verbal readings never disagree with the arithmetic.** Over all 1601 positions
of $x$: zero cases where the monotonicity note disagreed with the sign of $f(x)$, and zero where
the concavity note disagreed with the sign of $f'(x)$.

`[COMPUTED]` **The three slopes of $f$ read back correctly** from the $g''$ row: $2$, $-2$, and
$1.3333$ on the pieces containing $x = 1$, $3$, and $6$.

`[COMPUTED]` **Changing the lower limit shifts $g$ by a constant.** For seven values of $a$
($0, 1, 2, 3.5, 5, 6.5, 8$), the values of $g$ at all five feature locations
($0.5, 3.5, 7.25, 2, 5$) shifted by an identical amount, with spread below $10^{-9}$, and that
amount equalled $-g_0(a)$ in every case. So no feature moves, which is what the article claims
and what the caption tells the reader to watch for.

`[COMPUTED]` **$g(a) = 0$ for every lower limit**, checked at 229 values of $a$, all exactly zero.

`[COMPUTED]` **The two maxima.** With $a = 0$, $g(3.5) = \tfrac{17}{4}$. With $a = 2$,
$g(3.5) = \tfrac94$. Same location, different value, both read from the panel.

`[COMPUTED]` **Reversing the limits works.** $\int_5^2 f = 0$, $\int_8^5 f = 3$, and
$\int_2^0 f = -2$ — each the negative of the corresponding forward integral, confirmed against
the segment areas $2, 0, -3$.

## Judgment claims

`[JUDGMENT]` "A definite integral of zero says the accumulation returned to where it started, not
that nothing happened." An interpretation, made concrete by the middle segment where $f$ is
nowhere zero and $g$ is nowhere constant.

`[JUDGMENT]` "The sign flip feels as though it ought to reverse something, and it does not."
A claim about how the reversal reads, offered as an invitation to check it on the tool.

`[JUDGMENT]` The closing note's claim about the order of parts on a free-response question. It
matches the structure your existing FTC article already describes and is presented as a habit.

---

## Flags raised in this session

1. **The first draft was 685 words and leaned entirely on the table**, which is thin for an
   article carrying a tool. The worked geometry — three triangles, cut at the axis crossing —
   was added because it is the one thing FUN-6.A.1 asks for that the table cannot express, and it
   brought the article to 799 words. It also gave the article a number for the error it warns
   about: $\tfrac{19}{4}$ rather than $\tfrac{17}{4}$.

2. **The exhaustive sweep is over two controls this time**, which is why the grid is coarse in
   $a$ and fine in $x$ rather than full. 2945 pairs at every displayed digit is enough to make
   the shift claim; a full $1601^2$ sweep would be 2.6 million panel renders for no additional
   confidence.

3. **The overlap with your 17 July article was the main design constraint**, and it is worth
   your eye. I chose to make this article the reading rather than the theorem, and to link back
   for the derivation. If it still feels like a second pass over the same ground, the parts most
   easily cut are the translation table's first four rows, which the older article states in
   prose.

4. **799 words**, four `##` headings, a ten-row table, no italics, two cross-links, both
   resolving. Inside the 650–950 target, and the read-time formula's table term accounts for the
   extra minute.

5. **Sequence 20 and 21 are your existing Riemann sums and FTC articles**, both already carrying
   those numbers. This is 22 and there is no collision — I checked the whole corpus again after
   the sequence 15 mistake, and AP Calculus still has no duplicates.

6. **The concavity gap from the last ledger is now larger.** This article's table uses concave
   up and concave down as known terms, as do linearization and optimization. Unit 5 topics 5.6
   and 5.7 remain unwritten and are not in the approved plan. That is now four articles resting
   on an idea the sequence never introduces.
