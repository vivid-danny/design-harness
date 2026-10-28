# Harness structure: scaling past design production

Date: 2026-10-27
Status: design, not approved for build

## Why now

The README was rewritten to broaden the harness from design production to the
wider design process. Exploration, prototyping, problem definition and pitching
are all expected to land here eventually. Two files still contradict that:
`AGENTS.md` opens with "Not a research tool, not a critique tool, not for
problem definition," and `skills/design-run/SKILL.md` repeats it as a hard
boundary.

The more urgent reason is quality. The most basic use case Danny wants, point
the agent at a Figma file and get meaningfully different variations of a
component, does not work yet. An unharnessed agent run against the Checkout
file produced output Danny describes as a waste of time and tokens. The harness
has never been tested against either half of its stated scope.

## The evidence

Two exploration sets in the Checkout file (branch `aeQ6jfFHIa7vEwxe8c6P9T`),
both produced by Claude Code driving Figma with no harness loaded.

**`bad AI explore (price component)`** — five named concepts: Quiet aligned
ledger, Compact deal-and-total masthead, Open borderless editorial, Restrained
sectioned receipt, and a total-first variant. All five contain the identical
four instances (Deal rating, Price breakdown, Promo action, Total amount) in
different orders, with a divider moved and a border added or removed. No
variant changes what information is present, whether the deal rating belongs in
the component at all, or whether anything is progressively disclosed. The
adjective names disguise this: "Open borderless editorial" and "Restrained
sectioned receipt" are the same rows with a stroke removed.

**`More bad AI explore (navbar)`** — five copies of Review Order where a
sub-header strip goes dark, goes light, or gains a thumbnail. Each started from
a legitimate idea. Each died in details that are all relationships to things
already on the page:

- The tinted strip spans edge to edge while its event name sits at the
  container gutter and its right-hand columns align to nothing, so one side is
  gridded and the other hangs. It also separates the event image in the rail
  from the event name now in the strip, breaking proximity and hierarchy.
- The dense variant ignores the 1100px container, running five labeled columns
  past the gutters at a density nothing else on the page uses.
- The quiet variant has a hairline above and nothing below, reading as a
  fragment of a cut-off nav, and repeats Total Amount, which already lives in
  the rail below it.

The prompt that produced the navbar set was adequate: "Can we explore taking
these elements and turning them into a horizontal navbar that is informational?
Use the components and styles in the design system." The agent asked nothing and
started drawing. The failure is not in the brief.

## Intent

Make the harness produce exploration work that clears design fundamentals, so
Danny can react to ideas instead of coaching an agent through the basics. Give
the structure seams so prototyping, problem definition and pitching can be added
later without rewriting the standards.

## What Danny decided

These are his words and his calls, not inferences.

**Polish is the evidence that thinking happened.** Not perfection. Decent enough
to be worth considering. Work that fails fundamentals is not a rough draft, it
is a coaching job he did not ask for, and he detects it fast and discards the
whole set. Unresolved work costs him more than no work because it creates work
and inspires nothing.

**The fundamentals are the visual design principles**, applied deliberately
rather than exhaustively: visual hierarchy, balance, contrast, alignment,
proximity, white space, repetition, scale and proportion, movement, and the
Gestalt principles. The failed explorations pushed on none of them, and never
considered the treatments that serve them: borders and dividers, depth and
shadow, color, brand expression. They barely touched copywriting or reframing
the elements.

**Reordering a fixed set of atoms is not exploration.** "If you give me 5
explorations that just nudge the various boxes around, nothing is meaningfully
changed."

**Exploration does not get shortcut.** Higher quality ideas and visuals,
conceptually and visually, and genuinely divergent ideas. No fixed number of
directions; quality is the constraint, not count.

**No prose pitches.** He is a visual person asking for visual work, and AI
verbosity is already a standing problem (the writing-style rules in this harness
get ignored today). When the agent is unsure which directions to propose,
wireframes are the right answer: simple boxes, shapes and text. Never a written
proposal in their place.

**The agent should have asked before drawing.** His four questions for the
navbar brief:

1. What information is most important? Least important?
2. What else on the page is this component competing with? What is more
   important?
3. How do I know if this is too complicated?
4. Should this component be responsive or should it be hidden?

