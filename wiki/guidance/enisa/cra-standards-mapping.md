---
type: Official Guidance
title: ENISA CRA Requirements Standards Mapping
description: Authoritative ENISA study mapping CRA Annex I essential cybersecurity and vulnerability handling requirements to published international and European standards.
category: guidance
tags: [cra, guidance, enisa, standards-mapping, annex-i, supporting-standards, gap-analysis]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-02-21T00:00:00Z
sources:
  - id: enisa-standards-mapping
    resource: https://www.enisa.europa.eu/publications/cyber-resilience-act-requirements-standards-mapping
    title: Cyber Resilience Act Requirements - Standards Mapping Study
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2024-11-25T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2024-11-25
  relevant_provisions:
    - Article 27
    - Article 28
    - Annex I
  language: en
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

ENISA's *Cyber Resilience Act Requirements - Standards Mapping Study* provides an exhaustive technical mapping between each essential requirement in CRA Annex I (Part I product security properties and Part II vulnerability handling) and existing published international and European standards [^enisa-standards-mapping].

# Legal effect

This mapping is non-binding and analytical [^enisa-standards-mapping]. Conformance with the mapped supporting standards does not confer a statutory presumption of conformity under Article 27. Presumption of conformity is exclusively established when harmonised standards developed under Standardisation Request M/606 are officially cited in the Official Journal of the European Union (OJEU).

# Applicability

Serves as an essential reference for European standardisation committees (CEN, CENELEC, ETSI), manufacturers compiling technical documentation during the transitional period, and conformity assessment bodies.

# Key topics or guidance coverage

The study systematically maps Annex I clauses to major cybersecurity standard families [^enisa-standards-mapping]:

- **Industrial Automation and Control Systems:**
  - *EN IEC 62443-4-1:* Security development lifecycle requirements for product suppliers (mapping to Annex I Part I and Part II).
  - *EN IEC 62443-4-2:* Technical security requirements for IACS components.
- **Consumer and IoT Devices:**
  - *ETSI EN 303 645:* Baseline cybersecurity for consumer Internet of Things (mapping to default configuration, authentication, and vulnerability management clauses).
- **Radio Equipment & Embedded Wireless:**
  - *EN 18031-1, EN 18031-2, EN 18031-3:* Common security requirements for radio equipment under Directive 2014/53/EU.
- **Vulnerability Handling and Coordinated Disclosure:**
  - *ISO/IEC 29147:* Vulnerability disclosure processes for receiving and communicating vulnerability reports (Annex I Part II Point 5).
  - *ISO/IEC 30111:* Vulnerability handling processes for investigation, triage, and patch development (Annex I Part II Point 2).
- **Information Security Management & Evaluation Criteria:**
  - *ISO/IEC 27001 / ISO/IEC 27002:* Organizational controls supporting secure product lifecycles.
  - *ISO/IEC 15408 / ISO/IEC 18045 (Common Criteria):* Security evaluation criteria relevant for high-assurance and critical components.
- **Standardisation Gaps Identified:** Highlights areas where existing international standards only partially cover CRA requirements (such as automated SBOM maintenance, explicit support period declarations, and mandatory Union reporting mechanisms), justifying the specific work items under Standardisation Request M/606.

# Dates and transitions

- **Publication Date:** November 2024.
- **Transitional Role:** Serves as the primary bridge while new harmonised European standards (EN 40000 series and vertical EN 304 standards) are drafted and cited.

# Related concepts

- [Secure-by-Design Guidance](./secure-by-design-guidance.md)
- [European Commission Standardisation Guidance](../european-commission/standardisation-guidance.md)
- [Conformity Assessment Guidance](../european-commission/conformity-assessment-guidance.md)

[^enisa-standards-mapping]: European Union Agency for Cybersecurity (ENISA), Cyber Resilience Act Requirements - Standards Mapping Study, https://www.enisa.europa.eu/publications/cyber-resilience-act-requirements-standards-mapping
