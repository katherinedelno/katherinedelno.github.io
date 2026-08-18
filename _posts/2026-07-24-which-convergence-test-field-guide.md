---
layout: post
title: "Choosing a convergence test"
date: 2026-07-24
description: "The form of a series usually suggests which convergence test to try first. A reliable sequence keeps the tests from becoming a disconnected list."
course: "AP Calculus BC"
read_time: "5 min read"
math: true
kind: mechanics
sequence: 30
interactive: false
blurb: "The form of a series usually suggests which convergence test to try first. A reliable sequence keeps the tests from becoming a disconnected list"
image: "/assets/og/which-convergence-test-field-guide.png"
---

The convergence tests are easier to use when they are organized by the structure of the series. A series with factorials suggests a different first move from a series with polynomial terms, and an alternating series raises a different question from a positive one. A reliable decision sequence helps narrow the choice.

## Step 0: check the terms

Always begin with $$\lim_{n\to\infty}a_n$$. If $$\lim_{n\to\infty}a_n\neq0$$, then $$\textstyle\sum a_n$$ diverges by the $$n$$-th term test. For example, $$\textstyle\sum\tfrac{3n}{n+1}$$ diverges because $$\tfrac{3n}{n+1}\to3$$. If the terms do approach zero, the test is inconclusive, and it cannot prove convergence.

## Step 1: look for a special family

## Geometric series

A geometric series has a constant ratio between consecutive terms. For $$\textstyle\sum ar^n$$, the series converges exactly when $$\vert r\vert<1$$, and when it converges, the sum can also be found from the geometric-series formula.

## $$p$$-series

A $$p$$-series has the form $$\textstyle\sum\tfrac{1}{n^p}$$, and it converges exactly when $$p>1$$. [The harmonic series](/2026/07/23/harmonic-series-surprises-of-infinity.html) is the boundary case $$p=1$$, and it diverges. These two families have complete criteria, so they are worth recognizing before using a more general test.

## Step 2: factorials and exponentials suggest the ratio test

The ratio test is especially useful when terms contain $$n!,\; c^n$$, or other multiplicative growth. Compute

$$L = \lim_{n\to\infty} \left\vert \frac{a_{n+1}}{a_n} \right\vert$$

If $$L<1$$, the series converges absolutely. If $$L>1$$, the series diverges. If $$L=1$$, the test is inconclusive.

For example, $$\textstyle\sum\tfrac{2^n}{n!}$$ gives $$\left\vert \tfrac{a_{n+1}}{a_n} \right\vert = \tfrac{2}{n+1} \to0$$, so the series converges. The ratio test is usually a poor choice for ordinary $$p$$-series because it returns $$L=1$$ for both convergent and divergent cases.

## Step 3: algebraic terms suggest comparison

For expressions involving powers and roots of $$n$$, identify the dominant terms. Consider $$\tfrac{n}{n^3+4}$$, which for large $$n$$ behaves like $$\tfrac{n}{n^3} = \tfrac{1}{n^2}$$, and that suggests comparison with a convergent $$p$$-series. For $$\tfrac{1}{\sqrt{n^2+1}}$$, the dominant behavior is $$\tfrac1n$$, and that suggests a divergent benchmark.

Limit comparison is often the cleanest method. If $$\lim_{n\to\infty}\tfrac{a_n}{b_n}=L$$ with $$0<L<\infty$$, then the two positive-term series share the same convergence behavior. Direct comparison can be shorter when the needed inequality is obvious, but the direction matters. Being smaller than a convergent series proves convergence, and being larger than a divergent series proves divergence, while the reverse directions prove nothing.

## Step 4: alternating signs

For an alternating series, check absolute convergence first. Given $$\textstyle\sum(-1)^n b_n$$, test $$\textstyle\sum b_n$$. If the absolute-value series converges, the original series converges absolutely, and if it diverges, then check the alternating series test.

If $$b_n$$ is positive, decreasing, and approaches zero, the alternating series converges conditionally. The alternating series test proves convergence only, and failure of its hypotheses does not prove divergence.

## Step 5: consider the integral test

The integral test is useful when the corresponding function is positive, continuous, decreasing, and easy to integrate. A common example is $$\textstyle\sum\tfrac{1}{n\ln n}$$. The related improper integral is $$\textstyle\int\tfrac{1}{x\ln x}\,dx$$, which becomes simple under $$u=\ln x$$, and the series diverges. By contrast, $$\textstyle\sum\tfrac{1}{n(\ln n)^2}$$ converges. These examples do not fit neatly into the ordinary $$p$$-series family, and the ratio test is inconclusive.

## Three common mistakes

## Treating $$L=1$$ as a conclusion

For the ratio test, $$L=1$$ means the test gives no conclusion. Use another test.

## Using comparison in the wrong direction

If $$0\le a_n\le b_n$$ and $$\textstyle\sum b_n$$ converges, then $$\textstyle\sum a_n$$ converges. If $$a_n\ge b_n\ge0$$ and $$\textstyle\sum b_n$$ diverges, then $$\textstyle\sum a_n$$ diverges. The other two directions are inconclusive.

## Naming a test without checking its hypotheses

A written justification should state the test, verify the relevant conditions, and state the conclusion. For the alternating series test, that means showing that the magnitudes decrease to zero, and for limit comparison, that means showing a positive finite limit and identifying the known comparison series.

## Intervals of convergence

For a power series, the ratio test usually finds the radius of convergence, and the result takes the form $$\vert x-c\vert<R$$. Then check the two endpoints separately. At an endpoint, the ratio test typically becomes inconclusive, so the problem turns back into an ordinary numerical series. One endpoint may converge while the other diverges, and the endpoint analysis is part of the interval.

<div class="article-note" markdown="1">
A useful practice drill is to classify series without solving them. For each one, identify the first test you would try and the feature that suggests it. The choice of test should become a reading skill before it becomes an algebra exercise.
</div>
