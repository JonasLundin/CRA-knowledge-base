---
type: Product Category
title: Virtual Private Network (VPN) Products
description: Software and hardware products providing virtual private network encryption and tunneling functions under Annex III Class I point 5 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-i, vpn, tunneling, encryption, networking]
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
  provision: Annex III Class I point 5, Article 32(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 5 of Annex III Class I designates products with digital elements whose core function is virtual private network (VPN) client or server tunneling as Important Products (Class I).[^cra-annex-3] [^reg-2025-2392]

# Legal effect

VPN software and hardware appliances must satisfy the conformity assessment procedures of Article 32(2) and meet strict requirements on cryptographic suite selection, session management, and credential protection.[^cra-art-32]

# Applicability

Covers:
- Standalone VPN client applications for desktops, mobile devices, or embedded systems;
- Dedicated VPN gateway server software and hardware appliances;
- Remote access VPN appliances and site-to-site IPsec / WireGuard / TLS tunneling devices.[^reg-2025-2392]

# Requirements or coverage

- **Conformity assessment route:** Module A (with full application of cited harmonised standards) or third-party Module B+C / Module H (Article 32(2));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 20 (ETSI EN 304-620);
- **Crypto evaluation:** Cryptographic algorithms, key negotiation, and forward secrecy must comply with state-of-the-art standards.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Network Management Systems](network-management-systems.md)
- [Routers, Modems & Switches (Class I)](routers-modems-switches.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
