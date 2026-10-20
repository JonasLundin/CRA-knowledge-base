# Changelog

## [0.3.0] - 2026-11-18

### Added
- Added concept for horizontal draft standard *prEN 40000-1-4: Cybersecurity requirements for products with digital elements — Part 1-4: Generic security requirements* covering M/606 Lines 02–14 (`wiki/standards/harmonised/pren-40000-1-4.md`).
- Added concept and sources for *ENISA Technical Advisory for Software Bill of Materials (SBOM)* (`enisa-sbom-advisory`, published 22 October 2026) and *SBOM Adoption State of Play - 2026* (`enisa-sbom-state-of-play`, 9 June 2026) in `wiki/guidance/enisa/sbom-technical-advisory.md`.
- Added normative sources for EUCC amending acts *Commission Implementing Regulation (EU) 2024/3144* (`reg-2024-3144`) and *Commission Implementing Regulation (EU) 2025/2462* (`reg-2025-2462`) and Cybersecurity Act amendment *Regulation (EU) 2025/37* (`reg-2025-37`).
- Published comprehensive standalone release note for v0.3.0 in `releases/v0.3.0.md` following `CKB-RNS-01`.

### Changed
- Reconciled CEN-CLC/JTC 13 WG 9 horizontal `EN 40000` series numbering and November 2026 ratification status across harmonised standard concepts, M/606 lines 01–15, and supporting standards: `EN 40000-1-1` (*Vocabulary*, ratified 2 November 2026, available 18 November 2026; non-OJEU-cited baseline), `EN 40000-1-2` (*Principles for cyber resilience*, Line 01, ratified 2 November 2026, available 18 November 2026; non-OJEU-cited framework), `prEN 40000-1-3` (*Vulnerability handling*, Line 15, targeted for OJEU citation), `prEN 40000-1-4` (*Generic security requirements*, Lines 02–14), and `CEN/CLC/TR 40000-1-5` (*Threats and security objectives*).
- Updated ENISA Single Reporting Platform (SRP) guidance (`single-reporting-platform.md`, `srp-assigned-representative-registration.md`, `srp-interface-guidance.md`) for platform release `v1.2.1` (deployed 20 October 2026), detailing the updated Secondary AR / backup user invitation workflow.
- Updated M/606 standardisation request timeline (`wiki/timeline/standardisation-m606-deadline.md`, `wiki/standards/process/how-cra-standards-are-built.md`) to reflect the July 2026 Commission amendment shifting 2026 deadlines to 31 October 2026 (Type A Horizontal Principles & Type B Vulnerability Handling) and 31 December 2026 (Type C Vertical Product-Specific Standards), plus the November 2026 ratification of `EN 40000-1-1` and `EN 40000-1-2`.
- Added concrete 2026 draft European Standard numbers across vertical committees, M/606 lines, and product categories: CEN/TC 224 WG 17 (`prEN 40000-10`, `prEN 40000-11`, `prEN 18330`), CLC/TC 47X (`prEN 50765:2026`, `prEN 50766:2026`, `prEN 50764:2026`), CLC/TC 65X WG 3 (`prEN 50770-1` through `prEN 50770-6`), and ETSI TC CYBER/EUSR (`EN 304 642` for telecommunications network functions).
- Refreshed `checked_at` (`2026-11-18`) and advanced `stale_after` (`2027-05-18`) across all 338 concepts; updated `sources.yaml` (272 sources) and `coverage.yaml` (338 concepts, baseline `2026-11-18`).

### Fixed
- Corrected CRA Article 27(8)–(9) legal mechanism references in `wiki/law/eu/cra/articles/article-27.md` and `wiki/standards/certification-schemes/eucc.md` from implementing acts to delegated acts (in accordance with Article 61) for specifying qualifying European cybersecurity certification schemes.
- Repaired 39 truncated or missing ELI anchor fragments (`#art_32`, `#art_35`, `#ann_1`–`#ann_8`, `#ann_i_part_1`–`2`) across product category, glossary, and annex footnotes.

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
