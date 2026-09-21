# Bow tie worked examples

Three complete, **generic** examples to use as adaptable starting templates — not finished
assessments. Adapt every threat, barrier and consequence to the actual site, plant, people and the
current law and standards, and validate with a competent person. Regulatory references are
NZ/AU-oriented; confirm the equivalent in the relevant jurisdiction.

---

## Example 1 — Crane: suspended load

**Hazard:** Suspended load during a crane lift
**Top event:** Uncontrolled release / fall of the suspended load

### Threats & preventive barriers

| Threat | Preventive barriers | Escalation factors |
|---|---|---|
| Mechanical failure (crane structure/hoist) | Crane pre-start inspection checklist; current crane certification | Inspection not completed; certification lapsed |
| Rigging / sling failure | Pre-lift rigging inspection by a competent rigger; certified sling selected for the load | Sling not inspected; incorrect SWL selected |
| Operator error | Licensed/competent crane operator; lift plan for complex lifts | Operator unlicensed or unfamiliar with the crane type |
| Overloading | Lift-plan load calculation; rated capacity indicator (RCI) active | Lift plan not followed; RCI bypassed or faulty |
| Communication failure | Dogger/banksman in constant visual/radio contact; lift signals confirmed pre-lift | No banksman; radio not tested before the lift |
| Environmental (wind) | Wind speed assessed before the lift; job stopped if wind exceeds the crane's limit | Wind not monitored; limits not known |

### Consequences & recovery barriers

| Consequence | Recovery barriers | Escalation factors |
|---|---|---|
| Fatality or serious injury to crew | Enforced exclusion zone; mandatory hard hats in the lift area | Zone not enforced; workers enter during the lift |
| Injury to public / third party | Site perimeter secured; spotter controlling public access | Perimeter breach; spotter distracted |
| Property / structural damage | Pre-lift hazard ID of structures below; load path planned away from infrastructure | Load path not reviewed; overhead services not identified |
| Regulatory / legal consequence | Incident reporting protocol; regulator-notification procedure | Incident not reported; scene/evidence not preserved |

---

## Example 2 — Bulk fuel: loss of containment

**Hazard:** Diesel fuel in a bulk storage tank
**Top event:** Loss of containment from the storage tank

### Threats & preventive barriers

| Threat | Preventive barriers | Escalation factors |
|---|---|---|
| Corrosion / tank wall failure | Periodic tank inspection; corrosion-treatment programme | Inspection overdue; corrosion not actioned |
| Overfilling | High-level alarm; fill procedure with two-person check | Alarm bypassed; procedure not followed |
| Vehicle impact | Bollards / physical protection around the tank | Bollards removed or damaged |
| Fitting / valve failure | Scheduled valve inspection; correct fittings specified and installed | Fittings substituted; inspection not done |

### Consequences & recovery barriers

| Consequence | Recovery barriers | Escalation factors |
|---|---|---|
| Environmental damage (drain / waterway) | Bunded containment (≥110% capacity); drains isolated before filling | Bund cracked; drain not isolated |
| Fire | No ignition sources in the fuel area; extinguisher mounted adjacent | Ignition sources present; extinguisher discharged/expired |
| Worker exposure / injury | PPE (gloves, eye protection) when handling fuel; eyewash station | PPE unavailable; eyewash not functional |
| Regulatory / cleanup cost | Spill-response kit on site; environmental incident-reporting procedure | Kit not stocked; reporting procedure unknown |

---

## Example 3 — Working at height

**Hazard:** Working at height on scaffolding or an elevated platform
**Top event:** Person falls from height

### Threats & preventive barriers

| Threat | Preventive barriers | Escalation factors |
|---|---|---|
| Improperly secured plank / platform | Scaffold built and signed off by a competent scaffolder; pre-use inspection each shift | Scaffold not inspected; built by an unqualified person |
| Guardrail failure (corrosion / damage) | Inspection includes guardrail integrity; defects tagged out of service | Inspection missed corrosion; defect not reported |
| Trip on tools/materials | Housekeeping procedure — clear platform before work; tool tethering where required | Procedure not enforced; tools left unsecured |
| Strong winds / instability | Wind-speed check before and during work; defined stop-work threshold | No wind monitoring; threshold unknown to workers |

### Consequences & recovery barriers

| Consequence | Recovery barriers | Escalation factors |
|---|---|---|
| Fatal / serious injury to fallen worker | Personal fall-arrest system (harness + lanyard, correctly anchored); safety nets below | Harness not worn; anchor point inadequate |
| Injury to person below | Exclusion zone below the work; overhead protection (catch platform/net) | Zone not established; people walk under |
| Major project delay / shutdown | Emergency rescue plan (competent rescuer on site); first aider on site | No rescue plan; first aider absent |

---

## How to use these

- Treat each as a **starting template** — adapt threats, barriers and consequences to the specific
  site and task; do not adopt them verbatim.
- Sweep the **6M framework** (`bowtie-methodology.md`) to check you haven't missed a category.
- Any gap — a threat with no effective barrier, or a critical control with a fatal escalation
  factor — is a finding to raise and close.
- Flag the **critical controls** (the few that carry the risk) and assess each with
  `control-assurance.md`. Score residual risk with `../scripts/risk_matrix_scorer.py`.
