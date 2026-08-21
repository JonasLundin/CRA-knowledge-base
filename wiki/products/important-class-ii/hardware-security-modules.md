---
type: Product Category
title: Hardware Security Modules and Secure Elements (Class II)
description: Hardware Security Modules (HSMs), smart cards, secure elements, and smartcard readers under Annex III Class II point 5 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-ii, hsm, secure-element, smartcards, cryptography]
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
  provision: Annex III Class II point 5, Article 32(3)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 5 of Annex III Class II covers dedicated cryptographic hardware devices, including Hardware Security Modules (HSMs), secure elements (eSE), smart cards, and smart card readers.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Mandates third-party conformity assessment under Article 32(3) (Module B+C, Module H, or EUCC/CSA certification at level 'substantial'). Self-assessment is prohibited.[^cra-art-32]

# Applicability

Applies to:
- Dedicated network and PCIe Hardware Security Modules (HSMs) used in banking, PKI, and cloud services;
- Embedded Secure Elements (eSE) and eSIM microcontrollers;
- Smart cards used for identity verification and digital signatures;
- Physical smart card readers and USB cryptographic tokens.[^reg-2025-2392]

# Requirements or coverage

- **Mandatory conformity assessment route:** **Module B + C** or **Module H** evaluated by a notified body, or European cybersecurity certificate (Article 32(3));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 39 / 41 (CEN/TC 224);
- **Cryptographic assurance:** Physical enclosure protection, active zeroization of master keys upon physical intrusion, Common Criteria (ISO/IEC 15408 / EUCC) alignment, and side-channel resistance.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [PKI & Digital Certificate Issuance Software](../important-class-i/pki-and-certificate-software.md)
- [Smartcards & Secure Elements (Critical)](../critical/smartcards-and-secure-elements.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
