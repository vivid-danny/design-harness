# Evals

A fixed brief with a known outcome, re-run whenever the rules or skills change, to check whether the harness got better instead of just different.

Without this, every change to `AGENTS.md` or a skill is a guess. The harness accumulates instructions and nobody knows which ones are carrying weight.

## Layout

```
evals/
└── <project-slug>/
    ├── brief.md       the prompt, verbatim, unchanged between runs
    ├── expected.md    what good looks like for this brief
    └── runs/
        └── YYYY-MM-DD-<note>.md
```

## `brief.md`

The exact prompt. Do not improve it between runs. A brief that gets edited is a brief that can't be compared, and a slightly vague brief is closer to real conditions anyway.

Include whatever a real brief would carry: the customer or business goal, the surface, any data or fixtures. Nothing else.

## `expected.md`

What a good response looks like, written before or independently of any run. Not a model answer, a set of conditions:

- Did it name the context and the path before building?
- Did it state three named axes before drawing?
- Are the directions distinct, or three versions of one screen?
- Did it use library components, or draw lookalikes?
- Did it name what it fabricated?
- Does the output clear `production-quality.md`?
- Is the copy clean per `skills/write-copy/linter.py`?

## `runs/`

One file per run. What the harness produced, which conditions it met, and which it missed. Link the Figma output.

Record the failure honestly. A run that looks good but skipped the axis step is a failure of the harness, and writing it down as a pass wastes the only instrument here.

## Using a result

A missed condition points at a specific file. Divergence failures point at `AGENTS.md` workflow step 3 and `explore-directions`. Wrong-library components point at the search scoping rule. Invented data points at the hard rules. Fix the instruction, then re-run the same brief.

Keep the old run files. The point is the trend.
