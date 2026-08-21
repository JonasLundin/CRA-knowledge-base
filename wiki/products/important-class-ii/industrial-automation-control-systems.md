---
type: Product Category
title: Industrial Automation and Control Systems (IACS)
description: Programmable logic controllers, distributed control systems, and industrial automation controllers under Annex III Class II point 6 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-ii, iacs, plc, scada, dcs, ot-security]
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
  provision: Annex III Class II point 6, Article 32(3)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 6 of Annex III Class II covers Industrial Automation and Control Systems (IACS) designed for operational technology (OT) monitoring, automation, and physical process control.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Mandates third-party conformity assessment under Article 32(3) (Module B+C or Module H). Self-assessment (Module A) is prohibited.[^cra-art-32]

# Applicability

Applies to:
- Programmable Logic Controllers (PLCs) and Remote Terminal Units (RTUs);
- Distributed Control Systems (DCS) engineering workstations and controllers;
- Supervisory Control and Data Acquisition (SCADA) master controllers and human-machine interface (HMI) panels;
- Industrial PCs (IPCs) executing automated process control logic.[^reg-2025-2392]

# Requirements or coverage

- **Mandatory conformity assessment route:** **Module B + C** or **Module H** evaluated by a notified body, or European cybersecurity certificate (Article 32(3));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 37 (CLC/TC 65X / EN IEC 62443 family);
- **OT security properties:** Firmware signing, deterministic process isolation, support for network segmentation (Purdue model zones), robust handling of malformed industrial bus frames, and secure remote engineering access.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Industrial IoT Devices for Critical Environments](industrial-iot-devices.md)
- [Firewalls & IDPS (Class II)](firewalls-and-idps.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
