---
type: Legal Instrument
title: Regulation (EU) 2017/746 (In Vitro Diagnostic Medical Devices - Sector Exclusion)
description: Statutory exclusion of in vitro diagnostic medical devices and IVD software from the scope of the Cyber Resilience Act under CRA Article 2(2)(b).
category: law
tags: [cra, sector-exclusion, ivdr, in-vitro-diagnostics, samd, article-2]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-08-21T00:00:00Z
sources:
  - id: reg-2017-746
    resource: http://data.europa.eu/eli/reg/2017/746/oj/eng
    title: Regulation (EU) 2017/746 on in vitro diagnostic medical devices (IVDR)
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
  celex: 32017R0746
  eli: http://data.europa.eu/eli/reg/2017/746/oj/eng
  relevant_cra_provisions:
    - Article 2(2)(b)
    - Recital 18
    - Recital 19
  applicability: full_statutory_exclusion
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) 2017/746 (In Vitro Diagnostic Medical Devices Regulation / IVDR) establishes the regulatory framework for in vitro diagnostic medical devices, diagnostic software, and accessories placed on the EU market.[^reg-2017-746] Under Cyber Resilience Act Article 2(2)(b), products with digital elements covered by Regulation (EU) 2017/746 are fully excluded from the scope of the CRA.[^cra-art-2]

# Interaction and scope relationship

The interaction is a complete statutory exclusion:
- Products falling within the definition and scope of Regulation (EU) 2017/746 do not need to comply with CRA Annex I essential requirements, Article 14 reporting, or CRA conformity procedures.[^cra-art-2]
- Cybersecurity, software lifecycle, and incident reporting for IVD products are regulated under the dedicated IVDR framework.[^reg-2017-746]

# When the instrument applies

Regulation (EU) 2017/746 applies whenever a product qualifies as an in vitro diagnostic medical device under IVDR Article 2(2), including:
- Standalone diagnostic software and algorithms used for analyzing human specimens;[^reg-2017-746]
- Automated diagnostic laboratory instruments, DNA sequencers, PCR machines, and connected analyzers;[^reg-2017-746]
- Dedicated accessories and digital data systems intended to enable the diagnostic function of an IVD device.[^reg-2017-746]

# Exclusion or concurrency with CRA

Under CRA Article 2(2)(b), the CRA does not apply to products with digital elements subject to Regulation (EU) 2017/746. The exclusion is total and non-concurrent.[^cra-art-2]

**Boundary condition:** General-purpose laboratory IT equipment, office computers, or hospital local area networks that are not classified as IVD devices or IVD accessories remain within the horizontal scope of the CRA.[^cra-art-2]

# Technical or procedural satisfaction of CRA elements

IVD device cybersecurity is evaluated exclusively under the IVDR framework:[^reg-2017-746]
1. **General Safety and Performance Requirements (GSPRs):** IVDR Annex I imposes binding cybersecurity obligations:
   - **GSPR 13.2:** Safe interoperability with external devices and networks;
   - **GSPR 16.1 & 16.2:** Secure software development lifecycle, risk analysis, and information security management;
   - **GSPR 16.4:** Hardware, network, and environmental operating parameters.
2. **Conformity assessment:** Conducted by IVDR-designated Notified Bodies under IVDR Chapter IV.[^reg-2017-746]
3. **Vigilance and reporting:** Serious incidents and field safety corrective actions are reported under IVDR Articles 82–87 to national competent authorities and logged in EUDAMED.[^reg-2017-746]

# Relevant provisions

- **Regulation (EU) 2017/746:** Article 2(2) (Definitions), Annex I Section 13.2 & Section 16 (Software and cybersecurity requirements), Articles 82–87 (Vigilance).[^reg-2017-746]
- **Regulation (EU) 2024/2847:** Article 2(2)(b) (Exclusion of IVD medical devices), Recitals 18, 19.[^cra-art-2]

# Dates and transition

- Regulation (EU) 2017/746 entered into application on 26 May 2022.[^reg-2017-746]
- The CRA exclusion under Article 2(2)(b) applies from the entry into force of the CRA.[^cra-art-2]

# Related concepts

- [Regulation (EU) 2017/745 (Medical Devices Exclusion)](reg-2017-745-medical-devices.md)
- [Scope & Exclusions Overview](../../../../obligations/scope/exclusions.md)
- [CRA Article 2: Scope](../../cra/articles/article-2.md)

[^reg-2017-746]: Regulation (EU) 2017/746, http://data.europa.eu/eli/reg/2017/746/oj/eng
[^cra-art-2]: Regulation (EU) 2024/2847, Article 2, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
