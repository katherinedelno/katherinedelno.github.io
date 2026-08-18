---
layout: post
title: "Which chi-square test? Independence or homogeneity"
date: 2026-07-15
description: "The two chi-square tests use the same calculation. The study design determines whether the question is about association within one sample or distributions across several groups."
course: "AP Statistics"
read_time: "5 min read"
math: true
kind: mechanics
sequence: 15
interactive: false
blurb: "The two chi-square tests use the same calculation. The study design determines whether the question is about association within one sample or distributions across several groups"
image: "/assets/og/which-chi-square-test.png"
---

The chi-square tests for independence and homogeneity use the same test statistic:

$$\chi^2 = \sum \frac{(O-E)^2}{E}$$

They also use the same degrees of freedom, $$(r-1)(c-1)$$, and the distinction comes from how the data were collected and what the question asks.

## Test for independence

Use a test for independence when one sample is classified according to two categorical variables. For example, take one random sample of students, and for each student, record grade level and preferred study method. The question is whether those two variables are associated in the population, and the hypotheses concern independence between two categorical variables.

## Test for homogeneity

Use a test for homogeneity when separate groups or samples are compared on one categorical response. For example, sample juniors and seniors separately, and within each group, record preferred study method. The question is whether the distribution of study method is the same across the populations.

## The table can look identical

A two-way table does not reveal by itself which test generated it. The same counts could arise from:

- one sample classified by two variables
- several separate samples measured on one variable

The arithmetic is identical. The design is not, so read the description of data collection before naming the procedure.

## Expected counts

For either test, the expected count in a cell under the null is

$$E = \frac{(\text{row total})(\text{column total})}{\text{grand total}}$$

The chi-square statistic compares observed and expected counts across all cells, and large discrepancies produce a larger value of $$\chi^2$$. The relevant large-count condition is checked using expected counts, not observed counts, and that distinction matters.

## Randomization and independence

The randomization condition depends on the design. A test for independence commonly begins with one random sample, while a homogeneity test uses independent random samples or may arise from a randomized experiment. When sampling without replacement from a finite population, the usual 10% condition supports approximate independence within the sample, and the statistical conditions should match the actual way the data were generated.

## Conclusion

After computing the statistic and p-value, compare the p-value with $$\alpha$$. For a test of independence, the conclusion concerns evidence of an association between the two categorical variables, and for a test of homogeneity, the conclusion concerns evidence that the population distributions differ.

<div class="article-note" markdown="1">
Do not “accept” the null after a large p-value. Failing to reject means the data did not provide convincing evidence for [the alternative](/2026/07/14/writing-parameters-in-ap-statistics.html).
</div>
