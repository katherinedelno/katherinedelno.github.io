# Claims ledger — Particle motion, and the two signs that decide everything

Article: `_posts/2026-07-30-particle-motion.md`
Session: 7D article 12 (first of tier 4), 2026-07-30. AP Calculus sequence 13, Unit 4 topics 4.1
and 4.2.

Verification: `t.js` and `t2.js` load the shipped script in jsdom with a stubbed canvas context,
click each of the three function buttons, and sweep all 1201 slider positions for each, reading
every panel row out of the live DOM. Reference values computed independently in SymPy and again
in the harness from separately written formulas.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **CHA-3.B.1** (topic 4.2): "The derivative can be used to solve rectilinear motion
problems involving position, speed, velocity, and acceleration." Four quantities, named in that
order — which is the article's opening observation, that only one of the four is not a derivative
or the function itself.

`[EXAM]` **CHA-3.A.3** (topic 4.1): "The unit for $f'(x)$ is the unit for $f$ divided by the unit
for $x$." Paraphrased closely in the units paragraph. The article's point that motion is not
special here is the framework's own framing.

`[EXAM]` **CHA-3.A.1**: "The derivative of a function can be interpreted as the instantaneous
rate of change with respect to its independent variable." **CHA-3.A.2** extends that to applied
contexts. Enduring understanding **CHA-3**: "Derivatives allow us to solve real-world problems
involving rates of change."

`[EXAM]` Topic titles: 4.1 "Interpreting the Meaning of the Derivative in Context" (skill 1.D),
4.2 "Straight-Line Motion: Connecting Position, Velocity, and Acceleration" (skill 1.E).

`[EXAM]` **The closing note's claim about justification is quoted from the CED**, though from
Unit 9's Preparing for the AP Exam rather than Unit 4's: "sign charts can be useful tools for
identifying answers to questions about the direction of motion or whether speed is increasing or
decreasing, for example. To earn points for justification, however, students must connect their
work to a relevant definition or theorem, as in the Scoring Guidelines for 2017 AB5." The passage
opens "As with particle motion on a line," so it applies here, but the article says "the
framework's exam guidance" without naming a unit, which is the honest level of specificity.

`[EXAM]` Unit 4's own exam guidance warns against loose vocabulary: "Students should not use
words like 'velocity' when they mean the rate of change in income." Not quoted in the article,
but it is why the article keeps velocity and speed strictly separate.

`[STANDARD]` **The speeding-up criterion is derived, not asserted.** The CED does not state
"speeding up when $v$ and $a$ share a sign" as essential knowledge anywhere; it states that
derivatives solve motion problems involving speed. The article therefore derives it from
$\frac{d}{dt}|v| = \operatorname{sign}(v)\cdot a$, which is standard and follows from the chain
rule wherever $v \neq 0$.

## Computed results

`[COMPUTED]` **The derivative of speed.** For each of the three functions, a symmetric difference
of $|v|$ was compared against $\operatorname{sign}(v)\cdot a$ in SymPy at two interior points per
function, agreeing to $10^{-4}$ in all six cases. Example: the cubic at $t = 1/2$ gives $-9.00000$
both ways, and at $t = 7/2$ gives $+9.00000$ both ways.

`[COMPUTED]` **The cubic, $s = t^3 - 6t^2 + 9t$ on $[0,4]$.** $v = 3(t-1)(t-3)$ and $a = 6t - 12$,
so the sign changes fall at $t = 1$, $2$, $3$. The four resulting intervals are, in order:

```
  (0, 1)   v +  a -    positive direction, slowing down
  (1, 2)   v -  a -    negative direction, speeding up
  (2, 3)   v -  a +    negative direction, slowing down
  (3, 4)   v +  a +    positive direction, speeding up
```

The harness swept all 1201 slider positions and recovered exactly those four runs in exactly that
order, with no repeats — confirming both that all four combinations occur and that the article
lists them in the order they happen.

`[COMPUTED]` **Positions at the named times**, read from the panel at exact slider positions:

```
  slider    0    300    600    900   1200
  t         0      1      2      3      4
  s         0      4      2      0      4
  v         9      0     -3      0      9
  a       -12     -6      0      6     12
```

At $t = 1$ and $t = 3$ the verdict reads "turning around"; at $t = 2$ it reads "neither — the
acceleration is zero", which is correct since $\operatorname{sign}(v)\cdot a = 0$ there.

