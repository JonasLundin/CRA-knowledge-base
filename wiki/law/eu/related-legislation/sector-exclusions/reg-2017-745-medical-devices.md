---
type: Legal Instrument
title: Regulation (EU) 2017/745 (Medical Devices Regulation - Sector Exclusion)
description: Statutory exclusion of medical devices and medical device software from the scope of the Cyber Resilience Act under CRA Article 2(2)(a).
category: law
tags: [cra, sector-exclusion, mdr, medical-devices, samd, article-2]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-08-21T00:00:00Z
sources:
  - id: reg-2017-745
    resource: http://data.europa.eu/eli/reg/2017/745/oj/eng
    title: Regulation (EU) 2017/745 on medical devices (MDR)
    author: European Parliament and Council
    last_modified: 2017-05-05T00:00:00Z
  - id: cra-art-2
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
    title: Regulation (EU) 2024/2847, Article 2
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  celex: 32017R0745
  eli: http://data.europa.eu/eli/reg/2017/745/oj/eng
  relevant_cra_provisions:
    - Article 2(2)(a)
    - Recital 18
    - Recital 19
  applicability: full_statutory_exclusion
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) 2017/745 (Medical Devices Regulation / MDR) establishes the comprehensive regulatory regime for medical devices and their accessories placed on the EU market.[^reg-2017-745] Under Cyber Resilience Act Article 2(2)(a), products with digital elements to which Regulation (EU) 2017/745 applies are completely excluded from the scope of the CRA to avoid regulatory overlap and respect the dedicated medical safety framework.[^cra-art-2]

# Interaction and scope relationship

The relationship between the MDR and the CRA is a complete statutory exclusion:
- Products falling within the definition and regulatory scope of Regulation (EU) 2017/745 are exempt from all CRA requirements, including Annex I essential requirements, Article 14 vulnerability reporting, and CRA CE marking.[^cra-art-2]
- Medical devices are governed exclusively by the cybersecurity, risk management, software lifecycle, and vigilance provisions embedded within the MDR framework.[^reg-2017-745]

# When the instrument applies

Regulation (EU) 2017/745 applies whenever a product meets the definition of a medical device under MDR Article 2(1), including:
- Standalone Software as a Medical Device (SaMD) intended for diagnostic, therapeutic, monitoring, or predictive medical purposes;[^reg-2017-745]
- Embedded software, firmware, and connected hardware components incorporated into active medical devices (e.g., pacemakers, infusion pumps, surgical robots);[^reg-2017-745]
- Accessories specifically intended by their manufacturer to be used together with a medical device.[^reg-2017-745]

# Exclusion or concurrency with CRA

Under CRA Article 2(2)(a), the CRA does not apply to products with digital elements covered by Regulation (EU) 2017/745. The exclusion is total and non-concurrent for the medical device itself.[^cra-art-2]

**Boundary condition:** General-purpose IT hardware, operating systems, or cloud infrastructure that are not manufactured as dedicated medical devices or medical device accessories remain subject to the CRA even if used within healthcare environments.[^cra-art-2]

# Technical or procedural satisfaction of CRA elements

The cybersecurity of medical devices is enforced independently through MDR provisions and MDCG guidance:[^reg-2017-745]
1. **General Safety and Performance Requirements (GSPRs):** MDR Annex I sets binding cybersecurity rules:
   - **GSPR 14.2:** Interoperability and compatibility without compromising safety;
   - **GSPR 17.1 & 17.2:** Software lifecycle, risk management, verification, validation, and state-of-the-art information security;
   - **GSPR 17.4:** Minimum IT environment and network security requirements.
2. **Conformity assessment:** Conducted by MDR-designated Notified Bodies under MDR Chapter IV rather than CRA notified bodies.[^reg-2017-745]
3. **Vigilance and post-market surveillance:** Cybersecurity incidents and serious incidents are reported under MDR Articles 87–92 and logged into EUDAMED rather than the CRA Single Reporting Platform.[^reg-2017-745]

# Relevant provisions

- **Regulation (EU) 2017/745:** Article 2(1) (Definitions), Annex I Section 14.2 & Section 17 (Software and IT security requirements), Articles 87–92 (Vigilance).[^reg-2017-745]
- **Regulation (EU) 2024/2847:** Article 2(2)(a) (Exclusion of medical devices), Recitals 18, 19.[^cra-art-2]

# Dates and transition

- Regulation (EU) 2017/745 entered into application on 26 May 2021.[^reg-2017-745]
- The CRA exclusion under Article 2(2)(a) applies from the entry into force of the CRA.[^cra-art-2]

# Related concepts

- [Scope & Exclusions Overview](../../../../obligations/scope/exclusions.md)
- [Regulation (EU) 2017/746 (In Vitro Diagnostics Exclusion)](reg-2017-746-in-vitro-diagnostics.md)
- [CRA Article 2: Scope](../../cra/articles/article-2.md)

[^reg-2017-745]: Regulation (EU) 2017/745, http://data.europa.eu/eli/reg/2017/745/oj/eng
[^cra-art-2]: Regulation (EU) 2024/2847, Article 2, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
