# Classifying high energy — the threshold, the quick classifiers, the equations

How to decide whether an energy source is **high energy** (a serious injury or fatality is the
*most likely* outcome of contact) or **low energy** (it is not). Used at step 3 of the method in
`../SKILL.md`. **Not legal advice** — these are decision aids from published research, not
statutory tests.

> **Sources last verified: 2026-09-03.**

## The threshold

The method rests on a study of 500+ injuries in which energy magnitude was estimated **blind to
the outcome**, then compared against actual severity. The distribution is the whole argument:

| Energy magnitude | Most likely outcome |
|---|---|
| **Below ~500 J** | First-aid injury |
| **~500 – 1,500 J** | Medical treatment / lost-time injury |
| **Above ~1,500 J** | **Serious injury or fatality (SIF)** |

**High energy = more than approximately 1,500 joules.** CHASNZ states the NZ figure as
"approximately 1,500 joules or more".

Two things follow, and both are the point of the method:

1. **"Most likely", not "worst possible".** A SIF is remotely possible from almost anything, so
   worst-case reasoning cannot prioritise. Energy magnitude can.
2. **The threshold is a filter, not a score.** 1,600 J and 160,000 J are both high energy and both
   need a direct control. Do not rank hazards by joules.

### Health hazards use a different test

For **chemical, biological, sound, vibration, radiation and thermal exposure**, joules are the
wrong unit. These are high energy when:

- exposure exceeds the **workplace exposure standard (WES in NZ / WES in AU)** for the substance
  or agent; or
- oxygen is reduced below about **16%**; or
- the material is strongly corrosive (**pH below ~2 or above ~12.5**); or
- the exposure is **Immediately Dangerous to Life or Health (IDLH)**.

Involve an occupational hygienist, chemist or other competent person for anything marginal —
see `../../hazardous-substances-specialist/`.

### A unit warning worth knowing

US-sourced energy-based safety material frequently states the threshold as **"500 ft-lb"** while
simultaneously stating **1,500 J**. These are not the same number: 1,500 J ≈ **1,100 ft-lb**, and
500 ft-lb ≈ 680 J. The underlying research and the CHASNZ guide both use **1,500 joules** — work
in **joules** and treat any imperial restatement as suspect.

## Quick classifiers — almost always high energy

Use these first; they cover the large majority of real site hazards without any calculation.
Each is a rule of thumb whose derivation is in the equations below.

| Situation | Why it is high energy |
|---|---|
| **A person at ~1.2 m (4 ft) or more above the surface below** | An average adult body at 1.2 m already exceeds 1,500 J. Measured ground surface to the soles of the feet. |
| **A suspended load** | Anything needing lifting equipment is heavy enough that even ~0.3 m of elevation clears the threshold. Carries **two** energies — gravity *and* lateral motion. |
| **Mobile plant or a vehicle in motion near a person on foot** | Mass alone clears the threshold at walking pace. Assessed **from the point of view of the person on foot**, not the operator. |
| **A vehicle occupant at or above ~50 km/h (30 mph)** | The conservative crash threshold; assessed from the occupants' point of view. |
| **Heavy rotating equipment beyond a powered hand tool** | Rotational energy is hard to compute in the field; treat as high energy by default. |
| **Contact with a surface or substance at ~65 °C (150 °F) or hotter** | Third-degree burns from ~2 seconds of contact. |
| **Any release of steam** | Always exceeds the threshold. |
| **Fire with a sustained fuel source** | Even lightly combustible material burns far above the temperature threshold. |
| **An explosion** | Effectively always. |
| **An unsupported excavation or trench face ≥ 1.5 m (5 ft)** | Soil pressure rises about 2 kPa per 0.3 m of depth (roughly 6 kPa/m); at 1.5 m the face carries around 10 kPa — lethal load in a collapse. |
| **Electricity at or above 50 V** | The recognised threshold for current sufficient to kill. |
| **Any arc flash** | By voltage exposure. |
| **Toxic or radiation exposure at or above the exposure limit** | See the health-hazard test above. |

