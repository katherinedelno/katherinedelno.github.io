---
layout: post
title: "Which chi-square test? A short guide to choosing the right one"
date: 2026-07-15
description: "Goodness-of-fit, independence, or homogeneity — how to tell which chi-square procedure a problem calls for, and the conditions to check before you run it."
read_time: "5 min read"
---

On the AP Statistics exam, students rarely lose chi-square points because they can't compute the statistic. They lose them because they run the wrong test, or skip the conditions that justify running it at all. All three chi-square procedures use the same arithmetic — the sum of (observed − expected)² divided by expected — but they answer different questions, and the exam expects you to recognize which question you are being asked.

Here is the distinction, in the order I teach it.

## Goodness-of-fit

One categorical variable, one sample. You have a claimed distribution — a spinner is fair, blood types follow certain percentages, customers arrive evenly across weekdays — and you are testing whether your observed counts are consistent with it. The expected counts come from the claim (the total times each claimed proportion). Degrees of freedom are the number of categories minus one.

## Test for independence

One sample, two categorical variables recorded on each individual. You take a single group of people and classify each one two ways — say, grade level and preferred study method — and ask whether the two variables are associated. The data live in a two-way table, and the degrees of freedom are (rows − 1) × (columns − 1).

## Test for homogeneity

Two or more separate samples, one categorical variable. Here you have distinct groups collected independently — seniors and juniors surveyed separately, three schools sampled on their own — and you ask whether those groups share the same distribution of one variable. The table and the degrees-of-freedom formula are identical to the independence test; only the question and the data collection differ.

## The tell is in how the data were collected

Independence and homogeneity produce the same numbers, so students often guess between them. Don't guess — read the design. **One sample cross-classified two ways points to independence. Several samples compared on one variable points to homogeneity. A single sample checked against a target distribution is goodness-of-fit.** The way the data were gathered decides the test, not the way the table looks.

## Check the conditions before you compute

All three tests share the same three conditions, and all three are easy points to lose:

- **Random** — the data come from a random sample or a randomized experiment.
- **Expected counts of at least 5** — and this means *expected*, not observed. Checking the observed counts is one of the most common errors I see.
- **Independent observations** — including the 10% condition when sampling without replacement.

## And finish the conclusion properly

State the test statistic, degrees of freedom, and P-value, then compare the P-value to your significance level and write a conclusion *in context* that refers back to the alternative hypothesis. A conclusion that never mentions the actual variables, or that "accepts" the null hypothesis, leaves earned points on the table.

<div class="article-note" markdown="1">
The real goal isn't memorizing three recipes — it's being able to look at an unfamiliar problem under time pressure, decide which test it calls for, and justify that choice on your own. That judgment is what the exam is actually measuring, and it's what we build session by session.
</div>
