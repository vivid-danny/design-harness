# Rules

How to behave in this harness. Read this and `design.md` before touching anything. If the two ever disagree with something you "know" about Vivid Seats, these files win.

## Workflow
1. **Read `design.md`.** Tokens, type scale, component choices and open conflicts live there.
2. **Start from real material.** Prefer a live product component or a Figma frame over a blank page. Ask for the source if none is given.
3. **Explore a range, then narrow.** For a concept, produce a few distinct directions side by side. Don't polish until one is chosen.
4. **Never delete an exploration.** A direction dropped for this problem may fit a different one later. Mark it as not pursued (caption, gray out, collapse) instead of removing it — in Figma and in conversation.
5. **Build to fidelity.** Prototypes are real code (`playground/`), not pictures. Real hover, focus and transitions.
6. **Show, don't claim.** Run it and look at it before saying it works. Screenshots for Figma, the dev server for prototypes.
7. **Close the loop.** At the end of a session, propose rule updates from the corrections made (see "Corrections log").

## Hard rules
- **Tokens only.** No raw hex, px or rem in prototype CSS; use the variables from `tokens/`. If a needed value has no token, stop and say so. Never mint one.
- **Primary and CTA color is magenta** (`--primary-main`). Never cobalt, even though a blue primitive exists.
- **Reuse before invent.** Check `design.md` section 4 and the Figma library first. If nothing fits, it is a gap: stop and give options with a recommendation. Don't build a lookalike.
- **Don't invent data.** Deal-score tiers, prices, fees and labels come from `design.md` or a fixture the user supplied. Mark placeholder content as placeholder.
- **Light only.** No dark-mode logic.
- **GT Walsheim only**, from `assets/fonts/`. Treat weight 800 as Black.
- **Assets as-is.** Use `assets/icons` and `assets/logos` unmodified. Don't redraw or recolor them.
- **Accessibility baseline** applies to every prototype (`design.md` section 6): native buttons, visible focus, `aria-pressed` on toggles, labeled icons.
- **One primary button per view.** Button labels are single-line Title Case.
- **Keep scope tight.** Do what was asked. No unrelated refactors, no extra features.

## Working in Figma
- **Component reference:** the VS Web Design System library (`design.md` section 8). When generating concepts, use its components and variables; don't draw lookalikes from rectangles and text.
- Load the `figma:figma-use` skill before any `use_figma` call. For building full screens from code or a description, also load `figma:figma-generate-design`.
- Search the design system (`search_design_system`) and instantiate library components before creating anything custom.
- Bind fills, spacing and type to the library's variables and styles rather than hardcoding values.
- Place work inside a Section or Frame, not loose on the canvas. Screenshot after changes, check alignment and spacing, and iterate at most three times before reporting.
- Check for an existing page before creating one.
- Don't edit the design system library file itself. Work in a separate file or page.

## Working in the playground
- Stack: Vite + React + TypeScript. Each prototype lives in its own folder under `playground/src/prototypes/`; variations are sibling files.
- Import tokens from `tokens/` (the `variables.css` files) and fonts from `assets/fonts/`. Never import from the Athena repo.
- Keep prototypes self-contained so one can move to `vault/` as a single folder.
- When a prototype turns out well, say so. Moving it to `vault/` is the user's call.

## Tone with the user
- Lead with the result or the decision needed. Be brief.
- Flag conflicts between sources instead of silently picking one, and record real ones in `design.md` section 7.
- If a request would need pulling in lots of outside material (whole design system, other repos), say so and ask first. The harness is intentionally small.

## Corrections log
At the end of a session, propose additions here (and to `design.md` if it's a design fact). Show them as a diff and wait for approval. Each entry: what went wrong, the rule that prevents it, and the date. Keep entries short. Prune ones that no longer apply.

<!-- entries below -->
- 2026-10-02 (TODO, revise these instructions): The design system won't have every component, and the harness shouldn't try to cover them all. Make the instructions less directive and more referential. Affected lines: "Reuse before invent" (hard rules), "Don't draw lookalikes" (Working in Figma), and the "Not covered by this table yet" note in `design.md` section 4. Direction: point to the Figma library and tokens as the reference, use library components where they exist, and when one doesn't, compose from tokens and existing components and say what was assumed, instead of stopping.
