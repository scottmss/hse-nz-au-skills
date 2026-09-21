# The plain-language method

The jurisdiction-neutral core of `plain-language-reviewer` — audience, plain English, instruction
documents, layout, and the limits of translation. The NZ regulatory anchor is in `nz-gpg.md`; the
checklist is in `review-checklist.md`; testing is in `comprehension-testing.md`.

> **Verify-pointer, not a reproduction.** Summarised from the WorkSafe NZ good practice guidelines
> *Writing for health and safety — guidance for workplace health and safety writers* (November
> 2017), with the method generalised to NZ/AU work. Read the source for its worked examples and
> word lists. **Not legal advice.**
>
> **Sources last verified: 2026-09-04.**

## The five questions

Every review answers these, in order. The first two are the ones people skip, and skipping them is
why most rewrites fail.

1. **What is the document for?**
2. **Who will read it?**
3. **What are the main messages?**
4. **Is it effective?**
5. **How will it be shared and used?**

## 1. What is the document for?

A document that is trying to do three jobs at once does none of them. Decide which of these it is,
and split it if the answer is "more than one":

| Type | What it does | Test it against |
|---|---|---|
| **Policy** | States the organisation's position — what is to be done, by whom, how | Is the position unambiguous? |
| **Procedure** | Steps that must be done in order, each starting with an action word | Could someone follow it without asking? |
| **Instruction / work instruction** | Tells one person how to do one thing | Is every step observable? |
| **Information sheet** | Describes or explains something | Is it findable at the moment of need? |
| **Form** | Asks for information | Is every field's meaning obvious? |
| **Checklist / action list** | Confirms things were done | Is each item a single, checkable fact? |
| **Table** | Lets a reader compare things | Are rows and columns labelled? |
| **Flowchart** | Shows decisions and sequence | Is every branch resolved? |
| **Graph** | Shows trend or change | Are axes and units labelled? |
| **Sign** | Instructs or warns at a point in space | Do workers know what the symbol means? |

**On signs specifically:** a sign is rarely a sufficient control on its own. Confirm workers
understand both the words and any symbol, and never let a sign stand in for a physical control.
Cross-check against `../../energy-based-safety-specialist/references/direct-controls.md` — signage
is an alternate control, always.

**Scale the document to the risk.** Low-risk work needs simple documents; a short table of hazard,
harm, controls, monitoring and who is responsible, kept on the wall and actually updated, beats a
40-page manual nobody opens. Complexity should be earned by the risk, not by the template.

## 2. Who will read it?

Write for them, not for the auditor. Work through:

- What do they already **know** about this topic?
- **How often and when** will they use it — daily at the workface, once at induction, or in an
  emergency at 3am?
- Is **English their first language**?
- **How well can they read?** Assume a range, not an average.
- **Can they read numbers?** Numeracy and literacy are separate skills.
- What **everyday words** do they already use for these things? Use those words.
- Do any readers need a **format other than regular print**? See `comprehension-testing.md`.

**Ask them.** Workers should tell you what the document needs to cover and how it should look,
before it is drafted. This is the worker engagement duty doing real work.

## 3. What are the main messages?

- What do workers need to **know**?
- What do workers need to **do**?
- Which activities and tasks must be covered?
- What are the risks and hazards involved?
- What is the best way to get this across — is it even words?

Anything that serves none of these comes out. **Length is a barrier**, not thoroughness. The
shorter the document, the more of it gets read.

## 4. Writing in plain English

Plain English means: a clear message, short simple sentences, everyday words, technical and legal
language explained, and a layout that helps.

### Sentences
One or two ideas per sentence. Long sentences are where meaning goes to hide. If you cannot say a
sentence aloud in one breath, split it.

### Everyday words
Use the ordinary word. *Now*, not *at this point in time*. The substitution list in
`review-checklist.md` and the linter in `../scripts/readability_check.py` carry the common
offenders.

### Technical terms
Workers — especially where English is a second language — may not know common H&S terms. Where
there is no simple alternative, **explain the concept first in plain English, then give the term**:

> You must remove (eliminate) the hazard.

Not the reverse. The plain words carry the meaning; the term is the label you are teaching.

### Acronyms and abbreviations
Expand on first use — *Accident Compensation Corporation (ACC)*. Then ask a harder question: **do
your workers already say this acronym out loud?** If not, do not use it at all. An expanded acronym
that nobody uses is still an obstacle on every later page.

### Write words in full
**Do not**, not *don't*. Full forms carry more weight in an instruction, and contractions are one
of the first things to trip a reader with limited English.

### Numbers
Words for one to ten; figures for 11 and above. Keep figures for measurements, doses, pressures and
times regardless — *4 m*, *2 seconds*, *50 V*.

### Active voice with a real actor
*The supervisor checks the guard* beats *the guard is to be checked*. Passive voice hides who does
it, which in an H&S document means nobody does it. Passive is acceptable where the actor genuinely
does not matter, or where naming them would mislead — say so rather than leaving it accidental.

### Say what to do, not what to avoid doing
An instruction that only forbids leaves the reader without the next action.

## 5. Instruction documents

The rules that separate a usable procedure from an unusable one:

- **Write the steps in the order they happen.** If you are unsure of the order, ask workers who do
  it correctly, and watch them do it. Do not reconstruct the sequence from memory or from the
  previous version of the document.
- **Number each step and start it with a verb.** *1. Deliver all ducting to the site. 2. Store in
  areas set aside by the builder. 3. Clear the work area of all obstacles.*
- **Put the task first, then bullet the steps under it**, where instructions are grouped by task.
- **Be specific where the source guidance leaves a blank.** "Wear protective clothing" and "use a
  suitable dust mask" are not instructions — name the actual clothing and the actual mask class.
  This is the single most common failure in real H&S documents, and it is a control problem as much
  as a writing one.
- **Make it visually clear which parts are instructions and which are information.** Supporting
  detail goes in a box or in italics, not inline where it interrupts the sequence.
- **Use images to illustrate key actions and objects.**

## 6. Layout

Plan it rather than inheriting it from the last document.

**Easier to read:**
- plenty of white space
- headings and subheadings that break up blocks and help readers find their part
- important headings in a **larger font** rather than underlined
- short paragraphs, one main message each
- **left-aligned** text
- a plain font — Arial, Calibri, Verdana — and the **same font and layout throughout**
- photos or illustrations that are relevant, easy to understand, and show people and equipment
  workers recognise as their own

**Harder to read:**
- **coloured text** — worse than black on white, and it can disappear when photocopied in black
  and white
- **blocks of capital letters** — fine for a heading, but in body text they LOOK LIKE SHOUTING and
  are measurably slower to read
- **too much bold and italic** — emphasis only works when it is rare
- underlining for emphasis — it reads as a hyperlink and cuts descenders

**For long documents you are legally required to hold** (safety data sheets and the like): put the
most important information on **one page**, use diagrams and symbols alongside words, and **attach
the one-page summary to the front** of the full document.

## 7. Translation and its limits

- **Do not assume a worker who speaks a language can read it.** Spoken fluency and literacy are
  different, and the assumption is a common and serious one.
- **Use a qualified translator.** A bilingual colleague is not a translator — H&S documents carry
  consequences, and a well-meant approximation is worse than none.
- **Some languages have no matching technical or workplace terms** for NZ/AU concepts. The
  translation may need to explain rather than substitute.
- **Check the dialect before translating.** Languages vary by region — including **te reo Māori**,
  where spelling and pronunciation differ between rohe. Ask which variety your workers actually
  read.
- **Consider images instead.** Photos and diagrams that carry the key message often outperform a
  translated wall of text, and they work for every language at once.
