# Direct controls vs alternate controls

The single most useful idea in energy-based safety, and the one most often applied loosely. Used
at steps 5 and 6 of the method in `../SKILL.md`.

> **Sources last verified: 2026-11-09.** Definition per CHASNZ (v2.0, Feb 2024) after
> Hallowell (2023) / Erkal & Hallowell, *Moving Beyond TRIR* (2023). The four-rule statement,
> DC-E/DC-M split and qualifying alternate controls follow CSRA, *Energy-Based Risk Assessment*
> (2026) and Raheemy, Sherratt & Hallowell (2026). **Not legal advice.**

## The four rules

A control is a **direct control** only if it meets **all four** rules. CHASNZ states the test in
three parts; CSRA's 2026 statement makes installation a rule of its own. It is the same test.

**1. Targeted.** It is designed and intentionally used to address *that specific high-energy
hazard*. A control that happens to reduce several risks in general is not targeted at this one.

**2. Effective.** It eliminates the exposure, or reduces or isolates it so that a serious injury
or fatality is **no longer the most likely outcome**. For physical energy, that means below the
~1,500 J threshold. For a health hazard, it means below the exposure standard.

**3. Installed, verified, maintained and used properly.** **A control that is missing a required
part, or is not used as designed, is treated as absent.** It is not partially effective. There is
no partial credit.

**4. Effective despite an unrelated human error.** It still works when a competent person makes an
ordinary mistake during the work, such as a trip, a moment of distraction or a misjudged step. As
the research puts it, it is not *if* a worker will make a mistake, it is *when*. Measures that
depend mainly on a worker's attention, memory or compliance fail this rule.

Rule 4 is what does the work. It is why energy-based safety is stricter than the hierarchy of
controls, and it is where most nominated controls fail.

**Keep rules 3 and 4 apart.** A mistake *in setting up or using the control* (not clipping on, a
cover left unfixed, isolation not proven) is a rule 3 failure: the control is absent today. A
mistake *unrelated to the control* is what rule 4 tests. This is why CSRA rates a fall-arrest
system as a direct control: once it is correctly connected, it holds when the worker trips. Whether
it *is* connected is a verification question, so verify it rather than assuming it.

## Eliminate or mitigate: DC-E and DC-M

CSRA's Risk Remaining model splits direct controls in two:

- **DC-E** eliminates the exposure.
- **DC-M** mitigates or isolates it.

Both are HECA successes. RR gives DC-E ~0% and DC-M 5%. If unsure, use DC-M. See `rr-ebra.md`.

## Alternate controls

Everything that is not a direct control. CHASNZ's term covers training, PPE, barriers, signs,
procedures, permits, supervision and monitoring alike.

CSRA's 2026 work narrows this. Only three kinds earn credit when no direct control is feasible;
this skill calls them **qualifying alternate controls**:

- **physical obstacles (PO)**
- **dedicated monitoring (DM)**
- **visual reminders (VR)**

Two from different kinds, meeting five rules, form an **alternative control system (ACS)**. The
rest (training, procedures, permits, JSAs, briefings, experience and most PPE) are **supporting
activities**. They earn nothing on their own, though hazard-specific training, a safe work plan
and a quality pre-job brief are prerequisites for any ACS. Full rules are in `rr-ebra.md`.

**Alternate controls are often necessary and frequently unavoidable.** Some work genuinely has no
available direct control. The rule is not "don't use them". It is:

> **An alternate control never equals a direct control.**

In a HECA assessment, a high-energy hazard held only by alternate controls is recorded as an
**exposure**, whatever they are, because that is the honest accounting HECA exists to force. RR then
says *how much* protection they give. Even the best ACS (20%) leaves four times the risk of a
mitigating direct control (5%).

## Worked judgements

The value is in the marginal cases. These are the ones that come up. **Class** is the
classification for Risk Remaining (`rr-ebra.md`).

