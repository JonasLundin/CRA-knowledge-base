---
type: Product Category
title: Smart Meter Gateways (Class II)
description: Smart meter gateways and communication units within smart energy metering systems under Annex III Class II point 4 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-ii, smart-meters, energy-grid, smart-meter-gateways, ami]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-annex-3
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
    title: Regulation (EU) 2024/2847, Annex III
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
  provision: Annex III Class II point 4, Article 32(3)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 4 of Annex III Class II designates smart meter gateways and advanced metering infrastructure (AMI) communication controllers as Important Products with Digital Elements (Class II).[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Mandates third-party conformity assessment under Article 32(3) to protect electricity, gas, water, and thermal energy metering data and grid switching commands from tampering or unauthorized disruption.[^cra-art-32]

# Applicability

Applies to:
- Smart meter gateways interfacing local metering devices with wide-area grid management networks;
- Data concentrators and secure communication units deployed in smart energy grids;
- Sub-metering gateways with remote disconnect or grid balancing functions.[^reg-2025-2392]

# Requirements or coverage

- **Mandatory conformity assessment route:** **Module B + C** or **Module H** evaluated by a notified body, or European cybersecurity certificate (Article 32(3));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 40 (CEN-CLC JTC 13 / WG 6);
- **Security features:** Hardware security modules / secure elements for cryptographic key storage, TLS 1.3 / IPsec tunnel encryption, role-based grid operator access, and tamper-evident casing.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Hardware Security Modules & Secure Elements (Class II)](hardware-security-modules.md)
- [Industrial Automation & Control Systems (IACS)](industrial-automation-control-systems.md)
- [Smart Meter Gateways (Critical)](../critical/smart-meter-gateways-critical.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
