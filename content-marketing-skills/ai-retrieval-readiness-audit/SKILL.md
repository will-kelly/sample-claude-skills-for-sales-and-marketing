---
name: ai-retrieval-readiness-audit
description: Audits a set of content (docs, knowledge base articles, product pages, help center exports, Markdown folders) for how well RAG systems, internal AI assistants and answer engines can find, chunk and trust it, then ranks the fixes. Use when someone asks "is our content AI ready", "why does our chatbot give wrong answers", "prep our knowledge base for RAG", "AEO audit", "documentation debt", or uploads a docs or KB export.
---

# AI retrieval readiness audit

When an internal assistant gives a wrong answer, teams blame the model. Usually the model retrieved exactly what it was given: three conflicting versions of the same policy, a page whose only heading is "Overview," and an answer that lives in a screenshot. Documentation debt you could live with when humans were searching becomes a correctness problem once a machine is.

This skill audits the content, not the model.

## When to use this

- Before connecting a knowledge base, SharePoint site, Confluence space or Notion workspace to an AI assistant
- When an assistant is already live and giving wrong or stale answers
- When marketing wants product content to show up correctly in answer engines

## When not to use this

- Model selection, embedding choice, or retrieval pipeline tuning. Say that's an engineering question and the content audit should come first anyway.
- A single page. Use an editing skill; this needs a set to find duplication and conflict.

## Workflow

### 1. Get the content

Accept a folder of Markdown or HTML, an export (zip), or pasted pages. If there are more than a few dozen files, run the scanner first:

```bash
python scripts/scan_content.py <path-to-content-folder> --out scan.json
```

The scanner reports per-file signals (heading structure, section length, missing dates, duplicate titles, near-duplicate passages, image-only content). It doesn't judge. You do.

For pasted content or small sets, read it directly and gather the same signals by hand.

### 2. Score against the rubric

Load `references/readiness-rubric.md`. Score the content set on its six dimensions. Each score cites specific files or passages. Sample at least ten files for anything you didn't scan programmatically, and say what you sampled.

### 3. Find the conflicts

The highest-risk problem is two sources that disagree. Look for:

- Same topic, different answers (pricing, limits, policy, version numbers)
- Old and new versions both live with no "superseded" marker
- Marketing pages that contradict the docs

List each conflict with both sources quoted. These go to the top of the fix list regardless of score.

### 4. Rank the fixes

Rank by **wrong-answer risk × traffic**, not by effort. A stale pricing page beats a hundred pages with weak headings. Use the fix patterns in `references/fix-patterns.md`.

### 5. Deliver

1. **Readiness score.** Six dimensions, total, one line of evidence each
2. **Conflicts found.** Each with both sources quoted and which one should win (or "needs an owner to decide")
3. **Top ten fixes,** ranked, each with file(s), the problem, the fix pattern, and an owner role
4. **Governance gap.** One paragraph on what process let this happen and the smallest rule that would stop it recurring
5. **What the audit couldn't see** (permissions, content behind auth, attachments it couldn't parse)

## Voice

Practical and specific. Name files. Quote passages. This is an audit someone will work through with a checklist, not a strategy deck.
