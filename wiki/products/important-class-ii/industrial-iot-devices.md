---
type: Product Category
title: Industrial IoT Devices for Critical Environments (Class II)
description: Connected industrial sensors, actuators, and edge gateways deployed in critical infrastructure under Annex III Class II point 7 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-ii, iiot, industrial-iot, ot, critical-infrastructure]
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
  provision: Annex III Class II point 7, Article 32(3)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 7 of Annex III Class II covers Industrial Internet of Things (IIoT) devices, industrial edge gateways, and connected field sensors deployed in essential infrastructure (energy, transport, water, manufacturing).[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Mandates third-party conformity assessment under Article 32(3) (Module B+C or Module H). Self-assessment is prohibited.[^cra-art-32]

# Applicability

Applies to:
- Industrial edge computing nodes and IoT gateways bridging OT fieldbuses with cloud platforms;
- Connected industrial actuators, valves, and flow meters used in automated chemical/utility facilities;
- Condition monitoring sensors with cellular, 5G private, or wireless mesh links deployed in critical sectors.[^reg-2025-2392]

# Requirements or coverage

- **Mandatory conformity assessment route:** **Module B + C** or **Module H** evaluated by a notified body, or European cybersecurity certificate (Article 32(3));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 37 (CLC/TC 65X / EN IEC 62443);
- **Security baselines:** Hardware-based identity provisioning (e.g. IEEE 802.1AR), mutual TLS authentication, encrypted telemetry, and remote attestation.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Industrial Automation & Control Systems (IACS)](industrial-automation-control-systems.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
