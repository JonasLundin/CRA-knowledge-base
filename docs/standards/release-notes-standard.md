# CRA Knowledge Base Release Notes Standard (CKB-RNS-01)

## 1. Purpose and Scope

This standard establishes the mandatory structure, governance principles, and verification requirements for publishing release notes across all versions of the **CRA Knowledge Base**.

Because this repository serves as an Open Knowledge Foundation (OKF) compliant knowledge bundle bridging EU statutory regulations, technical standards, and engineering implementation, release notes must provide cryptographic traceability, legal accuracy, and actionable technical clarity for software engineers, product security incident response teams (PSIRTs), and regulatory compliance officers.

---

## 2. Governance and Versioning Principles

### 2.1 Semantic Versioning for Regulatory Knowledge Bundles

Releases adhere to **Semantic Versioning 2.0.0** (`vMAJOR.MINOR.PATCH`), mapped specifically to regulatory knowledge dynamics:

1. **MAJOR (`vX.0.0`) — Epochal Regulatory Milestones or Breaking Taxonomy Changes:**
   - Statutory application transitions (e.g., CRA Full Application on 11 December 2027).
   - Breaking modifications to the underlying Open Knowledge Foundation schema (e.g., transition from OKF v0.2 to v1.0).
   - Structural reorganization of the core article hierarchy or conceptual ontology that requires migration by downstream consuming tools.
2. **MINOR (`v0.X.0`) — Normative Source Reconciliations and Significant Concept Additions:**
   - Incorporating newly published European Commission delegated or implementing acts.
   - Reconciling substantive revisions to official administrative guidance (e.g., EC Implementation FAQ revisions, ENISA platform updates).
   - Introducing new horizontal/vertical harmonised standards drafts (e.g., prEN 40000 series, ETSI EN 304 series).
   - Adding new concept clusters, roles, or procedure guides.
3. **PATCH (`v0.0.X`) — Errata, Cross-Reference Fixes, and Maintenance:**
   - Correcting typos, broken hyperlinks, or stale metadata dates.
   - Minor clarifications in descriptive text that do not alter the underlying legal interpretation.
   - Maintenance updates to validation scripts, test harnesses, or CI/CD pipelines.

### 2.2 Dual-Audience Architecture

Every release note must balance:
- **Legal and Regulatory Context:** Clear citations of EU Treaties, Regulations, Directives, Official Journal of the EU (OJEU) entries, and administrative guidelines.
- **Engineering and Operational Impact:** Actionable checklists, architecture decisions, and workflow adaptations for product security teams, developers, and open-source stewards.

---

## 3. Required Sections in Every Release Note

Every release note document (`releases/v<VERSION>.md`) must contain the following standardized sections in the specified order:

```markdown
# Release Notes: v<MAJOR>.<MINOR>.<PATCH> — <Theme/Headline>

## 1. Release Metadata
## 2. Executive Summary & Regulatory Context
## 3. Normative Drift & Source Reconciliation Ledger
## 4. Concept & Content Changes (Keep a Changelog)
    ### Added
    ### Changed
    ### Deprecated
    ### Removed
    ### Fixed
    ### Security & Compliance
## 5. Implementation & Operational Guidance (Downstream Impact)
## 6. Verification, Validation & Integrity Evidence
## 7. Migration Guide & Breaking Changes
## 8. Upcoming Regulatory Milestones & Roadmap
```

### 3.1 Release Metadata
A structured key-value block at the top:
- **Version:** Semantic version number (e.g., `0.2.0`).
- **Release Date:** ISO 8601 calendar date (`YYYY-MM-DD`).
- **Git Commit / Tag:** Target commit hash and tag name.
- **Regulatory Epoch / Milestone:** Specific CRA implementation milestone (e.g., *Article 14 Go-Live (11 September 2026)*).
- **OKF Schema Version:** Bundle schema declaration (e.g., `0.2`).
- **Total Catalog Size:** Count of concept files, reserved files, and normative sources.

### 3.2 Executive Summary & Regulatory Context
A concise executive briefing explaining:
- The legal or operational catalyst for the release (e.g., publication of Commission guidelines, platform go-live, or standardisation milestone).
- Primary takeaways for organizations building, importing, or distributing products with digital elements in the EU.

### 3.3 Normative Drift & Source Reconciliation Ledger
An explicit tabular record tracking every normative source added, updated, or checked in [`sources.yaml`](file:///Users/jonaslundin/CRA-knowledge-base/sources.yaml):

| Source ID | Issuing Authority | Title | Version / Doc Ref | Previous Date | Current Date | Drift Summary |
|---|---|---|---|---|---|---|
| `ec-cra-faq` | European Commission | CRA Implementation FAQ | v1.4 | 2026-08-01 | 2026-09-04 | Realigned to 7-chapter structure; added AEV telemetry rules |

### 3.4 Concept & Content Changes
Grouped strictly under standard Keep a Changelog categories:
- **Added:** New concept files, directories, tools, or templates.
- **Changed:** Updated guidance, reconciled statutory interpretations, expanded definitions.
- **Deprecated:** Concepts or practices phased out by newer official acts.
- **Removed:** Deleted files or obsolete references.
- **Fixed:** Corrected statutory timelines, erroneous cross-references, or broken links.
- **Security & Compliance:** Specific additions regarding vulnerability handling, reporting quotas, encryption, or risk assessment.

### 3.5 Implementation & Operational Guidance
Direct, non-abstract instructions for engineering and PSIRT practitioners detailing:
- Required tooling adjustments (e.g., SRP authentication methods, MFA requirements).
- Triage window protocols and awareness triggers.
- Documentation and conformity assessment impacts.

### 3.6 Verification, Validation & Integrity Evidence
Reproducible commands and exact verification outputs demonstrating that the bundle satisfies all quality gates:
- Schema validation: `uv run --with pyyaml python3 tools/validate.py wiki` (must show 0 errors, 0 warnings).
- Unit tests: `uv run --with pyyaml --with pytest pytest tools/test_validate.py` (must pass 100%).
- Concept inventory: Total concept count matching `coverage.yaml`.

### 3.7 Migration Guide & Breaking Changes
Explanation of any deprecated structures or semantic shifts from previous versions, accompanied by remediation steps.

### 3.8 Upcoming Regulatory Milestones & Roadmap
Chronological horizon scanning outlining the next regulatory gates (e.g., Notified Body accreditation deadlines, full general application date, secondary implementing acts).

---

## 4. Release Artifacts & Synchronization

When a release is created, maintainers must synchronize across four synchronized artifacts:

1. **Standalone Release File:** Created at `releases/v<VERSION>.md`.
2. **Top-Level Changelog:** An entry added to [`CHANGELOG.md`](file:///Users/jonaslundin/CRA-knowledge-base/CHANGELOG.md) under `[<VERSION>] - <YYYY-MM-DD>`.
3. **Repository Version Manifests:** Updated [`VERSION`](file:///Users/jonaslundin/CRA-knowledge-base/VERSION) and [`CITATION.cff`](file:///Users/jonaslundin/CRA-knowledge-base/CITATION.cff).
4. **GitHub Release:** Published via `gh release create v<VERSION> -F releases/v<VERSION>.md` using the standard release notes.
