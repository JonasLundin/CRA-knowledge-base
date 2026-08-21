#!/usr/bin/env python3
"""Validate the CRA OKF bundle and its publication constraints."""

from __future__ import annotations

import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import unquote

import yaml


RESERVED = {"index.md", "log.md"}
REQUIRED = {
    "type",
    "title",
    "description",
    "category",
    "status",
    "generated",
    "stale_after",
    "sources",
    "x-cra",
}
STATUSES = {"draft", "stable", "deprecated"}
CATEGORIES = {
    "law",
    "requirement",
    "guidance",
    "standard",
    "product",
    "role",
    "procedure",
    "authority",
    "timeline",
    "glossary",
}
LINK_RE = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")
FOOTNOTE_RE = re.compile(r"\[\^([^]]+)]")
SCRIPT_RE = re.compile(r"<(?:script|iframe|object|embed)\b", re.IGNORECASE)

errors: list[str] = []
warnings: list[str] = []


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return text[4:end], text[end + 5 :]


def parse_datetime(value: object) -> datetime | None:
    if isinstance(value, datetime):
        return value if value.tzinfo else None
    if isinstance(value, date):
        return datetime(value.year, value.month, value.day, tzinfo=timezone.utc)
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo:
        return parsed
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return parsed.replace(tzinfo=timezone.utc)
    return None


def check_links(path: Path, root: Path, body: str) -> None:
    for raw_target in LINK_RE.findall(body):
        target = unquote(raw_target.split("#", 1)[0].strip())
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = root / target.lstrip("/") if target.startswith("/") else path.parent / target
        if target.endswith("/"):
            resolved /= "index.md"
        if not resolved.resolve().is_relative_to(root.resolve()):
            errors.append(f"{path}: internal link escapes bundle: {raw_target}")
        elif not resolved.exists():
            warnings.append(f"{path}: unresolved internal link: {raw_target}")


def check_reserved(path: Path, root: Path, text: str) -> None:
    front_raw, body = split_frontmatter(text)
    if front_raw is not None:
        if path != root / "index.md":
            errors.append(f"{path}: reserved file must not have frontmatter")
        else:
            try:
                front = yaml.safe_load(front_raw) or {}
            except yaml.YAMLError as exc:
                errors.append(f"{path}: invalid root index frontmatter: {exc}")
                return
            if front != {"okf_version": "0.2"}:
                errors.append(f'{path}: root index must declare only okf_version: "0.2"')
    check_links(path, root, body)


def check_sources(path: Path, front: dict[str, object], body: str) -> None:
    raw_sources = front.get("sources")
    if not isinstance(raw_sources, list) or not raw_sources:
        errors.append(f"{path}: sources must be a non-empty list")
        return

    source_ids: set[str] = set()
    for position, source in enumerate(raw_sources, 1):
        if not isinstance(source, dict):
            errors.append(f"{path}: source {position} is not a mapping")
            continue
        resource = source.get("resource")
        if not isinstance(resource, str) or not resource.startswith(("http://", "https://", "/", "./", "../")):
            errors.append(f"{path}: source {position} has no valid resource")
        source_id = source.get("id")
        if source_id is not None:
            if not isinstance(source_id, str) or not source_id.strip():
                errors.append(f"{path}: source {position} has an invalid id")
            elif source_id in source_ids:
                errors.append(f"{path}: duplicate source id {source_id!r}")
            else:
                source_ids.add(source_id)

    references = set(FOOTNOTE_RE.findall(body))
    definitions = set(re.findall(r"(?m)^\[\^([^]]+)]:", body))
    for reference in references - source_ids:
        errors.append(f"{path}: footnote {reference!r} has no matching sources[].id")
    for definition in definitions - source_ids:
        errors.append(f"{path}: footnote definition {definition!r} has no matching sources[].id")


def check_concept(path: Path, root: Path, text: str) -> None:
    front_raw, body = split_frontmatter(text)
    if front_raw is None:
        errors.append(f"{path}: missing YAML frontmatter")
        return
    try:
        front = yaml.safe_load(front_raw)
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid YAML frontmatter: {exc}")
        return
    if not isinstance(front, dict):
        errors.append(f"{path}: frontmatter must be a mapping")
        return

    missing = REQUIRED - set(front)
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(sorted(missing))}")
    if "id" in front:
        errors.append(f"{path}: concept ID is its path; remove redundant id field")
    for field in ("type", "title", "description"):
        if field in front and (not isinstance(front[field], str) or not front[field].strip()):
            errors.append(f"{path}: {field} must be a non-empty string")
    if front.get("status") not in STATUSES:
        errors.append(f"{path}: invalid status {front.get('status')!r}")
    if front.get("category") not in CATEGORIES:
        errors.append(f"{path}: invalid category {front.get('category')!r}")

    generated = front.get("generated")
    if not isinstance(generated, dict) or not generated.get("by") or parse_datetime(generated.get("at")) is None:
        errors.append(f"{path}: generated requires by and an offset-aware ISO 8601 at")
    if parse_datetime(front.get("stale_after")) is None:
        errors.append(f"{path}: stale_after must be an ISO 8601 date or offset-aware datetime")

    extension = front.get("x-cra")
    if not isinstance(extension, dict):
        errors.append(f"{path}: x-cra must be a mapping")
    elif parse_datetime(extension.get("checked_at")) is None:
        errors.append(f"{path}: x-cra.checked_at must be an ISO 8601 date or offset-aware datetime")

    if front.get("status") == "stable" and not front.get("verified"):
        errors.append(f"{path}: stable concept requires verified metadata")
    if front.get("type") == "Standard" and isinstance(extension, dict):
        if extension.get("presumption_of_conformity") is True:
            if extension.get("ojeu_cited") is not True or not extension.get("ojeu_reference"):
                errors.append(f"{path}: presumption of conformity requires an OJEU citation reference")

    if SCRIPT_RE.search(body):
        errors.append(f"{path}: executable or embedded HTML is not allowed")
    check_sources(path, front, body)
    check_links(path, root, body)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "wiki").resolve()
    if not root.is_dir():
        sys.exit(f"not a directory: {root}")

    all_files = sorted(path for path in root.rglob("*") if path.is_file() or path.is_symlink())
    for path in all_files:
        if path.is_symlink():
            errors.append(f"{path}: symlinks are not allowed")
            continue
        if path.suffix.lower() != ".md":
            errors.append(f"{path}: only Markdown files are allowed in the bundle")
            continue
        text = path.read_text(encoding="utf-8")
        if path.name in RESERVED:
            check_reserved(path, root, text)
        else:
            check_concept(path, root, text)

    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error:   {error}")

    concepts = sum(1 for path in all_files if path.suffix.lower() == ".md" and path.name not in RESERVED)
    print(f"\n{len(all_files)} files ({concepts} concepts), {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
