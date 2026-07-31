# Claims ledger — Where a function fails to be differentiable

Article: `_posts/2026-07-30-where-differentiability-fails.md`
Session: 7D article 7 (tier 2), 2026-07-30. AP Calculus sequence 8, Unit 2, topic 2.4.

Verification: `t.js` loads the shipped script in jsdom, steps all four functions across the
h slider, and reads both one-sided quotients back out of the running panel.

---

## Framework grounding

`[EXAM]` Topic 2.4 is titled "Connecting Differentiability and Continuity: Determining When
Derivatives Do and Do Not Exist", sits under enduring understanding FUN-2, and carries
suggested skill 3.E, "Provide reasons or rationales for solutions and conclusions." All from
the CED's Course at a Glance, primary source. The article's structure follows that title
literally: the connection first, then the determination.

**Secondary only:** that FUN-2.A states differentiability implies continuity, and that the
named failures are corners, cusps, vertical tangents, and discontinuities. The Calculus CED
fetch truncates inside Unit 2's sample instructional activities, roughly a hundred lines
before Unit 2's essential knowledge. The mathematics is `[STANDARD]` and needs no source;
what I cannot do is quote the framework's own wording, so the article does not claim to.

## Computed results

All read out of the shipped tool. Every $h$ the prose cites is exactly reachable: the slider
runs $v \in [0, 400]$ with $h = 10^{v/100 - 4}$, so $10^{-4}$ through $1$ all land exactly.

`[COMPUTED]` **Corner**, $|x|$ at 0. One-sided quotients are exactly $-1$ and $+1$ at every
$h$ tested (0.1, 0.001, 0.0001). They are constant, not converging: $|h|/h$ is the sign of
$h$.

`[COMPUTED]` **Cusp**, $x^{2/3}$ at 0. The quotient is $h^{-1/3}$ on the right and its
negative on the left:

```
  h = 0.1      right  +2.1544   left  -2.1544
  h = 0.01     right  +4.6416   left  -4.6416
  h = 0.001    right +10.0000   left -10.0000
  h = 0.0001   right +21.5443   left -21.5443
```

All four pairs cited in the prose, each verified to $10^{-3}$.

`[COMPUTED]` **Vertical tangent**, $x^{1/3}$ at 0. The quotient is $h^{-2/3}$, positive from
both sides:

```
  h = 0.1     +4.6416      h = 0.001    +100.0000
  h = 0.01   +21.5443      h = 0.0001   +464.1589
```

Left and right agree at every $h$, which is the article's point: agreement on $+\infty$ is
not agreement on a number.

`[COMPUTED]` **Discontinuity**, $f(x) = x$ for $x < 0$ and $x + 1$ for $x \geq 0$. The right
quotient sits at exactly $+1$ for every $h$; the left reads $+11$ at $h = 0.1$ and $+1001$ at
$h = 0.001$, growing without bound.

`[COMPUTED]` The first three functions are continuous at 0 and the fourth is not, checked at
$x = \pm 10^{-6}$.

`[STANDARD]` Differentiability implies continuity. The contrapositive — not continuous,
therefore not differentiable — is the form the article gives, because it is the one that
ends an argument.

`[STANDARD]` The converse fails, and the article's first three buttons are the
counterexamples: all continuous at 0, none differentiable there.

`[COMPUTED]` The piecewise example, $f(x) = x^2$ for $x \leq 1$ and $2x - 5$ for $x > 1$:

```
  f(1)            =  1
  left limit      =  1
  right limit     = -3
  left derivative =  2      (from 2x at x = 1)
  right derivative=  2      (from the constant slope of 2x - 5)
```

The slopes match exactly and the values do not, so continuity fails and no derivative exists
at 1. This is the whole reason the article insists on testing continuity first.

`[COMPUTED]` The closing note's two extra functions, verified so the self-test has answers:
$-x^{2/3}$ gives left $+\infty$, right $-\infty$ — a cusp with the signs swapped; and
$\sqrt{|x|}$ gives left $-\infty$, right $+\infty$ — also a cusp.

## Judgment claims

`[JUDGMENT]` "A student who does only the second step can be caught out." The piecewise
example demonstrates the trap rather than asserting how often students fall into it.

`[JUDGMENT]` The classification is entirely a question about the two one-sided quotients,
which is the reason the panel prints them separately and prints nothing else. A design
argument, stated as one.

---

## Flags raised in this session

1. **The slider trap, caught before the test this time.** The h slider originally ran from
   $v = 1$, which puts the smallest $h$ at $1.02 \times 10^{-4}$ rather than $10^{-4}$, while
   the prose cites 0.0001 and the cusp value 21.5443 that goes with it. Changed the minimum
   to 0 before running the harness. That is five instances of this class in 7D; it is now the
   first thing I check when a prose value names a control setting.

2. **Unit 2's essential knowledge is still unreachable**, for the second article running.
   Everything in the framework section above is from the Course at a Glance, which is
   primary but thin — a title, an enduring understanding code, and a skill. If you can get
   me Unit 2's topic pages, topic 2.4 is where it would pay off most in this tier, since
   "determining when derivatives do and do not exist" is the framework naming the article's
   entire content.

3. **Short at 677 words**, against a corpus median of 746. The interactive carries four
   distinct cases and the panel explains each in its own words, so the prose does not repeat
   them. If you want it longer the natural addition is a second piecewise example that
   *passes* both tests, as a contrast to the one that fails continuity.

4. **The vertical tangent is the case worth watching students on.** Left and right agree at
   every $h$, and the panel says so, which makes it the one case where the readout looks like
   success. The article addresses it directly — they agree on something that is not a number
   — but it is the sentence most likely to need saying out loud.
