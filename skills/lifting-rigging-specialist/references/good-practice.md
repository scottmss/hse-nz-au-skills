# Lifting & Rigging — good practice (NZ/AU)

Methodology reference for `lifting-rigging-specialist`. Summarised from the **NZ Approved Code of
Practice for Load-lifting Rigging** (MBIE, 5th ed., Crown copyright — free to reproduce with
attribution) and aligned to the AU model WHS framework. AS/NZS and equivalent standards are
**copyright — cited as verify-pointers, not reproduced**. Confirm the current edition of every source.

> **Not legal advice; not engineering certification.** A competent rigger/dogger or engineer must
> validate every weight, WLL, de-rating and gear choice against the actual load and conditions.

---

## 1. The rigging discipline in one line

You must, before the load leaves the ground, **know the weight, know the centre of gravity, and know
the de-rated capacity of every item of gear in the configuration you are using** — and keep people out
from under the load. Most rigging failures trace back to a failure in one of those.

---

## 2. Know the weight (load estimation)

"An intelligent *guess* is not good enough." Establish the weight by, in order of preference:

1. **Marked weight** on the load — but confirm it includes *all* parts (e.g. a machine may exclude its
   motor; a hollow body may hold contents that can shift).
2. **Documentation / drawings** stating the weight.
3. **Weigh it** (e.g. while still on the truck/trailer).
4. **Calculate** from volume × material density. Mark the weight on the load if it may be lifted again.
5. **Test-lift** to read the crane's load indicator as a cross-check.

**Volumes** (for calculation): rectangular = L×W×H; cylinder = πr²×L; thick-walled pipe =
π(r₁²−r₂²)×L; pyramid = ¼×L×W×H; sphere = 4/3·πR³.
**Approx. densities (kg/m³):** steel 7700, concrete 2400, aluminium 2700, brass 8500, copper 8800,
lead 11200, brick 2100, water 1000, timber ~800, coal 900. *Average figures — actual mass varies with
composition/water content; confirm with the supplier.*
(1 tonne = 1000 kg; 1 long ton = 1016 kg; 1 US/short ton ≈ 907–909 kg.)

---

## 3. Centre of gravity, balance and stability

- The **centre of gravity (CoG)** is the point from which the load would hang in perfect balance.
- For a stable, level lift, the **hook must be vertically above the CoG**. If it is not, the load will
  swing/shift until the CoG settles under the hook — making placement difficult and dangerous.
- A load is **inherently stable when the lifting gear is attached ABOVE the CoG** and positioned around
  it. Gear attached level with or below the CoG makes the load **top-heavy and liable to topple** —
  toppling forces (wind, acceleration, braking) are always present on a suspended load.
- **Stability = resistance to toppling.** Narrow base + high CoG topples easily; wide base + low CoG is
  stable. A single-leg sling deliberately offset from the CoG (e.g. a pipe/drum) will hang tilted but
  can still be inherently stable.
- With **rigid loads on 3 or 4 legs**, consider how many legs *actually* carry the weight — often only
  two or three do real work and the rest are a small balancing force, so larger-capacity gear is needed.

---

## 4. Factors of safety (working load limit vs breaking load)

Gear is rated to a **Working Load Limit (WLL)** — the breaking load divided by a factor of safety.
Indicative factors from the Code (confirm against the marking/manufacturer):

| Gear | Factor of safety |
|---|---|
| Chain / chain slings | 4 : 1 |
| Wire rope / wire-rope slings | 5 : 1 |
| Flat webbing & round slings (metal components) | 4 : 1 (rated to suit) |
| Fibre (natural) rope | higher factors; refer to standard |

Gear and components **not made to a standard** must be rated by a competent person (test to destruction
or engineering calculation) and proof-load tested to the relevant factor. Never exceed the marked WLL.

---

## 5. Sling angle de-rating (the big one)

As the **included angle between sling legs opens up**, the tension in each leg rises and the
**assembly WLL falls**. Two recognised rating methods (see `../scripts/sling_wll_calculator.py`):

- **Uniform / general-purpose method** — uses the **worst-case angle within a band** and rates 3- and
  4-leg slings on **3 effective legs** (conservative; assumes a rigid load may not share equally).
  Simple and safe; the default for general lifting.
- **Trigonometric / special-purpose method** — uses the **actual angle** and can credit the **actual
  number of legs** *only where equal sharing genuinely occurs* (flexible load or adjustable legs).
  Higher capacity but only valid when sharing is assured.

Rules of thumb the calculator enforces:

