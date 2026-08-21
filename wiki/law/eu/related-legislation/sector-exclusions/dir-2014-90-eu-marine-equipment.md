---
type: Legal Instrument
title: Directive 2014/90/EU (Marine Equipment Directive - Sector Exclusion)
description: Statutory exclusion of marine equipment placed on board EU flag ships from the scope of the Cyber Resilience Act under CRA Article 2(3).
category: law
tags: [cra, sector-exclusion, maritime, med, wheel-mark, imo, article-2]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-08-21T00:00:00Z
sources:
  - id: dir-2014-90-eu
    resource: http://data.europa.eu/eli/dir/2014/90/oj/eng
    title: Directive 2014/90/EU on marine equipment and repealing Council Directive 96/98/EC (MED)
    author: European Parliament and Council
    last_modified: 2014-08-28T00:00:00Z
  - id: cra-art-2
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
    title: Regulation (EU) 2024/2847, Article 2
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  celex: 32014L0090
  eli: http://data.europa.eu/eli/dir/2014/90/oj/eng
  relevant_cra_provisions:
    - Article 2(3)
    - Recital 22
  applicability: full_statutory_exclusion
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Directive 2014/90/EU (Marine Equipment Directive / MED) establishes harmonised safety and performance standards for equipment placed or intended to be placed on board EU flag ships pursuant to international maritime safety conventions (including SOLAS 1974).[^dir-2014-90-eu] Under Cyber Resilience Act Article 2(3), products with digital elements to which Directive 2014/90/EU applies are excluded from the scope of the CRA to respect the international maritime safety framework and the IMO convention regime.[^cra-art-2]

# Interaction and scope relationship

The relationship between Directive 2014/90/EU and the CRA is an express statutory exclusion:
- Equipment placed on board EU ships requiring flag-state type-approval under international conventions and certified with the 'wheel mark' is exempt from the CRA.[^cra-art-2]
- Maritime cybersecurity for such systems is regulated under the MED and the relevant International Maritime Organization (IMO) resolutions (e.g., MSC.428(98) on Maritime Cyber Risk Management in safety management systems).[^dir-2014-90-eu]

# When the instrument applies

Directive 2014/90/EU applies whenever:
- Marine equipment (such as bridge navigation systems, ECDIS, radar, automatic identification systems (AIS), Voyage Data Recorders (VDR), and radio communication equipment) is placed on board an EU ship;[^dir-2014-90-eu]
- The equipment is listed in Commission implementing regulations adopted under MED Article 35 specifying applicable testing standards;[^dir-2014-90-eu]
- The equipment undergoes conformity assessment by MED notified bodies and receives the wheel mark.[^dir-2014-90-eu]

# Exclusion or concurrency with CRA

Under CRA Article 2(3), the CRA does not apply to products with digital elements covered by Directive 2014/90/EU. The exclusion is total for wheel-marked marine equipment.[^cra-art-2]

**Boundary condition:** Digital equipment used on recreational craft, private yachts, or small vessels that are not covered by international conventions (e.g. consumer chartplotters, handheld marine radios, or fishfinders subject to the Recreational Craft Directive 2013/53/EU or RED) remain within the scope of the CRA.[^cra-art-2]

# Technical or procedural satisfaction of CRA elements

Marine equipment cybersecurity is assured through dedicated maritime international testing standards:[^dir-2014-90-eu]
1. **Testing standards:** Implementing regulations under the MED incorporate IEC/ISO standards that include cybersecurity criteria, such as **IEC 61162-460** (Digital interfaces: Ethernet interconnections with cybersecurity provisions) and **IEC 62923** (Bridge alert management).[^dir-2014-90-eu]
2. **Conformity assessment & wheel mark:** Assessed under MED modules (B+D, B+E, B+F, or G) by MED notified bodies, leading to the wheel mark rather than the CRA CE mark.[^dir-2014-90-eu]
3. **Operational integration:** Coordinated with shipowner Safety Management Systems (SMS) audited under the International Safety Management (ISM) Code.[^dir-2014-90-eu]

# Relevant provisions

- **Directive 2014/90/EU:** Article 3 (Scope), Article 9 & 10 (Wheel mark and conformity assessment), Article 35 (Implementing acts for technical standards).[^dir-2014-90-eu]
- **Regulation (EU) 2024/2847:** Article 2(3) (Exclusion of marine equipment), Recital 22.[^cra-art-2]

# Dates and transition

- Directive 2014/90/EU entered into force on 17 September 2014 and applied from 18 September 2016.[^dir-2014-90-eu]
- The CRA Article 2(3) exclusion applies from CRA entry into force.[^cra-art-2]

# Related concepts

- [Scope & Exclusions Overview](../../../../obligations/scope/exclusions.md)
- [CRA Article 2: Scope](../../cra/articles/article-2.md)

[^dir-2014-90-eu]: Directive 2014/90/EU, http://data.europa.eu/eli/dir/2014/90/oj/eng
[^cra-art-2]: Regulation (EU) 2024/2847, Article 2, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
