# Launch kit: keyless cloud auth for runners (sprint release)

**Source:** sprint release notes (four items)
**Product:** [Product], a hosted CI/CD runner service for GitHub Actions
**Prepared by:** [Name] · **Target publish date:** [DATE]

## Assumptions I made

I didn't ask questions, so here's what I filled in. Each one is also on the checklist at the end.

- **Who it's for.** Platform and DevOps engineers who run GitHub Actions on [Product] runners, plus the security teams who have to sign off on how those pipelines reach cloud accounts.
- **What they couldn't do before.** Jobs on [Product] runners couldn't use OIDC federation to get cloud credentials, so customers kept long-lived AWS keys, GCP service account JSON keys, or Azure client secrets in GitHub secrets. I'm treating that as the main pain this release fixes. Engineering should confirm it's accurate. If OIDC already partly worked, the story needs to change.
- **How it works.** Workflows use the standard GitHub Actions OIDC flow (`permissions: id-token: write` plus the official cloud login actions). Customers don't need a proprietary action. Each cloud still needs a trust relationship configured on its side.
- **Status.** OIDC federation is GA on all plans. The org-level secrets audit log is **beta**, available to org admins on [PLAN(S)]. The Windows log streaming fix and the Node 22 default apply to everyone right away.
- **Node 22.** "Default Node" means the Node version preinstalled on the runner image. Workflows that pin a version with `actions/setup-node` aren't affected. Workflows that rely on the preinstalled default will now run on Node 22.
- **No pricing change.** Nothing here is a new SKU or add-on.

---

## 1. Translation table

| What shipped (engineering) | What the customer can now do | Who cares most |
|---|---|---|
| Added OIDC federation for AWS, GCP, Azure in runner auth module | Deploy to AWS, GCP, and Azure from [Product] runners using short-lived credentials, and delete the long-lived cloud keys stored in GitHub secrets | Platform engineers, security and compliance teams |
| New org-level secrets audit log (beta) | See who created, changed, or deleted secrets across the org, and when, without piecing it together repo by repo | Security teams, org admins, auditors |
| Fixed flaky log streaming on Windows runners | Watch Windows job logs live without gaps or stalls | Teams building .NET, desktop, or game projects on Windows |
| Bumped default Node to 22 | Get a current LTS Node by default. Workflows that rely on the preinstalled version should be checked | Anyone with JavaScript/TypeScript builds that don't pin Node |

The first two rows are the external story. The bottom two belong in release notes and the FAQ. They matter to the people affected, but they're a fix and a maintenance change, not a launch.

## 2. Tier recommendation: Tier 2 (targeted launch)

| Factor | Score | Why |
|---|---|---|
| Customer impact | 2 | Removes stored cloud keys, which customers couldn't do on our runners before |
| Audience reach | 1 | Matters most to teams that deploy to cloud from CI, which is a big segment but not everyone |
| Competitive significance | 1 | GitHub-hosted runners already support OIDC, so this closes a gap in deals more than it sets us apart |
| Revenue tie | 1 | Helps retention, and helps with security reviews in enterprise deals. No new SKU |
| Story value | 1 | Useful and easy to explain, but not news outside our customer base |
| **Total** | **6 / 10** | |

**Reasoning:** OIDC is the headline. It solves a real security problem and it's simple to explain. It's mostly parity with GitHub's own runners, though, which keeps it out of Tier 1. One adjustment could push it higher: if "you'll have to store static cloud keys" comes up as an objection in security reviews, this removes it, and sales should hear about it fast. The secrets audit log is beta, so it gets a secondary mention and doesn't get a launch of its own.

**Separate from tiering:** the Node 22 default change needs a direct heads-up to customers no matter what tier this is. It can break builds, so it's a support and trust issue more than a marketing one. It's in the email, the release notes, and the FAQ.

**Tier 2 assets:** short blog post, customer email, 2 LinkedIn and 2 X/Bluesky posts, sales one-pager, internal FAQ, release notes entry. No press release.

---

## 3. Assets

### 3.1 Announcement blog post (short, about 550 words)