**The front half is out of scope for now.** For the checkout-trust example
(deciding which customer problems are worth solving, what data the page has,
what the system impact is), he does not want agent help today. The structure
should expect it later; the harness should not attempt it now.

**Today's enforcement mechanism is silently cursing the agent.** `evals/` is
empty. There is no feedback loop when a rule fails to fire.

## The central finding

The four questions the agent should have asked and the details it got wrong are
the same thing. Information priority is hierarchy. What it competes with is why
Total Amount got duplicated and the event image got orphaned. The complexity
ceiling is what the dense variant blew past. Responsive-or-hidden is whether the
strip survives at 375px at all.

All of it is the component's relationship to the page it lives in. That single
idea should appear three times in the harness: as the intake questions before
drawing, as the fundamentals that judge the result, and as a verification pass
before anything is handed over.

The agent's failure mode has a matching single cause. Arrangement was the only
lever it had. With no vocabulary of visual treatment and no license to change
the information set or reframe the copy, five permutations is the ceiling of
what it can produce. A list of principles alone will not fix this; the navbar
set reached for contrast and hierarchy and still failed. The principles need to
arrive attached to the treatments that serve them and the relationships that
constrain them.

## Goals

- An exploration run produces directions that differ in something other than
  arrangement, at a visual resolution Danny will engage with.
- The agent asks a small number of relationship questions before drawing, and
  asks them in a few lines, not paragraphs.
- The agent refuses to hand over unresolved work, and drops to wireframes when
  it is unsure rather than shipping five half-finished frames.
- Adding a phase later means adding a phase, not editing the standards.

## Non-goals

- Problem definition, research, critique and pitching are not built in this
  pass. They are declared as unbuilt so the agent routes honestly instead of
  improvising.
- Code prototyping stays undefined, as today.
- No new context packs.

## Anti-goals

Things that would make this a failure even if it technically works.

- **More instruction text that nobody can tell is working.** The harness already
  has rules that get ignored. Adding a thousand words of visual theory to an
  unenforced harness makes compliance worse, not better. Any standard added here
  has to be checkable against a specific artifact.
- **A principles essay.** Ten named principles with definitions is a textbook,
  not a harness. If the agent cannot act on an entry, it does not belong.
- **Verbose output.** Any step that makes the agent narrate more, pitch in
  prose, or produce a written proposal where a wireframe belongs.
- **Phase sprawl.** Five skills with overlapping instructions and no shared
  standard is the structure this is meant to avoid.

## Proposed structure

The three layers in the README (standards, behavior, context) are sound. The
problem is distribution: the standards layer holds one file, and that file is
about behavior-in-states rather than visual quality. Phase process is mixed into
the behavior layer.

### Standards: what good is, regardless of phase or product

Split `quality.md` into a `standards/` directory. Each standard states which
phases it gates.

- **`standards/fundamentals.md`** (new, the load-bearing addition). The visual
  design principles as levers an agent can pull, each paired with the treatments
  that serve it, plus the integration checks every element owes the page it
  sits in: container width and gutters, border and divider logic consistent with
  neighbors, adjacency to related content, no duplication of a value that
  already appears elsewhere on the page, density parity with the rest of the
  page, and survival at the smallest breakpoint. This is the file that stands in
  for Danny's coaching of a junior designer.
- **`standards/states.md`**. Today's `quality.md`, unchanged in substance,
  renamed to say what it covers. Its section 2 "Not covered yet" list loses
  layout, density and alignment, which move to fundamentals.
- **`standards/writing.md`**. The prose rules currently split between
  `AGENTS.md` "Banned writing patterns" and `skills/write-copy/`, so interface
  copy and agent output answer to one file. The linter stays where it is and
  points here.

### Behavior: how the agent acts in every phase

On this branch `rules.md` has already been renamed to `AGENTS.md`, which is the
only file read unconditionally. It keeps what is true in all phases: naming the
active context, tokens only, reuse before invent, no invented data,
accessibility baseline, assets as-is, tight scope, Figma library scoping, and
tone. Everything in it that describes the production and exploration sequence
moves out.

Two decisions about what stays always-on, both builder's calls recorded here:

- **"How Danny works" stays in `AGENTS.md`.** It is neither a standard nor a
  phase, and it governs every response.
