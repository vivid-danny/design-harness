#!/usr/bin/env python3
"""Stop hook: check the turn's final reply against the harness style rules.

Stop fires after the reply is already on screen, so this cannot shorten it. A
block makes the model append a correction, which is why the block reasons ask
for one corrected sentence rather than a rewritten reply, and why only the
unambiguous failures block at all.

Blocks on: a `blocker`-severity pattern finding from linter.py, a reply over
twice its tier's ceiling, a section header, or prose that restates a file the
same turn edited. Everything else is logged and nothing is said.

Every tier signal is read from the harness (the user's own message, the turn's
tool calls, permissionMode) and never from anything the model wrote. An escape
valve the model can emit becomes reflexive boilerplate within a few turns.

Fails open. A crash here must never block a turn.
"""

import json
import os
import pathlib
import re
import subprocess
import sys

HARNESS = pathlib.Path(__file__).resolve().parents[2]
WRITE_COPY = HARNESS / "skills" / "write-copy"
LOG = pathlib.Path.home() / ".cache" / "claude-brevity" / "metrics.jsonl"

WORD = re.compile(r"[A-Za-z0-9']+")

AFFIRMATION = re.compile(
    r"^(?:yes|yep|yeah|sure|ok|okay|k|do it|go ahead|go for it|please do|sounds good|"
    r"agreed|agree|correct|right|perfect|great|thanks|ship it|proceed)\b[\s.!,]*$",
    re.I,
)

DETAIL = re.compile(
    r"(?i)\b(?:explain|why|how does|how do|walk me through|detail|details|options?|"
    r"trade-?offs?|compare|comparison|pros and cons|break (?:it|this) down|"
    r"what are the|teach|coach|elaborate|expand on|unpack)\b"
)

NEGATOR = re.compile(r"(?i)\b(?:don'?t|do not|no|without|skip|not|rather than|instead of)\b")

DOCUMENT_ASK = re.compile(
    r"(?i)\b(?:write (?:a|the) (?:report|doc|document|spec|prd|brief|plan)|"
    r"draft (?:a|the) (?:report|doc|document|spec|prd|brief))\b"
)

SYSTEM_PREFIXES = (
    "<system_instruction>", "<system-reminder>", "<command-name>",
    "<local-command", "<user-prompt-submit-hook>",
)

EDIT_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}