**Headline options**

1. Deploy to AWS, GCP, and Azure without storing cloud keys
2. Your CI pipeline shouldn't be holding long-lived cloud credentials
3. Short-lived cloud credentials are now built into [Product] runners

**Byline:** [AUTHOR NAME, TITLE]

---

**Deploy to AWS, GCP, and Azure without storing cloud keys**

If your pipelines deploy to the cloud, there's probably an access key sitting in your GitHub secrets right now. It might be an AWS key pair, a GCP service account JSON file, or an Azure client secret. Somebody created it a while ago, it never expires, and rotating it is on a to-do list somewhere.

Starting today, you can delete it. [Product] runners now support OIDC federation with AWS, Google Cloud, and Azure.

**What's new**

With OIDC, your workflow doesn't keep a credential at all. When a job runs, it asks GitHub for a signed identity token that says which repo, branch, and workflow it's running for. Your cloud provider checks that token against rules you've set and hands back temporary credentials scoped to that job. They expire when the job ends.

You end up with no long-lived keys in your secrets and nothing to rotate. If a log or a compromised dependency leaks a credential, it's only good for a few minutes.

**How it works**

If you've already set up OIDC on GitHub-hosted runners, it works the same way here. Set up the trust relationship in your cloud account once, then grant the `id-token: write` permission in your workflow:

```yaml
jobs:
  deploy:
    runs-on: [product-runner-label]
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/deploy-role
          aws-region: us-east-1
      - run: aws s3 sync ./dist s3://my-bucket
```

GCP (`google-github-actions/auth`) and Azure (`azure/login`) follow the same pattern. Our docs have a step-by-step setup for each cloud: [DOCS LINK].

**Where this helps**

- **Getting through a security review.** "No long-lived cloud credentials in CI" is an easy thing to show an auditor.
- **Multi-cloud teams.** One approach covers all three providers, so you don't need a different secret-handling process for each.
- **Tighter scoping.** Cloud-side trust rules can limit access by repo, branch, or environment. Production deploys can be restricted to `main`.

**Also new: org-level secrets audit log (beta)**

Org admins can now see one log of every secret created, updated, or deleted across the organization, with who did it and when. It's in beta, so expect the format and filters to change as we get feedback. It's available on [PLAN(S)] at **Settings → Security → Audit log** [CONFIRM PATH]. It records metadata about changes to secrets. It never shows secret values.

**A couple of other changes this sprint**

- Live log streaming on Windows runners is now reliable. The gaps and stalls some of you reported are fixed.
- The preinstalled Node version on runner images is now Node 22. If you depend on the default without pinning a version, check the release notes before your next build.

**Availability**

OIDC federation for AWS, GCP, and Azure is generally available on all [Product] plans today. The secrets audit log is in beta on [PLAN(S)]. Neither one costs extra.

**Get started:** [Set up OIDC for your cloud provider →][DOCS LINK]

---

### 3.2 Customer email

**Subject line options** (under 50 characters)

1. Remove cloud keys from your CI secrets
2. OIDC is here for AWS, GCP, and Azure
3. Short-lived cloud credentials, now on [Product]

**Preview text:** Plus a Node 22 default change worth checking before your next build. *(76 characters)*

**Body** (about 140 words)

> Hi [FIRST NAME],
>
> Most CI pipelines that deploy to the cloud keep a long-lived access key in GitHub secrets. Those keys don't expire, they're tedious to rotate, and they're risky if they leak.
>
> [Product] runners now support OIDC federation with AWS, GCP, and Azure. Your jobs get short-lived credentials when they run, so you can delete the stored keys.
>
> **Do you need to do anything?** OIDC is opt-in. Nothing changes until you set it up.
>
> **One thing to check:** runner images now come with Node 22 by default. If your workflows use the preinstalled Node without pinning a version with `actions/setup-node`, test a build or pin the version you need.
>
> Org admins on [PLAN(S)] also get a new secrets audit log, now in beta.
>
> [Set up OIDC →][DOCS LINK]
>
> [SENDER NAME]

