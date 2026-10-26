---
name: runbook-first
description: Write the runbook for an AI tool, agent or skill as part of the build, so it stays understandable and maintainable as data, systems and processes change. Use before any build is called done.
---

# Runbook first

Every internal AI tool is one reorg away from becoming documentation debt. The person who built it moves on, the CRM field it reads gets renamed, the prompt quietly drifts, and six months later nobody knows whether the output is still right or why anyone trusted it.

This skill treats the runbook as part of the build, not cleanup. If it isn't written, the build isn't shipped.

## When to use

- Before handing any tool, agent, automation or skill to users
- When inheriting something someone else built
- At each meaningful iteration, to update what changed

## The one-page runbook

Keep it to one page. Long runbooks don't get read, and unread runbooks are debt with formatting.

**What it does**
One sentence a rep would understand. Then one sentence on what it deliberately doesn't do.

**Who owns it**
A named person and a backup. "The FDA team" is not an owner.

**Inputs and sources of truth**
Every field, doc, system and prompt it depends on, with where each one lives and who owns that source. This is the section that matters most later.

**How to tell it's working**
What a good output looks like, with one real example. What a bad one looks like, with one real example.

**Drift triggers**
The specific upstream changes that will break it or make it quietly wrong:
- A field renamed or deprecated
- Messaging or positioning updated
- A new segment, product or region added
- Model or platform version changes
- The source doc's owner leaving

For each, note who would notice and how.

**Known failure modes**
What it gets wrong today, honestly. Users trust tools more when the limits are written down.

**How to change it**
Where the prompt, config or code lives. How to test a change before it goes to the team.

**Retire when**
The condition that means this should be turned off. Every tool needs one.

## Rules

- Write for the person who inherits it, not the person who built it.
- Plain language. If a sales manager can't follow the "what it does" section, rewrite it.
- Date every update and say what changed in one line.
- If you can't fill in "inputs and sources of truth," the tool isn't ready. Send it back through `build-or-skip`.
