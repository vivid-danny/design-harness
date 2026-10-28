#!/usr/bin/env python3
"""Deterministic check for the writing patterns this harness bans.

A model asked to avoid its own tells is a poor judge of whether it did, so the
check runs outside the model. Reports findings; never rewrites.

Usage:
    python3 linter.py FILE [FILE ...]
    python3 linter.py --json FILE
    cat draft.md | python3 linter.py -
"""

import argparse
import json
import re
import sys

# (id, severity, compiled pattern, message)
# Severity: blocker breaks a hard rule, important reads as machine-written,
# polish is a judgement call worth a look.
RULES = [
    ("em-dash", "blocker", r"[—–]",
     "Em or en dash. Restructure into commas, a full stop, or parentheses."),
    ("double-hyphen", "blocker", r"(?<=\w)--(?=\w)|\s--\s",
     "Double hyphen standing in for an em dash."),
    ("spaced-hyphen", "important", r"\S \- \S",
     "Spaced hyphen standing in for an em dash. Use a comma or a full stop."),
    ("smart-quote", "important", r"[‘’“”]",
     "Curly quote. Use straight quotes and apostrophes."),

    # Negative parallelism, the "not X, it's Y" family.
    ("not-x-but-y", "blocker",
     r"(?i)\b(?:it'?s|its|this is|that'?s|we'?re|they'?re)\s+not\s+[^.,;!?]{1,60}[,;]\s*(?:it'?s|its|but|rather)\b",
     "Negative parallelism (\"it's not X, it's Y\"). State what the thing is."),
    ("not-just", "important",
     r"(?i)\b(?:not|isn'?t|aren'?t)\s+(?:just|merely|simply|only)\s+[^.,;!?]{1,60}[,;]\s*(?:it'?s|its|but|they'?re)\b",
     "Negative parallelism (\"not just X, it's Y\")."),
    ("less-about", "important",
     r"(?i)\bless\s+about\s+[^.,;!?]{1,60}[,;]?\s*(?:and\s+)?more\s+about\b",
     "Negative parallelism (\"less about X, more about Y\")."),

    # Lead-ins and filler Danny called out by name.
    # No trailing \b: several of these end in a comma, where \b cannot match.
    # "the thing is" only counts at the start of a clause. "what the thing is"
    # is ordinary prose.
    ("lead-in", "blocker",
     r"(?i)(?:^|(?<=[.;:!?]\s)|(?<=^- )|(?<=\*\*))(?:here'?s the thing|the thing is|let'?s be clear|to be honest|honestly,|at the end of the day|that said,)",
     "Throat-clearing lead-in. Start with the point."),
    ("filler-adverb", "important",
     r"(?i)\b(?:genuinely|really|truly|actually|basically|essentially|literally|incredibly|extremely)\b",
     "Filler adverb carrying no information."),
    ("preamble", "blocker",
     r"(?im)^(?:great question|sure[!,]|certainly[!,]|absolutely[!,]|let me |i'?ll |looking at your |to answer your question)",
     "Preamble announcing what you are about to do."),
    ("closer", "important",
     r"(?i)(?:let me know if you need anything else|hope (?:this|that) helps|happy to clarify|feel free to ask|anything else\?)",
     "Closing pleasantry. End when the answer is done."),

    # Inflated vocabulary.
    ("kill-list", "important",
     r"(?i)\b(?:delve|leverage(?:s|d|ing)?|tapestry|realm|robust|seamless(?:ly)?|pivotal|myriad|plethora|unlock(?:s|ing)? the|harness(?:es|ing)? the power|game[- ]chang(?:er|ing)|cutting[- ]edge|best[- ]in[- ]class|world[- ]class|enterprise[- ]grade|streamline(?:s|d)?|supercharge|elevate your|dive deep|deep dive)\b",
     "Inflated word. Use the plain one."),
    ("participle-tail", "important",
     r"(?i),\s+(?:highlighting|underscoring|showcasing|emphasizing|demonstrating|reflecting|ensuring|allowing|enabling)\s",
     "Participle tail faking analysis. Give the point a real clause."),
    ("formulaic-transition", "polish",
     r"(?i)\b(?:furthermore|moreover|consequently|additionally|notably|importantly)\b",
     "Formulaic transition. Use \"also\", \"but\", \"so\", or start the sentence."),

    # Redundant UX writing, for interface copy.
    ("redundant-ux", "important",
     r"(?i)\b(?:click here to|tap here to|please note that|in order to proceed|continue to the next step)\b",
     "Redundant UX writing. Say the action."),
]

