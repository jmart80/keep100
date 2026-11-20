#!/usr/bin/env python3
"""Check the Keep100 repo is internally consistent. Runs in CI on every push.

Usage: python3 scripts/validate.py

No model calls and no network. Exit code 1 on any error.
It checks: manifests and versions, every skill's frontmatter and size, that
every file and skill a skill mentions exists, the company model contract,
that every step in the checklist is ticked by some skill, the pipeline
format, the scripts against the example workspaces, and the eval cases.
"""
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
VENDORED = {"ui-ux-pro-max"}
ERRORS = []

FORBIDDEN = {
    "${CLAUDE_PLUGIN_ROOT}": "use ${CLAUDE_SKILL_DIR}, and call another skill by name instead of by path",
    "`ument": "leftover from a find-and-replace",
    "the packet": "leftover from the skill this was adapted from",
    "gold stars": "ratings are never shown unless confirmed",
    "—": "em dash. The kit's own writing check bans it",
    "sales/prospects.md": "contacts live in sales/pipeline.csv",
    "Getting customers table": "contacts and posts no longer live in progress.md",
    "Getting customers log": "contacts and posts no longer live in progress.md",
}
# Files that describe the 1.0.0 layout in order to migrate away from it.
MIGRATION_FILES = {"skills/update-workspace/changes.md", "skills/workspace-audit/SKILL.md"}
MIGRATION_TERMS = {"sales/prospects.md", "Getting customers table", "Getting customers log"}
PROMPT_KEYS = {"schema_version", "name", "description", "tags", "plugins", "runs", "expected_outcome",
               "model", "max_turns", "timeout_seconds", "allowed_tools", "append_system_prompt", "env"}
GRADER_TYPES = {"llm", "regex", "tool_used", "tool_order", "file_exists", "baseline"}


def err(message):
    ERRORS.append(message)


def rel(path):
    return str(Path(path).relative_to(ROOT))


def frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not match:
        return None, text
    fields = {}
    for line in match.group(1).splitlines():
        pair = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if pair:
            fields[pair.group(1)] = pair.group(2).strip().strip('"')
    return fields, text[match.end():]


def headings(text):
    return {line[3:].strip() for line in text.splitlines() if line.startswith("## ")}


def check_manifests():
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    version = plugin.get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        err(f"plugin.json version {version!r} is not MAJOR.MINOR.PATCH")
    listed = [p.get("version") for p in market.get("plugins", []) if p.get("name") == plugin.get("name")]
    if listed != [version]:
        err(f"marketplace.json lists version {listed}, plugin.json says {version}")
    contract = json.loads((ROOT / "docs" / "contract.json").read_text())
    for skill in contract["version_skills"]:
        text = (SKILLS / skill / "SKILL.md").read_text()
        found = re.search(r"^Kit version: (\S+)$", text, re.M)
        if not found or found.group(1) != version:
            err(f"skills/{skill}/SKILL.md says Kit version {found.group(1) if found else 'nothing'}, plugin.json says {version}")
    if f"## {version}" not in (SKILLS / "update-workspace" / "changes.md").read_text():
        err(f"update-workspace/changes.md has no section for {version}")
    changelog = ROOT / "CHANGELOG.md"
    if not changelog.exists() or f"## {version}" not in changelog.read_text():
        err(f"CHANGELOG.md has no section for {version}")
    return version, contract


def check_skills():
    names = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    readme = (ROOT / "README.md").read_text()
    for name in names:
        folder = SKILLS / name
        path = folder / "SKILL.md"
        if not path.exists():
            err(f"skills/{name} has no SKILL.md")
            continue
        text = path.read_text()
        fields, body = frontmatter(text)
        if fields is None:
            err(f"{rel(path)}: no frontmatter")
            continue
        if fields.get("name") != name:
            err(f"{rel(path)}: name {fields.get('name')!r} does not match the folder")
        description = fields.get("description", "")
        if not description:
            err(f"{rel(path)}: no description")
        if len(description) > 1024:
            err(f"{rel(path)}: description is {len(description)} characters, limit 1024")
        if "<" in description or ">" in description:
            err(f"{rel(path)}: description contains angle brackets")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
            err(f"skills/{name}: name must be lowercase letters, numbers and hyphens")
        if text.count("\n") > 500:
            err(f"{rel(path)}: {text.count(chr(10))} lines, limit 500")
        if name in VENDORED:
            continue
        if f"`{name}`" not in readme:
            err(f"README.md does not list the {name} skill")
        for doc in folder.rglob("*.md"):
            check_doc(doc, folder, names)
        for script in folder.rglob("*.py"):
            try:
                compile(script.read_text(), str(script), "exec")
            except SyntaxError as error:
                err(f"{rel(script)}: does not compile: {error}")
    return names


