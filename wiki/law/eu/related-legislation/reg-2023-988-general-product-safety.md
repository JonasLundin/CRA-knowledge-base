---
type: Legal Instrument
title: Regulation (EU) 2023/988 (General Product Safety Regulation)
description: Horizontal consumer product safety regulation interacting with CRA Article 11 as lex generalis and establishing specific cybersecurity risk carve-outs.
category: law
tags: [cra, gpsr, product-safety, article-11, lex-specialis, consumer-protection]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-08-21T00:00:00Z
sources:
  - id: reg-2023-988
    resource: http://data.europa.eu/eli/reg/2023/988/oj/eng
    title: Regulation (EU) 2023/988 on general product safety (GPSR)
    author: European Parliament and Council
    last_modified: 2023-05-23T00:00:00Z
  - id: cra-art-11
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_11
    title: Regulation (EU) 2024/2847, Article 11
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  celex: 32023R0988
  eli: http://data.europa.eu/eli/reg/2023/988/oj/eng
  relevant_cra_provisions:
    - Article 11
    - Recital 31
    - Recital 32
  applicability: lex_generalis_with_cyber_exclusion
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) 2023/988 (General Product Safety Regulation / GPSR) establishes the horizontal safety net for consumer products placed or made available on the EU market, ensuring high consumer health and safety protection where specific Union harmonisation legislation does not exist.[^reg-2023-988] Under Cyber Resilience Act Article 11, the CRA operates as lex specialis for cybersecurity risks, carving out specific chapters of the GPSR for products with digital elements while maintaining GPSR applicability for non-cyber risks.[^cra-art-11]

# Interaction and scope relationship

The relationship between the GPSR and the CRA follows the classic *lex specialis derogat legi generali* principle codified in GPSR Article 2(1) and CRA Article 11:
- **Cybersecurity risks:** The CRA provides specific, exhaustive Union harmonisation rules for cybersecurity aspects, vulnerability handling, and security updates of products with digital elements.[^cra-art-11]
- **Non-cyber risks:** The GPSR applies residually to consumer products with digital elements for other health and safety hazards (e.g., physical, mechanical, thermal, or choking hazards) not covered by specific sectoral legislation.[^reg-2023-988]

# When the instrument applies

Regulation (EU) 2023/988 applies whenever:
- A product with digital elements is supplied or made available to consumers and presents health or safety risks outside the scope of CRA cybersecurity requirements;[^reg-2023-988]
- General consumer safety traceability, product recalls, or consumer notice requirements for non-cyber defects are enforced under GPSR Articles 9, 35, and 36;[^reg-2023-988]
- Online marketplaces fulfill horizontal product safety obligations under GPSR Chapter IV for products sold to consumers.[^reg-2023-988]

# Exclusion or concurrency with CRA

Under CRA Article 11, the application of Regulation (EU) 2023/988 to products with digital elements is restricted as follows:[^cra-art-11]

1. **Exclusion of GPSR for cybersecurity risks:** Where a product with digital elements is subject to the CRA, the following GPSR provisions **do not apply** in relation to cybersecurity risks covered by the CRA:[^cra-art-11]
   - **Section 1 of Chapter III:** General obligations of economic operators (manufacturers, authorized representatives, importers, distributors);[^reg-2023-988]
   - **Chapter V:** Distance sales rules for economic operators;[^reg-2023-988]
   - **Chapter VII:** Safety Gate rapid alert system and information exchange;[^reg-2023-988]
   - **Chapters IX to XI:** Market surveillance, penalties, and final provisions.[^reg-2023-988]
2. **Concurrent application for non-cyber risks:** For consumer products with digital elements (such as smart toys, connected kitchen appliances, or wearable fitness trackers), the GPSR remains fully applicable to address non-cyber physical safety hazards.[^cra-art-11]

# Technical or procedural satisfaction of CRA elements

- **Safety Gate vs Single Reporting Platform:** Cybersecurity vulnerabilities and security incidents are reported through the ENISA Single Reporting Platform under CRA Article 14, rather than the Safety Gate rapid alert system under GPSR Chapter VII.[^cra-art-11]
- **Technical documentation and risk assessment:** When conducting the general product safety risk assessment under GPSR Article 6, manufacturers of consumer connected devices must account for cybersecurity vulnerabilities that could directly induce physical safety hazards (e.g., smart locks failing to unlock during a fire, or connected heaters overheating due to firmware manipulation). The cybersecurity controls themselves must meet CRA Annex I.[^reg-2023-988][^cra-art-11]

# Relevant provisions

- **Regulation (EU) 2023/988:** Article 1 (Subject matter), Article 2 (Scope and relationship with Union harmonisation legislation), Chapter III Section 1 (Obligations of manufacturers and operators), Chapter V (Distance sales), Chapter VII (Safety Gate), Chapters IX–XI (Market surveillance and penalties).[^reg-2023-988]
- **Regulation (EU) 2024/2847:** Article 11 (Interaction with Regulation (EU) 2023/988), Recitals 31, 32.[^cra-art-11]

# Dates and transition

- Regulation (EU) 2023/988 entered into force on 12 June 2023 and applies from 13 December 2024.[^reg-2023-988]
- CRA Article 11 carve-out rules apply from the main CRA date of application on 11 December 2027.[^cra-art-11]

# Related concepts

- [Scope & Exclusions Overview](../../../obligations/scope/index.md)
- [CRA Article 11: Interaction with GPSR](../cra/articles/article-11.md)
- [CRA Article 14: Notification Obligations](../cra/articles/article-14.md)

[^reg-2023-988]: Regulation (EU) 2023/988, http://data.europa.eu/eli/reg/2023/988/oj/eng
[^cra-art-11]: Regulation (EU) 2024/2847, Article 11, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_11
