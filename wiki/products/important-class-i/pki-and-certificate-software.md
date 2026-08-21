---
type: Product Category
title: Public Key Infrastructure and Digital Certificate Issuance Software
description: Software applications for PKI management and digital certificate issuance under Annex III Class I point 9 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-i, pki, certificates, cryptography, ca]
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
  provision: Annex III Class I point 9, Article 32(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 9 of Annex III Class I covers public key infrastructure (PKI) software and digital certificate generation, validation, and revocation software.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

PKI software products are subject to Class I conformity assessment under Article 32(2), recognizing their foundational role in trust anchor management, TLS validation, and electronic signing across digital infrastructure.[^cra-art-32]

# Applicability

Applies to:
- Certificate Authority (CA) software suites and Registration Authority (RA) software;
- Automated certificate management protocol (e.g. ACME, EST, SCEP) servers;
- OCSP responder and CRL generation software.[^reg-2025-2392]

# Requirements or coverage

- **Conformity assessment route:** Module A (with full application of cited harmonised standards) or third-party Module B+C / Module H (Article 32(2));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 24 (ETSI EN 304-624);
- **Cryptographic key protection:** Strict key isolation, entropy verification, secure zeroization, and audit logging of all certificate operations.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Identity Management & Privileged Access Systems](identity-management-systems.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)
- [Hardware Security Modules](../../products/important-class-ii/hardware-security-modules.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
