---
name: management-talk
description: "name: management-talk"
---

---
name: management-talk
description: Rewrite engineer-to-engineer content for engineering-org leadership (VPs, directors, PMs, release managers, execs in an engineering-savvy company) and shape it for the channel it is going to — JIRA comment, Slack post, async standup line, email, or meeting talking-points. Trigger when the user asks to write/rewrite for management / exec / VP / director / PM / release manager, asks for an "executive summary / leadership update / status update", says "make this less technical / less jargony", or asks for a slack / email / standup / meeting version of work originally written engineer-to-engineer.
---

# Management Talk

Same audience and translation rules as a written status report, but **shaped for the channel** — JIRA comment, Slack post, async standup, email, or meeting talking-points. The audience reads code names but not code. The channel decides the length, formatting, and how much structure to leave on the page.

Use this any time engineering content needs to flow up the org, sideways into product/release, or into a non-engineering meeting — regardless of the destination.

## When to invoke

- "write something for management / exec / VP / director / PM / release manager"
- "rewrite this for [non-eng audience]"
- "make this non-technical" / "less techy" / "less jargony"
- "send a slack update / standup note / email" *about a piece of engineering work*
- "executive summary" / "exec summary" / "leadership update" / "status update"
- "talking points for [meeting]" *based on an engineering update*

If the channel is unclear after the trigger, ask one short question — *"JIRA, Slack, standup, or email?"* — and stop.

## Audience — what "engineering-org leadership" means

Engineering-savvy non-engineers: VPs, directors, PMs, release managers, execs in companies that ship technical products. They read product/framework names and cross-reference JIRA keys and PRs. They do not read code.

They want: *what's the state, what does it mean for customers, who owns it, what's next.* They do not want: how the bug works at the function level.

This is **not** for marketing, finance, customer-facing, or true ELI5 audiences — those need a different rewrite. Flag and confirm before producing one.

## Tone

**Keep.** Product names, framework names, team-owned component names, JIRA keys, PR numbers, customer/workload identifiers (`Tada`, `DeepSpeed`, `PyTorch`, `Llama-2-70B`, `vLLM`, `JIRA-12345`, `PR #5751`). These are the bridge between engineering and leadership tracking.

**Strip.** Function names, file paths, struct fields, commit SHAs, code expressions, env var names, line numbers, internal data-structure jargon (`tadaLaunchPrepare`, `tada/prim.h::syncWaitPeer`, `scratchBuf`, `0e0a6bac`). None of this is actionable to the audience.

**Translate.** Mechanism into one or two sentences of plain-English cause-and-effect. Not *"the kernel reads from `scratchBuf == NULL`"* but *"the GPUs end up reading from an uninitialized buffer and wait forever for a signal that never arrives."* Translate without lying — a race stays a race; a regression stays a regression.

**Don't over-strip.** Engineering-org leadership reads concept-level technical vocabulary fluently — *race condition, synchronization, uninitialized buffer, fast-path, workaround, registration, queue, driver, kernel* (in the GPU sense). The line is between *concept exists and matters here* (keep) and *here's the function/struct/file/SHA* (strip). Replacing "race" with "timing issue" patronizes the reader.

**Bias toward** active voice, concrete subjects, short paragraphs. *"We found the bug. Alex wrote the fix. PR is up for review."* beats *"The root cause has been identified and a fix has been authored and submitted for review."*

**Avoid:**

- Hedging that isn't really hedging (*"we believe," "appears to," "may have"*). State it or don't.
- Re-stating the obvious for thoroughness (*"This bug is in Tada, which is used for GPU communication, which is important for distributed training, which..."*).
- Telling leadership how to do their job (*"you should prioritize," "this needs to land before X"*). Give them the facts; they decide.
- Engineering-process minutiae: bisect runs, debug iterations, GDB sessions. They care that you found it, not how. (Exception: when the *process* itself is the story — *"we burned three weeks before realising the bisect was misleading"* — then a single sentence as a learning, not a play-by-play.)

## Channel shapes

Same content, different shell. Pick the shape that matches where it's going.

