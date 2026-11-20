#!/usr/bin/env python3
"""Check, queue and summarize sales/pipeline.csv for Keep100.

Usage:
  pipeline.py check FILE [--today YYYY-MM-DD]
  pipeline.py due   FILE [--today YYYY-MM-DD] [--new N]
  pipeline.py stats FILE [--since YYYY-MM-DD]

Standard library only. Exit code 1 when `check` finds errors.
"""
import argparse
import csv
import sys
from datetime import date, datetime, timedelta

# Days after the first email that each follow-up is due. Email 1 is day 0.
FOLLOW_UP_DAYS = {2: 3, 3: 7, 4: 12, 5: 19}
# A trigger older than this is no longer a reason to write.
STALE_AFTER_DAYS = 60
# Warn when fewer than this many A and B prospects are waiting.
MIN_QUEUE = 20

COLUMNS = [
    "added", "name", "role", "company", "link", "email", "email_source",
    "lane", "trigger", "trigger_date", "source_url", "grade", "status",
    "sent_1", "sent_2", "sent_3", "sent_4", "sent_5",
    "replied", "reply_type", "next_step", "next_date", "notes",
]
REQUIRED = ["added", "name", "role", "company", "link", "lane", "trigger",
            "trigger_date", "source_url", "grade", "status"]
STATUSES = {"queued", "active", "replied", "call_booked", "won", "lost",
            "not_now", "stopped", "bounced", "parked"}
REPLY_TYPES = {"positive", "question", "objection", "not_now", "referral",
               "wrong_person", "opt_out", "auto_reply"}
DATE_COLUMNS = ["added", "trigger_date", "sent_1", "sent_2", "sent_3",
                "sent_4", "sent_5", "replied", "next_date"]
# Statuses that must never receive another email.
CLOSED = {"won", "lost", "stopped", "bounced", "parked"}


def parse_date(text):
    text = (text or "").strip()
    if not text:
        return None
    return datetime.strptime(text, "%Y-%m-%d").date()


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        header = [h.strip() for h in (reader.fieldnames or [])]
        rows = []
        for number, raw in enumerate(reader, start=2):
            row = {(k or "").strip(): (v or "").strip() for k, v in raw.items()}
            row["_line"] = number
            rows.append(row)
    return header, rows


def who(row):
    return f"line {row['_line']} ({row.get('name') or 'no name'}, {row.get('company') or 'no company'})"


