---
type: Product Category
title: Routers, Modems, and Switches for Critical Networks (Class II)
description: Routers, modems, and network switches intended for industrial, enterprise backbone, or telecommunications infrastructure use under Annex III Class II point 3 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-ii, routers, switches, critical-networking, industrial-ethernet]
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
  provision: Annex III Class II point 3, Article 32(3)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 3 of Annex III Class II covers routers, broadband modems, and network switches intended for industrial process networks, telecommunications carrier backbones, and critical enterprise infrastructure.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Mandates third-party conformity assessment under Article 32(3). Module A self-assessment is strictly excluded.[^cra-art-32]

# Applicability

Applies to:
- Carrier-grade core and edge routing equipment;
- Ruggedized industrial Ethernet switches used in power grids, transport, and manufacturing;
- Enterprise core distribution switches and data center fabrics.[^reg-2025-2392]

# Requirements or coverage

- **Mandatory conformity assessment route:** **Module B + C** or **Module H** evaluated by a notified body, or European cybersecurity certificate (Article 32(3));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 27 (ETSI EN 304-627);
- **Infrastructure-grade security:** BGP route origin validation, hardware root-of-trust boot validation, encrypted management planes (SSHv2 / TLS 1.3), MACsec wire-rate encryption, and isolated control/data planes.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Routers, Modems & Switches (Class I)](../important-class-i/routers-modems-switches.md)
- [Industrial Automation & Control Systems (IACS)](industrial-automation-control-systems.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
