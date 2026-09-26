# Changelog

## [0.2.0] - 2026-09-26

### Added
- Added concept and source for *CRA SRP Glossary* (v1.1, 5 September 2026) covering 43 standardized notification fields (`wiki/guidance/enisa/srp-glossary.md`).
- Added concept and source for *List of CSIRTs Designated as Coordinators* (4 September 2026) across all 27 EU Member States (`wiki/guidance/enisa/srp-csirt-coordinators.md`).
- Added source and endpoint references for the live *Single Reporting Platform (SRP) Production Portal* at `https://portal.cra-srp.enisa.europa.eu` (`enisa-srp-portal`).
- Created the formal *CRA Knowledge Base Release Notes Standard* (`CKB-RNS-01`) in `docs/standards/release-notes-standard.md`.
- Created standardized release note templates in `docs/standards/release-notes-template.md` and `.github/RELEASE_TEMPLATE.md`.
- Published comprehensive standalone release note for v0.2.0 in `releases/v0.2.0.md`.

### Changed
- Reconciled EC Implementation FAQ (`ec-cra-faq`) in `sources.yaml` and concepts to Version 1.4 (4 September 2026), structured across seven official chapters.
- Reconciled Commission Guidance C(2026) 5252 publication date to 27 July 2026 and incorporated Section 9.1 Article 14 guidance.
- Reconciled ENISA Single Reporting Platform (SRP) suite (`enisa-srp-hub`, `enisa-srp-faq`, `enisa-srp-registration`, `enisa-srp-notification`, `enisa-srp-api-guide`) to latest September 2026 releases and URLs.
- Corrected SRP technical interface documentation to reflect AR web portal interface functions and the absence of an external API at initial release.
- Documented SRP EU Login MFA authentication, AR role delegation, 20-notification quota for unvalidated ARs, advisory against pre-emptive registration, and non-EU lead CSIRT selection hierarchy.
- Explicitly documented statutory awareness thresholds, triage standards ("sufficient degree of certainty"), positive telemetry/external triggers, third-party component reachability, and negative exclusions (Recital 68 good-faith research/CVD, static scan noise) across early warning, reporting overview, and glossary concepts.
- Updated `sources.yaml` header with 267 sources audited as of 2026-09-26.

### Fixed
- Corrected statutory final report timelines under Article 14(2)(d) (14 days after corrective measure is in place) and Article 14(4)(c) (1 month after 72h report).
- Corrected Particular Exceptional Circumstances (PEC) dissemination and restricted routing rules under Article 16(2) and Delegated Regulation (EU) 2026/881.

## [0.1.1] - 2026-08-21

- Fixed the initial GitHub Actions dependency-cache configuration.

## [0.1.0] - 2026-08-21

Initial public preview.

- Added the OKF v0.2 CRA knowledge bundle with 334 draft concepts.
- Covered all 71 CRA articles, eight annexes, current secondary legislation, and related EU law.
- Added M/606, its 41 requested lines, 17 ETSI public-enquiry drafts, committee work, and supporting standards metadata.
- Added role, obligation, product, reporting, conformity, timeline, glossary, guidance, and jurisdiction views.
- Added source provenance, coverage manifests, validation, licensing, contribution, and security documentation.

All concepts are draft and unverified. This release is for general orientation only and must not be used as the basis for compliance-impacting decisions.
