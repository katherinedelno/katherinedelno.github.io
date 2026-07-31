# Claims ledger — The rules, and choosing among them

Article: `_posts/2026-07-30-derivative-rules-and-choosing.md`
Session: 7D article 8 (last of tier 2), 2026-07-30. AP Calculus sequence 9, Unit 2, topics 2.5–2.10.

Verification: `t.js` loads the shipped script in jsdom, walks all ten expressions, answers each
one, and reads the classification, the feedback text, and the running score back out of the
live DOM. Symbolic and numeric results checked with SymPy.

---

## Framework grounding

All quotations below are from the AP Calculus AB and BC Course and Exam Description, read from
the copy in your own Admin folder.

`[EXAM]` **FUN-3 (enduring understanding), quoted almost verbatim in the second paragraph:**
"Recognizing opportunities to apply derivative rules can simplify differentiation." This is the
article's entire thesis, stated by the framework rather than by me. Worth knowing it is there.

`[EXAM]` **The suggested-skill split is real and is the article's structure.** From Unit 2's
Unit at a Glance: topics 2.5, 2.6, 2.7, 2.8, and 2.9 all carry skill **1.E**, "Apply appropriate
mathematical rules or procedures, with and without technology." Topic 2.10 alone carries skill
**1.D**, "Identify an appropriate mathematical rule or procedure based on the relationship
between concepts... to solve problems." Apply versus identify, in the CED's own words. The
classification drill is skill 1.D and nothing else — it never asks for a derivative.

`[EXAM]` Topic titles, verbatim: 2.5 Applying the Power Rule; 2.6 Derivative Rules: Constant,
Sum, Difference, and Constant Multiple; 2.7 Derivatives of cos x, sin x, e^x, and ln x;
2.8 The Product Rule; 2.9 The Quotient Rule; 2.10 Finding the Derivatives of Tangent,
Cotangent, Secant, and/or Cosecant Functions.

`[EXAM]` FUN-3.A.1: "Direct application of the definition of the derivative and specific rules
can be used to calculate the derivative for functions of the form $f(x) = x^r$."

`[EXAM]` FUN-3.A.2 and FUN-3.A.3: sums, differences, and constant multiples differentiate
termwise, and combined with the power rule this covers polynomials.

`[EXAM]` FUN-3.A.4: "Specific rules can be used to find the derivatives for sine, cosine,
exponential, and logarithmic functions." Exactly four, which is why the article says four.

`[EXAM]` FUN-3.B (learning objective): "Calculate derivatives of products and quotients of
**differentiable** functions." The differentiability hypothesis is in the framework's own
statement of the objective, which is why the article states it rather than assuming it.

`[EXAM]` FUN-3.B.3: "Rearranging tangent, cotangent, secant, and cosecant functions using
identities allows differentiation using derivative rules." The article's claim that these four
are not a second memorised list is the framework's position, not a preference of mine.

`[EXAM]` LIM-3.A (learning objective): "Interpret a limit as a definition of a derivative."
LIM-3.A.1: "In some cases, recognizing an expression for the definition of the derivative of a
function whose derivative is known offers a strategy for determining a limit." This sits inside
Unit 2, which is why the closing section belongs in this article rather than in Unit 1.

## Computed results

`[COMPUTED]` **The tangent derivation, end to end.** Quotient rule on $\sin x / \cos x$ gives
$(\cos^2 x + \sin^2 x)/\cos^2 x = 1/\cos^2 x = \sec^2 x$. Confirmed symbolically:
`diff(sin(x)/cos(x)) - sec(x)**2` simplifies to 0.

`[COMPUTED]` **Secant.** `diff(1/cos(x)) - sec(x)*tan(x)` simplifies to 0. The article now
states the result, so it is checked.

`[COMPUTED]` **The worked quotient, $(x^3 + 2x)/x$.** The quotient rule numerator
$(3x^2+2)(x) - (x^3+2x)(1)$ expands to exactly $2x^3$; dividing by $x^2$ gives $2x$. Direct
simplification gives $x^2 + 2$, derivative $2x$. Same answer, and the displayed intermediate
$2x^3/x^2$ is the real expansion, not a convenient fiction.

