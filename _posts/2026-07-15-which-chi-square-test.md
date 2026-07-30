---
layout: post
title: "Which chi-square test? Independence or homogeneity"
date: 2026-07-15
description: "With goodness-of-fit removed from the revised AP Statistics course, the chi-square decision comes down to independence versus homogeneity. Here is how to tell them apart and the conditions to check."
course: "AP Statistics"
read_time: "5 min read"
math: true
kind: mechanics
sequence: 12
interactive: false
blurb: "Independence versus homogeneity, and how to tell them apart"
---

Starting with the revised AP Statistics course, the College Board removed the chi-square goodness-of-fit test. That actually simplifies a question students used to find confusing. The chi-square procedures you will use on the exam now all involve two-way tables, so the real decision is between just two tests: the test for independence and the test for homogeneity.

They are easy to mix up, because they use the same statistic,

$$\chi^2 = \sum \frac{(O - E)^2}{E},$$

and the same degrees of freedom, $$(r-1)(c-1)$$, where $$r$$ and $$c$$ are the number of rows and columns. What separates them is the question being asked and, above all, how the data were collected.

## Test for independence

One sample, two categorical variables. You take a single group of individuals and classify each one two ways, then ask whether the two variables are associated. For example, you survey one group of students and record both their grade level and their preferred study method, and ask whether study method is related to grade level.

## Test for homogeneity

Two or more separate samples, one categorical variable. Here you have distinct groups collected independently, and you ask whether they share the same distribution of a single variable. For example, you survey seniors and juniors separately and compare how each group's study methods are distributed.

## The tell is in how the data were collected

Because the arithmetic is identical, students often guess between the two. Do not guess, read the design. **One sample cross-classified two ways is a test for independence. Several separate groups compared on one variable is a test for homogeneity.** The way the data were gathered decides the test, not the way the table looks on the page.

## A quick example of each

Say you want to know whether study method is related to how students do in a course. If you take one class of 40 students and record, for each student, both their main study method (alone or in a group) and whether they earned an A, you have one sample split by two questions. That is a test for independence.

Now suppose instead you take 40 students who study alone and a separate 40 who study in groups, and record each student's grade. Those are two groups collected separately and compared on one variable. That is a test for homogeneity.

The table looks the same either way, and the computation is identical. The only difference is that in the first case one group was classified by two questions, and in the second, two groups were each asked one.

## Check the conditions before you compute

Both tests share the same three conditions, and all three are easy points to lose:

- **Random**: the data come from a random sample or a randomized experiment.
- **Expected counts of at least 5**: every expected count must satisfy $$E \geq 5$$, and this means expected counts, not observed. Checking the observed counts is one of the most common errors I see.
- **Independent observations**: including the 10% condition when sampling without replacement.

## Finish the conclusion properly

State the test statistic, the degrees of freedom, and the $$P$$-value, then compare the $$P$$-value to your significance level $$\alpha$$ and write a conclusion in context that refers back to the alternative hypothesis. A conclusion that never names the actual variables, or that "accepts" the null hypothesis, leaves earned points on the table.

<div class="article-note" markdown="1">
If you have older review books that still include a goodness-of-fit test for a single categorical variable, that is the piece no longer part of the course. It remains a valid statistical idea, but it will not appear on the current AP exam. The real goal, either way, is being able to look at an unfamiliar problem under time pressure, decide which test it calls for, and justify that choice on your own.
</div>
