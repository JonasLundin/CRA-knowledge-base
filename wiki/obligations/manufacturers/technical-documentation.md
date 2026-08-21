---
type: Requirement
title: Technical Documentation Requirements under the CRA
description: Contents, retention periods, and compilation duties for technical documentation and SBOMs under Article 31 and Annex VII of Regulation (EU) 2024/2847.
category: requirement
tags: [cra, technical-documentation, compliance, sbom, annex-vii]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-13
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
    title: Regulation (EU) 2024/2847, Article 13
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-art-31
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_31
    title: Regulation (EU) 2024/2847, Article 31
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-annex-7
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_7
    title: Regulation (EU) 2024/2847, Annex VII
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 31, Annex VII
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Article 31 and Annex VII of Regulation (EU) 2024/2847 specify the mandatory structure and elements of the technical documentation that manufacturers must draw up before placing a product on the market.[^cra-art-31] [^cra-annex-7]

# Legal effect

Technical documentation constitutes the primary evidence demonstrating compliance with Annex I essential cybersecurity requirements. It must be made available to market surveillance authorities upon reasoned request.[^cra-art-31]

# Applicability

Applies to all manufacturers of products with digital elements made available on the EU market.[^cra-art-13]

# Requirements or coverage

Under Annex VII, the technical documentation must contain at least:

1. **General product description:** Intended purpose, versions, hardware/software architecture, and user instructions;
2. **Cybersecurity risk assessment:** Documented analysis of threats, attack surfaces, and risk mitigation measures;
3. **Software Bill of Materials (SBOM):** Machine-readable inventory of top-level and critical nested software dependencies;
4. **Standards and specifications:** References to harmonised standards, common specifications, or alternative technical specifications applied;
5. **Verification and test reports:** Test protocols, penetration test results, vulnerability scans, and conformity assessment evidence;
6. **Vulnerability handling documentation:** Processes for CVD, patching, and security update delivery;
7. **Retention period:** Must be kept for at least 10 years after placing on the market or for the declared support period, whichever is longer (Article 13(4)).[^cra-art-13] [^cra-annex-7]

# Dates and transitions

- Applies from 11 December 2027.

# Related concepts

- [Cybersecurity Risk Assessment](cybersecurity-risk-assessment.md)
- [Software Bill of Materials](../vulnerability-handling/software-bill-of-materials.md)
- [EU Declaration of Conformity](eu-declaration-of-conformity.md)
- [Market Surveillance Framework](../market-surveillance/market-surveillance-framework.md)

[^cra-art-13]: Regulation (EU) 2024/2847, Article 13, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
[^cra-art-31]: Regulation (EU) 2024/2847, Article 31, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_31
[^cra-annex-7]: Regulation (EU) 2024/2847, Annex VII, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_7
