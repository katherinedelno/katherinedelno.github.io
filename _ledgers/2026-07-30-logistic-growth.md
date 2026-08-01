# Claims ledger — Logistic growth, read without solving it

Article: `_posts/2026-07-30-logistic-growth.md`
Session: 7D article 20, 2026-07-30. AP Calculus **BC only**, sequence 26, Unit 7 topic 7.9.

Verification: `t.js` loads the shipped script in jsdom with a stubbed canvas context and sweeps a
grid of $(y_0, k)$ pairs — 71 by 23, 1633 combinations — comparing the tool's Runge–Kutta result
against the closed-form solution, which the tool itself never uses. Symbolic results from SymPy.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **FUN-7.H.1**, quoted almost in full in the opening: the model "arises from the
statement 'The rate of change of a quantity is jointly proportional to the size of the quantity
and the difference between the quantity and the carrying capacity'" and is
$\frac{dy}{dt} = ky(a-y)$. The article builds the equation from that sentence rather than
presenting it as given, which is what the framework does.

`[EXAM]` **FUN-7.H.2**, which is the article's thesis and its title: "The logistic differential
equation and initial conditions can be interpreted **without solving** the differential
equation."

`[EXAM]` **FUN-7.H.3**: the carrying capacity "as the independent variable approaches infinity
can be determined using the logistic growth model and initial conditions."

`[EXAM]` **FUN-7.H.4**: "The value of the dependent variable in a logistic differential equation
at the point when it is **changing fastest** can be determined using the logistic growth model
and initial conditions." Those two — capacity and fastest-change value — are the only two
quantities the framework names, which is why the article treats them as the whole topic.

`[EXAM]` **Topic 7.9's suggested skill is 3.F**, "Explain the meaning of mathematical solutions
in context" — the last section, which is written as three sentences about fish rather than as
algebra. Learning objective FUN-7.H is "Interpret the meaning of the logistic growth model in
context", marked bc only.

`[EXAM]` **Relevant to Unit 7 generally, from the fall 2026 corrections:** FUN-7.B.2 now reads
"There may be infinitely many solutions to a differential equation." Not quoted in this article,
but it is the unit the correction lands in, and it will matter for any future slope-field or
general-solution article.

## Computed results

`[COMPUTED]` **The closed form is a solution, and the tool does not use it.** SymPy confirms that
$y = \frac{a y_0}{y_0 + (a-y_0)e^{-akt}}$ satisfies $\frac{dy}{dt} = ky(a-y)$ exactly, has
$y(0) = y_0$, and tends to $a$. The interactive integrates the differential equation by classical
fourth-order Runge–Kutta instead. Across 1633 $(y_0, k)$ pairs the two agree to a worst relative
gap of $1.5\times10^{-5}$ at $t = 5$, which is the panel's displayed precision.

`[COMPUTED]` **Both facts the framework asks for, derived from the right-hand side alone.**
$ky(a-y) = 0$ exactly at $y = 0$ and $y = a$, so those are the constant solutions. The rate, as a
function of $y$, has derivative $k(a - 2y)$, zero at $y = a/2$, and its value there is
$\frac{ka^2}{4}$. Both from SymPy, and neither requires the solution.

`[COMPUTED]` **The second derivative, by the chain rule on the equation.** Substituting
$\frac{dy}{dt} = ky(a-y)$ into $\frac{d}{dt}[ky(a-y)]$ gives $k^2 y(a-y)(a-2y)$, which SymPy
returns in exactly that factored form. Its zeros in $y$ are $0$, $a/2$, and $a$, and for
$0 < y < a$ its sign is the sign of $a - 2y$. Checked numerically in the harness: positive at
$y = 10, 30, 49$; negative at $y = 51, 70, 99$; exactly zero at $0, 50, 100$.

`[COMPUTED]` **The worked instance, $a = 100$, $k = 0.02$, $y_0 = 10$**, read from the running
panel: $\frac{dy}{dt}(0) = 18$; fastest growth at $y = 50$ with rate $\frac{ka^2}{4} = 50$;
$y(5) = 99.9592$, matching the closed form to four decimals. SymPy also gives the time at which
$y$ reaches 50 as exactly $\ln 3 \approx 1.0986$ — deliberately not in the article, because that
is the question the framework does not ask.

