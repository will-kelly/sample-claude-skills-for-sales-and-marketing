---
name: revops-runbook-debt-audit
description: Audits a RevOps team's process documentation (playbooks, SOPs, field guides, wiki pages) for staleness, contradictions, and single points of failure. Use when a RevOps lead inherits a team, before a systems migration, or when the field keeps asking questions the docs supposedly answer.
---

# RevOps runbook debt audit

## What this is for

RevOps runs on process, and process runs on documentation that nobody budgets time to maintain. The territory rules page was right two reorgs ago. The deal desk SOP references an approval step that got cut. The person who knew how renewals really get booked left in the spring, and the wiki page still has their name as owner.

That's documentation debt, and in RevOps it compounds faster than almost anywhere, because every doc is load-bearing for someone's quota. This audit finds the debt, prices it, and tells you what to pay down first.

## Inputs

- The documentation itself: Confluence, SharePoint, Notion, Google Drive, the team's Slack canvases, whatever they use
- Page metadata where available: last edited, author, owner, view counts
- Optionally: recent field questions (Slack channel, ticket queue, enablement office hours) so you can see where docs are failing in practice
- Optionally: the list of recent changes (comp plan, territory, stage definitions, tools) so you know what docs should have been updated

## The process

### 1. Inventory

List every process doc in scope with its owner, last edit date, and the process it covers. Group by process area: lead management, opportunity management, forecasting, deal desk and approvals, quoting and contracts, territory and routing, comp and crediting, renewals and expansion, systems and tooling.

### 2. Score each doc on five debt signals

- **Stale:** last edit predates a known change to the process it covers.
- **Contradicted:** another doc, a recent announcement, or the system configuration says something different.
- **Orphaned:** no owner, or the owner has left or changed roles.
- **Shadowed:** the field asks questions in Slack that this doc should answer, which means people have stopped trusting it or can't find it.
- **Single-threaded:** the process depends on knowledge that exists in one person's head and nowhere in writing.

### 3. Price the debt

Rank by blast radius, not by how bad the doc looks. A sloppy but accurate page about Slack etiquette is cheap debt. A clean-looking but wrong page about discount approval thresholds is expensive. Order of cost, highest first: comp and crediting, deal desk and approvals, forecasting, territory and routing, everything else.

### 4. Find the patterns

Three or more docs with the same problem is a process failure, not a doc failure. "Every page touched by the Q2 territory change is stale" means changes ship without a doc update step. Name that, because fixing pages one at a time won't fix it.

## Routing

- **Answer:** the doc is current, owned, and consistent.
- **Escalate:** wrong or contradicted docs in comp, approvals, or forecasting. These go to the RevOps lead now, not in the quarterly cleanup.
- **Flag gap:** orphaned, shadowed, and single-threaded processes. These become the paydown backlog.

## Guardrails

- Don't rewrite docs in this skill. Audit first. Mixing the two hides the findings inside edits.
- Don't decide which of two contradicting docs is right. Show both and name who should decide.
- An old edit date isn't debt by itself. Some processes don't change. Stale only counts when you can point to the change the doc missed.
- If you can't see the system configuration, say so. A doc can match every other doc and still be wrong about how the CRM actually behaves.

## Output

1. Headline: total docs audited, how many carry high-cost debt, and the single most dangerous one.
2. Debt register: doc, process area, signals present, cost tier, owner, routing.
3. Patterns (three-plus instances), each tied to the upstream process that's causing them.
4. A 30-day paydown plan: the five fixes that remove the most risk, and the one process change that stops new debt from piling up.

## The failure mode this prevents

Confidently wrong documentation. Worse than no docs, because people follow it.
