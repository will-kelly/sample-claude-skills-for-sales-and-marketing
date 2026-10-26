---
name: ops-scorecard
description: Builds an operational scorecard for a content team, with metrics for how the engine runs (cycle time, review wait, plan versus shipped, reuse, refresh rate, sales usage) alongside the performance metrics most teams already report, plus how to collect each one with the tools they have. Use when a content lead needs to show the team's efficiency, justify headcount or tools, report beyond pageviews, or set baselines before changing a process.
---

# Ops scorecard

Content teams usually report on what content did: traffic, downloads, engagement. Almost none report on how the team works. So when a leader asks "why can't you produce more?" or "would AI help?", there's no data, just opinions. And when the team fixes a process, nobody can prove it got better.

This skill builds the missing half of the report: a small set of operational metrics, defined precisely, with a realistic way to collect each one.

## What you need from the user

- Team size and roles.
- Where work is tracked (project tool, spreadsheet, Slack, nothing).
- What they report today and to whom.
- What question leadership keeps asking. The scorecard should answer it.
- What they're about to change, if anything (new tool, AI pipeline, new review process). That changes which baselines matter most.

## The metric menu

Pick five to seven. More than that and nobody reads it.

**Flow**
- **Cycle time**: brief approved to published, median, by content type.
- **Review wait**: time drafts spend waiting for review, as a share of cycle time.
- **Plan versus shipped**: share of planned pieces published in the planned month.
- **Work in progress**: pieces started but not shipped. High WIP means slow everything.

**Demand**
- **Request volume and acceptance rate**: how many requests, and what share got a yes.
- **Unplanned work share**: share of output that wasn't on the plan at the start of the month.

**Leverage**
- **Reuse rate**: assets derived from each major piece (posts, emails, sales snippets).
- **Sales usage**: share of sales-enablement content actually used in deals, from the CRM or enablement tool.

**Health**
- **Refresh rate**: share of top-traffic content updated in the last 12 months.
- **Content debt**: number of pages flagged outdated or inaccurate, trending down or up.

**Performance** (keep whatever they already report, and connect it): pipeline influenced, conversions and organic traffic.

## How to run it

1. Pick the metrics that answer leadership's question and set baselines for any planned change.
2. **Define each one precisely**: the start event, the end event, what counts and what doesn't. Vague definitions produce arguments, not insight.
3. **Plan collection with existing tools.** For each metric: where the data lives, who records it, how often, and how much manual effort it takes. If a metric needs a new tool, mark it as phase two.
4. **Set targets carefully.** Start with baselines. Set targets after two or three months of data, not on day one.

## Output format

**Scorecard**

| Metric | Definition | Data source | Collected by | Frequency | Baseline | Target |
|---|---|---|---|---|---|---|

Leave Baseline and Target as "measure first" unless the user provided data.

**Why these metrics**: two or three sentences tying the set to leadership's question.

**Tracking setup**: the specific changes needed in their tools (status fields to add, dates to capture, a tag for unplanned work), written as a short checklist.

**Monthly report template**: a one-page layout, with the operational metrics next to the performance metrics and a short "what we changed and what happened" section.

If the user wants it, build the scorecard as a working spreadsheet with formulas.

## Rules

- Never track individual writer output as a performance metric. It optimizes for volume and kills quality. Team-level flow only.
- Every metric needs an owner and a source, or it'll be reported once and abandoned.
- Don't let operational metrics replace business outcomes. They explain the outcomes; they don't stand in for them.
