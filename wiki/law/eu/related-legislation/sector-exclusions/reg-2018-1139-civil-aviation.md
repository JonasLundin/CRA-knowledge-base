---
type: Legal Instrument
title: Regulation (EU) 2018/1139 (Civil Aviation Safety - Sector Exclusion)
description: Statutory exclusion of civil aviation products, parts, non-installed equipment, ATM/ANS systems, and certified drones from the Cyber Resilience Act under CRA Article 2(2)(c).
category: law
tags: [cra, sector-exclusion, aviation, easa, part-is, drones, article-2]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-08-21T00:00:00Z
sources:
  - id: reg-2018-1139
    resource: http://data.europa.eu/eli/reg/2018/1139/oj/eng
    title: Regulation (EU) 2018/1139 on common rules in the field of civil aviation and establishing a European Union Aviation Safety Agency (EASA)
    author: European Parliament and Council
    last_modified: 2018-08-22T00:00:00Z
  - id: reg-2023-203
    resource: http://data.europa.eu/eli/reg_del/2023/203/oj/eng
    title: Commission Delegated Regulation (EU) 2023/203 on management of information security risks in civil aviation (Part-IS)
    author: European Commission
    last_modified: 2023-02-17T00:00:00Z
  - id: cra-art-2
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
    title: Regulation (EU) 2024/2847, Article 2
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  celex: 32018R1139
  eli: http://data.europa.eu/eli/reg/2018/1139/oj/eng
  relevant_cra_provisions:
    - Article 2(2)(c)
    - Recital 20
  applicability: full_statutory_exclusion
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) 2018/1139 (EASA Basic Regulation) establishes common safety rules for civil aviation and establishes the European Union Aviation Safety Agency (EASA).[^reg-2018-1139] Under Cyber Resilience Act Article 2(2)(c), products with digital elements certified, declared, or approved under Regulation (EU) 2018/1139 are excluded from the CRA, ensuring that aeronautical cybersecurity remains exclusively under the unified EASA safety regulatory framework.[^cra-art-2]

# Interaction and scope relationship

The relationship between Regulation (EU) 2018/1139 and the CRA is a complete statutory exclusion:
- Aircraft, avionics, airborne software, flight control systems, air traffic management (ATM/ANS) systems, and certified unmanned aircraft systems (UAS) are exempt from CRA requirements.[^cra-art-2]
- All airworthiness, software security assurance (e.g., ED-202A / DO-326A, ED-203A / DO-356A), and incident reporting requirements are administered by EASA and national aviation authorities.[^reg-2018-1139][^reg-2023-203]

# When the instrument applies

Regulation (EU) 2018/1139 applies whenever:
- An aircraft, engine, propeller, part, or non-installed equipment undergoes design certification, type-approval, or declaration under Article 9;[^reg-2018-1139]
- ATM/ANS systems and constituents are certified or declared under Article 40;[^reg-2018-1139]
- Unmanned aircraft systems requiring certification under Article 56 are placed on the market;[^reg-2018-1139]
- Aviation organisations implement Information Security Management Systems under Part-IS (Delegated Regulation (EU) 2023/203).[^reg-2023-203]

# Exclusion or concurrency with CRA

Under CRA Article 2(2)(c), products with digital elements subject to Regulation (EU) 2018/1139 are excluded from CRA scope. The exclusion applies to all digital hardware and software integral to the certified aviation design.[^cra-art-2]

**Boundary condition:** General-purpose consumer electronic devices (such as non-certified passenger tablets, consumer portable flight tracking accessories, or open-category toy drones not subject to EASA design certification) remain subject to the CRA.[^cra-art-2]

# Technical or procedural satisfaction of CRA elements

Aviation cybersecurity is governed through strict airworthiness certification and organisational standards:[^reg-2018-1139][^reg-2023-203]
1. **Design and airworthiness standards:** Aircraft cybersecurity is evaluated under CS-25/CS-23 certification specifications implementing EUROCAE ED-202A / RTCA DO-326A (Airworthiness Security Process Specification) and ED-203A / DO-356A (Airworthiness Security Methods).[^reg-2018-1139]
2. **Part-IS Information Security Management:** Commission Delegated Regulation (EU) 2023/203 and Implementing Regulation (EU) 2023/205 establish binding Part-IS requirements for identifying cybersecurity risks in information systems used for civil aviation operations.[^reg-2023-203]
3. **Occurrence reporting:** Aviation cybersecurity incidents are reported under Regulation (EU) No 376/2014 and EASA safety mechanisms rather than the CRA Single Reporting Platform.[^reg-2018-1139]

# Relevant provisions

- **Regulation (EU) 2018/1139:** Article 9 & Annex II (Airworthiness and environmental protection), Article 40 & Annex VIII (ATM/ANS equipment), Article 56 & Annex IX (Unmanned aircraft systems).[^reg-2018-1139]
- **Delegated Regulation (EU) 2023/203:** Part-IS requirements on information security management for aviation organisations.[^reg-2023-203]
- **Regulation (EU) 2024/2847:** Article 2(2)(c) (Exclusion of civil aviation products), Recital 20.[^cra-art-2]

# Dates and transition

- Regulation (EU) 2018/1139 entered into force on 11 September 2018.[^reg-2018-1139]
- Delegated Regulation (EU) 2023/203 (Part-IS) applies from 16 October 2025.[^reg-2023-203]
- The CRA Article 2(2)(c) exclusion applies from CRA entry into force.[^cra-art-2]

# Related concepts

- [Scope & Exclusions Overview](../../../../obligations/scope/exclusions.md)
- [CRA Article 2: Scope](../../cra/articles/article-2.md)

[^reg-2018-1139]: Regulation (EU) 2018/1139, http://data.europa.eu/eli/reg/2018/1139/oj/eng
[^reg-2023-203]: Commission Delegated Regulation (EU) 2023/203, http://data.europa.eu/eli/reg_del/2023/203/oj/eng
[^cra-art-2]: Regulation (EU) 2024/2847, Article 2, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
