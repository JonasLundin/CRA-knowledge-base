---
type: Standard
title: "ISO/IEC 29147: Vulnerability Disclosure"
description: Supporting international standard providing guidelines for the disclosure and receipt of potential security vulnerabilities in products.
category: standard
tags: [cra, standard, supporting-standard, vulnerability-disclosure, cvd, iso-iec]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: iso-iec-29147
    resource: https://www.iso.org/standard/72311.html
    title: "ISO/IEC 29147:2018 Information technology - Security techniques - Vulnerability disclosure"
    author: ISO/IEC JTC 1/SC 27
    last_modified: 2018-10-01T00:00:00Z
  - id: enisa-mapping
    resource: https://www.enisa.europa.eu/publications/cyber-resilience-act-requirements-standards-mapping
    title: Cyber Resilience Act Requirements Standards Mapping
    author: ENISA
    last_modified: 2024-11-01T00:00:00Z
x-cra:
  standard_number: ISO/IEC 29147
  standards_body: ISO/IEC
  technical_committee: ISO/IEC JTC 1/SC 27
  m606_entries: []
  standard_status: published
  ojeu_cited: false
  ojeu_reference: null
  presumption_of_conformity: false
  covers:
    - CRA Annex I Part II points 4-5
  access: restricted
  copyright: third-party
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

ISO/IEC 29147:2018 provides guidelines for vendors on receiving reports of security vulnerabilities and publishing vulnerability disclosure information[^iso-iec-29147]. It serves as an international baseline mapped to CRA Annex I Part II points 4 and 5 on Coordinated Vulnerability Disclosure (CVD)[^enisa-mapping].

# Legal effect

Use of ISO/IEC 29147 is voluntary. It has **not** been cited in the OJEU under Regulation (EU) 2024/2847 and does **not** confer a legal presumption of conformity under CRA Article 27.

# Applicability

Applies to manufacturers and software vendors establishing intake channels and policies for receiving reports from security researchers and users.

# Requirements and high-level coverage

ISO/IEC 29147 defines:
- Guidelines for establishing public vulnerability disclosure policies and points of contact (`security.txt`);
- Secure intake mechanisms for receiving vulnerability reports (PGP/GPG encryption, secure portals);
- Protocols for communicating with finders and acknowledging reports;
- Standard formats and guidelines for publishing security advisories.

# Related concepts

- `standards/supporting/iso-iec-30111`
- `standards/harmonised/pren-40000-1-3`
- `standards/m606/line-15`

[^iso-iec-29147]: ISO/IEC. ISO/IEC 29147:2018. https://www.iso.org/standard/72311.html
[^enisa-mapping]: ENISA. Cyber Resilience Act Requirements Standards Mapping. https://www.enisa.europa.eu/publications/cyber-resilience-act-requirements-standards-mapping