COMPILED = [(rid, sev, re.compile(pat), msg) for rid, sev, pat, msg in RULES]

# Three-word stacks: the rhetorical adjective triple ("clear, concise, and
# compelling"), not an ordinary list of things ("price, score, and seat").
# Matching adjectives against a list buys precision, which is what makes a
# linter worth trusting. A stack built from words outside the list is missed.
STACK_ADJECTIVES = {
    "bold", "clean", "clear", "cohesive", "compelling", "concise", "confident",
    "consistent", "delightful", "distinct", "dynamic", "effective", "efficient",
    "elegant", "engaging", "essential", "flexible", "fluid", "fresh", "friendly",
    "immersive", "innovative", "intentional", "intuitive", "meaningful",
    "modern", "polished", "powerful", "pivotal", "practical", "purposeful",
    "refined", "reliable", "responsive", "robust", "scalable", "seamless",
    "simple", "sleek", "smart", "sophisticated", "strategic", "streamlined",
    "thoughtful", "timeless", "versatile", "vibrant",
}

THREE_STACK = re.compile(
    r"\b([a-z]{3,14}), ([a-z]{3,14}),? and ([a-z]{3,14})\b"
)

SEVERITY_ORDER = {"blocker": 0, "important": 1, "polish": 2}

INLINE_CODE = re.compile(r"`[^`]*`")
IGNORE_LINE = re.compile(r"<!--\s*lint-ignore(?:-line)?\s*-->")
FENCE = re.compile(r"^\s*```")


def mask_code(line):
    """Blank out inline code spans, keeping offsets so columns stay accurate.

    A doc that names a banned pattern in backticks is documenting it, not
    committing it. This file and write-copy/SKILL.md both depend on that.
    """
    return INLINE_CODE.sub(lambda m: " " * len(m.group(0)), line)


def check(text, path):
    findings = []
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = line.strip()
        # Skip indented code and table rows; neither is prose.
        if line.startswith("    ") or stripped.startswith("|"):
            continue
        if IGNORE_LINE.search(line):
            continue
        line = mask_code(line)
        for rid, sev, pattern, msg in COMPILED:
            for m in pattern.finditer(line):
                findings.append({
                    "file": path,
                    "line": lineno,
                    "col": m.start() + 1,
                    "rule": rid,
                    "severity": sev,
                    "message": msg,
                    "match": m.group(0).strip(),
                })
        for m in THREE_STACK.finditer(line):
            if sum(w in STACK_ADJECTIVES for w in m.groups()) < 2:
                continue
            findings.append({
                "file": path,
                "line": lineno,
                "col": m.start() + 1,
                "rule": "three-word-stack",
                "severity": "important",
                "message": "Three-word adjective stack. Keep the one that carries weight.",
                "match": m.group(0),
            })
    findings.sort(key=lambda f: (SEVERITY_ORDER[f["severity"]], f["line"]))
    return findings


def report(findings):
    if not findings:
        print("clean")
        return
    counts = {}
    for f in findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    summary = ", ".join(
        f"{counts[s]} {s}" for s in ("blocker", "important", "polish") if s in counts
    )
    print(f"{len(findings)} finding(s): {summary}\n")
    for f in findings:
        print(f"{f['file']}:{f['line']}:{f['col']} ({f['severity']}) "
              f"[{f['rule']}] {f['message']}")
        print(f"    {f['match']!r}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+", help="files to check, or - for stdin")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()

    findings = []
    for path in args.paths:
        if path == "-":
            findings += check(sys.stdin.read(), "<stdin>")
        else:
            try:
                with open(path, encoding="utf-8") as fh:
                    findings += check(fh.read(), path)
            except OSError as exc:
                print(f"cannot read {path}: {exc}", file=sys.stderr)
                return 2

    if args.json:
        json.dump(findings, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        report(findings)

    return 1 if any(f["severity"] == "blocker" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
