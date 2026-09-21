# Direct controls vs alternate controls

The single most useful idea in energy-based safety, and the one most often applied loosely. Used
at steps 5 and 6 of the method in `../SKILL.md`.

> **Sources last verified: 2026-09-03.** Definition per CHASNZ (v2.0, Feb 2024) after
> Hallowell (2023) / Erkal & Hallowell, *Moving Beyond TRIR* (2023). **Not legal advice.**

## The three-part test

A control is a **direct control** only if it meets **all three** criteria. Two out of three is an
alternate control.

**1. Targeted.** It is designed and intentionally used to address *that specific high-energy
hazard*. A control that happens to reduce several risks in general is not targeted at this one.

**2. Effective when installed, verified and used properly.** It eliminates the energy, or
mitigates a person's exposure **below the 1,500 J threshold** (or below the exposure standard for
a health hazard). **A control that is incorrectly installed, or not inspected and maintained, is
treated as absent** — not as partially effective. There is no partial credit.

**3. Effective despite unintentional human error.** It still works when a competent person makes
an ordinary mistake during the work, unrelated to installing the control. As the research puts it:
it is not *if* a worker will make a mistake, it is *when*.

Criterion 3 is what does the work. It is why energy-based safety is stricter than the hierarchy of
controls, and it is where most nominated controls fail.

## Alternate controls

Everything else. Typically:

- training and competency
- PPE
- temporary barriers, cones, tape
- signage and labelling
- instructions, SOPs, permits, JSAs, toolbox talks
- supervision, spotters and observers
- inspection and monitoring regimes

**Alternate controls are often necessary and frequently unavoidable.** Some work genuinely has no
available direct control. The rule is not "don't use them" — it is:

> **An alternate control never compensates for the absence of a direct control.**

In a HECA assessment, a high-energy hazard held only by alternate controls is recorded as an
**exposure**, not as a success. That is the honest accounting the method exists to force.

## Worked judgements

The value is in the marginal cases. These are the ones that come up.

| Control | Verdict | Why |
|---|---|---|
| Guardrail on a platform edge | **Direct** | Targeted at the fall; physical; holds when someone trips or is distracted. |
| Harness + lanyard clipped to an anchor | **Usually alternate** | Depends on the worker clipping to the right anchor, correctly, every time. Fails criterion 3. It is still essential where nothing better exists — record it as alternate. |
| Fall-restraint line set so the edge cannot be reached | **Arguably direct** | If the length physically prevents reaching the fall exposure regardless of behaviour, it survives criterion 3. Assess the actual installation, not the label. |
| Covered and **secured** floor penetration | **Direct** | Physical, targeted, error-tolerant. |
| Penetration cover not fixed down | **Absent** | Criterion 2 — incorrectly installed means the control does not exist. |
| Trench shoring / shield box | **Direct** | Holds the face whether or not anyone remembers the depth rule. |
| Battering the face to a stable angle | **Direct** | Removes the energy geometry itself. |
| "Don't enter the trench" instruction | **Alternate** | Behavioural. |
| De-energise, isolate, lock out and **prove dead** | **Direct** | Energy removed and verified. The archetypal direct control. |
| Permit to work | **Alternate** | Paper authorising work is not a barrier against energy. |
| Arc-flash PPE | **Alternate** | Mitigates injury; does not mitigate the energy below threshold. |
| RCD on a circuit | **Edge case** | Direct *only* where the installation is verified and tested and it genuinely interrupts before harm. Never a substitute for isolation. State your reasoning. |
| Fixed or interlocked machine guard | **Direct** | Physical, targeted, error-tolerant. |
| Emergency stop | **Alternate** | Requires someone to see the event and reach the button in time. |
| Exclusion zone marked by hard barriers a person cannot casually cross | **Direct** | Physical separation. |
| Exclusion zone marked by tape or cones | **Alternate** | Communicates a boundary; does not enforce one. |
| Spotter / traffic controller | **Alternate** | An attentive human is exactly what criterion 3 assumes will fail. |
| Reversing camera or proximity alarm | **Alternate** | Informs the operator; does not prevent the movement. |
| Engineered plant/pedestrian separation (barriered walkway) | **Direct** | Physical, and holds when someone is distracted. |
| Designed drop zone under a lift, physically demarcated | **Direct** | Removes the exposure rather than the energy. |
| Tag lines on a load | **Alternate** | Improves control; the load still carries the energy. |
| On-tool water suppression / on-tool extraction for silica | **Direct** | Engineered at source; reduces exposure below the standard while working. |
| RPE with fit testing | **Alternate** | Depends on wear, fit and discipline every time. |
| Local exhaust ventilation designed and verified for the source | **Direct** | Engineered, verified, works regardless of attention. |
| Substituting a non-silica product | **Direct** | Energy eliminated entirely — the strongest form. |
| Pressure released and system positively isolated before work | **Direct** | Energy removed. |
| Pressure-relief valve | **Direct** | Physical, automatic, targeted — provided it is verified and maintained. |
| Depressurising "as per the procedure" with no verification step | **Alternate** | Criterion 2 fails without verification. |

## Two tests, not one

The **hierarchy of controls** (eliminate → substitute → isolate → engineer → administrate → PPE)
is the legal frame in both NZ and AU, and the language regulators and courts use. The
**direct-control test** is a survival frame. They overlap heavily but are not the same:

- **A control can rank well on the hierarchy and still fail criterion 3.** An engineering control
  that only works when correctly selected and deployed by the operator each time is engineered,
  but not error-tolerant.
- **Elimination and substitution always pass** both — they remove the energy.
- **PPE never passes** the direct-control test, but it can still be legally required.

Run both. Where they disagree, satisfy both. Never present the direct-control test as the legal
standard — see the jurisdiction note in `../SKILL.md`.

## Relationship to critical controls

The direct-control test is a sharper, more testable filter for nominating **critical controls** in
a bow tie. A critical control is usually defined as one whose failure would most likely allow a
fatality; the direct-control test asks a harder and more concrete question — *does it survive an
honest mistake?* Use it to challenge a critical-control list, then carry the survivors into
control assurance: see `../../critical-risk-manager/references/control-assurance.md`.

A useful review question for any critical-risk control set:

> **"If a competent, well-intentioned person makes one ordinary mistake here today, does anybody
> die?"** If the answer is yes, the control is alternate, whatever it is called on the register.
