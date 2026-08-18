---
layout: post
title: "What moves the least-squares line"
date: 2026-07-30
description: "Residuals, leverage, influence, correlation, and least squares become easier to distinguish when one point can be moved by hand."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: foundations
sequence: 2
interactive: true
blurb: "Residuals, leverage, influence, correlation, and least squares become easier to distinguish when one point can be moved by hand"
image: "/assets/og/least-squares-regression-influence.png"
---

A least-squares regression line summarizes a particular set of points. Move the points and the line changes, and some observations have much more influence on that change than others. The interactive below lets you move individual observations while watching the regression line, residual plot, correlation, and residual standard deviation update together.

{% include interactive-regression.html %}

When a point is selected, the dashed line shows the regression fit without that point, and the distance between the two fitted lines gives a visual sense of its influence.

## Residuals

A residual is $$y-\hat y$$, the observed response minus the response predicted by the line. A point above the line has a positive residual, and a point below has a negative residual.

The residual plot shows the same observations after the fitted linear trend has been subtracted, which makes departures from linearity easier to see. For a useful linear model, the residuals should look like unstructured scatter around zero, and a visible curve or other pattern is evidence that the linear model has missed systematic structure.

## Interpreting the numerical summaries

The slope gives the predicted change in $$y$$ for a one-unit increase in $$x$$. The intercept gives the predicted response at $$x=0$$, when that value is meaningful in context.

The correlation $$r$$ measures the strength and direction of a linear association, and the residual standard deviation $$s$$ measures the typical prediction error in the units of $$y$$. If $$s=8.41$$, a contextual interpretation is that predictions from the regression line are typically off by about 8.41 response units.

## Outliers and influential points are different

Load the “one outlier” example. The unusual point sits far from the regression line vertically but near the center of the observed $$x$$-values. It has a large residual, and removing it does not change the slope much.

Now load “one influential point.” The unusual point lies far from the rest of the data horizontally, and removing it changes the fitted line substantially. That point has high leverage.

In simple linear regression, leverage increases as an observation's $$x$$-value moves farther from $$\bar x$$. A point with high leverage has the potential to be influential, and whether it actually changes the fitted line also depends on its $$y$$-value. So a point can be:

- an outlier but not influential
- influential but not a large residual outlier
- both
- neither

Those labels describe different features.

## Why least squares uses squares

Press “show squares.” Each residual becomes the side length of a square, and the least-squares line is the line that minimizes

$$\sum (y_i-\hat y_i)^2$$

Large residuals therefore receive disproportionately large weight, and a residual of 20 contributes four times as much squared error as a residual of 10. The word “least squares” describes the optimization criterion literally.

## What correlation cannot tell you

Load the curved example. A high value of $$r$$ can occur even when the relationship is visibly nonlinear. Correlation measures linear association, and it does not test whether a line is the correct model. The residual plot is useful here because curvature that is easy to miss in the scatterplot can appear as a clear pattern after the line is removed.

Now load the two-cluster example. A strong overall correlation can also be created by [group structure](/2026/07/27/simpsons-paradox.html), and if two distinct groups sit in different parts of the plane, the line may connect the group centers even when there is little relationship within either group. So a numerical value of $$r$$ should never be interpreted without looking at the graph.

Likewise, $$r^2$$ is not a probability. It describes the proportion of variability in the response accounted for by the fitted linear relationship.

## Extrapolation

The fitted equation can produce a numerical prediction at any input, and that does not mean the data support that prediction. Using the line outside the observed range of $$x$$ is extrapolation, and the relationship may change beyond the data.

<div class="article-note" markdown="1">
A regression equation is a summary of the observed range, not a guarantee about values that were never studied.
</div>
