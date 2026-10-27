---
name: design-run
description: Entry point for design production work in this harness. Use when the user brings a design brief, asks for directions or concepts for a screen or component, or asks to explore options. Routes to reference gathering, Figma direction exploration, and copy work, after naming the active context pack and the path it is taking.
---

# Design Run

The front door. Read the brief, name the context and the path, then run the phases that apply.

Read `rules.md` and `quality.md` first. Read the active context pack's `design.md` once the context is settled.

## Before anything else

State two things in one or two lines, then proceed:

```
Context: vivid-web. Path: full run (references, 3 directions, then your pick).
Brief: a listing row for the seat map panel that makes Deal Score legible at a glance.
```

**Context.** Which pack under `contexts/`. The brief or the project goals usually make it obvious. When they don't, ask. Never assume Vivid Seats, and never carry the last project's context into this one.

**Path.** Which of the routes below. Never pick silently.

**Brief.** Restate it in one sentence: what it is, where it lives, what it has to do. A brief you can't restate in one sentence is a brief you don't understand yet.

## Paths

| Path | When | Phases |
|---|---|---|
| **Full run** | A concept needs exploring | `gather-references` → `explore-directions` → stop for the pick |
| **Directions only** | Danny has the references, or they aren't needed | `explore-directions` → stop for the pick |
| **References only** | Danny wants to see how others solved it before committing to anything | `gather-references` |
| **Refine a direction** | A direction is already chosen and needs detail, states, or copy | `explore-directions` on the single direction, plus `write-copy` |

**Code prototyping is not defined in this harness yet.** If the brief asks for a working prototype, say that the code path isn't built and offer the Figma path instead. Don't improvise a playground, don't scaffold a build, and don't produce a single HTML file as a substitute.

## Inputs the brief has to carry

This harness designs. It does not research or define problems.

**Customer and business goals come from the brief.** If the brief has none, say so and ask once rather than inventing them. A direction aimed at a goal you made up is worse than no direction.

**Data comes from the brief or the context pack.** Prices, fees, labels, scores, and tiers are never invented. Mark placeholder content as placeholder.

If the brief is thin on both goals and material, ask for the more important one and get on with the rest.

## Scope

One thing per run. If the brief spans several components ("the whole checkout"), narrow it: pick the piece that unblocks the most, say which and why, and offer the rest as follow-up runs.

## Finishing

Hand off whatever the path produced, then name one concrete next action. Don't recap the phases.

If anything was fabricated (a component the design system doesn't have, a layout with no precedent in the pack), it goes in the handoff by name. Burying it is the failure mode that makes an agent's work untrustworthy.
