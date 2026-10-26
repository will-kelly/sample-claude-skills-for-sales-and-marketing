# Example: container security launch post intro

## Input

> Introducing [Product] 3.0, the AI-powered, cloud-native security platform that eliminates vulnerabilities across your entire software supply chain. With one click, [Product] gives you complete visibility and automatically remediates risks before they reach production. Leading enterprises have reduced risk by 90%.

**Reader inferred:** platform and security engineers evaluating container security tools.

## Score card (5/20 — start over from a user interview)

| Dimension | Score | Why |
|---|---|---|
| Claim honesty | 0 | "eliminates vulnerabilities" and "complete visibility" are both false on their face |
| Mechanism clarity | 1 | "AI-powered" with no verb; no idea whether this scans, gates, or runs at runtime |
| Proof quality | 1 | "reduced risk by 90%" is unsourced and "risk" is unmeasured |
| Reader fit | 2 | Right reader, but "leading enterprises" talks past engineers to their bosses |
| Trade-off honesty | 1 | "one click" and "automatically remediates" hide every setup and approval step |

## Flagged lines

- "eliminates vulnerabilities across your entire software supply chain" — *Absolutes.* Every reader can name a vulnerability no scanner catches.
- "AI-powered, cloud-native security platform" — *Buzzword stacking; magic without mechanism.*
- "With one click" — *One-click.* Implies no setup, no permissions, no integration.
- "complete visibility" — *Complete / total.*
- "automatically remediates risks before they reach production" — *Automatically doing hard things.* Engineers hear "changes my builds without asking."
- "reduced risk by 90%" — *Unsourced percentages.*

## Top three rewrites

**1. The headline claim**
Before: "eliminates vulnerabilities across your entire software supply chain"
After: "finds known vulnerabilities in your images and dependencies, and blocks the ones that matter from reaching production"
What changed: scoped to known vulnerabilities and to what the tool controls. "The ones that matter" sets up the prioritization story.

**2. The automation claim**
Before: "automatically remediates risks before they reach production"
After: "opens a pull request with the fixed base image or dependency version. You review it like any other change."
What changed: names the mechanism and keeps the human in the loop, which is what engineers want anyway.

**3. The proof**
Before: "Leading enterprises have reduced risk by 90%."
After: "[NEED: benchmark with method, e.g. 'Across N production images, critical CVEs reaching deploy dropped from X to Y over Z weeks.'] Or one engineer's quote naming the problem it solved."
What changed: a number a practitioner can interrogate, or none at all.

## Question for the product team

What does 3.0 *not* catch, and what's the setup cost for a team with 200 services? Answer that honestly in the post and the rest of it becomes believable.
