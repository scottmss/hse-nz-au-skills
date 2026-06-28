# Crane types — characteristics, capacity behaviour & signature hazards (NZ/AU)

Reference for `crane-specialist`. Each crane type behaves differently on the **load chart**, on the
**ground**, and in **stability** — selecting and planning a lift means knowing the type's quirks. Use
alongside `good-practice.md`. Standards (**AS 1418** design, **AS 2550** safe use) are **copyright —
cited as verify-pointers, not reproduced**; confirm the current edition and the exact AS 2550 part.

> Licence/competency **classes** for each type live in `../../high-risk-work-specialist/` (AU HRWL
> crane classes; NZ competency). Don't transplant class codes here.

---

## Quick selector

| Type | Typical use | Rated on | Signature risk |
|---|---|---|---|
| **Mobile (all-terrain / truck / rough-terrain)** | General site lifting, road-mobile | Outriggers (and a separate on-rubber chart) | Set-up on soft/uneven ground; wrong chart area |
| **Crawler** | Heavy/long-duration, civil, wind farms | Tracks (can pick & carry on some duties) | Ground prep over a large track area; assembly; travel with load |
| **Tower** | Multi-storey construction | Fixed foundation / tie-ins | Erect/climb/dismantle phases; weathervaning; zoning with other towers |
| **Pick-and-carry (Franna / articulated)** | Yard, fabrication, short moves | On-rubber, deflection-corrected | Tip-over on slope/steer angle; travelling with suspended load |
| **Vehicle-loader (HIAB / truck-mounted articulating)** | Self-loading/unloading trucks | Stabiliser legs | Stability on the truck; deliveries near traffic/public |
| **Overhead / gantry (EOT, portal, mobile gantry)** | Workshops, yards, ports | Fixed runway / structure | Crush/pinch, runway/end-stops, load swing |

---

## Mobile cranes (all-terrain, truck-mounted, rough-terrain, city)

- **Most common and most versatile** — but most set-up-dependent. Capacity comes almost entirely from
  **outriggers fully deployed, level, on competent ground**; there is usually a **separate, much smaller
  on-rubber (pick-and-carry) chart**.
- Capacity differs **over-side vs over-rear vs over-front**, and with **boom length, jib, counterweight
  and outrigger spread** — use the exact chart area for the planned configuration.
- **Signature hazards:** outriggers on soft/fill ground or near excavations; not level; using the wrong
  chart; travelling on rubber with a load it isn't rated for; road-travel set-up errors.

## Crawler cranes

- Run on **tracks** — large bearing area, and many duties allow **pick-and-carry / travel with the load**
  (per the crane's duty chart), useful for long civil and wind-farm work.
- **No outriggers**, so the **whole track route and pad area** must be assessed and prepared (timber/steel
  mats); **out-of-level on tracks** severely cuts capacity.
- Often **lattice boom** with significant **assembly/disassembly** and transport — a high-risk phase in
  its own right.
- **Signature hazards:** ground failure under the tracks over a large footprint; travelling with load on
  a grade; assembly/dismantle; superlift/counterweight handling.

## Tower cranes

- For **multi-storey construction**: **hammerhead (saddle-jib)**, **luffing-jib** (tight/urban sites), and
  **self-erecting** types. Capacity varies along the jib (radius) per the chart.
- The **erection, climbing/jacking and dismantling phases are the highest-risk** — engineered procedures,
  the right assist crane, and exact sequence/bolt/wedge/ballast control.
- **Foundation/ballast and tie-ins** must be engineer-designed for the in-service and out-of-service
  loads. **Out of service the crane must weathervane** (slew freely into wind); set max in-service and
  out-of-service wind speeds.
- On congested sites, **multiple tower cranes / adjacent cranes** need **zoning / anti-collision and
  oversailing** controls and agreements.
- **Signature hazards:** erect/climb/dismantle, foundation/tie-in failure, storm/weathervane, collision
  with structures or other cranes, oversailing third-party property.

## Pick-and-carry cranes (Franna / articulated mobile)

- **On-rubber, articulated** cranes that **travel with the suspended load** — extremely common in yards
  and fabrication, and **over-represented in crane tip-overs**.
- Capacity is rated **on rubber and reduces as the machine articulates (steers)** — the chart is
  corrected for **tyre deflection** (correct tyre pressures matter) and assumes a firm, level surface.
- **Slopes and side-slopes are dangerous** — even a small grade or a pothole while carrying can tip it;
  dynamic effects (braking, steering, swinging load) reduce stability further.
- **Signature hazards:** travelling on a slope/uneven ground, over-articulation, speed/dynamics, tyre
  pressure/condition, load swing while moving.

## Vehicle-loader cranes (HIAB / truck-mounted articulating cranes)

- Mounted on a truck to **load/unload its own deck** (and nearby). Rated by **capacity × reach (tonne-
  metres)**; stability comes from **deployed stabiliser legs** on firm ground.
- Frequently operated **roadside / on deliveries** — near traffic, pedestrians and overhead lines.
- **Signature hazards:** truck not level / stabilisers on soft ground or in the gutter; overreach;
  unstable truck; struck-by during loading; power-line contact; public proximity.

## Overhead & gantry cranes (EOT bridge, portal/gantry, mobile gantry)

- **Fixed runway** cranes in workshops, yards and ports — **no outrigger/ground-bearing problem**, but
  the **runway/structure, end-stops, and the hoist** govern.
- **Signature hazards:** **crush/pinch** between load/crane and structure, **load swing** in a confined
  bay, runway/end-stop or hoist limit failure, dropped load over work areas, pendant/remote control
  errors. Use AS 2550 (bridge & gantry part) inspection and operating practice.

---

## Common threads (all types)

Regardless of type, the planning discipline is the same: **right crane for the worst-case pick → rated
capacity at the actual radius/configuration → gross load & utilisation → competent ground/foundation →
stability through the whole arc → wind/environment limits → lift plan and critical-lift classification →
competent crew.** See `good-practice.md`; run the gross-load/utilisation check with
`../scripts/crane_utilisation.py`.

**Standards by type (verify the current edition/part):** **AS 1418** (design) and the **AS 2550** safe-use
series — general (.1), tower (.4), mobile & vehicle-loading (.5), bridge & gantry — plus the **Code of
Practice for Safe Use of Mobile Cranes** and the **NZ Approved Code of Practice for Cranes**.

> **Not legal advice; not engineering certification.** A competent crane person validates type
> selection, configuration, ground and lift classification against the actual crane and site.
