# Claims ledger — Area between curves, and the average value of a function

Article: `_posts/2026-07-30-area-and-average-value.md`
Session: 7D article 21, 2026-07-30. AP Calculus sequence 27, Unit 8 topics 8.1, 8.4, 8.5, 8.6.

Verification: `t.js` loads the shipped script in jsdom with a stubbed canvas context, clicks each
of the five presets, and compares the signed integral and the total area against values computed
exactly in SymPy. The tool integrates numerically by composite Simpson and never uses a closed
form.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **CHA-4.B.1** (topic 8.1), quoted as the article's first display: "The average value of
a continuous function $f$ over an interval $[a,b]$ is $\frac{1}{b-a}\int_a^b f(x)\,dx$."
Learning objective CHA-4.B: "Determine the average value of a function using definite
integrals." Suggested skill 1.E.

`[EXAM]` **Enduring understanding CHA-4**, quoted in the opening: "Definite integrals allow us to
solve problems involving the accumulation of change over an interval."

`[EXAM]` **The confusion the second section is built on is the framework's own.** Unit 8's
Preparing for the AP Exam: "Some students confuse the average value and the average rate of
change of a function on an interval. To alleviate confusion, first provide students with average
value problems accompanied by relevant graphs and guide them to an understanding of **why an
average value may be less than, equal to, or greater than the midpoint of the range**." The
article gives one example of each of those three cases, which is what the guidance asks for.

`[EXAM]` **CHA-5.A.1** (topic 8.4): "Areas of regions in the plane can be calculated with
definite integrals." Its suggested skill is **4.C**, "Use appropriate mathematical symbols and
notation" — the only 4.C in the unit, and the reason the third section is about how the integrand
is written rather than about how it is evaluated.

`[EXAM]` **CHA-5.A.2** (topic 8.5): "Areas of regions in the plane can be calculated using
functions of either $x$ or $y$." Suggested skill 1.E.

`[EXAM]` **Topic 8.6 is "Finding the Area Between Curves That Intersect at More Than Two
Points"**, with suggested skill 2.B, "Identify mathematical information from graphical,
numerical, analytical, and/or verbal representations." A whole topic for the crossing case, which
is why the article gives it a section rather than a caveat.

## Computed results

Every figure below was computed in SymPy and then read back out of the running tool.

`[COMPUTED]` **The three midpoint cases on $[0,1]$**, all with range $[0,1]$ and midpoint
$\tfrac12$:

```
  f(x) = x       average value 1/2    equal to the midpoint
  f(x) = x²      average value 1/3    below it
  f(x) = √x      average value 2/3    above it
```

`[COMPUTED]` **Average value against average rate of change.** On $f(x) = x^2$ over $[1,3]$: the
average rate of change is $\frac{9-1}{2} = 4$; the average value of $f' = 2x$ is
$\frac12\int_1^3 2x\,dx = 4$, the same number; the average value of $f$ itself is
$\frac12\int_1^3 x^2\,dx = \tfrac{13}{3} \approx 4.3333$, a different one. The identity
$\frac{f(b)-f(a)}{b-a} = (f')_{\text{avg}}$ is the Fundamental Theorem divided by the width.

`[COMPUTED]` **All five presets, signed integral and total area, tool against SymPy:**

```
  preset                       signed      exact      total       exact
  x² and its average value     0.000000    0          0.256600    4√3/27 = 0.2566003
  √x and its average value     0.000000    0          0.197500    16/81  = 0.1975309
  y = x and y = x²             0.166700    1/6        0.166700    1/6
  y = x and y = x³             0.000000    0          0.500000    1/2
  x = y+2 and x = y²           4.500000    9/2        4.500000    9/2
```

All within $10^{-4}$, which is the displayed precision.

`[COMPUTED]` **The average-value presets have signed integral exactly zero**, which is what makes
the constant the average, and their two shaded pieces have equal area. For $x^2$ the crossing is
at $x = 1/\sqrt3$ and each piece is $\tfrac{2\sqrt3}{27}$; for $\sqrt x$ the crossing is at
$x = \tfrac49$ and each piece is $\tfrac{8}{81}$. Halves equal in both cases, exactly.

`[COMPUTED]` **The crossing case is flagged and the others are not.** The panel says "larger,
because the boundaries swap" only on $y = x$ against $y = x^3$, where the signed integral is 0
and the area is $\tfrac12$. On the three non-crossing presets it says the two agree, correctly.

`[COMPUTED]` **The $y$-oriented preset.** $y^2 = y+2$ gives $y = -1$ and $y = 2$ (both roots
verified by substitution), and $\int_{-1}^{2}\big((y+2)-y^2\big)dy = \tfrac92$, evaluated as
$\tfrac{10}{3} - \left(-\tfrac76\right)$. The tool reports the variable of integration as $y$.

`[COMPUTED]` **The $x$ versus $x^2$ area.** $\tfrac12 - \tfrac13 = \tfrac16$, and both the
combined and the separated forms give it because $x \geq x^2$ on $[0,1]$ throughout.

`[COMPUTED]` **The $x$ versus $x^3$ area.** They meet at $-1$, $0$, $1$. Signed integral zero;
area $2\left(\tfrac12 - \tfrac14\right) = \tfrac12$.

## Judgment claims

`[JUDGMENT]` "Two of Unit 8's applications look unrelated and are the same calculation." The
article's organising claim, which the tool then enforces by putting average value and area in the
same panel with the same rows.

`[JUDGMENT]` "The midpoint of the range asks where the outputs sit. The average value asks how
long the function spends near each of them." An explanation of the three computed cases, not an
additional claim.

`[JUDGMENT]` The closing note's single question — am I allowed to let this cancel? — is a habit
offered as one.

---

## Flags raised in this session

1. **The interactive unifies the two halves of the article rather than illustrating them
   separately.** Average value is the constant $c$ for which $\int_a^b (f-c)\,dx = 0$, so it is
   an area-between-curves problem whose answer is zero. Making that the first two presets means
   the tool has one set of rows for both topics, and the reader sees why the definition has the
   shape it does. If you would rather average value had its own picture, that is a second canvas.

2. **One cross-link on the first pass**, and the count is becoming a pattern worth naming: four
   of the last six articles shipped their first draft with fewer than two. I have added a link
   check to the audit I run before writing the ledger, rather than continuing to notice it late.
   Three links here, all resolving.

3. **A false positive in my own inline-math audit.** The notation sentence contains
   `\textstyle\int_0^1 x\,dx - \int_0^1 x^2\,dx`, where the `\textstyle` declaration already
   applies to the whole group and therefore to both integrals. My checker flagged the second one.
   I added the redundant `\textstyle` rather than teach the checker about TeX scoping, on the
   grounds that the explicit form is also clearer to anyone editing the file — but recording it
   here so the pattern is not mistaken for a real defect if you see it elsewhere.

4. **827 words**, four `##` headings, one italicised span, three cross-links, all resolving.
   Inside the 650–950 target.

5. **Unit 8 is only partly covered and mostly by design.** This article takes 8.1, 8.4, 8.5, and
   8.6. Topics 8.2 and 8.3 (motion and applied contexts via integrals) are close cousins of the
   particle motion article at sequence 13. Topics 8.7 through 8.12 are volumes — cross sections,
   discs, washers — which are a substantial block with no article and are not in the approved
   plan. Topic 8.13, arc length, is BC and also unwritten. Volumes are the largest single gap
   left in the Calculus sequence.

6. **One article left in the plan**: sequence 28, parametric, vector, and polar. Everything else
   in the 31-row proposal is now written.
