"""Tests for the scripts the Keep100 skills run. No model calls, no network.

Run from the repo root:  python3 -m unittest discover tests
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPELINE = ROOT / "skills" / "prospect-list" / "scripts" / "pipeline.py"
CHECK = ROOT / "skills" / "writing-check" / "scripts" / "check.py"
BUILD = ROOT / "skills" / "dashboard" / "scripts" / "build.py"
AUDIT = ROOT / "skills" / "workspace-audit" / "scripts" / "audit.py"
VALIDATE = ROOT / "scripts" / "validate.py"
B2B = ROOT / "examples" / "b2b"
B2C = ROOT / "examples" / "b2c"
TODAY = "2026-11-20"


def run(script, *args):
    result = subprocess.run([sys.executable, str(script), *map(str, args)], capture_output=True, text=True, cwd=ROOT)
    return result.returncode, result.stdout + result.stderr


class Workspace(unittest.TestCase):
    """Gives each test a throwaway copy of an example workspace."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.ws = self.tmp / "ws"
        shutil.copytree(B2B, self.ws)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def edit(self, relative, old, new):
        path = self.ws / relative
        text = path.read_text()
        self.assertIn(old, text)
        path.write_text(text.replace(old, new))


class PipelineTests(Workspace):
    def setUp(self):
        super().setUp()
        self.csv = self.ws / "sales" / "pipeline.csv"

    def test_example_passes_check(self):
        code, out = run(PIPELINE, "check", self.csv, "--today", TODAY)
        self.assertEqual(code, 0, out)
        self.assertNotIn("ERROR", out)

    def test_low_queue_is_a_warning(self):
        _, out = run(PIPELINE, "check", self.csv, "--today", TODAY)
        self.assertIn("Rebuild the list", out)

    def test_reply_must_end_the_sequence(self):
        self.edit("sales/pipeline.csv", ",A,replied,2026-11-14,", ",A,active,2026-11-14,")
        code, out = run(PIPELINE, "check", self.csv, "--today", TODAY)
        self.assertEqual(code, 1)
        self.assertIn("A reply ends the sequence", out)

    def test_opt_out_must_be_stopped(self):
        self.edit("sales/pipeline.csv", ",A,stopped,", ",A,lost,")
        code, out = run(PIPELINE, "check", self.csv, "--today", TODAY)
        self.assertEqual(code, 1)
        self.assertIn("opted out but status is not stopped", out)

    def test_email_needs_a_source(self):
        self.edit("sales/pipeline.csv", "ana@costa.example,published", "ana@costa.example,")
        code, out = run(PIPELINE, "check", self.csv, "--today", TODAY)
        self.assertEqual(code, 1)
        self.assertIn("email has no email_source", out)

    def test_bad_date_is_reported(self):
        self.edit("sales/pipeline.csv", "2026-11-11,https://costa.example/vagas", "11/11/2026,https://costa.example/vagas")
        code, out = run(PIPELINE, "check", self.csv, "--today", TODAY)
        self.assertEqual(code, 1)
        self.assertIn("not a YYYY-MM-DD date", out)

    def test_due_lists_follow_ups_and_skips_people_who_replied(self):
        code, out = run(PIPELINE, "due", self.csv, "--today", "2026-11-21", "--new", "5")
        self.assertEqual(code, 0, out)
        follow_ups = out.split("Next steps due")[0]
        self.assertIn("email 3  Tom Okafor", follow_ups)  # first email on the 14th, email 3 is due 7 days later
        self.assertIn("Lena Fischer", follow_ups)     # email 2 was due on day 3
        self.assertNotIn("Priya Nair", follow_ups)    # replied
        self.assertNotIn("Kim Tran", out)             # opted out, never listed anywhere

    def test_due_never_offers_a_stale_trigger(self):
        self.edit("sales/pipeline.csv", "Hiring a receptionist,2026-11-11", "Hiring a receptionist,2026-07-01")
        _, out = run(PIPELINE, "due", self.csv, "--today", TODAY)
        new = out.split("New first emails")[1].split("Held back")[0]
        self.assertNotIn("Ana Costa", new)
        self.assertIn("Held back", out)

    def test_stats_counts_the_funnel(self):
        code, out = run(PIPELINE, "stats", self.csv)
        self.assertEqual(code, 0, out)
        self.assertIn("5 people contacted", out)
        self.assertIn("3 replies", out)
        self.assertIn("Too few sends", out)

    def test_missing_file(self):
        code, out = run(PIPELINE, "check", self.tmp / "nope.csv")
        self.assertEqual(code, 1)
        self.assertIn("does not exist", out)


