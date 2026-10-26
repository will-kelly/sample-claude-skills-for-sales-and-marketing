---
name: ai-pipeline-blueprint
description: Designs an AI-assisted production pipeline for one recurring content type (blog posts, release notes, case studies, newsletters, battle cards). It maps each stage, decides where AI does the work, where it assists and where a human must decide, and outputs a pipeline spec with inputs, prompts, checkpoints and quality gates. Use when a team wants to use AI to produce content faster without losing quality, or asks "how should we use Claude in our content workflow?"
---

# AI pipeline blueprint

Most teams adopt AI for content by handing writers a chatbot and hoping. Output goes up for a month, then quality drops, reviewers get buried in drafts that sound like everyone else's, and somebody senior declares that AI doesn't work for "our kind of content."

The problem isn't the model. It's that nobody designed the pipeline. AI is good at some stages and bad at others, and the stages where it's bad are exactly where a human has to stay in charge: deciding what to say, checking that it's true, and judging whether it sounds like the company.

This skill designs that pipeline for one content type at a time.

## What you need from the user

- **The content type**: pick one. A pipeline for "all our content" is a pipeline for nothing.
- **How it's made today**: steps, people, tools, typical time.
- **Inputs that exist**: style guide, voice examples, briefs, source material (transcripts, release notes, product docs), past examples of good pieces.
- **Quality bar**: what makes a piece good or bad for this team. Ask for one example of each if they have them.
- **Constraints**: approved AI tools, data that can't leave the company, review requirements.

Before designing, check the engine. If intake or review is broken (see content-engine-diagnostic and review-bottleneck-mapper), say so. Faster drafting feeds a broken review process more drafts to sit on.

## How to design it

1. **Break the work into stages.** Typically: brief, research and sourcing, outline, draft, fact and claims check, voice edit, review, packaging (titles, metadata, social copy), publish.
2. **Assign each stage a mode**:
   - **AI does**: low judgment, high volume, easy to check. Metadata, summaries, first-pass outlines, format conversions.
   - **AI assists, human decides**: AI produces options or a draft and a person picks, edits and owns it. Drafting usually lives here.
   - **Human only**: the angle and point of view, final claims approval, anything requiring customer or legal judgment.
3. **Define the inputs for each AI stage.** What the model gets: brief, source material, voice examples, constraints. Most bad AI output is a missing-input problem.
4. **Write the gates.** Between stages, the specific checks a piece has to pass, such as "every statistic has a linked source," "no claims beyond the approved claims list" or "passes the voice checklist." Gates make quality checkable instead of a matter of taste.
5. **Plan the failure modes.** Hallucinated facts, generic voice, invented quotes, drift from the brief. For each, say which gate catches it.

## Output format

**Pipeline at a glance**

| Stage | Mode | Owner | Inputs | Output | Gate to pass |
|---|---|---|---|---|---|

**Stage specs**: for every AI or AI-assisted stage, a short spec: purpose, inputs, a starter prompt or Claude skill outline, what good output looks like, and the most common failure.

**Human checkpoints**: where a person must sign off, and what they're checking. Keep this list short and serious.

**Expected time**: current versus projected time per piece, by stage, marked as an estimate.

**Rollout plan**: run it on three to five pieces, compare against the old process on time and quality, then adjust. Name the metric that decides whether it's working.

## Rules

- Never put "AI does" on a stage that decides what the company claims or believes.
- Never let AI generate quotes, customer names, statistics or sources. It can find and summarize real ones the team provides.
- One content type per blueprint. If the user wants several, do the highest-volume one first.
- Be honest about time savings. Drafting gets faster. Review often doesn't, and sometimes gets slower at first.
