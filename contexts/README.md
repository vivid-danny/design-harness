# Contexts

A context pack holds everything true about one product. The harness itself (`AGENTS.md`, `quality.md`, `skills/`) holds everything true about how Danny works. Swapping packs is how the same harness designs for Vivid Seats Web one day and an internal tool the next without dragging Vivid's palette and voice along.

## Packs

| Pack | Product | Figma library |
|---|---|---|
| `vivid-web/` | Vivid Seats consumer web | VS Web Design System |

The org runs other libraries that may each become a pack: Vivid Seats App Design System, Distribution Design System (carries a `Partner Config` collection for white-labeled partner sites), PGM Design System, QCI Emails, Transactional Emails.

## What a pack contains

- **`design.md`** is required. Platform facts, token reference, component selection table, domain logic, accessibility specifics, assets, open conflicts, and the Figma file key plus library key for scoping searches.
- **`tokens/`** with the `variables.css` files the prototypes import.
- **`assets/`** with fonts, logos, and icons.

A pack with no `design.md` is not a pack. The agent will not infer one.

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
