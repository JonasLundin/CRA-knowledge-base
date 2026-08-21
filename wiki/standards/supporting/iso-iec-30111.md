---
type: Standard
title: "ISO/IEC 30111: Vulnerability Handling Processes"
description: Supporting international standard specifying processes for vendors to investigate, remediate, and manage security vulnerabilities in products.
category: standard
tags: [cra, standard, supporting-standard, vulnerability-handling, remediation, iso-iec]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: iso-iec-30111
    resource: https://www.iso.org/standard/69298.html
    title: "ISO/IEC 30111:2019 Information technology - Security techniques - Vulnerability handling processes"
    author: ISO/IEC JTC 1/SC 27
    last_modified: 2019-10-01T00:00:00Z
  - id: enisa-mapping
    resource: https://www.enisa.europa.eu/publications/cyber-resilience-act-requirements-standards-mapping
    title: Cyber Resilience Act Requirements Standards Mapping
    author: ENISA
    last_modified: 2024-11-01T00:00:00Z
x-cra:
  standard_number: ISO/IEC 30111
  standards_body: ISO/IEC
  technical_committee: ISO/IEC JTC 1/SC 27
  m606_entries: []
  standard_status: published
  ojeu_cited: false
  ojeu_reference: null
  presumption_of_conformity: false
  covers:
    - CRA Annex I Part II points 1-3, 6-8
  access: restricted
  copyright: third-party
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

ISO/IEC 30111:2019 specifies internal vendor processes to investigate, triage, remediate, and resolve security vulnerabilities reported in products and online services[^iso-iec-30111]. It is mapped by ENISA to the technical remediation obligations in CRA Annex I Part II[^enisa-mapping].

# Legal effect

Use of ISO/IEC 30111 is voluntary. It has **not** been cited in the OJEU under Regulation (EU) 2024/2847 and does **not** confer a legal presumption of conformity under CRA Article 27.

# Applicability

Applies to manufacturers and development teams handling internal vulnerability triage, patch development, and remediation verification.

# Requirements and high-level coverage

ISO/IEC 30111 defines:
- Vulnerability investigation, root cause analysis, and severity scoring (CVSS);
- Remediation development workflows (patches, workarounds, configuration changes);
- Remediation testing, verification, and regression analysis;
- Release coordination and communication processes.

# Related concepts

- `standards/supporting/iso-iec-29147`
- `standards/harmonised/pren-40000-1-3`
- `standards/m606/line-15`

[^iso-iec-30111]: ISO/IEC. ISO/IEC 30111:2019. https://www.iso.org/standard/69298.html
[^enisa-mapping]: ENISA. Cyber Resilience Act Requirements Standards Mapping. https://www.enisa.europa.eu/publications/cyber-resilience-act-requirements-standards-mapping