def check_doc(doc, folder, names):
    text = doc.read_text()
    where = rel(doc)
    for needle, why in FORBIDDEN.items():
        if where in MIGRATION_FILES and needle in MIGRATION_TERMS:
            continue
        if needle in text:
            line = text[: text.index(needle)].count("\n") + 1
            err(f"{where} line {line}: contains {needle!r}: {why}")
    for skill in re.findall(r"keep100:([a-z0-9-]+)", text):
        if skill not in names:
            err(f"{where}: mentions keep100:{skill}, which does not exist")
    mentioned = set(re.findall(r"`((?:references|scripts|assets)/[A-Za-z0-9_./-]+)`", text))
    mentioned |= set(re.findall(r"\$\{CLAUDE_SKILL_DIR\}/([A-Za-z0-9_./-]+)", text))
    mentioned |= set(re.findall(r"\]\(([A-Za-z0-9_./-]+\.(?:md|txt|py|html))\)", text))
    mentioned |= set(re.findall(r"`([A-Za-z-]+\.(?:md|txt))`", text)) & {p.name for p in folder.glob("*") if p.is_file()}
    for target in sorted(mentioned):
        if not (folder / target).exists() and not (doc.parent / target).exists():
            err(f"{where}: mentions {target}, which is not in the skill")


def check_contract(contract):
    places = {"template": SKILLS / "setup" / "workspace", "examples/b2b": ROOT / "examples" / "b2b", "examples/b2c": ROOT / "examples" / "b2c"}
    for label, base in places.items():
        for file, spec in contract["files"].items():
            path = base / file
            if not path.exists():
                err(f"{label}: {file} is in the contract but missing")
                continue
            have = headings(path.read_text())
            for heading in spec["headings"]:
                if heading not in have:
                    err(f"{label}/{file}: missing heading '## {heading}'")
        progress = (base / "progress.md").read_text()
        for key in contract["progress_keys"]:
            if not re.search(rf"^{re.escape(key)}:", progress, re.M):
                err(f"{label}/progress.md: missing the '{key}:' line")
    for skill in {w for spec in contract["files"].values() for w in spec["writer"]}:
        if " " not in skill and not (SKILLS / skill).is_dir():
            err(f"docs/contract.json names a writer that is not a skill: {skill}")


def check_steps():
    template = (SKILLS / "setup" / "workspace" / "progress.md").read_text()
    labels = re.findall(r"^- \[ \] (.+)$", template, re.M)
    if len(labels) != len(set(labels)) + 1:  # "Launch in three places" is on both tracks
        err("setup/workspace/progress.md: step labels must be unique, apart from the launch step on both tracks")
    skill_text = "\n".join(p.read_text() for p in SKILLS.glob("*/SKILL.md") if p.parent.name not in VENDORED)
    plan = (SKILLS / "today" / "plan.md").read_text()
    for label in sorted(set(labels)):
        if f'"{label}"' not in skill_text:
            err(f"no skill ticks the step \"{label}\". Add the tick to the skill that finishes it")
        if label not in plan and label not in {"Workspace created", "Company files drafted", "Company files confirmed", "Weekly brief scheduled", "Homepage headline rewritten"}:
            err(f"today/plan.md does not mention the step \"{label}\"")
    for quoted in set(re.findall(r'[Tt]ick "([^"]+)"', skill_text)):
        if quoted not in labels:
            err(f"a skill ticks \"{quoted}\", which is not a step in the progress template")


def check_pipeline_format():
    sys.path.insert(0, str(SKILLS / "prospect-list" / "scripts"))
    import pipeline  # noqa: E402
    header = ",".join(pipeline.COLUMNS)
    template = (SKILLS / "setup" / "workspace" / "sales" / "pipeline.csv").read_text().strip()
    if template != header:
        err("setup/workspace/sales/pipeline.csv header differs from pipeline.py COLUMNS")
    if header not in (SKILLS / "prospect-list" / "references" / "pipeline-format.md").read_text():
        err("prospect-list/references/pipeline-format.md header differs from pipeline.py COLUMNS")
    with open(ROOT / "examples" / "b2b" / "sales" / "pipeline.csv", newline="") as handle:
        if next(csv.reader(handle)) != pipeline.COLUMNS:
            err("examples/b2b/sales/pipeline.csv header differs from pipeline.py COLUMNS")


def run(args):
    return subprocess.run([sys.executable, "-I"] + args, capture_output=True, text=True, cwd=ROOT)


