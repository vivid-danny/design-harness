# Rules

How to behave in this harness. Read this, `quality.md`, and the active context pack before touching anything. If they ever disagree with something you "know" about a product, these files win.

Nothing in this file is product-specific. Product facts (tokens, components, brand, platform constraints) live in `contexts/`. If a rule here names a color, a typeface, or a domain concept, it's in the wrong file.

## Context

**Name the active context pack before you build.** Say which one you're using, in the same breath as the path you're taking.

- The brief or the project goals usually make it obvious. If they don't, ask. Never assume Vivid Seats.
- The context pack is the source for tokens, components, brand voice, and platform constraints. `contexts/README.md` covers what a pack holds and how to add one.
- **Non-branded work gets no brand spin.** Internal tools and partner sites that aren't Vivid branded don't inherit Vivid's palette, typeface, or voice.
- **No existing design system?** Ask for real material: screenshots, a live URL, a Figma file. Don't invent a visual language from nothing and don't reach for another context's.

## Workflow

1. **Read `quality.md` and the context pack's `design.md`.** `design.md` has the facts: tokens, type scale, component choices, open conflicts. `quality.md` has the bar: the states a component has to survive before it's done.
2. **Start from real material.** Prefer a live product component or a Figma frame over a blank page. Ask for the source if none is given.
3. **Explore a range, then narrow.** Produce a few distinct directions side by side. Don't polish until one is chosen.
   - **Each direction needs a name and a divergence axis, stated before anything is drawn.** The axis is what the direction answers differently: layout, density, hierarchy, interaction model, how much it asks of the user. Name directions for what they are ("Dense", "Editorial", "Guided"), never "Option A/B/C".
   - **No two directions occupy the same axis position.** Three versions of one screen with small modifications is a failed exploration, not three options. If two collapse into each other while you build, cut one and say so.
4. **Never delete an exploration.** A direction dropped for this problem may fit a different one later. Mark it as not pursued (caption, gray out, collapse) instead of removing it, in Figma and in conversation.
5. **Build to fidelity.** Interactive states are part of the design, not a later pass. Specify hover, focus, active, and transitions rather than implying them.
6. **Show, don't claim.** Look at the real thing before saying it works, and check it against `quality.md` section 1 rather than just the happy path. Screenshots for Figma.

## Hard rules

- **Tokens only.** No raw hex, px, or rem. Use the variables the active context provides. If a needed value has no token, stop and say so. Never mint one.
- **Reuse before invent.** Check the context pack's component table and its Figma library first.
- **Composing is allowed; lookalikes are not.** When the design system has nothing that fits, compose from existing components and tokens and keep going. State plainly what you fabricated and what you assumed. Don't stall waiting for permission, and don't quietly rebuild an existing component from rectangles and text.
- **Don't invent data.** Prices, fees, labels, scores, and tiers come from the context pack or a fixture the user supplied. Mark placeholder content as placeholder.
- **Accessibility is baseline, not polish.** WCAG 2.1 AA. Native `<button>` for actions, never `onClick` on a `<div>`. Visible focus on everything focusable. `aria-pressed` on toggles. Labeled meaningful icons, `aria-hidden` on decorative ones. Keyboard reachable and operable throughout.
- **One primary action per view.** Button labels are single-line Title Case.
- **Assets as-is.** Use the context pack's icons and logos unmodified. Don't redraw or recolor them.
- **Keep scope tight.** Do what was asked. No unrelated refactors, no extra features.

## Where the work happens

**Figma is the default venue for exploration.** Two reasons, both about the environment rather than preference:

1. Engineers here accept Figma designs. UI pull requests have been submitted and ignored, so a code artifact doesn't shorten the handoff.
2. The production front-end is cumbersome to explore in. A code variation means rebuilding production from scratch rather than editing it, which makes code exploration expensive here rather than cheap.

Code exploration is still a real option when the user asks for it, and it's worth suggesting when the goal is user testing, where real interaction carries information a frame can't. The code path isn't defined in this harness yet. Say so rather than improvising one.

## Working in Figma

- **Component reference is the active context pack's Figma library.** Instantiate its components and bind to its variables. Don't draw lookalikes from rectangles and text.
- **Scope every design system search to that library's key.** `search_design_system` searches every library in the org at once, so an unscoped search returns components from the wrong products. Pass `includeLibraryKeys`.
- Load the `figma:figma-use` skill before any `use_figma` call. For building full screens from code or a description, also load `figma:figma-generate-design`.
- Place work inside a Section or Frame, not loose on the canvas. Screenshot after changes, check alignment and spacing, and iterate at most three times before reporting.
- Check for an existing page before creating one.
- Don't edit the design system library file itself. Work in a separate file or page.

## Tone with the user

- Lead with the result or the decision needed. Be brief.
- Flag conflicts between sources instead of silently picking one. Record real ones in the context pack's open conflicts section.
- If a request would need pulling in a lot of outside material (a whole design system, other repos), say so and ask first. The harness is intentionally small.
