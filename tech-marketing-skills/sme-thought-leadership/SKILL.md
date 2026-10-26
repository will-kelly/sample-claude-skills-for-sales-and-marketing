---
name: sme-thought-leadership
description: Turns raw input from an engineer, architect, or technical exec — an interview transcript, recorded call, Slack thread, conference talk, or rough notes — into a bylined thought leadership article for a tech company's blog, LinkedIn, or a trade publication, written in the expert's voice and checked for technical accuracy. Also produces interview questions when there's no raw input yet. Use whenever someone wants to turn an SME's knowledge into content, ghostwrite for a CTO or engineer, write a byline or contributed article, "get content out of our engineers", or has a transcript they want to become a post.
---

# SME thought leadership

The best technical content at most tech companies is trapped in engineers' heads. They don't have time to write, and when marketing writes for them, it often comes out generic or subtly wrong. This skill gets the knowledge out with the least time from the expert, keeps their voice, and protects the technical accuracy that makes the piece credible.

## Two entry points

**No raw material yet?** Produce an interview guide (see `references/interview-guide.md`). Ask for the topic, the expert's role, and the target outlet, then write 10–12 questions designed to pull out opinions, stories, and specifics — not definitions the expert could get from a textbook. A 30-minute interview with good questions yields a full article.

**Have raw material?** Go straight to the workflow below.

## Workflow

### 1. Mine the source

Read the transcript or notes and pull out:

- **The point of view** — what does this person believe that their peers might disagree with? This is the spine of the piece. If you can't find one, the article will be a summary, not thought leadership; tell the person and suggest a follow-up question to draw one out.
- **Stories and specifics** — incidents, migrations, numbers, things that broke, decisions they'd make differently
- **Their phrases** — distinctive ways they explain things; these carry the voice
- **Technical claims** — anything that could be wrong, outdated, or confidential

### 2. Pick the angle and outlet format

Choose an angle that's the expert's genuine opinion, not a product pitch. Thought leadership that turns into an ad loses the reader, and trade editors reject it outright.

Adapt structure to the destination (details in `references/outlet-formats.md`):

- Company engineering blog — can go deeper technically, can mention the product where natural
- LinkedIn article — personal, first-person, shorter
- Trade publication byline (e.g., The New Stack, InfoWorld, DevOps.com, Dark Reading) — vendor-neutral, no product mentions, editors enforce this

### 3. Draft in their voice

- First person, the way they talk, minus filler
- Keep their distinctive phrasings and analogies
- Use their stories as evidence rather than generic "studies show"
- Open with something specific — an incident, a contrarian claim, a number — not a definition or "In today's fast-paced world"
- Avoid AI-sounding patterns: no "delve," no "it's not just X, it's Y," no triplets of adjectives, no tidy bow at the end summarizing what the reader just read

### 4. Accuracy and sensitivity pass

Before handing back, produce a review table for the expert:

| # | Claim or detail in the draft | Why it needs your check |
|---|---|---|

Flag: technical statements you inferred or simplified, version numbers and product names, anything about customers or internal systems that might be confidential, and any number not stated verbatim in the source. This table is what makes the expert's review take ten minutes instead of an hour.

## What not to do

- Don't invent experiences, stories, or quotes the expert didn't give. If the piece needs an example and the source has none, add a placeholder: `[EXAMPLE NEEDED: a time a deploy rollback saved you]`.
- Don't add claims the expert didn't make to "strengthen" the argument. It's their name on it.
- Don't flatten a strong opinion into a balanced survey. Hedging kills thought leadership.

## Output

1. One-paragraph angle summary and the outlet it's shaped for
2. Three headline options
3. The draft
4. The accuracy review table
5. A short pitch paragraph if the target is a trade publication