- Capacity factor for a leg at angle **β from vertical** = `cos(β)`. At β = 60° (120° included) a leg
  carries **double** the share it carries when vertical.
- **Keep the included angle ≤ 90° wherever practicable; 120° is the practical maximum** — beyond that
  the leg tensions escalate sharply. Use a **lifting beam/spreader** to keep angles tight and the load
  level rather than opening the slings up.
- **Choke/basket hitches** change capacity: a choke hitch **reduces** WLL (≈ 20% for square/oblong,
  ≈ 25% for round loads); a basket hitch can increase it only if the legs stay near-vertical and the
  load cannot slip.

---

## 6. Selecting and protecting the gear

- **Match the hitch and gear to the load shape and lifting points.** Confirm each item is rated, marked
  with its WLL, in current inspection, and identifiable in the register.
- **Packing / softeners at corners.** A sling bent around a sharp corner loses strength; a small radius
  stops the cutting action but **does not** stop the strength loss from a tight bend. Minimum radius:
  wire rope and webbing ≈ **4× diameter**; chain per the Code's table by chain size. Packing also helps
  the sling grip and protects the load.
- **Shackles, eyebolts, rings, lifting beams/spreaders, hooks** — use rated, certified items; load
  eyebolts in line (collar/load-rated for angular loading); never side-load a shackle or hook beyond
  its rating. Hooks should have a working latch.
- **Wire rope** must not be bent around a diameter less than 2× rope dia (soft-eye single leg) or 4×
  (grommet/basket). Discard wire rope per its discard standard.
- **Inspection & register:** chains, ropes and tackle get **thorough examination by a competent
  person**; keep a register recording size, ID mark, test/exam certificate, date first used, each
  examination and any defect/remedy.

---

## 7. Rigging for crane work — running the lift

General safety requirements from the Code:

- Keep inexperienced people clear of swinging loads, bights of slack rope, lead/snatch blocks and
  anchorages.
- Be sure of **the weight, where it goes, and that the gear can handle it**; decide the slinging method
  and check the right slings are on hand.
- Check the **swing area is clear** of power lines and obstructions; prepare any tie-back anchorages.
- **Once committed, complete the lift without stopping.** Gear is attached by a competent person and
  the area cleared first.
- **Exclusion zone** covers everything directly under the crane's operating and lifting area. **No one
  passes or stands under a suspended load.** Everyone is outside the lift/drop zone when slewing.
- **One designated signaller** gives standard signals; **anyone may call STOP and it is obeyed
  instantly**. Visual/audible alarms warn people to clear before the lift.
- Hands clear of moving ropes, blocks and sling eyes; keep fingers out from under loads (especially
  steelwork). Guide rope onto winch drums with a piece of wood, not the hands. Use **tag lines** to
  control the load from outside the drop zone.
- **Structures/anchorages** used to support lifting gear must be adequate for the imposed loads (not
  just proof-tested) and certified where required.

---

## 8. Critical questions to consider

- Is the **weight established** (not guessed), and does it include all parts/contents?
- Where is the **centre of gravity**, and is the hook over it / the gear above it?
- Is every item of gear **rated, marked, in-date, in the register**, and adequate for the **de-rated**
  configuration (sling angle, hitch, number of effective legs)?
- Is the **included angle controlled** (≤ 90° where practicable; spreader/beam if not)?
- Are **corners packed**, and is the load protected from sling damage and vice versa?
- Is the **exclusion zone** set, the **signaller** designated, **tag lines** rigged, and the **swing
  path** clear of services/obstructions?
- Are the **people competent** (dogger/rigger), and is this a **critical/tandem lift** needing a lift
  study and engineer? → `../../critical-risk-manager/` + `../../high-risk-work-specialist/`.
- Could a failure be a **notifiable event**? → `../../worksafe-nz-specialist/` / `../../safework-au-specialist/`.

---

## Sources & discipline

- **NZ ACOP for Load-lifting Rigging** (MBIE, 5th ed.) — Crown copyright; summarised and quoted with
  attribution. Verify the current edition/status (approved under the repealed HSE Act 1992; continues
  under HSWA 2015 transitional provisions).
- **AU**: model WHS plant/lifting duties and any jurisdiction lifting/cranes guidance — verify per
  state/territory via `../../safework-au-specialist/`.
- **AS/NZS and equivalent standards** (chain/wire-rope/webbing/round slings, shackles, eyebolts,
  lifting devices, **AS 2550 / AS 1418** cranes) — **copyright; cited as verify-pointers only.** Confirm
  the current edition before relying on any figure.
