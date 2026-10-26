---
name: technical-buyer-review
description: Reviews marketing copy — web pages, landing pages, emails, ads, decks, blog posts, product descriptions — through the eyes of a skeptical technical buyer (developer, SRE, security engineer, IT architect) and returns a scored credibility review with line-level fixes. Flags buzzwords, unprovable claims, vague benefits, missing specifics, and AI-sounding prose. Use whenever someone asks to review, critique, tighten, or "sanity check" tech marketing copy, asks "would an engineer buy this", "does this sound like fluff", "is this too salesy", or wants feedback on messaging before it ships.
---

# Technical buyer review

Engineers and IT pros read marketing copy looking for a reason to close the tab. One unsupported superlative or a page of adjectives with no docs link and they're gone. This skill reads copy the way they do, then fixes it.

## Inputs

The copy itself (pasted text, a file, or a URL to fetch), plus — if known — who the target reader is and where the copy will appear. If the reader isn't given, infer from the copy and state the assumption.

## Workflow

### 1. Run the scanner

Save the copy to a text file and run:

```bash
python scripts/scan_copy.py path/to/copy.txt
```

It flags known buzzwords, absolute claims ("100%", "never", "zero"), unattributed numbers, and common AI-writing tells, with line numbers. It's a fast first pass, not the review — some flags will be fine in context, and the most important problems (vague value, wrong audience) need judgment. If you can't run scripts, do this pass by eye using the lists in `references/red-flags.md`.

### 2. Read it as the buyer

Read the whole piece once as the target reader would, and answer:

- **The five-second test:** after the headline and first two lines, can the reader say what the product does and who it's for?
- **The "so what" test:** for each claim, would the reader understand why it matters to *them*?
- **The "prove it" test:** which claims would they want evidence for, and is it there?
- **The "show me" test:** is there anything concrete — a code snippet, architecture detail, integration name, real number, docs link?
- **The exit test:** where would they stop reading, and why?

### 3. Score

Score each dimension 1–5 using the rubric in `references/scoring-rubric.md`: clarity, specificity, credibility, audience fit, voice. Give the overall score as the average, and a one-line verdict.

### 4. Fix

Give line-level rewrites for the highest-impact problems — usually 5–10, not every line. Show:

| Original | Problem | Rewrite |
|---|---|---|

Rewrites must not add facts the copy didn't have. Where a fix needs information you don't have (a real number, an integration list), write the rewrite with a placeholder like `[ADD: p95 latency from benchmark]` and say so. Inventing a specific to make copy sound credible is exactly the problem this skill exists to catch.

### 5. Summarize

End with the top three changes that would most improve the piece, in priority order. If the copy is good, say so plainly and keep the fixes minor. Don't manufacture criticism to look thorough.

## Tone of the review

Direct, specific, useful. Write it the way a sharp senior PMM would mark up a colleague's draft: no softening every point, no piling on.