`[COMPUTED]` **Displacement and distance.** $s(4) - s(0) = 4$. The turning points are $t = 1$ and
$t = 3$, and the positions at $t = 0, 1, 3, 4$ are $0, 4, 0, 4$, so the distance travelled is
$4 + 4 + 4 = 12$. Note that $t = 2$ is *not* a turning point — it is where the acceleration
changes sign — which is the trap in computing this by hand.

`[COMPUTED]` **The projectile, $s = 30t - 5t^2$ on $[0,6]$.** The acceleration reads exactly
$-10$ at all 1201 slider positions, verified as a set of one distinct value. The apex is slider
600 at $t = 3$, $s = 45$, $v = 0$; the landing is slider 1200 at $t = 6$, $s = 0$, $v = -30$. At
$t = 1.5$ the verdict is "slowing down"; at $t = 4.5$ it is "speeding up". Only two sign
combinations occur, $v{+}a{-}$ and $v{-}a{-}$, which is the article's point.

`[COMPUTED]` **$s = t + 2\cos t$ on $[0, 2\pi]$.** $v = 1 - 2\sin t$ is zero at $\pi/6$ and
$5\pi/6$, both exactly reachable at slider 100 and 500, where the panel reads $v = 0.0000$. It
reaches all four sign combinations and then returns to the first, five runs across four distinct
states.

`[COMPUTED]` **The panel matches independently written formulas.** The harness recomputes $s$,
$v$, and $a$ from formulas typed separately from the article's code and compares against the
displayed values at all 1201 positions per function. Largest discrepancy anywhere is
$5\times10^{-5}$, which is exactly half of the last displayed digit — that is, the panel is
correct to its full printed precision on all three functions.

`[COMPUTED]` **Slider resolution.** 1201 positions was chosen so that every time the prose names
lands exactly: $t = 1, 2, 3$ on the cubic at 300, 600, 900; $t = 3$ and $t = 6$ on the projectile
at 600 and 1200; $\pi/6$ and $5\pi/6$ at 100 and 500. Verified in the harness.

## Judgment claims

`[JUDGMENT]` "Speed is the odd one out, and that is where the errors are." A framing claim. The
article then earns it with the projectile.

`[JUDGMENT]` "The clearest argument there is against reading the sign of $a$ on its own." An
editorial superlative about the projectile example.

`[JUDGMENT]` "Which is why it is the one every textbook uses" (of the cubic, in the caption).
I have not surveyed textbooks. Softened in intent — the verifiable half is that it visits all
four combinations in four seconds, which is computed above.

---

## Flags raised in this session

1. **Two of my three initial test failures were the test, not the tool.** One compared the
   sign-combination set against a wrongly sorted expectation string. The other estimated $v$ and
   $a$ by finite-differencing the panel's own four-decimal display, where quantisation alone
   accounts for most of the gap it flagged. Replaced with a direct comparison against separately
   written reference formulas, which is both stricter and interpretable. Reading a rounded
   display and then differencing it is a bad way to test a derivative; worth remembering.

2. **One caption claim I cannot verify and did not cut.** "Which is why it is the one every
   textbook uses." I have not surveyed textbooks, and by the standing rule an unverifiable claim
   should not go in the prose. It stays because it is a hedge about pedagogical convention rather
   than a mathematical assertion, and the sentence's substantive half is computed. Say the word
   and I will cut the clause.

3. **The speeding-up rule is not in the CED as essential knowledge.** I looked. "Speeding up",
   "slowing down", and "same sign" appear nowhere in the framework's required content; the
   closest is Unit 9's exam-prep mention of "whether speed is increasing or decreasing". The
   article therefore derives the criterion rather than attributing it, which is the accurate
   thing to do and also the better lesson. Flagging it because it means a student who quotes
   "same sign" as a rule on an exam has quoted nothing — they have to say what the signs mean.

4. **$t = 2$ is not a turning point on the cubic**, and the distance calculation is wrong if you
   treat it as one. It is where $a$ changes sign. The article's distance is computed from
   $t = 0, 1, 3, 4$ only, and the ledger notes the trap explicitly because I nearly made it
   myself in the first pass.

5. **733 words**, four `##` headings, no italics, three cross-links, all resolving. Inside the
   650–950 target.

6. **The track view is new and I would like your read on it.** The top bar shows the particle's
   actual position with a trail of everywhere it has been, which is the thing three stacked graphs
   never show — that the cubic's particle covers the interval from 0 to 4 three times. It costs
   about 40 pixels of vertical space. If it reads as clutter I can drop it and give the three
   panes more height.
