"""Validate this skill's structure and its intentionally simple frontmatter.

Standard library only. This is not a general YAML or behavioral validator.
"""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".opencode" / "skills" / "out-of-the-box"
EXPECTED = (
    "SKILL.md",
    "references/creative-methods.md",
    "references/research-and-selection.md",
    "references/b2b-design-and-architecture.md",
    "references/evaluation.md",
    "assets/decision-brief.md",
)


def validate():
    errors = []
    for relative in EXPECTED:
        if not (SKILL / relative).is_file():
            errors.append(f"Missing file: {relative}")

    main = SKILL / "SKILL.md"
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
    if name != SKILL.name or len(name) > 64:
        errors.append("Skill name must match its directory and be at most 64 characters.")
    if not isinstance(description, str) or not 1 <= len(description) <= 1024:
        errors.append("Description must be a string of 1-1024 characters.")
    if len(text.splitlines()) >= 500:
        errors.append("Keep SKILL.md below 500 lines for progressive disclosure.")

    documents = sorted(SKILL.rglob("*.md")) + [ROOT / "README.md"]
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

    if not errors:
        print(f"PASS: {len(EXPECTED)} skill files; name and description valid.")
        print(f"PASS: {len(text.splitlines())} lines in SKILL.md; local document links valid.")
        print("Behavioral scenarios require separate evaluation in fresh agent sessions.")
    return errors


if __name__ == "__main__":
    problems = validate()
    for problem in problems:
        print(f"FAIL: {problem}", file=sys.stderr)
    sys.exit(1 if problems else 0)
