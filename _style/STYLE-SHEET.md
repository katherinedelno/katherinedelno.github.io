# Style sheet — katherinedelno.com

Extracted from the 30 articles published between 2026-07-08 and 2026-07-30, with the six
named sample articles read in full. Every number below was computed from the corpus, not
estimated; the measuring scripts are described at the end.

Status: **draft, awaiting Katherine's corrections.** Read this file at the start of every
article session.

Underscore-prefixed directories are excluded from the Jekyll build, so nothing in `_style/`
is published.

---

## Part I — How the site is built

### Directory map

| Path | Contents |
|---|---|
| `_layouts/post.html` | The only layout. Wraps minima's `default`, hides the theme's title and post header, defines all article CSS inline. |
| `_includes/head.html` | Fonts, MathJax loader (fires only when `math: true`), link styling, mobile nav overrides. |
| `_includes/resource-entry.html` | One card on the resources index. Chooses eyebrow text by band. |
| `_includes/interactive-regression.html` | Present but unreferenced by any post. |
| `_posts/` | One `.md` per article, `YYYY-MM-DD-slug.md`. |
| `resources.md` | The index. All banding and sorting logic lives here. |
| `assets/` | Fonts, images, résumé. **No JavaScript or CSS assets for posts** — every interactive is inline in its post. |
| `_data/` | Does not exist. |
| `.github/workflows/featured-description-check.yml` | Warns (never fails) when a `featured` article's `description` falls outside 90–200 characters. |
| `_style/` | This style sheet and `read-time.py`. Underscore-prefixed, so never published. |
| `_ledgers/` | One claims ledger per article, named for the post it verifies. Also unpublished. |

### Front matter

Full set, in the order the existing posts use:

```yaml
layout: post
title: "The meaning of 95% confidence"
date: 2026-07-25
description: "A confidence level describes the method rather than any single interval. One hundred simulated studies make the distinction visible."
course: "AP Statistics"
read_time: "6 min read"
math: true
kind: foundations
sequence: 9
interactive: true
blurb: "Run a hundred studies and count which intervals capture the truth"
```

| Field | Values observed | Notes |
|---|---|---|
| `layout` | `post` | Always. |
| `title` | Sentence case, quoted | No terminal punctuation. Two use a colon (`After BC: multivariable calculus`), one a question mark. |
| `date` | `YYYY-MM-DD`, unquoted | |
| `description` | One or two sentences, quoted | Shown on **featured** cards and in SEO meta. Keep to 90–200 characters if the article is or may become featured. |
| `course` | `AP Calculus AB`, `AP Calculus BC`, `AP Calculus AB & BC`, `AP Statistics`, `AP Precalculus`, `All courses` | Drives banding and the article-header eyebrow. |
| `courses` | List, e.g. `[AP Calculus AB, AP Calculus BC]` | On 6 posts. **Read by no template.** Vestigial. |
| `section` | `beyond` | On 5 posts. **Read by no template.** `kind: beyond` is what actually bands an article. Vestigial. |
| `read_time` | `"5 min read"` … `"11 min read"` | Computed, not judged. Run `python3 _style/read-time.py --write`. Formula under Length. |
| `math` | `true` | On all 30. Gates the MathJax script. |
| `kind` | `mechanics`, `foundations`, `beyond` | Renders as the eyebrow "Mechanical" / "Foundations" / nothing. `beyond` also moves the article into the "Looking ahead" band. |
| `sequence` | Integer | Sort order **within a band**, not within a course. Gaps are tolerated; duplicates within one band produce an arbitrary order. |
| `interactive` | `true` / `false` | **Read by no template.** Kept as an editorial record. |
| `blurb` | Short phrase, no terminal period | Shown on non-featured cards. Usually imperative or descriptive: "Drag one point and watch the line, the residuals, and r respond". |
| `featured` | `true` | Katherine's alone — never set by Claude unless she asks. At most **five** per band; a sixth breaks the build loudly by design. Featured cards render in `sequence` position, so several disperse through a band rather than stacking at its top. The console warns when two sit fewer than four cards apart. |

### How the resources index bands an article

`resources.md` sorts all posts by `sequence`, then assigns each to exactly one band:

1. `kind == "beyond"` → **Looking ahead**
2. else `course == "AP Precalculus"` → **AP Precalculus**
3. else `course == "AP Statistics"` → **AP Statistics**
4. else → **AP Calculus**

So a `kind: beyond` article leaves its course band entirely. Newton's method carries
`course: "AP Calculus AB & BC"` but appears under Looking ahead.

Current occupancy, with `sequence` gaps as they stand today:

- **AP Calculus** 1, 2, 3, 5, 6, 7, 8, 9, 10 — gap at 4
- **AP Precalculus** 1, 2, 3, 4 — no gaps
- **AP Statistics** 1, 2, 4, 5, 7, 9, 10, 12 — gaps at 3, 6, 8, 11
- **Looking ahead** 1–9 — no gaps

