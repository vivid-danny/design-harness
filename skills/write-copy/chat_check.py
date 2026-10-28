#!/usr/bin/env python3
"""Structural check for a chat reply: length, formatting, and re-explanation.

`linter.py` catches the writing patterns this harness bans, sentence by
sentence. This catches the shape of the whole reply: how long it is, whether it
grew section headers, and whether it restates a file the same turn just edited.

Separate from `linter.py` on purpose. That tool takes file paths and reports
per-line findings, and Danny runs it by hand. This one is document-level, needs
the turn's context to pick a ceiling, and runs inside a hook.

Usage:
    cat reply.md | python3 -I chat_check.py --tier base -
    python3 -I chat_check.py --tier tight --edits edits.json --json -

`--edits` takes a JSON array of strings: the `content` and `new_string` of every
Write and Edit call in the turn. Without it the re-explain check is skipped.
"""

import argparse
import json
import pathlib
import re
import sys

# Run with -I so nothing is picked up from the caller's environment, which also
# drops this script's own directory from the path. Put it back explicitly.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from linter import FENCE, mask_code  # noqa: E402

# Ceilings per tier. Word count is the primary gate; a sentence budget on its
# own invites comma-splicing into one ninety-word sentence.
TIERS = {
    "tight":    {"sentences": 8,  "words": 160, "headers": 0, "bullets": 4},
    "base":     {"sentences": 12, "words": 240, "headers": 0, "bullets": 6},
    "detail":   {"sentences": 24, "words": 600, "headers": 0, "bullets": 12},
    "document": None,  # exempt
}

# Over this multiple of the sentence or word ceiling, the reply is a wall
# rather than a long answer.
SEVERE = 2

# Re-explain thresholds. A short "the ceiling is now 12" is a report; the
# floor keeps it from counting as a restatement.
REEXPLAIN_MIN_WORDS = 8
# n and the threshold were picked by sweeping both against three fixtures: a
# paraphrased restatement, a short legitimate report, and unrelated prose of
# similar length. 4-grams at 0.25 was the only pair that caught the first and
# cleared the other two.
REEXPLAIN_SHINGLE = 4
REEXPLAIN_SIMILARITY = 0.25
REEXPLAIN_MIN_HITS = 3
REEXPLAIN_MAX_SHARE = 0.4
# The share rule needs something to be a share of. Under this many candidates a
# single hit would be 50% and would block a two-sentence reply.
REEXPLAIN_MIN_CANDIDATES = 4

HEADER = re.compile(r"^#{1,6}\s")
BULLET = re.compile(r"^\s*(?:[-*+]|\d+\.)\s")
TABLE_ROW = re.compile(r"^\s*\|")
QUOTE = re.compile(r"^\s*>")

# Periods that do not end a sentence. Masked before splitting so a filename or
# a decimal doesn't inflate the count.
HAZARDS = [
    re.compile(r"\b[\w-]+\.(?:md|py|ts|tsx|js|jsx|json|scss|css|html|png|svg|sh|ya?ml|lock|txt)\b"),
    re.compile(r"\b\d+(?:\.\d+)+\b"),
    re.compile(r"(?i)\b(?:e\.g|i\.e|etc|vs|approx|no|fig|cf|al)\."),
]

SENTENCE_SPLIT = re.compile(r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z0-9\"'(\[])")

WORD = re.compile(r"[A-Za-z0-9']+")


def strip_structural(text):
    """Split a reply into prose lines, bullet lines, and structural counts.

    Fenced blocks, indented code, quotes and table rows are not prose. An error
    report or a failing test pasted in a fence should never read as an essay.
    """
    prose, bullets = [], []
    headers = 0
    in_fence = False

    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("    ") or not line.strip():
            continue
        if TABLE_ROW.match(line) or QUOTE.match(line):
            continue
        if HEADER.match(line):
            headers += 1
            continue
        masked = mask_code(line)
        if BULLET.match(masked):
            bullets.append(BULLET.sub("", masked).strip())
        else:
            prose.append(masked.strip())

    return prose, bullets, headers


def paragraph_blocks(text):
    """Blank-line-separated runs of prose, ignoring lists, tables and code."""
    blocks, current, in_fence = 0, False, False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            current = False
            continue
        if in_fence:
            continue
        stripped = line.strip()
        structural = (
            not stripped
            or line.startswith("    ")
            or TABLE_ROW.match(line)
            or QUOTE.match(line)
            or HEADER.match(line)
            or BULLET.match(line)
        )
        if structural:
            current = False
        elif not current:
            blocks += 1
            current = True
    return blocks