def check(path, today):
    header, rows = load(path)
    errors, warnings = [], []

    missing = [c for c in COLUMNS if c not in header]
    if missing:
        errors.append("missing columns: " + ", ".join(missing))
        print_report(errors, warnings)
        return 1

    seen_people, seen_emails = {}, {}
    for row in rows:
        label = who(row)
        for column in REQUIRED:
            if not row.get(column):
                errors.append(f"{label}: {column} is empty")

        dates = {}
        for column in DATE_COLUMNS:
            try:
                dates[column] = parse_date(row.get(column))
            except ValueError:
                errors.append(f"{label}: {column} is not a YYYY-MM-DD date ({row.get(column)!r})")
                dates[column] = None

        if row.get("grade") and row["grade"] not in {"A", "B", "C"}:
            errors.append(f"{label}: grade must be A, B or C")
        if row.get("lane") and row["lane"] not in {"trigger", "pain"}:
            errors.append(f"{label}: lane must be trigger or pain")
        status = row.get("status")
        if status and status not in STATUSES:
            errors.append(f"{label}: unknown status {status!r}")
        if row.get("reply_type") and row["reply_type"] not in REPLY_TYPES:
            errors.append(f"{label}: unknown reply_type {row['reply_type']!r}")

        for column in ("link", "source_url"):
            value = row.get(column)
            if value and not value.startswith(("http://", "https://")):
                errors.append(f"{label}: {column} is not a link")

        if row.get("email") and not row.get("email_source"):
            errors.append(f"{label}: email has no email_source. Never keep an address without knowing where it came from")
        if dates.get("replied") and not row.get("reply_type"):
            errors.append(f"{label}: replied is set but reply_type is empty")
        if dates.get("replied") and status == "active":
            errors.append(f"{label}: replied but still active. A reply ends the sequence")
        if row.get("reply_type") == "opt_out" and status != "stopped":
            errors.append(f"{label}: opted out but status is not stopped")
        if status == "stopped" and dates.get("next_date"):
            errors.append(f"{label}: stopped rows must not have a next_date")
        if status == "not_now" and not dates.get("next_date"):
            warnings.append(f"{label}: not_now with no next_date, so nobody will follow up")
        if status == "queued" and row.get("grade") == "C":
            warnings.append(f"{label}: grade C should be parked, not queued")
        if status == "queued" and dates.get("sent_1"):
            errors.append(f"{label}: queued but sent_1 is set. Use active")
        if status == "active" and not dates.get("sent_1"):
            errors.append(f"{label}: active but sent_1 is empty")

        sent = [dates.get(f"sent_{n}") for n in range(1, 6)]
        for index in range(1, 5):
            if sent[index] and not sent[index - 1]:
                errors.append(f"{label}: sent_{index + 1} is set but sent_{index} is not")
            if sent[index] and sent[index - 1] and sent[index] < sent[index - 1]:
                errors.append(f"{label}: sent_{index + 1} is earlier than sent_{index}")

        trigger_date = dates.get("trigger_date")
        if trigger_date and trigger_date > today:
            errors.append(f"{label}: trigger_date is in the future")
        if status == "queued" and trigger_date and (today - trigger_date).days > STALE_AFTER_DAYS:
            warnings.append(f"{label}: trigger is {(today - trigger_date).days} days old. Find a newer one or park the row")
        if status == "queued" and row.get("grade") in {"A", "B"} and not row.get("email"):
            warnings.append(f"{label}: queued with no email. Find a published address or another way to reach them")

        person = (row.get("name", "").lower(), row.get("company", "").lower())
        if all(person):
            if person in seen_people:
                errors.append(f"{label}: same person as line {seen_people[person]}")
            seen_people[person] = row["_line"]
        email = row.get("email", "").lower()
        if email:
            if email in seen_emails:
                errors.append(f"{label}: same email as line {seen_emails[email]}")
            seen_emails[email] = row["_line"]

    waiting = sum(1 for r in rows if r.get("status") == "queued" and r.get("grade") in {"A", "B"})
    if waiting < MIN_QUEUE:
        warnings.append(f"only {waiting} A and B prospects are waiting. Rebuild the list before it runs out (minimum {MIN_QUEUE})")

    print(f"{len(rows)} rows, {waiting} waiting")
    print_report(errors, warnings)
    return 1 if errors else 0


def print_report(errors, warnings):
    for line in errors:
        print("ERROR  ", line)
    for line in warnings:
        print("WARNING", line)
    if not errors and not warnings:
        print("OK")


def next_follow_up(row):
    """Return (email number, due date) for the next unsent follow-up, or None."""
    first = parse_date(row.get("sent_1"))
    if not first:
        return None
    for number in range(2, 6):
        if not row.get(f"sent_{number}"):
            return number, first + timedelta(days=FOLLOW_UP_DAYS[number])
    return None


def due(path, today, new_count):
    _, rows = load(path)

    follow_ups = []
    for row in rows:
        if row.get("status") != "active" or row.get("replied"):
            continue
        upcoming = next_follow_up(row)
        if upcoming and upcoming[1] <= today:
            follow_ups.append((upcoming[1], upcoming[0], row))
    follow_ups.sort(key=lambda item: (item[0], item[2]["_line"]))

    come_back = []
    for row in rows:
        if row.get("status") in CLOSED or row.get("status") in {"queued", "active"}:
            continue
        when = parse_date(row.get("next_date"))
        if when and when <= today:
            come_back.append((when, row))
    come_back.sort(key=lambda item: item[0])

    waiting = [r for r in rows if r.get("status") == "queued" and r.get("grade") in {"A", "B"}]
    queued, stale = [], []
    for row in waiting:
        seen = parse_date(row.get("trigger_date"))
        if seen and (today - seen).days > STALE_AFTER_DAYS:
            stale.append(row)
        else:
            queued.append(row)
    queued.sort(key=lambda r: (r.get("grade"), -(parse_date(r.get("trigger_date")) or date.min).toordinal()))
    first_emails = queued[:new_count]

    print(f"Today: {today.isoformat()}")
    print(f"\nFollow-ups due ({len(follow_ups)})")
    for due_date, number, row in follow_ups:
        late = (today - due_date).days
        suffix = f", {late} days late" if late > 0 else ""
        print(f"  email {number}  {row['name']}, {row['role']} at {row['company']}  (line {row['_line']}{suffix})")

    print(f"\nNext steps due ({len(come_back)})")
    for when, row in come_back:
        print(f"  {row['name']} at {row['company']}: {row.get('next_step') or 'follow up'}  (status {row['status']}, line {row['_line']})")

    print(f"\nNew first emails ({len(first_emails)} of {new_count} wanted)")
    for row in first_emails:
        flag = "" if row.get("email") else "  [no email yet]"
        print(f"  {row['grade']}  {row['name']}, {row['role']} at {row['company']}: {row['trigger']} ({row['trigger_date']}){flag}")

    if stale:
        print(f"\nHeld back, trigger older than {STALE_AFTER_DAYS} days ({len(stale)})")
        for row in stale:
            print(f"  {row['name']} at {row['company']}: {row['trigger']} ({row['trigger_date']}, line {row['_line']})")

    remaining = len(queued) - len(first_emails)
    if remaining < MIN_QUEUE:
        print(f"\nQueue after today: {remaining}. Below the minimum of {MIN_QUEUE}. Rebuild the list.")
    else:
        print(f"\nQueue after today: {remaining}")
    return 0


