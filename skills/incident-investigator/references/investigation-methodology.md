# Five Whys investigation methodology

The full method for a Five Whys root cause analysis (RCA) of a workplace incident. Single-thread:
it drills one causal line to its systemic root. For multi-causal events, pair it with Fishbone
(`../../complex-problem-analyst/`). **Not legal advice.**

## The principle

Start with a specific problem and ask **"Why?"** repeatedly, each answer feeding the next question,
until fixing the answer would prevent recurrence. The number five is a guide, not a rule — stop when
the team agrees the systemic root cause is reached (often 3–7 whys).

## Step 1 — Problem statement

One clear, specific, factual sentence: **what happened · where · when · who (roles)** — observable,
measurable where possible, and **blame-free**.

- ✅ "A mobile crane sling parted during a tandem lift at the yard on 14 March; the load dropped
  ~2 m onto hardstand; no injury, minor load damage."
- ❌ "Someone used a bad sling."

A vague statement produces a vague analysis — invest time here.

## Step 2 — The why-chain

| Step | Prompt | Answer |
|---|---|---|
| Why 1 | Why did the incident happen? | … |
| Why 2 | Why did [Why 1 answer] happen? | … |
| Why 3 | Why did [Why 2 answer] happen? | … |
| Why 4 | Why did [Why 3 answer] happen? | … |
| Why 5 | Why did [Why 4 answer] happen? | … |

**Validation at each step:** *"If we fixed this, would the problem still happen?"* — Yes → keep
asking; No → root cause.

**Facilitation rules:**
- **Never stop at "human error".** Ask why the error was possible — what in the system, tools, or
  conditions allowed it. "Operator skipped the check" is a *why*, not an end point.
- **No blame.** Causes are systemic; the question is "what conditions allowed this?", not "who messed
  up?". Blame shuts down the honesty the investigation depends on.
- **Be specific.** Push past trivially simple answers to the real mechanism.
- **Include operational knowledge.** Talk to the people who do the work; understand work-as-done, not
  just work-as-imagined.
- **Schedule/commercial pressure is a cause, not an excuse.** If it contributed, ask why pressure was
  allowed to override the safety step — that points at a management/system root cause.

## Step 3 — Identify root cause(s)

For each candidate: *"If this were eliminated, would the incident have been prevented?"* If yes →
confirmed root cause; document it. **Multiple root causes are valid** — a chain can branch, and most
serious events have more than one. If the chain keeps returning to a single weak system (e.g. no
pre-start gate), that's your lever.

## Step 4 — Corrective actions

For each root cause:

| Field | Content |
|---|---|
| **What** | The specific action (concrete, not "raise awareness"). |
| **Who** | A named person or role accountable. |
| **When** | A due date. |
| **Verify** | How effectiveness will be checked, and when. |

Prefer **hard controls** (elimination/engineering) over more procedure or training where reasonably
practicable — a corrective action that just adds another administrative step on top of a system that
already failed is weak. Cross-check against the hierarchy of controls in `../../critical-risk-manager/`.

## Step 5 — Gaps and unknowns

State honestly: what information wasn't available, what needs further investigation, and what is
suspected but unconfirmed. A good RCA is candid about its limits.

## Worked example

**Incident:** A crane sling parted during a lift; the load dropped ~2 m; no injury.

| Why | Answer |
|---|---|
| 1 — Why did the sling part? | It was beyond its safe working life — visible wear and fraying. |
| 2 — Why was a worn sling used? | It was not removed from service before the lift. |
| 3 — Why wasn't it removed? | The pre-lift inspection was not completed that morning. |
| 4 — Why wasn't the inspection done? | The operator skipped the checklist under pressure to start early. |
| 5 — Why did pressure override the checklist? | There was no supervisory gate requiring inspection sign-off before work began. |

**Root cause:** No supervisory pre-lift sign-off gate exists before crane work commences.
**Corrective action:** Add a mandatory supervisor sign-off on the pre-lift inspection to the job card
before any crane work begins. **Owner:** Operations Manager. **Due:** [date]. **Verify:** audit the
next 20 job cards for completed sign-off; spot-check on site.

> Note the chain did **not** stop at "operator skipped the checklist" (human error) — it asked why
> that was possible and reached a **system** cause that a control can fix.

## When to switch to Fishbone

If, while building the chain, you find **several independent factors converged** (e.g. a worn sling
*and* no guard *and* an untrained crew *and* production pressure), the single thread will not capture
it. Switch to or run alongside `../../complex-problem-analyst/` (Fishbone/Ishikawa) to map all factor
categories at once, then Five-Whys the most significant 1–3.

## Output

Produce: incident details · the why-chain · validated root cause(s) · a corrective-actions table
(action/owner/due/verify) · a 2–3 sentence summary for reporting · gaps and unknowns. A portable
visual is a simple symptom → … → root-cause chain in Markdown.
