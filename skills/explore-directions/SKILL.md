---
name: explore-directions
description: Generate multiple distinct design directions in Figma using a design system library. Use when a concept needs exploring before committing, when the user asks for options or directions for a screen or component, or when a chosen direction needs refining into states and detail. Enforces a named divergence axis per direction.
---

# Explore Directions

Produce directions Danny can choose between. The value is the divergence. Three versions of one screen with small modifications teaches him nothing and wastes the review.

**This is exploration, not production.** See the two kinds of work in `AGENTS.md`. Draw what the comparison needs and stop there. Detail spent on a direction that gets dropped is detail wasted, and it buries the comparison the exploration exists to give him. Production detail arrives after Danny picks, as a separate run.

Read `AGENTS.md` and the active context pack's `design.md` before starting. `production-quality.md` is a production gate and doesn't apply here. `design-quality.md` does, from the first frame. Load the `figma:figma-use` skill before any `use_figma` call, and `figma:figma-generate-design` when building a full screen.

## Phase 1: Ground the work

Before touching Figma, know four things:

- **The design system.** Which library, and its library key for scoping searches.
- **The surrounding context.** Where this renders, against what background, beside what neighbors, at what sizes.
- **The real material.** A live component, a production screenshot, or a Figma frame. Per `AGENTS.md`, don't start from a blank page.
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
- **One line per direction. No second sentence.** The frames carry the argument. If the axis needs a paragraph to explain, it isn't an axis yet.
- **No two directions share an axis position.** If two differ only in accent color, spacing, or copy, they are one direction. Replace one with a real alternative.
- Sharing the pack's tokens is not convergence. Every direction should look like it could ship in this product.

**Completion check:** every direction has a name and a stated axis, and no two sit at the same position on their axis. If you can't state the axis in a phrase, you don't have a direction yet.

## Phase 3: Build in Figma

- **Scope every `search_design_system` call to the active pack's library key** via `includeLibraryKeys`. Unscoped searches return components from every library in the org, so you will instantiate the wrong product's button without noticing.
- Instantiate library components and bind fills, spacing, and type to the library's variables. Never rebuild an existing component from rectangles and text.
- Place work inside a Section or Frame, never loose on the canvas. Check for an existing page before creating one.
- Never edit the design system library file. Work in a separate file or page.
- Each direction gets its own frame, labeled with its name and a one-line axis so the canvas is readable without the chat. That label is the only text you add to the canvas. No rationale paragraphs, no notes section, no summary block.

**When the library has nothing that fits:** compose from existing components and tokens, keep going, and record what you fabricated. Component gaps are normal, not an error state. Don't stall for permission.

**Content realism.** Real names, plausible numbers and dates, strings at the length they occur in the product. Placeholder text hides every layout problem you are trying to find. Domain values (scores, tiers, fee rules, status labels) come only from the context pack or a fixture the user supplied.

**States are optional here, and the brief decides.** The resting state is the floor. Draw more when the direction lives in them: an interaction concept, a selection model, a tray that only exists open. Draw fewer, or just the one, when the comparison is about layout or hierarchy and a state matrix would only pad the canvas. A full set of hover, focus, active, and disabled is production work, so reach for it when asked and not by reflex.

## Phase 4: Look at it

Screenshot each direction and inspect it. Check alignment, spacing, and whether the direction still reads as the axis you named.

Real content at real length is the one production concern that belongs here, because a direction that only holds at placeholder length isn't a direction. Everything else in `production-quality.md` waits for the production run.

Iterate at most three times, then report. If a direction isn't working after three passes, say that rather than polishing it quietly.

**If two directions converged while you built them, cut one and say so.** Two distinct directions beat three padded to look like a set.

## Phase 5: Hand off

Short. A table, then the file location. The handoff explains what's on the canvas, it doesn't re-argue it, and no cell runs past a line:

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
