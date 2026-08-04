---
layout: post
title: "Writing parameters in AP Statistics"
date: 2026-07-14
description: "Defining the parameter is where a lot of inference answers quietly go wrong. Here is a clean way to write parameters and hypotheses, with a worked example for every procedure."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: mechanics
sequence: 10
interactive: false
blurb: "A clean way to write parameters and hypotheses for every procedure"
image: "/assets/og/writing-parameters-in-ap-statistics.png"
---

Almost every inference problem in AP Statistics starts by defining a parameter, and it is one of the most common places to lose easy points. The fix is a habit rather than a new idea. Once you are clear on what a parameter is and how to write one, hypotheses and confidence intervals stop feeling like guesswork.

## A parameter is not a statistic

A *parameter* is a fixed number that describes a whole population. A *statistic* is a number you calculate from a sample. Inference is always about the parameter: you use the statistic you can see to draw a conclusion about the parameter you cannot.

The symbols matter, because using the wrong one changes the meaning:

- A population proportion is $$p$$; the sample proportion is $$\hat{p}$$.
- A population mean is $$\mu$$; the sample mean is $$\bar{x}$$.

So hypotheses and parameter definitions are written with $$p$$ and $$\mu$$, never with $$\hat{p}$$ or $$\bar{x}$$. A hypothesis like $$H_0: \hat{p} = 0.5$$ is automatically wrong, because $$\hat{p}$$ is something you measured, not something you are making a claim about.

## A template that always works

Define every parameter the same way:

> Let [symbol] = the true [mean or proportion] of [the variable] for [the population].

Naming the population and the variable in words is what earns the point. A bare symbol is not enough.

## One proportion

A school claims 60% of students bike to school. You suspect it is lower and survey a random sample.

$$p = \text{the true proportion of all students at the school who bike to school}$$

$$H_0: p = 0.60 \qquad H_a: p < 0.60$$

## One mean

A coffee shop advertises a mean wait time of 4 minutes. You time a random sample of visits.

$$\mu = \text{the true mean wait time, in minutes, for all visits to the shop}$$

$$H_0: \mu = 4 \qquad H_a: \mu \neq 4$$

## Two proportions

You compare the proportion of first-year and second-year students who use the tutoring center, sampling each group separately. Use a *difference of proportions*, and define which group is which:

$$p_1 - p_2, \text{ where } p_1 = \text{true proportion of first-years who use the center, and } p_2 = \text{the same for second-years}$$

$$H_0: p_1 - p_2 = 0 \qquad H_a: p_1 - p_2 \neq 0$$

Writing $$H_0: p_1 - p_2 = 0$$ says the two proportions are equal, which is usually the claim of "no difference."

## Two means

You compare the mean study time of athletes and non-athletes from two independent samples:

$$\mu_1 - \mu_2, \text{ where } \mu_1 = \text{true mean study time for athletes and } \mu_2 = \text{true mean study time for non-athletes}$$

$$H_0: \mu_1 - \mu_2 = 0 \qquad H_a: \mu_1 - \mu_2 \neq 0$$

## Paired data: the one everyone mixes up

If the data are *paired* (each subject measured twice, or matched pairs), you do not have two independent groups. You work with the population of *differences*, and there is just one parameter:

$$\mu_d = \text{the true mean difference (after minus before) for the population}$$

$$H_0: \mu_d = 0 \qquad H_a: \mu_d > 0$$

For example, if you record each student's score before and after a study workshop, every student gives you one difference, so you use $$\mu_d$$, not $$\mu_1 - \mu_2$$. The tell is the design: two measurements on the same subjects (or matched pairs) means paired; two separate groups means a difference of means.

## For a confidence interval, define the parameter too

The same definitions apply. A confidence interval estimates a parameter, so you still write, for instance, "$$\mu$$ = the true mean wait time for all visits," and then [interpret the interval](/2026/07/25/what-95-percent-confident-means.html) as capturing that $$\mu$$, never as capturing $$\bar{x}$$ or "the sample."

## The mistakes to avoid

- Writing hypotheses about $$\hat{p}$$ or $$\bar{x}$$ instead of $$p$$ or $$\mu$$.
- Giving a symbol with no context: define the population and the variable in words.
- Using $$\mu$$ for a proportion, or $$p$$ for a mean.
- Treating paired data as two independent groups (using $$\mu_1 - \mu_2$$ when you should use $$\mu_d$$).

<div class="article-note" markdown="1">
Defining the parameter well is not a formality. It forces you to decide what population you are talking about and which procedure fits, before any calculation. Get that right and the rest of the problem tends to follow; get it wrong and even a perfect calculation answers the wrong question.
</div>