class WritingCheckTests(Workspace):
    def draft(self, text, *args):
        path = self.tmp / "draft.md"
        path.write_text(text)
        return run(CHECK, path, *args)

    def test_saved_sequence_passes_as_a_template(self):
        code, out = run(CHECK, self.ws / "sales" / "2026-11-14-sequence.md", "--format", "cold-email", "--template",
                        "--brand", self.ws / "company" / "brand.md")
        self.assertEqual(code, 0, out)

    def test_unfilled_placeholder_fails_when_sending(self):
        code, out = run(CHECK, self.ws / "sales" / "2026-11-14-sequence.md", "--format", "cold-email")
        self.assertEqual(code, 1)
        self.assertIn("{first_name}", out)

    def test_banned_words_and_dashes(self):
        code, out = self.draft("We leverage a robust platform — it streamlines everything.\n")
        self.assertEqual(code, 1)
        for term in ("leverage", "robust", "streamline", "dash used as a separator"):
            self.assertIn(term, out)

    def test_brand_can_allow_a_word(self):
        brand = self.tmp / "brand.md"
        brand.write_text("# Brand\n\n## Words we allow\njourney\n\n## Words we never use\nsynergize\n")
        code, out = self.draft("Your running journey starts here.\n", "--brand", brand)
        self.assertEqual(code, 0, out)
        code, out = self.draft("Let's synergize.\n", "--brand", brand)
        self.assertEqual(code, 1)

    def test_plain_words_are_not_flagged(self):
        code, out = self.draft("We built a craftsman's bench. The vitality of the team transformation is fine.\n")
        self.assertEqual(code, 0, out)

    def test_cold_email_limits(self):
        long_body = " ".join(["word"] * 110)
        code, out = self.draft(f"## Email 1\nSubject: late slots\n\nHi Ana,\n\n{long_body}\n\nSee https://example.com\n",
                               "--format", "cold-email")
        self.assertEqual(code, 1)
        self.assertIn("Never over 100", out)
        self.assertIn("No links in emails 1 to 3", out)

    def test_landing_page_limits_and_matching_buttons(self):
        page = ("## 1. Hero\nHeadline: One two three four five six seven eight nine ten eleven\n"
                "Subheadline: Short and clear.\nCTA: Start free trial\nMicrocopy: No card needed\n"
                "## 6. Final CTA\nHeadline: Fill the slot\nCTA: Get started\n")
        code, out = self.draft(page, "--format", "landing-page")
        self.assertEqual(code, 1)
        self.assertIn("headline is 11 words", out)
        self.assertIn("differs from the hero", out)


