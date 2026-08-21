---
type: Product Category
title: Smart Meter Gateways (Critical)
description: High-assurance smart meter gateways for critical utility infrastructure under Annex IV point 2 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, critical, smart-meters, grid-security, energy, annex-iv]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-annex-4
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_4
    title: Regulation (EU) 2024/2847, Annex IV
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-art-32
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_32
    title: Regulation (EU) 2024/2847, Article 32
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: reg-2025-2392
    resource: http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
    title: Commission Implementing Regulation (EU) 2025/2392 on Technical Descriptions
    author: European Commission
    last_modified: 2025-11-15T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Annex IV point 2, Article 32(4)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 2 of Annex IV covers smart meter gateways and advanced metering communication units deployed in high-capacity energy networks and critical national grid infrastructures.[^cra-annex-4] [^reg-2025-2392]

# Legal effect

Subject to mandatory European cybersecurity certification at assurance level 'high' pursuant to Article 32(4).[^cra-art-32]

# Applicability

Applies to:
- Smart meter gateways deployed in transmission and high-voltage distribution networks;
- Secure gateway units managing central grid balancing, feed-in limitation, and load shedding commands;
- Centralized smart metering hubs with direct interfaces to critical transmission system operators (TSOs).[^reg-2025-2392]

# Requirements or coverage

- **Mandatory certification route:** European cybersecurity certificate under Regulation (EU) 2019/881 at assurance level **'high'** (Article 32(4));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 40 (CEN-CLC JTC 13 / WG 6);
- **Security assurance:** Common Criteria / EUCC evaluation (EAL4+ / AVA_VAN.5 level or equivalent), cryptographic separation of metrology and communication domains, and tamper logging.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Smart Meter Gateways (Class II)](../important-class-ii/smart-meter-gateways.md)
- [Industrial Automation & Control Systems (IACS)](../important-class-ii/industrial-automation-control-systems.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-4]: Regulation (EU) 2024/2847, Annex IV, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_4
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
