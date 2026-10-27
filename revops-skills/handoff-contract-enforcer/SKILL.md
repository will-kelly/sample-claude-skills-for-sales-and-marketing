---
name: handoff-contract-enforcer
description: Checks marketing-to-SDR, SDR-to-AE, and AE-to-CS handoffs against the written agreement for what each team owes the next. Use when leads are rejected, deals stall after handoff, or teams blame each other for pipeline quality.
---

# Handoff contract enforcer

## What this is for

Every GTM org has handoff rules. Marketing passes leads that meet a bar. SDRs book meetings with the right fields filled in. AEs hand closed deals to CS with the context needed to onboard. Those rules are usually written once, in a kickoff deck, and then live on as tribal knowledge while everyone quietly renegotiates them.

When the handoffs break, the arguments sound like "marketing leads are junk" or "sales never follows up." Both sides are usually half right, and neither has the receipts. This skill gets the receipts.

## Inputs

- **The contract:** whatever the teams agreed to. SLA docs, lead definitions, stage entry criteria, handoff checklists, CS onboarding requirements. If it exists only in a slide, that's fine. If it doesn't exist at all, see below.
- **The handoffs:** a sample or export of records at each transition, with the fields and notes that came across, plus timestamps.
- **The rejections:** recycled leads, rejected meetings, stalled onboarding, with reasons if anyone recorded them.

### If there is no contract

Don't write one from best practice and pretend it's theirs. Instead, reconstruct the implied contract from what each side actually rejects and accepts, label it clearly as reconstructed, and make "get both sides to sign this" the top recommendation. Half the value of this skill is surfacing that the contract was never agreed.

## The process

1. **Parse the contract into checkable obligations.** For each handoff, list what the sending team owes (fields, qualification criteria, context, timing) and what the receiving team owes back (response time, acceptance or rejection with reason, feedback).
2. **Check each sampled handoff against both sides.** The sender's obligations and the receiver's. Enforcement that only checks one direction is just picking a side.
3. **Classify each breach:**
   - **Sender miss:** the record didn't meet the bar when it was passed.
   - **Receiver miss:** the record met the bar, and the receiver didn't act within the SLA or rejected it without a valid reason.
   - **Contract ambiguity:** the rule is vague enough that both sides can claim they followed it. These are the most useful findings.
   - **Contract drift:** the rule as written and the rule as practiced have split. Name both.
4. **Measure the gap.** Breach rate per handoff, per direction, per rule.

## Routing

- **Answer:** the handoff met the contract on both sides.
- **Escalate:** a breach pattern (three or more instances) that touches pipeline the forecast depends on, or any breach that affects comp crediting.
- **Flag gap:** ambiguous or missing rules. These go to whoever owns the contract, with suggested wording marked as a suggestion.

## Guardrails

- Check both directions every time. If you only find sender misses, look harder at the receiver side before you report.
- Never name individual reps in the pattern view. Teams and stages, not people.
- Don't treat "rejected" as proof of a bad lead. A rejection without a recorded reason is itself a receiver miss.
- If the sample is small or obviously cherry-picked, say so in the first line of the output.

## Output

1. Headline: where the handoffs are actually breaking, in one or two sentences.
2. Contract as parsed (or as reconstructed, clearly labeled).
3. Breach table: handoff, rule, direction, count, rate, example record.
4. Ambiguities and drift, each with the current wording and a suggested rewrite.
5. A short note to both team leads that a reasonable person on either side could read without getting defensive.

## The failure mode this prevents

The blame loop. Marketing and sales spend a year arguing about lead quality, both with anecdotes, while the actual problem is a definition nobody wrote down.
