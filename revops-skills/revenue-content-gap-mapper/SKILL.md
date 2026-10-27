---
name: revenue-content-gap-mapper
description: Connects sales content gaps to where deals actually stall, using pipeline data, loss reasons, and field requests. Use when enablement or product marketing needs to justify what to build next, or when RevOps asks why content isn't moving the pipeline.
---

# Revenue content gap mapper

## What this is for

Content teams usually prioritize by who asked loudest. RevOps sees where deals die but doesn't own the content that might have saved them. The two rarely sit in the same room with the same data.

This skill puts them in the same room. It maps where deals stall or lose, what the buyer or rep needed at that moment, and whether content for that moment exists, is findable, and is any good. The output is a content backlog ranked by pipeline exposure instead of by volume of Slack requests.

## Inputs

- **Pipeline movement:** stage conversion rates and time-in-stage, ideally by segment
- **Loss and slip reasons:** closed-lost reasons, slip notes, win/loss interview summaries
- **Field requests:** Slack asks, enablement tickets, "does anyone have a deck for..." messages
- **The content inventory:** what exists, where it lives, last updated, usage if tracked
- **Optionally:** call recordings or summaries where objections come up

## The process

### 1. Find the stall points

Use the pipeline data to find stages with the worst conversion or longest dwell time, by segment. These are the candidate moments where content might matter. Note where content plausibly can't help (budget freezes, a lost champion) and set those aside honestly.

### 2. Name the need at each stall point

For each stall point, pull from loss reasons, slip notes, and field requests to name what was needed. Be concrete: "a security questionnaire answer for FedRAMP-adjacent buyers," not "security content." Only treat a need as real if it shows up three or more times across sources.

### 3. Check the content against the need

For each need, classify:

- **Missing:** nothing exists.
- **Unfindable:** it exists, but the field keeps asking for it, which means they can't find it or don't know it's there.
- **Stale:** it exists and is findable but out of date with the product, pricing, or competitive situation.
- **Wrong shape:** it exists and is current, but it's a 30-slide deck when the moment needs a one-page answer a rep can forward.
- **Covered:** the content exists, works, and the gap is somewhere else.

"Covered" is a real finding. Say it plainly; it stops the team from building content to fix a non-content problem.

### 4. Size the exposure

For each gap, estimate pipeline exposure: deals at that stall point in the period, and their value. Use the team's own numbers. Don't project win-rate lift from fixing content; nobody can support that number, and it undermines everything else in the report.

## Routing

- **Answer:** the gap is real, sized, and the fix is clear.
- **Escalate:** a large exposure where the fix belongs to a team that isn't in the room (legal, security, product). Name the owner.
- **Flag gap:** a stall point where you can't tell what's needed because loss reasons are blank or useless. That's a data capture fix, and it goes on the list too.

## Guardrails

- Never claim content will lift win rates by a specific amount. Size the exposure, not the upside.
- A single loud request is not a gap. Three independent signals is the minimum.
- Don't recommend more content when the finding is "unfindable." The fix there is distribution and governance, not production.
- Name non-content problems as non-content problems.

## Output

1. Headline: the one gap with the most pipeline exposure, in a sentence.
2. Stall map: stage, segment, conversion or dwell problem, need, content status.
3. Ranked backlog: gap, classification, exposure, owner, smallest useful fix.
4. Non-content findings, kept separate so they don't get lost.
5. Data capture fixes that would make the next run of this map sharper.

## The failure mode this prevents

Content built for requests instead of revenue. A library that grows every quarter while the same deals stall at the same stage for the same reason.
