# Claims ledger — Optimization, and the step that is not calculus

Article: `_posts/2026-07-30-optimization.md`
Session: 7D article 16 (tier 4), 2026-07-30. AP Calculus sequence 19, Unit 5 topics 5.10 and
5.11, with the Candidates Test from 5.5.

Verification: `t.js` loads the shipped script in jsdom with a stubbed canvas context, clicks each
of the three problem buttons, sweeps all 1201 slider positions for each, and reads every panel
row and the full candidate list out of the live DOM. Reference values from SymPy.

---

## Framework grounding

All quotations from the AP Calculus AB and BC Course and Exam Description, read from the copy in
your own Admin folder.

`[EXAM]` **Topic 5.10's suggested skill is 2.A**, "Identify common underlying structures in
problems involving different contextual situations" — quoted in the opening paragraph, and the
reason the article is organised around one structure rather than a catalogue of problem types.

`[EXAM]` **Topic 5.11's suggested skill is 3.F**, "Explain the meaning of mathematical solutions
in context" — the fourth section.

`[EXAM]` **FUN-4.B.1**: "The derivative can be used to solve optimization problems; that is,
finding a minimum or maximum value of a function on a given interval." Quoted almost verbatim.
Learning objective FUN-4.B: "Calculate minimum and maximum values in applied contexts or analysis
of functions."

`[EXAM]` **FUN-4.A.3**, the Candidates Test: "Absolute (global) extrema of a function on a closed
interval can only occur at critical points or at endpoints." Quoted. Topic 5.5's full title is
"Using the Candidates Test to Determine Absolute (Global) Extrema", skill 1.E.

`[EXAM]` **Enduring understanding FUN-4**: "A function's derivative can be used to understand
some behaviors of the function." Topic titles: 5.10 "Introduction to Optimization Problems",
5.11 "Solving Optimization Problems".

`[EXAM]` The definition of a critical point — derivative zero or failing to exist — is FUN-1.C.2,
already quoted in the sequence 17 article and reused here.

## Computed results

`[COMPUTED]` **Problem 1, the fence.** $2x + y = 100$ gives $A(x) = x(100-2x) = -2x^2 + 100x$ on
$[0,50]$. $A'(x) = 100 - 4x$, zero at $x = 25$. Candidates and values, read from the panel:

```
  x = 0     A = 0        endpoint
  x = 25    A = 1250     critical point
  x = 50    A = 0        endpoint
```

Maximum area 1250 square metres at $x = 25$, where $y = 50$. $A'' = -4 < 0$ confirms the
critical point is a maximum independently. Slider 600 lands exactly on $x = 25$.

`[COMPUTED]` **Problem 2, the box.** $V(x) = x(12-2x)^2 = 4x^3 - 48x^2 + 144x$ on $[0,6]$.
$V'(x) = 12(x-2)(x-6)$, zero at $x = 2$ and $x = 6$. Candidates:

```
  x = 0     V = 0        endpoint
  x = 2     V = 128      critical point
  x = 6     V = 0        critical point and endpoint
```

Maximum volume 128 cubic inches at $x = 2$, where the base side is 8 inches. The panel tags
$x = 6$ with both roles and the domain row says so, which is the detail I wanted visible.
Slider 400 lands exactly on $x = 2$.

`[COMPUTED]` **Problem 3, the closest point.** $D^2(x) = x^2 + (x^2-2)^2 = x^4 - 3x^2 + 4$, with
$\frac{d}{dx}D^2 = 2x(2x^2-3)$ vanishing at $x = 0$ and $x = \pm\sqrt{3/2} = \pm 1.224745$. The
panel reports exactly three candidates, all tagged critical point and none tagged endpoint:

```
  x = -1.2247   D² = 1.75    critical point
  x =  0.0000   D² = 4.00    critical point
  x =  1.2247   D² = 1.75    critical point
```

Smallest is $\tfrac74$, so the minimum distance is $\tfrac{\sqrt7}{2} = 1.3228757$, attained at
two points. $\tfrac{d^2}{dx^2}D^2 = 6(2x^2-1)$ is $-6$ at $x = 0$ and $+12$ at
$x = \pm\sqrt{3/2}$, so the second derivative test classifies all three: $x = 0$ is a local
**maximum** of the distance, which is the trap the article names.

`[COMPUTED]` **The panel matches independently written formulas** for the free variable and the
objective at all 1201 slider positions on all three problems, to better than $10^{-4}$ — that
is, exact to the four decimals displayed.

`[COMPUTED]` **The prose arithmetic.** $\sqrt7/2 = 1.3229$ to four decimals; $\sqrt{1.75}$ and
$\sqrt7/2$ agree to the last bit; $12(x-2)(x-6)$ vanishes at $x = 2$ and $x = 6$; the endpoint
values $y = 100-2(50) = 0$ and $12 - 2(6) = 0$ are what force the right ends of the two domains.

## Judgment claims

`[JUDGMENT]` "Fences, boxes, and distances are the same problem wearing different clothes." The
article's thesis, which the interactive then demonstrates by putting all three in one panel with
the same rows.

`[JUDGMENT]` "The step that gets skipped" (of the domain). A claim about student behaviour I
cannot source. It is the article's title and its argument, and the article earns it by showing
that neither domain endpoint appears anywhere in the objective's algebra.

`[JUDGMENT]` "A student who finds one critical point and stops has a defensible-looking answer of
2, which is wrong." The number 2 is computed — $D(0) = 2$ exactly — and the rest is a claim about
a plausible error rather than a measured one.

`[JUDGMENT]` The closing note's exercise, three lines per problem with no differentiating, is the
same shape as the drill in the sequence 9 article and is offered as a habit.

---

## Flags raised in this session

1. **The article shipped with zero cross-links on its first pass**, which is a first for 7D and
   would have left it isolated in a corpus where every neighbour points at something. Three added:
   related rates from 20 July, which is the same translation problem in the other direction; the
   Extreme Value Theorem article at sequence 17, which is what guarantees the extrema exist at
   all; and the differentiability article, for the half of the critical-point definition that
   gets forgotten. The article also grew from 691 to 872 words in the process, which it needed.

2. **The third problem's panel calls its rows "candidates" even though the Candidates Test does
   not apply there.** That is deliberate and the domain row says so in words, but it is the one
   place in the tool where a label is doing something slightly different from what it does
   elsewhere. If it reads as sloppy rather than pointed, the fix is to relabel that row for the
   unbounded case.

3. **The panel reports $D^2$, not $D$.** The canvas title says $D^2(x)$, the objective row is
   labelled in squared units, and the free-variable row prints the actual distance alongside — so
   all three are on screen at once, which is the point of the last section. Worth knowing that a
   reader glancing only at the objective row will read 1.75 and not 1.3229.

4. **872 words**, four `##` headings, one italicised span, three cross-links, all resolving.
   Inside the 650–950 target.

5. **Unit 5 is now half covered and the plan does not finish it.** Sequence 17 took 5.1 and 5.2,
   sequence 18 is your existing f′ article, and this takes 5.5, 5.10, and 5.11. That leaves 5.3
   (intervals of increase and decrease), 5.4 (first derivative test), 5.6 (concavity), 5.7
   (second derivative test), 5.8 (sketching), 5.9 (connecting f, f′, f″), and 5.12 (implicit
   relations, partly covered by the sequence 11 article). Several of those are served by your
   existing "Reading the graph of f′", but concavity and the second derivative test are invoked
   by three articles now without ever having been introduced. Worth a decision before Unit 6.
