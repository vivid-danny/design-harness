# Design Quality


**This file applies to both kinds of work.** An exploration and a production build are judged by the same craft questions. `production-quality.md` asks whether the information is there, which only a decided component owes. This file asks whether the result is any good, which a direction owes from the first frame.

Read this document with the active context pack's `design.md`, which has the product facts these questions refer to.

**The one exemption is deliberate low fidelity.** When Danny asks for wireframes, a greybox, or a sketch, hierarchy still applies and the rest waits. Low fidelity is a request, never a default, and never something you decide to deliver on your own.

## 1. Hierarchy: can you name the reading order?

- **Hierarchy is explicit.** Can you say what gets read first, second, and third? Do size, weight, and color agree with that order, or do two of them argue?
- **The sizes are a decision.** Can you defend every distinct size in the component, or did the count accumulate as elements were added?
- **The text colors are a decision.** Same question. Levels of text color are hierarchy; disabled and inverse are states and don't count toward it.
- **Line length is set rather than inherited.** Does body copy have a measure you chose? Text running the full width of a wide container is tiring to read, and the fix is a max width rather than a smaller size.

## 2. Color: is every use of color doing work?

- **The strongest color is on the most important thing.** Does the highest-saturation element on the surface match what you want looked at first? If three things carry brand color, none of them is the primary action.
- **The surface is quiet enough for color to register.** Is most of the component neutral, so color reads as a signal instead of as the background?
- **Meaning holds.** Does each color mean the same thing everywhere? Status colors report status, primary marks the primary action. Neither gets borrowed because a thing needed emphasis.
- **Nothing is colored to fill space.** Can you say what each colored element is telling the user? A tint applied for visual interest is decoration, and it costs you a signal you'll want later.

Contrast is the accessibility baseline in `AGENTS.md`. Whether the states exist at all is `production-quality.md` section 1.3. This file is about intent.

## 3. States that read

- **Default is distinct.** Is each state visibly different from `default`, or does hover read as the resting state with a slight tint on top?
- **Disabled explains itself.** Does the user know why it's disabled and what would enable it?
- **Pending reassures.** Does the waiting state tell the user the system heard them, or does it only stop them from clicking again?

## 4. Content that guides

- **Empty states say what would fill them.** Does it give guidance ("No results yet") rather than blank space?
- **Errors say what to do.** Does the message explain what's wrong and the fix, rather than "Invalid"?
- **It survives without the icon.** Does it still make sense without the illustration or icon carrying the meaning?
- **Labels earn their width.** Is every word in the component doing something, or is some of it narrating the interface back to the user?

Copy rules and the linter live in `skills/write-copy/`.

## Not covered yet

Add when the work needs it:
- Motion and transition quality (duration, easing, what animates and what doesn't)
- Layout, density and alignment
