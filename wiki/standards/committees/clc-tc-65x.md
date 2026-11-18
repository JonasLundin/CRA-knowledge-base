---
type: Authority
title: CLC/TC 65X
description: CENELEC Technical Committee 65X Industrial-process measurement, control and automation developing CRA standards for operational technology (OT) and industrial cybersecurity.
category: standard
tags: [cra, cenelec, clc-tc65x, industrial-automation, ot-security, iec-62443, m606]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-05-18T00:00:00Z
sources:
  - id: clc-tc65x
    resource: https://www.cenelec.eu/dyn/www/f?p=104:7:0::::FSP_ORG_ID:1257159
    title: CLC/TC 65X Industrial-process measurement, control and automation
    author: CENELEC
    last_modified: 2026-06-01T00:00:00Z
  - id: stan4cra-clc65x
    resource: https://www.stan4cra.eu/clctc65x
    title: CLC TC 65X Technical Work
    author: STAN4CR
    last_modified: 2026-06-01T00:00:00Z
  - id: m606
    resource: https://ec.europa.eu/transparency/documents-register/detail?ref=C(2025)618&lang=en
    title: Commission Implementing Decision C(2025) 618 (Mandate M/606)
    author: European Commission
    last_modified: 2025-01-31T00:00:00Z
x-cra:
  committee_name: CLC/TC 65X
  standards_body: CENELEC
  mandate_lines: [20, 21, 22, 25, 27, 36]
  working_groups:
    - WG 3: Cyber Security (Industrial / OT security)
  key_references:
    - EN IEC 62443-4-1:2018/prAA (WI 81487)
    - EN IEC 62443-4-2:2019/prAA (WI 79973)
    - prEN 50770-1 to prEN 50770-6 (OT vertical profiles)
  checked_at: 2026-11-18T00:00:00Z
---

# Summary

CENELEC Technical Committee 65X (Industrial-process measurement, control and automation)[^clc-tc65x][^stan4cra-clc65x] develops European standardisation deliverables for industrial automation and control systems (IACS) and Operational Technology (OT) under Standardisation Request M/606[^m606]. CLC/TC 65X coordinates closely with IEC TC 65 under the Frankfurt Agreement.

# Legal effect

Deliverables and amendments developed by CLC/TC 65X do not confer presumption of conformity with Regulation (EU) 2024/2847 until approved as European Standards (EN) and cited in the Official Journal of the European Union (OJEU).

# Responsibilities and work programme

Working Group 3 (WG 3: Cyber Security) develops European amendments and vertical profiles (`prEN 50770` series) based on the `EN IEC 62443` series:
- **WI 81487**: `EN IEC 62443-4-1:2018/prAA` (Security for industrial automation and control systems - Secure product development lifecycle requirements).
- **WI 79973**: `EN IEC 62443-4-2:2019/prAA` (Security for industrial automation and control systems - Technical security requirements for IACS components).
- **`prEN 50770` Series**: Six dedicated Operational Technology (OT) vertical European Standard drafts profiling `EN IEC 62443-4-2` and `EN IEC 62443-4-1` for industrial network and security appliances.

# M/606 work allocation and `prEN 50770` deliverables

CLC/TC 65X WG 3 provides industrial/OT-specific vertical deliverables (`prEN 50770-1` to `prEN 50770-6`) for product categories shared with ETSI TC CYBER:
- **Topic 20 (`prEN 50770-4`)**: Virtual Private Network (VPN) products intended for industrial / OT use (CRA Annex III Class I point 5).
- **Topic 21 (`prEN 50770-2`)**: Network management systems (NMS) intended for industrial / OT use (CRA Annex III Class I point 6).
- **Topic 22 (`prEN 50770-6`)**: Security Information and Event Management (SIEM) systems intended for industrial / OT use (CRA Annex III Class I point 7).
- **Topic 25 (`prEN 50770-3`)**: Physical and virtual network interfaces for industrial / OT systems (CRA Annex III Class I point 10).
- **Topic 27 (`prEN 50770-5`)**: Industrial / OT routers, modems, and switches (CRA Annex III Class I point 12).
- **Topic 36 (`prEN 50770-1`)**: Firewalls and intrusion detection/prevention systems (IDS/IPS) specifically intended for industrial / OT use (CRA Annex III Class II point 2).

# Related concepts

- `standards/process/how-cra-standards-are-built`
- `standards/committees/etsi-tc-cyber-eusr`
- `standards/supporting/en-iec-62443-4-1`
- `standards/supporting/en-iec-62443-4-2`
- `standards/m606/line-20`
- `standards/m606/line-27`
- `standards/m606/line-36`

[^clc-tc65x]: CENELEC TC 65X. https://www.cenelec.eu/dyn/www/f?p=104:7:0::::FSP_ORG_ID:1257159
[^stan4cra-clc65x]: STAN4CR. CLC TC 65X Technical Work. https://www.stan4cra.eu/clctc65x
[^m606]: Commission Implementing Decision C(2025) 618. https://ec.europa.eu/transparency/documents-register/detail?ref=C(2025)618&lang=en
