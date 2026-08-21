---
type: Requirement
title: Remote Data Processing Solutions under the CRA
description: Conditions under which cloud services and backend processing solutions are in scope as integral parts of products with digital elements under Article 2(1) and Article 3(2).
category: requirement
tags: [cra, cloud, remote-data-processing, scope]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-2
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
    title: Regulation (EU) 2024/2847, Article 2
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
  provision: Article 2(1), Article 3(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) 2024/2847 covers remote data processing solutions (such as companion cloud backends, APIs, and remote processing pipelines) when they are developed by or on behalf of the manufacturer and are essential to a primary function of the product with digital elements.[^cra-art-2] [^cra-art-3]

# Legal effect

Remote data processing solutions within scope are evaluated as part of the product with digital elements. Manufacturers must ensure that backend processing and communication links meet Annex I essential cybersecurity requirements and are included in the cybersecurity risk assessment and technical documentation.[^cra-art-2]

# Applicability

A remote data processing service is covered under Article 3(2) if all of the following conditions are met:

1. **Distance processing:** Data processing is performed at a distance (e.g. cloud platform, SaaS backend, hosted service);
2. **Manufacturer control or development:** The software/service is designed and developed by the manufacturer, on its behalf, or under its control;
3. **Primary function dependency:** The absence of the remote processing would prevent the product with digital elements from performing one of its primary functions.[^cra-art-3]

Independent third-party cloud services or generic websites that are not under the manufacturer's control or not essential to the product's primary functionality do not fall within CRA scope (they may be subject to NIS2 or other frameworks).[^ec-cra-faq]

# Requirements or coverage

- **End-to-end security:** Security across the communication channel between the physical/local product and remote processing endpoints.
- **Vulnerability management:** Remote endpoints must be monitored, patched, and included in Article 14 vulnerability reporting if actively exploited.
- **Risk assessment:** The manufacturer's risk assessment must document attack vectors originating from or passing through remote data processing solutions.[^cra-art-2]

# Dates and transitions

- Applies from 11 December 2027 with full CRA application.
- Reporting obligations under Article 14 for actively exploited vulnerabilities affecting remote processing apply from 11 September 2026.[^cra-art-2]

# Related concepts

- [Product Scope](product-scope.md)
- [Cybersecurity Risk Assessment](../manufacturers/cybersecurity-risk-assessment.md)
- [Article 14 Reporting Overview](../reporting/article-14-reporting.md)
- [Glossary: Remote Data Processing](../../glossary/remote-data-processing.md)

[^cra-art-2]: Regulation (EU) 2024/2847, Article 2, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
[^cra-art-3]: Regulation (EU) 2024/2847, Article 3, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^ec-cra-faq]: European Commission, Cyber Resilience Act Implementation Frequently Asked Questions, https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
