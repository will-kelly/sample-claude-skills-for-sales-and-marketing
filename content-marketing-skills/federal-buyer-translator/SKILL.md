---
name: federal-buyer-translator
description: Rewrites commercial B2B tech marketing (web pages, one-pagers, solution briefs, emails) for US federal buyers, and flags claims that procurement, security or legal reviewers can't use. Use when someone says "make this work for federal", "public sector version", "B2G", "gov version of this page", or pastes commercial copy and names an agency, FedRAMP, ATO or a contract vehicle.
---

# Federal buyer translator

Commercial tech copy sells to a buyer who can say yes. Federal copy sells to a chain of people who can each say no: the mission owner, the program office, the contracting officer, the ISSO, and whoever signs the ATO. Most "public sector versions" of a commercial page just swap "customers" for "agencies" and add a flag. This skill does the real translation.

## When to use this

- A commercial asset needs a federal version
- A federal asset was written by a commercial team and reads like it
- Someone wants a sanity check before copy goes to a federal prospect, a capture team, or a GSA listing

## When not to use this

- State and local government (different buyers, different procurement rules; say so and offer a general public sector pass instead)
- Defense-specific classified or CUI program content. Flag it and stop; that needs a human with clearance context.
- Proposal volumes responding to a specific solicitation. That's proposal writing with compliance matrices, not marketing.

## Workflow

### 1. Get the context you need

Ask only for what's missing. You need:

- The asset (pasted or attached)
- Target buyer: civilian agency, DoD, intel community, or "federal generally"
- The product's actual compliance status in the buyer's own words (FedRAMP level and stage, any agency ATOs, CMMC level if relevant). If they don't know, don't guess. Write placeholders.
- Contract vehicles the product is actually on, if any

### 2. Run the claims audit first

Read `references/claim-risk-patterns.md`. Go line by line and flag every claim that matches a pattern. For each flag, give:

- The quoted line
- The risk category (compliance overstatement, unverifiable outcome, procurement mismatch, commercial-only proof)
- Why a federal reviewer would stop on it
- What a safe version needs (a fact, a qualifier, or deletion)

Never resolve a compliance claim by guessing. "FedRAMP compliant" becomes `[FedRAMP status: confirm level and stage, e.g. Moderate, Authorized]`, not "FedRAMP Moderate Authorized."

### 3. Reframe the value

Read `references/buyer-frame-map.md`. Federal buyers buy against mission outcomes, risk reduction and audit-readiness, not growth or competitive advantage. Map each commercial value claim to its federal equivalent. Where there's no honest equivalent, cut it rather than force it.

### 4. Rewrite

Produce the federal version. Rules:

- Lead with the mission problem, not the product
- Name the buying friction you remove (time to ATO, inherited controls, an existing vehicle) when it's true
- Replace commercial logos and case studies with public sector proof, or with `[NEED: federal reference or public sector case study]`
- Keep it plain. Federal readers are drowning in acronyms; spell out anything past FedRAMP, ATO and CUI on first use
- No "partner with you on your journey." No "revolutionize." No urgency theater tied to fiscal year-end unless the seller has a real reason.

### 5. Deliver

Output in this order:

1. **Claims audit table** (line, category, why it fails, fix)
2. **Federal rewrite** with placeholders visible in square brackets
3. **Open questions** the seller must answer before the copy ships (compliance status, vehicles, references)
4. **What not to say on a sales call** (two or three lines; the claims most likely to come back as a protest risk or a lost deal if a rep repeats them)

## Voice

Plain, specific, a little dry. Write like someone who has sat through an ATO kickoff and doesn't want to sit through another one because of a bad sentence.
