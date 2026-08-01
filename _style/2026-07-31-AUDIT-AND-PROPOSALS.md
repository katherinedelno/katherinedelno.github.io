# Article audit, featured selection, and new-article proposals

2026-07-31. All 55 published articles read in full and checked against the current CEDs:

- `ap-calculus-ab-and-bc-course-and-exam-description.pdf` **plus** the Fall 2026
  Clarifications and Corrections
- `ap-precalculus-course-and-exam-description.pdf`
- `ap-statistics-course-and-exam-description-effective-fall-2026.pdf`

Every numerical claim, worked example, and slider-dependent assertion was recomputed
independently. Corrections were applied directly to the article files; the change log is
Part I.

---

## Part 0 — Headline

**The corpus is in excellent shape.** Across roughly 78,000 words I found no errors of
mathematical substance — no wrong derivative, no wrong integral, no misstated theorem, no
mis-set condition. Every worked example I recomputed came out right, including the ones
where it would have been easy to be sloppy: the folium's vertical-tangent point at
$(2^{5/3}, 2^{4/3})$, the $x^{100}/e^{x}$ peak near $3.7 \times 10^{156}$ at $x = 100$, the
cardioid's arc length of exactly 8, the Charig kidney-stone case mix of 77%, the
$t_{10}$ area of 0.9216 between $\pm 1.96$, and all five regression presets' correlations
and slopes.

The eight corrections below are of three kinds: one factual overstatement, one sign error
in a self-test, one editorial comment left in the source, and five places where an
article's instruction and its own interactive had drifted apart or where CED wording had
moved. None of them would mislead a student about the mathematics. All are now fixed.

**CED alignment is current, including the parts that are easy to miss.** The
Extreme Value Theorem article states the *closed*-interval hypothesis and explicitly flags
that FUN-1.C.1 was corrected for Fall 2026 — the original CED reads $(a,b)$ and the
correction reads $[a,b]$. The chi-square article correctly reflects the removal of
goodness-of-fit. The distribution explorer covers exactly the six distributions that
survived the revision and correctly omits the geometric. Nothing in the corpus teaches
content that has been cut, and nothing teaches inference for regression slope, which the
revised Statistics course also dropped.

---

## Part I — Corrections applied

### 1. `2026-07-23-harmonic-series-surprises-of-infinity.md` — factual error

**Was:** "To pass 100, you would need more terms than there are atoms in the observable
universe."

$H_n > 100$ first at $n = e^{100 - \gamma} \approx 1.5 \times 10^{43}$. The observable
universe holds on the order of $10^{80}$ atoms, so the comparison is off by
thirty-seven orders of magnitude in the wrong direction.

**Now:** gives the actual figure, $1.5 \times 10^{43}$, with a time comparison that is
checkable — a trillion terms per second still needs $\approx 5 \times 10^{23}$ years, so it
would not be a millionth done when the sun dies. The 12,367 figure for $H_n > 10$ in the
same sentence was correct and is untouched.

### 2. `2026-07-25-transformations-four-dials.md` — sign error

**Was:** "If your sine version needs $h = \pi/4$, you have understood the quarter-lap
relationship."

For $g(x) = a\sin\big(b(x-h)\big) + k$ with $b = 2$, a peak on the $y$-axis needs
$b(0 - h) = \pi/2$, so $h = -\pi/4$. Setting $h = +\pi/4$ puts a **trough** on the axis.
A student who checked their answer against the dials would have found the graph
contradicting the article.

**Now:** the note derives the sign rather than asserting it, and lands on
$2\sin(2x + \tfrac{\pi}{2}) + 1 = 2\cos(2x) + 1$. This is the one correction I would call a
genuine error rather than a drift.

### 3. `2026-07-30-what-a-p-value-is.md` — editorial comment in published source

An HTML comment beginning `<!-- VERIFY: I have called the one-tail-for-two-sided slip...`
was still in the file. Invisible in the rendered page, visible in View Source. Removed.

### 4. `2026-07-27-conditional-probability-and-the-base-rate.md` — instruction the tool cannot follow

The article note said "set the prevalence to 10%... and at 50% prevalence...". The slider
runs `min=1 max=100` with `prev = value/1000`, so its **maximum is 10%** and 50% is
unreachable. Reworded so the 10% case is a slider action (it is exactly the maximum) and
the 50% case is presented as arithmetic carried past the slider's range. Both figures,
69% and 95%, verified.

### 5. `2026-07-15-which-chi-square-test.md` — CED wording

The revised CED (EK 3.14.D.1) states the three conditions as: randomization — *differently
worded for the two tests* — the 10% condition, and "all expected counts should be **greater
than** 5." The article had a single merged randomization bullet and wrote the count
condition as $E \geq 5$.

Rewritten to match the CED's three-part structure, including the detail that the
randomization condition reads differently for independence than for homogeneity, which is
the same design distinction the article is about. The "at least 5" phrasing is noted as
what older review books say, since students will meet both.

