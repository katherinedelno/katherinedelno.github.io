# Claims ledger — Two existence theorems, and what they refuse to tell you

Article: `_posts/2026-07-30-mean-value-and-extreme-value-theorems.md`
Session: 7D article 15 (tier 4), 2026-07-30. AP Calculus sequence 17, Unit 5 topics 5.1 and 5.2.

Verification: `t.js` loads the shipped script in jsdom with a stubbed canvas context, clicks each
of the four scenario buttons, and reads all six panel rows and their notes out of the live DOM,
comparing against values derived symbolically in SymPy.

---

## Framework grounding

Quotations from the AP Calculus AB and BC Course and Exam Description and from the separate
Clarifications and Corrections document, both read from the copies in your own Admin folder.

`[EXAM]` **Enduring understanding FUN-1**, the article's opening sentence: "Existence theorems
allow us to draw conclusions about a function's behavior on an interval without precisely
locating that behavior." The same FUN-1 that carries the Intermediate Value Theorem at sequence
6, which is why the article opens by pointing back at it.

`[EXAM]` **FUN-1.B.1** (topic 5.1): "If a function $f$ is continuous over the interval $[a, b]$
and differentiable over the interval $(a, b)$, then the Mean Value Theorem guarantees a point
within that open interval where the instantaneous rate of change equals the average rate of
change over the interval." Both interval types are the framework's, and the article's remark
about the asymmetry is an explanation of them rather than an addition.

`[EXAM]` **FUN-1.C.2**: "A point on a function where the first derivative equals zero or fails to
exist is a critical point of the function." **FUN-1.C.3**: "All local (relative) extrema occur at
critical points of a function, though not all critical points are local extrema." Both close to
verbatim in the article.

`[EXAM]` **Topics 5.1 and 5.2 both carry suggested skill 3.E**, "Provide reasons or rationales
for solutions and conclusions" — quoted in the closing note, and the reason that note is about a
sentence rather than a calculation. Topic 5.2's full title is "Extreme Value Theorem, Global
Versus Local Extrema", which is what the fourth section is about.

`[EXAM]` **FUN-1.C.1, and this one needs care.** The base CED prints: "If a function $f$ is
continuous over the interval **$(a, b)$**, then the Extreme Value Theorem guarantees that $f$ has
at least one minimum value and at least one maximum value on $[a, b]$." As printed that is
**false** — see the computed counterexample below. The Clarifications and Corrections document,
to be implemented for Fall 2026, updates it to read "continuous over the interval **$[a, b]$**".
The article states the corrected version.

## Computed results

`[COMPUTED]` **The bracket glyphs, established rather than assumed.** The clarification's
brackets are set in SymbolMT using Private Use Area codepoints, so every plain text extraction
drops them. Reading the PDF's spans with their fonts gives the actual glyphs: `U+F8EE`
(bracketlefttp), `U+F8F0` (bracketleftbt), `U+F8F9` (bracketrighttp), `U+F8FB` (bracketrightbt).
All four are square-bracket pieces; no parenthesis glyph (`U+F8EB`, `U+F8ED`, `U+F8F6`, `U+F8F8`)
appears anywhere in the sentence. The correction is unambiguously to the closed interval.

`[COMPUTED]` **The base CED's printed statement is false**, which is presumably why it was
corrected. Take $f(x) = x$ on $(0,1)$, with $f(0) = f(1) = \tfrac12$. It is continuous on
$(0,1)$, so the printed hypothesis holds. Its values on $[0,1]$ are $\{\tfrac12\} \cup (0,1)$:
the supremum 1 is not attained and the infimum 0 is not attained, so there is neither a maximum
nor a minimum on $[0,1]$. The conclusion fails outright.

`[COMPUTED]` **Scenario 1, $f(x) = x^3 - 4.5x^2 + 6x$ on $[0,3]$.** $f(0) = 0$, $f(3) = 4.5$, so
the average rate is $\tfrac32$. $f'(x) = 3(x-1)(x-2)$, and $f'(c) = \tfrac32$ at
$c = \tfrac{3 \pm \sqrt3}{2} = 0.633975,\ 2.366025$. The tool reports two points at 0.6340 and
2.3660, matching to $10^{-4}$ — the panel prints four decimals, so that is exact agreement.

`[COMPUTED]` **The extrema on scenario 1 are at the endpoints, and the endpoints are not critical
points.** Candidates: $f(0) = 0$, $f(1) = 2.5$, $f(2) = 2$, $f(3) = 4.5$. Global maximum 4.5 at
$x=3$; global minimum 0 at $x=0$. And $f'(0) = f'(3) = 6 \neq 0$, so neither endpoint is a
critical point. The interior critical points give local extrema of 2.5 and 2, neither global.
This is the whole content of the fourth section and every figure in it is computed.

