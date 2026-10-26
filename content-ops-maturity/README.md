# Content ops maturity skills for B2B marketing teams

Seven Claude skills that find where a content engine actually breaks, and fix that first.

Built by [Will Kelly](https://github.com/will-kelly).

> **About this repo**: these are portfolio work samples. They show how I approach content operations and how I'd turn that approach into working AI tooling for a marketing team. They work if you install them, but they aren't a maintained product.

## Why these exist

When content isn't working, teams fix the stage they can see. Writers seem slow, so they hire freelancers. Output seems low, so they buy an AI writing tool. Traffic is dropping, so they publish more. And nothing changes, because the real problem was somewhere else: nobody owned intake, review took three weeks, or nothing published in the last three years had ever been updated.

I've spent years inside enterprise content operations: documentation, marketing, enablement, governance across SharePoint, Confluence and Notion. The pattern holds almost everywhere. A content engine runs at the speed of its weakest stage, and adding power anywhere else just builds a bigger queue in front of the constraint.

That matters more now, because a lot of teams are adding AI to their content workflow. AI makes drafting faster. If review, intake or maintenance is broken, faster drafting gives the broken stage more work to choke on.

These skills diagnose first, then fix the specific stage that's breaking.

## The skills

| Skill | What it does | Use it when |
|---|---|---|
| [content-engine-diagnostic](content-engine-diagnostic/) | Scores eight stages on a five-level maturity model and names the one constraint holding the engine back | Content feels slow or ineffective and nobody agrees why |
| [request-intake-triage](request-intake-triage/) | Sets up intake and scores incoming requests, with a brief for every yes and a redirect for every no | The team is drowning in ad hoc requests |
| [review-bottleneck-mapper](review-bottleneck-mapper/) | Maps the approval chain, separates working time from waiting time, and redesigns review with tiers, scopes and windows | Drafts sit in review for weeks |
| [content-inventory-audit](content-inventory-audit/) | Sorts every page into keep, update, merge or retire from sitemap, CMS and analytics exports | Traffic is declining, or a migration is coming |
| [docs-marketing-drift-check](docs-marketing-drift-check/) | Flags where marketing claims contradict docs, release notes and pricing | After a release, rebrand, or "sales says the site is wrong" |
| [ai-pipeline-blueprint](ai-pipeline-blueprint/) | Designs an AI-assisted pipeline for one content type, with clear AI, assisted and human-only stages and quality gates | The team wants to use AI without losing quality |
| [ops-scorecard](ops-scorecard/) | Builds operational metrics (cycle time, review wait, plan versus shipped, refresh rate) and how to collect them | Leadership asks why the team can't produce more |

## Where to start

Start with **content-engine-diagnostic**. It names the constraint and points to the skill that addresses it:

- Intake is the constraint → **request-intake-triage**
- Review is the constraint → **review-bottleneck-mapper**
- Maintenance is the constraint → **content-inventory-audit**, then **docs-marketing-drift-check**
- Production is genuinely the constraint, and the rest is healthy → **ai-pipeline-blueprint**
- Measurement is the constraint, or you need proof that a fix worked → **ops-scorecard**

Set a baseline with **ops-scorecard** before you change anything. It's the only way to show that the fix worked.

## Design choices worth noting

A few decisions run through the whole set, and they're the part I'd point a hiring manager to:

- **One constraint, not a list.** The diagnostic is built to name a single bottleneck and say what not to fix yet. Teams that try to fix every stage at once usually fix none of them.
- **Score what happens, not what the process doc says.** The maturity model scores the "usually we just..." version of a process, and anything that depends on one person is capped at level 2.
- **Process before tools, process before AI.** No skill recommends a purchase when the real gap is ownership or process, and the AI pipeline skill checks intake and review health before designing anything.
- **AI stays out of judgment calls.** In the pipeline blueprint, AI never decides what the company claims, believes or quotes. Those stages are human-only by design.
- **Every no comes with a redirect.** Intake triage won't decline a request without offering something smaller or existing, because a bare no teaches people to route around the process.
- **Team metrics only.** The scorecard never tracks individual writer output, because that optimizes for volume and quietly kills quality.
- **Unknown stays unknown.** Missing data shows up as "unknown" or "measure first," not as a confident-sounding estimate.

## Structure

```
content-engine-diagnostic/
  SKILL.md
  references/maturity-model.md
request-intake-triage/SKILL.md
review-bottleneck-mapper/SKILL.md
content-inventory-audit/SKILL.md
docs-marketing-drift-check/SKILL.md
ai-pipeline-blueprint/SKILL.md
ops-scorecard/SKILL.md
dist/          one zip per skill
```

## Companion set

These pair with the [anti-vendor-theater skills](https://github.com/will-kelly), another sample set focused on what the content says. This set handles how it gets made. The two connect in a couple of places: **docs-marketing-drift-check** feeds the claims-ladder, and **ai-pipeline-blueprint** can use theater-detector as one of its quality gates.

## Try them yourself

The skills run as-is in Claude.

- **Claude apps**: upload any zip from `dist/` as a custom skill in your Claude settings (skills need to be enabled for your account or organization).
- **Claude Code**: copy the skill folders into `~/.claude/skills/`.

Then ask in plain language, such as "why is our content so slow?" or "help me audit our blog," and the right skill loads.
