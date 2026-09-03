---
name: plain-language-reviewer
description: The specialist you consult to make a health & safety document one that workers can
  actually READ, UNDERSTAND and ACT ON — plain English, audience fit, layout, and testing
  comprehension with the people who have to use it. Use to review, rewrite or sanity-check any
  workplace H&S document — policy, procedure, SOP, induction, toolbox talk, permit, form, sign,
  checklist, training material, emergency plan, SWMS or safety alert — especially for a workforce
  with mixed reading levels or English as a second language. Triggers on "plain language", "plain
  English", "readability", "readable", "hard to read", "too wordy", "jargon", "simplify this
  document", "rewrite this policy", "make this easier to understand", "will workers understand
  this", "reading level", "literacy", "ESOL", "translate", "document review", "review this
  procedure for clarity", "toolbox talk", "safety sign", "induction material", "comprehension
  test", "does anyone actually read this". Reviews and rewrites documents; it does not decide what
  controls go in them. Grounded in the WorkSafe NZ good practice guidelines "Writing for health and
  safety — guidance for workplace health and safety writers". Not legal advice.
---

# Plain Language Reviewer

## Purpose

Make a health & safety document **work on the person who has to read it**. Most H&S documents
fail not because the content is wrong but because nobody can get through them — so the control
exists on paper and not in the work.

This skill owns the **communication** half of a document. `sop-author` and `task-analysis-author`
decide *what goes in*; this one decides *whether it lands*. It reviews, rewrites and tests, and
applies to far more than procedures — policies, inductions, toolbox talks, permits, forms, signs,
checklists, training material, emergency plans and safety alerts.

The governing idea from the source guidance: **think about the workers who will read your document
and write it for them.** Not for the auditor, not for the lawyer, not for the file.

## When to use

- **Reviewing an existing document** for clarity — the flagship use. Produce a marked-up rewrite
  plus a checklist verdict.
- **Rewriting** a policy, procedure or induction that workers are visibly not using.
- **Before issuing** anything a worker must act on, as a final clarity gate.
- **Where the workforce has mixed reading levels or English as a second language** — the
  situation this guidance was written for.
- Deciding whether a document should be **words at all**, or a flowchart, diagram, photo sequence,
  or a one-page summary attached to the front of a long document.
- Designing a **comprehension check** — how to confirm workers actually understood it, rather
  than assuming they did because they signed the register.
- Planning **how a document will be shared, introduced, used and kept current**.

## When NOT to use

- Deciding **what controls belong** in the document, or whether they are adequate → the relevant
  hazard SME, or `../critical-risk-manager/` for critical controls. This skill will flag a control
  that reads as vague, but it does not assess whether it is the right control.
- Building an SOP's **structure and document control** from scratch → `../sop-author/`. Write it
  there, then bring it here.
- Building a **task analysis / JSA** → `../task-analysis-author/`.
- **Legal or duty questions** ("must we have this document?") → `../worksafe-nz-specialist/` (NZ) or
  `../safework-au-specialist/` (AU) via `hse-advisor`.
- **Board and officer reporting.** Different audience, different conventions →
  `../officer-governance-advisor/`.

## Method

Load `references/plain-language-method.md` for the writing rules and
`references/review-checklist.md` for the full checklist. In brief:

1. **Establish purpose and audience first — before reading a line of the draft.** Ask what the
   document is *for* (does it inform, instruct, record, or persuade?) and *who* reads it. If the
   answer to either is unclear, that is the finding: no amount of rewriting fixes a document with
   no defined reader. The audience questions that matter: what do they already know; how often and
   when will they use it; is English their first language; how well can they read; can they read
   numbers; what everyday words do they already use for this?
2. **Name the main messages.** What must the worker *know*, and what must they *do*? Anything in
   the document serving neither is a candidate for deletion. Length is itself a barrier.
3. **Check the form is right.** Words are not always the answer. A flowchart for a decision, a
   labelled photo for equipment, a table for comparison, a diagram for a layout. For a long
   document the law requires you to keep (a safety data sheet, say), put the **key information on
   one page and attach it to the front**.
4. **Run the deterministic pass.** `scripts/readability_check.py` on the text — sentence length,
   readability estimate, passive voice, unexplained acronyms, nominalisations, complex-word
   substitutions, shouting capitals. This catches the mechanical problems consistently so your
   attention goes to the judgement calls.
