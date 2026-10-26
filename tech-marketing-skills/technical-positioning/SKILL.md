---
name: technical-positioning
description: Builds a positioning and messaging framework for a B2B technology product — category, competitive alternatives, differentiated value, proof, and per-persona messaging for technical and economic buyers (developers, platform/DevOps, security, IT ops, CIO/CFO). Use whenever someone asks for positioning, a messaging house, a messaging framework, value props, a positioning statement, persona messaging, "how do we talk about this product", or is repositioning a SaaS, devtools, cloud, security, data, or AI product, even if they never say the word "positioning".
---

# Technical positioning

Turn what a product team knows about their product into a positioning and messaging framework a tech marketing team can actually write from. The output has to survive two readers: the engineer who will smell vague claims instantly, and the budget holder who needs to know why this beats doing nothing.

## Why this skill exists

Most positioning docs for technical products fail in one of two ways. They're written for analysts ("AI-powered unified platform for modern teams") and say nothing a buyer can test, or they're feature lists with a tagline bolted on. This skill forces the work in the right order: who you're actually up against, what you do that they don't, why that matters to a specific person, and what proves it.

## Inputs to gather

Work from whatever the person provides: product docs, a PRD, a website URL, sales call notes, win/loss notes, a competitor list. If key inputs are missing, ask for them in one short batch rather than one at a time. The essentials:

1. What the product does, in plain terms, and how it's deployed or bought (SaaS, self-hosted, open core, marketplace, usage-based)
2. Who buys it and who uses it (often different people)
3. What customers would do if the product didn't exist — the real competitive alternatives, including "build it in-house," "keep the spreadsheet," and "use the feature our cloud provider bundles"
4. Any proof on hand: customer results, benchmarks, certifications, adoption numbers

If the person can't supply proof, proceed anyway — but mark every unsupported claim (see "Claims discipline" below). Don't stall the whole framework waiting on numbers.

## Workflow

### 1. Name the competitive alternatives first

Before writing a single value prop, list what the buyer would actually do instead. For tech products these usually fall into four buckets:

- **Direct competitors** — named vendors in the same category
- **Platform-bundled features** — what AWS, Azure, GCP, Microsoft 365, GitHub, Datadog, etc. already give them "for free"
- **Build it yourself** — scripts, open-source tools glued together, an internal platform team
- **Do nothing** — tolerate the pain, live with the manual process

The bundled-feature and build-it-yourself alternatives are where tech marketing most often loses deals without noticing. Always address them.

### 2. Find the differentiated capabilities

For each capability the product has, ask: do the alternatives also have this? Keep only what's actually different or meaningfully better. Parity features belong in a sales FAQ, not in positioning.

### 3. Translate capabilities into value, per persona

Use the chain **capability → what it lets you do → why that matters to this person**. Stop at the level that persona cares about. A developer cares that tests run in 40 seconds instead of 12 minutes. A VP of engineering cares about deploy frequency. A CFO cares about the headcount you didn't have to add. Same capability, three different endpoints.

Read `references/tech-personas.md` for what each common technical persona is measured on, what they distrust, and the words that land or backfire with them. Pick the 3–4 personas that matter for this product; don't write for all of them.

### 4. Pick the category frame

Decide whether the product competes in an existing category, a subcategory of one, or is genuinely creating a new one. Default to an existing or sub-category — category creation is expensive and most products don't need it. Explain the choice in one or two sentences.

### 5. Attach proof to every claim

Each value statement gets a proof point or an explicit gap. Acceptable proof for technical buyers, roughly in order of credibility: public benchmarks with methodology, customer results with a named or describable customer, third-party validation (analysts, certifications like SOC 2 or FedRAMP, CNCF graduation), open-source adoption signals, then internal data.

### 6. Write the framework

Use the structure in `references/framework-template.md`. Keep the whole thing scannable — a marketing team should be able to pull a headline, a persona value prop, or a proof point without reading it end to end.

## Claims discipline

Never invent numbers, customer names, benchmarks, or certifications. When a claim needs proof that wasn't provided, write the claim and flag it inline:

`[PROOF NEEDED: customer metric showing reduced MTTR]`

When a claim is directional (the person said "it's way faster" without data), soften the language to what's supportable and flag it:

`Cuts build times significantly [PROOF NEEDED: benchmark vs. GitHub Actions default runners]`

This matters because positioning docs get copied into web pages and sales decks. An invented number in a framework becomes a liability on a landing page three months later.

## Language rules

Technical buyers punish fluff. In every message:

- Prefer verbs and specifics over adjectives ("ships policies as code" beats "powerful policy management")
- Avoid the dead words: seamless, robust, cutting-edge, next-generation, revolutionary, best-in-class, leverage, unlock, empower, game-changing, single pane of glass
- Say "AI" only when you can say what the model actually does in the workflow
- Name the integration, the standard, or the protocol instead of "integrates with your stack"

## Output

Deliver the framework as a document the team will keep and edit. End with a short "Open questions" list covering the proof gaps and any assumptions you made about personas or competitors, so the team knows exactly what to go validate.