class DashboardTests(Workspace):
    def data(self, workspace=None):
        code, out = run(BUILD, workspace or self.ws, "--json", "--today", TODAY)
        self.assertEqual(code, 0, out)
        return json.loads(out)

    def test_counts_steps_and_finds_the_next_one(self):
        data = self.data()
        self.assertEqual((data["steps_done"], data["steps_total"]), (18, 23))
        self.assertEqual(data["next"], {"section": "Getting customers (B2B)", "label": "First sales call"})
        self.assertEqual(data["days_in"], 18)
        self.assertEqual(data["product"], "Kneecap")

    def test_skipped_steps_are_not_counted(self):
        skipped = [i for s in self.data()["sections"] for i in s["items"] if i["state"] == "skipped"]
        self.assertEqual(len(skipped), 1)
        self.assertEqual(skipped[0]["label"], "Product emails")
        self.assertTrue(skipped[0]["note"].startswith("skipped:"))

    def test_ticking_a_step_moves_the_dashboard(self):
        self.edit("progress.md", "- [ ] First sales call", "- [x] First sales call")
        data = self.data()
        self.assertEqual(data["steps_done"], 19)
        self.assertEqual(data["next"]["label"], "Launch in three places")

    def test_paying_customer_is_counted(self):
        self.edit("progress.md", "| Date | Customer | Plan |\n|---|---|---|\n",
                  "| Date | Customer | Plan |\n|---|---|---|\n| 2026-11-25 | Northgate Physio | Clinic, founding |\n")
        self.assertEqual(self.data()["paying_customers"], 1)

    def test_reads_company_status_and_pipeline(self):
        data = self.data()
        status = {f["name"]: f["status"] for f in data["company"]}
        self.assertEqual(status["Positioning"], "Provisional")
        self.assertEqual(status["Pricing"], "Confirmed")
        self.assertNotIn("Facts", status)
        self.assertEqual(data["pipeline"], {"reached": 5, "replies": 3, "calls": 0, "paid": 0, "waiting": 2})

    def test_b2c_workspace_has_no_pipeline(self):
        data = self.data(B2C)
        self.assertIsNone(data["pipeline"])
        self.assertEqual(data["next"]["label"], "Positioning")
        self.assertEqual(data["hours_a_day"], "1 hour")

    def test_writes_a_self_contained_page(self):
        out_file = self.tmp / "dash.html"
        code, out = run(BUILD, self.ws, "--out", out_file, "--today", TODAY)
        self.assertEqual(code, 0, out)
        self.assertIn("18 of 23 steps done", out)
        html = out_file.read_text()
        self.assertIn("<title>Kneecap progress</title>", html)
        self.assertNotIn("/*KEEP100_DATA*/", html)
        self.assertNotIn('src="http', html)
        blob = html.split('<script id="keep100-data" type="application/json">')[1].split("</script>")[0]
        self.assertEqual(json.loads(blob)["steps_done"], 18)

    def test_script_tags_in_progress_cannot_break_the_page(self):
        self.edit("progress.md", "Product: Kneecap", "Product: Knee</script><script>alert(1)</script>")
        out_file = self.tmp / "dash.html"
        run(BUILD, self.ws, "--out", out_file, "--today", TODAY)
        html = out_file.read_text()
        self.assertNotIn("</script><script>alert(1)", html)

    def test_fresh_template_builds(self):
        data = self.data(ROOT / "skills" / "setup" / "workspace")
        self.assertEqual(data["steps_done"], 0)
        self.assertEqual(data["product"], "")
        self.assertEqual(data["next"]["label"], "Workspace created")

    def test_no_workspace(self):
        code, out = run(BUILD, self.tmp / "empty")
        self.assertEqual(code, 1)
        self.assertIn("Run Keep100 setup first", out)


class AuditTests(Workspace):
    def test_example_reports_only_unconfirmed_facts(self):
        code, out = run(AUDIT, self.ws, "--today", TODAY)
        self.assertEqual(code, 1)
        lines = [l for l in out.splitlines() if l and not l.endswith("things to look at")]
        self.assertTrue(all(l.startswith("UNCONFIRMED") for l in lines), out)

    def test_duplicate_price_is_found(self):
        self.edit("company/facts.md", "## Results\n", "## Results\n- [confirmed] The Clinic plan costs $79 a month. (source: Maya)\n")
        _, out = run(AUDIT, self.ws, "--today", TODAY)
        self.assertIn("DUPLICATE", out)
        self.assertIn("$79", out)

    def test_stale_file_is_found(self):
        _, out = run(AUDIT, self.ws, "--today", "2027-02-01")
        self.assertIn("STALE", out)
        self.assertIn("company/product.md", out)

    def test_untagged_quote_is_found(self):
        self.edit("company/customers.md", '- [prospect] [verbatim] "The waiting list is a page', '- "The waiting list is a page')
        _, out = run(AUDIT, self.ws, "--today", TODAY)
        self.assertIn("UNTAGGED", out)

    def test_not_a_workspace(self):
        code, out = run(AUDIT, self.tmp)
        self.assertEqual(code, 1)
        self.assertIn("not a Keep100 workspace", out)


class RepoTests(unittest.TestCase):
    def test_validate_passes(self):
        code, out = run(VALIDATE)
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