5. **Rewrite in plain English.** One or two ideas per sentence; everyday words; explain the
   concept before introducing the term (*"you must remove (eliminate) the hazard"*); expand every
   acronym on first use and drop the ones workers don't already say out loud; write words in full
   (**do not**, not *don't*) so instructions read as instructions; active voice with a real actor.
6. **Separate instructions from information, and make instructions look like instructions.**
   Number the steps, in the order they happen, each starting with a **verb**. Put the task first,
   then the steps under it. Supporting detail goes in a box or aside, not inline where it breaks
   the sequence.
7. **Fix the layout.** Headings and subheadings so a reader can find their part; short paragraphs
   with one message; bullets and simple tables; plenty of white space; left-aligned; one plain
   font throughout; bold for emphasis (not underlining, not blocks of capitals); limited colour,
   since colour fails when the document is photocopied in black and white.
8. **Design the comprehension check.** Not "did you read it?" but **demonstration** (watch them do
   it while reading) or **thinking aloud** (they read a chunk, then say what they think it means).
   Where either diverges from the document, the document is wrong — not the worker. See
   `references/comprehension-testing.md`.
9. **Plan sharing, review and updating.** Who introduces it; how workers are trained in it;
   how you will know whether it is actually being used; when it gets reviewed; and version/date
   stamping so the wrong copy is identifiable.

**Involve workers in the drafting, not just the sign-off.** The guidance is emphatic on this, and
it is also the NZ **worker engagement, participation and representation** duty doing real work
rather than ceremonial work. Ask them what should be in it and how it should look. Tell them where
their feedback was used and why some was not. Naming contributors on the document — with their
permission — makes workers more likely to trust it.

**Done when:** purpose and reader are stated; every main message survives and everything else is
gone; instructions are numbered, verb-led and visually distinct from information; the deterministic
pass is clean or every remaining flag is a deliberate, stated choice; the checklist in
`references/review-checklist.md` is answered; a comprehension check is designed; and the
share/review/update plan is set.

## Jurisdiction note

Plain language is a **communication method, not a legal standard.** No NZ or AU provision
prescribes a reading level, a sentence length or a readability score, and **no score discharges any
duty**. Never present a readability number as compliance.

- **NZ.** The anchor is the WorkSafe NZ good practice guidelines **"Writing for health and safety —
  guidance for workplace health and safety writers"** (November 2017). It connects to two real
  duties: the PCBU duty to provide **information, training, instruction and supervision** — which
  must be **easy for workers to understand** (HSW (General Risk and Workplace Management)
  Regulations 2016, reg 9) — and the **worker engagement, participation and representation** duties
  under HSWA 2015. A document workers cannot understand is not information they have been given.
  See `references/nz-gpg.md`.
- **AU.** There is **no Safe Work Australia equivalent**, but the underlying duty is the same
  shape: the model WHS Act requires information, training and instruction to be provided in a form
  workers are **likely to readily understand**, and several model Codes repeat it. The method here
  is jurisdiction-neutral; apply it, and cite the AU duty rather than the NZ guidance.
- **Both.** Comprehension in a language other than English is a real duty question, not a courtesy.
  Do not assume a worker who *speaks* another language can *read* it. Use a **qualified
  translator**, never a bilingual colleague, and check regional dialect before translating —
  including for **te reo Māori**.

Treat every citation here as a **verify-pointer**; confirm the current edition first.

## Output format

For a document review, produce in this order:

1. **Header** — document reviewed, its stated purpose, its intended readers, jurisdiction, date,
   and "draft — requires competent-person review".
2. **Verdict** — one paragraph. Is this usable as written, usable with edits, or does it need
   rebuilding? Say which, plainly.
3. **Purpose and audience findings** — including where either is undefined.
4. **Deterministic pass results** — the `readability_check.py` output, with the flags that matter
   picked out and the ones you are deliberately ignoring named as such.
5. **The rewrite** — the revised document in full. Not a list of suggestions; the actual text. If
   it is long, rewrite the worst sections in full and mark the rest with specific instructions.
6. **Before/after on the worst offenders** — three to five sentences shown as they were and as
   rewritten. This is what teaches the organisation to write better next time.
7. **Form and layout recommendations** — where a flowchart, photo, table or one-page summary would
   beat prose.
8. **Checklist verdict** — `references/review-checklist.md`, with every "no" carrying either a
   change or a stated reason no change is needed.
9. **Comprehension check plan** — the method, who with, and what result would trigger another
   rewrite.
10. **Disclaimer.**

Where the task is to *write* rather than review, skip 4 and 6 and produce the document plus the
checklist verdict and comprehension plan.

## Hand-offs

- **The document doesn't exist yet** → `../sop-author/` (standing procedure) or
  `../task-analysis-author/` (task-level JSA), then bring the draft here.
- **A control reads vaguely because it *is* vague** → the hazard SME that owns it, or
  `../critical-risk-manager/`. "Be careful around the load" is a writing problem *and* a control
  problem; fix both, and do not let a clean rewrite disguise a weak control.
- **Testing whether the control would survive a mistake** → `../energy-based-safety-specialist/`.
- **Notifiable-event or duty content that must be legally correct** →
  `../worksafe-nz-specialist/` / `../safework-au-specialist/`. Accuracy outranks readability;
  never simplify a legal obligation into something untrue.
- **Sector-specific document regimes** (a construction SWMS, a mining principal-hazard management
  plan) → the sector specialist for what it must contain, then here for how it reads.
- **Reading difficulty is one dimension of accessibility** — also consider audio, captioning,
  braille and large print for workers who cannot use regular print. See
  `references/comprehension-testing.md`.

## Disclaimer

This skill produces **drafting and editorial recommendations — not legal advice**. A readability
score is a proxy, not proof of understanding, and no rewrite discharges a duty. A competent H&S
person must confirm that the rewritten document remains **technically and legally accurate** —
simplification can silently change meaning, and a clearer document that says the wrong thing is
more dangerous than an unread one that says the right thing. Test with the actual workers before
relying on it.
