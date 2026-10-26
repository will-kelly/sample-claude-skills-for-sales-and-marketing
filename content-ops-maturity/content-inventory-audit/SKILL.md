---
name: content-inventory-audit
description: Audits a content library from a sitemap, CMS export or analytics CSV and sorts every piece into keep, update, merge or retire, flagging stale, duplicate, orphaned and off-strategy content. Use when a team asks what content they have, why organic traffic is declining, what to refresh first, or whether to delete old content, or before a site migration or redesign.
---

# Content inventory audit

Most teams have no idea how much content they own. A site with three years of blogging, a few acquisitions and two rebrands usually has hundreds of pages nobody has looked at since they went live. Some still rank and quietly bring in leads. Some describe products that no longer exist. Several say the same thing in slightly different ways and compete with each other in search.

This skill takes whatever export the team has and turns it into a decision list.

## What you need from the user

Any of these, more is better:
- A sitemap URL or XML file.
- A CMS export (title, URL, publish date, last updated, author, category).
- An analytics export (pageviews, entrances, conversions, by URL, ideally 12 months).
- A search console export (clicks, impressions, average position, by URL).
- The team's current product names, priority topics and audiences, so off-strategy content can be spotted.

If the files are large, work in code. Load them with pandas, join on normalized URL, and compute in scripts rather than reading rows into the conversation.

## How to run it

1. **Build the inventory.** One row per URL. Normalize URLs (lowercase, strip tracking parameters and trailing slashes) before joining sources.
2. **Add signals** to each row where data allows:
   - Age since last update.
   - Traffic and trend (last 6 months versus prior 6).
   - Conversions or assisted conversions.
   - Search position and impressions.
   - Topic or cluster, inferred from title and URL.
   - Staleness markers in the title or slug: old years, retired product names, old version numbers.
3. **Find duplicates and overlaps.** Group pages that target the same topic or query. Within each group, the strongest page is the merge target.
4. **Decide** for every row:
   - **Keep**: performing, current, on strategy.
   - **Update**: valuable (traffic, rankings or conversions) but stale. These are usually the highest-return work in the whole audit.
   - **Merge**: overlaps with a stronger page. Redirect into the target and fold in anything unique.
   - **Retire**: no traffic, no links, off strategy or inaccurate. Redirect or remove.
   - **Review**: not enough data to decide. Keep this bucket small.
5. **Prioritize** updates and merges by expected impact.

## Output format

Deliver the full inventory as a spreadsheet with a Decision column and the signals behind it. In the reply, summarize:

**What you have**: total pages, how many by decision, and the share of total traffic coming from the top 10% of pages.

**Top 15 actions**, ranked:

| Page | Decision | Why | Expected impact |
|---|---|---|---|

**Merge groups**: each cluster of overlapping pages, with the target page named.

**Patterns**: two or three things the inventory says about how the team creates content. For example, "60% of posts from 2023 target topics no longer in the strategy," or "product pages haven't been updated since the rebrand."

**Redirect plan**: a reminder that every merge and retire needs a 301 redirect, with the map in its own sheet tab.

## Rules

- Never recommend deleting a page that has meaningful traffic, backlinks or conversions without saying so explicitly.
- Retire doesn't mean delete. Default to redirecting into the closest relevant page.
- Be clear about missing data. If there's no analytics export, decisions rest on age and topic only, and the output should say so at the top.
- Don't pretend to know rankings or traffic you weren't given.
