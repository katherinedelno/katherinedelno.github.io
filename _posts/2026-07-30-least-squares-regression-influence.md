---
layout: post
title: "What moves the least-squares line"
date: 2026-07-30
description: "A draggable scatterplot with a linked residual plot: outliers, influential points, and why the residual plot catches what r misses."
course: "AP Statistics"
read_time: "7 min read"
math: true
kind: foundations
sequence: 1
interactive: true
blurb: "Drag one point and watch the line, the residuals, and r respond"
---

Press the regression button and every calculator agrees: one line, a slope to six digits, an $$r^2$$ that looks reassuring. The exam is rarely interested in the button. It asks two questions instead: what do the numbers mean, and which points are responsible for them? Both questions have answers you can see. Every point in the scatterplot below can be dragged, and everything that depends on the points moves with them.

{% include interactive-regression.html %}

## Drag one point

The plot underneath the scatterplot is the residual plot: the same points with the line subtracted out. Each residual is the vertical gap between a point and the line,

$$\text{residual} = y - \hat{y},$$

actual minus predicted, so a point above the line has a positive residual and a point below has a negative one. Drag any point up and down and watch the two plots move as one picture, because that is what they are. The residual plot is the scatterplot seen from the line's point of view, and it magnifies exactly what the scatterplot hides: whether what's left over after the line has done its work is noise or structure.

Four numbers update as you drag. The slope and intercept define the line itself. The correlation $$r$$ measures the strength and direction of the linear relationship, and $$s$$, the standard deviation of the residuals, is the typical size of a miss — how far off the line's predictions run, in the units of $$y$$. When an exam question asks you to interpret $$s = 8.41$$, that is the sentence it wants: predictions from this line are typically off by about 8.41 units.

## An outlier is not an influential point

Load the "one outlier" preset. One point sits far above the cloud, near the middle of the x-range. Its residual is enormous — and the line barely notices it. Select it and drag it: the slope moves in the third decimal place. The point is an outlier, but it is not influential.

Now load "one influential point." One point sits far to the right, and the line has bent toward it. Select it, and the dashed ghost line appears: the fit computed without that point. Here the two lines disagree completely — slope 0.399 without the point, 0.025 with it. One point has flattened the entire relationship.

The difference between the two presets is not how wrong the point is; it is where the point stands. The readout calls this leverage,

$$h_i = \frac{1}{n} + \frac{(x_i - \bar{x})^2}{S_{xx}},$$

and the formula says in symbols what the dragging shows directly: distance from $$\bar{x}$$ is what buys a point its power over the line. Vertical distance from the line makes a residual. Horizontal distance from the rest of the data makes leverage. Moving the line takes both, which you can verify by dragging any point around the plot and watching when the ghost line diverges. **An outlier is a point the line fails to fit. An influential point is a point the line cannot afford to ignore.** They are different failures, they are diagnosed differently — one from the residual plot, one by refitting without the point — and a single point can be either, both, or neither.

## Why squares

The name "least squares" is a literal description, not a brand name. Press "show squares": each residual becomes an actual square, with area equal to the squared residual, and the shaded area on the plot is the sum the method minimizes.

The line now has two open handles. Drag them and make your own line — a steeper one, a flatter one, one that chases the outlier. The readout keeps score: your sum of squares against the least-squares minimum. You can reduce the gap, and with care you can get close, but you cannot beat the minimum, and "snap to least squares" will show you how much area your best attempt was still carrying. Of all possible lines, the least-squares line is the one that leaves behind the smallest total squared error. That is the entire definition, and it is why single large misses cost so much: squaring punishes a residual of 20 four times as hard as a residual of 10.

## What r cannot see

Load "curved." The correlation is $$r = 0.918$$, a number most students would be delighted to report, and the scatterplot is plainly not a line — it bends, and the residual plot underneath shows the bend as an unmistakable arc: positive residuals at both ends, negative in the middle. $$r$$ measures linear association and nothing else. It will report a strong value for a relationship that is strong and curved, because it has no way to know the difference. The residual plot knows. A patterned residual plot means the linear model is the wrong model, whatever $$r$$ says, and this is precisely why exam questions hand you a residual plot and ask whether a linear model is appropriate.

Now load "two clusters." The correlation is $$r = 0.957$$, and there is almost no relationship in the data at all — just two separate groups, one high and one low, with the line dutifully connecting their centers. Strong correlation can be manufactured by group structure rather than by any relationship between the variables. Ask what the two clusters are before trusting the line between them.

One more reading discipline while the numbers are in front of you: $$r^2 = 0.842$$ is not $$r$$, and it is not a probability. It is the proportion of the variation in $$y$$ that the linear relationship with $$x$$ accounts for. The two numbers answer different questions, and the exam asks for each by name.

## Beyond the data

The line in the scatterplot turns gray past the smallest and largest x-values in the data. The equation is perfectly willing to produce $$\hat{y}$$ for any $$x$$ you like — that is what equations do — but outside the range of the observed data there is no evidence the pattern continues. Prediction out there is extrapolation, and the gray is a reminder that the data have no opinion about it.

Drag a few points before you leave. The line every calculator prints is not a fact about the world; it is a summary of particular points, some of which matter far more than others. Knowing which ones, and why, is the part the button cannot do for you.
