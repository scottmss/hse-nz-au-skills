# Machinery & plant safety — New Zealand regulatory & GPG anchor

The **NZ-specific** layer for `machinery-safety-specialist`: what WorkSafe NZ points duty-holders to,
the standard to benchmark against, and the one structural way NZ differs from Australia (no general plant
registration). The hierarchy-of-controls method (guarding, isolation/LOTO) is jurisdiction-neutral and
lives in `good-practice.md`; this file is the NZ anchor for it.

> **Not legal advice.** Guidance, regulations and standards change. Treat every document below as a
> **verify-pointer** — confirm the current version before relying on it. Deep duty / registration /
> notifiable detail lives in `../../worksafe-nz-specialist/`.
>
> **Sources last verified: 2026-06-30.**

## The NZ frame — duty + GPG, not a plant register

- Machinery risk is governed by the **HSWA 2015** primary duty — manage the risk **so far as is
  reasonably practicable (SFAIRP)**. There is no prescriptive "guard everything to X" rule; you assess
  the plant and safeguard it to good practice.
- **Key NZ/AU difference — NZ has no general plant registration.** Australia requires **design
  registration** and **item registration** of specified plant (pressure vessels, certain cranes, lifts,
  amusement devices, etc.). **NZ does not maintain a register of plant designs or items.** Don't import
  the AU registration step into NZ work — confirm the actual NZ requirement.
- The **narrow high-hazard exception** is the **Health and Safety in Employment (Pressure Equipment,
  Cranes, and Passenger Ropeways) Regulations 1999 (PECPR)** — pressure equipment (vessels, piping,
  boilers) and **all powered cranes** (including vehicle-mounted) need **design verification** and
  periodic **inspection by an accredited body**. Those bodies keep **their own registers** — there is no
  central WorkSafe register. (PECPR is a saved regulation under HSWA — verify it's current.)

## WorkSafe NZ guidance (the documents to cite)

- **Safe Use of Machinery — good practice guidelines** (WorkSafe; the foundational machinery GPG): hazards
  by machine part, guarding, isolation/lockout.
  https://www.worksafe.govt.nz/topic-and-industry/machinery/safe-use-of-machinery/
- **Machinery** topic hub (guarding, lockout, specific machine types):
  https://www.worksafe.govt.nz/topic-and-industry/machinery/
- **Approved Code of Practice for Pressure Equipment (Excluding Boilers)** and PECPR material for
  pressure equipment / cranes.

## The standard to benchmark against (verify-pointer — copyright)

- WorkSafe explicitly directs duty-holders to the **AS/NZS 4024 — Safety of machinery** series as *the
  current state of knowledge* for safeguarding, and the **primary standard to benchmark against**. Key
  parts: **4024.1201** (risk assessment), **4024.1601** (guards & interlocks), **4024.1603** (prevention
  of unexpected start-up / energy isolation). (Now largely published as **AS 4024** — confirm the current
  designation and edition.)
- **AS/NZS 4024 is copyright** — cite and apply, do not reproduce.

## Competency (NZ)

- **Isolation / LOTO** by competent, authorised people; **electrical isolation** by a competent/**licensed
  electrical worker**.
- **Operators** trained for the specific machine, to the manufacturer's instructions.
- **PECPR equipment** (pressure equipment, powered cranes): **design verification** and **inspection** by
  a **recognised/accredited body**; the equipment's documentation must be current. Licensing/competency
  split → `../../high-risk-work-specialist/`.

## How NZ differs from AU (quick contrast)

- **NZ:** HSWA SFAIRP duty + the **Safe Use of Machinery GPG**, benchmark to **AS/NZS 4024**; **no
  general plant register** — only the narrow **PECPR** design-verification/inspection regime (accredited
  bodies, their own registers).
- **AU:** model **Code of Practice "Managing the risks of plant in the workplace"** (Victoria differs) +
  a **plant design and item registration** scheme for specified plant. Confirm via
  `../../safework-au-specialist/`.