### JIRA comment / written status report

Full structured block. Bolded section labels. Easy to scan from the ticket page.

Building blocks (use as many as fit):

- **Status / TL;DR.** One bolded line. Reader can stop here and have the right answer. *"Fixed pending merge."* / *"Root cause unknown — investigating."* / *"Blocked on vendor."* / *"Customer-visible regression in 7.2; rollback in flight."*
- **Impact.** Who's affected, how badly, what they see. Customer / workload / product terms, not test-suite terms. *"Llama-2-70B fine-tuning hangs on every eval step"* > *"the test fails."*
- **What broke.** Short paragraph. Plain-English mechanism, one level of why, no code identifiers.
- **Why now / how it slipped through.** Optional. Include when leadership will ask anyway: latent regression, CI gap, prior incomplete fix, change that landed during a freeze.
- **Owner.** Person + team + their PR/branch/JIRA artifact. One link, not five.
- **Next steps.** Concrete, near-term, ordered. *"Code review → merge → backport to 7.2."*
- **Workaround / mitigation.** If customers are hitting it now, what can they do today? One sentence.
- **Risk.** Optional. Real risks only — *"fix touches the hot path; perf regression possible until benchmarked."* Don't manufacture risk to look thorough.

Order by what matters most for *this* item.

### Slack — channel post or DM

Single message, no walls of text. Heavy bolded section labels read as "I escaped from JIRA" — don't.

- One **bolded TL;DR** as the first line.
- 2–4 short bullets underneath: impact, owner+link, next step. Drop blocks that don't apply.
- One link, embedded inline (`JIRA-12345` / `PR #5751`). Not a link wall.
- No greeting, no signoff. The channel is the context.
- If it's a **thread reply** rather than a new post, lose the TL;DR — just lead with the answer.

Length target: under ~80 words for a top-level post; under ~40 for a thread reply.

### Async standup note

The audience scans 10 of these in 30 seconds. Front-load the verb.

- 1–3 lines, max.
- Pattern: *"\<state\> \<thing\>. \<owner if not me\>. \<next\>."*
- Examples:
  - *"Fixed Tada hang affecting dumbModel runs (JIRA-12345). PR #5751 in review. Backport to v7.2 next."*
  - *"Still chasing the LLM-7B eval-step hang. Reproducer is reliable now; bisecting. No ETA yet."*
- No bullets, no bolded labels. The format **is** the sentence.

### Email — internal exec / cross-team

Subject line is half the value.

- **Subject:** the TL;DR rewritten as a noun phrase. *"Tada hang in dumbModel: fix in review (JIRA-12345)."*
- **Greeting:** match the recipient register (*Hi Sam,* / *Hi all,*).
- **Body:** the JIRA-comment shape, but as flowing paragraphs separated by blank lines rather than bolded section labels. Two or three paragraphs is plenty.
- **Sign off** with the next decision point that needs the recipient's attention, if any. If none, a plain *"— [Name]"* is fine.

### Meeting talking-points

You're going to *say* this, not show it.

- Bullet list, max one short clause per bullet.
- Order is the order you'll speak in.
- Include the numbers/keys you want to reference out loud, in the bullet itself, so you don't fumble.
- Skip prose. *"dumbModel LLM-7B fine-tuning was hanging."* / *"Root cause: skipped sync in Tada fast-path."* / *"Alex's fix in review, PR #5751."* / *"Backport to v7.2 once it lands."*

## Source material

The input is one of:

1. **A JIRA ticket key** (e.g. `JIRA-12345`) → fetch via `GET /rest/api/3/issue/<KEY>?fields=summary,status,priority,assignee,comment` plus any custom fields your instance uses for technical evaluation — usually the cleanest source of current state. The most recent substantive comment is what to reframe; don't dump the full thread.
2. **Pasted technical text** → use directly.
3. **The current conversation** → if you (or the user) just produced engineering content and the user now says *"now in slack"* / *"now for the VP,"* reuse what's in context.

If the source is ambiguous, ask one question and stop.

