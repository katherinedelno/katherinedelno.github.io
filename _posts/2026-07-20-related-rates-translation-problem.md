---
layout: post
title: "Related rates is a translation problem"
date: 2026-07-20
description: "Students don't struggle with the calculus in related rates. They struggle with the setup. A five-step translation routine, three fully worked examples, and the one mistake that sinks more solutions than any other."
course: "AP Calculus AB"
courses: [AP Calculus AB, AP Calculus BC]
read_time: "8 min read"
math: true
---

Related rates has a reputation it does not deserve. The calculus involved is one move, differentiating both sides with respect to time, and any student who can use the chain rule can do it. What actually goes wrong is the translation: turning a paragraph about a leaking cone or a sliding ladder into an equation worth differentiating. Treat it as a translation problem and the fog lifts.

## The five-step routine

1. **Draw and name.** Sketch the situation and give a letter to every quantity that changes. Anything changing gets a variable; anything permanently fixed gets a number.
2. **Write what you know and what you want, as derivatives.** "The radius grows at 3 cm/s" becomes $$\tfrac{dr}{dt} = 3$$. "How fast is the area growing?" becomes: find $$\tfrac{dA}{dt}$$. Signs carry meaning, so a shrinking quantity has a negative rate.
3. **Find a static equation** relating the variables: the Pythagorean theorem, similar triangles, a volume or area formula, a trig ratio. No rates yet, just geometry.
4. **Differentiate both sides with respect to $$t$$.** Every variable is secretly a function of time, so every term picks up its own rate by the chain rule.
5. **Now, and only now, substitute the snapshot values** and solve for the unknown rate. Then answer with units and a direction, as in "increasing at 2 square meters per minute."

The order of steps 4 and 5 is the entire game, which brings us to the classic mistake.

## The mistake that sinks more solutions than any other

Substituting the snapshot before differentiating. If a problem says "when the radius is 5," and you write $$A = \pi(5)^2$$ before differentiating, you have frozen the radius. It is now a constant, its derivative is zero, and the problem dissolves into nonsense.

The rule: a value that holds only at the instant in question enters after the differentiation. Only quantities that are constant for all time, such as the height of the wall, the length of the ladder, or the cone's fixed proportions, may be substituted early.

## Example 1: the sliding ladder

*A 13-foot ladder leans against a wall. The base slides away from the wall at 2 ft/s. How fast is the top sliding down when the base is 5 feet from the wall?*

**Name:** $$x$$ is the distance from wall to base, and $$y$$ is the height of the top. The 13 is constant for all time, since the ladder does not stretch.

**Know and want:** $$\tfrac{dx}{dt} = 2$$; find $$\tfrac{dy}{dt}$$ when $$x = 5$$.

**Static equation:** $$x^2 + y^2 = 169.$$

**Differentiate with respect to $$t$$:**

$$2x\,\frac{dx}{dt} + 2y\,\frac{dy}{dt} = 0.$$

**Snapshot:** when $$x = 5$$, the static equation gives $$y = 12$$. Substitute everything:

$$2(5)(2) + 2(12)\,\frac{dy}{dt} = 0 \quad\Longrightarrow\quad \frac{dy}{dt} = -\frac{5}{6}.$$

The top is sliding down at $$\tfrac{5}{6}$$ ft/s. The negative sign is not a blemish to erase. It answers the question "which direction," and the final sentence should say so.

## Example 2: the draining cone

*An inverted conical tank has radius 6 m and height 12 m. Water drains at 3 m³/min. How fast is the water level falling when the water is 4 m deep?*

**Name:** $$h$$ is the depth of the water, $$r$$ is the radius of the water surface, and $$V$$ is the volume. Here $$r$$ and $$h$$ both change, but the tank's shape chains them together.

**Eliminate a variable before differentiating.** Similar triangles give $$\tfrac{r}{h} = \tfrac{6}{12}$$, so $$r = \tfrac{h}{2}$$ at every instant. That is a for-all-time relationship, safe to substitute early:

$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi\left(\frac{h}{2}\right)^{2} h = \frac{\pi h^3}{12}.$$

**Differentiate:**

$$\frac{dV}{dt} = \frac{\pi h^2}{4}\,\frac{dh}{dt}.$$

**Snapshot:** $$\tfrac{dV}{dt} = -3$$, negative because the tank is draining, and $$h = 4$$:

$$-3 = \frac{\pi(16)}{4}\,\frac{dh}{dt} = 4\pi\,\frac{dh}{dt} \quad\Longrightarrow\quad \frac{dh}{dt} = -\frac{3}{4\pi}.$$

The water level is falling at $$\tfrac{3}{4\pi} \approx 0.239$$ m/min. Notice the two different substitution moments. The shape relationship $$r = h/2$$ went in before differentiating, because it is true at every instant. The value $$h = 4$$ waited until after, because it is true only at the instant in question.

## Example 3: the rising camera angle

*A camera on the ground 100 m from a launch pad tracks a rocket rising at 50 m/s. How fast is the camera's angle of elevation increasing when the rocket is 100 m up?*

**Name:** $$y$$ is the rocket's height and $$\theta$$ is the angle of elevation. The 100 m ground distance never changes.

**Static equation:** $$\tan\theta = \dfrac{y}{100}.$$

**Differentiate:**

$$\sec^2\theta\,\frac{d\theta}{dt} = \frac{1}{100}\,\frac{dy}{dt}.$$

**Snapshot:** when $$y = 100$$, the triangle is a 45-45-90, so $$\theta = \tfrac{\pi}{4}$$ and $$\sec^2\theta = 2$$:

$$2\,\frac{d\theta}{dt} = \frac{50}{100} \quad\Longrightarrow\quad \frac{d\theta}{dt} = \frac{1}{4}.$$

The angle grows at $$\tfrac14$$ radian per second. Radians, because the derivative formulas for trig functions are only true in radians. Answering in degrees per second here is a units error, not a style choice.

## Reading the signs like a grader

A quick internal checklist before you box an answer:

- **Does the sign match the story?** A draining tank has negative $$dV/dt$$; a falling ladder top has negative $$dy/dt$$. If your algebra produces a positive rate for a quantity the story says is shrinking, a sign was dropped in translation.
- **Do the units multiply out?** In $$\tfrac{dV}{dt} = \tfrac{\pi h^2}{4}\,\tfrac{dh}{dt}$$, the right side is m² times m/min, which is m³/min. If the units do not work, the equation is wrong before any numbers enter it.
- **Did every changing variable get a rate?** Differentiating $$x^2 + y^2 = 169$$ must produce both a $$\tfrac{dx}{dt}$$ and a $$\tfrac{dy}{dt}$$. A missing rate almost always means a variable was accidentally treated as a constant, which is the too-early substitution error in disguise.
- **Is the final sentence complete?** Value, units, direction: "the depth is decreasing at $$\tfrac{3}{4\pi}$$ meters per minute when $$h = 4$$." On the exam, the interpretation is frequently its own point.

<div class="article-note" markdown="1">
A diagnostic to try: rework the cone example, but suppose the tank is also being filled at 5 m³/min while draining at 3. Only one thing changes, since $$\tfrac{dV}{dt}$$ becomes $$+2$$, and the entire routine runs identically. When a one-word change in the story changes exactly one number in your setup, the translation is working.
</div>
