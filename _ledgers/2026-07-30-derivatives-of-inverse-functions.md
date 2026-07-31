# Claims ledger — Derivatives of inverse functions

Article: `_posts/2026-07-30-derivatives-of-inverse-functions.md`
Session: 7D article 11 (last of tier 3), 2026-07-30. AP Calculus sequence 12, Unit 3 topics 3.3
and 3.4.

Verification: `t.js`, `t2.js`, and `t3.js` load the shipped script in jsdom with a stubbed canvas
context, click each of the five function buttons, and sweep all 1201 slider positions for each,
reading every panel row back out of the live DOM.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **FUN-3.E.1** (topic 3.3): "The chain rule and definition of an inverse function can be
used to find the derivative of an inverse function, **provided the derivative exists**." Both
halves are in the article — the derivation runs exactly that route (definition of an inverse,
then chain rule), and the closing section is the clause.

`[EXAM]` **FUN-3.E.2** (topic 3.4): "The chain rule applied with the definition of an inverse
function, **or the formula for the derivative of an inverse function**, can be used to find the
derivatives of inverse trigonometric functions." The framework names both routes, which is why
the article says both are available and short.

`[EXAM]` **Topic 3.3's suggested skill is 3.G**, "Confirm that solutions are accurate and
appropriate" — the only topic in Units 2 and 3 carrying a justification skill rather than 1.C,
1.D, or 1.E. The interactive is built around it: two independent confirmations of the same
number. Topic 3.4 carries 1.E.

`[EXAM]` Topic titles: 3.3 "Differentiating Inverse Functions", 3.4 "Differentiating Inverse
Trigonometric Functions".

`[EXAM]` Unit 3's exam guidance recommends "mixed practice differentiating general functions
using select values provided in tables and graphs... products, quotients, compositions, and
inverses of functions, especially those with names other than $f$ and $g$." The closing note's
advice about reading the right column of a table comes from that.

`[STANDARD]` The theorem as stated, with its three hypotheses — $f$ one-to-one and differentiable
on an interval, $f^{-1}$ defined near $a$, and $f'(f^{-1}(a)) \neq 0$ — is the standard statement.
The CED asserts the rule and the non-vanishing condition; the rest is standard analysis.

## Computed results

Everything below was read out of the running tool unless marked otherwise.

`[COMPUTED]` **The two slopes multiply to exactly 1.** Across all five functions and all 1201
slider positions, the product row reads 1 with error exactly 0 in double precision at every
position where both slopes exist. Three positions report no product: $b = \pm\pi/2$ on the
restricted sine, and $b = 0$ on $x^3$.

`[COMPUTED]` **The reciprocal agrees with the memorised inverse derivative.** The tool computes
$1/f'(b)$ and, separately, evaluates the formula a student would memorise — $1/a$ for $\ln$,
$1/\sqrt{1-a^2}$ for $\arcsin$, $1/(1+a^2)$ for $\arctan$, $1/(3a^{2/3})$ for the cube root — and
prints the gap. Worst gaps over 4804 positions:

```
  e^x     0            (bit-identical everywhere)
  sin x   2.5e-9  absolute, at slider 1199, where the answer itself is 381.97
  tan x   4.4e-16 absolute
  x³      1.1e-13 absolute, where the answer is 612.24
```

The worst **relative** gap anywhere in the tool is $6.5 \times 10^{-12}$. The article's claim
that the gap "never exceeds seven parts in a trillion" is that figure rounded up.

`[COMPUTED]` **The worked example lands on an exact slider position.** Slider 900 on $x^3 + x$
gives $b = 1$, $a = 2$, $f'(1) = 4$, and $(f^{-1})'(2) = 0.25$ — all read from the panel, all
exact. Independently: $1^3 + 1 = 2$ and $3(1)^2 + 1 = 4$.

`[COMPUTED]` **The two inverse trigonometric derivations check out at named points.** Slider 800
on the restricted sine gives $b = \pi/6$ and $a = 0.5$, with $(f^{-1})'(0.5) = 1.1547$, matching
$2/\sqrt3 = 1.15470$ to four decimals from both the reciprocal and the $1/\sqrt{1-a^2}$ formula.
Slider 960 on the tangent gives $b = \pi/4$, $a = 1$, $f'(b) = \sec^2(\pi/4) = 2$, and
$(f^{-1})'(1) = 0.5$, matching $1/(1+1^2)$.

