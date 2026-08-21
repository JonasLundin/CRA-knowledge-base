---
type: Product Category
title: Firewalls and Intrusion Detection Systems (Class II)
description: Enterprise and industrial firewalls, intrusion detection and prevention systems under Annex III Class II point 2 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-ii, firewalls, idps, industrial-firewalls, perimeter-security]
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
  provision: Annex III Class II point 2, Article 32(3)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 2 of Annex III Class II covers firewalls, intrusion detection systems (IDS), and intrusion prevention systems (IPS) intended for industrial control networks, enterprise perimeters, and critical infrastructure environments.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Mandates third-party conformity assessment under Article 32(3) (Module B+C or Module H). Self-assessment (Module A) is prohibited.[^cra-art-32]

# Applicability

Applies to:
- Next-Generation Firewalls (NGFW) for enterprise data centers and campus networks;
- Industrial firewalls protecting operational technology (OT) and SCADA zones;
- Enterprise-scale Network Intrusion Prevention Systems (NIPS) and Deep Packet Inspection (DPI) appliances.[^reg-2025-2392]

# Requirements or coverage

- **Mandatory conformity assessment route:** **Module B + C** or **Module H** evaluated by a notified body, or European cybersecurity certificate (Article 32(3));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 36 (ETSI EN 304-636);
- **Industrial and high-assurance properties:** Deep packet inspection of industrial protocols (e.g. Modbus, OPC UA, DNP3), resilient high-availability failover, tamper resistance, and audited rule parsing engines.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Firewalls & IDPS (Class I)](../important-class-i/firewalls-and-idps-class-i.md)
- [Industrial Automation & Control Systems (IACS)](industrial-automation-control-systems.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
