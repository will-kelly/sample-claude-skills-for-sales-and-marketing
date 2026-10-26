---
name: competitive-battlecard
description: Researches a competitor and builds a sales battlecard for a B2B tech company — quick positioning, where we win and lose, landmine questions, objection handling, proof points, and pricing/packaging notes — with every competitor claim sourced and dated. Use whenever someone asks for a battlecard, competitive intel, "how do we beat X", competitor comparison, a kill sheet, a competitive one-pager, objection handling against a named vendor, or is prepping sales for a deal against a specific competitor.
---

# Competitive battlecard

A battlecard is a tool a rep glances at in the five minutes before a call, or mid-call when a prospect says "but Competitor X does that too." It has to be fast to scan, honest enough that reps trust it, and current enough that it doesn't embarrass them.

## The two rules that make battlecards trustworthy

**1. Every claim about a competitor carries a source and a date.** Competitor pricing, features, and packaging change constantly. A rep who repeats a stale claim to a prospect who knows better loses credibility for the whole deal. So each competitive claim is tagged:

- `[Source: competitor pricing page, checked 2026-10-26]`
- `[Source: G2 reviews, pattern across 6+ reviews]`
- `[Source: sales team, unverified]` — allowed, but visibly marked

**2. Say where the competitor genuinely wins.** A battlecard that claims we win everywhere gets ignored after the first deal it fails in. Reps need to know when to reframe the conversation, and when to walk away from a deal that's a bad fit.

## Inputs

- Our product: what it does, positioning, key differentiators (use a positioning framework if the team has one)
- The competitor's name
- Any internal intel: win/loss notes, call recordings, CRM loss reasons, things reps hear

## Workflow

### 1. Research the competitor

If web search is available, research these in order and record the source and date for each:

1. Their homepage and product pages — how they position themselves, who they target
2. Pricing and packaging page
3. Docs — what the product actually does, integrations, deployment options, limits
4. Recent changelog or release notes, press releases, funding or acquisition news (last 6–12 months)
5. Review sites (G2, Gartner Peer Insights, TrustRadius) — look for *patterns* in complaints and praise, not single reviews
6. Community signals: GitHub activity for open-source competitors, Reddit and Hacker News discussions

If search isn't available, build from what the person provides and clearly mark the card as "needs external verification."

Don't use leaked documents, scraped gated content, or anything obtained by pretending to be a prospect. It's a legal and reputational risk, and reps shouldn't be carrying it.

### 2. Analyze

Compare across the dimensions that come up in technical deals: core capabilities, deployment model (SaaS/self-hosted/air-gapped), integrations and ecosystem, security and compliance (SOC 2, FedRAMP, data residency), pricing model and how it scales, ease of adoption, support, company stability and direction.

For each, decide: we win clearly / roughly even / they win. Be honest.

### 3. Build the card

Use the structure in `references/battlecard-template.md`. Keep it to what fits on two screens. Detail goes in an appendix, not the main card.

### Landmine questions

These are discovery questions a rep asks that naturally surface a competitor's weakness without bad-mouthing them. Good landmines are genuine questions a careful buyer *should* ask. For example: "How will you handle pipeline secrets when you move to multi-cloud?" — rather than "Did you know Competitor X stores secrets in plaintext?" Read `references/landmine-guide.md` for how to write them.

## Tone

Factual and respectful about competitors. Reps get forwarded, screenshotted, and quoted. Nothing in the card should embarrass the company if a competitor or prospect read it. No mocking, no speculation about the competitor's finances or people stated as fact.

## Output

The battlecard, plus a short "Refresh notes" section listing claims most likely to go stale (pricing, recent releases) and a suggested review date (default: 90 days).