### 6. `2026-07-27-benfords-law.md` — internal contradiction

The article called the first-digit test "exactly the goodness-of-fit machinery of a
statistics course" while the chi-square article correctly teaches that goodness-of-fit was
removed from the revised course. Reworded to name the test, state that the AP course no
longer includes it, and note that the $\sum (O-E)^2/E$ machinery is identical to the
two-way-table tests that stayed. Now cross-links to the chi-square article.

### 7. `2026-07-27-simpsons-paradox.md` — garbled Berkeley sentence

"...individual departments slightly favored women who had applied to the most competitive
programs" reads as a restrictive clause, i.e. that departments favored only that subset.
The actual finding is two separate facts. Rewritten. (`probability-against-intuition.md`
already states it correctly; the two now agree.)

### 8. `2026-07-30-least-squares-regression-influence.md` — orphaned number

"One more reading discipline **while the numbers are in front of you**: $r^2 = 0.842$..."
followed the *two clusters* paragraph, but 0.842 is the **curved** preset's $r^2$; clusters
reads 0.916. A student following along would have seen a different number. Re-anchored to
the curved preset, which also makes the point sharper — 84% of variation "explained" by a
line through a curve.

### Also adjusted (polish, not error)

- `2026-07-25-what-95-percent-confident-means.md`: the worked interval was described as
  "mean amount of sleep... between 47.1 and 54.9 minutes," i.e. students sleeping under an
  hour. Changed to commute time. Separately, the article's simulation uses a $z$-interval
  with known $\sigma$, which is not an AP procedure; the closing note now says so
  explicitly and explains why the simplification is worth making (constant interval width
  is the whole visual argument).
- `2026-07-27-buffons-needle.md`: Buffon posed the problem in 1733 and published his
  solution in 1777. Corrected, and the front-matter description now says "eighteenth
  century" rather than naming a year.

### Noted, not changed

- `2026-07-21-reading-the-graph-of-f-prime.md` carries `interactive: true` in an
  uncommitted working change, but the article's figure is a static SVG with no controls.
  The field is metadata only — nothing in `_layouts/` or `_includes/` reads it — so this is
  a data-integrity question rather than a rendering one. Your call.

---

## Part II — Featured ("big box") articles for AP Calculus

### Two mechanical constraints before the picks

1. **`resources.md` hard-errors on a second `featured: true` in one section.** Lines 97–100
   include the nonexistent `ERROR-two-featured-articles-in-one-section`, which is a
   deliberate loud failure. Adding a second featured calculus article breaks the build
   until that guard is changed.

2. **Featured articles are hoisted to the front of the grid, not left in sequence
   position.** The section loop renders `feats` first, then everything else. So right now
   the FTC box appears first regardless of its `sequence: 21`. To get "roughly equally
   dispersed," the two loops need to become one loop over `items` in sequence order, with
   `featured=true` passed through per item. That is the change that actually produces the
   layout you're describing.

3. Featured boxes render `description` rather than `blurb`, and the
   `featured-description-check` workflow warns outside 90–200 characters. Two of my picks
   need a trim — flagged below.

### The five

Chosen for the intersection of *what students actually get wrong*, *what the exam actually
asks*, and *how much of the rest of the course depends on it*. Sequence positions in
brackets.

| # | Article | Seq | Why it earns the space |
|---|---|---|---|
| 1 | **What a limit claims, and what it does not** | 2 | Everything downstream is a limit. Students who never internalize that the limit ignores the point carry the confusion into differentiability, continuity, and improper integrals — three later articles are written to clean up that specific damage. Best possible opener: it is the article that makes the rest legible. |
| 2 | **The chain rule, layer by layer** | 10 | The most-applied rule in the course, and its failure mode (dropping the inner factor) is the single most common differentiation error on the exam. Five later articles depend on it: implicit differentiation, related rates, inverse derivatives, $u$-substitution, and the parametric second derivative. |
| 3 | **Reading the graph of f′** | 18 | Your own framing: "Every AP Calculus exam contains some version of this question," and "one of the most-missed problem types in the course." Highest single-question frequency on the free-response section. Non-negotiable. |
| 4 | **The Fundamental Theorem of Calculus from first principles** | 21 | Keep. The conceptual keystone, and the existing feature already works. |
| 5 | **Approximation by Taylor polynomials** | 31 | Anchors the BC half, which otherwise has no big box at all. The entire second semester of BC — error bounds, radius of convergence, series manipulation — is this one idea used twelve ways, and it is where BC students most reliably lose the thread. Also gives the section a strong closing box. |

**Dispersion:** 2 / 10 / 18 / 21 / 31 out of 31 articles, i.e. roughly 6%, 32%, 58%, 68%,
100% of the way down the section.

**The one soft spot:** #3 and #4 sit three apart, with only *optimization* and *Riemann
sums* between them. In a three-column grid that is about one row of separation. Two ways
to open it up if the layout looks crowded:

