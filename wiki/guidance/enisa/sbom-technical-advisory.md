---
type: Official Guidance
title: ENISA Technical Advisory for Software Bill of Materials (SBOM)
description: Practical technical guidance from ENISA on the six-phase SBOM lifecycle, declaring known unknowns, cryptographic signing, and STRIDE threat modeling for CRA supply chain compliance.
category: guidance
tags: [cra, guidance, enisa, sbom, software-bill-of-materials, supply-chain, spdx, cyclonedx, threat-modelling]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-11-18T00:00:00Z }
stale_after: 2027-05-18T00:00:00Z
sources:
  - id: enisa-sbom-advisory
    resource: https://www.enisa.europa.eu/publications/enisa-technical-advisory-for-software-bill-of-materials
    title: ENISA Technical Advisory for Software Bill of Materials
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-10-22T00:00:00Z
  - id: enisa-sbom-state-of-play
    resource: https://www.enisa.europa.eu/publications/sbom-adoption-state-of-play-2026
    title: SBOM Adoption State of Play - 2026
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-06-09T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2026-10-22
  relevant_provisions:
    - Article 3(40)
    - Article 13(5)
    - Article 14
    - Article 24
    - Annex I Part II point 1
    - Annex VII
  language: en
  checked_at: 2026-11-18T00:00:00Z
---

# Summary

Published on 22 October 2026 (building on ENISA's 9 June 2026 *SBOM Adoption State of Play - 2026* survey report [^enisa-sbom-state-of-play]), the *ENISA Technical Advisory for Software Bill of Materials* provides practical, CRA-aligned operational and architectural guidance for establishing and maturing SBOM capabilities across the software development lifecycle [^enisa-sbom-advisory]. It is specifically tailored to help micro, small, and medium-sized enterprises (SMEs), manufacturers, and open-source software stewards implement CRA Annex I Part II point (1) and support rapid vulnerability triage under Article 14.

# Legal effect

This technical advisory is non-binding [^enisa-sbom-advisory]. It does not constitute a formal legal interpretation of Regulation (EU) 2024/2847 or confer a legal presumption of conformity under Article 27, but provides authoritative engineering practices for fulfilling the SBOM and component due-diligence obligations in CRA Article 13(5), Annex I Part II point (1), and Annex VII.

# Applicability

Applies to manufacturers of products with digital elements, SMEs, open-source software stewards (Article 24), DevSecOps engineers, and product security teams generating, validating, storing, or consuming SBOMs.

# Key topics or guidance coverage

The advisory structures SBOM implementation around a continuous lifecycle and threat-informed engineering practices [^enisa-sbom-advisory]:

- **Six-Phase Continuous SBOM Lifecycle:**
  1. *Build & Generation:* Automated generation of machine-readable SBOMs (using industry-standard formats such as **SPDX** or **CycloneDX**) integrated directly into CI/CD build pipelines rather than manual post-build inventorying.
  2. *Validation:* Automated verification of schema conformity, syntactic validity, metadata completeness, and accuracy against actual compiled artifacts.
  3. *Cryptographic Signing:* Applying digital signatures and provenance attestations to guarantee SBOM authenticity and detect tampering.
  4. *Secure Storage:* Retaining versioned SBOMs in access-controlled, immutable repositories aligned with CRA technical documentation retention duties (Article 13(13) and Annex VII).
  5. *Consumption:* Feeding SBOMs continuously into vulnerability management, advisories (such as CSAF/VEX), and incident response workflows so teams can rapidly determine exposure when a new actively exploited vulnerability emerges (supporting the 24-hour SRP early warning deadline under Article 14(2)(a)).
  6. *Maintenance:* Re-generating and updating SBOMs whenever direct or transitive dependencies, build flags, or patches change across the support period.
- **Declaring "Known Unknowns":** Rather than silently omitting dependencies where deep transitive resolution fails (e.g., dynamically linked binaries or opaque third-party modules), ENISA recommends explicitly declaring "known unknowns" in the SBOM metadata so risk assessments accurately reflect visibility gaps.
- **STRIDE-Based SBOM Threat Model:** The advisory defines an indicative threat model for SBOM ecosystems using the STRIDE framework (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege), addressing risks such as poisoned dependency metadata, unauthorized disclosure of confidential internal component graphs, and unsigned SBOM substitution.

# Dates and transitions

- **Baseline Survey Report (*SBOM Adoption State of Play - 2026*):** Published **9 June 2026** [^enisa-sbom-state-of-play].
- **Technical Advisory Publication:** Published **22 October 2026** [^enisa-sbom-advisory].
- **CRA Statutory Alignment:** Supports immediate operational readiness for Article 14 vulnerability triage (applicable since 11 September 2026) and full Annex I Part II point (1) SBOM compliance (applicable from **11 December 2027**).

# Related concepts

- [Secure-by-Design Guidance](./secure-by-design-guidance.md)
- [CRA Standards Mapping](./cra-standards-mapping.md)
- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [Software Bill of Materials (SBOM) Requirements](../../obligations/vulnerability-handling/software-bill-of-materials.md)
- [prEN 40000-1-3: Vulnerability Handling](../../standards/harmonised/pren-40000-1-3.md)

[^enisa-sbom-advisory]: European Union Agency for Cybersecurity (ENISA), ENISA Technical Advisory for Software Bill of Materials, https://www.enisa.europa.eu/publications/enisa-technical-advisory-for-software-bill-of-materials
[^enisa-sbom-state-of-play]: European Union Agency for Cybersecurity (ENISA), SBOM Adoption State of Play - 2026, https://www.enisa.europa.eu/publications/sbom-adoption-state-of-play-2026
