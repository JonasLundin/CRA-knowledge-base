---
type: Product Category
title: Tamper-Resistant Microprocessors and Microcontrollers
description: Microprocessors and microcontrollers equipped with physical and logical anti-tamper mechanisms under Annex III Class I point 18 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-i, tamper-resistance, hardware-security, semiconductors]
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
  provision: Annex III Class I point 18, Article 32(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 18 of Annex III Class I covers microprocessors and microcontrollers engineered with physical and logical anti-tamper mechanisms to protect sensitive cryptographic operations and credentials against probing and side-channel analysis.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Requires Class I conformity assessment under Article 32(2), evaluating resistance against physical tampering, fault injection, and electrical manipulation.[^cra-art-32]

# Applicability

Applies to:
- Secure microcontrollers with active tamper-detection meshes and voltage/clock glitch detectors;
- Crypto-processor ICs with side-channel countermeasures (DPA/SPA resistance);
- Security controllers used in automotive, financial, or industrial embedded equipment.[^reg-2025-2392]

# Requirements or coverage

- **Conformity assessment route:** Module A (with full application of cited harmonised standards) or third-party Module B+C / Module H (Article 32(2));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 38 / 39 (CEN/TC 224 / CLC/TC 47X);
- **Physical security properties:** Active shielding, cryptographic key zeroization upon breach detection, and fault-injection countermeasures.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Microprocessors & Microcontrollers (Class I)](microprocessors-and-microcontrollers.md)
- [Hardware Security Modules](../../products/important-class-ii/hardware-security-modules.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
