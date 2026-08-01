# Claims ledger — Increasing at a decreasing rate

Article: `_posts/2026-07-31-increasing-at-a-decreasing-rate.md`
Session: P2, 2026-07-31. AP Precalculus sequence 1, Unit 1 topics 1.1, 1.2, 1.3.

Source: `ap-precalculus-course-and-exam-description.pdf` via `pdftotext -layout`.

Verification: the four presets' tables were recomputed in Python and compared against the
closed forms. All four are quadratics chosen so that the outputs, the average rates of
change, and the changes in those rates are exact two-decimal values at every one of the
seven inputs.

---

## The definitions the article rests on

`[EXAM]` Increasing, quoted from EK 1.1.A.3: "A function is increasing over an interval of
its domain if, as the input values increase, the output values always increase. That is,
for all $a$ and $b$ in the interval, if $a < b$, then $f(a) < f(b)$." Decreasing is the
mirror statement, EK 1.1.A.4.

`[EXAM]` Average rate of change as a secant slope, quoted from EK 1.3.A.3: "The average rate
of change over the closed interval $[a, b]$ is the slope of the secant line from the point
$(a, f(a))$ to $(b, f(b))$." This is why the tool draws all six secants rather than
describing the third column in words.

`[EXAM]` Concavity, quoted from EK 1.1.B.3 and 1.1.B.4: "The graph of a function is concave
up on intervals in which the rate of change is increasing," and "concave down on intervals
in which the rate of change is decreasing."

`[EXAM]` The same statement again in numerical form, from EK 1.3.B.3: "When the average rate
of change over equal-length input-value intervals is increasing for all small-length
intervals, the graph of the function is concave up." The article uses the numerical version
because it is what the fourth column computes.

## The disambiguation, which is the article's point

`[EXAM]` The compound phrase is examinable in all four of its forms. The CED's own sample
multiple-choice item offers exactly these four options: "increasing at a decreasing rate",
"decreasing at a decreasing rate", "increasing at an increasing rate", "decreasing at an
increasing rate". A separate sample activity has students given phrases such as "the
function is increasing with a decreasing rate" and asked to sketch.

`[EXAM]` **The signed reading is the framework's, and it says so by example.** From the
Unit 3 instructional notes: a student "may say 'From $\pi/2$ to $\pi$ radians, as the angle
increases the values of sine decrease, and over equal-angle intervals, the values of sine
decrease at a decreasing rate.'"

This settles the ambiguity the article is built around, and it is worth spelling out why.
On $[\pi/2, \pi]$ sine falls from 1 to 0 and falls *faster* as it goes. The framework calls
that a **decreasing** rate. So the second half of the phrase tracks the signed rate of
change, not its magnitude, and the counterintuitive consequence follows: a curve that is
falling and flattening out is *decreasing at an increasing rate*.

`[COMPUTED]` Verified numerically on the framework's own example. Sine on $[\pi/2, \pi]$
over six equal intervals gives successive average rates of $-0.0341$, $-0.0999$, $-0.1589$,
$-0.2071$, $-0.2412$, $-0.2588$ — strictly decreasing, and sine is concave down there.
Both halves of the framework's sentence check out.

## Why quadratics

`[EXAM]` From EK 1.3.A.1: "For a linear function, the average rate of change over any length
input-value interval is constant." From EK 1.3.A.2: "For a quadratic function, the average
rates of change over consecutive equal-length input-value intervals can be given by a linear
function." From EK 1.3.B.2: those rates "are changing at a constant rate." From EK 1.3.B.1,
a linear function's rates change "at a rate of zero", which is the article's reason a line
is neither concave up nor concave down.

`[EXAM]` Degree from successive differences, EK 1.5.A.6, cited to explain why the constant
fourth column is a fingerprint rather than a coincidence.

## Rate at a point

`[EXAM]` From EK 1.2.A.2: "The rate of change at a point can be approximated by the average
rates of change of the function over small intervals containing the point, if such values
exist." This is the sentence the closing section leans on to call the third column a
difference quotient before it has that name, and it is the reason the cross-link to
`derivative-as-a-limit` is a real connection rather than a signpost.

## Computed results

The four presets, all on inputs $0$ through $6$:

```
  preset                              f(0..6)                                    ROC              4th col
  x²/4 + 2            increasing   2, 2.25, 3, 4.25, 6, 8.25, 11        +0.25 .. +2.75    +0.5 constant
  −x²/4 + 3x + 2      increasing   2, 4.75, 7, 8.75, 10, 10.75, 11      +2.75 .. +0.25    −0.5 constant
  −x²/4 + 11          decreasing   11, 10.75, 10, 8.75, 7, 4.75, 2      −0.25 .. −2.75    −0.5 constant
  x²/4 − 3x + 11      decreasing   11, 8.25, 6, 4.25, 3, 2.25, 2        −2.75 .. −0.25    +0.5 constant
```

`[COMPUTED]` All four are exact at two decimals at every input, and the four are reflections
of one another, so the family covers the four combinations with a single shape. The third
column is uniformly signed in each case, so the first half of the verdict is unambiguous;
the fourth column is constant in each case, so the second half is too.

`[COMPUTED]` The fourth preset is the one the prose singles out. Its rates run
$-2.75, -2.25, -1.75, -1.25, -0.75, -0.25$ — negative throughout, so the function is
decreasing, and strictly increasing as a sequence, so the rate is increasing. *Decreasing at
an increasing rate*, for a curve that visibly flattens as it falls. This is the case the
colloquial reading gets backwards.

`[COMPUTED]` The closing note's coffee example is the same configuration: temperature falling
toward room temperature, fastest at the start, so the signed rate rises toward zero. Concave
up, decreasing at an increasing rate. Newton's law of cooling is exponential decay toward an
asymptote, which is concave up on its whole domain.

## Placement

Sequence 1. Topics 1.1–1.3 precede the factored-form article's 1.5–1.10, so under the
ordering policy the band shifts again and Precalculus is now in College Board topic order
end to end for the first time: 1.1–1.3, then 1.5–1.10, then 1.12, then composition, then
Unit 2, then Unit 3.

Featured cards sit at display positions 1 and 6. With six articles that is hole-free at
both breakpoints and exact on mobile, and it lets the unit-circle card keep the feature it
has had since the band was created. Position 6 is valid only because it is the band's
*second* featured card — as the first it would fail, since mobile requires an even number of
ordinary cards before a full-width one.
