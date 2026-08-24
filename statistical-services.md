---
layout: page
title: Statistical Services
permalink: /statistical-services/
description: "Selective, project-based statistical analysis, statistical review, and mathematics and statistics assessment work. M.S. Statistics, University of Washington."
---


<style>
  @import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800;900&display=swap');
  /* ---- Scoped styling for the Statistical Services page ----
     Nothing new is invented here. The tokens, the label rule, the section
     divider, the dot list, the definition card, and the button are the same
     components used on the private instruction, practice, and resources
     pages, renamed only where a page-local variant was needed. */
  .site-header .site-title{display:none}
  .page-heading,.post-header{display:none}
  body{font-family:'Hanken Grotesk',-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}

  .pg{--ink:#1f1f1f;--muted:#5c5c5c;--line:#e6e6e6;--accent:#2b2b2b;--accent-soft:#f0f0f0;--card:#fbfbfb;--faint:#9a9a97;color:var(--ink);line-height:1.65}
  .pg p{max-width:72ch}
  .pg h1,.pg h2,.pg h3,.pg h4{font-weight:700}
  .pg b,.pg strong{font-weight:600}
  .pg .label{text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700;color:var(--accent);margin:0 0 .7rem}

  .pg-hero{margin:0 0 1rem;max-width:64ch}
  .pg-hero h1{font-size:2.1rem;line-height:1.15;margin:0 0 .9rem;letter-spacing:-.02em;font-weight:700}
  .pg-hero p{font-size:1.06rem;color:var(--muted);line-height:1.6;margin:0 0 .9rem}
  .pg-hero p:last-child{margin-bottom:0}

  .pg-jump{display:flex;gap:8px 24px;flex-wrap:wrap;margin:2rem 0 0}
  .pg-jump a{font-size:.76rem;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--muted);text-decoration:none}
  .pg-jump a:hover{color:var(--ink)}

  .pg-section{margin:3.4rem 0 0;padding-top:2.8rem;border-top:1px solid var(--line);scroll-margin-top:24px}
  .pg-section h2{font-size:1.35rem;margin:0 0 1rem;letter-spacing:-.01em}

  /* Areas of work. The two-column row from the course list on the private
     instruction page: name on the left, the work itself on the right. */
  .sv-areas{margin-top:1.6rem}
  .sv-area{display:grid;grid-template-columns:210px minmax(0,1fr);gap:28px;padding:26px 2px}
  .sv-area+.sv-area{border-top:1px solid var(--line)}
  .sv-area h3{margin:0;font-size:1.06rem;line-height:1.3;letter-spacing:-.01em}
  .sv-area p{margin:0;max-width:62ch}
  .sv-area p+p{margin-top:.7rem}
  .sv-note{font-size:.9rem;color:var(--muted)}

  .sv-list{list-style:none;padding:0;margin:1rem 0 0;max-width:62ch}
  .sv-list li{position:relative;padding:0 0 .55rem 1.4rem;color:var(--ink)}
  .sv-list li:last-child{padding-bottom:0}
  .sv-list li::before{content:"";position:absolute;left:0;top:.55em;width:6px;height:6px;border-radius:50%;background:var(--accent)}

  /* Principles card. The definition grid from the practice page. */
  .sv-standard{margin:1.6rem 0 0;padding:26px 28px;border:1px solid var(--line);border-radius:12px;background:var(--card)}
  .sv-standard dl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px 32px;margin:0}
  .sv-standard dt{font-size:.95rem;font-weight:700;letter-spacing:-.01em;margin:0 0 .3rem}
  .sv-standard dd{margin:0;font-size:.875rem;color:var(--muted);line-height:1.6}


  .pg-btn{display:inline-block;background:var(--accent);color:#fff !important;padding:13px 26px;border-radius:10px;text-decoration:none;font-weight:600;border:1px solid var(--accent);transition:opacity .15s ease}
  .pg-btn:hover{opacity:.9}
  .pg-cta{text-align:center;margin:3.4rem 0 1rem;padding:2.4rem 1rem;background:var(--accent-soft);border-radius:16px}
  .pg-cta h2{border:none;margin:0 0 .5rem;font-size:1.35rem}
  .pg-cta p{margin:0 auto 1.4rem;color:var(--muted);max-width:54ch}

  /* Selected work. The statistics strip is the existing project component
     from projects.css; the rest of the section is ordinary section prose. */
  .sv-more{font-size:.95rem;margin-top:1.1rem}

  .pg-fine{margin-top:2.6rem;padding-top:1.6rem;border-top:1px solid var(--line)}
  .pg-fine p{font-size:.9rem;color:var(--muted);max-width:74ch}
  .pg-fine .label{color:var(--muted)}
  .pg-fine .label::before{display:none}

  @media (max-width:720px){
    .sv-area{grid-template-columns:1fr;gap:10px;padding:22px 0}
    .sv-standard dl{grid-template-columns:1fr;gap:18px}
    .sv-standard{padding:20px}
    .pg-hero h1{font-size:1.7rem}
    .pg-section{margin-top:2.8rem;padding-top:2.2rem}
  }
  @media (prefers-reduced-motion: reduce){
    .pg-btn{transition:none}
  }
</style>
<div class="pg" markdown="0">

  <div class="pg-hero">
    <p class="label">Services</p>
    <h1>Statistical and Quantitative Services</h1>
    <p>Statistical work depends on more than selecting a procedure and producing output. The design of a study, the structure of the data, the assumptions of the model, and the question being asked all constrain what an analysis can reasonably establish.</p>
    <p>I accept a small number of projects in statistical analysis, statistical review, and mathematics and statistics assessment work. I hold an M.S. in Statistics from the University of Washington and a B.S. in Mathematics. Most of my working time is spent teaching, which is a continual exercise in making quantitative reasoning legible to someone who does not yet share it.</p>
  </div>

  <nav class="pg-jump" aria-label="Page sections">
    <a href="#areas">Areas of work</a>
    <a href="#method">How I work</a>
    <a href="#work">Selected work</a>
    <a href="#background">Background</a>
    <a href="#scope">Scope</a>
    <a href="#inquiries">Inquiries</a>
  </nav>

  <!-- AREAS OF WORK -->
  <div class="pg-section" id="areas">
    <p class="label">Areas of work</p>
    <h2>Four kinds of project</h2>
    <p>The scope below reflects the work I am prepared to take responsibility for professionally, rather than the full range of methods I have encountered in coursework and research.</p>

    <div class="sv-areas">

      <div class="sv-area">
        <h3>Statistical analysis and research support</h3>
        <div>
          <p>I take a research question and a dataset and return an analysis another statistician could check. In practice that means agreeing first on what the question is in statistical terms, preparing the data with every decision recorded, fitting a model suited to how the data were collected, and reporting estimates with their uncertainty and their qualifications.</p>
          <ul class="sv-list">
            <li>research questions translated into estimands, models, and testable hypotheses</li>
            <li>data preparation and checking, with the choices documented rather than buried</li>
            <li>regression and related modeling, chosen to match how the data were collected</li>
            <li>exploratory analysis, model checking, and diagnostics</li>
            <li>figures and tables designed to communicate the relevant findings clearly</li>
            <li>reproducible analysis in R, delivered as commented code that regenerates every reported number</li>
            <li>methodological consultation at the design stage, which is usually where it is worth the most</li>
          </ul>
        </div>
      </div>

      <div class="sv-area">
        <h3>Statistical review</h3>
        <div>
          <p>I review statistical analyses with attention to whether the chosen method fits the design and the data, whether important assumptions have been examined, and whether the resulting interpretation is supported by the analysis. Depending on scope, this may include:</p>
          <ul class="sv-list">
            <li>the analytical strategy and the choice of method</li>
            <li>model assumptions and the checks available for them</li>
            <li>statistical code and output, where the analysis was done in R</li>
            <li>interpretation, including multiplicity, missing data, and the other points at which a finding weakens</li>
            <li>the quantitative sections of reports and manuscripts</li>
          </ul>
        </div>
      </div>

      <div class="sv-area">
        <h3>Assessment and quantitative content</h3>
        <div>
          <p>I develop and review mathematics and statistics assessment material, including individual items, solutions, rationales, and related quantitative content. My teaching work has involved substantial original curriculum and problem development, with particular attention to conceptual structure, notation, common errors, and the reasoning an item actually requires.</p>
          <ul class="sv-list">
            <li>item writing in statistics, precalculus, and calculus, including AP-level and introductory college material</li>
            <li>item review for mathematical and statistical accuracy</li>
            <li>solutions, rationales, and scoring notes, including the reasoning behind each incorrect option</li>
            <li>review of conceptual difficulty and mathematical rigor</li>
            <li>alignment review against a stated framework or course description</li>
          </ul>
          <p class="sv-note" style="margin-top:1rem;">Work of this kind, written for my own students, is public on this site: the <a href="/practice/">practice sets</a> show the item and solution standard, and the <a href="/resources/">resource articles</a> show the instructional writing.</p>
        </div>
      </div>

      <div class="sv-area">
        <h3>Quantitative communication</h3>
        <div>
          <p>I also work on the communication of quantitative material where statistical accuracy and clarity are both important.</p>
          <ul class="sv-list">
            <li>statistical explanations written for non-specialist readers</li>
            <li>methods and results sections reviewed or revised for statistical accuracy and clarity</li>
            <li>mathematical and statistical editing, including notation and the consistency of terms</li>
            <li>clarity review of quantitative material intended for publication, teaching, or internal use</li>
          </ul>
        </div>
      </div>

    </div>
  </div>

  <!-- HOW I WORK -->
  <div class="pg-section" id="method">
    <p class="label">How I work</p>
    <h2>Method before output</h2>
    <p>Four commitments follow from those constraints, and they hold on every project.</p>

    <div class="sv-standard">
      <dl>
        <div>
          <dt>Method follows design</dt>
          <dd>The analytical method should follow from the structure of the data, the research design, and the question being asked. I do not treat statistical procedures as interchangeable tools chosen after the fact.</dd>
        </div>
        <div>
          <dt>Assumptions are explicit</dt>
          <dd>Statistical conclusions depend on assumptions. I make those assumptions visible and examine them where the analysis permits, rather than leaving them implicit in software output.</dd>
        </div>
        <div>
          <dt>Analysis is reproducible</dt>
          <dd>When code is part of an engagement, I organize the analysis so that the major steps can be inspected, reproduced, and revised. The objective is not only to obtain a result but to leave a clear analytical record.</dd>
        </div>
        <div>
          <dt>Interpretation stays within the evidence</dt>
          <dd>I distinguish between what an analysis establishes, what it suggests, and what remains uncertain. Limitations are part of the interpretation rather than a qualification added at the end.</dd>
        </div>
      </dl>
    </div>
  </div>

  <!-- SELECTED WORK -->
  <div class="pg-section" id="work">
    <p class="label">Selected work</p>
    <h2>Methodological research: RandomForestSpecCheck</h2>
    <p>The work below is graduate research rather than client work. I include it because it shows the kind of statistical problem I take on and how I approach method.</p>

    <p style="margin-top:1.4rem;">RandomForestSpecCheck is a model diagnostic I developed as sole author in 2025, in the Department of Statistics at the University of Washington. A linear mixed model can be misspecified in several ways at once, and the standard diagnostics each look for a failure the analyst already suspects. The procedure asks a random forest to predict the fitted model's conditional residuals from covariates the analyst names, scores it out of bag so that fitting residual noise earns it nothing, and generates the null distribution by permuting residuals within clusters, which preserves the clustered design. Across 5,400 simulated datasets, the false-positive rate under correct specification ran between one and three percent against a nominal five percent level.</p>

    <p style="margin-top:.9rem;">The same simulations established where the diagnostic is not informative. It does not detect misspecified variance structure, and a wholly omitted cluster-level effect is invisible to it. Both results are stated in the write-up as part of the method's scope. The work was written for submission to a statistics methodology journal and has not been peer reviewed.</p>

    <p style="margin-top:.9rem;">My applied work includes a doubly robust causal analysis of national survey data and two natural language classification projects, one of them using conformal prediction to return label sets meeting a target coverage level.</p>

    <p class="sv-more"><a href="/statistical-work/">View selected statistical work &rarr;</a></p>
  </div>

  <!-- BACKGROUND -->
  <div class="pg-section" id="background">
    <p class="label">Background</p>
    <h2>Training and qualifications</h2>
    <p>I hold an <b>M.S. in Statistics from the University of Washington</b> and a <b>B.S. in Mathematics from the University of Nevada, Reno</b>. My graduate work covered a full theoretical inference sequence in which estimators, tests, and intervals were derived rather than applied, along with regression for independent and correlated data, experimental design, categorical data analysis, causal inference, and statistical computing in R and Python. My undergraduate training was proof-based, through two semesters of real analysis.</p>
    <p>I have taught statistics as a graduate teaching assistant in a university mathematics and statistics department, designed and led a one-on-one directed reading course in statistical learning at the University of Washington, and taught privately since 2025. Explaining a method precisely to someone who does not already accept it is a large part of what a statistical collaborator is asked to do.</p>
    <p>Complete coursework, research, and teaching history are on the <a href="/about/">about page</a>.</p>
  </div>

  <!-- SCOPE -->
  <div class="pg-section" id="scope">
    <p class="label">Engagements</p>
    <h2>Scope</h2>
    <p>Projects are accepted selectively and scoped individually according to the statistical question, the available materials, the timeline, and methodological fit. I take responsibility only for work that falls within my areas of competence and will decline or narrow an engagement when the requested analysis requires expertise outside that scope.</p>
    <p style="margin-top:1.1rem;">I do not undertake clinical or regulatory statistical work, legal expert analysis, or analyses structured to support a predetermined conclusion.</p>
    <p style="margin-top:1.1rem;">Fees are quoted for the project once it has been scoped, and agreed in writing before work begins. Data, unpublished manuscripts, and assessment material are treated as confidential, and I am glad to sign an agreement to that effect. Where a project would warrant acknowledgment or authorship, that is settled during scoping rather than afterward.</p>
  </div>

  <!-- INQUIRIES -->
  <div class="pg-section" id="inquiries">
    <p class="label">Inquiries</p>
    <h2>What to include</h2>
    <p>A first message does not need to be long. The more of the following it contains, the sooner I can tell you whether I am the right person and what the work would involve.</p>
    <ul class="sv-list">
      <li>a short description of the project and the question behind it</li>
      <li>the kind of work needed: analysis, review, assessment material, or writing</li>
      <li>the data or materials involved and their current state</li>
      <li>any methodological context, including approaches already used or expected</li>
      <li>your timeline, and any deadline that cannot move</li>
    </ul>
    <p style="margin-top:1.2rem;">I reply to inquiries within a few business days.</p>
  </div>

  <div class="pg-cta">
    <h2>Project inquiries</h2>
    <p>Write with a brief description and a timeline. I will tell you whether it is a fit, what I would need, and what it would cost.</p>
    <a href="mailto:hi@katherinedelno.com?subject=Project%20inquiry" class="pg-btn">Discuss a project</a>
  </div>

  <div class="pg-fine">
    <p class="label">Note</p>
    <p>This page describes project work only. Private mathematics and statistics instruction, which remains the larger part of my practice, is described under <a href="/private-instruction/">private instruction</a>.</p>
  </div>

</div>
