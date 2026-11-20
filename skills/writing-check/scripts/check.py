#!/usr/bin/env python3
"""Mechanical checks for a Keep100 draft. The judgment calls stay in SKILL.md.

Usage:
  check.py FILE [--format general|cold-email|landing-page|product-email|social|blog]
                [--brand company/brand.md] [--template]

--template allows merge fields such as {first_name} in a saved email sequence.

Checks banned words and phrases, dashes used as separators, leftover
placeholders, and the word limits for the format. Exit code 1 on any ERROR.
Standard library only.
"""
import argparse
import re
import sys
from pathlib import Path

LIST_FILE = Path(__file__).resolve().parent.parent / "banned.txt"

PLACEHOLDER = re.compile(r"\{\{[^}]*\}\}|\{[a-z_][a-z0-9_ |/+-]*\}|\[\[[^\]]*\]\]", re.I)
LEFTOVER = re.compile(r"\b(?:TODO|TBD|lorem ipsum)\b", re.I)
MERGE_FIELDS = {"{first_name}", "{company}", "{role}", "{trigger}"}
LINK = re.compile(r"https?://|www\.", re.I)
WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’%$.,:/-]*")


def load_list(path=LIST_FILE):
    sections, current = {}, None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1]
            sections[current] = []
        elif current:
            sections[current].append(line.lower())
    return sections


def brand_words(path):
    """Return (allowed, never) from the brand file's two word sections."""
    allowed, never = set(), set()
    if not path or not Path(path).exists():
        return allowed, never
    target = None
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("## "):
            title = line[3:].strip().lower()
            target = allowed if title == "words we allow" else never if title == "words we never use" else None
            continue
        if target is None or not line or line.startswith("<!--") or line.endswith("-->"):
            continue
        for part in re.split(r"[,;]", line.lstrip("-* ").strip()):
            word = part.strip().strip('"').lower()
            if word:
                target.add(word)
    return allowed, never


def pattern_for(term):
    """Match the term on word boundaries, with common endings for single words."""
    if " " in term or "-" in term or "'" in term:
        return re.compile(r"(?<![A-Za-z])" + re.escape(term).replace("'", "['’]") + r"(?![A-Za-z])", re.I)
    stem = term[:-1] if term.endswith("e") else term
    return re.compile(r"\b" + re.escape(stem) + r"(?:e|es|ed|ing|s|d)?\b", re.I)


def count_words(text):
    return len(WORD.findall(text))


def strip_markup(line):
    return re.sub(r"[*_`>#]", "", line)


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, where, message):
        self.errors.append(f"ERROR   {where}: {message}")

    def warn(self, where, message):
        self.warnings.append(f"WARNING {where}: {message}")

    def show(self):
        for line in self.errors + self.warnings:
            print(line)
        if not self.errors and not self.warnings:
            print("OK")
        else:
            print(f"{len(self.errors)} errors, {len(self.warnings)} warnings")
        return 1 if self.errors else 0


def check_terms(lines, fmt, lists, allowed, never, report):
    banned = [t for t in lists.get("words", []) + lists.get("phrases", []) if t not in allowed]
    if fmt in {"cold-email", "product-email"}:
        banned += [t for t in lists.get("email", []) if t not in allowed]
    banned += [t for t in never if t not in banned]
    review = [t for t in lists.get("review", []) if t not in allowed]
    checks = [(pattern_for(t), t, True) for t in banned] + [(pattern_for(t), t, False) for t in review]
    for number, line in enumerate(lines, start=1):
        for regex, term, is_error in checks:
            if regex.search(line):
                if is_error:
                    report.error(f"line {number}", f'banned term "{term}"')
                else:
                    report.warn(f"line {number}", f'check "{term}" is meant literally')


def check_marks(lines, report, template=False):
    bangs = 0
    for number, line in enumerate(lines, start=1):
        if "—" in line or " – " in line or " -- " in line:
            report.error(f"line {number}", "dash used as a separator. Use a full stop or a comma")
        for match in PLACEHOLDER.finditer(line):
            if template and match.group(0).lower() in MERGE_FIELDS:
                continue
            report.error(f"line {number}", f"leftover placeholder {match.group(0)}")
        if LEFTOVER.search(line):
            report.error(f"line {number}", "leftover TODO, TBD or filler text")
        bangs += line.count("!")
    if bangs > 1:
        report.warn("whole draft", f"{bangs} exclamation marks. One at most")


def split_sections(lines, heading):
    """Yield (title, first line number, body lines) for each heading match."""
    sections, title, start, body = [], None, 0, []
    for number, line in enumerate(lines, start=1):
        match = heading.match(line)
        if match:
            if title is not None:
                sections.append((title, start, body))
            title, start, body = match, number, []
        elif title is not None:
            body.append(line)
    if title is not None:
        sections.append((title, start, body))
    return sections


