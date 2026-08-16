---
layout: post
title: "Writing parameters in AP Statistics"
date: 2026-07-14
description: "Define the population quantity before beginning inference. The symbol, variable, and population should all be explicit."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: mechanics
sequence: 10
interactive: false
blurb: "Define the population quantity before beginning inference. The symbol, variable, and population should all be explicit"
image: "/assets/og/writing-parameters-in-ap-statistics.png"
---

Inference is about population parameters.

The data give us sample statistics.

A clear solution should distinguish those two before any interval or test is carried out.

## Parameter versus statistic

A parameter is a fixed numerical characteristic of a population.

A statistic is calculated from a sample.

For a proportion,

$$p$$

denotes the population proportion, while

$$\hat p$$

denotes a sample proportion.

For a mean,

$$\mu$$

denotes the population mean, while

$$\bar x$$

denotes a sample mean.

Hypotheses are statements about parameters.

So

$$H_0:p=0.60$$

is meaningful.

A null hypothesis written as

$$H_0:\hat p=0.60$$

is not the same claim because $$\hat p$$ is already observed from the sample.

## A useful definition pattern

A parameter definition should name three things:

- the symbol
- the variable or characteristic being measured
- the population

For example:

$$p = \text{the true proportion of all students at the school who bike to school}.$$

Or:

$$\mu = \text{the true mean wait time, in minutes, for all visits to the coffee shop}.$$

The word “true” is useful shorthand for emphasizing that the quantity belongs to the population rather than the sample.

## One proportion

Suppose a school claims that 60% of students bike to school and you suspect the true proportion is lower.

Define

$$p = \text{the true proportion of all students at the school who bike to school}.$$

Then

$$H_0:p=0.60$$

and

$$H_a:p<0.60.$$

## One mean

Suppose a coffee shop advertises a mean wait time of 4 minutes.

Define

$$\mu = \text{the true mean wait time, in minutes, for all visits to the shop}.$$

A two-sided test would use

$$H_0:\mu=4$$

and

$$H_a:\mu\neq4.$$

## Two proportions

Suppose we compare first-year and second-year students.

Define

$$p_1 = \text{the true proportion of first-year students who use the tutoring center}$$

and

$$p_2 = \text{the true proportion of second-year students who use the tutoring center}.$$

Then a no-difference null is

$$H_0:p_1-p_2=0.$$

The order of the groups should remain consistent throughout the problem.

## Two means

For two independent populations,

$$\mu_1-\mu_2$$

describes the difference in population means.

For example,

$$\mu_1 = \text{the true mean weekly study time for athletes}$$

and

$$\mu_2 = \text{the true mean weekly study time for non-athletes}.$$

A no-difference null is

$$H_0:\mu_1-\mu_2=0.$$

## Paired data

Paired data use one population of differences.

If each student has a before and after score, define a difference such as

$$d=\text{after}-\text{before}.$$

Then

$$\mu_d = \text{the true mean after-minus-before difference for the population}.$$

A null hypothesis may be

$$H_0:\mu_d=0.$$

This is a one-sample mean problem on the differences.

It is not a two-independent-sample mean problem.

## Confidence intervals use the same parameters

A [confidence interval](/2026/07/25/what-95-percent-confident-means.html) estimates a parameter.

So the parameter should still be defined in context.

An interval for $$\mu$$ is not an interval for $$\bar x$$.

The sample mean is already known.

The uncertainty concerns the population mean.

<div class="article-note" markdown="1">
Defining the parameter correctly often makes the procedure choice much easier because it forces the population and the response variable to be identified first.
</div>
