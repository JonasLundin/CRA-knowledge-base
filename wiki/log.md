# Bundle Update Log

## 2026-11-18

* **v0.3.0 Release — Normative Standardisation, ENISA Guidance, Certification & Citation Sweep**:
  - Reconciled CEN-CLC/JTC 13 WG 9 horizontal `EN 40000` series structure and November 2026 ratification milestones: `EN 40000-1-1` (*Vocabulary*) and `EN 40000-1-2` (*Principles for cyber resilience*, M/606 Line 01) passed CEN Formal Vote on 1 October 2026, achieved formal CEN-CENELEC ratification on 2 November 2026, and reached target availability on 18 November 2026 (documented as foundational non-OJEU-cited standards per CEN-CENELEC project records), alongside `prEN 40000-1-3` (*Vulnerability handling*, M/606 Line 15, targeted for OJEU citation), `prEN 40000-1-4` (*Generic security requirements*, M/606 Lines 02–14), and `CEN/CLC/TR 40000-1-5`.
  - Added concept and sources for *ENISA Technical Advisory for Software Bill of Materials* (published 22 October 2026) and *SBOM Adoption State of Play - 2026* (9 June 2026) in `wiki/guidance/enisa/sbom-technical-advisory.md`, covering the six-phase SBOM lifecycle, declaring "known unknowns", cryptographic signing, and STRIDE-based SBOM threat modeling.
  - Updated ENISA Single Reporting Platform (SRP) guidance (`single-reporting-platform.md`, `srp-assigned-representative-registration.md`, `srp-interface-guidance.md`) for platform release `v1.2.1` (deployed 20 October 2026), detailing the updated Secondary AR / backup user invitation workflow.
  - Updated M/606 standardisation request timeline (`standardisation-m606-deadline.md`, `how-cra-standards-are-built.md`) to reflect the July 2026 Commission amendment shifting 2026 deadlines to 31 October 2026 (Type A Horizontal Principles & Type B Vulnerability Handling) and 31 December 2026 (Type C Vertical Product-Specific Standards).
  - Added concrete 2026 draft European Standard numbers across non-ETSI and ETSI vertical committees and M/606 lines: CEN/TC 224 WG 17 (`prEN 40000-10`, `prEN 40000-11`, `prEN 18330`), CLC/TC 47X (`prEN 50765:2026`, `prEN 50766:2026`, `prEN 50764:2026`), CLC/TC 65X WG 3 (`prEN 50770-1` through `prEN 50770-6`), and ETSI TC CYBER/EUSR (`EN 304 642` for telecom network functions).
  - Integrated EUCC amending acts (`Commission Implementing Regulation (EU) 2024/3144` and `Commission Implementing Regulation (EU) 2025/2462` on product series and minor/major change rules) and the Cybersecurity Act amendment (`Regulation (EU) 2025/37` on managed security services).
  - Corrected CRA Article 27(8)–(9) legal mechanism references from implementing acts to delegated acts (in accordance with Article 61) for specifying qualifying European cybersecurity certification schemes.
  - Repaired 39 truncated or missing ELI anchor fragments (`#art_32`, `#art_35`, `#ann_1`–`#ann_8`, `#ann_i_part_1`–`2`) across product category, glossary, and annex footnotes, and refreshed `checked_at` (`2026-11-18`) and `stale_after` (`2027-05-18`) across all 338 concepts.

## 2026-09-26

* **v0.2.0 Release & SRP Go-Live Integration**:
  - Integrated official live Single Reporting Platform production endpoint (`https://portal.cra-srp.enisa.europa.eu`) as `enisa-srp-portal` across SRP overview and registration concepts.
  - Audited all 267 normative sources in `sources.yaml` following the 11 September 2026 Article 14 application milestone.
  - Established formal CRA Knowledge Base Release Notes Standard (`CKB-RNS-01`), reusable templates, and published comprehensive release notes for v0.2.0.
  - Bumped version to 0.2.0 across manifests (`VERSION`, `CITATION.cff`, `CHANGELOG.md`).

## 2026-09-07

* **Normative Drift Reconciliation**: Updated drifted European Commission and ENISA Single Reporting Platform (SRP) normative sources and concepts:
  - Reconciled EC Implementation FAQ (`ec-cra-faq`) to Version 1.4 (4 September 2026) across its seven official chapters.
  - Reconciled EC Guidance C(2026) 5252 (`ec-c-2026-5252`) publication date (27 July 2026) and reporting provisions.
  - Reconciled ENISA SRP documentation suite (updated August/September 2026) to reflect live endpoints, EU Login authentication, 20-notification unvalidated quota, advisory against pre-emptive registration, and absence of external API at initial launch.
  - Added official concepts for *CRA SRP Glossary* (v1.1, 43 reporting fields) and *List of CSIRTs Designated as Coordinators*.
  - Corrected statutory final report timelines under Article 14(2)(d) (14 days after corrective measure) and Article 14(4)(c) (1 month after 72h report).
  - Explicitly defined statutory awareness thresholds and triage standards ("sufficient degree of certainty"), telemetry and external report triggers, third-party component reachability, and negative exclusions (Recital 68 good-faith research/CVD, static scan noise) in early warning, reporting, and glossary concepts.

## 2026-08-21

* **Creation**: Established the OKF v0.2 bundle and began source-grounded ingestion.

