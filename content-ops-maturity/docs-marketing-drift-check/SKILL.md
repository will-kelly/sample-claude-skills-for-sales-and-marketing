---
name: docs-marketing-drift-check
description: Compares what marketing says about a product (web pages, decks, datasheets, battle cards) against what the documentation, release notes and pricing pages say, and flags every contradiction, outdated claim and feature that marketing describes but the docs don't support. Use after a release or rebrand, before a website refresh or sales kickoff, or when sales or support report that marketing content doesn't match the product.
---

# Docs and marketing drift check

Marketing content and product documentation are written by different teams on different schedules, and they drift apart. The website still lists an integration that was deprecated last spring. The datasheet says "unlimited" and the pricing page says 50. A deck describes a workflow the product hasn't supported since version 3. Technical buyers check the docs during evaluation. When the two don't match, they believe the docs, and they start wondering what else marketing got wrong.

This skill finds the drift before a buyer does.

## What you need from the user

- **Marketing sources**: the pages and assets to check. URLs, files or pasted text.
- **Source of truth**: product docs, release notes, changelogs, pricing pages, API references. Ask which wins when docs and release notes disagree. Usually it's the most recent release notes.
- Optional: a list of recent changes (deprecations, renames, pricing changes) to focus the check.

## How to run it

1. **Extract claims from the marketing sources.** Every statement about features, integrations, limits, platforms, pricing, certifications and product names. One claim per row.
2. **Check each claim against the source of truth.** Find the relevant passage and decide:
   - **Matches**: docs confirm it.
   - **Outdated**: was true, isn't now (renamed, deprecated, changed).
   - **Contradicts**: docs say something different.
   - **Overstated**: docs support a narrower version (a beta described as generally available, one cloud described as "any cloud").
   - **Unsupported**: docs say nothing about it. Could be fine, could be vapor. Needs a human answer.
3. **Rate the risk** of each mismatch:
   - **High**: pricing, limits, security or compliance claims, and anything a contract might rely on.
   - **Medium**: features and integrations a buyer would test.
   - **Low**: naming and terminology.
4. **Look the other way too.** Note significant capabilities in recent release notes that marketing doesn't mention at all. That's drift in the other direction, and it's free messaging.

## Output format

**Summary**: claims checked, how many in each status, and the number of high-risk mismatches.

**Mismatches**, high risk first:

| Asset | Marketing says (excerpt) | Docs say (excerpt) | Status | Risk | Fix |
|---|---|---|---|---|---|

**Unsupported claims**: a list to send to product management, written as questions.

**Shipped but not marketed**: capabilities the docs describe that marketing doesn't mention.

**Recurring causes**: if a pattern explains several mismatches (for example, a product rename never pushed to old pages), name it so the team can fix the process, not just the pages.

## Rules

- Quote short excerpts only, enough to locate the passage.
- The docs can be wrong too. If a docs passage looks outdated, flag it for the docs team rather than assuming marketing is the problem.
- "Unsupported" isn't "false." Don't tell the team to cut a claim just because docs are silent. Tell them to confirm it.
- Keep fixes concrete: the replacement wording, or the asset owner to contact.
