# Mermaid diagram template for bow ties

Mermaid has no native bow tie layout, but a **left-right flowchart** renders one well — preventive
barriers on the left, the top event in the centre, recovery (mitigating) barriers on the right.
Portable: works in any Markdown renderer that supports Mermaid, and can be exported to an image for
a Word document or report. The table in `bowtie-methodology.md` remains the source of truth; this is
the picture.

## Basic structure

```mermaid
flowchart LR
    H([⚠️ HAZARD\nSuspended load])

    subgraph LEFT["← THREATS & PREVENTIVE BARRIERS"]
        direction TB
        T1[Threat: Rigging/sling failure]
        T2[Threat: Operator error]
        T3[Threat: Overload]
        PB1{{PB: Pre-lift rigging inspection}}
        PB2{{PB: Licensed operator + lift plan}}
        PB3{{PB: Rated capacity indicator}}
    end

    TE(["🔴 TOP EVENT\nUncontrolled release\nof suspended load"])

    subgraph RIGHT["CONSEQUENCES & RECOVERY BARRIERS →"]
        direction TB
        C1[Consequence: Fatality / serious injury]
        C2[Consequence: Property damage]
        C3[Consequence: Regulatory action]
        RB1{{RB: Enforced exclusion zone}}
        RB2{{RB: Emergency response plan}}
        RB3{{RB: Incident notification procedure}}
    end

    T1 --> PB1 --> TE
    T2 --> PB2 --> TE
    T3 --> PB3 --> TE

    TE --> RB1 --> C1
    TE --> RB2 --> C2
    TE --> RB3 --> C3

    style TE fill:#cc0000,color:#fff,stroke:#990000
    style H fill:#ff6600,color:#fff
    style PB1 fill:#0066cc,color:#fff
    style PB2 fill:#0066cc,color:#fff
    style PB3 fill:#0066cc,color:#fff
    style RB1 fill:#009933,color:#fff
    style RB2 fill:#009933,color:#fff
    style RB3 fill:#009933,color:#fff
```

## Colour conventions

| Colour | Meaning |
|---|---|
| 🟠 Orange | Hazard |
| 🔴 Red | Top event |
| 🔵 Blue | Preventive barrier |
| 🟢 Green | Recovery (mitigating) barrier |
| White / default | Threat or consequence |

## Showing escalation factors

Branch an escalation-factor node off the barrier it weakens:

```mermaid
flowchart LR
    T1[Threat: Rigging failure]
    PB1{{PB: Pre-lift inspection}}
    EF1[/EF: Inspector rushed\nor not competent/]
    TE(["🔴 TOP EVENT"])

    T1 --> PB1 --> TE
    PB1 -. weakened by .-> EF1

    style PB1 fill:#0066cc,color:#fff
    style EF1 fill:#ffcc00,color:#333
    style TE fill:#cc0000,color:#fff
```

## Tips

- Keep it readable — at most **4–5 threats and 4–5 consequences** in one diagram. For complex
  hazards, split into one diagram per consequence cluster (Format C in `bowtie-methodology.md`).
- In a Word document, export the rendered diagram as an image and embed it.
- In Markdown/README, use the Mermaid code block directly.
- Flag **critical controls** distinctly (e.g. a thicker stroke) so the few load-bearing barriers
  stand out from the supporting ones.
