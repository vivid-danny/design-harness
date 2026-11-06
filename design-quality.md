# Design Quality


**This file applies to both kinds of work.** An exploration and a production build are judged by the same craft questions. This file guides the agent to a better result and output regardless of the type of work.

Read this document with the active context pack's `design.md`, which has the product facts these questions refer to.

**The one exemption is deliberate low fidelity.** When Danny asks for wireframes, a greybox, or a sketch, this file waits. Low fidelity is a request, never a default, and never something the agent delivers on its own.

## 1. Hierarchy

- Name the reading order before you build: first, second, third.
- Size, weight, and color agree with that order. When two of them disagree, the hierarchy is broken.
- Every distinct type size is defensible. Counts accumulate when nobody decides.
- Levels of text color are hierarchy. Disabled and inverse are states and don't count toward it.
- Body copy gets a max width, not a smaller size. Text running the full width of a wide container is tiring to read.

## 2. Typography

- Fewer sizes, stronger hierarchy. Three in a component is usually enough.
- Weight carries emphasis before size does.
- Text color encodes relationship: primary, secondary, tertiary. Don't add a fourth level without naming what it means.
- Bind line height and letter spacing to the type scale. A size without its paired line height is half a decision.
- All caps is for labels only. It slows reading at any length past a word or two.

## 3. Layout

- Spacing is built on a base unit of 8, subdivided to 4 and 2 for micro adjustments. Use the pack's spacing tokens, which usually encode this already.
- A value outside the scale is a stop, not a judgment call. Say so rather than typing a number.
- Spacing encodes grouping. Space inside a group is always tighter than space between groups.
- Proximity is the grouping signal. Elements near each other read as one unit whatever the borders say.
- White space is a density control. Add it to let the eye rest, not to fill the frame.
- Align optically. Icons, punctuation, and round shapes need the eye, not the math.
- Apply the rules the same way every time. Inconsistent spacing reads as broken rather than varied.

## 4. Color

- The highest-saturation element on the surface is the thing to look at first. Three elements in brand color means no primary action.
- Most of the surface is neutral. Color reads as a signal only against quiet.
- Each color means one thing everywhere. Status colors report status, primary marks the primary action, and neither gets borrowed for emphasis.
- Error, warning, success, and info are reserved. They never run decoratively.
- Every colored element answers what it is telling the user. A tint for visual interest spends a signal you will want later.

## 5. Accessibility

- WCAG 2.2 AA is the floor: 4.5:1 for body text, 3:1 for large text and UI boundaries.
- Touch targets are 24x24 CSS px minimum, 44x44 where the control sits on its own.
- Color never carries meaning alone. Pair it with text, an icon, or position.
- Focus is visible on everything focusable, and visible against the surface it sits on.
- Reading order matches visual order.

## 6. States

- Every state is visibly different from default at a glance. A slight tint is not a state.
- Disabled says why it is disabled and what would enable it.
- Pending confirms the system heard the user. Blocking a second click is not the same as reassurance.
- Nothing depends on hover. Touch has no hover.

## 7. Content

- Empty states say what would fill them.
- Errors say what happened and what to do.
- The design survives without the icon. Icons reinforce meaning and never carry it.
- Every word earns its width. Cut copy that narrates the interface back to the user.

Copy rules and the linter live in `skills/write-copy/`.

## 8. Motion

- Motion explains a change in state or position. When nothing changed, nothing animates.
- Transitions are short enough to feel immediate. Anything the user waits on is too slow.
- Elements entering ease out. Elements leaving ease in.
- Content is readable before the motion finishes. Nothing essential sits behind an animation.
- Reduced motion is honored. The design still works with every transition removed.
