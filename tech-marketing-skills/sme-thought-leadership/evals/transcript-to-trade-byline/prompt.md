---
tags: [sme-thought-leadership]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash, WebSearch, WebFetch]
---

Here are notes from a call with our principal SRE, Dana. Turn this into a byline for The New Stack.

Dana: Honestly most teams over-alert. We had 900 alerts a week at one point and on-call was miserable. We deleted 70% of them in one quarter and incidents didn't go up. The trick was asking for every alert, 'what would you do at 3am if this fired?' If the answer is nothing, delete it. People think more alerts means safer. It's the opposite, because the real one gets lost.
