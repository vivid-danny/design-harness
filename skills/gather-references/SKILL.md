---
name: gather-references
description: Collect competitive examples and design references before exploring directions. Use when starting a design run that needs precedent, when the user supplies inspiration to work from, or when a specific visual or flow decision would be settled by seeing how others solved it. Searches Mobbin and reports what the references show.
---

# Gather References

Find evidence that settles a decision. Not a research phase, not a moodboard exercise.

## When to search

**Supplied material first.** If Danny gave you screenshots, links, or a Figma file, that's the reference set. Work from it before reaching for Mobbin.

**Search when it resolves something concrete.** Name the decision before you search: how dense should this row be, where does the price sit relative to the score, what does a selected state look like when the set is long. A search without a decision behind it is ceremony.

**Skip it when the answer is already in the context pack.** A component that exists with a documented usage rule doesn't need competitive precedent.

## Searching Mobbin

`search_screens` for a single screen, `search_flows` for a multi-step journey, `search_sections` for a website section.

- `platform: "web"` for web work, `"ios"` for app work. Match the context pack, not the device you're imagining.
- `output_destination: "design_tool"` when the results feed Figma.
- Keep `task_intent` identical across every call in one run.
- Query one screen or one journey per call, in plain language, starting with what kind of screen it is. Name a specific app to filter to it. Don't stack multiple intents into one query, don't add elements Danny didn't ask about, and don't pad with style words like "modern" or "clean".

Competitors worth naming directly when the work is consumer ticketing: StubHub, SeatGeek, Ticketmaster.

## The rule that matters

**Open an item and look at the image before describing it.** Search results give you titles and metadata; those are leads, not evidence. A claim about what a screen looks like requires having looked at the screen. A claim about motion requires a recording or a live interaction, which Mobbin stills can't give you, so don't make one.

If an image won't load, use another source and say the first one was inaccessible. Never describe what was behind a gate.

## Reporting

Lead with the finding, not the catalog. Three references that answer the decision beat twelve that illustrate the topic.

For each one: what it does, and what that implies for the decision you named. Cite it as a markdown link to its `mobbin_url` so Danny can open it. Separate what you observed from what you inferred.

**Popularity proves nothing about usability.** A pattern appearing in four products means four teams shipped it, not that it converts or that users understand it. Say "common" when it's common. Don't say "proven".

Stop when the evidence answers the decision.

## Saving images

Inline previews are low-resolution and for your reading only. If Danny wants a reference saved, embedded, or pasted into Figma, download from `image_url`, which is the high-resolution file. Those URLs expire after 30 days, so download rather than linking. Cite with `mobbin_url`.
