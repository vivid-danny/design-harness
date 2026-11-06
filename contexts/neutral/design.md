# Neutral

Design reference for work with no product design system behind it: greenfield concepts, internal tools, and prototypes where the visual language hasn't been decided. It supplies three things and deliberately no more: a token set, a type scale, and the accessibility baseline. Everything a real pack knows about its product, this one leaves to the brief.

**Source of truth: nothing.** Every value here was written for the pack. It is not an export, not a snapshot, and not derived from a shipping product. That is the point and also the limit (see section 5).

**Figma library:** none. `search_design_system` has nothing to return for this pack, so don't call it. Work in code, or build Figma frames from these tokens by hand and say that's what you did.

**When this pack is active:** only when it has been named. The rule in `README.md` still holds. If the brief leaves the product unclear, ask. This pack is what you reach for when the answer is "there isn't one," not a fallback you pick because asking felt slow.

## 1. Tokens

Files in `tokens/`. Import the `.css` files; don't hardcode the values below.

| Set | File | Names |
|---|---|---|
| Colors | `tokens/colors.css` | `--text-*`, `--links-*`, `--surface-*`, `--background-*`, `--primary-*`, `--status-*`, `--shadow-*`, plus `--gray-*` / `--accent-*` primitives |
| Spacing and radius | `tokens/layout.css` | `--spacing-*`, `--radius-*` |
| Type scale | `tokens/typography.css` | `--font-family`, `--{role}-font-size`, `-font-weight`, `-line-height` |
| Breakpoints, elevation, z-index | `tokens/scss/` | SCSS only (`$breakpoint-*`, `$elevation-*`, `$z-index-*`) |

**Names match `vivid-web` on purpose.** Same variable names, same spacing and radius values, same breakpoints and z-index order. Work built in this pack can be re-pointed at a real pack by swapping the imports, with no find-and-replace through the markup. What differs is color and type.

### Color
- **One accent, no secondary or tertiary.** `--primary-main` #1D54C4 carries every primary action, link, and selected state. There is no second brand hue on purpose; if the work needs one, it needs a real pack.
- **Text:** `--text-primary` #18181B, `--text-secondary` #52525B, `--text-disabled` #9A9AA4, `--text-contrast` #FFF.
- **Surfaces:** `--background-default` #FFF, `--background-off-white` / `--surface-background` #F7F7F8, `--surface-divider` #DCDCE0, `--background-backdrop` #18181B99.
- **Status** (`--status-{error|warning|success|info}-{light|main|dark|contrast}`): error #C02626, warning #B45309, success #156F3F, info reuses the accent.
- `--primary-interaction-hover` (4% alpha) and `-interaction-selected` (8% alpha) are the state overlays, same convention as `vivid-web`.

### Spacing, radius
`--spacing-` none 0, 2xs 0.125rem, xs 0.25rem, sm 0.5rem, md 0.75rem, lg 1rem, xl 1.5rem, 2xl 2rem, 3xl 2.5rem, 4xl 3rem, 5xl 3.5rem. `--radius-` none 0, sm 0.25rem, md 0.5rem, lg 1rem, rounded 62.5rem.

### Breakpoints, elevation, z-index (SCSS only)
M 48rem (768px), L 64rem (1024px), XL 90rem (1440px). Elevation 0 to 4 on gray-900 at 8 to 14% alpha. Z-index order matches `vivid-web` exactly.

## 2. Typography

Font: **system stack** (`-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, Roboto, Helvetica, Arial, sans-serif), plus `--font-family-mono` for IDs, codes, and tabular values. No font files, no licensing question, no `assets/fonts/`.

| Role | Size / line height | Weight |
|---|---|---|
| title-xxl | 40 / 48 | 700 |
| title-xl | 32 / 40 | 700 |
| title-lg | 24 / 32 | 700 |
| title-md | 20 / 28 | 600 |
| title-sm | 18 / 24 | 600 |
| body-regular / medium / bold | 16 / 24 | 400 / 500 / 700 |
| small-regular / medium / bold | 14 / 20 | 400 / 500 / 700 |
| caption-regular / medium / bold | 12 / 16 | 400 / 500 / 700 |
| overline | 12 / 16, letter-spacing 0.075rem | 700 |

No `subtitle-*` and no `footnote-*`. Both exist in `vivid-web` to serve marketing and legal copy this pack has no equivalent of. If the work needs a subtitle role, use `title-sm` at weight 400 and say you did.

## 3. Accessibility

The baseline in `AGENTS.md` applies, WCAG 2.2 AA. Specific to this pack:

- **Contrast is checked, not assumed.** Every `main` and text value in section 1 clears 4.5:1 on `--background-default`: text-primary 16.9, text-secondary 7.7, primary-main 6.7, error 5.9, warning 5.0, success 6.2. `--text-disabled` is 2.8 and is only valid on inactive controls, which WCAG 1.4.3 exempts. Don't use it for low-emphasis live text.
- Visible focus: `outline: 2px solid currentColor; outline-offset: 2px`. Never `outline: none` without a replacement.
- Native controls use `disabled`. Only custom focusable controls use `aria-disabled`. Never both.
- Selected state must be distinguishable without perceiving hue. With one accent against a grayscale this matters more here than in a multi-hue pack, so pair the accent with weight, a border, or an icon.

## 4. Components

No component library, so there is no selection table. Compose from semantic HTML and the tokens above: a real `<button>` for actions, `<a href>` for navigation, a labeled `<input>`, `<dialog>`, `<details>`, `<table>` with `<th scope>`. The rule in `AGENTS.md` holds: don't rebuild out of divs what the platform already gives you.

**Before calling anything done:** run it against `../../production-quality.md` and `../../design-quality.md`.

## 5. Open conflicts

**No one approved these values.** The colors and the scale were chosen when the pack was written, not exported from a product, so there is no team to confirm them against and no code they already match. That caps what the pack can produce: concepts, prototypes, and explorations. **Never ship a production handoff from it.** If an engineer is going to implement the work, it needs a real design system first.

The tokens-only rule in `AGENTS.md` applies here exactly as it does in a product pack. These tokens are the vocabulary; if a design needs a value they don't cover, stop and say so rather than adding one on top.

## 6. Deliberately empty

A real pack carries platform facts, brand voice, domain logic, assets, and a reference set. This one carries none of them, because a baseline that guesses at them is worse than one that asks.

- **Platform facts, audience, density, voice:** the brief supplies these. If it doesn't, ask before the first frame.
- **Domain logic:** none. Every label, price, status, and score in work built here is placeholder and must be marked as placeholder. Real domain logic is a signal the work belongs in a product pack.
- **Assets:** none, no logos and no icon set. For icons use an unmodified open set (Lucide, Phosphor, or the platform's own) and name which one.
- **Reference set:** no ring 1. `gather-references` gets nothing from this pack; the brief names the references or there aren't any.
- **Also missing:** motion tokens, chart colors (use the `dataviz` skill's palette and say so), dark mode.
