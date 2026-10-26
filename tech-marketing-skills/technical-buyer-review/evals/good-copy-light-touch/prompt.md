---
tags: [technical-buyer-review]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash, WebSearch, WebFetch]
---

Quick sanity check before this ships:

Run Terraform plans in 30 seconds, not 10 minutes. Ephemeral runners with cached providers, OIDC to AWS/GCP/Azure, no long-lived keys. Free for public repos. Read the docs →
