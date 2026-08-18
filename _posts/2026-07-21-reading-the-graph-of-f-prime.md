---
layout: post
title: "Reading the graph of f′"
date: 2026-07-21
description: "A graph of f' tells you where f increases, decreases, turns, and changes concavity. The main task is keeping the two functions separate."
course: "AP Calculus AB"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "6 min read"
math: true
kind: mechanics
sequence: 17
interactive: true
blurb: "A graph of f' tells you where f increases, decreases, turns, and changes concavity. The main task is keeping the two functions separate"
featured: true
image: "/assets/og/reading-the-graph-of-f-prime.png"
---

A common AP Calculus question gives the graph of $$f'$$ and asks about $$f$$. The difficulty is mostly translation. The picture is not the graph of $$f$$. It is information about $$f$$. Two facts organize nearly everything that follows:

- the sign of $$f'$$ tells you whether $$f$$ is increasing or decreasing
- the slope of $$f'$$ tells you the concavity of $$f$$

## The translation table

| You see on the graph of $$f'$$ | You conclude about $$f$$ |
|---|---|
| $$f'$$ above the $$x$$-axis | $$f$$ is increasing |
| $$f'$$ below the $$x$$-axis | $$f$$ is decreasing |
| $$f'$$ crosses zero from positive to negative | $$f$$ has a relative maximum |
| $$f'$$ crosses zero from negative to positive | $$f$$ has a relative minimum |
| $$f'$$ is decreasing | $$f$$ is concave down |
| $$f'$$ is increasing | $$f$$ is concave up |
| $$f'$$ changes from decreasing to increasing, or the reverse | $$f$$ may have a point of inflection |
| signed area between $$f'$$ and the axis | total change in $$f$$ |

The height of the graph and the shape of the graph answer different questions. The height of $$f'$$ tells you the sign of the derivative, and the shape of $$f'$$ tells you whether the derivative itself is increasing or decreasing.

## A worked example

Suppose the graph of $$f'$$ on $$[0,8]$$ consists of line segments through $$(0,3),\; (2,0),\; (4,-3),\; (6,0),\; (8,3)$$.

<div class="viz" markdown="0">
<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graph of f prime: piecewise linear, starting at (0,3), decreasing to (4,-3), increasing to (8,3)">
  <!-- gridlines: 75 px per unit, x = 0 at 50 and x = 8 at 650 -->
  <g stroke="#ececec" stroke-width="1">
    <line x1="125" y1="40" x2="125" y2="260"/><line x1="200" y1="40" x2="200" y2="260"/>
    <line x1="275" y1="40" x2="275" y2="260"/><line x1="350" y1="40" x2="350" y2="260"/>
    <line x1="425" y1="40" x2="425" y2="260"/><line x1="500" y1="40" x2="500" y2="260"/>
    <line x1="575" y1="40" x2="575" y2="260"/>
    <line x1="50" y1="80" x2="650" y2="80"/><line x1="50" y1="220" x2="650" y2="220"/>
  </g>
  <!-- axes -->
  <line x1="50" y1="150" x2="665" y2="150" stroke="#9a9a9a" stroke-width="1.5"/>
  <line x1="50" y1="30" x2="50" y2="270" stroke="#9a9a9a" stroke-width="1.5"/>
  <!-- f' curve -->
  <polyline points="50,80 200,150 350,220 500,150 650,80" fill="none" stroke="#1f1f1f" stroke-width="3" stroke-linejoin="round"/>
  <!-- zero crossings + turning point -->
  <circle cx="200" cy="150" r="5" fill="#1f1f1f"/>
  <circle cx="500" cy="150" r="5" fill="#1f1f1f"/>
  <circle cx="350" cy="220" r="5" fill="#fff" stroke="#1f1f1f" stroke-width="2.5"/>
  <!-- labels -->
  <g font-family="Hanken Grotesk, sans-serif" font-size="15" fill="#5c5c5c">
    <text x="195" y="140">2</text><text x="345" y="145">4</text><text x="495" y="140">6</text><text x="645" y="143">8</text>
    <text x="34" y="85">3</text><text x="26" y="226">−3</text>
    <text x="600" y="60" font-weight="700" fill="#1f1f1f" font-style="italic">y = f ′(x)</text>
  </g>
</svg>
<p class="viz-caption">The graph of the <em>derivative</em>. Filled dots: where f ′ crosses zero, the candidates for extremes of f. Open dot: where f ′ itself bottoms out, which is a point of inflection of f, not a minimum of f.</p>
</div>

Where is $$f$$ increasing? Wherever $$f'>0$$, so $$f$$ increases on $$(0,2)$$ and $$(6,8)$$. It does not matter that $$f'$$ is decreasing on $$(0,2)$$. The derivative is still positive there, so $$f$$ is increasing.

Where does $$f$$ have a relative maximum? At $$x=2$$, because $$f'$$ changes from positive to negative there. At $$x=6$$, $$f'$$ changes from negative to positive, so $$f$$ has a relative minimum.

Where is $$f$$ concave down? Where $$f'$$ is decreasing, and that occurs on $$(0,4)$$. Likewise, $$f$$ is concave up on $$(4,8)$$, where $$f'$$ is increasing. The point $$x=4$$ is a point of inflection because the concavity changes there.

## Recovering values of $$f$$

If one value of $$f$$ is known, [signed area under $$f'$$](/2026/07/17/fundamental-theorem-from-the-ground-up.html) gives the rest. Suppose $$f(0)=1$$, so that

$$f(8) = f(0)+\int_0^8 f'(x)\,dx$$

From $$0$$ to $$2$$, the graph contributes a triangle of area $$3$$. From $$2$$ to $$6$$, the graph is below the axis and contributes $$-6$$. From $$6$$ to $$8$$, it contributes another $$3$$, so $$f(8) = 1+3-6+3 = 1$$. The function ends at the same value where it began, even though it increased, decreased, and increased again in between.

To find an absolute minimum, evaluate $$f$$ at the relevant candidates. Here, $$f(0)=1,\; f(2)=4,\; f(6)=-2,\; f(8)=1$$, so the absolute minimum occurs at $$x=6$$. No formula for $$f$$ was needed.

## Three common mistakes

## Treating the picture as $$f$$

The lowest point on the graph of $$f'$$ is not automatically a minimum of $$f$$. A minimum of $$f'$$ says something about the slope of $$f$$ and therefore about concavity, and extrema of $$f$$ are found by looking for sign changes in $$f'$$.

## Assuming $$f'=0$$ is enough

A zero of $$f'$$ is only a critical point. For a relative maximum or minimum, the sign of $$f'$$ must change, and if $$f'$$ touches zero and remains positive on both sides, $$f$$ keeps increasing.

## Answering about the wrong function

It helps to label conclusions explicitly. Write “$$f$$ is increasing because $$f'>0$$” rather than simply “increasing.”

<div class="article-note" markdown="1">
That small habit keeps the graph and the function it describes from being confused.
</div>
