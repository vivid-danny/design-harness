---
name: write-copy
description: Write or audit user-facing interface copy and the harness's own prose. Use whenever a design includes text (button labels, empty states, error messages, fee and price language, microcopy) or when handing off directions and findings. Strips the patterns that read as machine-written, enforced by a linter rather than by judgement.
---

# Write Copy

Two jobs with different rules: the copy inside the design, and the prose in the handoff. Both get checked by `linter.py` rather than by eyeballing, because a model asked to avoid its own tells is a poor judge of whether it did.

## The linter

```
python3 skills/write-copy/linter.py <file>        # readable report
python3 skills/write-copy/linter.py --json <file> # machine-readable
cat draft.md | python3 skills/write-copy/linter.py -
```

Exits 1 when a blocker is present. It reports and never rewrites; restructuring is your job.

Run it on anything long enough to hide a tell: a handoff, a spec, a set of empty states. A three-word button label does not need it.

| Severity | Meaning |
|---|---|
| blocker | Breaks a hard rule. Fix before shipping the text. |
| important | Reads as machine-written. Fix unless there is a reason. |
| polish | Worth a look. |

## Interface copy

The text inside mockups and prototypes.

- **Clarity outranks voice** on fees, payment, legal, and support copy. A user deciding whether to spend money needs to understand the number, not enjoy the sentence.
- **Button labels are single-line and Title Case.** If a label needs two lines, the label is too long. Shorten the copy rather than resizing the button.
- **No redundant UX writing.** `Continue`, not `Click here to continue to the next step`. The control already says it is a control.
- **Empty states guide.** `No results yet` beats blank space. Say what would fill it.
- **Errors say what happened and what to do.** Not `Something went wrong`.
- **Brand voice comes from the active context pack**, never from this skill. Non-branded work gets no brand spin, so an internal tool does not inherit a consumer tone because that was the last pack you read.
- **Never invent a number, a fee, or a legal line.** Those come from the brief or the context pack. Mark placeholders as placeholders.

Real copy at real length is part of the design. Placeholder text hides the overflow problems `production-quality.md` section 1.2 exists to catch.

## Harness prose

Direction tables, fabrication callouts, findings, handoffs, anything Danny reads.

Banned outright, and all checked by the linter:

- **Em dashes.** Restructure into commas, a full stop, or parentheses. This includes the en dash and the double hyphen standing in for one.
- **Negative parallelism.** No `it's not X, it's Y`, no `not just X, but Y`, no `less about X, more about Y`. State what the thing is.
- **Question-then-answer.** Don't pose a question to answer it yourself.
- **Three-word stacks.** `Clear, concise, and compelling` is one adjective doing the work and two riding along. Keep the one that carries weight.
- **Filler adverbs.** `genuinely`, `really`, `truly`, `actually`, `basically`.
- **Lead-ins.** `here's the thing`, `the thing is`, `to be honest`, `at the end of the day`.
- **Preamble.** No `Great question`, no `Let me...`, no `I'll...`, no `Looking at your...`.
- **Closers.** No `Hope this helps`, no `Let me know if you need anything else`.
- **Inflated vocabulary.** `delve`, `leverage`, `robust`, `seamless`, `pivotal`, `realm`, `tapestry`, `streamline`, `game-changing`, `best-in-class`. Use the plain word. Swap test: if `start` loses nothing, `commence` was decoration.
- **Participle tails.** Don't bolt `highlighting...`, `underscoring...`, `showcasing...` onto a sentence to fake analysis.
- **Formulaic transitions.** `furthermore`, `moreover`, `consequently`. Use `also`, `but`, `so`, or start the sentence.
- **Curly quotes.** Straight quotes and apostrophes.

Also, from how Danny works:

- **Lead with the result or the decision needed.**
- **Vary sentence length.** Uniform rhythm reads as machine.
- **Take a position.** Reflexive hedging is a tell. Keep a hedge only when it carries real uncertainty; deleting one you mean manufactures confidence.
- **Say it once.** No dutiful closing summary of what you just said.
- **No empty praise.** Specific and earned, or nothing.

## What this skill is not

It does not govern code or identifiers. It does not apply to text written for a model to read, where density beats humanity. It is not permission to be vague: concise and direct, never thin.
