#!/usr/bin/env python3
"""Validate Obsidian cache notes per docs/contracts/cache-note-schema-v1.md."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

REQUIRED_KEYS = frozenset(
    {
        "uuid",
        "fingerprint",
        "adversarial_status",
        "similarity_gate",
        "embedding_model",
        "schema_version",
        "source",
    }
)
ADV_ALLOWED = frozenset({"tentative", "verified", "deprecated"})
HEADINGS = ("problem", "solution", "why it works", "lessons learned")


def split_frontmatter(raw: str) -> tuple[dict | None, str, str | None]:
    """Return (meta, body, error_message).

    Parses the first YAML block between **line** `---` delimiters only, so `---`
    inside the markdown body does not truncate content (critical for valid notes).
    """
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    if not text.startswith("---\n") and not text.startswith("---\r"):
        if text.lstrip().startswith("---"):
            return None, raw, "frontmatter must start with --- followed by newline"
        return None, raw, "file does not start with YAML frontmatter (---)"
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, raw, "file does not start with YAML frontmatter (---)"
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, raw, "incomplete frontmatter (no closing --- line)"
    yaml_blob = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1 :])
    try:
        meta = yaml.safe_load(yaml_blob)
    except yaml.YAMLError as e:
        return None, body, f"YAML parse error: {e}"
    if meta is None:
        return {}, body, None
    if not isinstance(meta, dict):
        return None, body, "frontmatter must be a YAML mapping (object)"
    return meta, body, None


def validate_source(meta: dict) -> list[str]:
    errs: list[str] = []
    s = meta.get("source")
    if s is None:
        return ["missing_or_empty:source"]
    if isinstance(s, dict):
        if not s.get("project"):
            errs.append("source.project missing")
        if not s.get("context"):
            errs.append("source.context missing")
    elif isinstance(s, str):
        if not s.strip():
            errs.append("source string empty")
    else:
        errs.append("source must be string or mapping with project/context")
    return errs


def find_heading_indices(body: str) -> dict[str, bool]:
    found = {h: False for h in HEADINGS}
    for line in body.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line, re.IGNORECASE)
        if not m:
            continue
        title = m.group(1).strip().lower()
        for h in HEADINGS:
            if title == h:
                found[h] = True
                break
    return found


def validate_file(path: Path) -> list[str]:
    errs: list[str] = []
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return [f"read_error: {e}"]
    meta, body, ferr = split_frontmatter(raw)
    if ferr:
        return [ferr]
    assert meta is not None
    for k in REQUIRED_KEYS:
        if k not in meta or meta[k] is None or meta[k] == "":
            errs.append(f"missing_or_empty:{k}")
    st = meta.get("adversarial_status")
    if st is not None and str(st) not in ADV_ALLOWED:
        errs.append(f"invalid_adversarial_status:{st!r}")
    sv = meta.get("schema_version")
    if sv is not None:
        try:
            if int(sv) != 1:
                errs.append(
                    f"unsupported_schema_version:{sv} (only v1 supported by this validator)"
                )
        except (TypeError, ValueError):
            errs.append(f"invalid_schema_version:{sv!r}")
    if "source" in meta and meta["source"] is not None:
        errs.extend(validate_source(meta))
    heads = find_heading_indices(body)
    for h, ok in heads.items():
        if not ok:
            errs.append(f"missing_section:{h.replace(' ', '_')}")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, required=True, help="Obsidian vault root")
    ap.add_argument(
        "--folder",
        type=str,
        default="00_LLM_Cache",
        help="Subfolder under root (default 00_LLM_Cache)",
    )
    ap.add_argument("--json", action="store_true", help="Print machine-readable report")
    args = ap.parse_args()
    base = args.root / args.folder
    if not base.is_dir():
        print(f"Not a directory: {base}", file=sys.stderr)
        return 2

    md_files = sorted(base.rglob("*.md"))
    report: dict[str, list[str]] = {}
    for p in md_files:
        rel = p.relative_to(args.root)
        errs = validate_file(p)
        if errs:
            report[str(rel)] = errs

    if args.json:
        print(json.dumps({"invalid": report, "checked": len(md_files)}, indent=2))
        return 1 if report else 0
    if not report:
        print(f"OK: {len(md_files)} markdown file(s) under {base}")
        return 0
    print(f"FAILED: {len(report)} file(s) with errors (of {len(md_files)}):\n")
    for rel, errs in sorted(report.items()):
        print(f"  {rel}")
        for e in errs:
            print(f"    - {e}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