`[COMPUTED]` **The two products that collapse.** $x^2 \cdot x^5$ differentiates to $7x^6$;
$\sqrt{x}\cdot x = x^{3/2}$ differentiates to $\tfrac32 x^{1/2}$, and SymPy returns
`3*sqrt(x)/2`, which is the same thing.

`[COMPUTED]` **The two genuine quotients cancel nothing.** $(x^2+1)/(x-3)$ and $(\sin x)/x^2$
both leave the quotient rule as the shortest route; neither numerator shares a factor with its
denominator.

`[COMPUTED]` **The differentiability hypothesis is not decorative.** $|x| \cdot 1$ has
one-sided difference quotients $-1$ and $+1$ at 0, so no derivative; $|x| \cdot |x| = x^2$ for
real $x$ (verified symbolically and at $x = -3, -0.5, 0, 0.5, 3$) and has derivative 0 at 0.
Two products, one factor failing differentiability in each, opposite outcomes — which is the
article's point that the rule goes silent rather than returning a verdict.

`[COMPUTED]` **The LIM-3.A.1 limit.** $(2+h)^5 - 2^5$ expands to
$h^5 + 10h^4 + 40h^3 + 80h^2 + 80h$ — **five terms**, which is the number the article cites.
Dividing by $h$ and letting $h \to 0$ gives 80, matching $f'(2) = 5 \cdot 2^4 = 80$.
Numerically: 80.080040 at $h = 10^{-3}$, 80.000800 at $10^{-5}$, 80.000008 at $10^{-7}$.

`[COMPUTED]` **The drill itself, from the running DOM.** All ten expressions appear in order;
each one accepts its intended classification; a wrong answer names the correct category and
explains it; a second click on the same expression does not double-count. Exactly five items
are `rewrite`, which is what the prose and the caption both now say.

## Judgment claims

`[JUDGMENT]` "Memorising them is a week's work at most." A claim about the material, not about
students — the rules occupy one index card, which the article shows.

`[JUDGMENT]` "The product and quotient rules apply more often than they are needed." Supported
by the five rewrite cases, on all of which both rules would produce the right answer.

`[JUDGMENT]` "The long way is where sign errors live." Argued rather than measured: the
displayed quotient-rule route carries a subtraction, two derivatives, and a squared denominator
that the direct route does not.

`[JUDGMENT]` The closing note's exercise — annotate a page with first moves only, then compare
with a classmate — is a teaching suggestion in the spirit of skill 1.D.

---

## Flags raised in this session

1. **My own prose miscounted the drill, and the harness caught it.** I wrote "four of the ten
   want a rewrite" when the correct count is five: `tan x`, `(x³+2x)/x`, `x²·x⁵`, `sec x`, and
   `√x · x`. The test asserted four and failed. Both the caption and the body paragraph now say
   five, with the breakdown spelled out. This is the argument for testing the interactive's data
   against the prose rather than reading them side by side.

2. **Three step-count claims were loose and are now checked against what is displayed.** I had
   written "four lines" twice and once inside the interactive, in places where the shown
   derivation is three steps (the quotient) or four (the tangent). All three now match the
   displayed work. The drill's feedback text and the body paragraph agree.

3. **A read-time bug, found and fixed, affecting one other article.** The detector in
   `_style/read-time.py` matched `<div class="viz"` with a closing quote, so it missed
   `<div class="viz de-wrap">` — the distribution explorer, which was therefore scored as having
   no interactive. Its read time was one minute short. The regex now accepts a space or a quote,
   and the explorer's front matter has been corrected from 5 to 6 minutes. No other article was
   affected; all 41 now agree with the formula.

4. **787 words**, comfortably inside the 650–950 target, and the four `##` headings match the
   corpus median. Three italicised spans, against a corpus range of 0–21.

5. **"Cusp" has a cousin here.** The framework never uses the phrase "recognition step" either,
   though skill 1.D is exactly that idea in the CED's own language. The article uses the
   framework's framing (identify versus apply) rather than inventing vocabulary, so this is
   noted rather than flagged.

6. **One question for you.** The drill has no shuffle — the ten expressions cycle in a fixed
   order, so a student going through twice sees the same sequence. I left it deterministic
   because the order builds an argument (easy, easy, easy, then the four contested ones
   interleaved). If you would rather it randomised after the first pass, that is a four-line
   change and I can make it whenever.
