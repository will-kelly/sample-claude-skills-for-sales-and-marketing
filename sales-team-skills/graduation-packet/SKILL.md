---
name: graduation-packet
description: Hand off an AI tool to engineering, analytics or operations when it needs production systems, sensitive data or long-term ownership. Use when a prototype outgrows the builder.
---

# Graduation packet

Forward-deployed builds are supposed to be fast and a little scrappy. Some of them work well enough that they need to become real: wired into production systems, touching customer or financial data, owned by a team with on-call and a roadmap. That transition is where good tools usually die, because the handoff is a Slack message and a link to a prompt.

This skill borrows from how regulated and federal environments handle it. Nobody there gets to say "it works on my laptop." You show what the system touches, who can see what, and who's accountable. That discipline is lighter here, but the questions are the same.

## When to use

Any of these is a graduation trigger:

- It needs write access to a production system (CRM, billing, customer comms)
- It reads data that's sensitive: customer PII, financials, contract terms, anything regulated
- More than one team depends on it
- It needs to run unattended
- You'd be worried if you went on vacation

## The packet

**Why it's graduating**
Which trigger, plus the evidence it's worth it (link the before-and-after ledger).

**What it touches**
Every system, with read or write, and the account or credential it uses today. Be specific about anything running under a personal login.

**Data classification**
Each data type it reads or writes, sorted into: public, internal, confidential, restricted. Where restricted data goes, including into model context. Retention: does anything get stored, logged or cached, and where.

**Access**
Who can use it, who can change it, and who should be able to but can't yet.

**Audit trail**
What's logged today, and what would be needed to answer "why did it do that?" after the fact.

**Current state, honestly**
What's prototype quality. What's hardcoded. What breaks under load. What the runbook says.

**Proposed owner**
The receiving team, a named contact, and what they're agreeing to: maintenance, model updates, user support.

**What the forward-deployed team keeps**
Usually: user feedback loop and prioritization input. Write it down so nobody assumes.

**Open questions for the receiving team**
The ones you can't answer. Better to list them than discover them in a security review.

## Rules

- Start this conversation early. If a build is likely to graduate, loop in the receiving team before it's popular.
- Never route around a review because the tool is useful. Useful tools that skipped review are the ones that get shut off.
- The receiving team decides if it's ready. Your job is to make that decision easy.