---

### 3.3 Social posts

**LinkedIn, variant A (problem-led)**

> Quick question for platform teams: how old is the oldest cloud access key in your GitHub secrets?
>
> For a lot of teams the honest answer is "older than some of the people on the team."
>
> Long-lived CI credentials stick around because removing them was a hassle. On [Product] runners, it isn't anymore.
>
> We now support OIDC federation with AWS, GCP, and Azure. Jobs ask the cloud for short-lived credentials at runtime, scoped to the repo and branch you allow, and they expire when the job ends.
>
> There's nothing stored and nothing to rotate.
>
> Setup guide for all three clouds in the first comment.

*(Note: link goes in the first comment, assuming that's still our LinkedIn practice. Confirm with social.)*

**LinkedIn, variant B (outcome-led, security audience)**

> "No long-lived cloud credentials in CI/CD" used to be a hard control to meet.
>
> Now it's a config change for teams running GitHub Actions on [Product].
>
> This sprint we shipped:
> → OIDC federation for AWS, GCP, and Azure, generally available on all plans
> → An org-level secrets audit log, in beta, so admins can see who changed which secret and when
>
> If you're preparing for a SOC 2 or FedRAMP review [CONFIRM: OK to name frameworks], those two features cover a lot of the questions auditors ask about CI.
>
> Details: [BLOG LINK]

**X / Bluesky, variant A (how it works)**

> [Product] runners now support OIDC for AWS, GCP, and Azure.
>
> ```
> permissions:
>   id-token: write
> ```
>
> Add that, point your cloud login action at a role, and delete the stored key. [DOCS LINK]

*(about 190 characters including the link)*

**X / Bluesky, variant B (problem-led)**

> The AWS key in your CI secrets doesn't need to be there.
>
> OIDC federation is now live on [Product] runners for AWS, GCP, and Azure. You get short-lived credentials per job and nothing to rotate. [BLOG LINK]

*(about 210 characters including the link)*

---

### 3.4 Sales one-pager

**OIDC federation for AWS, GCP, and Azure**
*Status: GA, all plans. Companion feature: org-level secrets audit log (beta, [PLAN(S)])*

**The one-sentence pitch**
Teams running GitHub Actions on [Product] can now deploy to AWS, GCP, and Azure with short-lived credentials, so they don't have to keep long-lived cloud keys in CI.

**Who to bring it up with**

- Platform and DevOps leads who own CI/CD and cloud deploys
- Security, GRC, and compliance teams, especially during a security review or vendor assessment
- Deals that stalled over "we can't store static keys with a third-party runner"
- Prospects moving off GitHub-hosted runners who already use OIDC there. This takes away a reason to stay.

**Discovery questions**

1. "How do your pipelines authenticate to your cloud accounts today? Stored keys, or OIDC?"
2. "When did you last rotate the cloud credentials your CI uses, and who owns that?"
3. "Has your security team flagged long-lived credentials in CI as a finding or a control gap?"

**What it does**

- Works with the standard GitHub Actions OIDC flow and the official AWS, GCP, and Azure login actions
- Gives each job temporary credentials scoped by trust rules the customer controls (repo, branch, environment)
- The secrets audit log (beta) records who created, changed, or deleted a secret across the org, and when

**What it doesn't do**

- It doesn't set up the cloud side. Customers still create the IAM role, workload identity pool, or federated credential in their own cloud account.
- It doesn't cover cloud providers other than AWS, GCP, and Azure yet. There's no committed date for others.
- It doesn't remove secrets that aren't cloud credentials (API tokens, registry passwords, and so on).
- The audit log is beta. It isn't a SIEM, and don't promise log export or retention terms until they're confirmed. [NEEDS: audit log retention and export details]

**Competitive angle**

- **vs. GitHub-hosted runners:** OIDC used to be something GitHub-hosted runners had that we didn't. Now we match it, so the conversation can move back to [Product]'s strengths: [NEEDS: approved differentiators, e.g., speed, cost, machine sizes].
- **vs. [COMPETITOR]:** [NEEDS: confirm whether [COMPETITOR] supports OIDC on all three clouds. Don't claim an advantage until it's verified.]

**Objections and responses**

- *"We already use OIDC on GitHub-hosted runners. Will it break if we move?"*
  No. It's the same flow and the same actions. Most teams only change the `runs-on` label. [CONFIRM with engineering: whether trust policy subject claims need any changes.]
- *"Is the audit log ready for production compliance evidence?"*
  It's in beta. It's useful today for visibility, but don't present it as a system of record for audits yet. GA timing: [NEEDS: approved answer or "no committed date"].
- *"Does this cost extra?"*
  No. OIDC is included on all plans. The audit log beta is included on [PLAN(S)].

**Resources**
Docs: [DOCS LINK] · Blog: [BLOG LINK] · Demo environment: [DEMO LINK]

---

### 3.5 Internal FAQ (sales, support, CS)

**Pricing and packaging**

**Q: Does OIDC federation cost extra?**
A: No. It's included on all plans.

**Q: Which plans get the secrets audit log?**
A: [PLAN(S)], as a beta. [CONFIRM whether it stays on the same plans at GA.]

**Availability**

**Q: Is OIDC GA or beta?**
A: GA for AWS, GCP, and Azure.

**Q: Is it available in every runner region and on every OS?**
A: [NEEDS: confirm Linux, Windows, and macOS runners, and any region limits.]

**Q: What about GovCloud, Azure Government, or other sovereign clouds?**
A: [NEEDS: engineering answer. Don't say yes until it's confirmed.]

**Migration and upgrade impact**

**Q: Do customers have to change anything?**
A: Not for OIDC. It's opt-in. For Node 22, maybe. See below.

**Q: A customer's build broke after the update. Could it be Node?**
A: Possibly. Runner images now ship Node 22 as the default. Workflows that use the preinstalled Node without `actions/setup-node` will pick up 22. Fix: pin the version they need with `actions/setup-node`. [CONFIRM: is there an image tag or setting to temporarily keep the previous default, and how long will it be available?]

**Q: Why change the default Node?**
A: Node 22 is the current LTS line, and older lines are going out of support. Keeping the default current keeps builds on supported, patched runtimes.

**Q: A customer is moving from GitHub-hosted runners and already uses OIDC. What do they change?**
A: Usually just the `runs-on` label. [CONFIRM: whether the token's subject or issuer claims differ on our runners in a way that affects existing cloud trust policies.]

**Known limitations**

**Q: Does OIDC replace all secrets?**
A: No, only cloud credentials for AWS, GCP, and Azure. Other tokens and passwords still live in secrets.

**Q: Does the audit log show secret values?**
A: Never. It records who did what to which secret, and when. It doesn't record the value.

**Q: Can the audit log be exported to a SIEM?**
A: [NEEDS: approved answer. If not supported in beta, say "not in the beta; no committed date."]

**Roadmap**

**Q: When will other clouds or providers (Vault, Oracle Cloud, etc.) be supported?**
A: No committed date. Log the request in [FEEDBACK CHANNEL].

**Q: When does the audit log go GA?**
A: [NEEDS: approved answer, or "no committed date."]

**Security and compliance**

**Q: Is OIDC more secure than stored keys?**
A: For most teams, yes. Credentials are short-lived, scoped to the job, and never stored, so there's nothing long-lived to leak or rotate. The customer still controls the trust rules in their cloud account, and loose rules (for example, trusting any branch) weaken the benefit. Point them to the scoping guidance in the docs.

**Q: Windows logs used to drop out mid-job. Is that fixed?**
A: Yes, live log streaming on Windows runners is fixed in this release. If a customer still sees gaps, escalate to [SUPPORT ESCALATION PATH] with the job ID.

---

### 3.6 Release notes entry (customer-facing)

> **⚠ Behavior change: default Node version is now 22**
> Runner images now ship with Node 22 as the preinstalled default. If your workflows rely on the default without using `actions/setup-node`, they'll run on Node 22 starting with this release. To keep a specific version, pin it with `actions/setup-node`. [Docs →][NODE DOCS LINK]
>
> **New: OIDC federation for AWS, GCP, and Azure**
> Jobs on [Product] runners can now get short-lived cloud credentials through the standard GitHub Actions OIDC flow. You no longer need long-lived cloud keys in your secrets. Grant `id-token: write` in your workflow and configure a trust relationship in your cloud account. Generally available on all plans. [Setup guide →][DOCS LINK]
>
> **New (beta): org-level secrets audit log**
> Org admins on [PLAN(S)] can see a single log of secret creates, updates, and deletes across the org, including who made each change and when. Secret values are never recorded. This feature is in beta and may change. [Docs →][AUDIT LOG DOCS LINK]
>
> **Fixed: log streaming on Windows runners**
> Live logs on Windows runners no longer stall or drop lines during a job.

---

## 4. Consistency check

| Detail | Blog | Email | Social | One-pager | FAQ | Release notes |
|---|---|---|---|---|---|---|
| Feature name: "OIDC federation for AWS, GCP, and Azure" | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| OIDC status: GA, all plans | ✓ | implied (opt-in, no cost) | ✓ (LinkedIn B) | ✓ | ✓ | ✓ |
| Audit log labeled **beta** | ✓ | ✓ | ✓ (LinkedIn B) | ✓ | ✓ | ✓ |
| Audit log plans: [PLAN(S)] | ✓ | ✓ | n/a | ✓ | ✓ | ✓ |
| Node 22 framed as a behavior change, not a feature | ✓ | ✓ | not mentioned | n/a | ✓ | ✓ (flagged at top) |
| Windows fix framed as a fix | ✓ | not mentioned | not mentioned | n/a | ✓ | ✓ |
| No pricing change | ✓ | n/a | n/a | ✓ | ✓ | n/a |

## 5. Confirm before publishing

**Facts to verify with engineering/product**

- [ ] OIDC really wasn't usable on [Product] runners before this release. If it partly worked, rewrite the "couldn't do before" framing.
- [ ] OIDC uses the standard GitHub OIDC token and the official cloud actions, with no proprietary action required.
- [ ] Token subject and issuer claims match GitHub-hosted runners, so existing cloud trust policies work unchanged after a move.
- [ ] OIDC works on Linux, Windows, and macOS runners and in every region.
- [ ] Sovereign and government clouds (AWS GovCloud, Azure Government) are supported, or explicitly not supported.
- [ ] "Default Node" means the preinstalled runner image version, and whether customers can temporarily keep the previous default.
- [ ] The Windows log streaming fix is fully rolled out, not partial.

**Availability and packaging**

- [ ] OIDC is GA on **all** plans.
- [ ] Audit log beta plans: fill in [PLAN(S)] everywhere (blog, email, one-pager, FAQ, release notes).
- [ ] Audit log settings path (**Settings → Security → Audit log**) is correct.
- [ ] Audit log retention, export, and SIEM support answers.
- [ ] Audit log GA timing: approved answer or "no committed date."
- [ ] No pricing changes for any item.

**Dates and names**

- [ ] Publish date for the blog, email send, and social posts: [DATE]
- [ ] Product name and runner label substituted for [Product] and [product-runner-label]
- [ ] Blog author byline and email sender

**Placeholders still open**

- [ ] [DOCS LINK], [BLOG LINK], [NODE DOCS LINK], [AUDIT LOG DOCS LINK], [DEMO LINK]
- [ ] [NEEDS: approved differentiators] and [NEEDS: [COMPETITOR] OIDC support] in the one-pager
- [ ] [SUPPORT ESCALATION PATH] and [FEEDBACK CHANNEL] in the FAQ
- [ ] Approval to name SOC 2 or FedRAMP in LinkedIn variant B, or remove the reference
- [ ] LinkedIn link placement (post or first comment)

**Other notes**

- [ ] The example AWS account ID and bucket in the blog snippet are placeholders. Keep them obviously fake.
- [ ] Check that the action versions in the snippet (`@v4`) match what the docs recommend at publish time.