def check_scripts_on_examples():
    for name in ("b2b", "b2c"):
        result = run(["skills/dashboard/scripts/build.py", f"examples/{name}", "--json"])
        if result.returncode != 0:
            err(f"dashboard build fails on examples/{name}: {result.stdout.strip() or result.stderr.strip()}")
            continue
        data = json.loads(result.stdout)
        if not data["steps_total"] or not data["product"] or not data["company"]:
            err(f"dashboard data for examples/{name} is missing steps, product or company files")
    result = run(["skills/prospect-list/scripts/pipeline.py", "check", "examples/b2b/sales/pipeline.csv", "--today", "2026-11-20"])
    if "ERROR" in result.stdout:
        err("examples/b2b/sales/pipeline.csv fails its own check:\n" + result.stdout)
    template = (SKILLS / "dashboard" / "assets" / "dashboard.html").read_text()
    if template.count("/*KEEP100_DATA*/") != 1:
        err("dashboard/assets/dashboard.html must contain the data marker exactly once")
    if re.search(r"""(?:src|href)=["']https?://""", template):
        err("dashboard/assets/dashboard.html loads something from the network. It must be self-contained")
    banned = (SKILLS / "writing-check" / "banned.txt").read_text()
    for section in ("[words]", "[phrases]", "[review]", "[email]"):
        if section not in banned:
            err(f"writing-check/banned.txt is missing the {section} section")


def fired_skills(text):
    """Skills a skill-fired grader accepts, in order. The first is the one the case is about."""
    found = re.search(r'\)\?(?:\(\?:([a-z0-9|-]+)\)|([a-z0-9-]+))"', text)
    return (found.group(1) or found.group(2)).split("|") if found else []


def check_evals(names):
    folder = ROOT / "evals"
    cases = sorted(p.parent for p in folder.glob("*/prompt.md"))
    if not cases:
        err("evals/ has no cases")
    for case in cases:
        where = rel(case)
        fields, body = frontmatter((case / "prompt.md").read_text())
        if fields is None or not body.strip():
            err(f"{where}/prompt.md needs frontmatter and a prompt")
            continue
        for key in fields:
            if key not in PROMPT_KEYS:
                err(f"{where}/prompt.md: unknown key {key!r}")
        graders = sorted((case / "graders").glob("*.md"))
        if not graders:
            err(f"{where}: no graders")
        for grader in graders:
            g_fields, g_body = frontmatter(grader.read_text())
            kind = (g_fields or {}).get("type")
            if kind not in GRADER_TYPES:
                err(f"{rel(grader)}: type {kind!r} is not a grader type")
            if kind == "llm" and not g_body.strip():
                err(f"{rel(grader)}: an llm grader needs a rubric")
            if kind == "tool_used":
                for skill in fired_skills((g_fields or {}).get("input_match", "")):
                    if skill not in names:
                        err(f"{rel(grader)}: expects the skill {skill}, which does not exist")
        spec = case / "case.yaml"
        if spec.exists():
            text = spec.read_text()
            named = re.search(r"^name:\s*(\S+)", text, re.M)
            if not named or named.group(1) != case.name:
                err(f"{where}/case.yaml: name must be {case.name}")
            if 'schema_version: "1.1"' not in text:
                err(f"{where}/case.yaml: needs schema_version: \"1.1\"")
            script = re.search(r"scaffold_script:\s*(\S+)", text)
            if script and not (case / script.group(1)).exists():
                err(f"{where}/case.yaml: scaffold script {script.group(1)} is missing")
    covered = set()
    for grader in folder.glob("*/graders/*.md"):
        covered |= set(fired_skills(grader.read_text())[:1])
    for name in names:
        if name not in VENDORED and name not in covered:
            err(f"no eval case checks that the {name} skill fires")


def check_docs(names):
    for path in [ROOT / "README.md", ROOT / "START-HERE.md", ROOT / "CREDITS.md"] + sorted((ROOT / "docs").rglob("*.md")):
        text = path.read_text()
        for needle in ("—", "releases/latest", "can't install plugins", "cannot install skills"):
            if needle in text and "adr/0001" not in rel(path):
                err(f"{rel(path)}: contains {needle!r}")
        for skill in re.findall(r"keep100:([a-z0-9-]+)", text):
            if skill not in names:
                err(f"{rel(path)}: mentions keep100:{skill}, which does not exist")
        for link in re.findall(r"\]\((?!https?:|#|mailto:)([^)#]+)", text):
            if not (path.parent / link).exists():
                err(f"{rel(path)}: link to {link} is broken")


def main():
    _, contract = check_manifests()
    names = check_skills()
    check_contract(contract)
    check_steps()
    check_pipeline_format()
    check_scripts_on_examples()
    check_evals(names)
    check_docs(names)
    for line in ERRORS:
        print("ERROR  ", line)
    print(f"{len(ERRORS)} errors" if ERRORS else f"OK. {len(names)} skills checked")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
