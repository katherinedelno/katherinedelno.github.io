# Claims ledger — What a limit claims, and what it does not

Article: `_posts/2026-07-30-what-a-limit-claims.md`
Session: 7D article 1 (tier 1), 2026-07-30. AP Calculus sequence 2, Unit 1.

Verification: `t.js` loads the article's own `<script>` into jsdom and drives every control,
reading the output-bar height back out of the running readout rather than recomputing it.

---

## The mathematics

`[COMPUTED]` $\dfrac{x^2-4}{x-2} = x+2$ for $x \neq 2$, since $x^2 - 4 = (x-2)(x+2)$. At
$x = 2$ the formula is $0/0$ and defines nothing.

`[COMPUTED]` Output-bar heights for the hole, read off the shipped code:

```
  delta = 1        height 1.9995
  delta = 0.1      height 0.2000
  delta = 0.01     height 0.0200
  delta = 0.0001   height 0.0002
```

The prose cites the last two. The height is $2\delta$ exactly in the limit of dense
sampling; the tool samples 4000 points a side on the open interval, so it reports
$2\delta(1 - 1/4001)$, which is why $\delta = 1$ reads 1.9995 rather than 2. Not cited in
the prose.

`[COMPUTED]` Setting the value at $x = 2$ to undefined, to 4, or to 1 leaves the height at
0.0200, identical to twelve decimal places in all three cases. This is the article's central
claim and it is verified rather than asserted: the window excludes the centre, so the marker
is not among the outputs collected.

`[COMPUTED]` The jump, $f(x) = x+2$ for $x<2$ and $x-1$ for $x>2$: bar height 3.0000 at
$\delta = 0.1$, $0.01$, and $0.001$. One-sided values at $x = 2 \mp 10^{-9}$ are 3.999999999
and 1.000000001.

`[COMPUTED]` The oscillation: bar height exactly 2.0000 at $\delta = 1$, $0.01$, and
$0.0001$.

`[STANDARD]` $\sin\!\left(\frac{1}{x-2}\right)$ attains both $+1$ and $-1$ in every
punctured neighbourhood of 2. As $x \to 2^+$, $u = 1/(x-2) \to +\infty$, so $u$ passes
through $\pi/2 + 2k\pi$ for infinitely many integers $k$. Checked numerically: for
$\delta = 10^{-3}$ and $\delta = 10^{-6}$ alike, at least three such inputs lie inside the
window. The tool therefore returns $[-1, 1]$ exactly for this mode rather than by sampling.

## Standard results

`[STANDARD]` A two-sided limit exists if and only if both one-sided limits exist and are
equal. Stated in the article as a biconditional.

`[STANDARD]` The limit is independent of the value of the function at the point, and of
whether the function is defined there. This is the definition, not a consequence.

`[STANDARD]` A function can fail to have a limit without a jump and without an asymptote.
Oscillation is the standard counterexample.

`[STANDARD]` The derivative is a limit of difference quotients undefined at the point of
interest; the definite integral is a limit of Riemann sums. Both stated in the opening as
motivation; the second links to the existing Riemann sums article.

## Exam claims

**None. Both were cut** on Katherine's instruction, 2026-07-30, because I could not source
them. What they were:

1. "The free-response section tests that separation directly: a graph with a hole at
   $x = 3$ and a dot somewhere else entirely, asking for the limit and for $f(3)$ as two
   questions with two different answers." Unsourced, and on reflection probably overstated
   — limit-versus-value graph reading is more characteristically a multiple-choice
   construction, and AB free-response graph questions usually hand you $f'$ rather than $f$.
2. "Saying which of those happened is usually worth its own point." No basis at all.

The closing section was rewritten as a reading technique with no claim about the exam
attached. The mathematics it states — that the limit is the common destination of the two
sides when there is one, and that failure comes in more than one kind — is `[STANDARD]` and
is carried by the article's own interactive. The section heading changed from "What this
buys on the exam" to "Reading a limit off a graph" to match.

## Judgment claims

`[JUDGMENT]` Covering the point with a finger and reading only the two sides is a reliable
habit. Offered as a technique, not as a claim about what students do.

`[JUDGMENT]` A student who can explain the oscillation case in one sentence understands
limits better than one who can compute twenty of them. In the closing note, clearly framed
as an opinion.

---

## Flags raised in this session

1. **Two exam claims were cut, on instruction.** I have the AP Calculus CED's unit list and
   exam weightings from the primary source, but not the Unit 1 essential-knowledge
   statements — the PDF fetch truncated before them, as it did for Statistics. Rather than
   ship unsourced claims about the exam, both sentences are gone and the closing section is
   now a reading technique. **This article therefore contains no `[EXAM]` claims at all**,
   which is a first for the programme and is fine: the article's job is conceptual.

   Standing consequence for the rest of 7D: until I can read the Calculus essential-
   knowledge statements, every article in this programme will be light on exam-specific
   claims relative to the Statistics ones, where I could source them to numbered statements.
   If you want that parity, the fix is getting me the Unit 1–10 topic detail; the fetch
   truncates at about 105,000 characters and the document is far longer.

2. **A control the prose outran, caught by the harness.** A draft cited $\delta = 0.0001$
   against a slider that bottomed out at $0.001$. This is the third time this session that
   reading numbers back out of the shipped code has caught a claim the reader could not
   reproduce; it is worth keeping as a standing check for every remaining 7D article.

3. **The jump's bar height does not contract.** A draft said it "contracts to a height of 3
   and stops there." It is 3 at every $\delta$, because the bar spans the outputs from both
   sides at once and those never approach each other. Corrected to say the height sits at 3
   throughout, which is the more useful observation anyway.

4. **Sampling artefact, not cited but worth knowing.** At $\delta = 1$ the hole's bar reads
   1.9995 rather than 2.0000, because the sampler works on the open interval and never
   reaches the endpoints. It is invisible at the scales the prose uses, and arguably correct
   — the endpoints are genuinely not in the punctured window.

5. **This is the first 7D article, so the tier order begins.** Article 2 is continuity's
   three conditions, which the closing paragraph of this one hands off to. That handoff is
   currently unlinked, since the article does not exist; it wants a link added once it does.

---

## Corrections applied 2026-07-30, CED-alignment pass

**The handoff is linked.** Flag 5 above is resolved. The closing of "Failing without a jump"
pointed forward to an article that did not exist when this one was written. It now links to
[continuity's three conditions](/2026/07/30/continuity-three-conditions.html), giving this
article two outbound links.

Flag 1 stands corrected in the 7D-2 ledger: the reason I gave for cutting the two exam claims
was wrong, though the cut itself was right on the merits.
