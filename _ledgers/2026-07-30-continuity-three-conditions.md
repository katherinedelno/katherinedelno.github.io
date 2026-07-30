# Claims ledger — Continuity's three conditions, and the ways it fails

Article: `_posts/2026-07-30-continuity-three-conditions.md`
Session: 7D article 2 (tier 1), 2026-07-30. AP Calculus sequence 4, Unit 1.

Verification: `t.js` loads the article's own `<script>` into jsdom, steps every case, and
reads the three-condition checklist, the verdict, and the repair button's state back out of
the running tool. 19 assertions, all passing.

**Correction to the previous ledger.** The 7D-1 ledger recorded that I could not reach the
Calculus CED's essential-knowledge statements because the fetch truncated. That was wrong.
The fetch saved its full 105,672 characters to a file and only the *display* was truncated;
the Unit 1 topic detail was there the whole time, at lines 2603–2800. Every `[EXAM]` claim
below is sourced. The 7D-1 article is unaffected in substance — the two claims cut from it
were about the free-response format, which is elsewhere in the document — but the reason I
gave for cutting them was mistaken.

---

## The definition

`[EXAM]` The three conditions, quoted from LIM-2.A.2 (topic 1.11, Defining Continuity at a
Point): "A function $f$ is continuous at $x = c$ provided that $f(c)$ exists,
$\lim_{x \to c} f(x)$ exists, and $\lim_{x \to c} f(x) = f(c)$."

`[EXAM]` The three named types, quoted from LIM-2.A.1 (topic 1.10, Exploring Types of
Discontinuities): "Types of discontinuities include removable discontinuities, jump
discontinuities, and discontinuities due to vertical asymptotes." The article uses exactly
these three names and no others.

`[EXAM]` Repair, from LIM-2.C.1 (topic 1.13, Removing Discontinuities): "If the limit of a
function exists at a discontinuity in its graph, then it is possible to remove the
discontinuity by defining or redefining the value of the function at that point, so it
equals the value of the limit." This is the justification for the repair button, and for the
claim that repairability depends on the *second* condition rather than the first or third.

`[EXAM]` Continuity on an interval, from LIM-2.B.1 (topic 1.12): "A function is continuous
on an interval if the function is continuous at each point in the interval."

`[EXAM]` The shortcut, quoted from LIM-2.B.2: "Polynomial, rational, power, exponential,
logarithmic, and trigonometric functions are continuous on all points in their domains." The
article reproduces the list in full and stresses the qualifier, which is the load-bearing
part.

`[EXAM]` Piecewise continuity at a boundary, from LIM-2.C.2: "the value of the expression
defining the function on one side of the boundary must equal the value of the expression
defining the other side of the boundary, as well as the value of the function at the
boundary."

## Computed results

All read out of the shipped tool, not recomputed.

`[COMPUTED]` The five cases produce exactly the condition patterns the prose claims:

```
  case              cond 1   cond 2   cond 3   verdict                     repair
  Continuous          ok       ok       ok     Continuous at x = 2          off
  No value           fail      ok        -     Removable discontinuity      on
  Wrong value         ok       ok      fail    Removable discontinuity      on
  Sides disagree      ok      fail       -     Jump discontinuity           off
  Unbounded          fail     fail       -     vertical asymptote           off
```

`[COMPUTED]` "No value" fails only the first condition: the limit is still 4.

`[COMPUTED]` "Wrong value" satisfies the first two and fails the third: $f(2) = 1$ while the
limit is 4.

`[COMPUTED]` "Sides disagree" reports one-sided values of 4.00 and 1.00, evaluated at
$2 \mp 10^{-7}$.

`[COMPUTED]` Repair is enabled for exactly the two cases where the limit exists, and
disabled for the other three. Applying it to either removable case turns all three
conditions true and the verdict to "Continuous at x = 2".

`[STANDARD]` $1/(x-2)^2$ is unbounded above from both sides, since the square is positive on
either side of 2. The article uses the squared form rather than $1/(x-2)$ so that both
one-sided behaviours are the same, which keeps the case cleanly about the asymptote rather
than also about a sign change.

## Judgment claims

`[JUDGMENT]` Students lose points by reporting that a rational function is "continuous
everywhere", or by treating a removable hole as disqualifying the function from continuity
anywhere. Asserted from teaching experience, not sourced. The underlying mathematics —
LIM-2.B.2's "in their domains" qualifier — is sourced.

`[JUDGMENT]` The closing note's claim that "the limit existing is what makes repair
possible" is the better rule than "removable discontinuities are repairable". This is a
pedagogical preference, though LIM-2.C.1 does state the condition in exactly that direction.

---

## Flags raised in this session

1. **I gave you a wrong reason last session.** I said the Calculus CED detail was out of
   reach and asked you to supply it. It was already on disk from a fetch I had made — I
   grepped that file for unit names, found them, and never went back for the topic detail.
   Nothing shipped incorrectly as a result, but the two claims cut from 7D-1 were cut on a
   premise that did not hold, and the standing warning I gave about the rest of 7D being
   thin on exam claims is withdrawn. This article has six sourced `[EXAM]` claims.

2. **7D-1 may want its cut section back.** Now that I can read the framework, the honest
   position is that one of the two cut claims was probably wrong anyway (free-response graph
   questions in AB typically supply $f'$), and the other had no basis. I would leave 7D-1 as
   it stands. Raising it because the reason for the cut has changed even though the outcome
   is the same.

3. **The two removable cases share a name but not a broken condition.** "No value" breaks
   the first, "wrong value" breaks the third, and the framework calls both removable. That
   is a genuine feature of the taxonomy rather than an artefact of my presentation, and the
   article says so explicitly, because a student who thinks "removable" names a single
   failure will misread one of the two.

4. **Nothing about one-sided continuity.** The framework's interval topic (1.12) does not
   raise endpoint or one-sided continuity in its essential knowledge, so the article does
   not either. If your students meet it in a textbook treatment, that is a gap worth
   knowing about.
