# AP Calculus sequence — proposed ordering

Status: **awaiting Katherine's approval.** No front matter is written until this is agreed.

The AP Calculus band currently holds 9 articles. 7D adds 22, giving 31. The `sequence` field
sets display order on the resources index, so the whole band has to be renumbered once.

## The principle

**Sequence follows the College Board's unit order, and within a unit, its topic order.**
Verified against the *AP Calculus AB and BC Course and Exam Description* (the 2026-27
clarifications document confirms course content is unchanged):

| Unit | Title |
|---|---|
| 1 | Limits and Continuity |
| 2 | Differentiation: Definition and Fundamental Properties |
| 3 | Differentiation: Composite, Implicit, and Inverse Functions |
| 4 | Contextual Applications of Differentiation |
| 5 | Analytical Applications of Differentiation |
| 6 | Integration and Accumulation of Change |
| 7 | Differential Equations |
| 8 | Applications of Integration |
| 9 | Parametric Equations, Polar Coordinates, and Vector-Valued Functions (BC) |
| 10 | Infinite Sequences and Series (BC) |

AB and BC stay interleaved in one band, as they are today — a BC-only topic sits at its
natural unit position rather than in a separate block. That is already how Euler's method
sits between the FTC and the series articles.

**Writing order and display order are different things.** The tier numbering in your brief
is the order you want them written; the `sequence` numbers below are the order a reader
meets them. Where the two disagree I have followed the course, and marked it.

## The proposed sequence

`seq` is the new value. `was` is the current one, for the nine that already exist.

| seq | was | Unit | Article | Level | kind |
|---|---|---|---|---|---|
| 1 | 1 | — | Notation in AP Calculus | AB & BC | mechanics |
| 2 | — | 1 | What a limit claims, and what it does not | AB & BC | foundations |
| 3 | — | 1 | Indeterminate forms and the algebra that resolves them | AB & BC | mechanics |
| 4 | — | 1 | Continuity's three conditions, and the ways it fails | AB & BC | foundations |
| 5 | — | 1 | Limits at infinity and end behavior | AB & BC | mechanics |
| 6 | — | 1 | The Intermediate Value Theorem and how to invoke it | AB & BC | mechanics |
| 7 | — | 2 | The derivative as a limit | AB & BC | foundations |
| 8 | — | 2 | Where a function fails to be differentiable | AB & BC | foundations |
| 9 | — | 2 | The rules, and choosing among them | AB & BC | mechanics |
| 10 | — | 3 | The chain rule and reading the layers | AB & BC | mechanics |
| 11 | — | 3 | Implicit differentiation | AB & BC | mechanics |
| 12 | — | 3 | Derivatives of inverse functions | AB & BC | mechanics |
| 13 | — | 4 | Particle motion: position, velocity, acceleration, speed | AB & BC | foundations |
| 14 | 3 | 4 | A procedure for related rates | AB | mechanics |
| 15 | — | 4 | Linearization and the tangent line as approximation | AB & BC | foundations |
| 16 | — | 4 | L'Hôpital's rule and when it applies | AB & BC | mechanics |
| 17 | — | 5 | The Mean Value Theorem and the Extreme Value Theorem | AB & BC | mechanics |
| 18 | 2 | 5 | Reading the graph of f′ | AB | mechanics |
| 19 | — | 5 | Optimization as a procedure | AB & BC | mechanics |
| 20 | 5 | 6 | Riemann sums and the definition of the integral | AB | foundations |
| 21 | 6 | 6 | The Fundamental Theorem of Calculus from first principles | AB | foundations |
| 22 | — | 6 | Accumulation functions and the second Fundamental Theorem | AB & BC | foundations |
| 23 | — | 6 | Integration by parts, and partial fractions | BC | mechanics |
| 24 | — | 6 | Improper integrals | BC | mechanics |
| 25 | 7 | 7 | Euler's method and the effect of step size | BC | foundations |
| 26 | — | 7 | Logistic growth | BC | foundations |
| 27 | — | 8 | Area between curves, and average value of a function | AB & BC | foundations |
| 28 | — | 9 | Parametric, vector, and polar: three systems, one calculus | BC | foundations |
| 29 | 8 | 10 | The harmonic series and conditional convergence | BC | foundations |
| 30 | 9 | 10 | Choosing a convergence test | BC | mechanics |
| 31 | 10 | 10 | Approximation by Taylor polynomials | BC | foundations |

Nine existing articles move; none changes any field but `sequence`. Newton's method is
untouched — it carries `kind: beyond` and lives in the Looking ahead band.

## Where I departed from your tier order, and why

**Unit 1.** Your tiers run limit → continuity → limits at infinity → indeterminate forms →
IVT. The CED runs limits, then algebraic manipulation (1.6, which is where indeterminate
forms live), then continuity (1.10–1.13), then asymptotes and limits at infinity (1.14–1.15),
then IVT (1.16). I have put indeterminate forms third and continuity fourth to match. If you
teach continuity before the algebra, say so and I will swap them back — this is a teaching
preference, not a correctness question.

**Unit 6.** Your tier 4 places accumulation functions before area between curves, which I
have kept, but I have put your new accumulation article *after* the existing FTC article
rather than before it. Your FTC piece already builds the area function from first principles;
the new one is the notational and applied companion, and reads better second.

**Everything else** follows your tier order exactly.

## Two things to decide

**Consecutive numbering, or gaps?** The table above numbers 1–31 consecutively. The
alternative is to number by tens — 10, 20, 30 — so a future insertion never renumbers
anything. Consecutive is more readable in front matter; gapped is cheaper to maintain. The
current band already has an accidental gap at 4, which is what consecutive numbering would
tidy up.

**Your brief says eighteen articles; the tiers list twenty-two.** Tiers 1–4 are exactly 18,
which I take to be "the Calculus front half". Tier 5 — integration by parts and partial
fractions, improper integrals, logistic growth, and parametric/vector/polar — is four more,
all BC, all beyond the front half. I have planned for all 22. Tell me if tier 5 is meant for
a later program instead, in which case sequences 23, 24, 26 and 28 come out and the rest
close up.
