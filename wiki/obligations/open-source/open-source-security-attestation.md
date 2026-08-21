---
type: Requirement
title: Voluntary Open-Source Security Attestations under the CRA
description: Voluntary security attestation mechanisms and cooperation frameworks for open-source stewards under Article 24 of Regulation (EU) 2024/2847.
category: requirement
tags: [cra, open-source, attestation, voluntary-compliance, supply-chain]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-24
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_24
    title: Regulation (EU) 2024/2847, Article 24
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: ec-guidance-5252
    resource: https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
    title: Commission Guidance C(2026) 5252 on CRA Implementation
    author: European Commission
    last_modified: 2026-06-30T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 24(3)–(5)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Article 24(3) of Regulation (EU) 2024/2847 enables open-source software stewards to establish voluntary security attestation mechanisms to demonstrate that specific FOSS components follow secure development practices.[^cra-art-24]

# Legal effect

Voluntary security attestations do not shift legal manufacturer liability onto the steward, but they provide downstream commercial manufacturers with standardized evidence to fulfill their third-party component due diligence obligations under Article 13(5).[^cra-art-24]

# Applicability

Available to open-source software stewards and project maintainers wishing to provide documented assurance to downstream commercial integrators.[^cra-art-24]

# Requirements or coverage

Voluntary security attestation programs may include:

1. **Development security practices:** Documentation of source code integrity controls, multi-party reviews, and CI/CD signing;
2. **Vulnerability management:** Adherence to CVD processes, security advisory publication, and rapid patch delivery;
3. **Dependency tracking:** Maintenance and publication of machine-readable SBOMs for major release artifacts;
4. **Standardised templates:** Alignment with Union guidelines and harmonised standards developed under standardisation request M/606.[^cra-art-24] [^ec-guidance-5252]

# Dates and transitions

- Effective from 11 December 2027.

# Related concepts

- [Open-Source Software Steward Role](open-source-software-steward.md)
- [Third-Party Components Due Diligence](../manufacturers/third-party-components.md)
- [Software Bill of Materials](../vulnerability-handling/software-bill-of-materials.md)

[^cra-art-24]: Regulation (EU) 2024/2847, Article 24, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_24
[^ec-guidance-5252]: European Commission, Commission Guidance C(2026) 5252 on CRA Implementation, https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
