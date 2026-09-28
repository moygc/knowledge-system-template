#!/usr/bin/env python3
r"""
export_public_release.py

Produces a clean, verified export of the files eligible for public
distribution from a private Knowledge_System working repository,
following the release procedure defined in DEPLOYMENT.md section 6.

This script never pushes to a remote and never commits on your behalf.
It only prepares and verifies a clean directory for you to review.

Usage:
    python export_public_release.py <source_repo> <output_dir> [options]

Example:
    python export_public_release.py \
        C:\Users\SPARTAN PC\Local_Work\SYSTEMS\Knowledge_System \
        C:\Users\SPARTAN PC\Local_Work\release_20260928 \
        --scrub-patterns C:\Users\SPARTAN PC\.release_scrub.txt \
        --apply
"""

from __future__ import annotations

import argparse
import fnmatch
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Mirrors DEPLOYMENT.md section 2 (Distribution Contract). Keep in sync
# if the contract changes; the script also cross-checks this list
# against the repository's actual tracked files, so a mismatch between
# this list and .gitignore is reported rather than silently trusted.
CONTRACT_PATTERNS = [
    "README.md",
    "system_definition.md",
    "system_manifest.yaml",
    "DEPLOYMENT.md",
    "AGENTS.md",
    "CLAUDE.md",
    ".gitignore",
    ".gitattributes",
    "LICENSE*",
    "00_Inbox/README.md",
    "01_Knowledge/README.md",
    "02_Learning/README.md",
    "02_Learning/Courses/README.md",
    "03_Library/README.md",
    "04_Templates/**",
    "01_Knowledge/Concepts/.gitkeep",
    "01_Knowledge/Models/.gitkeep",
    "01_Knowledge/Methods/.gitkeep",
    "01_Knowledge/Frameworks/.gitkeep",
    "03_Library/Sources/.gitkeep",
    "03_Library/Records/.gitkeep",
]

# Built-in scrub checks, always run regardless of a custom pattern file.
EM_DASH = "\u2014"
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
BIBTEX_ENTRY_RE = re.compile(r"^@\w+\{", re.MULTILINE)


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def tracked_files(repo: Path) -> list[str]:
    output = run_git(repo, "ls-files")
    return [line for line in output.splitlines() if line]


def matches_contract(path: str) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in CONTRACT_PATTERNS)


def load_scrub_patterns(path: Path | None) -> list[str]:
    if path is None:
        return []
    if not path.exists():
        print(f"warning: scrub pattern file not found: {path}", file=sys.stderr)
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def scan_file(content: str, custom_patterns: list[str]) -> list[str]:
    findings = []
    if EM_DASH in content:
        findings.append("contains U+2014 (em dash)")
    if EMAIL_RE.search(content):
        findings.append("contains what looks like an email address")
    if BIBTEX_ENTRY_RE.search(content):
        findings.append("contains a BibTeX entry (@type{...})")
    for pattern in custom_patterns:
        if pattern in content:
            findings.append(f"matches custom scrub pattern: {pattern!r}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_repo", type=Path, help="Path to the private working repository")
    parser.add_argument(
        "output_dir",
        type=Path,
        help="Path to write the clean export (created fresh; must not already exist)",
    )
    parser.add_argument(
        "--scrub-patterns",
        type=Path,
        default=None,
        help="Optional text file of extra literal strings to flag, one per line "
        "(keep this file private, never commit it)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually write the export directory. Without this flag, only the report "
        "is printed (dry run).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Write the export even if scrub findings were reported. Use only after "
        "reviewing the findings yourself.",
    )
    args = parser.parse_args()

    source = args.source_repo.resolve()
    if not (source / ".git").exists():
        print(f"error: {source} is not a git repository", file=sys.stderr)
        return 2

    files = tracked_files(source)
    if not files:
        print("error: no tracked files found; refusing to produce an empty export", file=sys.stderr)
        return 2

    off_contract = [f for f in files if not matches_contract(f)]
    custom_patterns = load_scrub_patterns(args.scrub_patterns)

    findings_by_file: dict[str, list[str]] = {}
    for rel_path in files:
        full_path = source / rel_path
        try:
            content = full_path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        findings = scan_file(content, custom_patterns)
        if findings:
            findings_by_file[rel_path] = findings

    print(f"Tracked files in {source}: {len(files)}")
    print()

    if off_contract:
        print(
            f"OFF-CONTRACT FILES ({len(off_contract)}): tracked but not matched by any "
            "pattern in DEPLOYMENT.md section 2"
        )
        for f in off_contract:
            print(f"  - {f}")
        print()

    if findings_by_file:
        print(f"SCRUB FINDINGS ({len(findings_by_file)} file(s)):")
        for f, findings in findings_by_file.items():
            print(f"  {f}:")
            for finding in findings:
                print(f"    - {finding}")
        print()

    has_blockers = bool(off_contract) or bool(findings_by_file)

    if has_blockers and not args.force:
        print("Export NOT written. Review the findings above.")
        print(
            "Re-run with --force once you have reviewed them and confirm they are safe "
            "to include, or fix the underlying files (or DEPLOYMENT.md section 2) and "
            "re-run."
        )
        return 1

    if not args.apply:
        print("Dry run only (no --apply given). No files were written.")
        return 0

    if args.output_dir.exists():
        print(
            f"error: {args.output_dir} already exists; refusing to overwrite. "
            "Remove it or pick a new path.",
            file=sys.stderr,
        )
        return 2

    for rel_path in files:
        src = source / rel_path
        dst = args.output_dir / rel_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    print(f"Clean export written to: {args.output_dir}")
    print(f"{len(files)} file(s) copied. No .git directory included.")
    print(
        "Next: review the directory yourself, then copy it over your public repository's "
        "working tree, `git add`, commit, and push manually. This script never does that "
        "for you."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
