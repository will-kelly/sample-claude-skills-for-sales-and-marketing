---
name: content-engine-diagnostic
description: Diagnoses where a marketing team's content engine actually breaks, across intake, planning, production, review, publishing, distribution, measurement and maintenance, and scores each stage on a five-level maturity model. Use when a team says content is slow, inconsistent or not working, when a new content leader is assessing what they inherited, or before buying tools or AI to "fix" content.
---

# Content engine diagnostic

When content isn't working, teams usually blame the stage they can see. Writers are slow. The blog doesn't rank. We need more output. Then they buy a tool or hire a freelancer for that stage, and nothing changes, because the real break was two stages upstream. Drafts were slow because nobody owned intake. The blog didn't rank because nothing ever got updated.

This skill looks at the whole engine, scores each stage, and finds the constraint: the one stage limiting everything downstream. Fix that first. Everything else is secondary until it moves.

## What you need from the user

Run it as a short interview, a few questions at a time, rather than one long questionnaire. Start with:

- Team shape: who creates, who reviews, who publishes, who decides what gets made.
- Volume and mix: roughly what gets produced per month and in which formats.
- The complaint: what made them ask. In their words.
- Tools: where requests, drafts, reviews and published content live.

Then work through the stages using the questions in `references/maturity-model.md`. Skip stages that clearly don't apply. If the user has artifacts (a content calendar, a request form, a Slack review thread, analytics), ask for them. Artifacts beat descriptions.

## The eight stages

1. **Intake**: how requests arrive and get accepted or declined.
2. **Planning**: how priorities, calendars and briefs get set.
3. **Production**: how drafts get made.
4. **Review**: how drafts get approved by SMEs, legal, brand and leadership.
5. **Publishing**: how approved content goes live.
6. **Distribution**: how content reaches people after it's live.
7. **Measurement**: how the team knows what worked.
8. **Maintenance**: how existing content gets updated, merged or retired.

## How to score

Score each stage 1 to 5 using the level definitions in `references/maturity-model.md`. Score what actually happens, not what the process doc says. If people describe a process and then say "but usually we just...", score the "usually."

Then find the constraint. It's usually the lowest-scoring stage that sits upstream of the user's complaint. Explain the chain: how the constraint produces the symptom they reported.

## Output format

**The constraint**: one paragraph naming the stage that limits the engine and how it causes the problem the user came in with.

**Stage scores**

| Stage | Level (1–5) | Evidence | What's breaking |
|---|---|---|---|

**The chain**: a short trace from constraint to symptom. For example, "No intake owner → every request accepted → calendar is 3x capacity → reviews pile up → drafts age out → nothing ships on time."

**First three moves**: specific, small, doable in 30 days, aimed at the constraint. No tool purchases unless a tool is genuinely the fix.

**What not to fix yet**: stages that look bad but won't matter until the constraint moves. This saves teams from spreading effort across everything.

**Where AI helps and where it doesn't**: one or two lines. AI speeds up production. It doesn't fix missing ownership, broken review or no maintenance. Say plainly if the team is about to automate a broken stage.

## Rules

- One constraint. If you name four, you haven't found it.
- Score down when in doubt. A process that only works when one specific person is around is level 2, however good it looks.
- Don't recommend a maturity level the team can't sustain. Level 3 done consistently beats level 5 on paper.
- Keep the advice specific to what they told you. Generic best practices ("create a content calendar") only belong if the gap is genuinely that basic.