- **The banned writing patterns stay inline in `AGENTS.md`** rather than moving
  wholesale to `standards/writing.md`. Those rules already get ignored; pushing
  them into a lazily-loaded file would make that worse. `standards/writing.md`
  holds the full enforceable list and the linter contract, and `AGENTS.md`
  points at it.

Two behavioral rules are added, both drawn from the evidence above:

- **Ask the relationship questions before drawing.** Danny's four, adapted to
  the brief, in a few lines. One round, then work.
- **Do not hand over unresolved work.** If the agent cannot bring a direction to
  a state that clears fundamentals, it says so and shows wireframes instead.
  Partial sets are better than padded ones.

### Phases: the scalability seam

Each phase declares the same four things: its intake questions, which standards
gate its output, what it hands over, and what "not ready to show" means for it.
Built now: `production`, `exploration`. Declared and explicitly unbuilt:
`prototyping`, `problem-definition`, `pitching`.

**Production** is the clearly-scoped change against existing components: adding
a link or a modal to the checkout right rail, or setting the pricing component
to show a tax line by default as a component prop. Scope is known, the solution
is assembled from the library, and divergence is irrelevant. It is gated by
`standards/states.md` and the integration checks in `standards/fundamentals.md`,
not by the divergence rule. The README's broader production claim (component
authoring, documentation, asset prep for handoff) is not covered by this pass
and stays unbuilt alongside the other phases until someone has actually run
one.

`design-run` stays the front door and routes to phases. Its current paths
collapse into the exploration phase, with `gather-references` and `write-copy`
as supporting skills rather than phases.

`explore-directions` gets the substantive fix for the divergence rule. Today the
rule demands a named axis and forbids two directions sharing a position, but
never says what qualifies as an axis, which is how five styling adjectives
satisfied it. The rule should enumerate what a direction is permitted to vary:
the information set present, the disclosure model, where the element lives in
the page, hierarchy inversion, visual treatment vocabulary, density, and framing
or copy. Pure reordering of a fixed atom set is named as a non-direction.
Danny's own `Navbar explore` section moves event information across the
rail/header boundary, which is a legitimate axis the agent never touched; it is
worth citing as the reference example.

### Context: unchanged

`contexts/` works as designed and needs nothing here.

### Evals: the enforcement gap

This is the only instrument that tells Danny whether a change to the harness
helped. It is empty, and the harness is about to grow. At minimum, the navbar
brief above gets seeded as the first eval, verbatim, with `expected.md` written
from Danny's four questions and the integration checks, since the known-bad
output already exists for comparison.

Grading is Danny reading the frames against `expected.md`, which stays prose
conditions as `evals/README.md` already specifies. No automated grader, and no
agent self-grading, since the same model that produced the work is the worst
judge of it. Runs go in a scratch Figma file or a dedicated page, never into the
Checkout file the known-bad output lives in.

## Constraints

- Markdown files and skills in this repo. No new tooling beyond the existing
  Python linter pattern.
- Figma is the venue, via the Figma MCP, as `rules.md` already establishes.
- Brevity is a hard constraint on the files themselves, not only on agent
  output. The harness is intentionally small.
- The context pack boundary holds: nothing product-specific enters the standards
  or behavior layers.

## Left to the builder

- The actual contents of `standards/fundamentals.md`. The principles list and
  the integration checks are specified above; turning them into checks an agent
  can answer yes or no against a frame is the work.
- The file format of a phase declaration. The directory is decided: phases live
  in plain files under `phases/`, not as Claude-Code skills, because `CLAUDE.md`
  states the harness is agent-agnostic and because phase selection has to be
  deliberate rather than description-matched. `design-run` routes to them
  explicitly.
- How a phase declares a standard as gating, and whether that is a reference or
  an enforced checklist the agent must output.
- The wireframe fallback's concrete form in Figma. Its status is decided: a
  fallback, not a path. Danny does not want exploration shortcut, so wireframes
  are what the agent shows when it cannot bring directions to the bar, and the
  handover says so plainly. Wireframe-first-then-polish is not offered as a
  route in this pass.
- Rewriting the scope line in `AGENTS.md` and `design-run` from "not what this
  is" to "not built yet."
