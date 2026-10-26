# Sample Claude skills for sales and marketing

Twenty-four Claude skills for B2B and B2G technology go-to-market teams, grouped into four sets: tech marketing, content marketing, content operations, and AI builds for sales teams.

None of them are "write me a blog post" skills. Claude can already do that. These handle the calls around the writing: whether a technical buyer will believe the copy, whether the proof is real, why the content engine is slow, whether an AI assistant can find and trust what you've published, and whether a proposed AI tool for the sales team is worth building at all.

Built by [Will Kelly](https://github.com/will-kelly), content and AI workflow strategist and keen observer of the IT industry.

> **About this repo:** these are portfolio work samples. They show how I approach content, marketing and sales enablement problems, and how I turn that approach into AI tooling a team can run. They work if you install them, but they aren't a maintained product.

## Contents

- [The four sets](#the-four-sets)
- [Where to start](#where-to-start)
- [What the skills have in common](#what-the-skills-have-in-common)
- [How the sets connect](#how-the-sets-connect)
- [Install](#install)
- [Repo layout](#repo-layout)
- [Testing and helper scripts](#testing-and-helper-scripts)
- [About](#about)
- [License](#license)

## The four sets

### Tech marketing skills

[`tech-marketing-skills/`](tech-marketing-skills/) holds six skills for the work a product marketing or content team runs every month. Each one ships with evals and a packaged `.skill` file.

| Skill | What it does | Typical input | Output |
|---|---|---|---|
| [technical-positioning](tech-marketing-skills/technical-positioning/) | Builds a positioning and messaging framework for technical and economic buyers | Product docs, PRD, sales notes | Competitive alternatives, value pillars, persona messaging, proof gaps |
| [launch-kit-builder](tech-marketing-skills/launch-kit-builder/) | Sizes a release, then builds only the assets that tier deserves | Release notes, changelog, PRD | Tier call, blog post, email, social, sales one-pager, internal FAQ |
| [competitive-battlecard](tech-marketing-skills/competitive-battlecard/) | Builds a sourced, dated battlecard against a named competitor | Competitor name, win/loss notes | Two-screen battlecard with landmine questions and objection handling |
| [sme-thought-leadership](tech-marketing-skills/sme-thought-leadership/) | Turns an engineer's knowledge into a bylined article in their voice | Transcript, call notes, or nothing (it writes the interview guide) | Draft, headlines, accuracy review table, editor pitch |
| [customer-proof-story](tech-marketing-skills/customer-proof-story/) | Writes a case study and proof assets with every metric traced to its source | Customer interview or CSM notes | Case study, snippet, pull quotes, sales summary, approval package |
| [technical-buyer-review](tech-marketing-skills/technical-buyer-review/) | Reviews copy the way a skeptical engineer reads it | Any marketing copy | Scored review with line-level rewrites |

Two unedited sample runs live in [`tech-marketing-skills/examples/`](tech-marketing-skills/examples/).

### Content marketing skills

[`content-marketing-skills/`](content-marketing-skills/) holds five skills, each one a judgment call I made by hand for years before writing it down well enough for a model to make it too.

| Skill | What it does | Where the judgment comes from |
|---|---|---|
| [federal-buyer-translator](content-marketing-skills/federal-buyer-translator/) | Rewrites commercial tech marketing for federal buyers and flags claims procurement, security or legal reviewers can't use | Years inside a federal systems integrator |
| [vendor-theater-detector](content-marketing-skills/vendor-theater-detector/) | Scores DevOps, cloud-native and security copy for the claims practitioners dismiss on sight | Writing for and about security and container tooling vendors |
| [content-ops-maturity-diagnostic](content-marketing-skills/content-ops-maturity-diagnostic/) | Places a content operation on a five-level maturity model from a short intake conversation and names the one bottleneck | Enterprise content ops work where "we need more content" was never the real problem |
| [ai-retrieval-readiness-audit](content-marketing-skills/ai-retrieval-readiness-audit/) | Audits a content set for how well RAG systems, internal assistants and answer engines can find, chunk and trust it | Documentation debt and knowledge base governance in SharePoint, Confluence and Notion |
| [icp-reality-check](content-marketing-skills/icp-reality-check/) | Tests an ICP or persona for signs it was written without customer contact, and turns each weak spot into a question for sales or a customer | Too many ICPs that describe a buyer nobody on the team has met |

Each skill includes an `examples/` folder with a real before-and-after, so you can see good output before you run it.

### Content ops maturity skills

[`content-ops-maturity/`](content-ops-maturity/) holds seven skills that find where a content engine breaks and fix that stage first. A content engine runs at the speed of its weakest stage, and adding AI to drafting just builds a bigger queue in front of a broken review process.

| Skill | What it does | Use it when |
|---|---|---|
| [content-engine-diagnostic](content-ops-maturity/content-engine-diagnostic/) | Scores eight stages, from intake to maintenance, and names the constraint | Content feels slow or ineffective and nobody agrees why |
| [request-intake-triage](content-ops-maturity/request-intake-triage/) | Sets up intake and triages requests, with a brief for every yes and a redirect for every no | The team is drowning in ad hoc requests |
| [review-bottleneck-mapper](content-ops-maturity/review-bottleneck-mapper/) | Maps the approval chain, separates working time from waiting time, and redesigns review | Drafts sit in review for weeks |
| [content-inventory-audit](content-ops-maturity/content-inventory-audit/) | Sorts every page into keep, update, merge or retire from sitemap, CMS and analytics exports | Traffic is declining or a migration is coming |
| [docs-marketing-drift-check](content-ops-maturity/docs-marketing-drift-check/) | Flags where marketing claims contradict docs, release notes and pricing | After a release or rebrand, or when sales says the site is wrong |
| [ai-pipeline-blueprint](content-ops-maturity/ai-pipeline-blueprint/) | Designs an AI-assisted pipeline for one content type, with AI, assisted and human-only stages | The team wants to use AI without losing quality |
| [ops-scorecard](content-ops-maturity/ops-scorecard/) | Builds operational metrics like cycle time, review wait and refresh rate, plus how to collect them | Leadership asks why the team can't produce more |

### Sales team skills

[`sales-team-skills/`](sales-team-skills/) holds six skills for someone embedded with a sales team building AI tools that need to still work six months after the demo. Each maps to a responsibility in a forward-deployed AI role.

| Skill | What it does | Responsibility it covers |
|---|---|---|
| [workflow-debt-audit](sales-team-skills/workflow-debt-audit/) | Finds high-leverage workflows by looking for process that lives only in people's heads | Identify the highest-leverage workflows |
| [build-or-skip](sales-team-skills/build-or-skip/) | Runs build requests through four readiness gates and sets kill criteria | Prioritize what is and isn't worth building |
| [runbook-first](sales-team-skills/runbook-first/) | Writes a one-page runbook as part of every build | Keep what you build understandable and maintainable |
| [before-after-ledger](sales-team-skills/before-after-ledger/) | Captures a baseline before launch and measures time saved, quality, or new work made possible | Measure effect with real before-and-after evidence |
| [graduation-packet](sales-team-skills/graduation-packet/) | Hands a prototype off to engineering, analytics or ops when it outgrows the builder | Partner on production systems, sensitive data and long-term ownership |
| [results-readout](sales-team-skills/results-readout/) | Writes a decision-first brief for sales leadership and a reusable pattern writeup for builders | Share results with leadership and the wider team |

They run in order:

```
workflow-debt-audit → build-or-skip → (build) → runbook-first
                                              → before-after-ledger → results-readout
                                              → graduation-packet (when triggered)
```

## Where to start

Pick the problem that sounds most like yours.

| If you're saying... | Start with |
|---|---|
| "Our content is slow and nobody agrees why" | `content-engine-diagnostic` for a stage-by-stage audit, or `content-ops-maturity-diagnostic` for a faster conversational read |
| "Engineers won't buy this copy" | `technical-buyer-review` for any tech copy, `vendor-theater-detector` for DevOps, cloud and security |
| "We need a federal version of this page" | `federal-buyer-translator` |
| "Our chatbot gives wrong answers" | `ai-retrieval-readiness-audit` |
| "Here are the release notes, now what?" | `launch-kit-builder` |
| "How do we beat Competitor X?" | `competitive-battlecard` |
| "Does our ICP hold up?" | `icp-reality-check` |
| "Sales wants us to build an AI tool" | `workflow-debt-audit`, then `build-or-skip` |
| "Prove the fix worked" | `ops-scorecard` for content teams, `before-after-ledger` for sales builds. Set the baseline before you change anything. |

You don't have to name the skill. Ask in plain language and the right one loads.

## What the skills have in common

A few rules run through all four sets.

**Nothing invented.** No skill makes up metrics, customer names, quotes, benchmarks or certifications. Gaps get visible placeholders like `[PROOF NEEDED: ...]`, and unknowns stay labeled "unknown" or "measure first" rather than turning into confident estimates. An invented number in a draft becomes a liability on a landing page later.

**Diagnose before you rewrite.** Review skills produce findings first and edits second, and every finding quotes the line it came from. A rewrite with no diagnosis teaches the writer nothing.

**One constraint, not a list.** The diagnostics name a single bottleneck and say what not to fix yet. Teams that try to fix everything at once usually fix nothing.

**Process before tools, process before AI.** No skill recommends a purchase when the real gap is ownership or process. The AI pipeline and build-or-skip skills check whether the inputs are trustworthy before designing anything.

**AI stays out of judgment calls.** What the company claims, believes or quotes is a human decision. The skills hand that back explicitly with accuracy tables, approval packages and confirm-before-publishing lists.

**The skills say no.** Most include a "when not to use this" section, because a skill that triggers on everything is a skill nobody trusts.

## How the sets connect

The sets were built separately, but they hand off to each other:

- `technical-positioning` is the source of truth the launch, battlecard and proof skills align to.
- `customer-proof-story` feeds proof into launches and battlecards.
- Anything customer-facing can pass through `technical-buyer-review` or `vendor-theater-detector` before it ships.
- `ai-pipeline-blueprint` can use either review skill as a quality gate.
- `docs-marketing-drift-check` catches the claims that went stale after a launch kit shipped.
- `ai-retrieval-readiness-audit` and `workflow-debt-audit` come at the same problem from two sides: AI amplifies whatever state your content and process are already in.

## Install

Each skill is a self-contained folder with a `SKILL.md` at its root.

**Claude apps (web and desktop):** upload a skill as a zip in the Skills section of your Claude settings. Skills need to be enabled for your account or organization.

- `tech-marketing-skills/dist/` has a packaged `.skill` file for each skill.
- `content-ops-maturity/dist/` has a zip for each skill.
- For `content-marketing-skills` and `sales-team-skills`, zip the skill folder yourself:

  ```bash
  cd content-marketing-skills
  zip -r vendor-theater-detector.zip vendor-theater-detector/
  ```

**Claude Code:** copy a skill folder into `~/.claude/skills/` for personal use, or `.claude/skills/` inside a project.

```bash
git clone https://github.com/will-kelly/sample-claude-skills-for-sales-and-marketing.git
cp -r sample-claude-skills-for-sales-and-marketing/tech-marketing-skills/launch-kit-builder ~/.claude/skills/
```

**Claude API:** upload the skill folder through the Skills API and reference it in your requests.

## Repo layout

```
.
├── tech-marketing-skills/      6 skills, with evals, examples and packaged .skill files
├── content-marketing-skills/   5 skills, each with references and worked examples
├── content-ops-maturity/       7 skills, with packaged zips
└── sales-team-skills/          6 skills, SKILL.md only
```

Inside a skill folder:

```
skill-name/
├── SKILL.md       workflow and the trigger description Claude uses to pick the skill
├── references/    rubrics, templates and pattern libraries, loaded only when needed
├── examples/      sample input and output (where included)
├── scripts/       deterministic helpers (where included)
└── evals/         test prompts and grading criteria (tech marketing set)
```

Keeping the rubrics in `references/` keeps `SKILL.md` short enough to load fast. The detailed scoring tables only load when the skill is running.

Each set also has its own README with more detail on its design choices.

## Testing and helper scripts

**Evals.** Every skill in `tech-marketing-skills` ships with test cases in `evals/`, in the format `claude plugin eval` reads. Each skill covers a normal run and an edge case, such as a launch with no proof, a customer story with no metrics, or a thought leadership request with no source material. The graders check the things that usually go wrong: invented numbers, vendor-flavored bylines, and battlecards that claim to win everywhere.

**Scripts.** Two skills include Python helpers that handle the mechanical first pass so Claude can spend its judgment on the rest:

- `technical-buyer-review/scripts/scan_copy.py` flags buzzwords, absolute claims, unattributed numbers and common AI-writing tells, with line numbers.

  ```bash
  python scripts/scan_copy.py path/to/copy.txt
  ```

- `ai-retrieval-readiness-audit/scripts/scan_content.py` scans a folder of Markdown or HTML for retrieval signals like generic headings, duplicate content, missing review dates and oversized sections.

  ```bash
  python scripts/scan_content.py path/to/content-folder --out scan.json
  ```

Both report signals only. The judgment about what matters happens in the skill. If scripts can't run in your environment, the skills fall back to a manual pass using their reference lists.

## About

I'm Will Kelly, a content and AI workflow strategist and keen observer of the IT industry. I've spent 15+ years in enterprise technology content, written 300+ bylines for trade publications, and worked full time at GDIT/CSRA, Anchore and Section. My focus is documentation debt, content operations, AI readiness, and the DevOps, cloud, security and federal IT markets these skills are written for.

More work samples: [github.com/will-kelly](https://github.com/will-kelly)

## License

MIT. Use them, fork them, and tell me what broke. See [LICENSE](LICENSE).
