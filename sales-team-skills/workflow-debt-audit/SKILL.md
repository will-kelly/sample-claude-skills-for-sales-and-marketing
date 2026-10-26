---
name: workflow-debt-audit
description: Find the highest-leverage workflows in a sales or GTM team by treating undocumented process as debt. Use when scoping where AI tools should go, before anything gets built.
---

# Workflow debt audit

Most teams can tell you what they do. Very few can tell you how, and the gap between those two answers is where the leverage lives. This skill finds the workflows worth automating by looking for documentation debt: process that exists only in people's heads, Slack threads, personal templates and "ask Dana, she knows."

The premise: the workflows that hurt most aren't the slowest ones. They're the ones nobody wrote down, so every rep reinvents them, every new hire relearns them, and every AI tool pointed at them inherits the mess.

## When to use

- Starting with a new team (sales development, account management, solutions) and deciding where to look first
- A leader says "we should use AI for X" and you need to know whether X is real
- Before any build, to get inputs and outputs on paper

## What to collect

Ask for, or go find, these for each candidate workflow:

1. **Trigger.** What starts it? A new lead, a meeting booked, a quarter ending.
2. **Inputs.** Every source the person touches: CRM fields, enrichment tools, call notes, account plans, old emails, the spreadsheet only they use.
3. **Output.** What leaves their hands, and who consumes it next.
4. **Shadow docs.** The unofficial stuff: saved snippets, personal prompt libraries, bookmarked Slack threads, a Google Doc called "my process." These are the real spec.
5. **Variance.** Do three reps do this the same way? Ask three and compare.
6. **Re-explanation tax.** How often does someone have to explain this to someone else? Onboarding, handoffs, managers asking "where's that at?"

## How to score

Score each workflow 1 to 5 on five factors, then multiply frequency by the sum of the rest. Show the math, don't hide it.

| Factor | What a 5 looks like |
|---|---|
| Frequency | Daily, per rep |
| Time per instance | 20+ minutes of manual assembly |
| Variance across reps | Every rep does it differently and quality swings |
| Knowledge concentration | One or two people actually know how to do it well |
| Input stability | Inputs live in systems, not in people's memories |

Input stability cuts the other way from the others on purpose. A high-pain workflow with unstable inputs is a content problem first and a build second. Flag it, don't drop it.

## Output

A workflow ledger, one row per workflow:

- Workflow name in the team's own words (not yours)
- Trigger → inputs → output, one line
- Shadow docs found
- Score and the reasoning behind it
- Debt type: undocumented, contradictory, scattered, or stale
- Recommended next move: hand to `build-or-skip`, fix the source content first, or leave alone

End with the top three, in plain language, and the one question you still couldn't answer for each.

## Rules

- Use the team's vocabulary. If they call it "the prep doc," so do you.
- Sit with the work. A process interview is a hypothesis; watching someone do it is evidence. Mark which rows came from which.
- Don't recommend a build in this skill. The audit's job is to see clearly. Deciding is the next step.
- If every workflow scores high, the scoring is wrong or the team has a bigger problem than tooling. Say so.
