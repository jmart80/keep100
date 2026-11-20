#!/usr/bin/env python3
"""Build the Keep100 progress dashboard from a workspace folder.

Usage:
  build.py WORKSPACE [--out FILE] [--json] [--today YYYY-MM-DD]

Reads WORKSPACE/progress.md, the Status lines in WORKSPACE/company/, and
WORKSPACE/sales/pipeline.csv if it has rows. Writes WORKSPACE/dashboard.html
(or --out) from assets/dashboard.html. --json prints the data and writes
nothing. Standard library only.
"""
import argparse
import csv
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "dashboard.html"
MARKER = "/*KEEP100_DATA*/"
CHECKBOX = re.compile(r"^\s*[-*]\s*\[( |x|X|-)\]\s*(.+?)\s*$")
BULLET = re.compile(r"^\s*[-*]\s+(.+?)\s*$")
COMPANY_ORDER = ["product", "customers", "positioning", "pricing", "brand", "competitors"]


def parse_date(text):
    try:
        return datetime.strptime((text or "").strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def nice_date(day):
    return f"{day.day} {day.strftime('%B %Y')}"


def split_note(label):
    """Split 'Step name (skipped: reason)' into the name and the note."""
    match = re.match(r"^(.*?)\s*\((.+)\)\s*$", label)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return label, ""


def table_rows(lines):
    rows = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        rows.append(cells)
    return rows[1:] if rows else []


def parse_progress(text):
    header, sections, current = {}, [], None
    for line in text.splitlines():
        if line.startswith("## "):
            current = {"title": line[3:].strip(), "lines": []}
            sections.append(current)
        elif current is None:
            match = re.match(r"^([A-Za-z][A-Za-z ]+):\s*(.*)$", line.strip())
            if match:
                header[match.group(1).strip().lower()] = match.group(2).strip()
        else:
            current["lines"].append(line)
    return header, sections


def placeholder(value):
    return not value or "{{" in value


def build_data(workspace, today=None):
    workspace = Path(workspace)
    today = today or date.today()
    progress = workspace / "progress.md"
    if not progress.exists():
        raise FileNotFoundError(f"{progress} does not exist. Run Keep100 setup first.")
    header, sections = parse_progress(progress.read_text(encoding="utf-8"))

    checklist, open_loops, work_log, paying, numbers = [], [], [], 0, None
    for section in sections:
        title, lines = section["title"], section["lines"]
        items = []
        for line in lines:
            match = CHECKBOX.match(line)
            if match:
                state = {" ": "todo", "x": "done", "X": "done", "-": "skipped"}[match.group(1)]
                label, note = split_note(match.group(2))
                items.append({"label": label, "state": state, "note": note if state == "skipped" else ""})
        key = title.lower()
        if items:
            checklist.append({"title": title, "items": items})
        elif key.startswith("open loops"):
            open_loops = [m.group(1) for m in map(BULLET.match, lines) if m]
        elif key.startswith("work log"):
            work_log = [m.group(1) for m in map(BULLET.match, lines) if m][:6]
        elif key.startswith("paying customers"):
            paying = len([r for r in table_rows(lines) if any(r)])
        elif key.startswith("weekly numbers"):
            rows = [r for r in table_rows(lines) if any(r)]
            if rows:
                last = (rows[-1] + [""] * 5)[:5]
                numbers = {"week_of": last[0], "reached": last[1], "replies": last[2], "calls": last[3], "paid": last[4]}

    flat = [(s["title"], i) for s in checklist for i in s["items"]]
    done = sum(1 for _, i in flat if i["state"] == "done")
    counted = [pair for pair in flat if pair[1]["state"] != "skipped"]
    upcoming = next(((t, i) for t, i in flat if i["state"] == "todo"), None)

    company = []
    folder = workspace / "company"
    if folder.is_dir():
        names = [p.stem for p in folder.glob("*.md") if p.stem != "facts"]
        names.sort(key=lambda n: (COMPANY_ORDER.index(n) if n in COMPANY_ORDER else 99, n))
        for name in names:
            status, confirmed = "Draft", ""
            for line in (folder / f"{name}.md").read_text(encoding="utf-8").splitlines()[:12]:
                if line.lower().startswith("status:"):
                    status = line.split(":", 1)[1].strip() or "Draft"
                elif line.lower().startswith("last confirmed:"):
                    confirmed = line.split(":", 1)[1].strip()
            company.append({"name": name.capitalize(), "status": status, "last_confirmed": confirmed})

    pipeline = None
    sheet = workspace / "sales" / "pipeline.csv"
    if sheet.exists():
        with open(sheet, newline="", encoding="utf-8-sig") as handle:
            rows = [{(k or "").strip(): (v or "").strip() for k, v in row.items()} for row in csv.DictReader(handle)]
        if rows:
            pipeline = {
                "reached": sum(1 for r in rows if r.get("sent_1")),
                "replies": sum(1 for r in rows if r.get("replied") and r.get("reply_type") != "auto_reply"),
                "calls": sum(1 for r in rows if r.get("status") in {"call_booked", "won"}),
                "paid": sum(1 for r in rows if r.get("status") == "won"),
                "waiting": sum(1 for r in rows if r.get("status") == "queued" and r.get("grade") in {"A", "B"}),
            }

    started = parse_date(header.get("started"))
    hours = header.get("hours a day", "")
    now = datetime.now()
    return {
        "product": "" if placeholder(header.get("product")) else header["product"],
        "founder": "" if placeholder(header.get("founder")) else header["founder"],
        "track": "" if placeholder(header.get("track")) else header["track"],
        "kit_version": header.get("kit version", ""),
        "started": started.isoformat() if started else "",
        "started_text": nice_date(started) if started else "",
        "days_in": (today - started).days + 1 if started and today >= started else 0,
        "hours_a_day": "" if placeholder(hours) else (hours if re.search(r"[a-z]", hours, re.I) else f"{hours} hour" + ("" if hours.strip() == "1" else "s")),
        "steps_done": done,
        "steps_total": len(counted),
        "next": {"section": upcoming[0], "label": upcoming[1]["label"]} if upcoming else None,
        "paying_customers": paying,
        "sections": checklist,
        "company": company,
        "numbers": numbers,
        "pipeline": pipeline,
        "open_loops": open_loops,
        "work_log": work_log,
        "updated_text": f"{nice_date(today)}, {now.strftime('%H:%M')}",
    }


def render(data, template=TEMPLATE):
    html = Path(template).read_text(encoding="utf-8")
    if MARKER not in html:
        raise ValueError(f"{template} has no {MARKER} marker")
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    title = (data.get("product") or "Keep100").replace("<", "").replace(">", "")
    html = html.replace("<title>Keep100 progress</title>", f"<title>{title} progress</title>", 1)
    return html.replace(MARKER, blob, 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("workspace")
    parser.add_argument("--out")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--today")
    args = parser.parse_args()
    try:
        data = build_data(args.workspace, parse_date(args.today))
    except FileNotFoundError as error:
        print(f"ERROR   {error}")
        return 1
    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return 0
    out = Path(args.out) if args.out else Path(args.workspace) / "dashboard.html"
    out.write_text(render(data), encoding="utf-8")
    step = f"Next: {data['next']['label']}" if data["next"] else "Every step is done"
    print(f"Wrote {out}")
    print(f"{data['steps_done']} of {data['steps_total']} steps done. {step}. Paying customers: {data['paying_customers']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
