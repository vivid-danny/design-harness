# Contexts

A context pack holds everything true about one product. The harness itself (`AGENTS.md`, the two quality files, `skills/`) holds everything true about how Danny works. Swapping packs is how the same harness designs for Vivid Seats Web one day and an internal tool the next without dragging Vivid's palette and voice along.

## Packs

| Pack | Product | Figma library |
|---|---|---|
| `vivid-web/` | Vivid Seats consumer web | VS Web Design System |
| `neutral/` | None. Unbranded work with no design system | none |

The org runs other libraries that may each become a pack: Vivid Seats App Design System, Distribution Design System (carries a `Partner Config` collection for white-labeled partner sites), PGM Design System, QCI Emails, Transactional Emails.

## What a pack contains

- **`design.md`** is required. Platform facts, token reference, component selection table, domain logic, accessibility specifics, assets, open conflicts, and the Figma file key plus library key for scoping searches.
- **A reference set** in `design.md`, where the pack has competitors worth naming: who they are and which adjacent industries share the mechanics. `gather-references` reads it and holds no product names of its own. Internal tools often have no ring 1 at all, which is worth stating rather than leaving blank.
- **`tokens/`** with the `.css` files the prototypes import, plus whatever a token group needs that CSS variables can't carry. For `vivid-web` that is `scss/`, because media queries can't read `var()` so breakpoints have no CSS equivalent.
- **`assets/`** with fonts, logos, and icons.

A pack with no `design.md` is not a pack. The agent will not infer one.

## The neutral pack

`neutral/` is the pack for work that has no product behind it: greenfield concepts, internal tools, prototypes. It carries a token set, a type scale, and the accessibility baseline, and deliberately nothing else: no platform facts, no voice, no domain logic, no assets, no references. Its token names mirror `vivid-web`, so work built on it can be re-pointed at a real pack by swapping imports.

It is not a default. The rule below still applies: name the pack, and ask when the brief leaves it unclear. `neutral/` is what you use when the answer comes back "there isn't one," never a fallback picked because asking felt slow. Its values were written for the pack rather than taken from a product, so nothing built on it is a production handoff.

## Adding a pack

Start from real material. Screenshots of the live product, a URL, an existing Figma file, or an exported token set. Never invent a visual language from nothing, and never seed a new pack by copying another product's values.

If the product has no design system at all, say so and ask for material rather than designing from a blank page.

## Rules for the agent

- Name the active pack before building. If the brief and project goals leave it unclear, ask.
- Read only the active pack. Don't borrow components, tokens, or voice across packs.
- Scope every `search_design_system` call to the active pack's library key. Unscoped searches return components from every library in the org.
- Non-branded work gets no brand spin. An internal tool does not inherit consumer brand voice or a consumer palette because that's the pack you used last.

## Why packs are files, not skills

A pack looks like it could be a skill: a description, some instructions, a folder of resources. It isn't one, on purpose. Skills get selected when their description matches the request, and the first rule here is that the agent names the pack and asks when the brief leaves it unclear. Matching on "this sounds like consumer web" is the inference that rule exists to prevent.
