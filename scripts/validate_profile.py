#!/usr/bin/env python3
"""Validate the public profile without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_TEXT = (
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "SUPPORT.md",
)
REQUIRED_FILES = (*PUBLIC_TEXT, "LICENSE")
REQUIRED_README_TEXT = (
    "Danilo Díaz Tarascó",
    "CTO",
    "Electronic",
    "Selected open-source work",
    "ddtdanilo.github.io",
)
PROHIBITED_README_MARKUP = (
    "<img",
    "<table",
    "img.shields.io",
    "github-readme-stats",
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*]\(([^)\s]+)(?:\\s+[\"'][^\"']*[\"'])?\)")
HTML_LINK = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
ACTION_REF = re.compile(r"^\s*uses:\s*([^@\s]+)@([^\s#]+)", re.MULTILINE)
FULL_SHA = re.compile(r"[0-9a-f]{40}")


class ValidationError(RuntimeError):
    """Collect profile validation failures."""


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def check_required_files() -> list[str]:
    return [
        f"missing required file: {path}"
        for path in REQUIRED_FILES
        if not (ROOT / path).is_file()
    ]


def check_identity_and_language() -> list[str]:
    failures: list[str] = []
    readme = read("README.md")

    for value in REQUIRED_README_TEXT:
        if value not in readme:
            failures.append(f"README.md is missing required text: {value!r}")

    for value in PROHIBITED_README_MARKUP:
        if value.casefold() in readme.casefold():
            failures.append(f"README.md contains prohibited decorative markup: {value!r}")

    return failures


def check_links() -> list[str]:
    failures: list[str] = []
    for relative_path in PUBLIC_TEXT:
        text = read(relative_path)
        links = [*MARKDOWN_LINK.findall(text), *HTML_LINK.findall(text)]
        for target in links:
            if target.startswith(("#", "mailto:", "tel:")):
                if target.startswith(("mailto:", "tel:")):
                    failures.append(f"{relative_path}: direct personal contact link is not allowed")
                continue

            parsed = urlparse(target)
            if parsed.scheme:
                if parsed.scheme != "https":
                    failures.append(f"{relative_path}: non-HTTPS link: {target}")
                continue

            local_path = target.split("#", maxsplit=1)[0]
            if local_path and not (ROOT / local_path).exists():
                failures.append(f"{relative_path}: missing local link target: {target}")
    return failures


def check_workflow_pinning() -> list[str]:
    failures: list[str] = []
    workflow_dir = ROOT / ".github/workflows"
    for workflow in (*workflow_dir.glob("*.yml"), *workflow_dir.glob("*.yaml")):
        text = workflow.read_text(encoding="utf-8")
        for action, reference in ACTION_REF.findall(text):
            if not FULL_SHA.fullmatch(reference):
                failures.append(
                    f"{workflow.relative_to(ROOT)}: {action} is not pinned to a full commit SHA"
                )
    return failures


def main() -> int:
    checks = (
        check_required_files,
        check_identity_and_language,
        check_links,
        check_workflow_pinning,
    )
    failures = [failure for check in checks for failure in check()]
    if failures:
        print("Profile validation failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("Profile validation passed.")
    print(f"Checked {len(REQUIRED_FILES)} required files and {len(PUBLIC_TEXT)} content files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
