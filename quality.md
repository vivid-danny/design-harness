# Quality Bar

Two different jobs live in this file. Read it with the active context pack's `design.md`, which has the product facts these checks refer to.

**Section 1 is a gate.** It lists what a component must contain before an engineer or an agent can build it from the artifact alone. Every check is yes or no, answered against the real thing. A check you can't answer against something concrete has not been done.

**Section 2 is a lens.** Hierarchy, color, restraint. None of it is binary and none of it blocks a handoff. Read it while the work is still soft, and again before you show it.

Passing section 1 makes a component buildable. Passing section 2 makes it worth building. Good components are drawn. Great components survive the states nobody drew, which is also what makes them reusable across products instead of only in the screen they were born in.

## 1. Build-ready

The requirement set is not the same for a Badge and a listing Card. Three switches decide which checks apply:

| Switch | On when | Checks |
|---|---|---|
| Contains text | It renders any text, static or passed in | 1.2 |
| Interactive | The user can click, tap, type, focus, or toggle it | 1.3 |
| Renders remote data | Any value arrives from a request rather than a prop | 1.4 |

1.1 applies to everything. A Badge turns on one switch. A listing Card turns on all three.

### 1.1 Every component

- **Width behavior is declared.** Can you point at it? Autolayout with fill and hug set on every frame in Figma, a documented width behavior, or states drawn at more than one width. A frame that looks right only at the width you built it at has one layout rather than a width behavior.
- **Every breakpoint has a stated outcome.** Does the component say what it does at each breakpoint in the context pack, or does it have one layout and a hope?
- **Reflow or scale is a decision.** At the narrower breakpoint, does the layout rearrange, or does everything shrink proportionally? Either can be correct. Unstated is the failure.
- **Nothing escapes at the narrowest supported viewport.** Does anything force horizontal scroll or clip?
- **Fill and hug are deliberate.** For each frame, is the sizing choice one you made, or the default you got?
- **Every value is bound to a token.** Colors, spacing, radius, type. The tokens-only rule lives in `AGENTS.md`; this check is whether the artifact honors it, including the frames nobody looked at twice.

### 1.2 If it contains text

- **Long text.** Does it hold a value at 4x the length you designed for (80 characters, not 20)?
- **Multi-line.** Is the grow/truncate/wrap outcome a decision, not an accident? See the table below.
- **RTL.** Does the layout still work mirrored, in Arabic or Hebrew?
- **Localization.** Does it hold translated labels, which commonly run 30-50% longer than English?
- **Every text element maps to a role.** Is each one set to a named role from the context pack's type scale, rather than a size and weight chosen locally that happens to look close?

Pick the overflow outcome by context. Don't leave it to the browser:

| Context | Default |
|---|---|
| Card or detail surface | Wrap, up to 2 lines, then ellipsis |
| Dense row or list item | Truncate, with the full value available on hover and to screen readers |
| Price, date, seat, section, row, any value the user decides on | Never truncate. Reflow the layout instead |
| Single-line button label | The copy is too long. Shorten the label, don't resize the button |

### 1.3 If it's interactive

**Required for every interactive component:** `default`, `hover`, `focus-visible`, `active`, `disabled`.

Five states, all specified before the component is done. A component missing one isn't styled yet.

**Additions by component type:**

| Component type | Adds |
|---|---|
| Inputs, textareas, selects | `error` |
| Toggles, chips, tabs, radio, checkbox | `selected` or `checked` |
| Buttons that submit or fetch | `pending` |
| Links and navigation | `visited`, where it carries meaning |

Then the checks a list of state names can't make for you:

- **Not color alone.** Can a user distinguish selected from unselected without perceiving hue?
- **No hover on touch.** Does anything important live only in a hover state?
- **Pending blocks and holds.** Does the component refuse a second submission while pending, and keep its footprint when the label becomes a spinner?
- **Keyboard reachable and operable.** Can every action be reached and triggered without a pointer?

