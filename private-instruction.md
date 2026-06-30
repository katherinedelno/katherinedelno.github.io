---
layout: page
title: Private Instruction
permalink: /private-instruction/
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800;900&display=swap');
  /* ---- Scoped styling for the Private Instruction page ---- */
  .page-heading, .post-header { display:none; }
  body { font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; }

  .pi {
    --ink:#1a1a1a;
    --muted:#5b6168;
    --line:#e7e7e3;
    --accent:#959386;
    --accent-soft:#cac9c3;
    --accent-ink:#57554C;
    --card:#fbfbfa;
    color:var(--ink);
    line-height:1.6;
  }
  .pi p { max-width:74ch; }
  .pi h1, .pi h2, .pi h3, .pi h4, .pi b { font-weight:700; }

  .pi .label {
    text-transform:uppercase;
    letter-spacing:.14em;
    font-size:.72rem;
    font-weight:700;
    color:var(--accent-ink);
    margin:0 0 .5rem;
  }

  .pi-hero { margin:0 0 2.5rem; }
  .pi-hero h1 { font-size:2.1rem; line-height:1.15; margin:0 0 .6rem; letter-spacing:-.02em; font-weight:700; }
  .pi-hero .tagline { font-size:1.12rem; color:var(--muted); max-width:64ch; margin:0; }

  .pi-section { margin:2.6rem 0; padding-top:2.2rem; border-top:1px solid var(--line); }
  .pi-section:first-of-type { border-top:none; padding-top:0; }
  .pi-section h2 { font-size:1.35rem; margin:0 0 1rem; letter-spacing:-.01em; }

  /* Course cards */
  .pi-courses { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-top:1.2rem; }
  .pi-course {
    border:1px solid var(--line); border-radius:14px; padding:20px 20px 22px;
    background:var(--card);
  }
  .pi-course h3 { margin:0 0 .35rem; font-size:1.05rem; }
  .pi-course p { font-size:.94rem; color:var(--muted); margin:0; }

  /* Approach steps */
  .pi-steps { display:grid; grid-template-columns:repeat(2,1fr); gap:14px 28px; margin-top:1.1rem; }
  .pi-step { display:flex; gap:14px; align-items:flex-start; }
  .pi-step .num {
    flex:0 0 auto; width:30px; height:30px; border-radius:50%;
    background:var(--accent); color:var(--ink); font-size:.85rem; font-weight:700;
    display:flex; align-items:center; justify-content:center;
  }
  .pi-step h4 { margin:.15rem 0 .2rem; font-size:1rem; }
  .pi-step p { margin:0; font-size:.92rem; color:var(--muted); }

  /* Testimonials */
  .pi-quotes { display:grid; grid-template-columns:repeat(2,1fr); gap:18px; margin-top:1.2rem; }
  .pi-quote {
    border:1px solid var(--line); border-left:3px solid var(--accent);
    border-radius:12px; padding:22px 24px; background:#fff;
  }
  .pi-quote p { font-size:.96rem; margin:0 0 .9rem; }
  .pi-quote .who { font-size:.84rem; color:var(--muted); font-weight:600; letter-spacing:.02em; }

  /* Pricing */
  .pi-pricing { display:grid; grid-template-columns:repeat(2,1fr); gap:18px; margin-top:1.2rem; }
  .pi-price {
    position:relative; border:1px solid var(--line); border-radius:16px;
    padding:26px 24px; background:var(--card);
  }
  .pi-price.featured { border:1.5px solid var(--accent); background:#fff; box-shadow:0 6px 22px rgba(31,42,68,.07); }
  .pi-price .pill {
    position:absolute; top:-12px; left:24px; background:var(--accent); color:var(--ink);
    font-size:.68rem; font-weight:700; letter-spacing:.1em; text-transform:uppercase;
    padding:5px 11px; border-radius:999px;
  }
  .pi-price h3 { margin:.2rem 0 .15rem; font-size:1.08rem; }
  .pi-price .amt { font-size:1.9rem; font-weight:700; letter-spacing:-.02em; }
  .pi-price .amt span { font-size:.95rem; font-weight:500; color:var(--muted); }
  .pi-price .note { font-size:.9rem; color:var(--muted); margin:.5rem 0 0; }

  .pi-billing {
    margin-top:1.3rem; padding:16px 20px; background:var(--accent-soft);
    border-radius:12px; font-size:.93rem; color:var(--ink);
  }
  .pi-billing strong { color:var(--accent-ink); }

  /* Feature / tech lists */
  .pi-list { list-style:none; padding:0; margin:1rem 0 0; }
  .pi-list li { position:relative; padding:0 0 .55rem 1.4rem; font-size:.95rem; color:var(--ink); }
  .pi-list li::before {
    content:""; position:absolute; left:0; top:.55em;
    width:7px; height:7px; border-radius:50%; background:var(--accent);
  }
  .pi-list li b { font-weight:600; }

  /* CTA */
  .pi-cta { text-align:center; margin:2.6rem 0 1rem; padding:2.4rem 1rem; background:var(--accent-soft); border-radius:16px; }
  .pi-cta h2 { border:none; margin:0 0 .5rem; }
  .pi-cta p { margin:0 auto 1.3rem; color:var(--muted); max-width:52ch; }
  .pi-btn {
    display:inline-block; background:var(--accent); color:var(--ink) !important;
    padding:13px 26px; border-radius:10px; text-decoration:none; font-weight:600;
    border:1px solid var(--accent); transition:opacity .15s ease;
  }
  .pi-btn:hover { opacity:.9; }
  .pi-btn-outline { background:transparent; color:var(--accent-ink) !important; }
  .pi-btn-outline:hover { background:#fff; opacity:1; }
  .pi-cta-actions { display:flex; gap:12px; justify-content:center; flex-wrap:wrap; }
  .pi-cta .email { display:block; margin-top:1rem; font-size:.92rem; color:var(--muted); }

  .pi-fine { margin-top:2.4rem; padding-top:1.6rem; border-top:1px solid var(--line); }
  .pi-fine p { font-size:.9rem; color:var(--muted); }
  .pi-fine .label { color:var(--muted); }

  /* FAQ accordion */
  .pi-faq { margin-top:1.1rem; }
  .pi-faq details { border-bottom:1px solid var(--line); padding:15px 0; }
  .pi-faq details:first-of-type { border-top:1px solid var(--line); }
  .pi-faq summary {
    cursor:pointer; font-weight:600; font-size:1rem; list-style:none;
    display:flex; justify-content:space-between; align-items:center; gap:16px;
  }
  .pi-faq summary::-webkit-details-marker { display:none; }
  .pi-faq summary::after { content:"+"; color:var(--accent-ink); font-weight:400; font-size:1.35rem; line-height:1; }
  .pi-faq details[open] summary::after { content:"\2212"; }
  .pi-faq details p { margin:.7rem 0 0; color:var(--muted); font-size:.95rem; max-width:70ch; }

  /* Highlight callout */
  .pi-callout {
    margin-top:1.2rem; padding:20px 24px; border:1px solid var(--line);
    border-left:3px solid var(--accent); border-radius:12px; background:var(--card);
  }
  .pi-callout p { margin:0; }

  /* Sample-lesson preview cards (link to real PDFs) */
  .pi-samples { display:grid; grid-template-columns:repeat(2,1fr); gap:20px; margin-top:1.3rem; }
  .pi-sample {
    display:grid; grid-template-columns:124px 1fr; gap:20px; align-items:center;
    border:1px solid var(--line); border-radius:14px; padding:20px; background:var(--card);
  }
  .pi-sample-thumb {
    display:block; border:1px solid var(--line); border-radius:7px; overflow:hidden;
    box-shadow:0 5px 16px rgba(31,42,68,.12); transition:box-shadow .15s ease, transform .15s ease;
  }
  .pi-sample-thumb:hover { box-shadow:0 10px 26px rgba(31,42,68,.18); transform:translateY(-2px); }
  .pi-sample-thumb img { display:block; width:100%; height:auto; }
  .pi-sample-body .course { font-size:.74rem; color:var(--accent-ink); font-weight:700; text-transform:uppercase; letter-spacing:.1em; margin:0 0 .3rem; }
  .pi-sample-body h4 { margin:0 0 .35rem; font-size:1.02rem; line-height:1.25; }
  .pi-sample-body p { margin:0 0 .7rem; font-size:.88rem; color:var(--muted); }
  .pi-sample-link { font-size:.9rem; font-weight:600; color:var(--accent-ink); text-decoration:none; }
  .pi-sample-link:hover { text-decoration:underline; }

  @media (max-width:720px){
    .pi-courses, .pi-steps, .pi-quotes, .pi-pricing { grid-template-columns:1fr; }
    .pi-samples { grid-template-columns:1fr; }
    .pi-hero h1 { font-size:1.7rem; }
  }
</style>

<div class="pi" markdown="0">

  <div class="pi-hero">
    <h1>Private Mathematics &amp; Statistics Instruction</h1>
    <p class="tagline">Structured, one-on-one instruction in mathematics and statistics. AP-focused, with support for non-AP and college-level coursework as well.</p>
  </div>

  <!-- OVERVIEW -->
  <div class="pi-section">
    <p class="label">Overview</p>
    <p>I provide structured, one-on-one instruction in mathematics and statistics for high school and college students. Each session functions like a focused mini-class: direct instruction, guided practice, and an independent check to confirm the student can execute on their own. The emphasis is on correct setup, precise notation, well-justified reasoning, and clear, rubric-aligned written work. These are the habits that earn credit on the AP exam and in the classroom.</p>
  </div>

  <!-- COURSES -->
  <div class="pi-section">
    <p class="label">Courses</p>
    <h2>What I teach</h2>
    <div class="pi-courses">
      <div class="pi-course">
        <h3>AP Statistics</h3>
        <p>Procedure selection, condition checks, inference, and rubric-aligned statistical writing, with confident TI-84 use.</p>
      </div>
      <div class="pi-course">
        <h3>AP Calculus (AB/BC)</h3>
        <p>Limits, derivatives, integrals, and applications, with precise notation and AP free-response justification.</p>
      </div>
      <div class="pi-course">
        <h3>AP Precalculus</h3>
        <p>Functions, trigonometry, and analytic foundations that prepare students for AP Calculus and college math.</p>
      </div>
    </div>
    <p style="margin-top:1.1rem;font-size:.92rem;color:var(--muted);">AP courses are my focus, but I also support students in non-AP and college-level mathematics and statistics. These are my current offerings and I add courses each year, so if you don't see your course listed, please get in touch to discuss fit.</p>
  </div>

  <!-- WEBINARS -->
  <div class="pi-section">
    <p class="label">Free webinars</p>
    <h2>Succeeding in your course: free 45-minute webinars</h2>
    <p>This summer I'm hosting free 45-minute webinars on how to succeed in each course, with a separate session for AP Statistics, AP Calculus (AB/BC), and AP Precalculus. Webinars run in early August and again in late August or early September; exact dates are announced soon. Register now and I'll send you the details.</p>
    <ul class="pi-list">
      <li><b>AP Statistics</b></li>
      <li><b>AP Calculus (AB/BC)</b></li>
      <li><b>AP Precalculus</b></li>
    </ul>
    <div class="pi-callout">
      <p><b>Free for everyone who registers:</b> my master cheat sheet for that course &mdash; a concise, one-page-per-theme reference to the definitions, formulas, and procedures for the whole year. It's yours to keep whether or not you attend live, so register even if you can't make the date.</p>
    </div>
    <a href="https://forms.gle/PMQRaH75zCRBTLg3A" class="pi-btn" style="margin-top:1.2rem;" target="_blank" rel="noopener">Register for a webinar</a>
  </div>

  <!-- BACKGROUND -->
  <div class="pi-section">
    <p class="label">Background</p>
    <h2>Who you're working with</h2>
    <p>I hold an <b>M.S. in Statistics from the University of Washington</b> and a <b>B.S. in Mathematics from the University of Nevada, Reno</b>, with formal training in probability, statistical inference, regression, and the analytic foundations underlying calculus. My graduate training provides a rigorous theoretical foundation that carries through every session, from correct procedure selection to well-justified conclusions.</p>
    <p>I've taught in both structured university settings and one-on-one formats. As a graduate teaching assistant for large introductory statistics courses, I led weekly discussion sections, developed instructional materials, and helped students produce clear, defensible reasoning. I also mentored through UW's Directed Reading Program, designing and teaching a one-on-one short course in statistical learning.</p>
  </div>

  <!-- APPROACH -->
  <div class="pi-section">
    <p class="label">Approach</p>
    <h2>What a session looks like</h2>
    <p>Every session is built around the student, not a fixed script. Most of our time is spent solving problems together, and the teaching is calibrated to exactly what the student needs that day. Students are welcome to send specific problems, homework, or upcoming topics at least 24 hours in advance, and I'll build the session around them.</p>
    <div class="pi-steps">
      <div class="pi-step">
        <div class="num">1</div>
        <div>
          <h4>Targeted teaching</h4>
          <p>Calibrated to the moment: a condensed review of the essentials when a student just needs a refresher, or a full lecture that rebuilds the foundation when a topic isn't sticking.</p>
        </div>
      </div>
      <div class="pi-step">
        <div class="num">2</div>
        <div>
          <h4>Guided problem-solving</h4>
          <p>Where most of the session goes: working through AP-style problems and the student's own questions together, with targeted prompts and corrections that build reliable habits.</p>
        </div>
      </div>
      <div class="pi-step">
        <div class="num">3</div>
        <div>
          <h4>Independent practice</h4>
          <p>A few problems the student works on their own to confirm they can execute without prompts, followed by a quick review together.</p>
        </div>
      </div>
      <div class="pi-step">
        <div class="num">4</div>
        <div>
          <h4>Notes &amp; solutions</h4>
          <p>A summary, worked problems, and solutions uploaded after each meeting so the student can review between sessions.</p>
        </div>
      </div>
    </div>
    <p style="margin-top:1.3rem;">I'm equally attentive to the learning environment. Many capable students lose points to uncertainty under time pressure, disorganized work, or inconsistent written communication. Sessions are calm and focused: questions are taken seriously, mistakes are handled constructively, and confidence is built alongside skill.</p>
  </div>

  <!-- MATERIALS -->
  <div class="pi-section">
    <p class="label">Materials</p>
    <h2>Lessons built for your student, not pulled off a shelf</h2>
    <p>I teach from a complete curriculum I have written and typeset myself: a full set of lessons covering every topic in the course, plus reference sheets, procedure guides, and practice banks, all built to the same exacting standard. This is not a binder of worksheets pulled off a shelf. It is a coherent body of material I maintain and refine each year, and it is what lets every session move quickly and stay rigorous.</p>
    <p>Each lesson is kept consistent in structure and formatting from one topic to the next, so students always know where to look. Sessions stay individualized: the material is shaped around the student's course pacing and the specific gaps and recurring errors I observe.</p>
    <p style="margin-top:1.1rem;font-weight:600;">Each lesson includes:</p>
    <ul class="pi-list">
      <li><b>A condensed lecture</b> for a quick review of the key definitions, equations, and theorems.</li>
      <li><b>A full lecture</b> for students who need to rebuild their foundation in the topic.</li>
      <li><b>Model problems</b>, where I work through a few examples step by step to show the approach in action.</li>
      <li><b>Guided problem-solving</b>, the heart of each session: we work through problems together while I coach the student, ask guiding questions, and help them reason their way to the answer.</li>
      <li><b>Independent practice</b>, a few problems the student works on their own to confirm they can execute without prompts.</li>
      <li><b>A condensed one-page summary</b> of the topic for quick reference.</li>
    </ul>
    <p style="margin-top:1.1rem;">All of these materials are shared with the student after each session. An optional <b>problem set</b>, assigned between sessions and submitted to me for written feedback, is also available as part of the between-session support add-on.</p>
    <p style="margin-top:1.1rem;">I also provide supplemental study materials as they are useful, such as reference sheets and procedure guides that students can keep and return to throughout the year.</p>

    <p style="margin-top:1.6rem;font-weight:600;">See a real lesson</p>
    <p style="margin-top:.2rem;">These are complete student-copy lessons, exactly as a student receives them. Each opens as a full PDF &mdash; the same materials we work through together in session.</p>
    <div class="pi-samples">
      <div class="pi-sample">
        <a class="pi-sample-thumb" href="/assets/samples/ap-calculus-bc-sample-lesson.pdf" target="_blank" rel="noopener">
          <img src="/assets/img/previews/sample-lesson-calc-cover.png" alt="First page of the sample AP Calculus BC lesson" loading="lazy" decoding="async">
        </a>
        <div class="pi-sample-body">
          <p class="course">AP Calculus BC</p>
          <h4>Module 4C &mdash; Linearization &amp; L'Hospital's Rule</h4>
          <p>A complete lesson: lecture, model problems, guided practice, and independent work.</p>
          <a class="pi-sample-link" href="/assets/samples/ap-calculus-bc-sample-lesson.pdf" target="_blank" rel="noopener">View the full lesson (PDF) &rarr;</a>
        </div>
      </div>
      <div class="pi-sample">
        <a class="pi-sample-thumb" href="/assets/samples/ap-statistics-sample-lesson.pdf" target="_blank" rel="noopener">
          <img src="/assets/img/previews/sample-lesson-stats-cover.png" alt="First page of the sample AP Statistics lesson" loading="lazy" decoding="async">
        </a>
        <div class="pi-sample-body">
          <p class="course">AP Statistics</p>
          <h4>Module 3E &mdash; Chi-Square Inference</h4>
          <p>A complete lesson: lecture, model problems, guided practice, and independent work.</p>
          <a class="pi-sample-link" href="/assets/samples/ap-statistics-sample-lesson.pdf" target="_blank" rel="noopener">View the full lesson (PDF) &rarr;</a>
        </div>
      </div>
    </div>

    <div class="pi-callout" style="margin-top:1.6rem;">
      <p><b>Optional printed binder, $50 per semester.</b> For students on a full-semester weekly cadence, I can print, bind, and ship a complete copy of our lessons and resources, with the problem sets left blank so the student fills them in as we work through them together. Everything stays organized in one place, with room to take notes during each session, so there is no scrambling and nothing scattered across loose pages.</p>
    </div>
  </div>

  <!-- AP EXAM PREP -->
  <div class="pi-section">
    <p class="label">AP exam preparation</p>
    <h2>A focused shift before the exam</h2>
    <p>In the final one to two months before the AP exam, sessions transition into dedicated exam preparation. We move from new material toward timed practice, full free-response and multiple-choice work, and targeted review of the content most likely to appear.</p>
    <div class="pi-callout">
      <p>All exam-preparation materials are provided as part of this phase, at no cost beyond regular session time.</p>
    </div>
  </div>

  <!-- TESTIMONIALS -->
  <div class="pi-section">
    <p class="label">Testimonials</p>
    <h2>What families say</h2>
    <div class="pi-quotes">
      <div class="pi-quote">
        <p>&ldquo;Katherine is an attentive, thoughtful, and highly effective tutor. She helped my daughter build both confidence and understanding in AP Statistics, making challenging material feel approachable. Her follow-up was exceptional; she regularly checked in and ensured nothing fell through the cracks. I highly recommend Katherine to any family looking for a knowledgeable, supportive, and dedicated tutor.&rdquo;</p>
        <span class="who">Parent of 2025 AP Statistics student</span>
      </div>
      <div class="pi-quote">
        <p>&ldquo;Katherine worked closely with us to understand our child's challenges and develop approaches for her specific needs. She was flexible and adaptive, and not only increased our child's understanding but helped her gain the self-confidence needed to really deepen her comprehension and growth.&rdquo;</p>
        <span class="who">Parent of 2025 AP Statistics student</span>
      </div>
    </div>
  </div>

  <!-- PRICING -->
  <div class="pi-section">
    <p class="label">Pricing</p>
    <h2>Hourly, with one rate for every course</h2>
    <p>No packages or long-term commitment; you book the sessions you need. Sessions start at a 60-minute minimum and are booked in 30-minute increments, so we can size each meeting to the work at hand. I recommend a <b>weekly 90-minute session</b>: ninety minutes gives us enough time to teach the topic, practice it together, and leave room for an independent check.</p>
    <div class="pi-pricing">
      <div class="pi-price featured">
        <span class="pill">Recommended</span>
        <h3>90-minute session</h3>
        <div class="amt">$180<span> / session</span></div>
        <p class="note">Room to teach the topic, work through it together, and finish with an independent check — the cadence I recommend for steady weekly progress.</p>
      </div>
      <div class="pi-price">
        <h3>60-minute session</h3>
        <div class="amt">$130<span> / session</span></div>
        <p class="note">Best for targeted help, test review, or self-directed students who come with specific questions.</p>
      </div>
    </div>

    <p style="margin-top:1.5rem;font-weight:600;">Every session includes:</p>
    <ul class="pi-list">
      <li><b>Pre-planned, instructor-led teaching</b> aligned to your student's course and pacing.</li>
      <li><b>Session notes and full solutions</b> uploaded after each meeting for review.</li>
      <li><b>Calculator integration</b> (TI-84 Plus CE) so students avoid avoidable test-day mistakes.</li>
      <li><b>AP-aligned writing</b> focus on setup, justification, and interpretation.</li>
    </ul>

    <p style="margin-top:1.3rem;font-weight:600;">Optional add-on: between-session support &nbsp;<span style="color:var(--accent-ink);">$200/month ($50/week)</span></p>
    <ul class="pi-list">
      <li><b>Weekly assigned problem sets</b> with written feedback on method, setup, and communication, giving the student extra accountability to keep practicing between sessions.</li>
      <li><b>Generous between-session availability</b> on weekdays and weekends for questions and clarifications, so students never stay stuck for long and keep their momentum.</li>
      <li><b>Additional cheat sheets and study resources</b> to keep and reference throughout the year.</li>
      <li><b>Monthly parent check-ins</b> by email or call to review progress, strengths, and next steps.</li>
    </ul>

    <div class="pi-billing">
      <strong>Billing:</strong> Sessions are billed monthly, with invoices sent on the 1st. I accept a limited number of students each academic year; once capacity is reached, I maintain a short waitlist.
    </div>
  </div>

  <!-- TECHNOLOGY -->
  <div class="pi-section">
    <p class="label">How it works</p>
    <h2>Technology &amp; setup</h2>
    <ul class="pi-list">
      <li><b>Zoom-based sessions</b> delivered live.</li>
      <li><b>Digital whiteboard</b> with live handwriting and annotation for step-by-step setup and reasoning.</li>
      <li><b>Private shared folder</b> (Dropbox) for session notes and materials; parents may be added on request.</li>
      <li><b>Student setup:</b> a quiet location, stable internet, a graphing calculator (TI-84 Plus CE recommended), and a consistent note-taking method.</li>
    </ul>
  </div>

  <!-- FAQ -->
  <div class="pi-section">
    <p class="label">Questions</p>
    <h2>Frequently asked</h2>
    <div class="pi-faq">
      <details>
        <summary>Are sessions online or in person?</summary>
        <p>Sessions are conducted live over Zoom with a digital whiteboard for step-by-step work. This lets me support students wherever they are while keeping all notes and materials organized in one shared folder.</p>
      </details>
      <details>
        <summary>How do you align with my student's class?</summary>
        <p>I follow your student's course pacing and tailor each session to their current topics, assignments, and the specific errors I observe, so our work reinforces what is happening in the classroom rather than running parallel to it.</p>
      </details>
      <details>
        <summary>What happens before the AP exam?</summary>
        <p>In the final one to two months, sessions shift into focused exam preparation with timed practice, full free-response and multiple-choice work, and targeted review. All preparation materials are included.</p>
      </details>
      <details>
        <summary>What if we need to reschedule?</summary>
        <p>Occasional schedule changes are normal. I ask for reasonable notice when possible and do my best to accommodate.</p>
      </details>
      <details>
        <summary>Is the between-session support required?</summary>
        <p>No. It is an optional monthly add-on for families who want assigned practice, written feedback, and weekday support between sessions. Many students do well with the weekly session alone.</p>
      </details>
      <details>
        <summary>What does my student need to get started?</summary>
        <p>A quiet space, stable internet, a graphing calculator (TI-84 Plus CE recommended), and a consistent note-taking method.</p>
      </details>
    </div>
  </div>

  <!-- AVAILABILITY -->
  <div class="pi-section">
    <p class="label">Availability</p>
    <h2>Scheduling and getting started</h2>
    <p>I'm based in the Pacific time zone and regularly work with students in other time zones; we will find a weekly slot that fits your schedule.</p>
    <p>Weekly slots are limited and tend to fill quickly, so it is best to secure a place on the roster early. I take only a small number of students each academic year, and once the roster is full I keep a short waitlist.</p>
    <div class="pi-callout">
      <p><b>The strongest results start at the beginning of the course.</b> The ideal time to begin is the first weeks of the term, while each topic can be built correctly the first time, before small gaps quietly compound into the ones that cost points later. Students who join mid-semester are very welcome and can make real gains; we simply spend our early sessions closing those gaps before we get ahead of new material. Reserving a spot before the term begins lets us prepare, stay ahead of your class's pacing, and settle into a steady weekly rhythm from the very first week.</p>
    </div>
  </div>

  <!-- CTA -->
  <div class="pi-cta">
    <h2>Getting started</h2>
    <p>Two easy ways to begin — send me a quick email with your question, or book a free 15-minute meet-and-greet. After we talk, I'll recommend the best fit for your student.</p>
    <link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
    <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
    <div class="pi-cta-actions">
      <a href="mailto:hi@katherinedelno.com" class="pi-btn">Email me</a>
      <a href="https://calendly.com/katherinedelno" class="pi-btn pi-btn-outline"
         onclick="Calendly.initPopupWidget({url:'https://calendly.com/katherinedelno'});return false;">Book a meet-and-greet</a>
    </div>
    <span class="email">or email <a href="mailto:hi@katherinedelno.com">hi@katherinedelno.com</a></span>
  </div>

  <!-- DISCLAIMER -->
  <div class="pi-fine">
    <p class="label">Academic progress &amp; no guaranteed outcomes</p>
    <p>My goal is to help students build durable understanding, stronger problem-solving habits, and clearer written communication through structured instruction, targeted practice, and actionable feedback aligned with AP expectations.</p>
    <p>I cannot and do not guarantee any specific grade, test score, class placement, or AP exam result. Outcomes depend on factors outside my control, including the student's consistency between sessions, completion of assigned work, attendance, classroom instruction and grading policies, assessment difficulty, and test-day conditions. By enrolling, families are purchasing instructional time and academic coaching, not a promised outcome.</p>
    <p><small>AP&reg; is a registered trademark owned by the College Board, which is not affiliated with and does not endorse this private instruction service.</small></p>
  </div>

</div>
