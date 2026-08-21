---
type: Product Category
title: Tamper-Evident Microprocessors and Microcontrollers (Class II)
description: High-assurance microprocessors and microcontrollers with advanced tamper-evident mechanisms under Annex III Class II point 8 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-ii, semiconductors, tamper-evident, crypto-processor, hardware-security]
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
  provision: Annex III Class II point 8, Article 32(3)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 8 of Annex III Class II covers high-assurance microprocessors, microcontrollers, and secure enclave ICs manufactured with active tamper-evident shields, physical unclonable functions (PUF), and high-grade side-channel resistance.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Mandates third-party conformity assessment under Article 32(3) (Module B+C, Module H, or Common Criteria / EUCC certification). Self-assessment is prohibited.[^cra-art-32]

# Applicability

Applies to:
- Secure microcontrollers used in government identity documents and electronic passports;
- High-assurance payment terminal (PoS) crypto-processors;
- Automotive secure gateway microcontrollers managing critical vehicle bus commands.[^reg-2025-2392]

# Requirements or coverage

- **Mandatory conformity assessment route:** **Module B + C** or **Module H** evaluated by a notified body, or European cybersecurity certificate (Article 32(3));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 38 (CLC/TC 47X);
- **Advanced physical security:** Laser fault injection mitigation, active sensor mesh shielding across silicon layers, dynamic bus encryption, and PUF-derived key generation.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Tamper-Resistant Microprocessors & Microcontrollers (Class I)](../important-class-i/tamper-resistant-hardware.md)
- [Hardware Security Modules & Secure Elements (Class II)](hardware-security-modules.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
