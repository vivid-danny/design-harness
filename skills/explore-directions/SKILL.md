---
name: explore-directions
description: Generate multiple distinct design directions in Figma using a design system library. Use when a concept needs exploring before committing, when the user asks for options or directions for a screen or component, or when a chosen direction needs refining into states and detail. Enforces a named divergence axis per direction.
---

# Explore Directions

Produce directions Danny can choose between. The value is the divergence. Three versions of one screen with small modifications teaches him nothing and wastes the review.

Read `rules.md`, `quality.md`, and the active context pack's `design.md` before starting. Load the `figma:figma-use` skill before any `use_figma` call, and `figma:figma-generate-design` when building a full screen.

## Phase 1: Ground the work

Before touching Figma, know four things:

- **The design system.** Which library, and its library key for scoping searches.
- **The surrounding context.** Where this renders, against what background, beside what neighbors, at what sizes.
- **The real material.** A live component, a production screenshot, or a Figma frame. Per `rules.md`, don't start from a blank page.
- **The content.** Real names, real prices, real dates from the brief or a fixture. Never invented.

## Phase 2: Name the directions

**Do this before anything is drawn.** State the set as a list, each with a name and an axis:

```
1. Dense: information density. Every fact visible, nothing progressive.
2. Guided: how much the interface decides. Surfaces one recommendation, hides the rest behind a control.
3. Editorial: visual weight of the hero value. The headline number leads at display size, supporting facts recede.
```

**Rules for the set:**

- Default 3. More only when Danny asks. Past 5 the comparison dilutes.
- **Names describe the direction.** "Dense", "Guided", "Editorial", "Compact". Never "Option A/B/C", never "Version 1/2/3".
- **The axis is what the direction answers differently.** Layout, density, hierarchy, interaction model, how much the interface decides for the user, how much the user has to read.
- **No two directions share an axis position.** If two differ only in accent color, spacing, or copy, they are one direction. Replace one with a real alternative.
- Sharing the pack's tokens is not convergence. Every direction should look like it could ship in this product.

**Completion check:** every direction has a name and a stated axis, and no two sit at the same position on their axis. If you can't state the axis in a phrase, you don't have a direction yet.

## Phase 3: Build in Figma

- **Scope every `search_design_system` call to the active pack's library key** via `includeLibraryKeys`. Unscoped searches return components from every library in the org, so you will instantiate the wrong product's button without noticing.
- Instantiate library components and bind fills, spacing, and type to the library's variables. Never rebuild an existing component from rectangles and text.
- Place work inside a Section or Frame, never loose on the canvas. Check for an existing page before creating one.
- Never edit the design system library file. Work in a separate file or page.
- Each direction gets its own frame, labeled with its name and axis so the canvas is readable without the chat.

**When the library has nothing that fits:** compose from existing components and tokens, keep going, and record what you fabricated. Component gaps are normal, not an error state. Don't stall for permission.

**Content realism.** Real names, plausible numbers and dates, strings at the length they occur in the product. Placeholder text hides every layout problem you are trying to find. Domain values (scores, tiers, fee rules, status labels) come only from the context pack or a fixture the user supplied.

**Interactive states are part of the design.** Specify hover, focus, active, disabled, and selected rather than implying them. Draw the states that distinguish the direction; a direction whose whole idea is a selection model has to show selection.

## Phase 4: Look at it

Screenshot each direction and inspect it. Check alignment, spacing, and whether the direction still reads as the axis you named.

Run each direction against `quality.md` section 1. Overflow and empty are the two that most often break a direction that looked fine in the state you drew.

Iterate at most three times, then report. If a direction isn't working after three passes, say that rather than polishing it quietly.

**If two directions converged while you built them, cut one and say so.** Two distinct directions beat three padded to look like a set.

## Phase 5: Hand off

A table, then the file location:

| Direction | Axis | When it wins | What it costs |
|---|---|---|---|
| Dense | Information density | The user is comparing many listings fast | Heavy on a small screen; nothing recedes |
| Guided | How much the interface decides | First-time buyers who don't know what to compare | Hides detail power users want |

Then:
- **Fabrications**, by name. Every component or layout with no basis in the library, and what you assumed building it.
- **Open questions** the directions surfaced.
- Where the work is, as a Figma link.

**Don't pre-pick a favorite.** The choice is Danny's. If he asks which you'd pick, answer with a reason rooted in the product and the audience rather than aesthetics.

**Never delete a direction he passes on.** Caption it as not pursued, gray it out, or collapse it. A direction dropped here may fit a different problem later.
