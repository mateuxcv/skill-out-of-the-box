"""Behavioral tests for the repository validator, not for the AI agent."""

import copy
import json
from pathlib import Path
import tempfile
import unittest

from scripts.validate_skill import EXPECTED, SKILL_PATH, validate


CASE = {
    "id": 1,
    "name": "Example case",
    "prompt": "Propose a useful workflow improvement.",
    "context": "Proposal only; no network required.",
    "should_trigger": True,
    "expected_output": "A concrete comparison and falsifying test.",
    "assertions": ["The proposal compares an existing-stack alternative."],
    "files": [],
}


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        self.skill = self.root / SKILL_PATH
        for filename in EXPECTED:
            path = self.skill / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Reference\n", encoding="utf-8")
        self.metadata = (
            '---\nname: out-of-the-box\ndescription: "Creative B2B product decisions."\n'
            '---\n\n# Out of the Box\n'
        )
        self.write_main(self.metadata)
        for filename in ("README.md", "CONTRIBUTING.md"):
            (self.root / filename).write_text("# Documentation\n", encoding="utf-8")
        self.write_cases([copy.deepcopy(CASE)])

    def write_main(self, text):
        (self.skill / "SKILL.md").write_text(text, encoding="utf-8")

    def write_cases(self, cases):
        self.case_file = self.skill / "evals" / "evals.json"
        self.case_file.write_text(
            json.dumps({"skill_name": "out-of-the-box", "evals": cases}),
            encoding="utf-8",
        )

    def errors(self):
        return validate(self.root, verbose=False)

    def assert_error(self, fragment):
        errors = self.errors()
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_valid_package_and_negative_control(self):
        case = copy.deepcopy(CASE)
        case["should_trigger"] = False
        self.write_cases([case])
        self.assertEqual(self.errors(), [])

    def test_missing_required_reference(self):
        (self.skill / "references" / "creative-methods.md").unlink()
        self.assert_error("Missing file: references/creative-methods.md")

    def test_broken_links_in_all_document_scopes(self):
        for filename in ("README.md", "CONTRIBUTING.md", "docs/review.md"):
            with self.subTest(filename=filename):
                path = self.root / filename
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("[Missing](missing-file.md)\n", encoding="utf-8")
                self.assert_error(f"Broken local link in {path.name}")
                path.write_text("# Fixed\n", encoding="utf-8")

    def test_external_links_and_heading_only_links_are_not_fetched(self):
        (self.root / "README.md").write_text(
            "[External](https://example.invalid/doc) [Heading](#unvalidated-anchor)\n",
            encoding="utf-8",
        )
        self.assertEqual(self.errors(), [])

    def test_duplicate_metadata(self):
        self.write_main(self.metadata.replace("name: out-of-the-box", "name: out-of-the-box\nname: duplicate"))
        self.assert_error("Duplicate field: name")

    def test_invalid_frontmatter(self):
        self.write_main("# Missing metadata\n")
        self.assert_error("must start with YAML frontmatter")

    def test_blank_or_overlong_description(self):
        for description in ("   ", "x" * 1025):
            with self.subTest(length=len(description)):
                self.write_main(self.metadata.replace("Creative B2B product decisions.", description))
                self.assert_error("Description must be")

    def test_core_context_budget(self):
        self.write_main(self.metadata + "\n" * 500)
        self.assert_error("below 500 lines")

    def test_invalid_json(self):
        self.case_file.write_text("{", encoding="utf-8")
        self.assert_error("Cannot read evaluation cases")

    def test_invalid_top_level_evaluation_data(self):
        self.case_file.write_text("[]", encoding="utf-8")
        self.assert_error("must be an object")

    def test_duplicate_case_identifiers(self):
        self.write_cases([copy.deepcopy(CASE), copy.deepcopy(CASE)])
        self.assert_error("duplicate id")

    def test_trigger_is_a_boolean_not_a_string(self):
        case = copy.deepcopy(CASE)
        case["should_trigger"] = "false"
        self.write_cases([case])
        self.assert_error("boolean should_trigger")

    def test_boolean_is_not_an_integer_case_id(self):
        case = copy.deepcopy(CASE)
        case["id"] = True
        self.write_cases([case])
        self.assert_error("positive integer id")

    def test_cases_require_context_and_assertions(self):
        case = copy.deepcopy(CASE)
        case["context"] = ""
        case["assertions"] = []
        self.write_cases([case])
        self.assert_error("nonempty text for context")
        self.assert_error("text assertions")

    def test_fixture_must_exist(self):
        case = copy.deepcopy(CASE)
        case["files"] = ["evals/files/missing.csv"]
        self.write_cases([case])
        self.assert_error("missing fixture")

    def test_fixture_cannot_escape_skill(self):
        case = copy.deepcopy(CASE)
        case["files"] = ["../../../../README.md"]
        self.write_cases([case])
        self.assert_error("fixture must stay inside the skill")


if __name__ == "__main__":
    unittest.main()
