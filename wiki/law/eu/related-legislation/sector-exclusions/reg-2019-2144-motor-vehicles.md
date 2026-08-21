---
type: Legal Instrument
title: Regulation (EU) 2019/2144 (Motor Vehicles General Safety - Sector Exclusion)
description: Statutory exclusion of type-approved motor vehicles, systems, components, and separate technical units from the Cyber Resilience Act under CRA Article 2(2)(d).
category: law
tags: [cra, sector-exclusion, automotive, gsr, un-r155, un-r156, article-2]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-08-21T00:00:00Z
sources:
  - id: reg-2019-2144
    resource: http://data.europa.eu/eli/reg/2019/2144/oj/eng
    title: Regulation (EU) 2019/2144 on type-approval requirements for motor vehicles and their trailers (General Safety Regulation / GSR)
    author: European Parliament and Council
    last_modified: 2019-12-16T00:00:00Z
  - id: reg-2018-858
    resource: http://data.europa.eu/eli/reg/2018/858/oj/eng
    title: Regulation (EU) 2018/858 on the approval and market surveillance of motor vehicles and their trailers
    author: European Parliament and Council
    last_modified: 2018-06-14T00:00:00Z
  - id: cra-art-2
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
    title: Regulation (EU) 2024/2847, Article 2
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  celex: 32019R2144
  eli: http://data.europa.eu/eli/reg/2019/2144/oj/eng
  relevant_cra_provisions:
    - Article 2(2)(d)
    - Recital 21
  applicability: full_statutory_exclusion
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) 2019/2144 (Vehicle General Safety Regulation / GSR) establishes type-approval requirements for motor vehicles (categories M, N, and O) and their systems, components, and separate technical units.[^reg-2019-2144] Under Cyber Resilience Act Article 2(2)(d), products with digital elements subject to Regulation (EU) 2019/2144 are fully excluded from the CRA because the automotive sector is governed by dedicated international and EU cybersecurity type-approval standards.[^cra-art-2]

# Interaction and scope relationship

The relationship between Regulation (EU) 2019/2144 and the CRA is a complete statutory exclusion:
- Type-approved motor vehicles, in-vehicle Electronic Control Units (ECUs), telematics control units (TCUs), infotainment units, and autonomous driving systems are exempt from CRA essential requirements, CE marking, and Article 14 reporting.[^cra-art-2]
- Cybersecurity is governed through the type-approval framework of Regulation (EU) 2018/858 and the UNECE regulations mandated under the GSR.[^reg-2019-2144]

# When the instrument applies

Regulation (EU) 2019/2144 applies whenever:
- Motor vehicles of category M (passenger transport), N (goods transport), and O (trailers) are type-approved for the EU market;[^reg-2018-858]
- Systems, components, or separate technical units intended for installation in such vehicles undergo type-approval;[^reg-2019-2144]
- Automotive manufacturers establish and maintain a Cybersecurity Management System (CSMS) and Software Update Management System (SUMS).[^reg-2019-2144]

# Exclusion or concurrency with CRA

Under CRA Article 2(2)(d), the CRA does not apply to products covered by Regulation (EU) 2019/2144. The exclusion is total for type-approved vehicle equipment.[^cra-art-2]

**Boundary condition:** Aftermarket non-type-approved digital accessories (e.g., standalone smartphone navigation mounts, generic consumer dashcams, or third-party diagnostic apps that are not certified as automotive separate technical units) remain within the horizontal scope of the CRA.[^cra-art-2]

# Technical or procedural satisfaction of CRA elements

Automotive cybersecurity is enforced via binding international standards incorporated into EU law:[^reg-2019-2144]
1. **UN Regulation No 155 (Cybersecurity & CSMS):** Mandates that vehicle manufacturers implement an audited Cybersecurity Management System covering the vehicle development, production, and post-production phases, including vulnerability tracking and risk assessments.[^reg-2019-2144]
2. **UN Regulation No 156 (Software Updates & SUMS):** Mandates secure over-the-air (OTA) and wired software updates, update traceability, and type-approval validity post-update.[^reg-2019-2144]
3. **Type-approval approval authority:** Approvals are issued by national vehicle type-approval authorities (e.g., KBA in Germany, RDW in the Netherlands, Transportstyrelsen in Sweden) based on technical service audits rather than NLF notified bodies.[^reg-2018-858]

# Relevant provisions

- **Regulation (EU) 2019/2144:** Article 4 (General obligations and technical requirements), Annex II (Incorporation of UN Regulations No 155 and No 156).[^reg-2019-2144]
- **Regulation (EU) 2018/858:** Articles 6–8 (General obligations of manufacturers and type-approval framework).[^reg-2018-858]
- **Regulation (EU) 2024/2847:** Article 2(2)(d) (Exclusion of motor vehicles), Recital 21.[^cra-art-2]

# Dates and transition

- UN Regulation No 155 and No 156 compliance became mandatory for all new vehicle types from July 2022 and for all new vehicles produced from July 2024 under Regulation (EU) 2019/2144.[^reg-2019-2144]
- The CRA Article 2(2)(d) exclusion applies from CRA entry into force.[^cra-art-2]

# Related concepts

- [Scope & Exclusions Overview](../../../../obligations/scope/exclusions.md)
- [Regulation (EU) No 168/2013 (L-Category Vehicles)](reg-168-2013-l-category-vehicles.md)
- [CRA Article 2: Scope](../../cra/articles/article-2.md)

[^reg-2019-2144]: Regulation (EU) 2019/2144, http://data.europa.eu/eli/reg/2019/2144/oj/eng
[^reg-2018-858]: Regulation (EU) 2018/858, http://data.europa.eu/eli/reg/2018/858/oj/eng
[^cra-art-2]: Regulation (EU) 2024/2847, Article 2, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