def check_cold_email(lines, report):
    heading = re.compile(r"^#{1,4}\s*Email\s*(\d)", re.I)
    emails = split_sections(lines, heading)
    if not emails:
        emails = [(None, 1, lines)]
    for match, start, body in emails:
        number = int(match.group(1)) if match else 1
        where = f"email {number}"
        subject = next((l for l in body if l.lower().startswith("subject:")), None)
        text = [strip_markup(l) for l in body if not l.lower().startswith("subject:") and not l.startswith("```")]
        words = count_words(" ".join(text))
        if words > 100:
            report.error(where, f"{words} words. Never over 100")
        elif words > 75:
            report.warn(where, f"{words} words. Aim for 50 to 75")
        if number <= 3 and any(LINK.search(l) for l in text):
            report.error(where, "contains a link. No links in emails 1 to 3")
        if number <= 3 and any(re.search(r"\battach(?:ed|ment)", l, re.I) for l in text):
            report.error(where, "mentions an attachment. None in emails 1 to 3")
        if any(";" in l for l in text):
            report.warn(where, "semicolon in a conversational email")
        if number != 5 and any(re.match(r"\s*(?:[-*]|\d+[.)])\s", l) for l in text):
            report.warn(where, "list inside the email body")
        if subject:
            value = subject.split(":", 1)[1].strip()
            if not value.lower().startswith("re:"):
                if value != value.lower():
                    report.warn(where, "subject should be lowercase")
                if count_words(value) > 4:
                    report.warn(where, "subject should be 3 or 4 words")
                if "?" in value:
                    report.warn(where, "no question mark in the subject")
        elif match:
            report.warn(where, "no Subject: line")


LABEL_LIMITS = {"headline": 10, "subheadline": 25, "cta": 5, "microcopy": 8}
SECTION_LIMITS = {2: 80, 3: 60}


def check_landing_page(lines, report):
    heading = re.compile(r"^##\s*(\d)\.")
    ctas = {}
    for match, start, body in split_sections(lines, heading):
        number = int(match.group(1))
        prose = []
        for offset, line in enumerate(body, start=start + 1):
            label = re.match(r"\s*\**(Headline|Subheadline|CTA|Microcopy)\**\s*:\s*(.+)", line, re.I)
            if label:
                name, value = label.group(1).lower(), strip_markup(label.group(2)).strip()
                words = count_words(value)
                if words > LABEL_LIMITS[name]:
                    report.error(f"line {offset}", f"{name} is {words} words. Limit {LABEL_LIMITS[name]}")
                if name == "cta":
                    ctas.setdefault(number, value)
                    if words < 2:
                        report.error(f"line {offset}", "button text needs 2 to 5 words")
            elif not re.match(r"\s*(Formula|Visual|Archetype)\b", line, re.I):
                prose.append(strip_markup(line))
        limit = SECTION_LIMITS.get(number)
        if limit:
            words = count_words(" ".join(prose))
            if words > limit:
                report.error(f"section {number}", f"{words} words. Limit {limit}")
    if 1 in ctas and 6 in ctas and ctas[1].lower() != ctas[6].lower():
        report.error("section 6", f'button text "{ctas[6]}" differs from the hero "{ctas[1]}"')
    if 1 not in ctas:
        report.warn("section 1", "no CTA: line found in the hero")


def check_product_email(lines, report):
    for match, start, body in split_sections(lines, re.compile(r"^##\s+(.+)")):
        words = count_words(" ".join(strip_markup(l) for l in body if not l.lower().startswith("subject:")))
        if words > 120:
            report.warn(match.group(1).strip(), f"{words} words. Keep under 120")


def run(path, fmt="general", brand=None, template=False):
    report = Report()
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    allowed, never = brand_words(brand)
    check_terms(lines, fmt, load_list(), allowed, never, report)
    check_marks(lines, report, template)
    if fmt == "cold-email":
        check_cold_email(lines, report)
    elif fmt == "landing-page":
        check_landing_page(lines, report)
    elif fmt == "product-email":
        check_product_email(lines, report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("file")
    parser.add_argument("--format", default="general",
                        choices=["general", "cold-email", "landing-page", "product-email", "social", "blog"])
    parser.add_argument("--brand", help="path to company/brand.md, for allowed and banned words")
    parser.add_argument("--template", action="store_true", help="allow merge fields such as {first_name}")
    args = parser.parse_args()
    if not Path(args.file).exists():
        print(f"ERROR   {args.file} does not exist")
        return 1
    return run(args.file, args.format, args.brand, args.template).show()


if __name__ == "__main__":
    sys.exit(main())