def split_sentences(line):
    """Split on real sentence ends, returning the original text of each.

    Hazards are masked to the same length before splitting, so the boundaries
    found in the masked copy index straight back into the original.
    """
    masked = line
    for hazard in HAZARDS:
        masked = hazard.sub(lambda m: "x" * len(m.group(0)), masked)

    cuts = [0] + [m.end() for m in SENTENCE_SPLIT.finditer(masked)] + [len(line)]
    pieces = [line[a:b] for a, b in zip(cuts, cuts[1:])]
    return [p for p in pieces if len(WORD.findall(p)) >= 3]


def measure(text):
    prose, bullets, headers = strip_structural(text)

    sentences = []
    for line in prose:
        sentences += split_sentences(line)
    # A bullet is one sentence unless it carries more, so a list of six
    # one-liners is six, not a free pass.
    for b in bullets:
        pieces = split_sentences(b)
        sentences += pieces if pieces else ([b] if len(WORD.findall(b)) >= 4 else [])

    words = sum(len(WORD.findall(s)) for s in prose + bullets)

    return {
        "sentences": len(sentences),
        "words": words,
        "headers": headers,
        "bullets": len(bullets),
        "paragraphs": paragraph_blocks(text),
        "_sentences": sentences,
    }


def shingles(text, n=REEXPLAIN_SHINGLE):
    """Overlapping word n-grams, lowercased."""
    words = [w.lower() for w in WORD.findall(text)]
    if len(words) < n:
        return set()
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def similarity(sentence, block):
    """Share of the sentence's word n-grams that also appear in the block.

    Token-set overlap was the first attempt and it failed: a short, legitimate
    report reuses the vocabulary of the thing it reports on, so every word hit
    and it scored 1.0. Restating copies phrasing, and phrasing is runs of words
    in order, which is what an n-gram catches and a bag of words cannot.
    """
    sa = shingles(sentence)
    if not sa:
        return 0.0
    return len(sa & shingles(block)) / len(sa)


def check_reexplain(sentences, edits):
    """Count reply sentences that restate something the turn just wrote."""
    candidates = [s for s in sentences if len(WORD.findall(s)) >= REEXPLAIN_MIN_WORDS]
    if not candidates or not edits:
        return 0, 0

    hits = 0
    for sentence in candidates:
        if any(similarity(sentence, block) >= REEXPLAIN_SIMILARITY for block in edits):
            hits += 1
    return hits, len(candidates)


def check(text, tier, edits=None):
    limits = TIERS.get(tier)
    m = measure(text)
    sentences = m.pop("_sentences")

    findings = []
    if limits is None:
        return findings, m

    def add(severity, name, value, limit, message):
        findings.append({
            "check": name, "severity": severity,
            "value": value, "limit": limit, "message": message,
        })

    for name in ("sentences", "words"):
        limit = limits[name]
        if m[name] > limit * SEVERE:
            add("block", name, m[name], limit,
                f"{m[name]} {name}, ceiling {limit}. Cut to the ceiling.")
        elif m[name] > limit:
            add("log", name, m[name], limit, f"{m[name]} {name}, ceiling {limit}.")

    if m["headers"] > limits["headers"]:
        add("block", "headers", m["headers"], limits["headers"],
            f"{m['headers']} section header(s) in a chat reply. Remove them.")

    if m["bullets"] > limits["bullets"]:
        add("log", "bullets", m["bullets"], limits["bullets"],
            f"{m['bullets']} bullets, ceiling {limits['bullets']}.")

    hits, candidates = check_reexplain(sentences, edits or [])
    m["reexplain_hits"] = hits
    m["reexplain_candidates"] = candidates
    over_share = (candidates >= REEXPLAIN_MIN_CANDIDATES
                  and hits / candidates > REEXPLAIN_MAX_SHARE)
    if candidates and (hits >= REEXPLAIN_MIN_HITS or over_share):
        add("block", "reexplain", hits, REEXPLAIN_MIN_HITS,
            f"{hits} sentence(s) restate a file this turn edited. "
            "Name what changed and where instead.")

    return findings, m


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", help="file to check, or - for stdin")
    ap.add_argument("--tier", default="base", choices=sorted(TIERS))
    ap.add_argument("--edits", help="JSON file: array of edited text blocks")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()

    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()

    edits = []
    if args.edits:
        try:
            with open(args.edits, encoding="utf-8") as fh:
                edits = [str(e) for e in json.load(fh)]
        except (OSError, ValueError):
            edits = []

    findings, metrics = check(text, args.tier, edits)

    if args.json:
        json.dump({"tier": args.tier, "findings": findings, "metrics": metrics},
                  sys.stdout, indent=2)
        sys.stdout.write("\n")
    elif not findings:
        print(f"clean ({args.tier}): " + ", ".join(
            f"{k} {v}" for k, v in metrics.items()))
    else:
        for f in findings:
            print(f"({f['severity']}) [{f['check']}] {f['message']}")

    return 1 if any(f["severity"] == "block" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
