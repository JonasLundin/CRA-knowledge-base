---
type: Legal Instrument
title: Directive 2014/53/EU (Radio Equipment Directive)
description: Union harmonisation directive for radio equipment amended by CRA Article 68 to transition radio cybersecurity requirements into the Cyber Resilience Act framework.
category: law
tags: [cra, red, radio-equipment, article-68, spectrum, transition]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-08-21T00:00:00Z
sources:
  - id: dir-2014-53-eu
    resource: http://data.europa.eu/eli/dir/2014/53/oj/eng
    title: Directive 2014/53/EU on the harmonisation of the laws of the Member States relating to the making available on the market of radio equipment (RED)
    author: European Parliament and Council
    last_modified: 2014-05-22T00:00:00Z
  - id: cra-art-68
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_68
    title: Regulation (EU) 2024/2847, Article 68
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  celex: 32014L0053
  eli: http://data.europa.eu/eli/dir/2014/53/oj/eng
  relevant_cra_provisions:
    - Article 68
    - Recital 34
    - Recital 35
    - Recital 36
  applicability: concurrent_with_cyber_exclusion_amendment
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Directive 2014/53/EU (Radio Equipment Directive / RED) establishes the regulatory framework for placing radio equipment on the EU market, covering health and electrical safety (Article 3(1)(a)), electromagnetic compatibility (Article 3(1)(b)), effective and efficient use of radio spectrum (Article 3(2)), and specific delegated essential requirements (Article 3(3)).[^dir-2014-53-eu] CRA Article 68 directly amends RED Article 3(3) to carve out products with digital elements from RED delegated cybersecurity acts, establishing CRA as the single horizontal cybersecurity regime for connected radio devices.[^cra-art-68]

# Interaction and scope relationship

The relationship between RED and the CRA is one of concurrent application with a targeted sectoral handover of cybersecurity competence:
- **Radio-specific aspects:** Radio equipment with digital elements (such as Wi-Fi routers, Bluetooth peripherals, smartphones, and IoT gateways) remains fully subject to Directive 2014/53/EU for radio spectrum efficiency (Article 3(2)), EMC (Article 3(1)(b)), and electrical safety (Article 3(1)(a)).[^dir-2014-53-eu]
- **Cybersecurity aspects:** Essential requirements concerning network protection (Article 3(3)(d)), personal data/privacy protection (Article 3(3)(e)), and protection from fraud (Article 3(3)(f)) are transferred exclusively to the CRA for products within CRA scope.[^cra-art-68]

# When the instrument applies

Directive 2014/53/EU applies whenever:
- An electrical or electronic product intentionally emits and/or receives radio waves for radio communication and/or radiodetermination;[^dir-2014-53-eu]
- The manufacturer assesses compliance with health, safety, EMC, and radio spectrum efficiency requirements;[^dir-2014-53-eu]
- The product is CE-marked and accompanied by an EU declaration of conformity referencing Directive 2014/53/EU.[^dir-2014-53-eu]

# Exclusion or concurrency with CRA

Under CRA Article 68, Directive 2014/53/EU Article 3(3) is amended by adding the following rule:[^cra-art-68]
- Products with digital elements within the scope of Regulation (EU) 2024/2847 are **excluded from the scope of delegated acts** adopted pursuant to Article 3(3), points (d), (e), and (f) of Directive 2014/53/EU.[^cra-art-68]
- Consequently, radio products subject to CRA do not need to demonstrate compliance with RED delegated cybersecurity acts once CRA applies, avoiding dual certification.[^cra-art-68]

# Technical or procedural satisfaction of CRA elements

1. **Dual EU declaration of conformity:** For connected radio equipment, the manufacturer prepares a single EU declaration of conformity (or consolidated technical dossier) citing Directive 2014/53/EU for spectrum/safety/EMC and Regulation (EU) 2024/2847 for essential cybersecurity requirements.[^dir-2014-53-eu][^cra-art-68]
2. **Transition from RED Delegated Regulation (EU) 2022/30:** Prior to full CRA application, certain connected radio devices were regulated under Delegated Regulation (EU) 2022/30 (supported by standard family EN 18031). When CRA becomes fully applicable on 11 December 2027, CRA Annex I supersedes Delegated Regulation (EU) 2022/30 for products within CRA scope.[^cra-art-68]

# Relevant provisions

- **Directive 2014/53/EU:** Article 3(1) (Health, safety, and EMC), Article 3(2) (Radio spectrum), Article 3(3)(d)–(f) (Delegated cybersecurity, privacy, and anti-fraud requirements).[^dir-2014-53-eu]
- **Regulation (EU) 2024/2847:** Article 68 (Amendments to Directive 2014/53/EU), Recitals 34–36.[^cra-art-68]

# Dates and transition

- Directive 2014/53/EU entered into force on 11 June 2014 and applied from 13 June 2016.[^dir-2014-53-eu]
- CRA Article 68 amendment takes effect on 11 December 2027, formally phasing out the RED delegated cybersecurity regime in favour of the CRA.[^cra-art-68]

# Related concepts

- [Commission Delegated Regulation (EU) 2022/30 (RED Cybersecurity & EN 18031)](reg-2022-30-red-cybersecurity.md)
- [Scope & Exclusions Overview](../../../obligations/scope/index.md)
- [CRA Article 68: Amendments to Directive 2014/53/EU](../cra/articles/article-68.md)

[^dir-2014-53-eu]: Directive 2014/53/EU, http://data.europa.eu/eli/dir/2014/53/oj/eng
[^cra-art-68]: Regulation (EU) 2024/2847, Article 68, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_68
