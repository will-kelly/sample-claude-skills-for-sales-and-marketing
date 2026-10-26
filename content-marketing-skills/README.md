# Content marketing skills for Claude

Five Claude skills for B2B and B2G technology content marketing. Each one encodes a judgment call I've made by hand for years and finally wrote down well enough for a model to make it too.

None of these are "write me a blog post" skills. Claude can already do that. These are the calls that come *before* and *after* the writing: who the piece is really for, whether a buyer will believe it, whether the content operation behind it can sustain it, and whether an AI system can even find it.

## The skills

| Skill | What it does | Where the judgment comes from |
|---|---|---|
| [federal-buyer-translator](federal-buyer-translator/) | Rewrites commercial tech marketing for federal buyers and flags claims procurement can't use | Years inside a federal systems integrator, watching commercial copy die in the acquisition process |
| [vendor-theater-detector](vendor-theater-detector/) | Scores DevOps, cloud and security copy for the claims practitioners laugh at | Writing for and about security and container tooling vendors, and reading their competitors' copy |
| [content-ops-maturity-diagnostic](content-ops-maturity-diagnostic/) | Diagnoses a content operation's maturity from an intake conversation and points at the real bottleneck | Content ops work across enterprise teams where "we need more content" was never the actual problem |
| [ai-retrieval-readiness-audit](ai-retrieval-readiness-audit/) | Audits a content set for how well RAG systems and answer engines can retrieve and trust it | Documentation debt and knowledge-base governance work in SharePoint, Confluence and Notion |
| [icp-reality-check](icp-reality-check/) | Tests an ideal customer profile for signs it was written by people who've never met a customer | Too many ICP docs that describe a buyer nobody on the team has ever spoken to |

## How to install

**Claude.ai or the Claude desktop app:** zip a single skill folder (for example `vendor-theater-detector/`) and upload it under Settings → Capabilities → Skills.

**Claude Code:** copy the skill folder into `~/.claude/skills/` for personal use, or `.claude/skills/` inside a project.

**Claude API:** upload the folder through the Skills API and reference it by ID in your request.

Each skill is self-contained. `SKILL.md` holds the workflow, `references/` holds the rubrics and pattern libraries Claude loads only when it needs them, and `examples/` shows a real before-and-after so you can see what good output looks like before you run it.

## Design choices worth stealing

- **Diagnose before you rewrite.** Every skill produces findings first and edits second. A rewrite with no diagnosis teaches the writer nothing and hides the reasoning.
- **Rubrics live in references, not in SKILL.md.** The main file stays short enough to load fast. The detailed scoring tables load only when the skill is actually running.
- **Every finding cites the line it came from.** No "this section feels weak." Quote it, name the pattern, say why it fails, offer the fix.
- **The skills say no.** Each one has an explicit "when not to use this" section, because a skill that triggers on everything is a skill nobody trusts.

## About

Built by Will Kelly, a content and AI workflow strategist and keen observer of the IT industry. 15+ years in enterprise technology content, 300+ bylines, and full-time stints at GDIT/CSRA, Anchore and Section.

More work samples: [github.com/will-kelly](https://github.com/will-kelly)

## License

MIT. Use them, fork them, tell me what broke.
