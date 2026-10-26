# Forward-deployed AI skills

Six Claude skills for embedding with a sales team and building AI tools that actually stick. Each one maps to a responsibility in a forward-deployed AI role, and each one comes at it from the same place: most AI tooling fails because of the content and process underneath it, not the model on top.

| Skill | Job it does | Responsibility it covers |
|---|---|---|
| `workflow-debt-audit` | Finds high-leverage workflows by looking for undocumented process | Identify the highest-leverage workflows |
| `build-or-skip` | Readiness gates, verdicts and kill criteria for build requests | Prioritize what is and isn't worth building |
| `runbook-first` | One-page runbook written as part of every build | Make what you build understandable, documented and maintainable |
| `before-after-ledger` | Baseline capture and honest measurement | Measure effect with before-and-after evidence |
| `graduation-packet` | Handoff to engineering, analytics or ops | Partner when a tool needs production systems, sensitive data or long-term ownership |
| `results-readout` | Leadership brief plus a reusable pattern writeup | Share results with leadership and the wider team |

## How they chain

```
workflow-debt-audit → build-or-skip → (build) → runbook-first
                                              → before-after-ledger → results-readout
                                              → graduation-packet (when triggered)
```

Shipping fast and iterating with users happens between `build-or-skip` and the ledger. These skills don't slow that down; they make sure what ships quickly can still be trusted in six months.

## Install

Drop each folder into your skills directory, or upload the folder as a skill in Claude.

Built by Will Kelly. github.com/will-kelly
