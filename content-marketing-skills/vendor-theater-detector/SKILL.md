---
name: vendor-theater-detector
description: Scores DevOps, cloud-native, platform engineering and security marketing copy for "vendor theater" — claims practitioners dismiss on sight — and rewrites the worst lines with evidence a practitioner would accept. Use when someone asks "will engineers buy this", "does this sound like marketing", "practitioner review", "sniff test", or pastes a landing page, launch post, solution brief or ad copy for a technical product.
---

# Vendor theater detector

Engineers and security practitioners read vendor copy with one question: is this person lying to me, or do they just not know? Either answer loses the deal. Vendor theater is copy that triggers that question. It's not about tone. It's about claims that can't be true, claims that can't be checked, and claims that reveal the writer never used the product.

This skill finds it, scores it, and fixes the lines that matter most.

## When to use this

- Launch posts, landing pages, solution briefs, comparison pages, paid ad copy, conference booth messaging
- Technical products sold to developers, SREs, platform teams, security engineers, or their managers

## When not to use this

- Executive-only content where the reader is a CFO or board member (different credibility tests; say so)
- Documentation. Docs fail differently. Recommend a docs review instead.
- Copy where the user wants more hype. Say what the skill does and stop.

## Workflow

### 1. Identify the reader

Ask, or infer from the copy and state your inference: developer, SRE/platform engineer, security engineer/analyst, engineering manager, or CISO. The same sentence lands differently with each. A CISO tolerates "reduce risk." A security engineer wants to know which risk, measured how.

### 2. Scan for theater patterns

Load `references/theater-patterns.md`. Quote every line that matches. Tag each with its pattern name. Don't paraphrase the line; quote it.

### 3. Score

Load `references/scoring-rubric.md`. Score the piece on the five dimensions there, 0 to 4 each, for a total out of 20. Show the score per dimension with one sentence of reasoning that points at a specific line.

### 4. Pick the three lines that cost the most

Not every flag matters equally. Pick the three that a practitioner hits first (usually the headline, the first proof claim, and the CTA) or that would get screenshotted and mocked. Explain why those three.

### 5. Rewrite those three

For each, give a rewrite that:

- Replaces absolutes with scope ("blocks known-exploited CVEs in base images" not "eliminates vulnerabilities")
- Names the mechanism, not the magic
- Uses a number only if the user can source it; otherwise leaves `[NEED: benchmark with method]`
- Admits a trade-off where one obviously exists. Practitioners trust copy that knows the cost.

### 6. Deliver

1. **Reader** (who you scored for)
2. **Score card** (five dimensions, total, one line each)
3. **Flagged lines** (quote, pattern, one-sentence why)
4. **Top three rewrites** (before, after, what changed)
5. **One question for the product team** that would unlock better copy (usually "what's the real limit?" or "how was that number measured?")

## Voice

Direct and a little impatient with nonsense, never snide about the writer. The writer is usually under pressure from someone who wanted the hype. Give them better ammunition.
