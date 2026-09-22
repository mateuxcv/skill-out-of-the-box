"""Validate this skill's structure, evaluation inputs, and local file links.

Standard library only. This is not a general YAML or behavioral validator.
"""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = Path(".opencode") / "skills" / "out-of-the-box"
EXPECTED = (
    "SKILL.md",
    "references/creative-methods.md",
    "references/research-and-selection.md",
    "references/b2b-design-and-architecture.md",
    "references/evaluation.md",
    "assets/decision-brief.md",
    "evals/evals.json",
)


def nonempty_text(value):
    return isinstance(value, str) and bool(value.strip())


def validate_evals(path, skill):
    """Check evaluation inputs, not whether an agent passes their assertions."""
    errors = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return [f"Cannot read evaluation cases: {error}"]
    if not isinstance(payload, dict):
        return ["Evaluation data must be an object."]
    if payload.get("skill_name") != skill.name:
        errors.append("Evaluation skill_name must match the skill directory.")
    cases = payload.get("evals")
    if not isinstance(cases, list) or not cases:
        return errors + ["Evaluation data must contain a nonempty evals list."]

    identifiers = set()
    for index, case in enumerate(cases, 1):
        prefix = f"Evaluation case {index}"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be an object.")
            continue
        identifier = case.get("id")
        if type(identifier) is not int or identifier < 1:
            errors.append(f"{prefix} needs a positive integer id.")
        elif identifier in identifiers:
            errors.append(f"{prefix} has a duplicate id: {identifier}")
        else:
            identifiers.add(identifier)
        for field in ("name", "prompt", "context", "expected_output"):
            if not nonempty_text(case.get(field)):
                errors.append(f"{prefix} needs nonempty text for {field}.")
        if type(case.get("should_trigger")) is not bool:
            errors.append(f"{prefix} needs a boolean should_trigger.")
        assertions = case.get("assertions")
        if not isinstance(assertions, list) or not assertions or not all(
            nonempty_text(assertion) for assertion in assertions
        ):
            errors.append(f"{prefix} needs a nonempty list of text assertions.")
        files = case.get("files")
        if not isinstance(files, list):
            errors.append(f"{prefix} needs a files list (empty is allowed).")
            continue
        for filename in files:
            if not nonempty_text(filename):
                errors.append(f"{prefix} has an invalid fixture path.")
                continue
            target = (skill / filename).resolve()
            if Path(filename).is_absolute() or not target.is_relative_to(skill.resolve()):
                errors.append(f"{prefix} fixture must stay inside the skill: {filename}")
            elif not target.is_file():
                errors.append(f"{prefix} has a missing fixture: {filename}")
    return errors


def validate(root=ROOT, *, verbose=True):
    root = Path(root)
    skill = root / SKILL_PATH
    errors = []
    for relative in EXPECTED:
        if not (skill / relative).is_file():
            errors.append(f"Missing file: {relative}")

    main = skill / "SKILL.md"
    if not main.is_file():
        return errors

    text = main.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    fields = {}
    if not frontmatter:
        errors.append("SKILL.md must start with YAML frontmatter.")
    else:
        for line in frontmatter.group(1).splitlines():
            key, separator, value = line.partition(":")
            if not separator or key not in {"name", "description"}:
                errors.append(f"Unsupported frontmatter line for this validator: {line}")
                continue
            if key in fields:
                errors.append(f"Duplicate field: {key}")
            value = value.strip()
            if value.startswith('"'):
                try:
                    value = json.loads(value)
                except json.JSONDecodeError:
                    errors.append(f"Invalid quoted scalar: {key}")
                    continue
            elif key != "name":
                errors.append(f"Expected a double-quoted scalar: {key}")
            fields[key] = value

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("Invalid skill name.")
    if name != skill.name or (isinstance(name, str) and len(name) > 64):
        errors.append("Skill name must match its directory and be at most 64 characters.")
    if not nonempty_text(description) or len(description) > 1024:
        errors.append("Description must be a string of 1-1024 characters.")
    if len(text.splitlines()) >= 500:
        errors.append("Keep SKILL.md below 500 lines for progressive disclosure.")

    cases_path = skill / "evals" / "evals.json"
    if cases_path.is_file():
        errors.extend(validate_evals(cases_path, skill))

    documents = (
        sorted(skill.rglob("*.md"))
        + sorted((root / "docs").rglob("*.md"))
        + [root / "README.md", root / "CONTRIBUTING.md"]
    )
    for document in documents:
        if not document.is_file():
            errors.append(f"Missing document: {document}")
            continue
        content = document.read_text(encoding="utf-8")
        for link in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", content):
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (document.parent / unquote(parsed.path)).resolve()
            if not target.is_file():
                errors.append(f"Broken local link in {document.name}: {link}")

    if not errors and verbose:
        print(f"PASS: {len(EXPECTED)} skill files; name and description valid.")
        print(f"PASS: {len(text.splitlines())} lines in SKILL.md; local document links valid.")
        print("PASS: Evaluation case structure, identifiers, assertions, and fixture paths valid.")
        print("Behavioral scenarios require separate evaluation in fresh agent sessions.")
    return errors


if __name__ == "__main__":
    problems = validate()
    for problem in problems:
        print(f"FAIL: {problem}", file=sys.stderr)
    sys.exit(1 if problems else 0)
