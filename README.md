# Distilling Design Excellence

For anyone to help them better collaborate with agents and generate better interfaces. Agents left on their own will not produce high quality interfaces. They need context and clear rules for how to execute. The goal of this harness is to make the outputs handled by agents more consistent and better than without.


## What it is for

This harness helps navigate the different needs and stages of the product design process. The harness meets you where you are currently at and helps execute at a consistent quality bar.

At the moment, this harness supports design production. This includes generating Figma mockups, creating components, documentation, and prepping assets for handoff.

This harness will change over time to accommodate more parts of the product process.

## How it is put together

Three layers to help an agent work through the various stages of design.

| Layer | File | What belongs there |
|---|---|---|
| Standards | `quality.md` | Baseline checks to help determine when something is done. |
| Behavior | `AGENTS.md`, `skills/` | Process, tool reach, and prohibitions for the agent. |
| Context | `contexts/<pack>/` | Foundational rules and resources for a specific product or surface. |

The test for a new rule: if it names a color, a typeface, or a domain concept, it belongs in a context pack. If it would be wrong on an internal tool, it belongs in a context pack.

This matters because not everything I design is Vivid Seats branded. Internal tools and partner sites get no Vivid spin.

## Running it

Give the agent a brief. It will state the context and the path before it builds anything. If the brief does not make the context obvious, it asks. It never assumes which product or company is being used for.


## References

```
CLAUDE.md      symlink to AGENTS.md (Claude Code loads it by name)
AGENTS.md      how the harness behaves, plus how to talk to me
quality.md     the bar a component clears before it's done
skills/        the process, loaded per phase
contexts/      packaged product contexts for quickly establishing a visual language (tokens, assets, design reference)
evals/         briefs to refine this harness over time
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

`evals/` holds fixed briefs with known-good outcomes. Re-run one after changing a rule to find out whether the change helped. Without that, every edit to `AGENTS.md` is a guess.

## Credit

The harness pattern comes from [Will Newton](https://x.com/willdjthrill/status/2098205382195953873). The divergence-axis rule and the prose linter are adapted from [Emil Kowalski](https://github.com/emilkowalski/skills) and [Blake Cyze](https://github.com/blakecyze/skills).
