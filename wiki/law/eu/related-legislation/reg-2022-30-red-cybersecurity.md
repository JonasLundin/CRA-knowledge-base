---
type: Legal Instrument
title: Commission Delegated Regulation (EU) 2022/30 (RED Cybersecurity and EN 18031)
description: Transitional delegated act activating cybersecurity requirements for connected radio equipment under the Radio Equipment Directive and its interaction with the Cyber Resilience Act.
category: law
tags: [cra, red, delegated-regulation-2022-30, en-18031, iot-security, transition]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-08-21T00:00:00Z
sources:
  - id: reg-2022-30
    resource: http://data.europa.eu/eli/reg_del/2022/30/oj/eng
    title: Commission Delegated Regulation (EU) 2022/30 on the application of essential requirements in Article 3(3)(d), (e) and (f) of Directive 2014/53/EU
    author: European Commission
    last_modified: 2022-01-12T00:00:00Z
  - id: reg-2023-2444
    resource: http://data.europa.eu/eli/reg_del/2023/2444/oj/eng
    title: Commission Delegated Regulation (EU) 2023/2444 amending Delegated Regulation (EU) 2022/30 as regards the date of application
    author: European Commission
    last_modified: 2023-11-06T00:00:00Z
  - id: cra-art-68
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_68
    title: Regulation (EU) 2024/2847, Article 68
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  celex: 32022R0030
  eli: http://data.europa.eu/eli/reg_del/2022/30/oj/eng
  relevant_cra_provisions:
    - Article 68
    - Recital 34
    - Recital 35
    - Recital 36
  applicability: transitional_regime_superseded_by_cra
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Commission Delegated Regulation (EU) 2022/30 supplements Directive 2014/53/EU (RED) by activating essential requirements for network protection (Article 3(3)(d)), personal data and privacy protection (Article 3(3)(e)), and protection from monetary fraud (Article 3(3)(f)) for connected radio equipment, wearable devices, and smart toys.[^reg-2022-30] It serves as the interim regulatory regime for wireless IoT cybersecurity until full application of the Cyber Resilience Act on 11 December 2027, when CRA Article 68 excludes CRA products from RED delegated cybersecurity acts.[^reg-2023-2444][^cra-art-68]

# Interaction and scope relationship

The relationship between Delegated Regulation (EU) 2022/30 and the CRA is transitional and chronological:
- **Phase 1 (1 August 2025 to 10 December 2027):** Manufacturers of connected radio equipment falling under Delegated Regulation (EU) 2022/30 must meet the RED Article 3(3)(d)/(e)/(f) essential requirements.[^reg-2023-2444]
- **Phase 2 (From 11 December 2027 onward):** CRA Article 68 enters into force and amends RED Article 3(3) to exclude products with digital elements within CRA scope. From that date, CRA Annex I essential requirements completely supersede Delegated Regulation (EU) 2022/30 for products within CRA scope.[^cra-art-68]

# When the instrument applies

Delegated Regulation (EU) 2022/30 applies from 1 August 2025 to:
- Internet-connected radio equipment capable of communicating over the internet (Article 3(3)(d));[^reg-2022-30]
- Radio equipment capable of processing personal data, child-care radio equipment, toys with radio functionality, and wearable radio equipment (Article 3(3)(e));[^reg-2022-30]
- Radio equipment enabling the holder or user to transfer money or monetary value (Article 3(3)(f)).[^reg-2022-30]

# Exclusion or concurrency with CRA

Under CRA Article 68 and Recital 36, the coexistence of two parallel cybersecurity regimes for the same products is explicitly prevented. Once the CRA applies on 11 December 2027, products with digital elements are legally carved out of the RED delegated acts.[^cra-art-68]

# Technical or procedural satisfaction of CRA elements

1. **Role of EN 18031 harmonised standards:** Under standardisation request M/585, CEN and CENELEC developed the EN 18031 standard family:
   - **EN 18031-1:** Internet-connected radio equipment (RED Article 3(3)(d));
   - **EN 18031-2:** Radio equipment processing personal data and toys/wearables (RED Article 3(3)(e));
   - **EN 18031-3:** Radio equipment processing virtual money/monetary value (RED Article 3(3)(f)).
2. **Bridge to CRA Annex I:** While technical specifications implemented to satisfy EN 18031 provide strong technical maturity towards CRA baseline security, EN 18031 **does not automatically grant presumption of conformity under the CRA**.[^cra-art-68] CRA presumption of conformity requires compliance with harmonised standards developed specifically under Standardisation Request M/606 (e.g., the prEN 40000 family) and cited in the OJEU under CRA Article 27.[^cra-art-68]
3. **Vulnerability handling and lifecycle:** Delegated Regulation (EU) 2022/30 focuses on product security at the time of placing on the market, whereas CRA expands obligations across the entire expected product support period, including mandatory vulnerability reporting under CRA Article 14 and software update delivery.[^cra-art-68]

# Relevant provisions

- **Delegated Regulation (EU) 2022/30:** Articles 1–3 (Scope, product categories, and essential requirements).[^reg-2022-30]
- **Delegated Regulation (EU) 2023/2444:** Article 1 (Postponement of application date to 1 August 2025).[^reg-2023-2444]
- **Regulation (EU) 2024/2847:** Article 68 (Amendments to Directive 2014/53/EU), Recitals 34–36.[^cra-art-68]

# Dates and transition

- Adopted on 29 October 2021; date of application postponed to 1 August 2025 by Delegated Regulation (EU) 2023/2444.[^reg-2022-30][^reg-2023-2444]
- Displaced / superseded by CRA Annex I on 11 December 2027 for all products within CRA scope.[^cra-art-68]

# Related concepts

- [Directive 2014/53/EU (Radio Equipment Directive)](dir-2014-53-eu-radio-equipment.md)
- [How CRA Standards Are Built](../../../standards/process/how-cra-standards-are-built.md)
- [CRA Article 68: Amendments to Directive 2014/53/EU](../cra/articles/article-68.md)

[^reg-2022-30]: Commission Delegated Regulation (EU) 2022/30, http://data.europa.eu/eli/reg_del/2022/30/oj/eng
[^reg-2023-2444]: Commission Delegated Regulation (EU) 2023/2444, http://data.europa.eu/eli/reg_del/2023/2444/oj/eng
[^cra-art-68]: Regulation (EU) 2024/2847, Article 68, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_68
