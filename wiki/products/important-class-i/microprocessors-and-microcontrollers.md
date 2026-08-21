---
type: Product Category
title: Microprocessors and Microcontrollers (Class I)
description: General-purpose microprocessors and microcontrollers not covered by Class II under Annex III Class I point 13 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-i, microprocessors, microcontrollers, semiconductors, hardware]
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
  provision: Annex III Class I point 13, Article 32(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 13 of Annex III Class I covers microprocessors and microcontrollers placed on the market as discrete semiconductor components intended for integration into downstream digital products.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Semiconductor manufacturers placing standalone microprocessors or microcontrollers on the EU market must carry out Class I conformity assessment under Article 32(2) and document hardware security features in technical documentation.[^cra-art-32]

# Applicability

Applies to:
- General-purpose 32-bit and 64-bit microprocessors (MPUs);
- Embedded microcontrollers (MCUs) for IoT and industrial systems not categorized under Class II;
- System-on-Chip (SoC) integrated circuits sold as independent products.[^reg-2025-2392]

# Requirements or coverage

- **Conformity assessment route:** Module A (with full application of cited harmonised standards) or third-party Module B+C / Module H (Article 32(2));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 28 (CLC/TC 47X);
- **Hardware security properties:** Hardware memory protection (MPU/MMU), cryptographic acceleration, hardware random number generators (TRNG), and microcode update mechanisms.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Tamper-Resistant Microprocessors & Microcontrollers](tamper-resistant-hardware.md)
- [Boot Managers](boot-managers.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