### How an interactive is embedded

Everything is inline in the post's `.md`. No build step, no imports, no libraries — 25 of
the 30 posts carry one, and every one is hand-written canvas 2D.

```html
<div class="viz" markdown="0">
  <canvas id="XX-cv" width="700" height="300"></canvas>
  <div class="viz-controls">
    <label for="XX-n">Terms</label>
    <input type="range" id="XX-n" min="2" max="400" step="1" value="30">
    <span class="viz-value" id="XX-read"></span>
  </div>
  <p class="viz-caption">…</p>
</div>

<script>
(function(){
  var cv = document.getElementById('XX-cv'), c = cv.getContext('2d');
  var slider = document.getElementById('XX-n'), read = document.getElementById('XX-read');
  var W = cv.width, H = cv.height, pad = 36;
  var d__ = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W*d__; cv.height = H*d__; c.setTransform(d__, 0, 0, d__, 0, 0);
  function draw(){ … }
  slider.addEventListener('input', draw);
  draw();
})();
</script>
```

Fixed conventions:

- `markdown="0"` on the `viz` div, `markdown="1"` on the `article-note` div. Kramdown needs both.
- Every id is prefixed with a two- or three-letter article tag (`ci-`, `lad-`, `hs-`, `nm-`) so two interactives on one page cannot collide.
- The whole script is an IIFE. Nothing reaches global scope.
- Canvas is always `width="700"`; height ranges 150–360, and 300 is the mode.
- Device-pixel-ratio handling is verbatim the four lines above, capped at 2.
- Canvas text is `'700 12px Hanken Grotesk, sans-serif'` or the 13px equivalent.
- Buttons reuse the index's pill class: `<button type="button" id="…" class="res-filter" style="font-size:.72rem">`. A live numeric readout goes in `<span class="viz-value">`.
- Colours are hardcoded hex inside canvas, not `var(--…)`, because canvas cannot read CSS variables. Use the palette below.
- `draw()` is called once at the end so the figure is correct before any interaction.

### Palette and display tokens

Declared on `.pg` in `_layouts/post.html`:

| Token | Value | Use |
|---|---|---|
| `--ink` | `#1f1f1f` | Body text, the emphasized series in a plot |
| `--muted` | `#5c5c5c` | Captions, meta line, axis labels |
| `--line` | `#e6e6e6` | Rules, card borders |
| `--accent` | `#2b2b2b` | Labels, blockquote bar, slider accent |
| `--accent-soft` | `#f0f0f0` | `.article-note` background, inline `code` |
| `--card` | `#fbfbfb` | `.viz` background |
| `--faint` | `#9a9a97` | Declared on `resources.md` only; used in canvases for the third grey |

In canvas the working greys are, by frequency: `#1f1f1f` (29 uses), `#e0e0e0` (17),
`#5c5c5c` (10), `#c9c9c6` (7), `#9a9a97` (7). Everything is grey — there is no chromatic
colour anywhere on the site.

`box-shadow`, `text-shadow`, and gradients: **zero occurrences across the entire repo.**

Radii in use: 12px (`.viz`, `.article-note`), 10px (index card), 6px (canvas), 5px (inline
code), 999px (pill button). Not literally one radius, but one radius per role.

Body copy is capped at `max-width: 70ch`.

---

## Part II — The writing

### Length

Measured on prose + caption + closing note, with display and inline mathematics excluded.

| | Minimum | Median | Maximum |
|---|---|---|---|
| All 32 articles | 539 | **714** | 1128 |
| `kind: mechanics` (8) | 539 | 798 | 1041 |
| `kind: foundations` (15) | 600 | 705 | 1128 |
| `kind: beyond` (9) | 594 | 883 | 976 |

Body prose alone runs 391–1011, median 561. A caption is 37–113 words when present, median
89; the closing note is 39–94, median 65.

**Target: 650–950 words total.** Below 600 the page reads thin unless it is carrying a tool;
above 1100 only the harmonic series and least-squares influence have earned it.

**Target: 750–950 words total.** Below 650 the article reads thin; above 1150 only the
harmonic series has earned it. Write to the argument, then check against the range.

### `read_time`

Computed, never judged by eye. As of 2026-07-30:

```
minutes   = words/130 + 0.30·display_equations + 1.0·has_interactive
                      + 0.05·table_rows
read_time = max(5, round(minutes))
```

130 wpm rather than the 200–250 of ordinary prose, because these articles are read slowly
and re-read; 18 seconds to absorb a display equation and tie it back to the sentence that
introduced it; a full minute for an interactive, since the prose instructs the reader to
operate it; three seconds a table row. Inline mathematics stays inside the word count,
where it behaves like a word.