`[COMPUTED]` **Scenario 2, $f(x) = |x - 1.5| + 1$.** Continuous on $[0,3]$, not differentiable at
1.5. $f(0) = f(3) = 2.5$, so the average rate is 0, and $f'$ takes only the values $-1$ and $+1$.
The tool reports zero points $c$ and adds that the theorem no longer promises one. The Extreme
Value Theorem still delivers: maximum 2.5, minimum 1 at $x = 1.5$. One function, two theorems,
opposite outcomes.

`[COMPUTED]` **Scenario 3, a jump at 1.5.** $f(x) = x$ on $[0,1.5)$ and $x - 2$ on $[1.5,3]$.
Average rate $\tfrac13$; $f' = 1$ wherever it exists, so no $c$. The supremum on $[0,1.5)$ is
1.5 and is not attained, and $f(3) = 1$, so there is no maximum. The minimum, $-0.5$ at
$x = 1.5$, is attained. Both readings confirmed from the panel.

`[COMPUTED]` **Scenario 4, and it is the article's point.** The cubic on $(0,3]$ with $f(0)$
moved to 3. Continuity fails at the left endpoint, so both theorems are void. The Extreme Value
Theorem's conclusion also fails: $f(x) = x(x^2 - 4.5x + 6)$ and the quadratic factor has
discriminant $-3.75 < 0$, so it is positive everywhere and $f(x) > 0$ for every $x > 0$. Over
200,000 samples on $(0,3]$ the smallest value found is $9.0\times10^{-5}$ — approaching 0,
never reaching it. No minimum.

But the Mean Value Theorem's *conclusion* survives. The average rate is now $\tfrac12$, and
$f'(c) = \tfrac12$ at $c = \tfrac32 \pm \tfrac{\sqrt{15}}{6} = 0.854503,\ 2.145497$. The tool
reports 0.8545 and 2.1455. A void hypothesis withdraws the guarantee; it does not reverse it.

## Judgment claims

`[JUDGMENT]` "The case worth sitting with" (of the corner). Editorial.

`[JUDGMENT]` "Missing the endpoints is the standard way to lose this question." A claim about
what students do that I cannot source. It is adjacent to something I can — the theorem's
conclusion is about $[a,b]$, which includes its ends — and the sentence goes on to make that
argument. Flagging it as the softest claim in the article.

`[JUDGMENT]` "The theorem is partly to blame." Editorial, and deliberately generous.

---

## Flags raised in this session

1. **I found an error in the base CED, and then found that the College Board had already fixed
   it.** FUN-1.C.1 as printed gives the Extreme Value Theorem an open-interval hypothesis, which
   makes the statement false. The `Clarifications and Corrections` PDF — sitting in the same
   Admin folder as the CED, and effective this coming fall — corrects it to the closed interval.
   I had drafted the theorem correctly from standard analysis before finding either document,
   but the discrepancy is exactly the sort of thing that would have a student telling you the
   article contradicts the framework.

   **The article now carries one neutral sentence about it**, saying only that the statement was
   corrected for fall 2026 and the interval is the closed one. No editorialising about the
   College Board. If you would rather that sentence not be in a student-facing article, it is a
   clean single-sentence deletion and the theorem still reads correctly without it.

2. **The clarifications document changes two other things, and one of them is not about
   calculus.** Effective fall 2026:

   - **FUN-7.B.2** now reads "There may be infinitely many solutions to a differential
     equation." That lands in Unit 7, which is sequence 25–26 in the approved plan.
   - **The exam structure changed.** Multiple choice Part A goes from **30 questions in 60
     minutes to 29 questions in 62 minutes**; Part B goes from **15 questions in 45 minutes to
     13 questions in 38 minutes**. That is 42 multiple-choice questions instead of 45, and 100
     minutes instead of 105.

   I checked the corpus: no article states question counts or timings, so nothing is now wrong.
   But you may want that second item somewhere, and it is the kind of thing students ask about
   in August.

3. **The bracket problem is worth remembering for future CED work.** Both PDFs set mathematical
   brackets in SymbolMT with Private Use Area codepoints, so `pdftotext` silently drops them in
   every mode. Any CED quotation involving an interval has to be checked at the glyph level, not
   from the extracted text. I will do that from here on wherever a hypothesis names an interval.

4. **836 words**, four `##` headings, two italicised spans (both "at least"), three cross-links,
   all resolving. Inside the 650–950 target.

5. **The interactive has no slider**, which is a first for 7D. Four scenarios and nothing to
   drag: the whole point is a comparison across cases rather than a limit being approached, and
   adding a control would have implied there was something to explore within a case. Say the word
   if it reads as static.
