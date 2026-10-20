# Design Reference (Vivid Seats web)

Read this before designing anything. **Source of truth: vivid-web-athena** (snapshot in `tokens/`). Guidance that Athena's code can't express (philosophy, selection rules, domain logic) is condensed from the Vivid Seats Web Design System export. Where the two disagree, Athena wins and the disagreement is listed under **Open conflicts**.

Snapshot taken from Athena: 2026-10-02. Re-sync with `scripts/sync-tokens.sh` (optional).

## 1. Philosophy
- **Reuse before invent.** Compose existing components. If nothing fits, that is a tracked gap: stop and raise it with options and a recommendation. Never build a local lookalike.
- **Tokens only.** No raw hex, px or rem in prototype CSS. If a value has no token, say so instead of minting one.
- **Clarity beats cleverness**, especially around payment, fees, legal and support copy.
- **Don't invent data.** Tiers, labels, fee rules and prices come from a spec or a fixture, never from imagination.
- **Light only.** Web has no dark mode. Hover states exist on web.
- **Accessibility is baseline**, not polish: WCAG 2.1 AA (section 6).
- Brand voice: relatable, reliable, energetic, entertaining, plugged in. Let it be felt, not stated.

## 2. Tokens
Files in `tokens/`. In prototypes, import the `variables.css` files; do not hardcode the values below.

| Set | File | Names |
|---|---|---|
| Semantic colors | `tokens/semantic-colors/variables.css` | `--text-*`, `--links-*`, `--surface-*`, `--primary-*`, `--secondary-*`, `--tertiary-*`, `--background-*`, `--status-*`, `--shadow-*`, `--transparencies-*` |
| Primitive colors | `tokens/primitive-colors/variables.css` | `--gray-*`, `--magenta-*`, `--blue-*`, ... (prefer semantic) |
| Spacing and radius | `tokens/layout-tokens/variables.css` | `--spacing-*`, `--radius-*` |
| Type scale | `tokens/config/typography.json` | no CSS vars; see section 3 |
| Breakpoints, elevation, z-index | `tokens/scss/` | SCSS only (`$breakpoint-*`, `$elevation-*`, `$z-index-*`) |

### Color (semantic)
- **Text:** `--text-primary` #04092C, `--text-secondary` #717488, `--text-disabled` #A0A2B3, `--text-contrast` #FFF.
- **Links:** `--links-enabled` #CE3197, `--links-pressed` #8F1564, `--links-disabled` #D3D3DC.
- **Surfaces:** `--surface-background` #F6F6FB, `--surface-divider` #D3D3DC, `--background-default` #FFF, `--background-off-white` #EFEFF6, `--background-backdrop` #04092C99.
- **Primary (magenta):** lightest #FBE5F3, light #F7B4DF, **main #CE3197**, dark #8F1564, darkest #440C36, plus `-contrast`, `-interaction-hover` and `-interaction-selected`.
- **Secondary (teal):** main #13BDC3, dark #1C94A5, darkest #086E88, lightest #DAFAFB, light #B5F5F8.
- **Tertiary (purple):** main #5D50CB, dark #312784, darkest #211A58, lightest #F2F0FF, light #D9D6FD.
- **Status** (`--status-{kind}-{light|main|dark|contrast}`): warning main #FE894E, error main #DC1818, info main #277CF4, success main #19AA61.
- **Shadow:** `--shadow-default-weak` #4E516240, `--shadow-default-strong` #4E51624D.
- Every brand palette also has `-interaction-hover` (4% alpha) and `-interaction-selected` (8% alpha) for state overlays.

### Spacing, radius
- `--spacing-` none 0, 2xs 0.125rem, xs 0.25rem, sm 0.5rem, md 0.75rem, lg 1rem, xl 1.5rem, 2xl 2rem, 3xl 2.5rem, 4xl 3rem, 5xl 3.5rem.
- `--radius-` none 0, sm 0.25rem, md 0.5rem, lg 1rem, rounded 62.5rem.

### Breakpoints, elevation, z-index (SCSS only, mirror the values in CSS)
- Mobile-first. M = 48rem (768px), L = 64rem (1024px), XL = 90rem (1440px). Under 768px is "S".
- Elevation 0 to 4: offsets 0, 1/4, 2/8, 3/12, 4/16px blur on gray-600 at about 25-30% alpha.
- Z-index: fab 1000, toast 1100, tooltip 2000, dropdown 4000, backdrop 5000, banner 5050, nav 6000, sheet 6050, modal 7000, spinner 8000, alert 9000.

## 3. Typography
Font: **GT Walsheim** (fallbacks: Poppins, Helvetica, Arial, sans-serif). Weights used: 400, 500, 700, 800. Source: `tokens/config/typography.json`.

| Role | Size / line height | Weight |
|---|---|---|
| title-xxl | 40 / 50 | 800 |
| title-xl | 32 / 40 | 800 |
| title-lg | 24 / 30 | 800 |
| title-md | 20 / 25 | 700 |
| title-sm | 18 / 22.5 | 700 |
| subtitle-xxl / xl / lg / md / sm | 32/40, 24/30, 20/25, 18/22, 16/20 | 400 |
| body-regular / medium / bold | 16 / 24 | 400 / 500 / 700 |
| body-link | 16 / 24, underlined | 400 |
| small-regular / medium / bold | 14 / 21 | 400 / 500 / 700 |
| caption-regular / medium / bold | 12 / 18 | 400 / 500 / 700 |
| overline | 12 / 15, letter-spacing 0.075rem | 700 |
| footnote-regular / bold | 10 / 15 | 400 / 700 |

