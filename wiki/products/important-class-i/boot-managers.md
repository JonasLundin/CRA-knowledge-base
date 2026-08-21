---
type: Product Category
title: Boot Managers
description: Firmware and software boot managers responsible for initialising operating environments under Annex III Class I point 8 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-i, boot-managers, firmware, secure-boot]
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
  provision: Annex III Class I point 8, Article 32(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 8 of Annex III Class I covers boot managers (UEFI/BIOS bootloaders, second-stage bootloaders, and firmware initialization code) placed on the market as independent software products or embedded firmware.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Boot managers must undergo Class I conformity assessment under Article 32(2) to prevent firmware-level compromise and rootkit persistence beneath operating system visibility.[^cra-art-32]

# Applicability

Applies to:
- Standalone multi-boot loaders and UEFI application boot loaders;
- Embedded bootloader firmware for microcontrollers, system-on-chip (SoC) platforms, and embedded compute boards.[^reg-2025-2392]

# Requirements or coverage

- **Conformity assessment route:** Module A (with full application of cited harmonised standards) or third-party Module B+C / Module H (Article 32(2));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 23 (ETSI EN 304-623);
- **Root of trust & secure boot:** Enforce cryptographic signature verification of downstream kernel images and prevent unauthorized firmware modification.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Operating Systems (Class I)](operating-systems.md)
- [Tamper-Resistant Microprocessors & Microcontrollers](tamper-resistant-hardware.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
