# Ishikawa (Fishbone) 6M method

The full method for a Fishbone / Ishikawa analysis of a multi-causal workplace problem. **Not legal
advice.**

## Core idea

**Linear thinking** asks "what caused X? what caused that?" — one chain, one culprit. **Fishbone
thinking** asks "what *categories* of factors all contributed to X simultaneously?" The diagram puts
the **problem (effect)** at the fish head; the **bones** are cause categories; each bone carries
several contributing factors. Mapping all bones together reveals **intersections** — the combinations
that actually produce failures.

## Cause categories

### 6M (default)

| Category | Also called | Prompting questions |
|---|---|---|
| **People** | Man, human factors | Skills, training, fatigue, judgement, communication, supervision |
| **Process** | Method | Procedures, steps, standards, decision rules, SOPs |
| **Equipment** | Machine | Tools, vehicles, machinery, technology, maintenance state |
| **Environment** | Mother Nature, milieu | Weather, lighting, noise, layout, time pressure, culture |
| **Materials** | | Inputs, parts, substances, data/information quality |
| **Measurement** | | Inspection, verification, feedback loops, monitoring |

> In operational/maintenance H&S, the sixth M is often more useful as **Management** (organisational,
> oversight and regulatory factors) than *Measurement*. Adapt to context — completeness over labels.

### Alternative frameworks (adapt the bones to context)

- **Healthcare / H&S:** People, Policy, Procedure, Plant, Pathogens, Place.
- **Software / IT:** People, Process, Technology, Data, External, Communication.
- **Service / admin:** People, Process, Policy, Place, Partners, Information.
- **Simple 4M** (when 6M feels heavy): Man, Machine, Method, Materials.

You don't need all six bones on every diagram — drop those that don't apply; add domain-specific ones.

## Workflow

### 1. Define the problem (fish head)
A precise, factual effect statement — what happened, when/where, and the measurable impact. Observable,
not blame. *"The crane truck failed to start on arrival on 14 March, causing a 3-hour job delay"* —
not *"the truck broke down"*.

### 2. Brainstorm across ALL categories at once
For each bone: "how might factors in this category have contributed?" **Breadth before depth** — don't
chase one bone to its conclusion first. Useful framings: "what about [category] made this more
likely?"; "if [category] had been different, would it have been prevented or reduced?"; "what was
missing, degraded or suboptimal in [category]?" Capture short phrases; don't evaluate yet.

### 3. Build the diagram (portable ASCII default)

```
PROBLEM: [effect statement]

PEOPLE
  ├─ Operator unfamiliar with updated procedure
  ├─ Pre-start check skipped under time pressure
  └─ Supervisor unavailable at mobilisation
PROCESS
  ├─ No mandatory sign-off before departure
  └─ SOP not updated after last equipment change
EQUIPMENT
  ├─ Battery warning light ignored for 3 days
  └─ No spare battery on the vehicle
ENVIRONMENT
  ├─ Early start (5am) — reduced alertness
  └─ Customer pressure for on-time arrival
MATERIALS / INFORMATION
  └─ Job sheet didn't flag equipment-specific requirements
MEASUREMENT
  ├─ No pre-departure checklist in use
  └─ Maintenance fault log not reviewed by dispatch
```

A **Mermaid** alternative (left-right, bones angled off a spine) can be used where a rendered picture
is wanted, but the ASCII tree is the portable default and is easy to edit.

### 4. Identify the significant factors
Separate:
- **Root causes** — factors that, if corrected, prevent **recurrence** (not just this instance).
- **Contributing factors** — made it worse/more likely, but alone wouldn't have caused it.
- **Compounding intersections** — where two or more bones had to align (e.g. time pressure
  [Environment] + no checklist [Process] + unfamiliarity [People] all three). These are the real
  story of how the failure happened.

Factors appearing across multiple bones are often **systemic** — and the highest-value levers.

### 5. Corrective actions by category

| Factor | Category | Corrective action | Owner | Timeline |
|---|---|---|---|---|
| No pre-departure checklist | Process | Create and mandate a vehicle pre-departure checklist | Ops Manager | 2 weeks |
| Battery warning ignored | Equipment | Add a fault-escalation rule to the maintenance log | Workshop | 1 week |
| Supervisor unavailable | People | Define a mobilisation sign-off requirement | H&S Lead | 1 week |

Prioritise actions that address **multiple bones** or prevent multiple failure modes at once.

### 6. Gaps and unknowns
What information was unavailable, what needs further investigation, what is suspected but unconfirmed.

## Facilitation tips (team sessions)

- **Agree the effect first** before touching causes.
- **Sticky notes per category** — quantity before quality.
- **No-blame framing:** "what conditions allowed this?", not "who messed up?".
- **Five Whys within a bone** to drill a specific cause — then return to the full picture before
  concluding.
- **Hunt the intersection** — where do multiple bones point at the same gap? That's the lever.
- ~15–45 minutes as a group; solo analysis can be faster.

## Integration with Five Whys

Fishbone tells you **where** to look; Five Whys (`../../incident-investigator/`) tells you **how deep**.
Fishbone → pick the 1–3 most significant root causes → Five-Whys each. Don't Five-Whys every bone.

## Worked example

**Problem:** Two operators received minor hand injuries from the same equipment within three months.

```
PEOPLE
  ├─ Both operators new to this equipment (< 6 months)
  └─ No buddy system / supervised period for new operators
PROCESS
  ├─ No documented safe operating procedure for this equipment
  └─ Induction doesn't include hands-on familiarisation
EQUIPMENT
  ├─ Guard missing from pinch point (removed for cleaning, not replaced)
  └─ No visual warning at the pinch point
ENVIRONMENT
  ├─ Repetitive task — attention-fatigue factor
  └─ Production pressure to keep pace
MEASUREMENT
  └─ First injury not formally investigated — no lessons shared
```

**Key finding:** Not bad luck — the predictable result of inexperienced operators, missing guarding,
no SOP, and a culture that didn't investigate the first event.
**Primary lever:** Guard restoration + SOP creation addresses Equipment and Process together;
investigating all incidents addresses Measurement and feeds back into People and Process.
