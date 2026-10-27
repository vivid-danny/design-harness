# Quality Bar

What separates a good component from a great one. Read this with `design.md` before building, and run a component against section 1 before calling it done.

A component's **appearance** and its **behavior** are separate concerns. Appearance is how it looks in the state you drew. Behavior is what it does in every state you didn't. Good components are drawn. Great components survive the states nobody drew, which is also what makes them reusable across products instead of only in the screen they were born in.

Answer each check below yes or no against the actual component. A check you can't answer against something concrete isn't done, it's an opinion.

## 1. States every component must survive

### 1.1 Empty — what shows when there is nothing to show?
- **No icon.** Does it still make sense without the illustration or icon?
- **No label.** Does it hold up if the expected text is missing?
- **First use.** Does it show something useful before the user has added anything?
- **Placeholder.** Does it give guidance ("No results yet") rather than blank space?

### 1.2 Overflow — what happens when content is longer than expected?
- **Long text.** Does it hold a value at 4x the length you designed for (80 characters, not 20)?
- **Multi-line.** Is the grow/truncate/wrap outcome a decision, not an accident? See the table below.
- **RTL.** Does the layout still work mirrored, in Arabic or Hebrew?
- **Localization.** Does it hold translated labels, which commonly run 30-50% longer than English?

Pick the overflow outcome by context. Don't leave it to the browser:

| Context | Default |
|---|---|
| Card or detail surface | Wrap, up to 2 lines, then ellipsis |
| Dense row or list item | Truncate, with the full value available on hover and to screen readers |
| Price, date, seat, section, row, any value the user decides on | Never truncate. Reflow the layout instead |
| Single-line button label | The copy is too long. Shorten the label, don't resize the button |

### 1.3 Async — what happens while the app is waiting?
- **Loading.** Does the user see something during the fetch?
- **Skeleton.** Does the placeholder match the shape of what's arriving, so nothing jumps when it lands?
- **Optimistic UI.** Does the interface update before the server confirms, where the action is safe to assume?
- **Timeout.** Is there a defined behavior when the request takes too long?

### 1.4 Interactive — does every state read as distinct?
- **The full set.** Hover, focus-visible, active, disabled and selected, all specified. Accessibility requirements for these live in `design.md` section 6; this check is about whether they're visually legible.
- **Not color alone.** Can a user distinguish selected from unselected without perceiving hue?
- **No hover on touch.** Does anything important live only in a hover state?
- **Disabled explains itself.** Does the user know why it's disabled and what would enable it?

### 1.5 Error — a request can fail, not just be slow
- **What shows.** Is the failure visible in the component, or does it fail silently?
- **Recoverable in place.** Can the user retry without losing context or re-navigating?
- **Layout holds.** Does the component keep its footprint, or does the page collapse around it?
- **Partial failure.** If one item in a set fails, does the rest still render?

## 2. Not covered yet

Add when a prototype needs it:
- Motion and transition quality (duration, easing, what animates and what doesn't)
- Copy and microcopy quality
- Layout, density and alignment
- Responsive behavior across the S/M/L/XL breakpoints
- Performance (bundle, render, image weight)
