# RevOps skills

Six Claude skills for revenue operations, built around one idea: most RevOps problems that look like data or tooling problems are really documentation and definition problems wearing a costume.

Each skill is narrow on purpose, names the failure mode it prevents, and follows the same rules:

- **Cite or don't claim.** Every finding points back to a source record or document.
- **Three-way routing.** Every finding lands as answer, escalate, or flag gap.
- **Three instances before a pattern.** One bad record is an incident. Three is a process problem.
- **Never pick the winner.** When definitions or docs conflict, show both and name who decides.
- **Comp-adjacent always escalates.**

## The set

| Skill | Use it when | Failure mode it prevents |
|---|---|---|
| `revops-metric-registrar` | Numbers don't match across decks, dashboards, or teams | Definition creep |
| `forecast-narrative-auditor` | Before a forecast call, QBR, or board pre-read | Happy ears at scale |
| `handoff-contract-enforcer` | Marketing, SDR, AE, and CS are blaming each other for pipeline quality | The blame loop |
| `revops-runbook-debt-audit` | Inheriting a team, prepping a migration, or the field ignores the wiki | Confidently wrong documentation |
| `gtm-ai-readiness-check` | Before buying or piloting a revenue AI tool, or when one is underperforming | Buying the demo |
| `revenue-content-gap-mapper` | Enablement or PMM needs to justify what to build next | Content built for requests instead of revenue |

## How they fit together

The registrar is the foundation. The forecast auditor, handoff enforcer, and AI readiness check all get sharper when metric definitions are settled. The runbook debt audit and the content gap mapper are the documentation side of the same problem: one for the processes RevOps owns, one for the content the field sells with.

A sensible first run for a new team: runbook debt audit, then metric registrar, then whichever of the other four matches the loudest current pain.

## Installing

Each folder is a standalone skill. Upload a folder's zip in Claude's skill settings, or drop the folder into a project's `.claude/skills/` directory.

## Relationship to existing work

These are designed to sit alongside the deal desk precedent scribe, comp plan interpreter, pipeline-to-content converter, and Field Change Studio without overlapping them.