**If it accepts input**, error is a separate state from a failed request (1.4). An invalid value is fixed by correction, a failed request by retry.

- Is the error tied to the field programmatically, not just placed near it?
- Does it appear on blur or submit rather than on every keystroke?
- Does the field keep what the user typed, so they can correct it rather than retype it?

Accessibility requirements for these states live in the context pack's `design.md` section 6. The checks above are about whether the states exist and behave.

### 1.4 If it renders remote data

Four moments, each needing a defined outcome: the data is loading, the data is empty, the request failed, part of the set failed.

- **Loading.** Does the user see something during the fetch?
- **Skeleton.** Does the placeholder match the shape of what's arriving, so nothing jumps when it lands?
- **Optimistic or not.** Is updating before the server confirms a stated decision rather than an omission?
- **Timeout.** Is there a defined behavior when the request takes too long?
- **Missing field.** Does it hold up when an expected value doesn't come back?
- **First use.** Is there a state for before the user has added anything?
- **Failure is visible.** Does the failure show in the component, or does it fail silently?
- **Recoverable in place.** Can the user retry without losing context or re-navigating?
- **Layout holds.** Does the component keep its footprint, or does the page collapse around it?
- **Partial failure.** If one item in a set fails, does the rest still render?

This section covers data the component is waiting on, where nothing the user did caused the wait. For an action the user triggered, see `pending` in 1.3. For a value the user typed that didn't validate, see input error in 1.3.

## 2. Craft

Section 1 asks whether the information is there. This section asks whether the result is any good. Same topics, different altitude, and no yes or no answers.

### 2.1 Hierarchy: can you name the reading order?

- **Hierarchy is explicit.** Can you say what gets read first, second, and third? Do size, weight, and color agree with that order, or do two of them argue?
- **The sizes are a decision.** Can you defend every distinct size in the component, or did the count accumulate as elements were added?
- **The text colors are a decision.** Same question. Levels of text color are hierarchy; disabled and inverse are states and don't count toward it.
- **Line length is set rather than inherited.** Does body copy have a measure you chose? Text running the full width of a wide container is tiring to read, and the fix is a max width rather than a smaller size.

### 2.2 Color: is every use of color doing work?

- **The strongest color is on the most important thing.** Does the highest-saturation element on the surface match what you want looked at first? If three things carry brand color, none of them is the primary action.
- **The surface is quiet enough for color to register.** Is most of the component neutral, so color reads as a signal instead of as the background?
- **Meaning holds.** Does each color mean the same thing everywhere? Status colors report status, primary marks the primary action. Neither gets borrowed because a thing needed emphasis.
- **Nothing is colored to fill space.** Can you say what each colored element is telling the user? A tint applied for visual interest is decoration, and it costs you a signal you'll want later.

Contrast is the accessibility baseline in `AGENTS.md`. Whether the states exist is 1.3. This section is about intent.

### 2.3 States that read

- **Default is distinct.** Is each state visibly different from `default`, or does hover read as the resting state with a slight tint on top?
- **Disabled explains itself.** Does the user know why it's disabled and what would enable it?
- **Pending reassures.** Does the waiting state tell the user the system heard them, or does it only stop them from clicking again?

### 2.4 Content that guides

- **Empty states say what would fill them.** Does it give guidance ("No results yet") rather than blank space?
- **Errors say what to do.** Does the message explain what's wrong and the fix, rather than "Invalid"?
- **It survives without the icon.** Does it still make sense without the illustration or icon carrying the meaning?
- **Labels earn their width.** Is every word in the component doing something, or is some of it narrating the interface back to the user?

Copy rules and the linter live in `skills/write-copy/`.

## 3. Not covered yet

Add when a prototype needs it:
- Motion and transition quality (duration, easing, what animates and what doesn't)
- Layout, density and alignment
- Performance (bundle, render, image weight)
