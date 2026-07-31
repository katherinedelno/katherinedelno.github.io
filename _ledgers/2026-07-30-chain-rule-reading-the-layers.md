# Claims ledger — The chain rule and reading the layers

Article: `_posts/2026-07-30-chain-rule-reading-the-layers.md`
Session: 7D article 9 (first of tier 3), 2026-07-30. AP Calculus sequence 10, Unit 3, topic 3.1.

Verification: `t.js` loads the shipped script in jsdom, clicks each of the seven function
buttons, sweeps the x slider across all 301 positions for each, and reads the layer rows, the
product, and the measured-slope line back out of the live DOM. Reference derivatives computed
independently with SymPy.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy
in your own Admin folder.

`[EXAM]` **Topic 3.1's suggested skill is 1.C**, and its wording is the article's opening
argument: "Identify an appropriate mathematical rule or procedure based on the classification
of a given expression (e.g., Use the chain rule to find the derivative of a composite
function)." The chain rule is the CED's own parenthetical example of a classification problem.

`[EXAM]` FUN-3 (enduring understanding): "Recognizing opportunities to apply derivative rules
can simplify differentiation." Same enduring understanding as Unit 2, which is why this article
opens where the previous one closed.

`[EXAM]` FUN-3.C (learning objective): "Calculate derivatives of compositions of
**differentiable** functions." FUN-3.C.1: "The chain rule provides a way to differentiate
composite functions." The differentiability hypothesis is the framework's, not an embellishment.

`[EXAM]` Topic 3.1 is titled "The Chain Rule". Unit 3 is "Differentiation: Composite, Implicit,
and Inverse Functions", ~10–11 class periods AB and ~8–9 BC.

`[STANDARD]` The theorem as stated — if $g$ is differentiable at $x$ and $h$ is differentiable
at $g(x)$, then $h \circ g$ is differentiable at $x$ and $(h\circ g)'(x) = h'(g(x))\cdot g'(x)$
— is the standard statement with both hypotheses and both evaluation points. The CED states the
rule's existence, not its hypotheses in this form; the hypotheses are standard analysis.

`[JUDGMENT]` "They are not fractions." The Leibniz form is a notation, and the cancellation
reading is a mnemonic that happens to give the right answer here. Stated as a caution rather
than as a claim about what students believe.

## Computed results

Every derivative below was computed symbolically in SymPy, evaluated at $x = 4/5$ exactly, and
then compared against the value the shipped tool prints.

`[COMPUTED]` **All seven functions: chain product equals the true derivative, symbolically.**
For each, `simplify(product_of_factors - diff(f))` returns 0.

```
  function        f'(0.8) SymPy      layers   tool product
  (3x + 1)^5        2004.504000        2       2004.5040
  sin(x^2)             1.283353        2          1.2834
  (sin x)^2            0.999574        2          0.9996
  e^(sin x)            1.427558        2          1.4276
  ln(x^2 + 1)          0.975610        2          0.9756
  sin(e^(x^2))        -0.970869        3         -0.9709
  (x^2)^3              1.966080        2          1.9661
```

`[COMPUTED]` **The worked example.** $h(u) = u^5$, $g(x) = 3x+1$, giving
$5(3x+1)^4 \cdot 3 = 15(3x+1)^4$. Expanding both sides:
$1215x^4 + 1620x^3 + 810x^2 + 180x + 15$, identical. At $x = 0.8$ it is 2004.504, matching the
tool's first row.

`[COMPUTED]` **The caption's accuracy claim, checked exhaustively.** Across all seven functions
and all 301 slider positions — 2107 evaluations — the largest gap between the chain-rule product
and the symmetric-difference slope is $1.10 \times 10^{-6}$, at $(3x+1)^5$ with $x = 1.5$. The
caption says the two agree to four decimals everywhere, and $1.1\times10^{-6}$ is two orders
inside that.

`[COMPUTED]` **The look-alike pair.** $\frac{d}{dx}\sin(x^2) = 2x\cos(x^2)$ and
$\frac{d}{dx}(\sin x)^2 = 2\sin x\cos x$, which SymPy returns in the form $\sin(2x)$ — the
article gives both forms because the second is the one students recognise. At $x = 0.8$:
1.2834 and 0.9996, both read out of the running tool.

`[COMPUTED]` **The missing-factor arithmetic.** For $\sin(x^2)$ at $x = 0.8$: outer factor
$\cos(0.64) = 0.8021$, inner factor $2x = 1.6$, product 1.2834. Stopping at the outer factor
understates by exactly the factor 1.6. At $x = 0.05$ the inner factor is 0.1, so the same
omission *overstates* by a factor of ten. Both slider positions are exactly reachable — the
slider is integer-valued in hundredths, so $x = 0.05$ is position 5 and $x = 0.8$ is position
80. Checked in the harness rather than assumed.

`[COMPUTED]` **The callback to the previous article.** $(x^2)^3$: the chain rule gives
$3(x^2)^2\cdot 2x = 6x^5$, and so does the power rule on $x^6$. Verified symbolically and read
from the tool at $x = 1$, where both give exactly 6.

`[COMPUTED]` **The three-layer case needs no new rule.** $\sin(e^{x^2})$ produces three rows
tagged outer, middle, inner, and their product matches SymPy to $10^{-6}$ relative. The middle
factor is what appears when the inner function is itself a composition.

## Judgment claims

`[JUDGMENT]` "Almost every mistake made with it happens before that point." An argument the
article then makes concrete with the look-alike pair and the dropped factor, rather than a
frequency claim I can source.

`[JUDGMENT]` "The error does not have a characteristic size; it has a characteristic shape."
Supported by the two computed cases — the same omission understates at $x = 0.8$ and overstates
at $x = 0.05$.

`[JUDGMENT]` The closing note's test (name the last operation you would perform if evaluating
at a number) is a standard heuristic, offered as a habit rather than as a theorem.

---

## Flags raised in this session

1. **Two prose-versus-tool mismatches, caught before shipping.** I had written "Peel one layer
   at a time," which describes a peel button the tool does not have — it shows all layers at
   once. And the caption said the measured slope was "the last row" when it sits below the
   stack, not in it. Both reworded to describe what is actually on screen. That is the same
   class of error as the five slider mismatches in tier 2, and it is now the thing I check
   first.

2. **The verification is exhaustive rather than sampled.** Rather than checking a handful of
   points, the harness sweeps every slider position for every function and reports the worst
   case. For a claim of the form "these agree everywhere," a sweep is the honest test and it
   costs nothing.

3. **One claim cut for being unverifiable.** I wanted to say where $\sin(x^2)$ and
   $(\sin x)^2$ have equal derivatives — the equation $2x\cos(x^2) = \sin(2x)$ is
   transcendental and SymPy could not solve it. Rather than assert a numeric root I had not
   confirmed, the sentence is gone. The article makes its point from the two values at
   $x = 0.8$, which are computed.

4. **718 words**, four `##` headings, no italics, no inline `\frac` or `\dfrac`. Inside the
   650–950 target.

5. **A gap in the sequence plan worth your decision.** Unit 3 has six topics; the approved plan
   covers 3.1 (this article), 3.2 (implicit), and 3.3 (inverse functions). Topic 3.4
   (derivatives of inverse trigonometric functions), 3.5 (Selecting Procedures for Calculating
   Derivatives), and 3.6 (higher-order derivatives) have no article. Topic 3.5 in particular
   carries skill 1.C, the same classification skill as 3.1, and would be a natural companion
   piece to this one and to the previous article — a mixed drill across every rule in Units 2
   and 3. Say the word and I will add it to the plan; otherwise the sequence stands as approved.
