---
type: Economic Operator
title: Open-Source Software Steward Role and Obligations
description: Tailored obligations and cybersecurity policy requirements for open-source stewards under Article 24 of Regulation (EU) 2024/2847.
category: role
tags: [cra, open-source, steward, foss, governance, economic-operator]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-24
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_24
    title: Regulation (EU) 2024/2847, Article 24
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-art-3
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
    title: Regulation (EU) 2024/2847, Article 3
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: ec-cra-faq
    resource: https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
    title: Cyber Resilience Act Implementation Frequently Asked Questions
    author: European Commission
    last_modified: 2026-01-15T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 24
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

An open-source software steward is any legal person, other than a manufacturer, that has the purpose or objective of systematically providing support on a sustained basis for the development of specific products with digital elements qualifying as free and open-source software intended for commercial activities.[^cra-art-3] [^cra-art-24]

# Legal effect

Article 24 establishes a dedicated, light-touch regulatory regime for open-source software stewards. Stewards are exempt from manufacturer conformity assessment, CE marking, and product liability, but must establish baseline cybersecurity and vulnerability handling policies.[^cra-art-24]

# Applicability

Applies to open-source foundations, non-profit consortia, and legal entities that host, steward, or manage the development infrastructure for FOSS projects used in commercial products.[^cra-art-24] [^ec-cra-faq]

# Requirements or coverage

Under Article 24, open-source software stewards must:

1. **Cybersecurity policy:** Put in place and maintain a documented cybersecurity policy to promote the development of secure software (Article 24(1));
2. **Coordinated vulnerability disclosure:** Establish a coordinated vulnerability disclosure (CVD) process and provide a publicly accessible contact address for reporting vulnerabilities (Article 24(1));
3. **Vulnerability sharing:** Facilitate the sharing of vulnerability information and security fixes among project contributors, downstream manufacturers, and relevant CSIRTs/authorities (Article 24(1));
4. **Cooperation with authorities:** Cooperate with market surveillance authorities upon request (Article 24(2));
5. **No CE mark required:** Stewards are explicitly not required to draw up technical documentation, conduct Module A/H assessments, or affix CE marks.[^cra-art-24]

# Dates and transitions

- Applies from 11 December 2027.

# Related concepts

- [Commercial Activity Boundary](../scope/commercial-activity.md)
- [Open-Source Security Attestation](open-source-security-attestation.md)
- [Non-Commercial FOSS Developers](non-commercial-foss-developers.md)
- [Coordinated Vulnerability Disclosure](../vulnerability-handling/coordinated-vulnerability-disclosure.md)

[^cra-art-3]: Regulation (EU) 2024/2847, Article 3, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^cra-art-24]: Regulation (EU) 2024/2847, Article 24, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_24
[^ec-cra-faq]: European Commission, Cyber Resilience Act Implementation Frequently Asked Questions, https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
