---
type: Product Category
title: Network Management Systems
description: Centralised network management and orchestration systems under Annex III Class I point 6 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-i, network-management, nms, orchestration]
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
  provision: Annex III Class I point 6, Article 32(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 6 of Annex III Class I covers network management systems (NMS) designed to monitor, configure, control, and optimize computer networks and infrastructure devices.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

NMS software and appliances are subject to Class I conformity assessment under Article 32(2) to mitigate systemic risks of widespread network compromise or administrative takeover.[^cra-art-32]

# Applicability

Applies to:
- Software controllers and orchestration platforms managing network switches, routers, and access points;
- Software-Defined Networking (SDN) controllers;
- Network configuration and topology management suites.[^reg-2025-2392]

# Requirements or coverage

- **Conformity assessment route:** Module A (with full application of cited harmonised standards) or third-party Module B+C / Module H (Article 32(2));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 21 (ETSI EN 304-621);
- **Control plane security:** Multi-factor administrative authentication, encrypted telemetry/control links, and role-based access control.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Routers, Modems & Switches (Class I)](routers-modems-switches.md)
- [Security Information & Event Management (SIEM)](siem-systems.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
