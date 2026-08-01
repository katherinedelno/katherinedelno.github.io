---
layout: post
title: "Reading the graph of f′"
date: 2026-07-21
description: "The exam's favorite question hands you the derivative and asks about the function. The translation table, a worked example, and the three standing traps."
course: "AP Calculus AB"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
kind: mechanics
sequence: 17
interactive: true
blurb: "The translation table for the exam's favorite question"
featured: true
---

Every AP Calculus exam contains some version of this question: *the figure shows the graph of $$f'$$, the derivative of $$f$$*, followed by questions about $$f$$ itself. It is one of the most-missed problem types in the course, and almost every miss traces back to a single cause. At some point, the student's eyes start treating the picture as the graph of $$f$$.

The picture is not $$f$$. The picture is a report about $$f$$, written in a different language, and answering the questions means translating.

## The translation table

Everything on this problem type follows from two facts: the sign of $$f'$$ controls the direction of $$f$$, and the slope of $$f'$$ controls the concavity of $$f$$.

| You see on the graph of $$f'$$... | You conclude about $$f$$... |
|---|---|
| $$f'$$ above the $$x$$-axis | $$f$$ is increasing |
| $$f'$$ below the $$x$$-axis | $$f$$ is decreasing |
| $$f'$$ crosses zero, positive to negative | $$f$$ has a relative maximum there |
| $$f'$$ crosses zero, negative to positive | $$f$$ has a relative minimum there |
| $$f'$$ is decreasing | $$f$$ is concave down |
| $$f'$$ is increasing | $$f$$ is concave up |
| $$f'$$ turns around (its own max or min) | $$f$$ has a point of inflection |
| area trapped between $$f'$$ and the axis | total change in $$f$$ (signed) |

Notice what is not in the table: the height of a bump on the graph, or the location of its peaks. Those features of $$f'$$ answer questions about concavity and $$f''$$, not questions about where $$f$$ is largest.

## A worked example

The graph below shows $$f'$$ (not $$f$$) on the interval $$[0, 8]$$: line segments from $$(0,3)$$ down through $$(2,0)$$ to $$(4,-3)$$, then back up through $$(6,0)$$ to $$(8,3)$$.

<div class="viz" markdown="0">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graph of f prime: piecewise linear, starting at (0,3), decreasing to (4,-3), increasing to (8,3)">
  <!-- gridlines -->
  <g stroke="#ececec" stroke-width="1">
    <line x1="130" y1="40" x2="130" y2="260"/><line x1="210" y1="40" x2="210" y2="260"/>
    <line x1="290" y1="40" x2="290" y2="260"/><line x1="370" y1="40" x2="370" y2="260"/>
    <line x1="450" y1="40" x2="450" y2="260"/><line x1="530" y1="40" x2="530" y2="260"/>
    <line x1="610" y1="40" x2="610" y2="260"/>
    <line x1="50" y1="80" x2="650" y2="80"/><line x1="50" y1="220" x2="650" y2="220"/>
  </g>
  <!-- axes -->
  <line x1="50" y1="150" x2="660" y2="150" stroke="#9a9a9a" stroke-width="1.5"/>
  <line x1="50" y1="30" x2="50" y2="270" stroke="#9a9a9a" stroke-width="1.5"/>
  <!-- f' curve -->
  <polyline points="50,80 210,150 370,220 530,150 650,80" fill="none" stroke="#1f1f1f" stroke-width="3" stroke-linejoin="round"/>
  <!-- zero crossings + turning point -->
  <circle cx="210" cy="150" r="5" fill="#1f1f1f"/>
  <circle cx="530" cy="150" r="5" fill="#1f1f1f"/>
  <circle cx="370" cy="220" r="5" fill="#fff" stroke="#1f1f1f" stroke-width="2.5"/>
  <!-- labels -->
  <g font-family="Hanken Grotesk, sans-serif" font-size="15" fill="#5c5c5c">
    <text x="205" y="140">2</text><text x="365" y="145">4</text><text x="525" y="140">6</text><text x="640" y="143">8</text>
    <text x="34" y="85">3</text><text x="26" y="226">−3</text>
    <text x="600" y="60" font-weight="700" fill="#1f1f1f" font-style="italic">y = f ′(x)</text>
  </g>
