---
type: Requirement
title: Non-Commercial Open-Source Developers in the CRA
description: Legal status and full exemption of non-commercial FOSS developers and individual open-source contributors under Regulation (EU) 2024/2847.
category: requirement
tags: [cra, open-source, foss, individual-contributors, exemptions]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-2
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
    title: Regulation (EU) 2024/2847, Article 2
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
  provision: Article 2(1), Recitals 18–23
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) 2024/2847 contains explicit safeguards ensuring that individual developers, unpaid maintainers, and non-profit contributors providing free and open-source software outside commercial activity remain completely outside the scope of CRA obligations.[^cra-art-2] [^ec-cra-faq]

# Legal effect

Non-commercial FOSS developers have no compliance duties, no CE marking obligations, no mandatory reporting requirements under Article 14, and cannot be subjected to market surveillance enforcement or administrative fines under the CRA.[^cra-art-2]

# Applicability

Applies to:
- Individual programmers contributing code to public open-source repositories;
- Research institutions and hobbyists publishing open-source libraries without commercial intent;
- Maintainers receiving non-commercial donations, bug bounties, or foundation grants;
- Open-source package maintainers who do not commercialise or sell products.[^ec-cra-faq]

# Requirements or coverage

- **No manufacturer liability:** Non-commercial developers do not become manufacturers when downstream commercial entities take and incorporate their code into commercial products;
- **Responsibility placed on commercial integrators:** The commercial entity that integrates FOSS code into a commercial product carries full legal responsibility under Article 13(5) to test, secure, and maintain the component;
- **Voluntary contributions welcome:** Non-commercial developers may voluntarily coordinate vulnerability disclosures or provide security notices, but are under no legal compulsion to do so.[^cra-art-2] [^ec-cra-faq]

# Dates and transitions

- Effective from 11 December 2027.

# Related concepts

- [Commercial Activity Boundary](../scope/commercial-activity.md)
- [Open-Source Software Steward Role](open-source-software-steward.md)
- [Third-Party Components Due Diligence](../manufacturers/third-party-components.md)

[^cra-art-2]: Regulation (EU) 2024/2847, Article 2, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
[^ec-cra-faq]: European Commission, Cyber Resilience Act Implementation Frequently Asked Questions, https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
