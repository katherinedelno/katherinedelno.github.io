# Claims ledger — The derivative as a limit

Article: `_posts/2026-07-30-derivative-as-a-limit.md`
Session: 7D article 6 (tier 2, first), 2026-07-30. AP Calculus sequence 7, Unit 2.

Verification: `t.js` loads the shipped script in jsdom, steps all three functions across the
h slider from both sides, and reads the two quotient readouts back out of the running tool.

---

## Framework grounding

`[EXAM]` The obstacle, quoted from CHA-1.A.2 (topic 1.1): "Because an average rate of change
divides the change in one variable by the change in another, the average rate of change is
undefined at a point where the change in the independent variable would be zero." This is
the article's opening sentence, paraphrased closely.

`[EXAM]` The resolution, from CHA-1.A.3: "The limit concept allows us to define
instantaneous rate of change in terms of average rates of change." Quoted almost verbatim.

`[EXAM]` CHA-1.A.1: "Calculus uses limits to understand and model dynamic change."

`[EXAM]` Unit 2 topic titles, from the CED's Course at a Glance: 2.1 Defining Average and
Instantaneous Rates of Change at a Point; 2.2 Defining the Derivative of a Function and
Using Derivative Notation; 2.3 Estimating Derivatives of a Function at a Point; 2.4
Connecting Differentiability and Continuity.

`[EXAM]` The notation requirement is skill 4.C as listed against topic 2.2: "Use appropriate
mathematical symbols and notation (e.g., Represent a derivative using $f'(x)$, $y'$, and
$\frac{dy}{dx}$)." The article's notation section exists because the framework attaches that
skill to this topic, and it reproduces exactly those three forms.

**Secondary only:** that CHA-2.B is "represent the derivative of a function as the limit of a
difference quotient". The CED fetch truncates in the middle of Unit 2's sample instructional
activities, before Unit 2's essential knowledge. The definition itself is `[STANDARD]` and
needs no source; only the objective code is secondhand, and the article does not cite it.

## Computed results

All read out of the shipped tool.

`[COMPUTED]` $x^2$ at $a = 1$. The quotient is exactly $2 + h$:

```
  h = 1      3.000000        h = -0.1     1.900000
  h = 0.1    2.100000        h = -0.01    1.990000
  h = 0.01   2.010000        h = -0.001   1.999000
  h = 0.001  2.001000
```

The prose cites 3, 2.1, 2.01, 2.001 going down and 1.9, 1.99, 1.999 coming up. Every one
verified.

`[COMPUTED]` $x^3$ at $a = 1$, quotient $3 + 3h + h^2$: 7 at $h = 1$, 3.31 at $0.1$, 3.0301
at $0.01$, 2.71 at $-0.1$.

`[COMPUTED]` $\sin x$ at $a = 0$, quotient $\sin(h)/h$: 0.998334 at $h = \pm 0.1$, 0.999983
at $0.01$. These are the values the closing note asks the reader to find, and they are the
same numbers the indeterminate-forms article establishes by the squeeze theorem.

`[COMPUTED]` The two forms agree at every setting tested — $h = 1, 0.5, 0.1, -0.2, -0.001$ —
to within $10^{-9}$. They are algebraically the same fraction; the residual difference is
floating-point only, since $(a+h) - a$ is not bit-identical to $h$.

`[STANDARD]` $\dfrac{(1+h)^2 - 1}{h} = \dfrac{2h + h^2}{h} = 2 + h$, and the cancellation is
legal because the limit never evaluates at $h = 0$.

`[STANDARD]` The two-sided limit requires both one-sided approaches to agree. The article
makes the reader take $h$ negative for exactly this reason.

`[STANDARD]` The tangent line is defined by the limit, not the other way round. The article
uses $\sin x$ at the origin as the counterexample to "touches at one point": that tangent
crosses the curve and meets it again infinitely often.

## Judgment claims

`[JUDGMENT]` The $h$-form is easier to compute with and the $x$-form easier to recognise on
an exam question that hands you a limit and asks which derivative it is. Teaching
observation.

`[JUDGMENT]` Students learn the two forms as two facts. Asserted; the article's response is
to show the readouts agreeing at every $h$ rather than to argue.

---

## Flags raised in this session

1. **A dead zone in the slider, caught by the harness.** The first encoding mapped slider
   value $v$ to $|h| = 10^{|v|/100 - 3}$, so $v = 0$ had no sign and $h = -0.001$ was
   unreachable — while the prose cited 1.999, which needs exactly that. Remapped so
   $|v| = 1$ is $h = 0.001$ and $|v| = 301$ is $h = 1$, putting every power of ten within
   exact reach on both sides. This is the fourth control-versus-prose mismatch the DOM
   harness has caught in 7D.

2. **Powers of ten only.** On an integer log slider, $h = 0.5$ lands at 0.50119 rather than
   0.5. A draft cited a quotient of 2.5; the prose now cites 3, 2.1, 2.01, 2.001, all of
   which are exactly reachable. Worth knowing before building a lesson on a specific $h$.

3. **Unit 2's essential knowledge is still out of reach.** The Calculus CED fetch stops
   inside Unit 2's sample instructional activities. Everything sourced above comes from
   topic 1.1's essential knowledge, the Course at a Glance, and the skill list — all primary
   — but the formal definition's own statement is not among them. It is `[STANDARD]`
   mathematics, so nothing is unsupported; the article simply cannot quote the framework at
   the point where it would most like to.

4. **Typography pass, corpus-wide.** Applied while this article was in flight, on your
   instruction. `head.html` maps `$$` to displayMath, so inline `$$…$$` renders full-size.
   Corrected 21 inline fractions to `\tfrac`, 27 inline integrals and sums to `\textstyle`,
   and 5 fractions nested inside display fractions to `\tfrac`. Nine articles touched, six
   of them older ones — notation, FTC, harmonic series, convergence tests, beyond-BC, and
   Riemann sums. The rule is now written into the style sheet with a table.