</svg>
<p class="viz-caption">The graph of the <em>derivative</em>. Filled dots: where f ′ crosses zero, the candidates for extremes of f. Open dot: where f ′ itself bottoms out, which is a point of inflection of f, not a minimum of f.</p>
</div>

**Where is $$f$$ increasing?** Wherever $$f'$$ is positive. Read heights, not direction: $$f$$ increases on $$(0,2)$$ and $$(6,8)$$. It makes no difference that $$f'$$ is falling on $$(0,2)$$; it is positive there, so $$f$$ rises.

**Where does $$f$$ have a relative maximum?** At $$x = 2$$, because $$f'$$ changes from positive to negative there. That sentence, naming the sign change with its direction at the point, is the full justification, and the exam wants exactly that sentence. At $$x = 6$$ the sign change runs negative to positive, so $$f$$ has a relative minimum there.

**Where is $$f$$ concave down?** Wherever $$f'$$ is decreasing, which is $$(0,4)$$. It is concave up where $$f'$$ increases, on $$(4,8)$$. The point of inflection sits at $$x = 4$$, the open dot, where $$f'$$ turns around. The justification: $$f''$$ changes sign at $$x = 4$$, since $$f'$$ changes from decreasing to increasing there.

**If $$f(0) = 1$$, what is $$f(8)$$?** Use the [Fundamental Theorem](/2026/07/17/fundamental-theorem-from-the-ground-up.html) to accumulate the graph's signed areas. The triangles: from 0 to 2, area $$\tfrac12(2)(3) = 3$$ above the axis; from 2 to 6, area $$\tfrac12(4)(3) = 6$$ below the axis, which counts as $$-6$$; from 6 to 8, another $$+3$$. So

$$f(8) = f(0) + \int_0^8 f'(x)\,dx = 1 + 3 - 6 + 3 = 1.$$

The function ends exactly where it started. It climbed, fell further, and climbed back. Everything about $$f$$ was recoverable from a picture of $$f'$$ and one starting value.

**Where does $$f$$ attain its absolute minimum on $$[0,8]$$?** The candidates are the endpoints and the negative-to-positive crossing at $$x = 6$$. Running totals of accumulated area give $$f(0)=1$$, $$f(2) = 4$$, $$f(6) = -2$$, and $$f(8) = 1$$. The absolute minimum is $$f(6) = -2$$. Notice that the reasoning never needed a formula for $$f$$.

## The three traps

**Trap 1: treating the picture as $$f$$.** The most tempting wrong answer in the example above is "$$f$$ has a minimum at $$x = 4$$," because that is where the picture has a minimum. But the picture is $$f'$$, and the minimum of $$f'$$ is where $$f$$ bends, not where it bottoms out. Whenever you feel the pull to describe what the drawn graph is doing, stop and ask whether you are reporting the height of the graph or its shape. Questions about the direction and extremes of $$f$$ use only heights, meaning signs. Questions about the concavity of $$f$$ use only shape, meaning slopes.

**Trap 2: "$$f'$$ is zero, so there is an extreme."** Zero is not enough; the sign must actually change. If $$f'$$ touches zero and bounces back up, picture the graph dipping to the axis at a single point and rising again, then $$f$$ merely pauses and never turns. The exam plants this regularly. The justification sentence protects you: if you cannot truthfully write "changes from positive to negative," there is no maximum.

**Trap 3: answering about the wrong function.** After five minutes inside a problem, "where is the function increasing?" quietly gets answered about $$f'$$, that is, about where the drawn graph rises. Anchor yourself by labeling every conclusion as you go. Writing the letter $$f$$ or $$f'$$ in front of each fact is a two-second habit that catches the swap while it is still cheap to fix.

## Why the exam loves this question

It cannot be done by memorized procedure. There is no formula to differentiate and nothing to plug in, just a picture and the definitions. That makes it the purest test of whether the chain from sign of derivative to behavior of function actually lives in your head. Master the translation table and its justification sentences, and this becomes one of the most predictable point-earners on the exam. Graders ask for the same three sentences every year.

<div class="article-note" markdown="1">
A self-test: sketch any wavy $$f'$$ you like, then narrate the story of $$f$$ from left to right. It rises here, peaks there, bends at this point, bottoms out over there, with a justification for each claim. If a friend can sketch a plausible $$f$$ from your narration alone, you have won.
</div>