`[COMPUTED]` **The equilibria behave as constants.** With $y_0 = 0$ the tool returns $y(5) = 0$;
with $y_0 = 100$ it returns exactly 100; the rate reads 0 in both cases and the panel names them
equilibria. Starting at $y_0 = 150$, the rate is negative and $y(5) = 100.0015$, matching the
closed form to six figures — the approach from above.

`[COMPUTED]` **Neither key value depends on $k$ or $y_0$.** Sweeping 30 values of $k$ against 13
of $y_0$, the fastest-growth row read exactly 50 every time — a single distinct value across all
390 combinations. And the maximum rate equalled $ka^2/4$ at all 172 sampled values of $k$, with
no exceptions.

`[COMPUTED]` **The two misreadings named in the third paragraph.** $\frac{dy}{dt} = ky + (a-y)$
with $k = 0.02$, $a = 100$ has its only equilibrium at $y = \frac{5000}{49} \approx 102.04$ —
neither 0 nor 100. $\frac{dy}{dt} = k(a-y)$ has exactly one equilibrium, at $y = a$, and its
derivative with respect to $y$ is the constant $-k$, so it has no inflection and no S-shape.
Logistic has exactly two equilibria. All three confirmed in SymPy.

`[COMPUTED]` **The closing note's expanded form.** $0.5y - 0.001y^2$ and $0.001y(500-y)$ agree at
$y = 0, 100, 250, 500, 700$. Capacity 500, peak growth at 250, rate $0.001 \cdot 500^2/4 = 62.5$,
which also equals the expanded expression evaluated at 250.

`[COMPUTED]` **Slider resolution.** $y_0$ runs 0 to 160 in 1200 steps and $k$ runs 0 to 0.06 in
1200 steps, so $y_0 = 10, 50, 100, 150$ land on positions 75, 375, 750, 1125 and $k = 0.02$ on
400. All verified from the panel.

## Judgment claims

`[JUDGMENT]` "Exponential growth assumes nothing ever runs out." A framing sentence.

`[JUDGMENT]` "That is the method, not a fallback." An interpretation of FUN-7.H.2's placement as
essential knowledge rather than as a remark.

`[JUDGMENT]` "Reading a capacity off an unfactored equation is the most common way to lose the
point." A frequency claim I cannot source. The mechanism is demonstrated with real numbers, and
the sentence would survive being softened if you would rather it were.

---

## Flags raised in this session

1. **The interactive deliberately refuses the closed form.** FUN-7.H.2 says the model can be
   interpreted without solving it, so a tool that plotted the analytic solution would be teaching
   against the topic. Every curve comes from Runge–Kutta on $\frac{dy}{dt} = ky(a-y)$. The closed
   form appears only in the test harness, as the independent check — which is the right place for
   it, and gives a stronger verification than a self-consistency check would.

2. **Three headings and 693 words on the first pass**, below the corpus median of four headings
   and near the bottom of the length target. Added a section on translating the framework's
   sentence into the equation, including the two misreadings — both of which are now computed
   rather than asserted, and the second of which turns out to be Newton's law of cooling. That
   brought it to 911 words and four headings.

3. **Two run-in bold labels, which are within convention.** The style sheet permits bold at the
   head of a paragraph as a structural label — 46 of them across the corpus — while forbidding
   bold inside a sentence. `**The carrying capacity.**` and `**Where growth is fastest.**` are
   the permitted kind. Flagging it because my own audit script's mid-sentence regex spans the gap
   between two adjacent labels and reports a false positive; that is a bug in my checker, not in
   the article, and I have noted it rather than silently ignoring the warning.

4. **911 words**, four `##` headings, one italicised span, three cross-links, all resolving.
   Inside the 650–950 target.

5. **One computed value withheld from the article on purpose.** SymPy gives the time at which the
   worked population reaches half capacity as exactly $\ln 3$. It is a pretty number and it is
   tempting, but getting it requires the solution the topic is built on not needing, so it stays
   in this ledger. The article says instead that the timing is the one question the exam does not
   ask, which is the honest version.

6. **Unit 7 status.** This covers 7.9. Your Euler's method article covers 7.5 at sequence 25.
   Topics 7.1–7.4 (slope fields, reasoning from them, general and particular solutions), 7.6–7.7
   (separation of variables), and 7.8 (exponential models) have no articles. Separation of
   variables in particular is assumed by nothing yet but is the mechanical heart of the unit, and
   it is not in the approved plan.
