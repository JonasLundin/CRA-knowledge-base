# Release Notes: v<MAJOR>.<MINOR>.<PATCH> — <Theme / Headline>

## 1. Release Metadata

| Field | Value |
|---|---|
| **Version** | `v<MAJOR>.<MINOR>.<PATCH>` |
| **Release Date** | `<YYYY-MM-DD>` |
| **Git Commit / Tag** | `<COMMIT_HASH>` / `v<MAJOR>.<MINOR>.<PATCH>` |
| **Regulatory Milestone** | `<e.g., Article 14 Go-Live (11 September 2026)>` |
| **OKF Schema Version** | `0.2` |
| **Total Sources** | `<SOURCE_COUNT>` |
| **Total Concepts** | `<CONCEPT_COUNT>` |

---

## 2. Executive Summary & Regulatory Context

<!-- Concise 2-4 paragraph overview of the catalyst, statutory grounding, and key takeaways for manufacturers and downstream consumers. -->

---

## 3. Normative Drift & Source Reconciliation Ledger

| Source ID | Issuing Authority | Title | Version / Ref | Previous Date | Current Date | Drift / Change Summary |
|---|---|---|---|---|---|---|
| `<source-id>` | `<Authority>` | `<Document Title>` | `<vX.Y>` | `<YYYY-MM-DD>` | `<YYYY-MM-DD>` | `<Specific changes reconciled>` |

---

## 4. Concept & Content Changes

### Added
- `<Concept Title>` (`<file-path>`): `<Brief description>`

### Changed
- `<Concept Title>` (`<file-path>`): `<Brief description>`

### Deprecated
- `<Item>`: `<Reason>`

### Removed
- `<Item>`: `<Reason>`

### Fixed
- `<Concept Title>` (`<file-path>`): `<Correction details>`

### Security & Compliance
- `<Topic>`: `<Compliance implications>`

---

## 5. Implementation & Operational Guidance (Downstream Impact)

1. **PSIRT & Incident Response Protocols:**
   - `<Action item>`
2. **Product Development & Architecture:**
   - `<Action item>`
3. **Legal & Compliance:**
   - `<Action item>`

---

## 6. Verification, Validation & Integrity Evidence

### 6.1 OKF Schema & Bundle Integrity
```bash
$ uv run --with pyyaml python3 tools/validate.py wiki
<OUTPUT>
```

### 6.2 Automated Unit Testing
```bash
$ uv run --with pyyaml --with pytest pytest tools/test_validate.py
<OUTPUT>
```

---

## 7. Migration Guide & Breaking Changes

<!-- Detail any breaking changes to concept taxonomies or schema, and migration steps for consumers. If none, explicitly state "No breaking changes." -->

---

## 8. Upcoming Regulatory Milestones & Roadmap

- **`<DATE>`:** `<Milestone Description>`
- **`<DATE>`:** `<Milestone Description>`