def read_rows(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    return rows


def row_text(row):
    """Plain text of a transcript row, or '' when it carries none."""
    content = row.get("message", {}).get("content")
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    return "\n".join(
        b.get("text", "") for b in content
        if isinstance(b, dict) and b.get("type") == "text"
    )


def is_real_prompt(row):
    """A message Danny actually typed, not an injection or a tool result."""
    if row.get("type") != "user" or row.get("isSidechain") or row.get("isMeta"):
        return False
    content = row.get("message", {}).get("content")
    if isinstance(content, list) and any(
        isinstance(b, dict) and b.get("type") == "tool_result" for b in content
    ):
        return False
    text = row_text(row).strip()
    return bool(text) and not text.startswith(SYSTEM_PREFIXES)


def find_turn(rows):
    """The governing prompt and every row after it."""
    for i in range(len(rows) - 1, -1, -1):
        if is_real_prompt(rows[i]):
            return rows[i], rows[i + 1:]
    return None, rows


def keyword_prompt(rows, governing):
    """The prompt the tier keywords are read from.

    A bare "yes" inherits the previous prompt's tier. Without this the model
    can raise its own ceiling by asking "want me to lay out the options?" and
    reading the answer as a request for detail.
    """
    text = row_text(governing).strip()
    if not (len(WORD.findall(text)) <= 6 and AFFIRMATION.match(text)):
        return text
    seen = False
    for row in reversed(rows):
        if not is_real_prompt(row):
            continue
        if not seen:
            seen = True
            continue
        return row_text(row).strip()
    return text


def un_negated(pattern, text):
    """True when the pattern matches without a negator just before it."""
    for m in pattern.finditer(text):
        window = text[max(0, m.start() - 40):m.start()]
        if not NEGATOR.search(window):
            return True
    return False


def turn_facts(after):
    tools, edits, had_error = set(), [], False
    for row in after:
        if row.get("isSidechain"):
            continue
        content = row.get("message", {}).get("content")
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                name = block.get("name", "")
                tools.add(name)
                if name in EDIT_TOOLS:
                    inp = block.get("input", {}) or {}
                    for key in ("content", "new_string"):
                        value = inp.get(key)
                        if isinstance(value, str) and value.strip():
                            edits.append(value)
                    for sub in inp.get("edits", []) or []:
                        value = (sub or {}).get("new_string")
                        if isinstance(value, str) and value.strip():
                            edits.append(value)
            elif block.get("type") == "tool_result" and block.get("is_error"):
                had_error = True
    return tools, edits, had_error


def pick_tier(prompt, keywords, tools, had_error, permission_mode):
    if permission_mode == "plan" or "ExitPlanMode" in tools:
        return "document"
    if DOCUMENT_ASK.search(keywords):
        return "document"
    if had_error or un_negated(DETAIL, keywords):
        return "detail"
    asked = "?" in prompt
    if not asked and (tools & EDIT_TOOLS or not tools):
        return "tight"
    return "base"


def final_reply(after):
    for row in reversed(after):
        if row.get("type") != "assistant" or row.get("isSidechain"):
            continue
        text = row_text(row).strip()
        if text:
            return text
    return ""


def run(cmd, stdin_text):
    return subprocess.run(
        cmd, input=stdin_text, capture_output=True, text=True,
        cwd=str(WRITE_COPY), timeout=20,
    )


def pattern_findings(reply):
    proc = run([sys.executable, "-I", "linter.py", "--json", "-"], reply)
    try:
        return [f for f in json.loads(proc.stdout) if f.get("severity") == "blocker"]
    except ValueError:
        return []


def structural_findings(reply, tier, edits):
    cmd = [sys.executable, "-I", "chat_check.py", "--tier", tier, "--json"]
    edits_path = None
    if edits:
        edits_path = LOG.parent / "edits.json"
        edits_path.parent.mkdir(parents=True, exist_ok=True)
        edits_path.write_text(json.dumps(edits), encoding="utf-8")
        cmd += ["--edits", str(edits_path)]
    cmd.append("-")
    proc = run(cmd, reply)
    if edits_path:
        edits_path.unlink(missing_ok=True)
    try:
        return json.loads(proc.stdout)
    except ValueError:
        return {"findings": [], "metrics": {}}


def log(record):
    try:
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with open(LOG, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record) + "\n")
    except OSError:
        pass


def main():
    payload = json.loads(sys.stdin.read() or "{}")
    if payload.get("stop_hook_active"):
        return 0

    path = payload.get("transcript_path")
    if not path or not os.path.isfile(path):
        return 0

    rows = read_rows(path)
    governing, after = find_turn(rows)
    if governing is None:
        return 0

    reply = final_reply(after)
    if not reply:
        return 0

    prompt = row_text(governing).strip()
    keywords = keyword_prompt(rows, governing)
    tools, edits, had_error = turn_facts(after)
    tier = pick_tier(prompt, keywords, tools, had_error,
                     governing.get("permissionMode"))

    blockers = pattern_findings(reply)
    structural = structural_findings(reply, tier, edits)
    findings = structural.get("findings", [])

    log({
        "session": payload.get("session_id"),
        "tier": tier,
        "metrics": structural.get("metrics", {}),
        "pattern_blockers": [f.get("rule") for f in blockers],
        "findings": [f.get("check") for f in findings],
        "blocked": bool(blockers) or any(f["severity"] == "block" for f in findings),
    })

    reasons = []
    for f in blockers:
        reasons.append(f"{f['message']} Found: {f['match']!r}. Correct that sentence only.")
    for f in findings:
        if f["severity"] == "block":
            reasons.append(f["message"])

    if reasons:
        print(json.dumps({
            "decision": "block",
            "reason": " ".join(reasons) + " No apology, no explanation of the edit.",
        }))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
