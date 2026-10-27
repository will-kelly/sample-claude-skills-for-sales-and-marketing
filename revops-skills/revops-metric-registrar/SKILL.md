---
name: revops-metric-registrar
description: Builds and polices one source of truth for GTM metric definitions (MQL, SQL, pipeline, ARR, win rate). Use when numbers don't match across decks, dashboards, or teams.
---

# RevOps metric registrar

## What this is for

Half the arguments on a forecast call aren't about the number. They're about what the number means. Marketing's SQL isn't sales's SQL. Finance's ARR leaves out things the board deck counts. Somebody settled it in a Slack thread eighteen months ago and nobody wrote it down.

That's documentation debt with a revenue line attached. This skill pays it down in two modes:

- **Register:** turn scattered definitions into canonical registry entries.
- **Police:** check a deck, dashboard spec, report, or thread against the registry and flag drift.

## Inputs

Any mix of board or QBR decks, dashboard and report definitions, CRM field documentation, ops wiki pages, comp plans, and Slack threads where someone asked "wait, how do we count this?" Plus the existing registry, if there is one.

If there's no registry and no written definitions, say so up front. That is the first finding. Don't backfill from industry convention, because "the standard definition of SQL" is exactly the kind of thing people argue about.

## Register mode

For each metric you find, build an entry:

- **Name and aliases** (pipeline, open pipe, qualified pipe, and so on)
- **Definition as written**, quoted, with the source it came from
- **Formula and rules:** what's in, what's out, time window, currency, dedupe logic
- **System of record:** platform and field names, only if a source names them
- **Owner:** the person who settles disputes, only if a source names one
- **Consumers:** teams, reports, dashboards, and comp plans that use it
- **Conflicts:** every competing definition, side by side, each with its source
- **Status:** Canonical (one live definition, named owner), Contested (two or more live definitions), or Orphaned (used everywhere, defined nowhere)

## Police mode

Read the target document. For every metric it references:

1. Match it to a registry entry, including aliases.
2. Check whether the usage fits the canonical definition: same window, same inclusions, same source.
3. Flag drift with the exact line from the target and the registry rule it breaks.
4. Flag any metric the registry doesn't have. That's a new orphan.

## Routing

Every finding lands in one of three buckets:

- **Answer:** the definition is canonical and the source supports it.
- **Escalate:** the metric is contested and touches comp, the forecast, or board reporting. Send the side-by-side to the named owner, or to the RevOps lead if there's no owner.
- **Flag gap:** orphaned metric or missing owner. Log it as a debt item.

## Guardrails

- Never pick a winner between conflicting definitions. Show the conflict and name who should decide.
- If you can only see a dashboard's output and not its logic, mark the formula unverified. Don't reverse-engineer it.
- Anything comp-adjacent always escalates, no matter how small the drift looks.
- Call something a pattern only after three or more instances. One mismatched deck is an incident. Three is a process problem.

## Output

1. Registry entries in a consistent block format, ready to paste into a wiki or Notion database.
2. Drift report table: metric, where it appeared, what it said, what the registry says, routing.
3. Debt list ranked by blast radius: comp plans first, then board reporting, forecast, ops dashboards, everything else.

## The failure mode this prevents

Definition creep. A metric quietly changes meaning over a few quarters, the trend line breaks, and leadership makes a call off a chart that's comparing two different things.
