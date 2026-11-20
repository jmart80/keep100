#!/usr/bin/env python3
"""Read-only health check of a Keep100 workspace. Reports, never fixes.

Usage:
  audit.py WORKSPACE [--today YYYY-MM-DD] [--stale-days N]

Standard library only. Exit code 1 when anything is reported.
"""
import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

MONEY = re.compile(r"[$€£]\s?\d[\d,]*(?:\.\d+)?")
QUOTE_LINE = re.compile(r'^\s*[-*]\s.*"[^"]{12,}"')
TAGGED = re.compile(r"\[(?:verbatim|paraphrase)\]", re.I)
RULES_BUDGET = 90


def parse_date(text):
    try:
        return datetime.strptime((text or "").strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def read(path):
    return path.read_text(encoding="utf-8").splitlines() if path.exists() else []


def field(lines, name):
    for line in lines[:15]:
        if line.lower().startswith(name.lower() + ":"):
            return line.split(":", 1)[1].strip()
    return ""


def audit(workspace, today, stale_days):
    ws = Path(workspace)
    found = []

    def report(kind, message):
        found.append(f"{kind:<12} {message}")

    if not (ws / "progress.md").exists():
        return [f"{'MISSING':<12} progress.md. This is not a Keep100 workspace, or setup has not run."]

    company = ws / "company"
    files = sorted(company.glob("*.md")) if company.is_dir() else []
    if not files:
        report("MISSING", "company/ has no files")

    # Stale or unconfirmed company files
    for path in files:
        if path.name == "facts.md":
            continue
        lines = read(path)
        status, confirmed = field(lines, "Status"), field(lines, "Last confirmed")
        when = parse_date(confirmed)
        if status.lower() == "draft":
            report("DRAFT", f"company/{path.name} has never been confirmed")
        elif when and (today - when).days > stale_days:
            report("STALE", f"company/{path.name} was last confirmed {confirmed}, {(today - when).days} days ago")
        elif status and not when:
            report("STALE", f"company/{path.name} is {status} but has no Last confirmed date")

    # A price in more than one place
    pricing = read(company / "pricing.md")
    prices = sorted({m.group(0).replace(" ", "") for line in pricing for m in MONEY.finditer(line)})
    others = [p for p in files if p.name != "pricing.md"] + [ws / "CLAUDE.md"]
    for path in others:
        for number, line in enumerate(read(path), start=1):
            for match in MONEY.finditer(line):
                amount = match.group(0).replace(" ", "")
                where = path.relative_to(ws)
                if amount in prices:
                    report("DUPLICATE", f"{amount} is in pricing.md and also {where} line {number}. Keep it in pricing.md only")
                elif path.name == "facts.md":
                    report("CHECK", f"{amount} in {where} line {number}. If it is a price, it belongs in pricing.md")

    # Quotes without tags
    in_quotes = False
    for number, line in enumerate(read(company / "customers.md"), start=1):
        if line.startswith("## "):
            in_quotes = "in their own words" in line.lower()
        if in_quotes and QUOTE_LINE.match(line) and not TAGGED.search(line):
            report("UNTAGGED", f"company/customers.md line {number}: quote has no [verbatim] or [paraphrase] tag")

    # Facts with no status
    for number, line in enumerate(read(company / "facts.md"), start=1):
        if re.match(r"^\s*[-*]\s", line) and not re.search(r"\[(?:confirmed|unconfirmed)\]", line, re.I):
            report("UNTAGGED", f"company/facts.md line {number}: entry is neither [confirmed] nor [unconfirmed]")
        if re.search(r"\[unconfirmed\]", line, re.I):
            report("UNCONFIRMED", f"company/facts.md line {number}: {line.strip()[:90]}")

    # Leftover template placeholders
    for path in [ws / "CLAUDE.md", ws / "progress.md"] + files:
        for number, line in enumerate(read(path), start=1):
            if "{{" in line and "}}" in line:
                report("PLACEHOLDER", f"{path.relative_to(ws)} line {number}: {line.strip()[:70]}")

    # House rules that have grown
    rules = read(ws / "CLAUDE.md")
    if len(rules) > RULES_BUDGET:
        report("LONG", f"CLAUDE.md is {len(rules)} lines. Over {RULES_BUDGET}, rules start getting missed. Move procedures into skills")
    for area in ("research", "marketing", "sales", "social", "conversations"):
        area_rules = {l.strip() for l in read(ws / area / "CLAUDE.md") if l.strip().startswith("-")}
        repeated = area_rules & {l.strip() for l in rules if l.strip().startswith("-")}
        for line in sorted(repeated):
            report("REPEATED", f"{area}/CLAUDE.md repeats a root rule: {line[:70]}")

    # Contacts kept outside the pipeline
    progress = read(ws / "progress.md")
    if any(l.strip().lower() == "## getting customers" for l in progress) and any("| Who or where |" in l for l in progress):
        report("OLD LAYOUT", "progress.md still has the 1.0.0 contact table. Run keep100:update-workspace")
    if (ws / "sales" / "prospects.md").exists():
        report("DUPLICATE", "sales/prospects.md exists beside sales/pipeline.csv. Keep one list")

    # Saved work the log doesn't mention
    logged = " ".join(progress)
    for area in ("marketing", "sales", "social", "research"):
        folder = ws / area
        if not folder.is_dir():
            continue
        for path in sorted(folder.glob("20*.md")):
            if path.name not in logged:
                report("UNLOGGED", f"{area}/{path.name} is not in the Work log")

    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("workspace")
    parser.add_argument("--today")
    parser.add_argument("--stale-days", type=int, default=30)
    args = parser.parse_args()
    found = audit(args.workspace, parse_date(args.today) or date.today(), args.stale_days)
    for line in found:
        print(line)
    print("OK. Nothing to report." if not found else f"{len(found)} things to look at")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
