# Example audit: sample-kb

Four files from a fictional help center, in [`sample-kb/`](sample-kb/). Scanner output is in [`scan-output.json`](scan-output.json).

This example is small on purpose. The point it makes: the scanner found structural problems, but the two most dangerous issues were conflicts only a human (or the skill) reading the content would catch.

## Readiness score: 9/24 — expect wrong answers, fix before launch

| Dimension | Score | Evidence |
|---|---|---|
| Single source of truth | 0 | Three files give three different answers on who gets SSO, and two give different seat limits |
| Chunkability | 2 | `sso-setup-v2.md` is well structured; `sso-setup.md` and `plans-faq.md` use "Overview" and "Details" and open sections with "It" and "This" |
| Freshness signals | 2 | Two of four files have dates; `pricing.md` was last updated March 2024 |
| Machine-readable answers | 1 | `sso-setup.md` puts the actual steps in an image with no alt text |
| Scope and condition clarity | 2 | `sso-setup-v2.md` states the plan condition in the section; the others don't |
| Governance | 2 | An old SSO page sits beside its replacement with no superseded marker |

## Conflicts found

**Who gets SSO**
- `sso-setup.md`: "It is available on all plans."
- `sso-setup-v2.md`: "SSO is available on Acme Cloud Enterprise plans only."
- `plans-faq.md`: "SSO is included on Team and Enterprise."
- `pricing.md` implies Enterprise only ("Enterprise adds SSO").

Likely winner: `sso-setup-v2.md` (most recent review date, agrees with pricing). Needs a product owner to confirm before anything else changes.

**Team plan seat limit**
- `pricing.md`: "up to 50 seats"
- `plans-faq.md`: "up to 25 seats"

Needs an owner to decide. Neither file has a recent review date.

## Top fixes

| # | Files | Problem | Fix pattern | Owner |
|---|---|---|---|---|
| 1 | All SSO references | Three answers to "who gets SSO" | Pick a winner | Product manager, SSO |
| 2 | `pricing.md`, `plans-faq.md` | Conflicting seat limits | Pick a winner, then align marketing to docs | PMM + docs lead |
| 3 | `sso-setup.md` | Old version live beside new | Mark superseded, remove from assistant index | Docs lead |
| 4 | `sso-setup.md` | Steps only in an image | Text the screenshot | Docs writer |
| 5 | `plans-faq.md` | "Overview"/"FAQ" headings; "It includes…" | Name the heading, restate the subject | Docs writer |
| 6 | `pricing.md` | Last updated March 2024 | Date and own it | PMM |

## Governance gap

A new SSO page was published without retiring the old one, and pricing lives in two places owned by two teams. The smallest rule that stops this: any page that replaces another must retire or redirect it in the same change, and plan limits live on one page that the FAQ links to instead of restating.

## What the audit couldn't see

The content of `sso-steps.png`, any pages behind login, and whether the assistant's index already excludes older files.
