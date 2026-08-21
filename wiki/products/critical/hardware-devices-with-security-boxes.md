---
type: Product Category
title: Hardware Devices with Security Boxes
description: Dedicated hardware devices containing physical tamper-proof security enclosures under Annex IV point 1 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, critical, security-boxes, hardware-security, cryptography, annex-iv]
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
  provision: Annex IV point 1, Article 32(4)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 1 of Annex IV designates hardware devices incorporating physical security boxes (hardened physical containment enclosures with active intrusion detection and automated cryptographic destruction) as Critical Products with Digital Elements.[^cra-annex-4] [^reg-2025-2392]

# Legal effect

Classified as Critical under Annex IV. Manufacturers must demonstrate conformity via mandatory European cybersecurity certification at assurance level 'high' pursuant to Article 32(4).[^cra-art-32]

# Applicability

Applies to:
- High-assurance physical security boxes protecting critical key management infrastructure;
- Physical cryptographic vaults used in inter-bank payment clearing networks;
- Hardened physical enclosures with active environmental tamper triggers (temperature, pressure, vibration, drill sensors).[^reg-2025-2392]

# Requirements or coverage

- **Mandatory certification route:** European cybersecurity certificate issued under an EU Cybersecurity Act (Regulation (EU) 2019/881) scheme (such as EUCC) at assurance level **'high'** (Article 32(4));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 39 (CEN/TC 224);
- **Physical resistance:** Full physical encapsulation, active multi-sensor tamper response circuits, immediate key zeroization, and resistance against invasive microprobing.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Hardware Security Modules & Secure Elements (Class II)](../important-class-ii/hardware-security-modules.md)
- [Smartcards, Readers & Secure Elements (Critical)](smartcards-and-secure-elements.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-4]: Regulation (EU) 2024/2847, Annex IV, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_4
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_32
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
