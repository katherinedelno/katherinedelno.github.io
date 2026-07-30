# Claims ledger — Indeterminate forms and the algebra that resolves them

Article: `_posts/2026-07-30-indeterminate-forms.md`
Session: 7D article 4 (tier 1), 2026-07-30. AP Calculus sequence 3, Unit 1.

No interactive, per the brief. This is the first prose-only article in the programme, so
every worked example was checked symbolically and numerically rather than read back out of a
running tool.

---

## Framework grounding

`[EXAM]` Rearranging before evaluating, from LIM-1.E.1 (topic 1.6, Determining Limits Using
Algebraic Manipulation): "It may be necessary or helpful to rearrange expressions into
equivalent forms before evaluating limits." Quoted in the opening.

`[EXAM]` The three techniques named in topic 1.6's illustrative examples, which is why the
article covers exactly these: "Factoring and dividing common factors of rational functions";
"Multiplying by an expression involving the conjugate of a sum or difference in order to
simplify functions involving radicals"; "Using alternate forms of trigonometric functions".

`[EXAM]` Limit theorems, from LIM-1.D.2 (topic 1.5): "Limits of sums, differences, products,
quotients, and composite functions can be found using limit theorems."

`[EXAM]` The squeeze theorem, from LIM-1.E.2 (topic 1.8): "The limit of a function may be
found by using the squeeze theorem." It sits under the same learning objective as algebraic
rearrangement — LIM-1.E covers "equivalent expressions for the function **or** the squeeze
theorem" — which is why the article treats them together rather than as separate topics.

`[EXAM]` The two standard trigonometric limits are named in topic 1.8's illustrative
examples: "The squeeze theorem can be used to show $\lim_{x\to 0}\frac{\sin x}{x} = 1$ and
$\lim_{x\to 0}\frac{1-\cos x}{x} = 0$." The article states both and attributes them to the
squeeze theorem, as the framework does.

`[EXAM]` Selecting the procedure is its own topic. Topic 1.7 carries no essential knowledge
at all, only a note: "This topic is intended to focus on the skill of selecting an
appropriate procedure for determining limits." The article's closing section exists because
of that, and the claim that selection "is its own listed skill" is literally true.

`[EXAM]` Substitution is legal where the function is continuous, which rests on LIM-2.B.2 —
the standard families are continuous on their domains — already quoted in the continuity
article and linked from this one.

## Computed results

Every limit below was confirmed by evaluating the function at $\pm 10^{-4}$ and
$\pm 10^{-6}$ from the point, against the exact value.

`[COMPUTED]` The opening's three expressions, all reading $0/0$ at $x = 3$:

```
  (x^2-9)/(x-3)      limit 6            numeric at 3+1e-7:  6.000000
  (x-3)/(x^2-9)      limit 1/6          numeric at 3+1e-7:  0.166667
  (x-3)/(x-3)^2      does not exist     numeric at 3+1e-7:  1.0e+7 and rising
```

`[COMPUTED]` Factor and cancel: $\lim_{x\to 3}\frac{x^2-9}{x-3} = 6$. Values at
$3 \pm 10^{-4}$: 6.00010000 and 5.99990000.

`[COMPUTED]` Difference of cubes: $\lim_{x\to 2}\frac{x^3-8}{x^2-4} = 3$. Values at
$2 \pm 10^{-4}$: 3.00007500 and 2.99992500. The stated arithmetic
$\frac{4+4+4}{4} = 3$ checks: $x^2+2x+4$ at $x=2$ is 12, and $x+2$ is 4.

`[COMPUTED]` Conjugate: $\lim_{x\to 0}\frac{\sqrt{x+4}-2}{x} = \tfrac14$. Values at
$\pm 10^{-4}$: 0.24999844 and 0.25000156.

`[COMPUTED]` Compound fraction: $\lim_{x\to 0}\frac{\frac{1}{x+2}-\frac12}{x} = -\tfrac14$.
Values at $\pm 10^{-4}$: −0.24998750 and −0.25001250.

`[COMPUTED]` The two trigonometric limits:

```
  sin(x)/x       at x = 1e-2, 1e-4, 1e-6:  0.999983, 1.000000, 1.000000
  (1-cos x)/x    at x = 1e-2, 1e-4, 1e-6:  0.005000, 0.000050, 0.000001
```

`[COMPUTED]` The squeeze example $x^2\sin(1/x)$, shown against its bound:

```
  x = 0.1     value -0.0054402111   bound x^2 = 0.0100000000
  x = 0.01    value -0.0000506366   bound x^2 = 0.0001000000
  x = 0.001   value +0.0000008269   bound x^2 = 0.0000010000
  x = 0.0001  value -0.0000000031   bound x^2 = 0.0000000100
```

The value stays inside $\pm x^2$ at every scale, and both bounds go to zero.

`[STANDARD]` The cancellation in a factor-and-cancel step is legal because the limit never
evaluates at the point, so the cancelled factor is non-zero on every input the limit
inspects. Stated explicitly in the article, since it is the step students perform without
being able to justify.

`[STANDARD]` The quotient limit theorem requires the denominator's limit to be non-zero.
This is exactly the hypothesis that fails in every example here, which is the article's
organising observation.

`[STANDARD]` The difference quotient of $1/x$ has the compound-fraction shape, which is why
the technique recurs in Unit 2.

## Judgment claims

`[JUDGMENT]` "A student who starts multiplying by conjugates on a polynomial quotient has
not made an arithmetic error; they have skipped the step where the expression is read."
Teaching observation, unsourced, though topic 1.7's existence supports the underlying point
that selection is a separable skill.

`[JUDGMENT]` The closing note's drill — classify twenty limits without solving any — is a
pedagogical suggestion. It mirrors the drill in the existing convergence-test article, which
is deliberate: both topics are selection problems wearing computation clothes.

---

## Flags raised in this session

1. **The description said "four techniques" when the article gives five things**, and one of
   them, the squeeze theorem, is not a rewriting technique at all. Corrected before commit.
   Worth noting because the description is what appears on featured cards and in search
   results, and it is the field least likely to get re-read.

2. **"Alternate forms of trigonometric functions" is under-served.** The framework lists it
   as a third algebraic technique alongside factoring and conjugates, and I covered
   trigonometry only through the two standard limits. A worked example using a Pythagorean
   or double-angle identity to resolve a $0/0$ would close that gap. I left it out on length
   grounds; the article is already 772 words with six headings.

3. **No interactive, per your brief.** This is the first prose-only article in the
   programme, and it is worth saying that it did not want one. The content is a
   classification and four rewritings; there is nothing to drag. The closest thing to a
   visual argument is the squeeze bound, which the numbers above make adequately.

4. **The opening triple is the article's strongest asset and is entirely borrowed from
   arithmetic.** Three expressions that all read $0/0$ and have limits 6, $\tfrac16$, and
   nonexistent. If you ever want a single slide for this topic, that is it.
