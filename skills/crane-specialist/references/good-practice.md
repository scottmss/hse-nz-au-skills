# Cranes & lift planning — good practice (NZ/AU)

Methodology reference for `crane-specialist`. Summarised from the **NZ Approved Code of Practice for
Cranes** (WorkSafe NZ, Crown copyright — free to reproduce with attribution) and aligned to the AU
framework (**AS 1418** design, **AS 2550** series safe use). AS/NZS standards are **copyright — cited
as verify-pointers, not reproduced**. Confirm the current edition/status of every source.

> **Not legal advice; not engineering certification.** A competent crane person / lift planner must
> validate crane selection, rated capacity, ground, stability and lift classification against the
> actual crane chart and site.

---

## 1. The crane discipline in one line

Before the hook takes load you must know **the gross load, the working radius, and the crane's rated
capacity in the actual configuration** — and you must know the **ground will hold the outrigger/track
loads**. Most crane failures are an overload at radius, a stability/ground failure, or an unplanned
lift.

---

## 2. Selecting the crane

Choose for the **worst case of the job**, with margin:

- **The heaviest and farthest pick** in the configuration you will actually use (radius, boom length,
  jib, counterweight, outriggers vs on-rubber, over-side vs over-front).
- **Crane type to task:** mobile/all-terrain, crawler, tower, overhead/gantry (EOT), vehicle-loader
  crane (HIAB), pick-and-carry (e.g. Franna). Each has different stability and chart behaviour —
  pick-and-carry capacity drops sharply with articulation and is rated on-rubber.
- **Access, set-up area, headroom, obstructions and the swing path** all feed the choice.
- Leave **capacity margin** — running a crane near 100% of chart leaves nothing for dynamics, wind,
  out-of-level or uncertainty in the load.

---

## 3. Rated capacity and the load chart

- The **load chart governs**, not the crane's headline tonnage. Rated capacity **falls as the radius
  increases** and changes with boom length, jib, counterweight and set-up.
- **Working radius** is measured from the centre of rotation to the centre of the load — confirm the
  *actual* radius, including any load swing out.
- **Deductions:** the chart capacity is for everything below the boom point — subtract the **hook
  block, slings/rigging, lifting beam, jib/aux head and any stowed jib** to get the **net** load you
  can lift.
- **On outriggers vs on-rubber** and **over-side vs over-front** are different chart areas with very
  different capacities. Use the correct one.
- The crane's **Rated Capacity Indicator/Limiter (RCI/RCL/LMI)** and **anti-two-block** are controls,
  not a substitute for planning — never lift "to the alarm".

---

## 4. Gross load build-up & utilisation

Build the gross load and check it against the chart (see `../scripts/crane_utilisation.py`):

```
gross load = load weight + rigging/slings + hook block + lifting beam/ancillaries (+ jib/aux deductions)
utilisation % = gross load / rated capacity at the working radius x 100
```

- Get the **load weight** established (not guessed) — see `../../lifting-rigging-specialist/` for load
  estimation (weight + centre of gravity).
- **Classify by utilisation and complexity** (see §6). Many regimes treat **≥ 75% of chart** as a
  critical/major lift requiring a documented lift study; confirm the threshold your management system
  uses.

---

## 5. Set-up — ground, outriggers and stability

- **Ground bearing:** the load under each outrigger/pad (or track) can be **several times** the simple
  share of crane + load, because of geometry and slew. The **pad/mat must spread that load** so the
  resulting pressure stays within the **ground's safe bearing capacity**. Get the ground assessed where
  there is any doubt; beware fill, services trenches, basements, vaults and recent excavation.
- **Outrigger pads/mats/cribbing** sized and rated; fully deployed per the chart; crane **levelled**
  (out-of-level sharply reduces capacity and can cause overturn).
- **Proximity:** keep set-up and tracking clear of **excavations, slopes, edges and voids** (a zone of
  influence applies — a crane near a trench can collapse the batter).
- **Stability** means resistance to overturning — narrow set-up, high CoG, out-of-level, side loading
  and wind all reduce it. The crane must remain stable through the **whole lift arc**, not just at pick.

---

## 6. Lift planning & critical-lift classification

Every lift needs a plan proportionate to its risk. Escalate to a **documented lift study + lift
supervisor** when any apply (confirm your own triggers):

- **High utilisation** of the crane's rated capacity (commonly ≥ 75%).
- **Tandem / dual-crane (multi-crane) lifts** — load sharing, de-rate each crane (often to ~75–80%),
  one lift coordinator, synchronised movement.
- **Blind lifts**, lifts **over people, public, roads, live plant or operating areas**.
- **Personnel lifting** by crane (work box) — tightly controlled, last resort.
- **Non-routine** loads (long/flexible/awkward CoG), **night, weather or wind**-sensitive lifts,
  proximity to **power lines** (→ `../../electrical-energy-specialist/`).

The lift plan covers: crane + configuration + chart extract; gross load & utilisation; ground &
outriggers; rigging method (→ `../../lifting-rigging-specialist/`); radius/area of operation; wind and
weather limits; exclusion zones; communications/signalling and crew roles; emergency/rescue; and sign-off.

---

## 7. Environmental limits

- **Wind:** every crane and load has a wind limit — the manufacturer's **maximum operating wind speed**
  and the **load's sail area** both matter (a light but large load can be the limit). Stop and secure
  before the limit; monitor with an anemometer.
- **Power lines:** maintain minimum approach distances and use a spotter/isolation — detail in
  `../../electrical-energy-specialist/`.
- **Weather/visibility, lightning, ground softening after rain** — all can suspend a lift.

---

## 8. Inspection, maintenance & certification

- Cranes are inspected and maintained on a schedule: **pre-start checks, routine/periodic inspection,
  annual (major periodic) inspection, and a major inspection (commonly at 10 years / design-life
  trigger)** — per **AS 2550.1** (AU) and the manufacturer; keep the **crane log book / records** and
  certificates current.
- Confirm the crane has current **certification/registration** as required in the jurisdiction (some
  cranes are registrable plant in AU), and that modifications are engineer-approved.

---

## 9. Critical questions to consider

- Is this the **right crane** for the worst-case pick, with **capacity margin**?
- What is the **rated capacity at the actual radius/configuration**, and the **gross load** after
  deductions — what's the **utilisation %**? Is it a **critical lift**?
- Will the **ground hold** the outrigger/track loads — pads sized, level, clear of edges/excavations?
- Is the crane **stable through the whole arc**, including slew and out-of-level?
- Are **wind/weather limits** set, **exclusion zones** in place, **comms/signalling** agreed and **crew
  competent**? → `../../high-risk-work-specialist/`.
- Is the **rigging method** sound? → `../../lifting-rigging-specialist/`. Is a **bow tie / lift study**
  needed? → `../../critical-risk-manager/`.
- Could a failure be a **notifiable event** (overturn, dropped load, dangerous occurrence)? →
  `../../worksafe-nz-specialist/` / `../../safework-au-specialist/`.

---

## Sources & discipline

- **NZ Approved Code of Practice for Cranes** (WorkSafe NZ) — Crown copyright; summarised with
  attribution. Predates HSWA 2015 (under progressive review) but **remains published as good
  practice** — confirm current status.
- **AU**: **AS 1418** (crane design) and **AS 2550** series (safe use — .1 general, .4 tower, .5 mobile
  & vehicle-loading), **Code of Practice for Safe Use of Mobile Cranes**, plus state/territory guidance.
  **Copyright; cited as verify-pointers only.**
- HRWL crane operation classes live in `../../high-risk-work-specialist/`. Confirm the current edition
  of any standard before relying on a figure.