- Swap #3 for **A procedure for related rates** (seq 14), giving 2 / 10 / 14 / 21 / 31.
  Related rates is the topic students name as hardest; reading $f'$ is the topic they
  actually lose points on. I would keep reading $f'$.
- Or run **four** boxes — 2 / 10 / 18 / 31 — and drop the FTC feature. Cleanest spacing,
  but it demotes the best article on the site. I would not.

My recommendation is to keep all five and accept the tighter middle, because #3 and #4 are
the two highest-value articles in the section and the grid can carry it.

**Descriptions needing a trim for the 90–200 window:**

- *Taylor polynomials* is 209 characters. Suggested 178-character replacement:
  > "A polynomial that matches enough derivatives becomes locally indistinguishable from
  > the function it imitates. Where the approximation holds, where it fails, and how the
  > error gets measured."
- *Related rates* is 215, relevant only if you take the swap above.

The other three (182, 188, 153) are already inside the window.

### Implemented 2026-07-31

`resources.md`:

- The two render loops collapsed into one over `items`, so featured articles now sit in
  **sequence position** instead of being hoisted to the front of the grid.
- The build guard raised from `feats.size > 1` to `feats.size > 5`, with the include
  renamed to `ERROR-more-than-five-featured-articles-in-one-section`. The file still does
  not exist; that is the loud-failure mechanism, unchanged.
- A second console editing aid added alongside the description-length one: it warns when
  two featured boxes in a section sit fewer than four cards apart. It fires once on the
  current set, for the 18/21 pair, which is the tradeoff described above made visible in
  your own tooling rather than only in this file.

`_posts/`: `featured: true` added to *what-a-limit-claims*, *chain-rule-reading-the-layers*,
*reading-the-graph-of-f-prime*, and *taylor-polynomials-impersonate-functions*. FTC
unchanged. Taylor's `description` trimmed 209 → 189 characters; all five featured
descriptions are now inside the 90–200 window.

**Two side effects worth knowing about.**

1. **AP Precalculus' featured box moves from first to last.** *The unit circle and the sine
   curve* is `sequence: 4` of 4, so under sequence ordering it now closes the section
   instead of opening it. Nothing is broken, but the anchor effect is gone. If you want a
   big box at the top of that section, *The four parameters of transformation*
   (`sequence: 1`) is the natural pick and would work as a second featured article there.
   AP Statistics is unaffected — its featured article lands eighth of eleven, mid-grid,
   which reads well. Looking ahead is unaffected; its featured article is already first.

2. **The calculus grid picked up two holes, and they are now closed.** A `span 2` card that
   meets the cursor in column three wraps to the next row and leaves an empty cell behind
   it. At 2 / 10 / 18 / 21 / 31 that happened twice, at rows 8 and 12, plus a trailing gap.

   Every gap-free arrangement was enumerated. The cheapest moves one article one position:
   **2 / 10 / 18 / 22 / 31**, reached by swapping the `sequence` values of the FTC article
   (21 → 22) and the accumulation-functions article (22 → 21). The result is exactly 36
   cells in 12 full rows, no holes and no trailing gap, and the closest featured pair goes
   from three cards apart to four, which also clears the dispersion warning.

   The cost is one inversion of College Board topic order — FTC is topic 6.4 and
   accumulation functions are 6.5–6.6, so the dependent article now displays first. It is
   the smallest available disturbance: two articles in the same unit, one topic apart, still
   adjacent on the page and cross-linked, with the FTC card the larger of the two and
   therefore the one the eye reaches first. Every alternative was worse — moving Riemann
   sums or integration by parts across FTC breaks the unit order far more.

   If strict topic order matters more than the feature, the alternative is to leave both
   `sequence` values alone and feature *accumulation functions* instead of *FTC*. That is
   also gap-free and needs no reordering; it just gives the big box to the weaker article.

   The two remaining gaps are trailing cells at the end of AP Precalculus and Looking ahead,
   which are a function of article counts (5 and 10 cells against a 3-column grid) rather
   than of placement. They predate this change and read as the section ending rather than as
   a hole. AP Statistics is exact at 12 cells.

### For AP Statistics, when you get there

For symmetry, the same reasoning applied to the current stats set would give: **What moves
the least-squares line** (seq 1), **Sampling and bias** (3), **The Central Limit Theorem in
simulation** (7), **The meaning of 95% confidence** (9, currently featured), **What a
p-value cannot tell you** (11). That is 1 / 3 / 7 / 9 / 11 out of 12 — bunched at the back, because
Unit 1 and Unit 2 are thin in the current corpus. Proposals 3 and 4 below are the ones
that would fix the spacing as well as the coverage.

---

## Part III — Proposed new articles: AP Statistics

Ranked. Each is a real coverage gap against the revised five-unit CED, not a variation on
something already published.

### S1. Type I errors, Type II errors, and power

