# Tech marketing skills for Claude

Six Claude skills for a B2B technology marketing team. Each one packages a workflow a product marketing or content team runs every month — positioning, launches, competitive intel, thought leadership, customer proof, and copy review — into instructions Claude follows the same way every time.

Built by Will Kelly, content and AI workflow strategist.

## The skills

| Skill | What it does | Typical input | Output |
|---|---|---|---|
| [technical-positioning](technical-positioning/) | Positioning and messaging framework for technical and economic buyers | Product docs, PRD, sales notes | Framework with alternatives, value pillars, persona messaging, proof gaps |
| [launch-kit-builder](launch-kit-builder/) | Sizes a release and builds the launch assets that tier deserves | Release notes, changelog, PRD | Tier call, blog, email, social, sales one-pager, FAQ |
| [competitive-battlecard](competitive-battlecard/) | Sourced, dated sales battlecard against a named competitor | Competitor name, win/loss notes | Two-screen battlecard with landmines and objection handling |
| [sme-thought-leadership](sme-thought-leadership/) | Turns an engineer's knowledge into a bylined article in their voice | Transcript, call notes, or nothing (interview guide) | Draft, headlines, accuracy review table, editor pitch |
| [customer-proof-story](customer-proof-story/) | Case study and proof assets with traceable metrics | Customer interview or CSM notes | Case study, snippet, quotes, sales summary, approval package |
| [technical-buyer-review](technical-buyer-review/) | Reviews copy the way a skeptical engineer reads it | Any marketing copy | Scored review with line-level rewrites |

## What they have in common

**Nothing invented.** Every skill refuses to make up metrics, customer names, quotes, benchmarks, or certifications. Gaps get explicit placeholders like `[PROOF NEEDED: ...]` so the team knows exactly what to go get. In tech marketing an invented number in a draft becomes a liability on a landing page later.

**Written for technical buyers.** Developers, SREs, security engineers, and IT architects punish fluff. The skills push toward specifics: integrations, standards, workflows, code, real numbers with methods.

**Built for review, not just generation.** Each skill ends with what a human needs to check — open questions, an accuracy table for the SME, an approval package for the customer, a confirm-before-publishing list. That's where AI-assisted marketing usually breaks down, so the skills make it the easy part.

**Tested.** Each skill ships with test cases in `evals/` (the format `claude plugin eval` reads), covering a normal run and an edge case such as missing proof or no source material.

## How they fit together

```
technical-positioning ──► launch-kit-builder ──► technical-buyer-review
        │                         ▲                       ▲
        ▼                         │                       │
competitive-battlecard    customer-proof-story    sme-thought-leadership
```

The positioning framework is the source of truth the other skills align to. Customer stories feed proof into launches and battlecards. Everything customer-facing can pass through the technical buyer review before it ships.

## Sample outputs

Real runs of two skills against their test prompts, unedited:

- [examples/launch-kit-builder-sample.md](examples/launch-kit-builder-sample.md): four lines of sprint release notes become a Tier 2 launch kit. The skill picks the headline feature, keeps the beta label consistent across every asset, and flags a default-version change as a customer heads-up rather than marketing.
- [examples/technical-buyer-review-sample.md](examples/technical-buyer-review-sample.md): a buzzword-heavy landing page scores 1.2 out of 5, with line-level rewrites that use placeholders instead of invented facts.

## Install

**Claude apps:** download the `.skill` file for any skill from `dist/` and upload it in the Skills section of Claude's settings.

**Claude Code:** copy a skill folder into `~/.claude/skills/` (personal) or `.claude/skills/` in a project.

## Structure

```
skill-name/
├── SKILL.md          # instructions and trigger description
├── references/       # templates and guides Claude loads when needed
├── scripts/          # deterministic helpers (technical-buyer-review only)
└── evals/            # test prompts and grading criteria
```

`examples/` holds sample outputs and `dist/` holds the packaged `.skill` files.

## Try it

- "Here are our release notes for this sprint — turn them into launch content."
- "Build a battlecard: us vs. Datadog for log management."
- "Review this landing page copy for a developer audience."
- "Our CTO wants to write about why platform teams fail. Where do we start?"
