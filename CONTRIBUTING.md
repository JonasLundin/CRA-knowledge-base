# Contributing

Contributions should improve accuracy, coverage, or source freshness without turning the bundle into legal advice.

## Content Rules

1. Condense the essence in original wording.
2. Cite the primary source and exact article, paragraph, annex point, work item, or OJEU reference.
3. Distinguish binding law, non-binding guidance, drafts, final standards, and OJEU-cited harmonised standards.
4. Do not copy full instruments, long passages, standards clauses, tables, figures, PDFs, or spreadsheets.
5. Do not submit private compliance evidence, personal data, credentials, or confidential material.
6. Keep generated content `status: draft` and omit `verified`; maintainers add verification only after checking the source.
7. Retain superseded concepts as `deprecated` pages linked to their replacement.

## Concept Shape

Every non-reserved concept is Markdown with OKF v0.2 YAML frontmatter:

```yaml
---
type: Requirement
title: Example requirement
description: One sentence describing the concept.
category: requirement
tags: [cra]
status: draft
generated: { by: human:your-id, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: primary-source
    resource: https://example.eu/official-source
    title: Official source title
x-cra:
  jurisdiction: EU
  authority_level: binding
  checked_at: 2026-08-21T00:00:00Z
---
```

The path relative to `wiki/`, without `.md`, is the concept ID. Do not add a separate `id` field. `index.md` and `log.md` are reserved and normally have no frontmatter.

Use footnote labels matching `sources[].id` for sourced body claims.

## Pull Requests

State:

- what changed;
- the controlling primary source;
- the source's legal or standards status;
- its reuse terms;
- the date checked;
- affected concepts and coverage entries.

Run before opening a pull request:

```sh
python3 tools/validate.py wiki
```