**When no classifier fits — calculate.** Dropped tools, materials at height, hoses under pressure,
powered hand tools and small components are high energy under *some* conditions and not others.
This is exactly where guessing goes wrong in both directions. Use
`../scripts/energy_calculator.py`.

## The equations

All computations in SI. `g` = 9.8 m/s².

### Gravity — potential energy of a raised mass
```
E = mass (kg) × height (m) × 9.8
```
- 90 kg person falling 4.6 m → 90 × 4.6 × 9.8 ≈ **4,057 J — high energy**
- 0.45 kg tape measure dropped 3 m → 0.45 × 3 × 9.8 ≈ **15 J — low energy**

The second example is the one people get wrong. A dropped tape measure can injure; it is not a
SIF hazard, and treating it as one dilutes the whole method.

### Motion — kinetic energy of a moving mass
```
E = 0.5 × mass (kg) × velocity (m/s)²
```
1 m/s = 3.6 km/h. Energy grows with the **square** of speed — halving speed quarters the energy.

- 1,200 kg vehicle striking a worker at 11 m/s (40 km/h) → **≈ 72,600 J — high energy**
- Two workers carrying a 100 kg pipe walking into someone at 1.34 m/s → **≈ 90 J — low energy**

### Electrical
Assumes a human body resistance of 1,500 Ω and that all energy dissipates as heat.
```
E = time (s) × voltage (V)² / 1500        or       E = time (s) × current (A)² × 1500
```
- 220 V contact for 2 s → ≈ **65 J** — *low energy by this calculation*
- 10 kV arc flash for 0.05 s → ≈ **3,333 J — high energy**

**Read the first result carefully.** A 220 V contact computes below the threshold yet plainly
kills people — because the mechanism of electrical death is **ventricular fibrillation from
current across the heart**, not thermal energy deposition. This is a known limit of the energy
model. Use the **≥ 50 V classifier** for electrical work, not the equation, and treat the
calculation as informative only. Route to `../../electrical-energy-specialist/`.

### Pressure — stored energy in a vessel or line
Pressure in psi by convention (1 psi = 6.89 kPa); 1 J = 1 Pa·m³.
```
Vessel:  E = 7000 × pressure (psi) × 0.001 × volume (L)
Pipe:    E = 7000 × pressure (psi) × π × (0.5 × diameter (m))²      [per metre]
```
- 10 L acetylene cylinder at 250 psi → **≈ 17,500 J — high energy**
- 50 mm gas line at 40 psi → **≈ 550 J — low energy**

### Mechanical — rotation and elastic storage
```
Rotation:               E = 0.5 × I × ω²
  rotational inertia    I = 0.33 × mass × length²   (rod, rotating about one end)
                        I = 0.5  × mass × radius²   (cylinder, about its axis)
  angular velocity      ω (rad/s) = rpm × 0.104
Tension / compression:  E = 0.5 × k × distance²      k in N/m
```
- 0.3 kg grinder wheel, 114 mm diameter, 11,000 rpm → **≈ 320 J — low energy**
- Cable extending 0.25 m under 4,448 N (k ≈ 17,800 N/m) → **≈ 556 J — low energy**

Both surprise people. A grinding wheel below the threshold is still perfectly capable of a
serious laceration — **low energy does not mean safe**, it means *not most-likely-fatal*, and it
means the hazard is managed through the ordinary risk process rather than as a SIF exposure.

## Scoping rules — what is deliberately excluded

To keep an assessment finite and comparable:

- **Equipment integrity** — the condition of electrical, engine and hydraulic systems inside plant
  — is **out of scope**. Most observers cannot assess it, and guessing produces noise. Ask the
  people who maintain it.
- **Hypothetical, anticipated or speculated conditions** are excluded. Assess **work as observed**.
- One object may carry **more than one** high-energy hazard (a suspended load = gravity + motion).
- Two hazards sharing the **same energy source and the same direct control** are recorded once.
