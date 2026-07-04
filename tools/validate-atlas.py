#!/usr/bin/env python3
"""Dependency-free Atlas repository validator.

This validator intentionally avoids third-party YAML packages so it can run on a
fresh machine. It performs structural, reference, JSON, and safety checks that
cover the Atlas framework conventions.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_ATLAS_FILES = [
    "README.md",
    "manifest.yaml",
    "index.yaml",
    "capabilities.yaml",
    "contexts.yaml",
    "principles.md",
    "ATS.md",
]

REQUIRED_SCHEMAS = [
    "schemas/manifest.schema.json",
    "schemas/index.schema.json",
    "schemas/capabilities.schema.json",
    "schemas/agent.schema.json",
    "schemas/rule.schema.json",
    "schemas/context.schema.json",
]

REFERENCE_FILES = ["index.yaml", "capabilities.yaml", "contexts.yaml"]
REFERENCE_PATTERN = re.compile(
    r"(?:^\s*-\s+|:\s+)([A-Za-z0-9_./-]+\.(?:md|yaml|json))\s*$"
)
SECRET_PATTERNS = [
    re.compile(r"(?i)\b(api[_-]?key|secret|password|token|private[_-]?key)\s*[:=]\s*['\"]?[^\s'\"]{8,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY-----"),
]


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def add_error(errors: list[str], message: str) -> None:
    errors.append(f"ERROR: {message}")


def add_warning(warnings: list[str], message: str) -> None:
    warnings.append(f"WARN: {message}")


def check_required_files(atlas: Path, errors: list[str]) -> None:
    for item in REQUIRED_ATLAS_FILES + REQUIRED_SCHEMAS:
        path = atlas / item
        if not path.exists():
            add_error(errors, f"Missing required Atlas file: .atlas/{item}")
        elif path.is_file() and path.stat().st_size == 0:
            add_error(errors, f"Required Atlas file is empty: .atlas/{item}")


def check_json_files(atlas: Path, errors: list[str]) -> None:
    for path in sorted((atlas / "schemas").glob("*.json")):
        try:
            json.loads(read(path))
        except json.JSONDecodeError as exc:
            add_error(errors, f"Invalid JSON in .atlas/{rel(path, atlas)}: {exc}")


def extract_references(text: str) -> set[str]:
    refs: set[str] = set()
    for line in text.splitlines():
        match = REFERENCE_PATTERN.search(line)
        if match:
            refs.add(match.group(1))
    return refs


def check_references(atlas: Path, errors: list[str], warnings: list[str]) -> None:
    refs: set[str] = set()
    for item in REFERENCE_FILES:
        path = atlas / item
        if path.exists():
            refs.update(extract_references(read(path)))

    for ref in sorted(refs):
        target = atlas / ref
        if not target.exists():
            add_error(errors, f"Broken Atlas reference: .atlas/{ref}")

    for line in read(atlas / "contexts.yaml").splitlines():
        stripped = line.strip()
        if stripped.startswith("- ") and stripped.endswith("/"):
            folder = stripped[2:]
            if not (atlas / folder).exists():
                add_error(errors, f"Broken Atlas folder reference: .atlas/{folder}")
            elif not any((atlas / folder).iterdir()):
                add_warning(warnings, f"Referenced folder is empty: .atlas/{folder}")


def require_text(path: Path, root: Path, required: list[str], errors: list[str]) -> None:
    text = read(path)
    for item in required:
        if item not in text:
            add_error(errors, f".atlas/{rel(path, root)} missing required field or section: {item}")


def check_agents(atlas: Path, errors: list[str]) -> None:
    required = [
        "agent:",
        "  id:",
        "  name:",
        "  version:",
        "  status:",
        "  instruction:",
        "  inherits:",
        "  can:",
        "  cannot:",
        "  inputs:",
        "  outputs:",
        "  definition_of_done:",
    ]
    for path in sorted((atlas / "agents").glob("*.yaml")):
        require_text(path, atlas, required, errors)
        text = read(path)
        match = re.search(r"^\s+instruction:\s+(.+)$", text, re.MULTILINE)
        if match and not (atlas / match.group(1).strip()).exists():
            add_error(errors, f".atlas/{rel(path, atlas)} references missing instruction {match.group(1).strip()}")


def check_rules(atlas: Path, errors: list[str]) -> None:
    required = [
        "rule:",
        "  id:",
        "  name:",
        "  version:",
        "  status:",
        "  purpose:",
        "  applies_to:",
        "  requirements:",
        "  prohibited:",
        "  validation:",
    ]
    for path in sorted((atlas / "rules").glob("*.yaml")):
        require_text(path, atlas, required, errors)


def check_contexts(atlas: Path, errors: list[str]) -> None:
    require_text(
        atlas / "contexts.yaml",
        atlas,
        ["version:", "purpose:", "rules:", "contexts:", "include:", "exclude:"],
        errors,
    )


def check_secret_patterns(atlas: Path, errors: list[str]) -> None:
    scanned_suffixes = {".md", ".yaml", ".yml", ".json"}
    for path in sorted(atlas.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in scanned_suffixes:
            continue
        text = read(path)
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                add_error(errors, f"Possible secret-like value found in .atlas/{rel(path, atlas)}")
                break


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Atlas framework files.")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    args = parser.parse_args()

    repo = Path(args.root).resolve()
    atlas = repo / ".atlas"
    errors: list[str] = []
    warnings: list[str] = []

    if not atlas.exists():
        print("ERROR: .atlas directory not found")
        return 1

    check_required_files(atlas, errors)
    check_json_files(atlas, errors)
    check_references(atlas, errors, warnings)
    check_agents(atlas, errors)
    check_rules(atlas, errors)
    check_contexts(atlas, errors)
    check_secret_patterns(atlas, errors)

    for warning in warnings:
        print(warning)
    for error in errors:
        print(error)

    if errors:
        print(f"Atlas validation failed: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"Atlas validation passed: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
