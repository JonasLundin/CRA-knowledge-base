---
type: Product Category
title: Smartcards, Readers, and Secure Elements (Critical)
description: High-assurance smartcards, secure elements, and reader hardware under Annex IV point 3 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, critical, smartcards, secure-elements, crypto-chips, annex-iv]
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
  provision: Annex IV point 3, Article 32(4)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 3 of Annex IV covers high-assurance smartcards, embedded secure elements, and cryptographic reader peripherals operating in highest-trust security environments (such as national electronic IDs, qualified signature creation devices, and banking clearance).[^cra-annex-4] [^reg-2025-2392]

# Legal effect

Classified as Critical under Annex IV. Manufacturers must demonstrate conformity via mandatory European cybersecurity certification at assurance level 'high' under Article 32(4).[^cra-art-32]

# Applicability

Applies to:
- Qualified Electronic Signature Creation Devices (QSCD) smartcards under eIDAS (Regulation (EU) No 910/2014);
- High-security embedded Secure Elements (eSE) and Integrated SIMs (iSIM);
- Class 3/4 smart card readers with encrypted pin-pads (PIN Entry Devices).[^reg-2025-2392]

# Requirements or coverage

- **Mandatory certification route:** European cybersecurity certificate issued under an EU Cybersecurity Act scheme (such as EUCC) at assurance level **'high'** (Article 32(4));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 41 (CEN/TC 224);
- **Cryptographic resilience:** Full state-of-the-art protection against side-channel analysis (DPA/CPA), fault injection (light, EM, laser), and physical probing.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Hardware Security Modules & Secure Elements (Class II)](../important-class-ii/hardware-security-modules.md)
- [Hardware Devices with Security Boxes](hardware-devices-with-security-boxes.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-4]: Regulation (EU) 2024/2847, Annex IV, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_4
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