def stats(path, since):
    _, rows = load(path)

    def in_window(text):
        when = parse_date(text)
        return bool(when) and (since is None or when >= since)

    contacted = [r for r in rows if in_window(r.get("sent_1"))]
    emails = sum(1 for r in rows for n in range(1, 6) if in_window(r.get(f"sent_{n}")))
    replies = [r for r in rows if in_window(r.get("replied")) and r.get("reply_type") != "auto_reply"]
    by_type = {}
    for row in replies:
        by_type[row.get("reply_type") or "unlabeled"] = by_type.get(row.get("reply_type") or "unlabeled", 0) + 1
    calls = sum(1 for r in rows if r.get("status") == "call_booked")
    won = sum(1 for r in rows if r.get("status") == "won")
    opted_out = sum(1 for r in rows if r.get("status") == "stopped")
    bounced = sum(1 for r in rows if r.get("status") == "bounced")

    window = f"since {since.isoformat()}" if since else "all time"
    print(f"Funnel, {window}")
    print(f"  {len(contacted)} people contacted, {emails} emails sent")
    print(f"  {len(replies)} replies" + (f" ({', '.join(f'{count} {kind}' for kind, count in sorted(by_type.items()))})" if by_type else ""))
    print(f"  {calls} calls booked now, {won} paying customers")
    print(f"  {opted_out} opted out, {bounced} bounced")
    answered = [r for r in contacted if r.get("replied") and r.get("reply_type") != "auto_reply"]
    if contacted:
        print(f"  reply rate: {len(answered)} of the {len(contacted)} people first contacted in this window have replied")
    if len(contacted) < 30:
        print("  Too few sends to read a rate from. Look at who replied, not the percentage.")

    for label, key in (("lane", "lane"), ("grade", "grade")):
        groups = {}
        for row in contacted:
            bucket = groups.setdefault(row.get(key) or "blank", [0, 0])
            bucket[0] += 1
            if row in answered:
                bucket[1] += 1
        if groups:
            parts = [f"{name} {replied} of {sent}" for name, (sent, replied) in sorted(groups.items())]
            print(f"  replies by {label}: " + ", ".join(parts))
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_check = sub.add_parser("check")
    p_check.add_argument("file")
    p_check.add_argument("--today")

    p_due = sub.add_parser("due")
    p_due.add_argument("file")
    p_due.add_argument("--today")
    p_due.add_argument("--new", type=int, default=10)

    p_stats = sub.add_parser("stats")
    p_stats.add_argument("file")
    p_stats.add_argument("--since")

    args = parser.parse_args()
    try:
        if args.command == "check":
            return check(args.file, parse_date(args.today) or date.today())
        if args.command == "due":
            return due(args.file, parse_date(args.today) or date.today(), args.new)
        return stats(args.file, parse_date(args.since))
    except FileNotFoundError:
        print(f"ERROR   {args.file} does not exist. Build the list first.")
        return 1
    except ValueError as error:
        print(f"ERROR   {error}. Run `check` to find the row.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
