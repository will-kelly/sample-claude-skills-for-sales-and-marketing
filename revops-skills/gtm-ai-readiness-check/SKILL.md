---
name: gtm-ai-readiness-check
description: Assesses whether a revenue team's data, definitions, and documentation can actually support the AI tools they want to buy or roll out (forecasting AI, sales copilots, agentic SDRs, conversation intelligence). Use before a vendor eval, a pilot, or when a rollout is underperforming and everyone is blaming the model.
---

# GTM AI readiness check

## What this is for

Every revenue tool now has an AI story. Forecasting that predicts the quarter. Copilots that draft the follow-up. Agents that work the top of the funnel. The demos look great because the demo org has clean data, tight definitions, and documentation that matches reality.

Your org probably doesn't. The AI will find that out in production, at the field's expense. This check finds it out first, so the conversation with the vendor and with the CRO starts from what's true.

This is not a vendor comparison and it never recommends a product. It assesses the ground the product would stand on.

## Inputs

- **The use case:** what the team wants AI to do, in their words. "Predict slip risk." "Draft follow-ups after discovery calls." "Qualify inbound." Be specific; readiness is per use case, not per company.
- **The data it would need:** field lists, fill rates, a sample export, data dictionary if one exists
- **The definitions it would rely on:** stage criteria, lead and opportunity definitions, metric definitions
- **The documentation it would retrieve from:** playbooks, product docs, pricing and packaging, competitive material, call notes
- **Optionally:** the vendor's stated data requirements, so you can check them against reality

## The process

### 1. Translate the use case into dependencies

For the stated use case, list what the AI needs to be true to work. Slip-risk prediction needs reliable close dates, honest stage history, and activity capture. A follow-up copilot needs accurate call notes, current product messaging, and current pricing. An agentic SDR needs a defined ICP, approved messaging, and clean routing rules.

### 2. Check each dependency on four dimensions

- **Data:** does the field exist, is it filled, is it filled honestly? A close date field that's 98 percent populated and moved by reps every Friday is not a reliable input.
- **Definitions:** is there one agreed meaning? If marketing and sales disagree on what an SQL is, an AI trained or prompted on "SQL" inherits the argument.
- **Documentation:** is the content the AI would retrieve from current, owned, and consistent? Retrieval over stale docs produces confident, wrong answers with a citation attached.
- **Ownership:** when the AI gets something wrong, is there a named person who fixes the underlying source, or does the field just stop using the tool?

Rate each dependency: Ready, Fixable before pilot, or Blocking.

### 3. Call the readiness level for this use case

- **Go:** dependencies are ready or fixable in the pilot window.
- **Go narrow:** a smaller version of the use case is viable now. Name it.
- **Not yet:** blocking dependencies exist. Name them and the work to clear them.

Pick one. Don't hedge into a non-answer.

## Routing

- **Answer:** dependency is ready, with evidence.
- **Escalate:** a blocking dependency the sponsor doesn't seem to know about, especially if a contract is close to signing.
- **Flag gap:** dependencies that can't be assessed because the data, docs, or definitions weren't provided. Say what's missing.

## Guardrails

- Never recommend a vendor or rank vendors. Assess the org, not the market.
- Don't take vendor claims about data requirements at face value. Check them against what the use case actually needs.
- Fill rate is not data quality. Always ask how the field gets filled and by whom.
- Be honest about "Not yet." A readiness check that always says Go is just a sales deck with extra steps.

## Output

1. The call: Go, Go narrow, or Not yet, with a two-sentence reason a CRO can read in a hallway.
2. Dependency table: dependency, dimension, rating, evidence, fix.
3. The pre-pilot work list, ordered by what unblocks the most.
4. Questions to put to the vendor, built from the gaps you found.
5. What success looks like in the pilot, in terms the field would recognize.

## The failure mode this prevents

Buying the demo. An AI rollout that fails on bad inputs, gets blamed on the model, and makes the next AI initiative twice as hard to fund.