Run `python3 _style/read-time.py` to report, `--write` to apply. The script is the
authority; do not hand-set the field. Current spread: 5–11 minutes, median 7.

One trap the script documents: strip `$$…$$` mathematics **before** stripping HTML tags.
The other order lets a `<` inside mathematics — `L < 1`, `p > 1` — match the tag regex and
swallow everything up to the next `>`. That error understated three articles by several
hundred words apiece.

### Section structure

- **`##` only. Zero `###` in the entire corpus.** The hierarchy is one level deep.
- Heading count: median 4, range 2–9. `mechanics` articles carry more (median 6) because
  they enumerate procedure; `foundations` and `beyond` sit at 4.
- Heading length: mean 4.8 words, median 5, range 2–10.
- **Sentence case**, not title case: 125 of 133 headings lowercase every word after the
  first except proper nouns.
- **No terminal punctuation.** Zero headings end in a period. Zero end in a question mark.
- 18 of 133 contain a comma, 11 a colon.

Headings are a mix of noun phrases and short declarative clauses, roughly half and half,
and the clauses are the site's signature move — a heading that states the finding rather
than naming the topic:

> The method has the probability, not the interval
> The mistake that sinks more solutions than any other
> The tell is in how the data were collected
> Determinants stop being formulas
> Terms that vanish, a sum that does not

Opening words, by frequency: `The` (36), `Why` (12), `What` (9), `Where` (6), `A` (6).
The `Why …` heading is used for the section that explains a mechanism; the `What … on the
exam` heading closes many articles.

Three recurring patterns worth reusing:

- `Example 1: the sliding ladder` — numbered, colon, lowercase description.
- `Surprise 2: alternate the signs, and order suddenly matters` — a named series of results.
- `Try it` / `Turn the dials` / `Drag one point` — a two-or-three-word imperative heading
  directly above an interactive.

### How articles open

The first two sentences of each sample, verbatim:

**Notation in AP Calculus**
> "Most of the free-response points I see students lose in AP Calculus aren't lost on ideas."
> "They're lost on notation and justification."

**Which chi-square test? Independence or homogeneity**
> "Starting with the revised AP Statistics course, the College Board removed the chi-square goodness-of-fit test."
> "That actually simplifies a question students used to find confusing."

**A procedure for related rates**
> "Related rates has a reputation it does not deserve."
> "The calculus involved is one move, differentiating both sides with respect to time, and any student who can use the chain rule can do it."

**The harmonic series and conditional convergence**
> "Unit 10 is where calculus stops feeling like a faster version of algebra and starts producing results that sound false."
> "This piece collects three of the best examples, each one a true statement that reads like a mistake, together with real proofs rather than incantations."

**The meaning of 95% confidence**
> "The most commonly missed interpretation question in AP Statistics is also the most commonly asked: what does "95% confident" mean?"
> "Students want it to mean "there is a 95% chance the true mean is in my interval." It does not mean that, the exam knows students want it to mean that, and the scoring guidelines are written to catch it."

**Newton's method and its basins of attraction**
> "A tangent line is the best straight substitute for a curve at a point."
> "Newton's method takes that sentence seriously and turns it into an algorithm: to solve \\(f(x)=0\\), make a guess, replace the curve by its tangent line at the guess, and solve the tangent line's root instead, which is easy because lines are easy."

What they share:

1. **The first sentence is a claim, not an orientation.** Every one asserts something
   contestable or surprising. None announces a subject, and none tells the reader what the
   article will do.
