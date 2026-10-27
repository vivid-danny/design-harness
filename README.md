# Design Harness

A folder an agent reads before it touches anything, so design production work comes out matching how I work instead of the average of a training set.

Brief in, Figma directions out. The agent gathers references, produces directions that diverge, uses real design system components, and says plainly what it had to make up.

## What it is for

Design production and exploration. The less creative work that still deserves the creative process: taking a defined problem and producing directions, then detail.

## What it is not for

- **Research.** Customer and business goals come from the brief. This harness does not discover them.
- **Problem definition.** Bring a brief, not a question.
- **Critiquing my work.** It makes things; it does not grade them.

## How it is put together

Three layers. The split exists so the harness stays mine while the product context swaps underneath it.

| Layer | File | What belongs there |
|---|---|---|
| Standards | `quality.md` | The artifact. When a component is done. |
| Behavior | `rules.md`, `skills/` | The agent. Process, tool reach, prohibitions. |
| Context | `contexts/<pack>/` | One product's facts. Wrong on any other product. |

The test for a new rule: if it names a color, a typeface, or a domain concept, it belongs in a context pack. If it would be wrong on an internal tool, it belongs in a context pack.

This matters because not everything I design is Vivid Seats branded. Internal tools and partner sites get no Vivid spin.

## Running it

Give the agent a brief. It will state the context and the path before it builds anything:

```
Context: vivid-web. Path: full run (references, 3 directions, then your pick).
Brief: a listing row for the seat map panel that makes Deal Score legible at a glance.
```

Paths: full run, directions only, references only, or refine a chosen direction. Code prototyping is not built yet; the agent will say so rather than improvise.

If the brief does not make the context obvious, it asks. It never assumes Vivid Seats.

## Layout

```
CLAUDE.md      loader, plus how to talk to me
rules.md       how the harness behaves
quality.md     the bar a component clears before it's done
skills/        the process, loaded per phase
contexts/      product packs (tokens, assets, design reference)
evals/         fixed briefs for checking whether changes helped
```

### Skills

| Skill | Does |
|---|---|
| `design-run` | Front door. Names context and path, routes the phases. |
| `gather-references` | Competitive examples via Mobbin, or supplied inspiration. |
| `explore-directions` | Directions in Figma, each on a named divergence axis. |
| `write-copy` | Interface copy and handoff prose, checked by a linter. |

## The two rules doing the most work

**Every direction needs a named divergence axis, stated before anything is drawn, and no two directions may sit at the same position.** Three versions of one screen with small modifications is a failed exploration. This is the rule that stops the most common way this work goes mediocre.

**Every design system search is scoped to the active pack's library key.** The org runs six Figma libraries. An unscoped search returns components from the wrong product, and the agent will not notice.

## Keeping it honest

`evals/` holds fixed briefs with known-good outcomes. Re-run one after changing a rule to find out whether the change helped. Without that, every edit to `rules.md` is a guess.

## Credit

The harness pattern comes from [Will Newton](https://x.com/willdjthrill/status/2098205382195953873). The divergence-axis rule and the prose linter are adapted from [Emil Kowalski](https://github.com/emilkowalski/skills) and [Blake Cyze](https://github.com/blakecyze/skills).
