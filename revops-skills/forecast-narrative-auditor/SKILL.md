---
name: forecast-narrative-auditor
description: Checks the story behind a commit or best-case call against the evidence in the CRM and deal notes. Use before a forecast call, QBR, or board pre-read when you need to know which deals are carried by narrative instead of activity.
---

# Forecast narrative auditor

## What this is for

Every forecast has two layers. There's the number, and there's the story a rep or manager tells to defend it. "Champion is bought in." "Legal is just a formality." "They told us we're the frontrunner." The number gets scrutiny. The story usually doesn't, because nobody has time to check twenty deal narratives against twenty activity histories before a Monday call.

This skill does that check. It doesn't predict whether deals close. It tells you which claims have evidence behind them and which ones are running on vibes.

## Inputs

- The forecast or commit list (deal, stage, amount, close date, category)
- The narrative for each deal: forecast notes, manager comments, call-prep docs, Slack updates
- The evidence: activity history, stage change dates, contacts engaged, meeting notes, mutual action plans, call summaries

If you get narrative with no evidence attached, say so and stop. An audit with one side missing is just a re-read.

## The process

### 1. Extract the claims

Pull every factual claim out of each deal's narrative. Rewrite each as something checkable:

- "Champion is bought in" becomes "a named champion has engaged in the last 14 days"
- "Legal is a formality" becomes "legal or procurement has the paper and has responded"
- "We're the frontrunner" becomes "the buyer said this, and it's documented somewhere"

### 2. Match claims to evidence

For each claim, look for support in the evidence. Grade it:

- **Supported:** a dated record backs it, and you can cite it.
- **Stale:** evidence exists but is older than the deal's sales cycle tolerance (default 21 days; use the team's number if they give one).
- **Unsupported:** nothing in the record backs it.
- **Contradicted:** the record says otherwise. A champion who left the company. A close date that has slipped three times. A buyer who went dark after pricing.

### 3. Score the deal, not the rep

Roll up to a deal-level read: how much of this deal's forecast category is resting on unsupported or contradicted claims. Keep it about the deal. This is not a rep scorecard, and you shouldn't build one even if asked inside this skill. That's a different conversation with different stakes.

### 4. Look for patterns, carefully

Only call a pattern after three or more deals show the same gap. "Three commit deals in this region have no economic buyer contact" is a pattern. One deal like that is a question for the deal review.

## Routing

- **Answer:** the narrative holds up. Say so briefly. People should hear when their homework checks out.
- **Escalate:** a commit or best-case deal with a contradicted claim, or with most of its narrative unsupported. These go to the forecast owner before the call, not during it.
- **Flag gap:** the claim might be true, but the evidence isn't recorded. That's a documentation problem as much as a forecast one, and it should be logged as such.

## Guardrails

- Never move a deal between forecast categories yourself. Recommend, cite, and let the owner decide.
- Never infer buyer intent from tone. "The email sounded positive" is not evidence.
- Don't invent thresholds. If the team has no stale-activity rule, use the default and say you used it.
- Quote the narrative exactly when you challenge it. People argue less with their own words.

## Output

1. One-line headline: how much of the commit is evidence-backed versus narrative-backed, in dollars and deal count.
2. Escalation list: deal, the claim, what the record actually shows, cited.
3. Deal-by-deal table: deal, category, amount, supported / stale / unsupported / contradicted counts, routing.
4. Patterns (three-plus instances only), each with the deals that make it up.
5. Documentation gaps: claims that are probably true but live only in someone's head.

## The failure mode this prevents

Happy ears at scale. A forecast that rolls up a dozen optimistic stories nobody checked, then misses by the exact amount everyone privately suspected.
