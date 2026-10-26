---
name: launch-kit-builder
description: Turns engineering inputs — release notes, a changelog, a PRD, a Jira epic, a GitHub release, or a product manager's brain dump — into a tiered product launch kit for a tech company, including a launch tier recommendation, announcement blog post, customer email, social posts, sales enablement one-pager, and an internal FAQ. Use whenever someone mentions a launch, a release, a new feature announcement, GA or beta, "what's new" content, release notes that need to become marketing, or asks "how should we announce this", even if they only paste a changelog.
---

# Launch kit builder

Engineering ships constantly. Marketing can't give every release the same treatment, and the worst outcome is a big feature buried in release notes while a minor one gets a press release. This skill sizes the launch first, then builds only the assets that tier deserves, all from the same source of truth.

## Inputs

Accept whatever the person has: raw release notes, a PRD, ticket descriptions, a Slack thread, a demo transcript. Also useful, if available: the positioning framework (if the team has one, align to it), the target customers, the launch date, and whether the feature is GA, beta, or preview.

If something critical is missing — mainly *who this is for* and *what they couldn't do before* — ask once, briefly. Otherwise infer, state your assumption, and keep going.

## Step 1: Translate engineering to customer value

Before writing anything, build a short translation table. Engineering inputs describe what changed; customers care about what they can now do.

| What shipped (engineering) | What the customer can now do | Who cares most |
|---|---|---|

Example: "Added OIDC support to the runner auth module" → "Connect pipelines to AWS without storing long-lived keys" → platform and security teams.

This table is the backbone of every asset. If a row can't be completed, that change probably doesn't belong in external marketing.

## Step 2: Recommend a launch tier

Use `references/launch-tiers.md` to score the release and recommend Tier 1, 2, or 3. Show the reasoning in two or three lines so the team can disagree with it. Tiering is a judgment call the team owns; the skill's job is to make the call explicit.

## Step 3: Build the assets for that tier

| Asset | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Announcement blog post | Full (800–1,200 words) | Short (400–600 words) | — |
| Customer email | Yes | Yes | Roll into newsletter |
| Social posts (LinkedIn, X/Bluesky) | 3–5 variants | 2 variants | 1 post |
| Sales one-pager | Yes | Yes | — |
| Internal FAQ (sales and support) | Yes | Yes | 3–5 Q&As |
| Release notes entry (customer-facing) | Yes | Yes | Yes |
| Press release | Optional, only if there's genuine news | — | — |

Asset guidance and structures are in `references/asset-specs.md`. Read it before drafting.

## Writing principles for launch content

- **Lead with the problem the customer had, not the feature name.** Feature names are internal; problems are universal.
- **Show it working.** Include a code snippet, CLI command, config example, or a "before/after" where it fits. Technical readers trust what they can see.
- **Be honest about status.** Beta means beta. Say what's not included yet and what's coming. Overpromising at launch creates support tickets and churn.
- **One call to action per asset.** Docs link for developers, demo for buyers, upgrade path for existing customers.
- **Keep claims checkable.** No invented performance numbers or customer quotes. Use `[NEEDS: benchmark data]` or `[NEEDS: customer quote — approved]` placeholders.

## Consistency check

After drafting, verify that every asset uses the same feature name, availability status, pricing/plan details, and date. Inconsistent availability info across the blog, email, and sales sheet is the most common launch mistake. List any details you weren't sure about under "Confirm before publishing."

## Output

Deliver a single launch kit document with:

1. Translation table
2. Tier recommendation with reasoning
3. Each asset, clearly headed
4. "Confirm before publishing" checklist (names, dates, availability, pricing, placeholders still open)