2. **It is short.** All six first sentences run under 21 words: 9, 14, 15, 16, 20, 20.
3. **The second sentence turns.** It either sharpens the claim ("They're lost on notation
   and justification"), concedes and redirects ("That actually simplifies…"), or begins
   cashing it out. Related rates and Newton's method both put the whole thesis in sentence
   one and spend sentence two on the mechanism.
4. **The tension is named in the opening paragraph, never later.** By the end of paragraph
   one the reader knows what is at stake: a reputation undeserved, a removed test, an
   answer everyone gets wrong, a result that sounds false.
5. **No heading precedes the opening.** Prose starts immediately after the front matter,
   and the first `##` comes after one to four paragraphs.

### How articles close

Two moves, in this order.

**Last body section.** Usually titled for what the material buys — `What this buys you on
the exam`, `Why this is worth internalizing beyond the exam`, `Where the exam takes this`,
`Why a statistics student should care`. It is not a recap. It converts the article's
content into something the reader does: a checklist before boxing an answer, the three
wordings that lose the point, the reason a rule is shaped the way it is. When it is a list,
each item points back to a numbered result earlier in the article rather than restating it.

**The closing note.** A `<div class="article-note" markdown="1">` block, 45–95 words
(median 70), present on all 30 articles. **Required on every new article.**

It is always forward-facing — an exercise, prediction, self-test, or historical footnote —
and never a summary. The established openers:

> A self-test: … · An experiment at the slider: … · A diagnostic to try: …
> A question to take with you: … · Something to try at a whiteboard: …
> A puzzle to take with you: … · A prediction to test against the interactive: …
> A check worth performing on the interactive: … · A historical footnote with a caution attached: …

Two of the six samples close on an aphorism inside the note — "confidence is purchased
with width, which is why 100% confidence is available and useless" — which is the strongest
version of the form.

### Sentence length and rhythm

Across the corpus: mean 22.4 words, median 20.0, 10th percentile 7, 90th percentile 41.
The six samples: mean 22.7, median 19.0, 90th percentile 43.

The gap between mean and median is the whole rhythm. A long sentence that carries a
qualified claim through two or three clauses is followed by a short one that lands it:

> "The series diverges in theory and looks convergent on every calculator ever built."
> "Same terms, different order, different sum, half again as large."
> "It changes the answer."
> "The tension is not a blemish to erase."

Habits that produce the rhythm:

- **The colon does structural work**, introducing the payoff of the sentence before it.
  Used constantly; used far more than the dash.
- **Appositive definition rather than a parenthesis**: "This behavior, called quadratic
  convergence, is why…" — the term is dropped in mid-sentence, not set aside.
- **Semicolons separate two balanced claims**, not lists.
- **Paired negation**: "not a formality" / "not bureaucratic tidiness" / "not merely a
  geometric ornament". The pattern is *deny the small reading, then assert the large one*.
- Paragraphs are 2–5 sentences. Single-sentence paragraphs appear, and land.
- **No contractions.** Ten appear, all in the July 8 article; the following 29 articles
  have zero. Write without them.

### Person and address

The corpus drifts from 21–36 uses of "you" per 1000 words in the earliest articles to
literally zero in Newton's method, Benford's law, Buffon's needle, and Simpson's paradox.

**The target is the late voice.** Third person and impersonal construction by default.
"You" is available in exactly two places:

1. **At the interactive**, as an imperative: "Drag the slider and watch." "Choose a
   starting point and watch the tangent lines hunt." "Slide n and watch the rectangle
   total approach 12." No subject pronoun; the imperative carries it.
2. **In exam procedure**, where the reader is the one writing the answer: "the sentence
   that earns the point", "before you box an answer".

"We" is nearly absent (highest count in any article: 4). "I" appears in five articles, and
only where the claim is genuinely a teaching observation — "the most common errors I see",
"the fastest way I know to believe Riemann's theorem". That is the correct use and it
should stay rare.

"Students" appears 31 times in body prose, always attached to a specific error or a wrong
expectation ("Students want it to mean…", "students often guess between the two"), never
as a generic group with generic feelings.

### Worked examples

Established in the related rates article, which is the pattern for procedural pieces.

- **Heading**: `## Example 1: the sliding ladder` — numbered, colon, lowercase.
- **Problem statement in italics**, its own paragraph, stated as a complete problem with
  every number: *A 13-foot ladder leans against a wall. The base slides away from the wall
  at 2 ft/s. How fast is the top sliding down when the base is 5 feet from the wall?*
- **Bold run-in labels** naming the step, one per paragraph: `**Name:**`,
  `**Know and want:**`, `**Static equation:**`, `**Differentiate with respect to \(t\):**`,
  `**Snapshot:**`. These are structural, not emphasis, and they stay.
- **Display mathematics for each step that changes the equation**; inline for values.
- **A closing sentence that interprets**, never the bare number: "The top is sliding down
  at 5/6 ft/s. The negative sign is not a blemish to erase. It answers the question 'which
  direction,' and the final sentence should say so."
- **Step detail**: every algebraic step that a student could get wrong is shown; routine
  arithmetic is not. The cone example shows the substitution *and* explains why one
  substitution was legal early and the other was not. That commentary is the point of the
  example.
- Examples escalate. Ladder (Pythagorean), cone (similar triangles plus an elimination),
  camera (trigonometry plus a units subtlety). Each adds exactly one new difficulty.

### Mathematics typesetting

- **`$$…$$` for everything**, display and inline both. MathJax is configured for `\(…\)`
  inline, but **the corpus uses zero `\(…\)` and zero single-`$`.** Inline: `$$(r-1)(c-1)$$`.
  Display: `$$…$$` on its own line, blank line above and below.
- Display mathematics **carries its own terminal punctuation** — a comma if the sentence
  continues, a period if it ends. `$$\chi^2 = \sum \frac{(O-E)^2}{E},$$`

### Inline mathematics must be forced small

`head.html` maps `$$` to MathJax's **displayMath**, not inlineMath. So a `$$…$$` written
mid-sentence still renders in *display* style: full-height fractions, integral signs with
their limits stacked above and below, a full-size sigma. Left alone it wrecks the line
height of the paragraph around it.

Every chunky construct inside an inline `$$…$$` therefore has to be shrunk by hand:

| construct | inline form | display form |
|---|---|---|
| fraction | `\tfrac{a}{b}` | `\frac{a}{b}` |
| integral | `\textstyle\int_a^b` | `\int_a^b` |
| sum, product | `\textstyle\sum`, `\textstyle\prod` | `\sum`, `\prod` |
| absolute value | `\vert x\vert` | `\left\vert x\right\vert` |
| evaluation bar | — | `\left.\tfrac{dy}{dx}\right\vert_{x=a}` |

## Never type a bare pipe, anywhere kramdown can see it

**This is the one that breaks silently and looks like a rendering bug.** Kramdown starts a
table when a paragraph's first line contains an unescaped `|`. A line like

```
The function $$|x| \cdot 1$$ has no derivative at 0.
```

is not a paragraph containing absolute values. It is a three-cell table row, and it renders as
one: the prose is chopped into boxes and the mathematics never reaches MathJax. Nothing warns
you, and the source looks correct.

So absolute value is always `\vert … \vert`, and the evaluation bar is always
`\left. … \right\vert_{…}`. Never `|`, and never `\lvert`/`\rvert` either — those work, but the
corpus settled on `\vert` before this was written down, and one convention is worth more than a
marginally better one.

The rule applies to display equations on their own line as well as to inline mathematics, since
a display equation is also the first line of its block.

Pipes are safe in three places, all of which kramdown skips: inside `<script>`, inside any
element carrying `markdown="0"` (which is every `viz` block), and inside Liquid tags
`{%- … -%}` (which is how `resources.md` uses them). They are **not** safe inside an
`article-note`, which carries `markdown="1"`.

`_style/check.py` catches this, along with every other rule in this document that can be
checked mechanically. Run it before committing:

```
python3 _style/check.py            # every article
python3 _style/check.py _posts/…   # one file
```

It exits non-zero if it finds anything. The checks that catch *silent* failures — where the
page renders wrongly and nothing warns you — are the bare pipe, an odd number of `$$`,
unbalanced `\left`/`\right`, and unbalanced braces inside mathematics. The rest are the style
rules in this document.

`\dfrac` is **never** correct inline — it forces display style, which is the opposite of
what is wanted. In display mathematics it is only ever used to force a nested fraction back
to full size, which is also unwanted: **a fraction appearing inside another fraction's
numerator or denominator takes `\tfrac`**, so the compound fraction stays legible.

`\textstyle` applies to the rest of its group, so putting it at the front of the inline
expression is enough: `$$\textstyle\int_1^\infty \tfrac{1}{x^2}\,dx$$`.

Audited and enforced across all 39 articles on 2026-07-30: 21 inline fractions, 27 inline
integrals and sums, and 5 nested display fractions were corrected.
- `\quad\Longrightarrow\quad` chains a result to its consequence on one display line.
- `\text{…}` for words inside mathematics; `\,` before `dx` and between a coefficient and
  a derivative.
- Function names use their macros: `\ln`, `\sin`, `\log`, never italic letters.
- `\left…\right` for delimiters around fractions; plain parentheses otherwise.
- Set `math: true` in front matter or nothing renders.

### Interactives in the prose

The hand-off into an interactive is a two-part formula, and 25 of 25 follow it:

1. **A sentence naming exactly what is on screen, with its concrete parameters.**
   "The curve below is $$f(x) = x^3 - x$$, with roots at $$-1$$, $$0$$, and $$1$$."
   "The gray curve is the truth. The black path is Euler's method from $$x=0$$ to $$x=2$$."
2. **An imperative inviting one specific action.**
   "Choose a starting point and watch the tangent lines hunt."
   "Drag the slider and watch." "Slide $$n$$ and watch the rectangle total approach 12."

The word is *below*, never "the following" or "this figure". Deixis: `below` (39),
`picture` (37), `above` (31), `slider` (19).

**The caption does the interpretive work.** It is 39–118 words — a genuine paragraph, not a
label — and it tells the reader what to notice, what it means, and where the model breaks:

> "The base moves at a steady 2 ft/s, yet the top's speed changes with position: gentle
> when the ladder is steep, violent as it flattens out. That is the whole point of related
> rates. … Note what happens to dy/dt as x approaches 13: the formula sends the top's speed
> toward infinity, a sign the model is breaking down."

Captions use plain-text mathematics (`dy/dt`, `ln 2`), not `$$…$$`.

**After the interactive, a new `##` heading begins immediately** in 21 of 25 cases. The
interactive ends its section. Later prose refers back with "the simulation above", "visible
near $$x = \pm 0.577$$ in the interactive", "Recall the 12,367 terms" — a specific,
checkable reference, never "as we saw above".

### Cross-references between articles

**Convention: inline prose links.** As of 2026-07-30 there are **30 links across 24 of the
30 articles**. Before that pass there were none.

The link sits on a noun phrase inside a sentence that was already going to be written. It
is never a signpost ("see also", "read more about"), never a bare URL, and never the whole
clause — wrap the object, not the assertion:

> The sharp cutoff at $$p = 1$$ in the [p-series
> test](/2026/07/24/which-convergence-test-field-guide.html) is not bureaucratic tidiness.

> A statistics major today is substantially a data science degree, and [the least-squares
> idea from Unit 5](/2026/07/30/least-squares-regression-influence.html) is its seed.

Rules:

- **Absolute path, no domain**: `/2026/07/25/what-95-percent-confident-means.html`. Jekyll's
  default permalink is `/:year/:month/:day/:title.html` and `baseurl` is empty.
- **One or two links per article.** Six articles carry two; none carries more.
- **Link where the prose already names the other article's subject.** If a sentence has to
  be invented to hold the link, the connection is not real enough to link.
- **Keep the oblique unit references too** — "the conditional probability of Unit 2", "the
  same local linearity that underlies linearization in Unit 4". They do different work, and
  a link and a unit reference can sit in the same sentence.

Styling requires no CSS change. `_includes/head.html` already gives `.article-body a` ink
text with a 1px `#9a9a97` underline at 3px offset, darkening to `#1f1f1f` on hover. Regular
weight, no colour.

Six articles carry no outbound link, because no existing sentence in them named another
article's subject: `euler-method-step-size`, `buffons-needle`,
`conditional-probability-and-the-base-rate`, `independence-and-mutual-exclusivity`,
`newtons-method`, `simpsons-paradox`. Several of these become linkable once 7D fills the
Calculus gaps — Euler's method to linearization, Newton's method to linearization and to
the derivative-as-a-limit article.

### Vocabulary

The register is **precise, concrete, and unhedged**. The most frequent content words are
the objects themselves: point, series, line, test, function, curve, exam, sample, interval.

Characteristic verbs — the site's texture — are physical and transitive:

> hunt · climb · settle onto · trap · hop · catapult · drain · sink · undo · bracket ·
> collapse · tame itself · commit to · steer · convict · acquit · earn · cost

Characteristic constructions:

- **"is the entire game" / "is the whole point" / "is the entire argument"** — naming the
  crux flatly. One instance each; a family of three, not a tic.
- **"rather than"** (16 uses) is the workhorse contrastive, well ahead of "but". Paired
  with flat negation — `is not a…` (18), `It is not…` (12) — it produces the site's
  signature move: deny the small reading in a short sentence, then assert the large one.
- **"worth seeing" / "worth internalizing" / "worth classifying"** — instead of "important".
- **Concrete numbers in place of adjectives**: not "you would need very many terms" but
  "to push the total past 10 you need about 12,367 terms".
- **Named attribution with dates**: "due to Nicole Oresme around 1350", "Riemann proved
  this in 1854", "In 1879 Arthur Cayley asked". Every historical claim carries a name and
  a year.

Words the corpus does not use, verified by search across all 30 articles:

`crucial` · `vital` · `essential` · `powerful` · `robust` · `utilize` · `leverage` (as a
verb) · `delve` · `dive into` · `unpack` · `furthermore` · `moreover` · `in conclusion` ·
`to summarize` · `it is important to note` · `it is worth noting` · `keep in mind` ·
`note that` · `we will` · `in this article, we will`

Four expressions were retired and removed from the corpus on 2026-07-30:

- **`simply`** as an adverb — 3 in prose, 1 in a caption. The adjective forms `simple`,
  `simplest`, `simplifies` do real descriptive work and stay. One survivor: the blurb
  "three places intuition is simply wrong", where the sense is *flatly*, not *merely*.
- **`let's`** — 1, in the opening of the 95% confidence article.
- **"the good news is"** — 1, in the writing parameters article.
- **contractions** — 13 in total, 11 of them in the July 8 notation article. Now zero.

Adverbial **`just`** was audited and left alone. All 19 uses turned out to be restrictive
or comparative — "just geometry", "just two tests", "just above 1" — not the minimizing
sense. Do not write "it is just a matter of" or "just apply the rule"; "nothing but X" and
"only two of them" are fine and already in use.

`Notice` appears 6 times as a sentence opener and is acceptable; `Note that` never appears
and should not start.

---

## Part III — What this writing never does

Inferred from the sample, and merged with Katherine's stated prohibitions. Where the two
disagree the prohibition wins, and the disagreement is marked.

1. **Never announces itself.** No "In this article, we will…", no "This piece is about…",
   no roadmap paragraph. The first sentence is already the argument.
2. **Never recaps.** No closing paragraph that lists what was covered. The last section
   converts the material into use; the note sends the reader somewhere new.
3. **Never uses a rhetorical question as a heading.** Zero occurrences in 133 headings.
4. **Never uses an exclamation mark.** Zero in 30 articles — every apparent hit is a
   factorial inside mathematics. Never uses an emoji. Zero.
5. **Never encourages.** No "you've got this", "don't worry", "the good news is", no
   motivational closer. The one "good news" instance is retired.
6. **Never hedges the reader's ability.** No "this can seem tricky", no "don't be
   intimidated". Difficulty is described as a property of the material, not of the reader:
   "Related rates has a reputation it does not deserve."
7. **Never generalizes about students** except to name a specific error or a specific
   wrong expectation. "Students want it to mean 'there is a 95% chance…'" is allowed
   because it names the exact misreading. "Many students find this difficult" is not.
8. **Never uses a bulleted list where a paragraph works.** Only 7 of 30 articles contain a
   list at all: 5 of 7 `mechanics`, 2 of 14 `foundations`, **0 of 9 `beyond`**. Lists are
   for conditions, numbered procedure steps, and enumerated traps — genuinely enumerable
   things.
9. **Never bolds for emphasis inside a sentence.** Zero occurrences, as of the 2026-07-30
   pass that converted all 44. The only surviving bold is the **run-in label** at the head
   of a paragraph, list item, or table row (`**Snapshot:**`, `**Trap 2: …**`) — 56 of
   these, all structural. Emphasis inside a sentence uses italics; first use of a technical
   term uses italics; a table cell uses nothing, because the table already emphasizes.
10. **Never uses contractions.** Zero across all 30 articles.
11. **Never asserts a number it has not computed.** Every figure in the corpus is a real
    one: 12,367 terms to pass 10, r = 0.918, about 17%, 3/(4π) ≈ 0.239.
12. **Never cites a theorem without its hypotheses.** "f is continuous on [1,4] and
    differentiable on (1,4), so by the Mean Value Theorem…" — the hypothesis check is
    written out, because on the exam it is its own point.
13. **Never says "simply", "just" (minimizing), "obviously", "clearly", or "of course".**
    Nothing is described as easy.
14. **Never uses `###`.** One heading level.
15. **Never sets `featured`.** Katherine's alone.

---

## Measurement notes

All figures above were computed by script over `_posts/2026-*.md`, with front matter,
`<script>` blocks, `<style>` blocks, HTML tags, and `$$…$$` mathematics stripped before
counting. Word counts treat the body prose, the `viz-caption`, and the `article-note` as
three separately-measured components. Sentence segmentation splits on terminal punctuation
followed by a capital, with mathematics replaced by a placeholder token first, and discards
fragments under three words.

**Two traps, both of which produced wrong numbers before they were caught:**

1. **Strip `$$…$$` before stripping HTML tags.** A `<` inside mathematics — `L < 1`, `p > 1`
   — otherwise matches the tag regex and swallows text up to the next `>`. This understated
   the convergence-test guide by 594 words.
2. **Remove the `viz` block by matching `<div>` depth, not by a non-greedy `.*?</div>`.**
   The block contains nested `viz-controls` divs, so a non-greedy match stops at the first
   inner close and leaves every button label and control caption counted as prose. This
   inflated every interactive article; the first version of this style sheet reported a
   median of 802 words against a true 714, and a maximum of 1202 against a true 1128.

Scripts are not committed; they are reproducible from this description.

## Corrections applied, 2026-07-30

A single pass over all 30 live articles, after Katherine approved each decision:

| Change | Count |
|---|---|
| Mid-sentence bold converted (terms and emphasis to italics, table cells to plain) | 44 |
| Run-in labels preserved untouched | 56 |
| Contractions removed | 13 |
| Headings rephrased to drop a contraction | 3 |
| Adverbial `simply` removed | 4 |
| `let's` removed | 1 |
| "the good news is" removed | 1 |
| Closing notes written for articles that had none | 3 |
| Cross-article links added | 30 |

The three rephrased headings, all in the July 8 notation article: "Don't forget the
constant" → "Where the constant enters"; "Say what you're evaluating" → "Say what is being
evaluated"; "Don't drop the limit" → "Keep the limit attached".

Second person was deliberately **not** retrofitted. The July 8 article still runs at 21
uses of "you" per 1000 words; it is a mechanics article about what the reader writes on the
exam, where the style sheet permits it.

## Where the source documents are

Both Course and Exam Descriptions are in Katherine's own materials folder, and they are the
authority for every `[EXAM]` claim:

- `Curriculum & Course Materials/AP Calculus AB/Admin/Course and Exam Description/ap-calculus-ab-and-bc-course-and-exam-description.pdf`
- `Curriculum & Course Materials/AP Statistics/Admin/Course and Exam Description & Exam Reference Sheet/ap-statistics-course-and-exam-description-effective-fall-2026.pdf`

Extract with `pdftotext -layout` before searching. The Calculus CED yields about 732,000
characters and Statistics about 704,000. **Do not fetch these from the web**: the fetch
truncates near 106,000 characters, which stops inside Unit 2 for Calculus and Unit 2 for
Statistics, and cost two articles their sourcing before I noticed the local copies.

There is also a clarifications document for Calculus effective fall 2026, in the same folder,
confirming that course content is unchanged.

## Standing decisions for the article program

Recorded as they are made, so later sessions do not reopen them.

| Date | Decision |
|---|---|
| 2026-07-30 | Cross-references are inline prose links on a noun phrase. No signposting. |
| 2026-07-30 | Voice targets the late corpus: third person, "you" only at the interactive and in exam procedure. |
| 2026-07-30 | A closing `article-note` is required on every article. |
| 2026-07-30 | No bold outside structural run-in labels. Terms of art take italics. |
| 2026-07-30 | `read_time` is computed by `_style/read-time.py`, never set by hand. |
| 2026-07-30 | 7B, the distribution explorer, ships as a post like any other, not a standalone page. It therefore needs the full front matter set, a `sequence`, and a card on the resources index. |
| 2026-07-30 | **AP Calculus is sequenced by College Board unit order, and within a unit by its topic order.** AB and BC stay interleaved in one band. Numbering is consecutive, 1–31. The full plan is `_style/CALCULUS-SEQUENCE-PROPOSAL.md`, approved and applied. |
| 2026-07-30 | The tier numbering in the 7D brief is the **writing** order. `sequence` is the **display** order. They are allowed to disagree, and in Unit 1 and Unit 6 they do. |
| 2026-07-30 | 7D covers all 22 articles, tier 5 included, not the 18 of the front half alone. |
| 2026-07-31 | Up to five `featured` articles per band, rendered in `sequence` position rather than hoisted. Featured display positions: Calculus 1, 10, 17, 22, 31; Precalculus 1 and 4; Statistics 7; Looking ahead 1. |
| 2026-07-31 | **The grid must have no holes at either breakpoint**, and mobile is the binding constraint. A featured card spans two of three columns above 900px and the full width of two below it, so it leaves an empty cell behind whenever it has to wrap. Two rules, both about the card's *display position* rather than its `sequence` number: on mobile an **even** number of ordinary cards must precede it, so featured card number $k$ sits at a position of $k$'s own parity; on desktop it must not start in the last column. Simulate both before adding or moving a featured card — `resources.md` now runs the same simulation in the console and names the breakpoint that fails. |
| 2026-07-31 | **Two deliberate exceptions to College Board topic order**, both taken to close holes, both between adjacent same-unit articles with no dependency either way. Unit 6: the FTC article (topic 6.4) sits at sequence 22 and accumulation functions (6.5–6.6) at 21. Unit 5: reading the graph of $f'$ (5.3–5.9) sits at sequence 17 and the two existence theorems (5.1–5.2) at 18. The notation article moving from sequence 1 to 2 is *not* an exception, since it belongs to no College Board unit and was placed first by editorial choice. |
| 2026-07-31 | AP Precalculus carries two featured cards rather than one, at positions 1 and 4. With only four articles in the band, position 1 is the sole placement that is hole-free at both breakpoints, so featuring the transformations article was forced; keeping the unit-circle feature alongside it is also hole-free and preserves the existing choice. Revisit once P1 and P2 land, at which point position 5 becomes available too. |
| 2026-07-31 | Titles avoid the "*X*, and *the thing that Y*" construction unless the second clause is the thesis rather than an appendix. Eleven were rewritten; three kept. |
| 2026-07-31 | Every article is audited against the CED before it ships, and the Fall 2026 Calculus clarifications are part of that check — FUN-1.C.1's hypothesis interval was corrected from open to closed. |

Placements that need no renumbering, because they fall into existing `sequence` gaps:

- **7A**, the p-value article → AP Statistics **11**, between "Writing parameters" (10) and
  "Which chi-square test" (12).
- **7C**, sampling and bias → AP Statistics **3**, after "Simpson's paradox" (2).
- **7B**, the distribution explorer → AP Statistics **6** or **8**, both open. 8 sits it
  beside "The Central Limit Theorem in simulation" (7) and "The meaning of 95% confidence"
  (9), which is where a distribution tool is most wanted.

7D is the only tier that forces a renumber, and its complete ordering goes to Katherine for
approval before any front matter is written.

## Open questions for Katherine

1. **Vestigial front matter** — `courses`, `section`, and `interactive` are read by no
   template. Keep writing them for the record, or stop?

Resolved: the `sequence` gaps. AP Statistics filled 3, 8 and 11 with 7C, 7B and 7A, leaving
only 6. AP Calculus was renumbered 1–31 under the approved plan, and its 22 open slots are
the 7D articles.