**Gap.** The only current treatment is one paragraph inside the p-value article. The CED
gives this its own skill (2.D, "Identify types of errors and relationships among components
in statistical inference methods") and returns to it in Units 3 and 4.

**The misconception.** Students memorize the 2×2 table and cannot say what changes $\beta$.
They believe power is a property of a test rather than a property of a test *at a
particular alternative*, and they think lowering $\alpha$ is free.

**Interactive.** Two overlapping sampling distributions on one axis: the null-centered
curve and a true-parameter curve whose center is draggable. The critical value sits where
$\alpha$ puts it. Shade $\alpha$ on the null curve and $\beta$ on the true curve, with
power $= 1 - \beta$ as the complement, and print all three live. Three controls: drag the
true parameter, set $\alpha$, raise $n$. The payoff is watching each control move a
*different* pair of quantities — raising $n$ narrows both curves and buys power for free,
lowering $\alpha$ buys Type I protection by paying in $\beta$, and moving the truth closer
to $H_0$ destroys power while touching nothing else. The article writes itself off that
picture.

**Sequence:** ~10, between writing parameters and the p-value article.

---

### S2. Which inference procedure?

**Gap.** *Which chi-square test* does this beautifully for two procedures. Nothing does it
across all of them, and CED skill 2.C is literally "Identify appropriate statistical
inference methods."

**The misconception.** Students who can execute every procedure still pick the wrong one
under time pressure. The three decisions — categorical or quantitative, one sample or two,
paired or independent — are each easy; making all three from a paragraph is not.

**Interactive.** Same shape as the *derivative rules* classification drill, which is the
best-designed interactive on the site and deserves a statistics twin. A stem appears; four
buttons; feedback names the feature of the *design* that settles it, never the arithmetic.
Twelve stems, deliberately including the pairs that look alike: two independent samples of
students versus the same students measured twice; a two-way table from one sample versus
the same table from two; a proportion question phrased with counts.

**Sequence:** ~13, closing the inference run.

---

### S3. Describing a distribution in the exam's own words

**Gap.** The largest one in the corpus. Unit 1 is **20–30% of the exam** and the current set
covers only sampling and bias. Nothing on shape/center/spread/unusual features, nothing on
resistance, nothing on the $1.5 \times \text{IQR}$ rule, nothing on comparative language.

**The misconception.** Students describe one distribution when asked to compare two, omit
context, and choose mean-and-SD for a skewed distribution because those are the buttons
they know. The exam's phrasing — *compare*, not *describe* — is a scoring distinction
students lose points to every year.

**Interactive.** A dotplot whose points are draggable, with four linked readouts updating
live: mean and median (with the mean visibly chasing a dragged outlier while the median
sits still), SD and IQR, a boxplot with the $1.5 \times \text{IQR}$ fences drawn as actual
lines so a point crossing one flips from whisker to outlier marker in front of you, and a
running sentence stub. Second mode: two distributions side by side with a comparative
sentence builder. The resistance demonstration is the whole article and it is one drag
long.

**Sequence:** ~1, which also fixes the front-loading problem noted in Part II.

---

### S4. Combining random variables: means add, standard deviations do not

**Gap.** Unit 2 topics 2.8–2.9 have no article. This result is the hinge every two-sample
standard error in Units 3 and 4 swings on, and it is currently assumed rather than argued.

**The misconception.** Two of them, and the second is worse. Students add standard
deviations instead of variances. And when the question asks for a *difference*, they
subtract the variances — where the correct move is to add them, because independent
variability accumulates no matter which direction you combine in. That sign is the single
most counterintuitive fact in the probability unit.

**Interactive.** Two random variables with adjustable means and SDs. A simulation builds
the distribution of $X + Y$ and of $X - Y$ side by side. Next to each, three bars: the
true SD, the (wrong) sum of the SDs, and $\sqrt{\sigma_X^2 + \sigma_Y^2}$ — with the third
landing on the simulated value and the second overshooting visibly. A toggle for
*independent / not independent* that shows the whole result collapsing when independence
fails, since that hypothesis is the one students never check.

**Sequence:** ~6, before the CLT article, which needs this result.

---

### S5. One template for every confidence interval

**Gap.** The corpus teaches the individual procedures well but never says out loud that
there are only two templates.

**The idea.** Every confidence interval in the course is
$\text{estimate} \pm (\text{critical value})(\text{standard error})$, and every test
statistic is $(\text{estimate} - \text{null})/(\text{standard error})$. Six procedures,
two shapes, and the only thing that varies is which standard error and which reference
curve.

**Interactive.** A formula builder. Choose a procedure and watch the template populate,
with the piece that changed relative to the previous procedure highlighted. The point is
made by what *doesn't* move: the skeleton is identical from a one-proportion $z$-interval
to a two-sample $t$-interval, and students who see that stop memorizing six formulas.

**Sequence:** ~9, as the on-ramp to the whole inference sequence.

**If you build three, build S1, S3, and S2, in that order** — S1 is the biggest
conceptual gap, S3 the biggest coverage gap, S2 the biggest exam-day gap.

---

## Part IV — Proposed new articles: AP Precalculus

Only four precalc articles exist, and all of them serve Units 2 and 3. **Unit 1 is 30–40%
of the exam and has no coverage at all.** Both proposals below are Unit 1.

### P1. What the factored form tells you

**Gap.** Polynomial and rational functions, the largest single block of the course, entirely
uncovered.

**The misconception.** Students treat "find the zeros," "describe the end behavior," and
"find the asymptotes" as three unrelated procedures. They are three readings of one
factored expression. The specific confusions worth building the article around: a repeated
factor makes the graph *bounce* rather than cross, and an odd multiplicity above 1 makes it
*flatten* through; a common factor top and bottom is a **hole**, not a vertical asymptote,
and the graph is otherwise unchanged; and the three horizontal-asymptote cases are a degree
comparison, which is exactly the calculus article on limits at infinity arriving three
years early.

**Interactive.** A factored-form builder. Drag zeros along the $x$-axis; click a zero to
cycle its multiplicity 1 → 2 → 3; watch the curve cross, bounce, or flatten while the
expanded form, the degree, and the end-behavior statement update live. Second mode adds a
denominator: drag a denominator root onto a numerator root and watch the vertical asymptote
become a hole in one motion. That single drag is the article's best twelve seconds.

**Cross-course value:** the end-behavior half is a direct on-ramp to
`limits-at-infinity.md`, and the "bounce versus cross" half is the sign-chart reasoning
that Calculus Unit 5 assumes students already own.

---

### P2. Increasing at a decreasing rate

**Gap.** Topics 1.1–1.3, and the content that most distinguishes AP Precalculus from the
precalculus course it replaced.

**The misconception.** "Increasing at a decreasing rate" is the phrase students cannot
produce and cannot parse. They collapse it to "decreasing." Reading concavity from a table
of *successive average rates of change* — rather than from a picture — is the specific skill
the exam tests and the specific skill nobody practices.

**Interactive.** A curve with a table beneath it. The table shows equally spaced inputs,
the outputs, and the successive average rates of change in a third column, with the
*differences of those rates* in a fourth. Four preset curves covering the four
combinations: increasing at an increasing rate, increasing at a decreasing rate, and their
decreasing counterparts. A draggable secant pair on the curve stays linked to the
highlighted table row, so the number in the third column is visibly the slope of the drawn
segment. A sentence stub assembles from the two signs — one from the third column, one from
the fourth — and that assembly *is* the exam's answer.

**Cross-course value:** this is the most direct bridge on the site into
`derivative-as-a-limit.md`. The third column is the difference quotient before it has a
name; the fourth is the second derivative. A student who reads this article and then that
one has met the derivative twice before it is defined.

**If you build one, build P2** — it is the better article and the better bridge. **If you
build for coverage, build P1 first** — 30–40% of the exam with nothing on it is the more
urgent hole. Ideally both, P1 then P2, since P1 sets up the sign-reasoning P2 uses.

*Third option if you want one more:* **model selection from data** (topics 2.13–2.15) —
linear vs quadratic vs exponential vs logarithmic, and the semi-log plot that turns an
exponential into a line. Distinctive to AP Precalculus, and it would pair naturally with
the existing logarithms article.

---

## Part V — Beyond the course material

You asked specifically for enrichment with strong visualization. Ranked by visual payoff
per unit of prerequisite. The first two are already set up by articles you have published —
each one answers a question an existing article explicitly poses and leaves open.

### B1. The logistic map: from order into chaos

**Why this one first.** Two of your articles already point at it. *Logistic growth* teaches
$\frac{dy}{dt} = ky(a-y)$ and its placid S-curve; *After BC: differential equations* ends on
Lorenz and chaos without connecting the two. The connection is that the *discrete* logistic
map $x_{n+1} = rx_n(1 - x_n)$ — the same equation, stepped instead of flowed — does not
behave placidly at all. It settles, then oscillates between two values, then four, then
eight, and then goes chaotic, all as one parameter is turned. A student who has just spent
a week on logistic growth meeting this is the best payoff-to-setup ratio available.

**Interactive.** Two linked panels. Left: a cobweb plot for the current $r$, with the
staircase visibly converging, cycling, or filling the square. Right: the bifurcation
diagram, with a marker at the current $r$ sliding along the branching cascade. Drag $r$ from
2.5 to 4 and watch the left panel's behavior and the right panel's structure explain each
other. Add a zoom on the diagram to show the cascade repeating inside itself.

**The idea to land:** determinism and predictability are different things, and the boundary
between them is one slider wide. Feigenbaum's constant is right there if you want it.

**Courses:** BC primarily; accessible to Precalculus students who have iterated a function.

---

### B2. The Mandelbrot set: what Newton's method was pointing at

**Why.** Your Newton's method article ends by naming Julia sets and Cayley's 1879 failure,
and the Taylor article ends with "where is the wall? Hint: try $x = i$." Both are pointing
at the same place and neither goes there. This is the article that collects the debt.

**Interactive.** Escape-time rendering with zoom, on canvas. Click a point $c$ to show the
orbit of $0$ under $z \mapsto z^2 + c$ in a side panel — bounded (in the set) or escaping
(out) — so the picture is visibly a *record of a calculation* rather than a decoration.
Then the payoff: overlay the disk $|x| < 1$ on the real axis and show that the radius of
convergence of $\frac{1}{1+x^2}$ is set by singularities at $\pm i$, off the real line
entirely. The two puzzles close together.

**Courses:** BC; Precalculus students can operate it without the series half.

---

### B3. Why the bell curve is the shape it is

**Why.** Statistics students use $e^{-x^2/2}$ for a year without ever being told where it
came from, and your multivariable article already mentions the punchline —
$\int_{-\infty}^{\infty} e^{-x^2}dx = \sqrt{\pi}$, falling out in three lines once you square
it and switch to polar coordinates, and being the reason $\sqrt{2\pi}$ sits in the normal
density. That is a loop worth closing for the students taking both courses.

**Interactive.** The polar trick, animated: the square of the one-dimensional integral drawn
as a solid of revolution over the plane, then re-sliced into annuli, with the substitution
$u = r^2$ collapsing it. Alongside, a de Moivre–Laplace panel — a binomial histogram with
draggable $n$ and $p$, and the normal curve drawn over it, snapping into agreement as $n$
grows. Two independent routes to the same curve, which is the honest reason it is
everywhere.

**Courses:** Statistics + BC. This is the strongest cross-course article available.

---

### B4. How Google was built on an eigenvector

**Why.** Teased in *After AP Statistics*, and it is the one enrichment topic that reaches
all three courses: Precalculus already teaches transition matrices (topic 4.14, unassessed),
Statistics has conditional probability, and the linear algebra article already frames
PageRank as an eigenvector.

**Interactive.** A small graph — five or six nodes — with editable transition probabilities.
A random walker moves through it, leaving a running histogram of visit frequencies that
converges to the stationary distribution. Then reveal that the same vector is the
eigenvector of the transition matrix, and that ranking the nodes by it *is* PageRank.
Adding a link and watching the ranking reshuffle is the demonstration that sells it.

**Courses:** all three.

---

### B5. A curve that fills a square

*Added 2026-07-31 at Katherine's request. My original objection — that no published article
sets it up — was wrong, and the setup is better than the one I was looking for.*

**Why it works after all.** The Riemann sums article already teaches that a limit of
approximations can be a different kind of object from any of the approximations, and the
harmonic series article already teaches that infinity does not respect intuitions built on
finite cases. A space-filling curve is those two lessons collided. Every stage of Hilbert's
construction is an ordinary polygonal path with an ordinary length; the limit passes through
every point of a square.

**The misconception.** That a curve is one-dimensional because it is drawn with one
parameter. Dimension is not a count of parameters, and the failure of that intuition is what
forced mathematics to define dimension carefully in the first place. Peano's curve of 1890
is the reason the definition exists.

**Interactive.** One canvas, one slider: the Hilbert curve at order 1 through 7, drawn as a
continuous path with a moving dot tracing it. Two live readouts alongside — path length,
which doubles-and-a-bit at every order, and the largest gap between the curve and any point
of the square, which halves. Push the slider up and the two numbers run in opposite
directions, one to infinity and one to zero, which is the whole theorem in two columns.
A second mode overlays the order-*n* and order-*(n+1)* curves so the recursive replacement
is visible as a rule rather than as a picture.

**The idea to land.** Length and dimension are different questions, and a limit can change
the answer to the second while sending the answer to the first to infinity. Then the payoff:
this is not a curiosity. Hilbert curves are how image and database systems flatten two
dimensional data into one dimension while keeping nearby things near, which is a real
engineering technique built on a nineteenth-century monster.

**Courses:** BC primarily; Precalculus students can operate the slider and read both
numbers without the limit argument.

---

### B6. The map that preserves angles

*Added 2026-07-31 at Katherine's request. I had set this aside for steep prerequisites,
which stands — so the article should be built to need none of them.*

**The honest problem.** Conformal mapping properly belongs to complex analysis, two courses
past BC. Written at that level it would be the only article on the site a reader cannot
follow. So the article has to be built around what can be *seen* rather than what can be
proved, and it should say so in the opening rather than pretending otherwise.

**What survives the demotion.** Take the plane, apply $$z \mapsto z^2$$, and watch a grid.
Squares become curved quadrilaterals, areas stretch and shrink wildly, and yet every place
two grid lines crossed at a right angle, the images still cross at a right angle. That
observation needs no theory. It needs a grid and a slider.

**The link back.** The [linear algebra preview](/2026/07/26/linear-algebra-preview.html)
already teaches a matrix as a motion of the plane, with the determinant as the area factor.
This is the same question asked of a curved motion instead of a straight one, and the answer
is that the local behaviour of a complex differentiable map is a rotation and a scaling —
a matrix, at every point, varying from point to point. The article can make that sentence
land without proving it.

**Interactive.** A grid on the left, its image on the right, with a slider morphing
continuously from the identity to the chosen map so the deformation is watchable rather than
inferred. Four maps: $$z^2$$, $$1/z$$, $$e^z$$, and a Möbius map. A draggable crosshair on
the source grid puts a small right-angle marker at its image, and a readout gives the local
rotation and the local scale factor. The demonstration is that the marker stays a right
angle everywhere except where the readout reports a scale factor of zero — the one point
where the map is not conformal, which the reader can hunt for.

**The idea to land.** Angles and areas are independent properties of a transformation, and
there is an entire class of maps that abandons the second to protect the first. Then the
application: this is why the Mercator projection looks the way it does, and why every
navigational chart before satellites was a conformal map. Preserving angles is what lets a
compass bearing be a straight line.

**Courses:** BC and Precalculus. Deliberately proof-free.

---

### B7. Information, measured

*Added 2026-07-31 at Katherine's request. My original note said this wants a sequence rather
than one article. Having spent longer on it, one article is right — but it has to be the
right one, and the right one is not "here is the entropy formula".*

**Why one article.** The temptation is to cover entropy, coding, compression, and channel
capacity, which is a course. The single idea underneath all four is worth an article on its
own: the amount of information in an answer is the number of yes-or-no questions it saves
you, and that number is a logarithm. Everything else is application.

**The hook.** Twenty questions, played properly. If a set of $$2^{20}$$ possibilities can be
cut in half by each question, twenty questions suffice — so the information in an answer
drawn from that set is 20 bits, and the logarithm has appeared without being introduced.
Then the turn that makes it statistics rather than arithmetic: this only works when the
possibilities are equally likely. When they are not, a well-chosen question can do better
than halving, and the average number of questions needed drops below $$\log_2 n$$. Entropy is
exactly that average, minimised over all questioning strategies.

**The link back.** [Benford's law](/2026/07/27/benfords-law.html) is the natural companion
and already on the site — a distribution over nine digits that is provably not uniform, so
its entropy is below $$\log_2 9$$, and the shortfall is precisely why first-digit tests carry
information about fraud. The connection is real rather than decorative: a Benford
distribution carries about 2.88 bits against a uniform digit's 3.17, and that gap is what an
auditor is exploiting.

**Interactive.** A set of outcomes with draggable probabilities, held normalised. Three
things update: the entropy in bits, a live optimal question tree (the Huffman code, redrawn
as the bars move), and the average questions per outcome that the tree achieves. Drag toward
uniform and entropy climbs to its maximum while the tree becomes balanced; drag toward
certainty and both collapse toward zero. Preset buttons for a fair coin, a loaded die,
English letter frequencies, and Benford's digits.

**The idea to land.** Uncertainty is measurable, its unit is the bit, and the measurement is
a logarithm because questions compose multiplicatively while information adds. Shannon
published this in 1948, and it is the reason a compressed file has a size floor that no
algorithm will ever beat.

**Courses:** Statistics primarily, with a foot in Precalculus through logarithms.
The strongest cross-link on the enrichment roster after B3.

---

## Part VI — Title renames, 2026-07-31

### The tic

Fifteen of the fifty-five titles ran "*X*, and *the thing that Y*" — a headline followed by
an appendix clause. Underneath it was a narrower habit: nine titles ended in *the [noun]
that [verbs]* — the algebra that resolves them, the ways it fails, the two signs that decide
everything, the step that is not calculus, the check that catches both, the exponent that
decides. Individually each is fine. Fifty-five titles deep it reads as a formula, and a
formula is the opposite of the effect the construction is going for.

**Titles are cosmetic here — URLs come from filenames, not titles.** Nothing breaks.
I checked every internal cross-reference: the articles link to each other through
descriptive phrases ("a vertical asymptote", "the derivative at a point is a limit"), never
by quoting a title, so no prose needed touching.

### Kept (3)

The construction earns its keep when the second clause *is* the thesis rather than an
afterthought — when it reverses, withholds, or surprises.

| Title | Why it survives |
|---|---|
| **What a limit claims, and what it does not** | The antithesis is the article. A limit's silence about the point is the whole idea, and the title enacts it. Also the featured opener of the section. |
| **Two existence theorems, and what they refuse to tell you** | *Refuse* is doing real work. The article is about what the theorems decline to say, and no shorter title carries that. |
| **Optimization, and the step that is not calculus** | The clause is a genuine surprise in a calculus article, which is the hook. |

### Renamed (11)

| Was | Now |
|---|---|
| Continuity's three conditions, and the ways it fails | **Breaking continuity one condition at a time** |
| The Intermediate Value Theorem and how to invoke it | **Invoking the Intermediate Value Theorem** |
| The rules, and choosing among them | **Choosing a differentiation rule** |
| The chain rule and reading the layers | **The chain rule, layer by layer** |
| Particle motion, and the two signs that decide everything | **Why negative acceleration is not slowing down** |
| Linearization, and whether the answer is too big | **Over or under: reading a linearization** |
| L'Hospital's rule, and the step before it | **Checking the form before L'Hospital's rule** |
| Integration by parts, partial fractions, and the check that catches both | **Integration by parts and partial fractions** |
| Improper integrals, and the exponent that decides | **When an unbounded region has finite area** |
| Area between curves, and the average value of a function | **Area between curves and average value** |
| What a p-value is, and what it is not | **What a p-value cannot tell you** |

Notes on three of the choices:

- *Choosing a differentiation rule* now rhymes deliberately with the existing *Choosing a
  convergence test*. Both articles are about selection rather than execution, and the
  parallel says so.
- *Why negative acceleration is not slowing down* promotes the old blurb into the title,
  because the misconception is a better hook than the topic name. Its blurb was rewritten
  to avoid repeating itself.
- *What a p-value is, and what it is not* was the strongest instance of the pattern and also
  the most conspicuous echo, since *What a limit claims, and what it does not* is the same
  sentence in a different course. Keeping both would have made the tic visible from the
  index page. The limit one is the more original phrasing, so the p-value one moved.

Three blurbs were rewritten where the new title had made them redundant:
`continuity-three-conditions`, `particle-motion`, `lhospitals-rule`.

### Proposal titles in Parts III–V

Rewritten under the same rule before any of them get built, so the habit does not come back
with the next batch: *Type I errors, Type II errors, and power*; *Which inference
procedure?*; *Describing a distribution in the exam's own words*; *One template for every
confidence interval*; *What the factored form tells you*; *Increasing at a decreasing rate*;
*The logistic map: from order into chaos*; *How Google was built on an eigenvector*.

*Increasing at a decreasing rate* is the best of them — it is the exact phrase students
cannot parse, so the title is the diagnostic.

---

## Appendix — What was verified

Spot list of the non-obvious claims recomputed independently and confirmed correct:

- $x^{100}/e^x$ peaks at $x = 100$ at $\approx 3.7 \times 10^{156}$ and falls below 1 near
  $x = 647$ (`limits-at-infinity`)
- Folium denominator vanishes at $(2^{5/3}, 2^{4/3}) \approx (3.1748, 2.5198)$, and that
  point is on the curve (`implicit-differentiation`)
- Linearization errors 0.0000388 / 0.000154 / 0.000610 at $x = 4.05, 4.1, 4.2$, and the
  next Taylor term predicting 0.00015625 against a true 0.00015433 (`linearization`)
- MVT points at $(3\pm\sqrt3)/2$ and $3/2 \pm \sqrt{15}/6$, and that the modified cubic has
  infimum 0 unattained on $(0,3]$ (`mean-value-and-extreme-value-theorems`)
- Piecewise-linear integrand crossings, corner slopes, and $g(3.5) = 17/4$ with the three
  linear pieces contributing $2$, $0$, $-3$ (`accumulation-functions`)
- Cardioid area $3\pi/2$, rose area $\pi$, cardioid arc length exactly 8, and
  $d^2y/dx^2 = -9/y^3$ agreeing with implicit differentiation (`parametric-vector-polar`)
- $\int_0^{\pi} x\sin x\,dx = \pi$ from *both* the correct and the faulty antiderivative,
  and the two separating to $\pm 1$ at $\pi/2$ (`parts-and-partial-fractions`)
- All five regression presets: $r = 0.918$ (curved), $r = 0.957$ (clusters), slope 0.399
  vs 0.025 with and without the influential point, $s = 8.41$, and that the outlier's slope
  sensitivity $(x_i - \bar{x})/S_{xx} = 0.00026$ really is "the third decimal place"
  (`least-squares-regression-influence`)
- $P(-1.96 < T_{10} < 1.96) = 0.9216$ and $P(-1.96 < T_{300} < 1.96) = 0.9491$
  (`distribution-explorer`)
- p-values 0.6171 / 0.3173 / 0.0455 at $n = 25, 100, 400$, and that the two-sided $p = 0.05$
  boundary at 53.92 is exactly where the 95% interval's lower end hits 50.00
  (`what-a-p-value-is`)
- Charig kidney-stone rates 78/83, 93/87, 73/69, and the historical case mix
  $263/343 = 77\%$ (`simpsons-paradox`)
- Birthday probabilities 0.493 at $n=23$, 6% for a match to *your* birthday, and
  $\binom{23}{2} = 253$ (`probability-against-intuition`)
- All nine Benford proportions to three decimals (`benfords-law`)
