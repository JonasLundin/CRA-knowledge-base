---
type: Product Category
title: Password Managers
description: Software applications designed to store, generate, and manage credentials and secrets under Annex III Class I point 3 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-i, password-managers, credentials, vault]
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
  provision: Annex III Class I point 3, Article 32(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 3 of Annex III Class I classifies password managers as Important Products with Digital Elements (Class I), with technical parameters defined in Commission Implementing Regulation (EU) 2025/2392.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Password managers must meet Class I conformity assessment requirements under Article 32(2), with strict emphasis on end-to-end cryptographic protection, key derivation, and secure credential storage.[^cra-art-32]

# Applicability

Covers software applications whose primary purpose is to securely store, retrieve, auto-fill, generate, and synchronise passwords, passkeys, cryptographic keys, and sensitive authentication credentials across devices.[^reg-2025-2392]

# Requirements or coverage

- **Conformity assessment route:** Module A (with full application of cited harmonised standards) or third-party Module B+C / Module H (Article 32(2));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 18 (ETSI EN 304-618);
- **Remote processing coverage:** Cloud sync backends operated by the password manager provider qualify as remote data processing solutions under Article 3(2) and must be assessed in scope.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Identity Management & Privileged Access Systems](identity-management-systems.md)
- [Remote Data Processing Solutions](../../obligations/scope/remote-data-processing.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
