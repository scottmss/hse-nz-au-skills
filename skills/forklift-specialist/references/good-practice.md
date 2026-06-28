# Forklifts — good practice (NZ/AU)

Methodology reference for `forklift-specialist`. Summarised from the **NZ Approved Code of Practice for
Training Operators and Instructors of Powered Industrial Lift Trucks (forklifts)** (WorkSafe NZ, Crown
copyright — free to reproduce with attribution) and aligned to the AU framework (**AS 2359** Powered
industrial trucks + Safe Work Australia / state guidance). AS/NZS standards are **copyright — cited as
verify-pointers, not reproduced**. Confirm the current edition/status of every source.

> **Not legal advice; not engineering certification.** A competent person and the truck's **data plate
> and operator manual** govern. Validate capacity, de-rating, attachments and stability against the
> actual truck and load.

---

## 1. The forklift discipline in one line

Keep the **combined centre of gravity inside the stability triangle** and **never exceed the data-plate
capacity** for the actual **load centre, lift height and attachment** — then separate the truck from
people. Most forklift harm is a **tip-over** (operator crushed) or a **struck pedestrian**.

---

## 2. Stability — the stability triangle

- A counterbalance forklift sits on **three points**: the two front wheels and the **centre pivot of the
  steer (rear) axle**. Joining them makes the **stability triangle**.
- The truck is stable only while the **combined centre of gravity** (truck + load) stays **inside** that
  triangle. It moves:
  - **Forward** as the load gets heavier or the **load centre moves further out** → forward tip-over.
  - **Sideways** when turning (centrifugal effect), on a **side-slope**, or with an **eccentric load** →
    **lateral tip-over** (the most lethal; the rear axle pivots and the truck rolls).
  - **Up** as the load is **raised** (higher CoG) and when the **mast is tilted forward**.
- Consequences: **travel with the load low and mast tilted back**; slow down and don't turn sharply;
  never travel or turn with a raised load; treat side-slopes as a tip-over risk.

---

## 3. Capacity, load centre and de-rating

- The **data plate (capacity plate)** states the **rated capacity** at a **rated load centre** (commonly
  **500 mm** measured from the fork face) and often at a reference lift height. **The data plate
  governs** — it must reflect any **attachment** fitted.
- **Capacity falls as the load centre moves further from the fork face** (a long or deep load), as
  **lift height increases**, and when an **attachment** adds weight and moves the CoG forward.
- Use `../scripts/forklift_capacity.py` for a **conservative load-centre de-rating** (or an exact
  load-moment calc if you know the fork-face-to-front-axle distance). The script is a planning aid —
  the **manufacturer's capacity chart / attachment data plate is the authority**.
- **Attachments** (clamps, rotators, jibs, slippers, extensions) reduce net capacity and require an
  **amended/attachment data plate**; the truck must be rated *with the attachment fitted*.

---

## 4. Separation from people (the other killer)

- **Eliminate the interaction** where possible: separate forklift and pedestrian areas with **physical
  barriers**, one-way systems, dedicated **pedestrian walkways and crossings**, and **exclusion zones**
  around operating trucks. Site-wide traffic management lives in `../../mobile-plant-traffic-specialist/`.
- **Engineering aids:** proximity/blue-spot and red-zone lights, reversing alarms/cameras, speed
  limiting and geofencing, mirrors and convex mirrors at blind corners, good lighting.
- **Rules:** maintain separation and eye contact; assume pedestrians can't hear/see the truck; horn at
  intersections; never allow people under raised forks or to ride as passengers.

---

## 5. Operating essentials

- **Travel:** load low, mast back, face the direction of travel; if the load blocks the view, **travel
  in reverse** (except up ramps); slow at corners, doorways and blind spots.
- **Grades/ramps:** keep the **load on the upgrade side** — drive **up forwards, down in reverse**; do
  **not** turn on, or drive across, a slope.
- **Loading docks/edges:** chock/restrain trailers, use rated dock plates, beware drive-off at leading
  edges and unsecured trailers creeping ("trailer creep"); know the floor's load rating.
- **Loads:** stable, secured, within the back-rest; nothing overhanging dangerously; don't push/drag
  loads with the tips.
- **Leaving the truck:** forks fully down and tilted to the floor, controls neutral, **park brake on**,
  power off / key out; never leave it on a slope or with a raised load.
- **Lifting people:** only in a **manufacturer-approved work platform/cage**, secured to the carriage,
  with the operator at the controls and not leaving the seat — never on bare forks or a pallet.

---

## 6. Pre-start, maintenance & fuel/charging

- **Daily pre-start check** before use: data plate present/legible, **seatbelt and overhead guard/back-
  rest**, tyres, forks (no cracks/wear), mast/chains/hydraulics (no leaks), brakes, steering, horn,
  lights, warning devices; report and lock out defects.
- **Maintenance** on a schedule by competent persons; keep records; only fit **rated attachments** and
  re-plate accordingly.
- **Refuelling/charging** is a hazardous-substance activity → `../../hazardous-substances-specialist/`:
  **LPG** cylinder handling and leaks; **battery charging** (hydrogen build-up — ventilation, no ignition
  sources; acid/PPE/eyewash; charging-area controls); **diesel/petrol** exhaust and fire/spill. Charge
  and refuel only in designated, ventilated areas.

---

## 7. Critical questions to consider

- Is the load **within the de-rated capacity** for the **actual load centre, lift height and
  attachment**, per the **data plate**?
- Will the combined CoG stay **inside the stability triangle** through travel, turning, ramps and
  lifting? Any **side-slope or eccentric load** risk?
- Are **forklifts and people separated** — barriers, walkways, exclusion zones, warnings? → site traffic
  plan in `../../mobile-plant-traffic-specialist/`.
- Is the truck **pre-start checked**, the **seatbelt worn**, and the operator **competent/certified**? →
  `../../high-risk-work-specialist/`.
- Are **refuelling/charging** controls in place? → `../../hazardous-substances-specialist/`.
- Could an event be **notifiable** (tip-over, crush, serious injury)? → `../../worksafe-nz-specialist/` /
  `../../safework-au-specialist/`.

---

## Sources & discipline

- **NZ ACOP for Training Operators and Instructors of Powered Industrial Lift Trucks (forklifts)**
  (WorkSafe NZ) — Crown copyright; summarised with attribution. Predates HSWA 2015 (HSE Act 1992) but
  **remains published as good practice** — confirm current status. Plus WorkSafe forklift guidance and
  the **NZTA class F endorsement** for road use.
- **AU**: **AS 2359** (Powered industrial trucks — safe use), Safe Work Australia and state forklift
  guidance, HRWL **LF/LO** classes. **Copyright; cited as verify-pointers only.**
- HRWL/endorsement detail lives in `../../high-risk-work-specialist/`. Confirm the current edition of any
  standard before relying on a figure.