| Control | Verdict | Class | Why |
|---|---|---|---|
| Work moved to ground level | **Direct** | DC-E | The fall exposure no longer exists. |
| Guardrail on a platform edge | **Direct** | DC-M | Targeted at the fall; physical; holds when someone trips or is distracted. |
| Personal fall-arrest system: rated anchor, enough fall clearance, inspected, and the worker connected throughout | **Direct** | DC-M | CSRA's own rating. Once connected it holds through a trip (rule 4). It limits the consequence rather than preventing the fall, so DC-M, not DC-E. |
| Harness worn but not connected, connected to an unrated point, or without enough fall clearance | **Absent** | – | Rule 3: not used as designed. Check the connection; don't assume it. |
| Fall-restraint line set so the edge cannot be reached | **Direct** | DC-M (arguably DC-E) | If the length physically prevents reaching the edge regardless of behaviour, it survives rule 4. Assess the actual installation, not the label. |
| Covered and **secured** floor penetration | **Direct** | DC-M | Physical, targeted, error-tolerant. |
| Penetration cover not fixed down | **Absent** | – | Rule 3: incorrectly installed means the control does not exist. |
| Trench shoring / shield box | **Direct** | DC-M | Holds the face whether or not anyone remembers the depth rule. |
| Battering the face to a stable angle | **Direct** | DC-E | Removes the collapse geometry itself. |
| Stanchions and tape setting back from a trench edge, plus warning signs | **Alternate** | PO + VR = ACS2 if all five rules are met | CSRA's own example: the boundary slows people but doesn't stop entry. |
| "Don't enter the trench" instruction | **Supporting** | none | Behavioural, so it earns no RR credit. |
| De-energise, isolate, lock out and **prove dead** | **Direct** | DC-E | Energy removed and verified. The archetypal direct control. |
| Engineered cover-up on live conductors | **Direct where applicable** | DC-M | Listed by CSRA as a potential direct control. Check its rating and installation. |
| Permit to work | **Supporting** | none | Paper authorising work is not a barrier against energy. It is part of the safe work plan an ACS needs. |
| Arc-flash PPE | **Edge case** | state reasoning | Not a physical obstacle, monitoring or a reminder. Rated PPE matched to a calculated incident energy can be argued as DC-M on the same logic as fall arrest, but CSRA hasn't ruled on it. Default: no qualifying control. Never a substitute for isolation. |
| RCD on a circuit | **Edge case** | state reasoning | Direct *only* where the installation is verified and tested and it genuinely interrupts before harm. Never a substitute for isolation. State your reasoning. |
| Fixed or interlocked machine guard | **Direct** | DC-M | Physical, targeted, error-tolerant. |
| Emergency stop | **Alternate** | none | Requires someone to see the event and reach the button in time. |
| Engineered hard barricades keeping everyone out of a lift's drop and swing zone | **Direct** | DC-E | CSRA's own rating: the exposure is gone. |
| Exclusion zone marked by cones with toppers, tape or temporary fencing | **Alternate** | PO | Slows entry but doesn't prevent it. |
| Spotter whose only job is the hazard, in continuous contact, not exposed | **Alternate** | DM | Qualifies only if all three hold. A spotter with other jobs earns nothing. |
| Traffic controller / flagger | **Alternate** | DM | Only if their attention is dedicated to that hazard. |
| Proximity detection, or an alarm dedicated to the hazard | **Alternate** | DM | CSRA's example of dedicated monitoring. It warns but does not prevent the movement. |
| Reversing camera | **Alternate** | none by itself | An aid to an operator who is also driving, so not dedicated monitoring. State your reasoning if you give it credit. |
| A sign warning of an unusual or hidden hazard, readable by this crew | **Alternate** | VR | A generic sign doesn't qualify. It must tell workers something they wouldn't otherwise expect, in language they understand. |
| Engineered plant/pedestrian separation (barriered walkway) | **Direct** | DC-M | Physical, and holds when someone is distracted. |
| Tag lines on a load | **Alternate** | none | Improves control of the load, but the load still carries the energy. |
| On-tool water suppression / on-tool extraction for silica | **Direct** | health: HECA only | Engineered at source; reduces exposure below the standard while working. |
| RPE with fit testing | **Alternate** | health: HECA only | Depends on wear, fit and discipline every time. |
| Local exhaust ventilation designed and verified for the source | **Direct** | health: HECA only | Engineered, verified, works regardless of attention. |
| Substituting a non-silica product | **Direct** | DC-E | Energy eliminated entirely, the strongest form. |
| Pressure released and system positively isolated before work | **Direct** | DC-E | Energy removed. |
| Pressure-relief valve | **Direct** | DC-M | Physical, automatic, targeted, provided it is verified and maintained. |
| Depressurising "as per the procedure" with no verification step | **Absent** | – | Rule 3: without verification there is no direct control. The procedure itself is a supporting activity. |

## Two tests, not one

The **hierarchy of controls** (eliminate → substitute → isolate → engineer → administrate → PPE)
is the legal frame in both NZ and AU, and the language regulators and courts use. The
**direct-control test** is a survival frame. They overlap heavily but are not the same:

- **A control can rank well on the hierarchy and still fail rule 4.** An engineering control that
  only works when the operator selects and deploys it correctly each time is engineered, but not
  error-tolerant.
- **Elimination and substitution always pass** both, because they remove the energy.
- **Most PPE fails the direct-control test**, but it can still be legally required. Fall arrest
  that is properly designed and connected is CSRA's stated exception, as a mitigating control.

Run both. Where they disagree, satisfy both. Never present the direct-control test as the legal
standard. See the jurisdiction note in `../SKILL.md`.

## Relationship to critical controls

The direct-control test is a sharper, more testable filter for nominating **critical controls** in
a bow tie. A critical control is usually defined as one whose failure would most likely allow a
fatality. The direct-control test asks a harder and more concrete question: *does it survive an
honest mistake?* Use it to challenge a critical-control list, then carry the survivors into
control assurance: see `../../critical-risk-manager/references/control-assurance.md`.

A useful review question for any critical-risk control set:

> **"If a competent, well-intentioned person makes one ordinary mistake here today, does anybody
> die?"** If the answer is yes, the control is alternate, whatever it is called on the register.
