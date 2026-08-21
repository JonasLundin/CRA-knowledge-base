---
type: Requirement
title: Support Period Determination and Communication
description: Manufacturer obligations to determine, declare, and maintain security support periods for products under Article 13(8)–(10) of Regulation (EU) 2024/2847.
category: requirement
tags: [cra, support-period, security-updates, consumer-information, lifecycle]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-13
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
    title: Regulation (EU) 2024/2847, Article 13
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-art-3
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
    title: Regulation (EU) 2024/2847, Article 3
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
  provision: Article 13(8)–(10)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Under Article 13(8) of Regulation (EU) 2024/2847, manufacturers must determine and declare a support period during which vulnerabilities are effectively handled and security updates are provided for the product with digital elements.[^cra-art-13]

# Legal effect

The declared support period establishes a legally binding obligation on the manufacturer to provide security updates and vulnerability handling throughout that timeframe. Failure to provide security updates during the declared period is an infringement subject to market surveillance enforcement.[^cra-art-13]

# Applicability

Applies to all products with digital elements placed on the EU market.[^cra-art-13]

# Requirements or coverage

1. **Criteria for determination:** The support period must reflect the reasonably expected product lifetime, considering user expectations, the nature of the product, and relevant Union harmonisation legislation (Article 13(8));
2. **Default expectation:** For products with an expected lifetime of at least five years, the support period must be at least five years, unless the product's expected operational lifetime is shorter (Article 13(8));
3. **Pre-purchase information:** The support period (expressed as an exact end-date or duration) must be made available to consumers and users prior to purchase in a clear, visible, and accessible manner (Article 13(9), Annex II point 1);
4. **End-of-support transparency:** Manufacturers must publicly disclose when a product reaches its end of support.[^cra-art-13] [^ec-guidance-5252]

# Dates and transitions

- Applies from 11 December 2027.

# Related concepts

- [Manufacturer Role & Duties](manufacturer.md)
- [Security Updates](security-updates.md)
- [Vulnerability Handling Requirements](../vulnerability-handling/vulnerability-handling-requirements.md)
- [Glossary: Support Period](../../glossary/support-period.md)

[^cra-art-13]: Regulation (EU) 2024/2847, Article 13, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
[^cra-art-3]: Regulation (EU) 2024/2847, Article 3, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^ec-guidance-5252]: European Commission, Commission Guidance C(2026) 5252 on CRA Implementation, https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
