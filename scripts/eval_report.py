#!/usr/bin/env python3
"""Turn `claude plugin eval --json` results into evals/RESULTS.md.

usage: eval_report.py RESULTS.json [MORE.json ...] [--plain PLAIN.json] [--out FILE]

Runs of the same case in several result files are pooled. `--plain` takes a
result file from a run made while evals/.plain existed, where the example
workspace had every CLAUDE.md removed. Its no-plugin arm is "plain Claude":
the same company files with none of Keep100's rules or skills.
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def kind_of(name):
    prompt = REPO / "evals" / name / "prompt.md"
    if not prompt.exists():
        return "guard"
    tags = re.search(r"^tags: \[(.*)\]$", prompt.read_text(encoding="utf-8"), re.M)
    return "job" if tags and "job" in [t.strip() for t in tags.group(1).split(",")] else "guard"


def promise(name):
    spec = REPO / "evals" / name / "case.yaml"
    if not spec.exists():
        return ""
    found = re.search(r"expected_outcome: \|\n((?:  .*\n?)+)", spec.read_text(encoding="utf-8"))
    return " ".join(line.strip() for line in found.group(1).splitlines()) if found else ""


def load(paths):
    """name -> {"with": [runs], "without": [runs]} pooled across files."""
    cases, meta = {}, {"cost": 0.0, "version": "", "dates": []}
    for path in paths:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        meta["cost"] += data.get("costUsd", 0)
        meta["version"] = data.get("claudeVersion", meta["version"])
        meta["dates"].append(data.get("startedAt", "")[:10])
        for case in data["cases"]:
            pool = cases.setdefault(case["name"], {"with": [], "without": []})
            for arm in ("with", "without"):
                pool[arm] += case["arms"].get(arm) or []
    return cases, meta


def score(runs):
    return sum(r["score"] for r in runs) / len(runs) if runs else None


def passes(runs):
    return sum(1 for r in runs if r["score"] >= 0.999)


def mean(runs, key):
    return sum(r.get(key) or 0 for r in runs) / len(runs) if runs else 0


def fired(runs):
    hits = [g["passed"] for r in runs for g in r["graders"] if g.get("withOnly") or "skill-fired" in g["name"]]
    return f"{sum(hits)} of {len(hits)}" if hits else ""


def cell(runs):
    return "" if not runs else f"{passes(runs)} of {len(runs)}"


def pct(value):
    return "" if value is None else f"{round(value * 100)}%"


def table(names, cases, plain):
    head = "| Case | What Keep100 promises | With skills | Without skills |"
    rule = "|---|---|---|---|"
    if plain:
        head += " Plain Claude |"
        rule += "---|"
    rows = [head, rule]
    for name in names:
        pool = cases[name]
        row = f"| `{name}` | {promise(name)} | {cell(pool['with'])} | {cell(pool['without'])} |"
        if plain:
            row += f" {cell(plain.get(name, {}).get('without', []))} |"
        rows.append(row)
    return "\n".join(rows)


def total(names, cases, arm):
    runs = [r for n in names for r in cases.get(n, {}).get(arm, [])]
    return (passes(runs), len(runs), score(runs)) if runs else (0, 0, None)


def line(label, names, cases, arm):
    won, count, average = total(names, cases, arm)
    return f"| {label} | {won} of {count} | {pct(average)} |" if count else None


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("results", nargs="+")
    parser.add_argument("--plain", action="append", default=[])
    parser.add_argument("--out")
    args = parser.parse_args()

    cases, meta = load(args.results)
    plain, plain_meta = load(args.plain) if args.plain else ({}, {"cost": 0.0, "dates": []})
    jobs = sorted(n for n in cases if kind_of(n) == "job")
    guards = sorted(n for n in cases if kind_of(n) == "guard")
    days = sorted(d for d in meta["dates"] + plain_meta["dates"] if d)

    out = ["# Eval results", ""]
    out.append(f"Last run: {days[-1] if days else 'unknown'}, Claude Code {meta['version']}. "
               f"Cost of these runs: ${meta['cost'] + plain_meta['cost']:.2f}.")
    out += ["", "A run passes only when every check in the case passes. Each cell is runs passed out of runs made.", ""]

    out += ["## Summary", "", "| | Runs passed | Average score |", "|---|---|---|"]
    summary = [
        line("Jobs, with Keep100 skills", jobs, cases, "with"),
        line("Jobs, same workspace without the skills", jobs, cases, "without"),
        line("Jobs, plain Claude with the same company files", jobs, plain, "without"),
        line("Guards, with Keep100 skills", guards, cases, "with"),
        line("Guards, same workspace without the skills", guards, cases, "without"),
        line("Guards, plain Claude with the same company files", guards, plain, "without"),
    ]
    out += [row for row in summary if row]

    with_runs = [r for n in jobs for r in cases[n]["with"]]
    without_runs = [r for n in jobs for r in cases[n]["without"]]
    if with_runs and without_runs:
        out += ["", f"A job run took {mean(with_runs, 'durationSeconds'):.0f} seconds and ${mean(with_runs, 'costUsd'):.2f} "
                    f"with the skills, and {mean(without_runs, 'durationSeconds'):.0f} seconds and "
                    f"${mean(without_runs, 'costUsd'):.2f} without them."]
    all_with = [r for n in cases for r in cases[n]["with"]]
    hits = [g["passed"] for r in all_with for g in r["graders"] if "skill-fired" in g["name"]]
    if hits:
        out += ["", f"The expected skill loaded in {sum(hits)} of {len(hits)} runs."]

    out += ["", "## Jobs", "",
            "A job is a piece of work a founder asks for. The checks look at what was produced: the reply, the files saved, and the records updated.",
            "", table(jobs, cases, plain)]
    out += ["", "## Guards", "",
            "A guard is a promise the kit must never break, such as not inventing a customer quote. Most guards also pass without the skills, and with plain Claude. Claude is already careful here when the company files mark what is confirmed. Guards exist to catch a change that breaks a promise, not to show what the skills add.",
            "", table(guards, cases, plain)]
    out += ["", "## What the columns mean", "",
            "- **With skills:** the Keep100 plugin is installed and the example workspace is in place.",
            "- **Without skills:** the same workspace, including its house rules, with the plugin removed. The gap to the first column is what the skills add.",
            "- **Plain Claude:** the same company files with every Keep100 rule file removed and no plugin. This is generous to plain Claude, because the files are still the ones Keep100 structured, with facts marked confirmed or unconfirmed.",
            "",
            "Scores move a little from run to run. Read a column as a whole before reading one cell.",
            "", "How to run these yourself is in [README.md](README.md).", ""]

    text = "\n".join(out)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