## Output flow

1. **Confirm the channel** if it's not stated.
2. **Produce the draft** as a single chat block, formatted as the channel would render it.
3. **Ask where it goes:**
   - Default: print-only — the user copies it.
   - JIRA back-post: only if the user explicitly says so. Show the exact ADF payload, wait for explicit *"post it"* / *"go ahead"* / *"yes,"* then `POST /rest/api/3/issue/<KEY>/comment`.
   - **Never post to Slack, email, or any non-JIRA channel from this skill.** Hand the draft to the user; they post it.
4. **One iteration is normal, three is a smell.** If the user is on the third revision, ask what specific framing/audience assumption you're missing — don't keep tweaking blindly.

## Worked example — same bug, three channels

**Source (engineering JIRA comment):**

> **Mechanism:** the single-stream fast-path in `tadaLaunchPrepare` / `tadaLaunchKernel` / `tadaLaunchFinish` (gated on `scheduler->numStreams == 1 && !plan->persistent`) skipped the cross-stream event between `launchStream` and `handle->shared->deviceStream`. dumbModel hits this gate exactly. Kernel launched before deviceStream's IPC publish / scratch-buffer writes (the ones that populate `scratchBuf`) were visible to launchStream → `scratchBuf == NULL` in the kernel → stray pointer dereference → ring ready-flag read from garbage → thread spins forever.

### As a JIRA comment

> **Status: Fixed pending merge.** Bug found, fix validated, PR up for review.
>
> **Impact:** LLM-7B fine-tuning on 8 GPUs would hang every time it tried to evaluate the model — blocking the entire workload. Affects customers using dumbModel (a popular framework for training large models that don't fit on a single GPU), which means most large-model fine-tuning runs on the platform were exposed.
>
> **What broke:** Our GPU communication library (Tada) skipped an internal synchronization step under a specific configuration that dumbModel happens to trigger. The GPUs ended up reading from an uninitialized buffer and got stuck waiting for a signal that would never arrive. The unsafe shortcut had been in the code for months but wasn't reached by any real workload until now.
>
> **A previous fix attempt** added a defensive check that hid the symptom in some paths but left the underlying race in place. This new fix removes the unsafe shortcut entirely and tightens the safety check on the device side.
>
> **Owner:** Alex (Tada team). PR org/platform#5751.
>
> **Next steps:** code review → merge. Customers hitting this today can disable IPC registration as a temporary workaround.

### As a Slack post

> **Tada hang affecting dumbModel LLM-7B fine-tuning is fixed pending merge.** (JIRA-12345)
>
> - Skipped synchronization in the comms fast-path → GPUs read uninitialized memory → hang. Latent for months; dumbModel was the first workload to hit it.
> - Owner: Alex, PR #5751 in review.
> - Workaround until merge: disable IPC registration.

### As a standup note

> Fixed Tada hang on dumbModel LLM-7B (JIRA-12345). Alex's PR #5751 in review. Workaround posted in the ticket; backport to v7.2 next.

What changed between channels: same diagnosis, same owner, same next step. JIRA gets every block. Slack drops "why now" and "previous fix attempt" — too much for the channel. Standup keeps just state + key + owner + next. None of them mention `scratchBuf` or `tadaLaunchPrepare`.

## Rules

- **Never invent facts** to make the rewrite cleaner. If the engineering source says "root cause unknown," the rewrite says "root cause unknown" — do not promote a speculation to a finding for narrative tidiness.
- **Never strip a JIRA key, PR number, or customer/workload name** during de-jargoning. They're the cross-reference bridge — losing them breaks tracking.
- **Never invent owners.** If the source doesn't name one, ask the user — don't guess from `git blame` or recent commits.
- **Get sign-off before posting to JIRA.** Reuse the jira-check approval flow. Print-only output needs no approval.
- **Never post to Slack, email, or any non-JIRA channel from this skill.** Hand the draft to the user; they post it.
- **Stay out of advocacy.** This skill produces a status update, not a recommendation. If the user wants a recommendation memo, confirm before reframing.
