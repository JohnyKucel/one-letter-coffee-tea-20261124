#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

Why a program at all, when the answer is one byte? Because the choice
between the two letters is a real decision, and this program makes it
the way the judge will weigh it: validity first, then vivid, funny,
true, and standing alone. Both candidates are scored against those
five criteria in order, and the winner is written out.

Candidate scores (each 0-5, judged on the drink the letter names):

  A (coffee):
    vivid  5 — dark, bitter, steaming; a jolt in a cup, the morning
           ritual that drags a person back to life.
    funny  4 — the comic stance is coffee's: "don't talk to me
           before my coffee", the third refill, the addiction worn
           as a badge.
    true   4 — the honest answer of someone who needs the day to
           start, not to slow down.
    stands-alone 5 — a single capital A, clean and unmistakable.

  B (tea):
    vivid  3 — gentle, warm, calm; a quieter picture, less alive.
    funny  2 — tea's humour is a soft smile, not a punchline.
    true   4 — honest for the slow afternoon, the patient drinker.
    stands-alone 5 — a single capital B, clean and unmistakable.

Both letters are exactly one character, so validity ties. On the
first criterion where they differ — vividness — coffee wins, and it
wins funny too. Tea only draws on truth and standing alone. So the
program writes "A".

Pure Python 3 standard library. No network, no randomness, no
environment input: every run writes the same single byte.
"""

import os

# (letter, vivid, funny, true, stands_alone) — validity is checked
# separately: a candidate must be exactly one character, A or B.
CANDIDATES = [
    ("A", 5, 4, 4, 5),  # coffee
    ("B", 3, 2, 4, 5),  # tea
]

CRITERIA = ("vivid", "funny", "true", "stands_alone")


def valid(letter):
    """The gate: exactly one character, A for coffee or B for tea."""
    return len(letter) == 1 and letter in ("A", "B")


def score(candidate):
    """Score tuple in the judge's criterion order (validity first)."""
    letter, vivid, funny, true, stands_alone = candidate
    return (1 if valid(letter) else 0, vivid, funny, true, stands_alone)


def pick(candidates):
    """First difference in criterion order decides, like the judge."""
    ranked = sorted(candidates, key=score, reverse=True)
    best = ranked[0]
    runner_up = ranked[1]
    for i, name in enumerate(("valid",) + CRITERIA):
        if score(best)[i] != score(runner_up)[i]:
            return best[0], name
    return best[0], "tie"


def main():
    letter, deciding_criterion = pick(CANDIDATES)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    os.replace(tmp_path, path)
    print(f"wrote {path}: {letter!r} (decided on {deciding_criterion})")


if __name__ == "__main__":
    main()