`[COMPUTED]` **The failure case is exactly reachable.** Slider 600 on $x^3$ gives $b = 0$ and
$f'(0) = 0$ exactly. The reciprocal row becomes a flag rather than a number and says why; the
product row says there is nothing to form; the cube-root formula row says it is undefined there
too. One slider step away, at $b = 0.0029$, the reciprocal reads $3.918\times10^4$ and the
memorised formula reads the same — so the quantity blows up rather than breaking.

`[COMPUTED]` **The slider ranges were chosen so the quoted values are reachable.** With 1201
positions: $b = 1$ at 900 on $x^3+x$ (range $[-2,2]$), $b = \pi/6$ at 800 on the sine, $b = \pi/4$
at 960 on the tangent (range $\pm 5\pi/12$), $b = 0$ at 600 on $x^3$. All four verified in the
harness rather than by arithmetic on paper.

`[COMPUTED]` **The inverse of $x^3 + x$ really is beyond the course.** $f'(x) = 3x^2 + 1 > 0$ for
all $x$, so $f$ is strictly increasing and invertible on the whole line, and solving
$y = x^3 + x$ for $x$ requires the cubic formula. The tool draws the inverse by swapping
coordinates, so it never inverts anything either.

## Judgment claims

`[JUDGMENT]` "That picture is the whole theorem." The reflection argument is a genuine proof
sketch, not a mnemonic, but the article calls it a picture and gives the formal statement
immediately after.

`[JUDGMENT]` "An unusual thing to ask of a differentiation rule and a reasonable thing to ask of
this one." An observation about skill 3.G's placement, supported by its being the only
justification skill among the ten topics of Units 2 and 3.

`[JUDGMENT]` "Two derivations, four lines, and no list." Countable from the article's own
displays.

`[JUDGMENT]` The closing note's table advice — look down the $f(x)$ column, not the $x$ column —
is the standard reading of the exam-format problem, and the CED recommends table practice for
exactly these topics.

---

## Flags raised in this session

1. **My test harness was parsing the panel wrong, and the panel was the thing that needed
   fixing.** The readout printed labels and values in one text node, so a label containing the
   digit 1 — "(f⁻¹)′(a) = 1 / f′(b)" — made my parser read every row as 1, and the first run
   reported ten false failures. Rather than patch the regex, I wrapped every value in its own
   `.iv-val` span. That makes the panel testable by structure instead of by pattern, and it is
   the reason the later sweeps are trustworthy. Worth generalising to future tools.

2. **The slider originally could not reach any of the values the prose quotes.** With 1001
   positions, $b = 1$ landed at 822.58 and $b = \pi/6$ at 666.67. I changed the resolution to
   1201 and adjusted three ranges — including narrowing the tangent to $\pm 5\pi/12$ — so that
   every quoted $b$ sits on an integer position. That is the sixth instance of this class across
   7D, and the first one I checked for before writing the prose rather than after.

3. **A real numerical finding, which the article does not claim but you might like to know.**
   The two routes to $(\arcsin)'$ are mathematically identical but not numerically identical.
   Near $a = \pm 1$ the memorised formula $1/\sqrt{1-a^2}$ subtracts a number close to 1 from 1
   and loses precision, while $1/\cos b$ does not. That is the entire source of the $2.5\times
   10^{-9}$ gap, and it is a property of the formula rather than of the theorem. I left it out of
   the prose because the article is not about conditioning, but it is a nice example if a student
   ever asks why two correct formulas disagree.

4. **Two notation choices with no precedent in the corpus, both retired.** I had written
   $\mathbb{R}$ and $\sqrt[3]{x}$; neither appears anywhere else in your 44 articles. They are
   now "the whole real line" and $x^{1/3}$, which is the notation the differentiability article
   already uses for the same function. The tool's button still shows ∛x, so the prose names both
   forms once.

5. **677 words**, four `##` headings, no italics, three cross-links. Inside the 650–950 target,
   though on the lower half of it — the panel carries six rows of explanation that the prose
   therefore does not repeat.

6. **Tier 3 is complete, and Unit 3 topics 3.5 and 3.6 remain uncovered.** As flagged in the
   chain rule ledger, 3.5 ("Selecting Procedures for Calculating Derivatives", skill 1.C) would
   make a natural mixed-drill companion to sequence 9 and 10. Topic 3.6 (higher-order
   derivatives) is partly served by the second-derivative section of the implicit article and
   will come up again in particle motion at sequence 13. Neither is in the approved plan.
