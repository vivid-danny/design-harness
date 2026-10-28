#!/usr/bin/env python3
"""UserPromptSubmit hook: put the reply ceiling next to the prompt.

`AGENTS.md` carries the same rules, but it is read once and competes with
everything else in the file. This lands immediately before the response is
generated, which is the only moment anything can stop a long reply from
existing. Kept under 40 words for the same reason.
"""

import json
import sys

CEILING = (
    "Reply ceiling: 12 sentences, 240 words, no section headers. "
    "After editing a file, name what changed and where; the rationale is "
    "already in the file. Lead with the result, then stop."
)


def main():
    try:
        sys.stdin.read()
    except Exception:
        pass
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": CEILING,
        }
    }))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
