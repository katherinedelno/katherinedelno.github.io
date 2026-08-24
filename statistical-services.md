---
layout: page
title: Statistical Services
permalink: /statistical-services/
description: "Project-based statistical analysis, methodological and statistical review, and mathematics and statistics assessment development. Reproducible work in R. M.S. Statistics, University of Washington."
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
  .sv-area p{margin:0;font-size:.97rem;max-width:62ch}
  .sv-area p+p{margin-top:.7rem}
  .sv-note{font-size:.9rem;color:var(--muted)}

  .sv-list{list-style:none;padding:0;margin:1rem 0 0;max-width:62ch}
  .sv-list li{position:relative;padding:0 0 .5rem 1.4rem;font-size:.92rem;color:var(--ink)}
  .sv-list li:last-child{padding-bottom:0}
  .sv-list li::before{content:"";position:absolute;left:0;top:.55em;width:6px;height:6px;border-radius:50%;background:var(--accent)}

  /* Principles card. The definition grid from the practice page. */
  .sv-standard{margin:1.6rem 0 0;padding:26px 28px;border:1px solid var(--line);border-radius:12px;background:var(--card)}
  .sv-standard dl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px 32px;margin:0}
  .sv-standard dt{font-size:.95rem;font-weight:700;letter-spacing:-.01em;margin:0 0 .3rem}
  .sv-standard dd{margin:0;font-size:.875rem;color:var(--muted);line-height:1.6}

  .sv-callout{margin-top:1.3rem;padding:20px 24px;border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:12px;background:var(--card);max-width:74ch}
  .sv-callout p{margin:0;font-size:.97rem}
  .sv-callout p+p{margin-top:.8rem}

  .pg-btn{display:inline-block;background:var(--accent);color:#fff !important;padding:13px 26px;border-radius:10px;text-decoration:none;font-weight:600;border:1px solid var(--accent);transition:opacity .15s ease}
  .pg-btn:hover{opacity:.9}
  .pg-cta{text-align:center;margin:3.4rem 0 1rem;padding:2.4rem 1rem;background:var(--accent-soft);border-radius:16px}
  .pg-cta h2{border:none;margin:0 0 .5rem;font-size:1.35rem}
  .pg-cta p{margin:0 auto 1.4rem;color:var(--muted);max-width:54ch}

  /* Selected work. The kicker and the statistics strip are the existing
     project components from projects.css; only the wrapper is new here. */
  .sv-project{margin:1.8rem 0 0;max-width:74ch}
  .sv-project h3{margin:0 0 .8rem;font-size:1.14rem;line-height:1.3;letter-spacing:-.015em}
  .sv-project p{font-size:.97rem}
  .sv-project p+p{margin-top:.9rem}
  .pg .pj-stats{margin:1.5rem 0 1.4rem}
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
    <p>I accept a small number of projects at a time in statistical analysis, methodological review, and mathematics and statistics assessment work. I am most useful on projects that turn on care: choosing a method that matches the design, stating what the analysis assumes, and writing the result so that a reader can see exactly what it does and does not establish.</p>
    <p>I hold an M.S. in Statistics from the University of Washington and a B.S. in Mathematics. My graduate training was theoretical as well as applied, and my independent research was methodological. Most of my working time is spent teaching, which is a continual exercise in making quantitative reasoning legible to someone who does not yet share it. Both of those show in how I work.</p>
    <p>This is deliberately a small practice. What I offer is careful work inside a defined range of methods, an account of it that another statistician could check, and a direct answer when a project falls outside what I am trained to do.</p>
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
    <p>Each area below is bounded on purpose. The list is shorter than my coursework, because completing coursework in a method is not the same as being ready to take responsibility for it inside someone else's project.</p>

    <div class="sv-areas">

      <div class="sv-area">
        <h3>Statistical analysis and research support</h3>
        <div>
          <p>I take a research question and a dataset and return an analysis another statistician could check. In practice that means agreeing first on what the question is in statistical terms, preparing the data with every decision recorded, fitting a model suited to how the data were collected, and reporting estimates with their uncertainty and their qualifications.</p>
          <ul class="sv-list">
            <li>research questions translated into estimands, models, and testable hypotheses</li>
            <li>data cleaning and preparation, with the choices documented rather than buried</li>
            <li>regression and related modeling, chosen to match how the data were collected</li>
            <li>exploratory analysis, model checking, and diagnostics</li>
            <li>figures and tables built to carry a specific argument</li>
            <li>reproducible analysis in R, delivered as commented code that regenerates every reported number</li>
            <li>methodological consultation at the design stage, which is usually where it is worth the most</li>
          </ul>
        </div>
      </div>

      <div class="sv-area">
        <h3>Statistical review</h3>
        <div>
          <p>Review is often the most useful thing I can do on a short timeline. I read an analysis the way a careful referee reads it: whether the method suits the design, whether the assumptions were checked or merely inherited, and whether the conclusions stay inside what the model and the data support.</p>
          <ul class="sv-list">
            <li>whether the analytical approach fits the study design and the measurements taken</li>
            <li>assumptions the result depends on that were never stated</li>
            <li>interpretation checks: what the estimate means, against what it is being asked to mean</li>
            <li>multiplicity, missing data, and the other points at which a finding quietly weakens</li>
            <li>code and output review, where the analysis was done in R and the code is available</li>
            <li>the quantitative sections of a manuscript, report, or internal analysis</li>
          </ul>
          <p class="sv-note" style="margin-top:1rem;">Scope depends on the subject matter and the methods involved. I say at the outset which parts of an analysis I am able to evaluate and which I am not, and I put that in writing before the work begins.</p>
        </div>
      </div>

      <div class="sv-area">
        <h3>Assessment and quantitative content</h3>
        <div>
          <p>I write and review mathematics and statistics assessment material. This is the closest of the four areas to what I already do daily. My instructional practice runs on items I write myself, with solutions that show where each point is earned and with incorrect options chosen because a particular error produces them.</p>
          <ul class="sv-list">
            <li>item writing in statistics, precalculus, and calculus, including AP-level and introductory college material</li>
            <li>item review for mathematical and statistical accuracy</li>
            <li>solutions, rationales, and scoring notes, including the reasoning behind each incorrect option</li>
            <li>difficulty and conceptual-quality review, including whether an item tests the idea it claims to test</li>
            <li>alignment review against a stated framework or course description</li>
            <li>review of instructional material for mathematical correctness and for the accuracy of its explanations</li>
          </ul>
          <p class="sv-note" style="margin-top:1rem;">Work of this kind, written for my own students, is public on this site: the <a href="/practice/">practice sets</a> show the item and solution standard, and the <a href="/resources/">resource articles</a> show the instructional writing.</p>
        </div>
      </div>

      <div class="sv-area">
        <h3>Quantitative communication</h3>
        <div>
          <p>Some projects need an analysis explained rather than performed. I write and edit technical material for readers who have to act on a result without being able to reproduce it, and I try to do that without letting the result sound more certain than it is.</p>
          <ul class="sv-list">
            <li>statistical results written for a non-specialist audience</li>
            <li>methods and results sections drafted or revised</li>
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
    <p>Selecting a procedure and producing numbers is the smallest part of statistical work. The substantive part is working out what the design, the data, and the assumptions actually permit anyone to conclude, and then saying no more than that. Six commitments follow from it, and they hold on every project.</p>

    <div class="sv-standard">
      <dl>
        <div>
          <dt>The method follows the design</dt>
          <dd>How the data were produced decides the model, not the reverse. Clustering, repeated measurement, and the way a sample was drawn change what an estimate means before any software is opened.</dd>
        </div>
        <div>
          <dt>Assumptions are stated</dt>
          <dd>Every model rests on conditions. I write down the ones a result depends on, check the ones that can be checked, and name the ones the data cannot settle either way.</dd>
        </div>
        <div>
          <dt>The analysis reproduces</dt>
          <dd>Work is delivered as commented code that runs start to finish from the raw data. Every number in the write-up traces back to the line that produced it, including the ones in the figures.</dd>
        </div>
        <div>
          <dt>Interpretation stays inside the evidence</dt>
          <dd>Estimates are reported with their uncertainty and with what the design supports. An association is not described as an effect. A null result is reported as a null result.</dd>
        </div>
        <div>
          <dt>Limitations are part of the deliverable</dt>
          <dd>The write-up says where the analysis is weak and what would strengthen it. That section is not a formality. It is usually the part a careful reader turns to first.</dd>
        </div>
        <div>
          <dt>The result is written to be understood</dt>
          <dd>Quantitative work fails at the point of explanation more often than at the point of estimation. I write the account of an analysis for the person who has to act on it.</dd>
        </div>
      </dl>
    </div>
  </div>

  <!-- SELECTED WORK -->
  <div class="pg-section" id="work">
    <p class="label">Selected work</p>
    <h2>Statistical research</h2>
    <p>The work below is graduate research rather than client work, and it is described as such. I include it because it shows the kind of statistical problem I am able to take on, and because it is the clearest evidence available of how I approach method.</p>

    <div class="sv-project">
      <p class="pj-feature__kicker"><span>Independent research</span><span>Sole author</span><span>2025</span></p>
      <h3>RandomForestSpecCheck</h3>
      <p>A linear mixed model can be misspecified in several ways at once, and the standard diagnostics each look for a failure the analyst already suspects. I developed a nonparametric alternative. A random forest is asked to predict the fitted model's conditional residuals from covariates the analyst names. It is scored out of bag, so that fitting residual noise earns it nothing. The null distribution comes from permuting residuals within clusters, which breaks the relationship between residuals and predictors while preserving the clustered design. The result is a single screening test for mean structure the model has failed to account for.</p>
      <div class="pj-stats">
        <div class="pj-stat">
          <div class="pj-stat__value">5,400</div>
          <div class="pj-stat__label">simulated datasets across 54 parameter configurations, in the first study alone</div>
        </div>
        <div class="pj-stat">
          <div class="pj-stat__value">1&ndash;3%</div>
          <div class="pj-stat__label">empirical false-positive rate at a nominal 5% level, under correct specification</div>
        </div>
        <div class="pj-stat">
          <div class="pj-stat__value">80&ndash;100%</div>
          <div class="pj-stat__label">power against large departures in mean structure, in the designs that support it</div>
        </div>
      </div>
      <p>The same simulations established where the diagnostic has no power. It does not detect misspecified variance structure, and the within-cluster permutation leaves a wholly omitted cluster-level effect invisible to it. Both results are stated in the write-up as part of the method's scope rather than left out of it. The work was completed independently in the Department of Statistics at the University of Washington and written for submission to a statistics methodology journal. It has not been peer reviewed.</p>
      <p class="sv-more"><a href="/projects/random-forest-spec-check/">Read the full account</a></p>
    </div>

    <p style="margin-top:2.2rem;">My applied work includes a doubly robust analysis of food insecurity and type 2 diabetes across three cycles of NHANES, which returned a null estimate and spent most of its length on which parts of the causal question the survey data could identify at all, and two natural language classification projects, one of them pairing a fine-tuned transformer with conformal prediction to return label sets meeting a target coverage level. All four projects have full write-ups under <a href="/about/#statistical-work">statistical work</a>.</p>

    <p style="margin-top:1.1rem;">What they have in common is what governs paid work as well. The method should follow from the structure of the data and the question being asked, and the assumptions and the blind spots belong in the write-up rather than in the analyst's head.</p>
  </div>

  <!-- BACKGROUND -->
  <div class="pg-section" id="background">
    <p class="label">Background</p>
    <h2>Training and qualifications</h2>
    <p>I hold an <b>M.S. in Statistics from the University of Washington</b> and a <b>B.S. in Mathematics from the University of Nevada, Reno</b>. My graduate work covered a full theoretical inference sequence in which estimators, tests, and intervals were derived rather than applied, along with regression for independent and correlated data, experimental design, categorical data analysis, causal inference, and statistical computing in R and Python. My undergraduate training was proof-based, through two semesters of real analysis.</p>
    <p>I have taught statistics as a graduate teaching assistant in a university mathematics and statistics department, designed and led a one-on-one directed reading course in statistical learning at the University of Washington, and taught privately since 2025. I list teaching under qualifications rather than biography, because explaining a method precisely to someone who does not already accept it is a large part of what a statistical collaborator is asked to do.</p>
    <p>Complete coursework, research, and teaching history are on the <a href="/about/">about page</a>, which is the fuller account of the training this page draws on.</p>
  </div>

  <!-- SCOPE -->
  <div class="pg-section" id="scope">
    <p class="label">Engagements</p>
    <h2>Scope and availability</h2>
    <p>I take a small number of projects alongside a full teaching schedule, so availability is genuinely limited during the academic year. Each engagement is scoped individually before it begins: what the question is, what the deliverable is, what I would need from you, and how long it should take. Fees are quoted for the project once that is settled, and agreed in writing before any work starts.</p>
    <p style="margin-top:1.2rem;">Whether I take a project depends on:</p>
    <ul class="sv-list">
      <li>whether the methods involved are ones I have been trained in and have used</li>
      <li>whether the question is one the available data can actually answer</li>
      <li>whether the timeline allows the checking the work needs</li>
      <li>capacity, which is set by the teaching schedule first</li>
    </ul>
    <p style="margin-top:1.3rem;">Data, unpublished manuscripts, and assessment material are treated as confidential, and I am glad to sign an agreement to that effect before receiving anything. Where a research project would warrant acknowledgment or authorship, that is settled during scoping rather than after the analysis is finished.</p>

    <div class="sv-callout">
      <p>There is work I do not take. I do not accept clinical, regulatory, or legal engagements, and nothing here is medical, legal, or financial advice. I do not guarantee a particular finding, a statistically significant result, or a publication outcome, and I will not conduct an analysis built to reach a conclusion chosen in advance.</p>
      <p>If a project needs a method outside my training, I will say so rather than learn it at your expense, and where I can I will suggest a better-suited person.</p>
    </div>
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
    <p style="margin-top:1.2rem;">I reply to inquiries within a few business days. If a project is not a fit, I will say so directly rather than leave it open.</p>
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
