# Claims ledger — The Intermediate Value Theorem and how to invoke it

Article: `_posts/2026-07-30-intermediate-value-theorem.md`
Session: 7D article 5 (tier 1, final), 2026-07-30. AP Calculus sequence 6, Unit 1.

Verification: `t.js` loads the shipped script in jsdom, drives both modes across the target
range, and reads the hypothesis checklist, the verdict, and the crossing list back out of the
running tool.

---

## Framework grounding

`[EXAM]` The organising idea, quoted from enduring understanding FUN-1 (topic 1.16):
"Existence theorems allow us to draw conclusions about a function's behavior on an interval
without precisely locating that behavior." This is the article's opening sentence and its
thesis.

`[EXAM]` The statement, quoted from FUN-1.A.1: "If $f$ is a continuous function on the
closed interval $[a, b]$ and $d$ is a number between $f(a)$ and $f(b)$, then the Intermediate
Value Theorem guarantees that there is at least one number $c$ between $a$ and $b$, such that
$f(c) = d$." The article reproduces this in full rather than paraphrasing, because every
clause is load-bearing.

`[EXAM]` The learning objective is FUN-1.A, "Explain the behavior of a function on an
interval using the Intermediate Value Theorem", and the suggested skill is 3.E, "Provide
reasons or rationales for solutions or conclusions." The article's claim that "the writing is
the assessed part" rests on that pairing, which is as direct as the framework gets.

`[EXAM]` Continuity of polynomials, from LIM-2.B.2, used in the model sentence and linked to
the continuity article.

## Computed results

All read out of the shipped tool.

`[COMPUTED]` The continuous function is $f(x) = x^3 - 6x^2 + 9x + 1$ on $[0,4]$, with
$f(0) = 1$, $f(1) = 5$, $f(3) = 1$, $f(4) = 5$. Its derivative $3(x-1)(x-3)$ gives a local
maximum of 5 at $x = 1$ and a local minimum of 1 at $x = 3$, so its range on $[0,4]$ is
exactly $[1,5]$.

`[COMPUTED]` At $d = 3$ there are three crossings, at $x = 2-\sqrt{3}$, $x = 2$, and
$x = 2+\sqrt{3}$. The tool reports 0.2679, 2.0000, 3.7321; the exact values come from
$x^3-6x^2+9x-2 = (x-2)(x^2-4x+1)$. Each matched to within $5\times10^{-4}$.

`[COMPUTED]` Three crossings occur for every target strictly between 1 and 5. Checked at
$d = 1.5, 2, 2.5, 3, 3.5, 4, 4.5$; all report 3.

`[COMPUTED]` Outside the bracket there are none: $d = 5.5$ and $d = 0.5$ both report zero
crossings, and the first hypothesis still passes while the second fails. This is the case the
article uses to separate "the theorem does not apply" from "no crossing exists".

`[COMPUTED]` The jump function is $h(x) = 1+x$ on $[0,2)$ and $0.5x+3$ on $[2,4]$, chosen so
that $h(0) = 1$ and $h(4) = 5$ match the continuous case exactly. The left piece has range
$[1,3)$ and the right $[4,5]$, so every value in $[3,4)$ is skipped. At $d = 3.5$ the tool
reports: continuity fails, the bracket holds, the theorem does not apply, and there is no
crossing.

`[COMPUTED]` The closing note's drag. Sweeping the target from 2 to 5 in jump mode, the
crossing count reads `1111111111000000000011111111111` — one, then none, then one again —
while the verdict is "does not apply" at every point.

`[STANDARD]` A cubic with distinct local extrema takes every value strictly between its local
minimum and local maximum three times on an interval containing both, which is why the
continuous mode shows three crossings throughout the bracket.

## Judgment claims

`[JUDGMENT]` The two failures worth naming are skipping the continuity step and overclaiming
in the conclusion. Teaching observation. The first is supported indirectly: the framework
pairs this topic with skill 3.C elsewhere in Unit 1 ("Confirm whether hypotheses or
conditions of a selected definition, theorem, or test have been satisfied"), though topic
1.16 itself lists 3.E.

`[JUDGMENT]` "A conclusion that locates something is not a conclusion the theorem supports."
This is a mathematical claim rather than a judgment, and it follows from FUN-1's own wording
about not precisely locating behaviour.

---

## Flags raised in this session

1. **Tangencies are invisible to the crossing detector.** The tool finds crossings by sign
   change, so at $d = 1$ and $d = 5$ — where the target sits exactly at a turning value and
   the curve touches without crossing — it under-reports. A first draft of the closing note
   asked the reader to find the targets with exactly two crossings, which are precisely those
   two values, and the tool would have shown one. The note was rewritten around the jump
   mode instead, which is robust. The limitation remains in the tool and is worth knowing
   before you build a lesson on those two values.

2. **Strict versus inclusive "between".** The framework says $d$ is "a number between $f(a)$
   and $f(b)$" without settling whether the endpoints count. The tool requires strict
   betweenness, so at $d = 1$ or $d = 5$ exactly it reports that the theorem does not apply,
   even though a crossing plainly exists at an endpoint. Defensible, and it keeps the
   hypothesis check clean, but a student who drags to exactly 5 will see something that
   deserves a word from you.

3. **My test was wrong before the article was.** Two apparent failures in the first run were
   a regex in the test harness breaking on decimal points — `[^.]+` stopping at the "." in
   "0.2679" — not errors in the tool, which had reported the three crossings correctly all
   along. Worth recording because it is the opposite of the usual failure mode this session,
   where the harness caught the article.

4. **Tier 1 is complete.** Unit 1 now holds sequences 2 through 6: limits, indeterminate
   forms, continuity, end behaviour, and this. The five together cover topics 1.2 through
   1.16 with the exception of estimating limits from tables and graphs (1.3, 1.4) and the
   squeeze theorem's own topic number, which is folded into the indeterminate forms article
   because the framework files it under the same objective.
