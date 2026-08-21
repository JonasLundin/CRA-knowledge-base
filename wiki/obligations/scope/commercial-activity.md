---
type: Requirement
title: Commercial Activity Boundary in the Cyber Resilience Act
description: Criteria distinguishing products supplied in the course of commercial activity from non-commercial open-source software development under Regulation (EU) 2024/2847.
category: requirement
tags: [cra, scope, commercial-activity, open-source, foss]
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
  - id: ec-guidance-5252
    resource: https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
    title: Commission Guidance C(2026) 5252 on CRA Implementation
    author: European Commission
    last_modified: 2026-06-30T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 2(1), Recitals 18–23
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) 2024/2847 applies only to products with digital elements made available on the market in the course of a commercial activity. Free and open-source software (FOSS) developed or provided outside the course of a commercial activity is excluded from the CRA obligations.[^cra-art-2]

# Legal effect

Where software is developed and distributed without commercial intent, the developer or project is exempt from the manufacturer obligations (essential requirements, conformity assessment, CE marking, and Article 14 mandatory reporting). Dedicated lighter obligations apply to Open-Source Software Stewards under Article 24.[^cra-art-2]

# Applicability

### Indicators of non-commercial activity (excluded)
- Developing, maintaining, or sharing source code in public repositories without charging a price;
- Receiving purely voluntary donations or grants to support open-source infrastructure without commercial return;
- Individual contributions made by employees of commercial entities to open-source projects where the entity does not exercise direct control or integrate the project into its commercial offer;
- Non-profit hosting of package registries and code platforms.[^ec-cra-faq] [^ec-guidance-5252]

### Indicators of commercial activity (in scope)
- Charging a price or subscription fee for the software or its direct digital updates;
- Monetising the software by requiring user personal data for purposes other than security and functionality;
- Providing paid technical support, warranty, or software maintenance agreements as an integrated commercial product;
- Releasing software under a dual-licensing scheme where commercial proprietary licences are sold alongside open-source versions.[^ec-cra-faq]

# Requirements or coverage

- If a commercial entity takes open-source components and integrates them into a commercial product, that entity assumes full manufacturer responsibility under Article 13.
- Open-source foundations and legal entities providing systematic support to open-source software intended for commercial use may qualify as Open-Source Software Stewards under Article 24.[^cra-art-2]

# Dates and transitions

- Applicable horizontally with the full CRA regime from 11 December 2027.

# Related concepts

- [Product Scope](product-scope.md)
- [Open-Source Software Steward Role](../open-source/open-source-software-steward.md)
- [Non-Commercial FOSS Developers](../open-source/non-commercial-foss-developers.md)
- [Third-Party Components Due Diligence](../manufacturers/third-party-components.md)

[^cra-art-2]: Regulation (EU) 2024/2847, Article 2, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
[^ec-cra-faq]: European Commission, Cyber Resilience Act Implementation Frequently Asked Questions, https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
[^ec-guidance-5252]: European Commission, Commission Guidance C(2026) 5252 on CRA Implementation, https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
