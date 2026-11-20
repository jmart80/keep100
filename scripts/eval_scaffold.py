#!/usr/bin/env python3
"""Put an example workspace into an eval run's empty folder.

usage: eval_scaffold.py {b2b|b2c} [--variant old|messy] [--dest DIR] [--today YYYY-MM-DD]

Each eval case's place-workspace.sh calls this. It copies examples/<track>,
moves every date forward so the example is always "as of today", and applies
the variant the case asks for.

If the file evals/.plain exists, it also removes every CLAUDE.md from the copy.
That is the "plain Claude" comparison: the same company files with none of
Keep100's rules. See evals/README.md.
"""
import argparse
import re
import shutil
import sys
from datetime import date, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ANCHOR = date(2026, 11, 20)  # the day the example workspaces describe
ISO = re.compile(r"\b(20\d\d)-(\d\d)-(\d\d)\b")


def shift_text(text, days):
    def move(match):
        try:
            moved = date(int(match[1]), int(match[2]), int(match[3])) + timedelta(days=days)
        except ValueError:
            return match[0]
        return moved.isoformat()
    return ISO.sub(move, text)


def shift_dates(dest, days):
    if not days:
        return
    for path in sorted(dest.rglob("*"), reverse=True):
        if path.is_file() and path.suffix in {".md", ".csv"}:
            path.write_text(shift_text(path.read_text(encoding="utf-8"), days), encoding="utf-8")
        if path.is_file() and ISO.search(path.name):
            path.rename(path.with_name(shift_text(path.name, days)))


def edit(path, old, new):
    text = path.read_text(encoding="utf-8")
    if old not in text:
        sys.exit(f"eval_scaffold: expected text not found in {path.name}: {old[:50]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def make_old(dest):
    """A workspace last updated by kit version 1.0.0."""
    edit(dest / "progress.md", "Kit version: 1.1.0", "Kit version: 1.0.0")


def make_messy(dest):
    """Four problems the audit should find. Dates here are moved with the rest."""
    edit(dest / "company" / "positioning.md", "Last confirmed: 2026-11-06", "Last confirmed: 2026-07-14")
    edit(dest / "company" / "customers.md", "\n## What they use today instead",
         '- "Honestly the phone tag is what kills us."\n\n## What they use today instead')
    with open(dest / "company" / "facts.md", "a", encoding="utf-8") as handle:
        handle.write("- [confirmed] The Clinic plan costs $79 a month. (source: Maya)\n")
    (dest / "marketing" / "2026-11-12-pricing-page.md").write_text(
        "# Pricing page draft\n\nHeadline: Fill the slot before the kettle boils\n", encoding="utf-8")


VARIANTS = {"old": make_old, "messy": make_messy}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("track", choices=["b2b", "b2c"])
    parser.add_argument("--variant", choices=sorted(VARIANTS))
    parser.add_argument("--dest", default=".")
    parser.add_argument("--today")
    args = parser.parse_args()

    dest = Path(args.dest)
    shutil.copytree(REPO / "examples" / args.track, dest, dirs_exist_ok=True)
    if args.variant:
        VARIANTS[args.variant](dest)
    today = date.fromisoformat(args.today) if args.today else date.today()
    shift_dates(dest, (today - ANCHOR).days)
    if (REPO / "evals" / ".plain").exists():
        for rules in dest.rglob("CLAUDE.md"):
            rules.unlink()


if __name__ == "__main__":
    main()
