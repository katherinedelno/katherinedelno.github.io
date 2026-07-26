---
layout: post
title: "Related rates is a translation problem"
date: 2026-07-20
description: "Students don't struggle with the calculus in related rates — they struggle with the setup. A five-step translation routine, three fully worked examples, and the one mistake that sinks more solutions than any other."
course: "AP Calculus AB"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
---

Related rates has a reputation it doesn't deserve. The calculus involved is one move — differentiate both sides with respect to time — and students who can use the chain rule can do it. What actually goes wrong is the *translation*: turning a paragraph about a leaking cone or a sliding ladder into an equation worth differentiating. Treat it as a translation problem and the fog lifts.

## The five-step routine

1. **Draw and name.** Sketch the situation and give a letter to every quantity that changes. Anything changing gets a variable; anything permanently fixed gets a number.
2. **Write what you know and what you want, as derivatives.** "The radius grows at 3 cm/s" becomes $$\tfrac{dr}{dt} = 3$$. "How fast is the area growing?" becomes: find $$\tfrac{dA}{dt}$$. Signs carry meaning — a shrinking quantity has a negative rate.
3. **Find a static equation** relating the variables: Pythagorean theorem, similar triangles, a volume or area formula, a trig ratio. No rates yet — just geometry.
4. **Differentiate both sides with respect to $$t$$.** Every variable is secretly a function of time, so every term picks up its own rate by the chain rule.
5. **Now — and only now — substitute the snapshot values** and solve for the unknown rate. Then answer with units and a direction ("increasing at...").

The order of steps 4 and 5 is the entire game, which brings us to the classic mistake.

## The mistake that sinks more solutions than any other

**Substituting the snapshot before differentiating.** If a problem says "when the radius is 5," and you write $$A = \pi(5)^2$$ before differentiating, you have frozen the radius. It is now a constant; its derivative is zero, and the problem dissolves into nonsense.

The rule: *a value that holds only at the instant in question enters after the differentiation.* Only quantities that are constant for all time — the height of the wall, the length of the ladder, the cone's fixed proportions — may be substituted early.

## Example 1: the sliding ladder

*A 13-foot ladder leans against a wall. The base slides away from the wall at 2 ft/s. How fast is the top sliding down when the base is 5 feet from the wall?*

**Name:** $$x$$ = distance from wall to base, $$y$$ = height of the top. The 13 is constant for all time — the ladder doesn't stretch.

**Know / want:** $$\tfrac{dx}{dt} = 2$$; find $$\tfrac{dy}{dt}$$ when $$x = 5$$.

**Static equation:** $$x^2 + y^2 = 169.$$

**Differentiate with respect to $$t$$:**

$$2x\,\frac{dx}{dt} + 2y\,\frac{dy}{dt} = 0.$$

**Snapshot:** when $$x = 5$$, the static equation gives $$y = 12$$. Substitute everything:

$$2(5)(2) + 2(12)\,\frac{dy}{dt} = 0 \quad\Longrightarrow\quad \frac{dy}{dt} = -\frac{5}{6}.$$

The top is sliding **down** at $$\tfrac{5}{6}$$ ft/s. The negative sign isn't a blemish to erase — it *is* the answer to "which direction," and the sentence should say so.

## Example 2: the draining cone

*An inverted conical tank has radius 6 m and height 12 m. Water drains at 3 m³/min. How fast is the water level falling when the water is 4 m deep?*

**Name:** $$h$$ = depth of water, $$r$$ = radius of the water surface, $$V$$ = volume. Here $$r$$ and $$h$$ both change — but they're chained together by the tank's shape.

**Kill a variable before differentiating.** Similar triangles: $$\tfrac{r}{h} = \tfrac{6}{12}$$, so $$r = \tfrac{h}{2}$$ *at every instant* — a for-all-time relationship, safe to substitute early:

$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi\left(\frac{h}{2}\right)^{2} h = \frac{\pi h^3}{12}.$$

**Differentiate:**

$$\frac{dV}{dt} = \frac{\pi h^2}{4}\,\frac{dh}{dt}.$$

**Snapshot:** $$\tfrac{dV}{dt} = -3$$ (draining!) and $$h = 4$$:

$$-3 = \frac{\pi(16)}{4}\,\frac{dh}{dt} = 4\pi\,\frac{dh}{dt} \quad\Longrightarrow\quad \frac{dh}{dt} = -\frac{3}{4\pi}.$$

The water level is falling at $$\tfrac{3}{4\pi} \approx 0.239$$ m/min. Notice the two different substitution moments: the shape relationship $$r = h/2$$ went in *before* differentiating (true always), while $$h = 4$$ waited until *after* (true only at the instant).

## Example 3: the rising camera angle

*A camera on the ground 100 m from a launch pad tracks a rocket rising at 50 m/s. How fast is the camera's angle of elevation increasing when the rocket is 100 m up?*

**Name:** $$y$$ = rocket height, $$\theta$$ = angle of elevation. The 100 m ground distance never changes.

**Static equation:** $$\tan\theta = \dfrac{y}{100}.$$

**Differentiate:**

$$\sec^2\theta\,\frac{d\theta}{dt} = \frac{1}{100}\,\frac{dy}{dt}.$$

**Snapshot:** when $$y = 100$$, the triangle is a 45–45–90, so $$\theta = \tfrac{\pi}{4}$$ and $$\sec^2\theta = 2$$:

$$2\,\frac{d\theta}{dt} = \frac{50}{100} \quad\Longrightarrow\quad \frac{d\theta}{dt} = \frac{1}{4}.$$

The angle grows at $$\tfrac14$$ **radian** per second — radians, because the derivative formulas for trig functions are only true in radians. Answering "degrees per second" here is a units error, not a style choice.

## Reading the signs like a grader

A quick internal checklist before you box an answer:

- **Does the sign match the story?** Draining tank, negative $$dV/dt$$. Ladder top falling, negative $$dy/dt$$. If your algebra produces a positive rate for a quantity the story says is shrinking, a sign was dropped in translation.
- **Do the units multiply out?** In $$\tfrac{dV}{dt} = \tfrac{\pi h^2}{9}\,\tfrac{dh}{dt}$$, the right side is m² times m/min = m³/min. If the units don't work, the equation is wrong before any numbers enter.
- **Did every changing variable get a rate?** Differentiating $$x^2 + y^2 = 169$$ must produce both a $$\tfrac{dx}{dt}$$ and a $$\tfrac{dy}{dt}$$. A missing rate almost always means a variable was accidentally treated as a constant — the step-5-too-early error in disguise.
- **Is the final sentence complete?** Value, units, direction: "the depth is decreasing at $$\tfrac{1}{2\pi}$$ meters per minute when $$h = 6$$." On the exam the interpretation is frequently its own point.

<div class="article-note" markdown="1">
If you want a diagnostic: try the cone example, but suppose the tank is *also* being filled at 5 m³/min while draining at 3. Only one thing changes — $$\tfrac{dV}{dt}$$ becomes $$+2$$ — and the entire routine runs identically. When a one-word change in the story changes exactly one number in your setup, the translation is working.
</div>