Also defined: `creditCardLabel` 14px/500 and `stepLabel` 16px/500. Do not trust the SCSS `$text-size-*` constants; they don't match this JSON.

## 4. Components: pick by the job
Athena's design system lives in `src/design-system/components/`. Check there first, then for a variation of an existing component, and only then treat it as a gap.

| If the job is... | Athena component | Not |
|---|---|---|
| Commit an action | **Button** (`color`: primary, secondary, neutral; sizes small 32 / medium 40 / large 48px). One primary per view. Single-line, Title Case labels | a Chip |
| Filter or select within a shown set | **Chip** (toggle filters; needs `aria-pressed`) | a Button |
| Enter text | **Textfield** | a Chip |
| Binary or choice controls | **Checkbox**, **Radio / RadioButtonGroup**, **Toggle** | bespoke controls |
| Image-led tappable item | **Card** (image card with overlay, small variant), **CardPill** | a hand-rolled tile |
| Horizontal set of cards | **Carousel** | a custom scroller |
| Blocking decision | **Dialog**; viewport-adaptive: **AdaptiveModal**; side or bottom surface: **Drawer** | a toast |
| Inline notice | **Alerts** (error, info, success, warning) | a custom banner |
| Loading | **Skeleton** (content), **Loader** (spinner) | a custom spinner |
| Hints | **Tooltip** | a dialog |
| Navigation aids | **Tabs**, **Breadcrumbs**, **Pagination**, **Stepper** | tabs for steps |
| Layout and type | **Box**, **Typography**, **Divider** | raw MUI imports |

**Not covered by this table yet:** Badge, List Item, Search List Item, top Navigation bar, Footer, Filter Row, Sheet, Dropdown Menu, Toast. Navigation, footer, sheet and menu exist in the real design system and are candidates to port into this file on a later run. Until then, use the Figma library for them (section 8) and don't invent lookalikes.

Rules worth keeping from the export:
- One primary button per view. Irreversible actions need a confirmation dialog. A loading button shows a spinner.
- Chips filter, buttons commit, badges label. Don't swap them by look.
- Body-copy links keep a persistent underline; breadcrumb links reveal an underline on hover.
- Icons: prefer unfilled (regular). Decorative icons next to text get `aria-hidden`.

## 5. Domain logic
**Deal Score** (ticket listings only, 0-10 scale, never a general badge):

| Score | Tier |
|---|---|
| 10.0 exactly | Fantastic |
| 9.0 - 9.9 | Excellent |
| 8.0 - 8.9 | Great |
| 7.0 - 7.9 | Very Good |
| < 7.0 | render nothing |

There is no "Good" tier. Exactly 10.0 is reserved for the single best deal, usually one per production: never sprinkle Fantastic across a list. When unsure, use Excellent. Never invent or approximate values.

**Money:** format with the correct currency and locale; never hand-format prices. **Assets:** no new images in the repo; CDN images via Cloudinary (`media.vsstatic.com`, with `f_auto,q_auto,w_*,dpr_auto`).

## 6. Accessibility baseline (WCAG 2.1 AA)
- Native `<button>` for actions; never `onClick` on a `<div>`.
- Toggle buttons and chips: `aria-pressed`. Native controls use `disabled`; only custom focusable controls use `aria-disabled`. Never both.
- Visible focus on everything focusable: `outline: 2px solid currentColor; outline-offset: 2px`. Never `outline: none` without a replacement.
- Meaningful icons: `role="img"` plus `aria-label`. Decorative icons: `aria-hidden="true"`.
- Everything reachable and operable by keyboard.

## 7. Open conflicts (Athena wins; resolve with the design system team)
1. **CTA color (resolved).** The export says cobalt #1C6CDC is the CTA color and magenta never goes on controls. Wrong for web: cobalt exists only as a primitive token, not a semantic one. **Primary and CTA color is magenta** (`--primary-main` #CE3197). Never use cobalt for primary actions.
2. **Token names and type scale.** Export uses `--vs-*` tokens and a root-phi type scale; Athena uses `--spacing-*`, `--radius-*`, the px scale above. Use Athena's.
3. **Extra-bold weight.** Athena's title-lg/xl/xxl use weight 800, but the only fonts available are Regular (400), Medium (500), Bold (700) and Black (900) in `assets/fonts/`. Treat 800 as **Black**: declare Black at `font-weight: 900` and CSS font matching resolves a 800 request to the heavier face. Unconfirmed with the design system team, so don't hardcode 900 in prototypes; keep using the 800 value from the type scale.
4. **Components in the real design system but not yet in this file** (section 4): deferred to a later run.
5. **Athena's own stale doc:** `docs/onboarding/06-design-system.md` cites `$spacing-md` and `$font-size-base`, which don't match real tokens. Ignored.

## 8. Figma design system
The component reference for **concepts generated in Figma** is the VS Web Design System library: <https://www.figma.com/design/QITaTxYPUrqmzzB6NVayVu/VS-Web-Design-System?node-id=6257-105208> (file key `QITaTxYPUrqmzzB6NVayVu`). It has components for everything in section 4, including the ones not yet captured here. This file deliberately does not copy the whole design system; Figma is the source for component structure, this file is the source for rules and token values.

## 9. Assets
`assets/` (from the Vivid Seats asset pack): `fonts/` GT Walsheim woff2, `icons/` SVGs named `icon{Name}.svg`, `logos/` wordmark, brandmark and monochrome variants. Use these as-is; don't redraw icons or logos.

## 10. Not covered yet
Page layouts (performer, checkout, event/seat-map), motion tokens, and map colors. Add when a prototype needs them.
