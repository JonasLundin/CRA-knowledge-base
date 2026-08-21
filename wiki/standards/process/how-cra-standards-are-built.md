---
type: Procedure
title: How CRA Standards Are Built
description: Standardisation lifecycle for Cyber Resilience Act harmonised standards from standardisation request M/606 to OJEU citation.
category: standard
tags: [cra, standards, standardisation-process, m606, ojeu, etsi, cen, cenelec]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: m606
    resource: https://ec.europa.eu/transparency/documents-register/detail?ref=C(2025)618&lang=en
    title: Commission Implementing Decision C(2025) 618 on standardisation request M/606
    author: European Commission
    last_modified: 2025-01-31T00:00:00Z
  - id: cra-art-27
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_27
    title: Regulation (EU) 2024/2847, Article 27 (Presumption of conformity)
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: reg-1025-2012
    resource: http://data.europa.eu/eli/reg/2012/1025/oj/eng
    title: Regulation (EU) No 1025/2012 on European standardisation
    author: European Parliament and Council
    last_modified: 2012-10-25T00:00:00Z
  - id: cyberstand-process
    resource: https://cyberstand.eu/how-cra-standards-are-built
    title: How CRA Standards are built
    author: CYBERSTAND.eu
    last_modified: 2026-01-15T00:00:00Z
  - id: stan4cra-work
    resource: https://www.stan4cra.eu/technicalwork
    title: CRA Standardisation Technical Work
    author: STAN4CR
    last_modified: 2026-06-01T00:00:00Z
x-cra:
  process_type: standardisation_lifecycle
  mandate: M/606
  controlling_law: Regulation (EU) No 1025/2012
  presumption_basis: Regulation (EU) 2024/2847 Article 27
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

The standardisation lifecycle for the Cyber Resilience Act (CRA, Regulation (EU) 2024/2847) follows the legal framework of Regulation (EU) No 1025/2012[^reg-1025-2012]. The European Commission issues a standardisation request (Mandate M/606 / Decision C(2025) 618)[^m606] to the European Standardisation Organisations (ESOs: CEN, CENELEC, and ETSI). The work is structured into horizontal and vertical streams that progress through drafting, public enquiry, formal approval, Commission compliance assessment, and publication of citations in the Official Journal of the European Union (OJEU)[^cra-art-27].

# Legal effect

Harmonised standards remain voluntary. Manufacturers may choose alternative technical specifications to meet the CRA essential requirements set out in Annex I. However, conformity with harmonised standards whose references have been cited in the OJEU confers a legal presumption of conformity with the corresponding essential requirements under CRA Article 27[^cra-art-27].

Draft standards, committee work items, and published European Standards (EN) that have not been cited in the OJEU do not confer presumption of conformity.

# Standardisation architecture

Standardisation under M/606 is partitioned into two complementary tiers[^cyberstand-process][^stan4cra-work]:

## Horizontal standards (M/606 Lines 1–15)
Horizontal deliverables are product-agnostic and framework-oriented. Developed primarily within CEN-CLC/JTC 13 WG 9 (the EN 40000 family), they define baseline cybersecurity principles, generic engineering requirements across all Annex I Part I essential requirements (Lines 1–14), and vulnerability handling processes under Annex I Part II (Line 15).

## Vertical standards (M/606 Lines 16–41)
Vertical deliverables address specific product categories listed in CRA Annex III (Important products Class I and II) and Annex IV (Critical products). They translate horizontal security concepts into sector-specific requirements and attack-potential baselines. Work is distributed across:
- **ETSI TC CYBER / EUSR**: Software and connected device verticals (EN 304 series: browsers, password managers, OS, routers, IoT, virtualisation, firewalls);
- **CEN-CLC/JTC 13 (WG 6)**: Smart meter gateways (Line 40) and sector risk assessment;
- **CEN/TC 224 (WG 17)**: Identity and privileged access management (Line 16), hardware security boxes (Line 39), and smartcards/secure elements (Line 41);
- **CLC/TC 47X**: Microprocessors, microcontrollers, and trusted chip platforms (Lines 28, 29, 37, 38, 41);
- **CLC/TC 65X (WG 3)**: Industrial-process measurement, control, and automation systems (OT overlays for Lines 20–22, 25, 27, 36).

# Lifecycle stages

```text
[M/606 Request]
      │
      ▼
[Technical Committee Drafting]
      │
      ▼
[Public Enquiry / Open Consultation]
      │
      ▼
[Comment Resolution & ESO Approval / Formal Vote]
      │
      ▼
[Harmonised Standard (EN) Delivery]
      │
      ▼
[EC Compliance Assessment (HAS)]
      │
      ▼
[OJEU Citation Publication] ──► Presumption of Conformity (CRA Art. 27)
```

1. **Standardisation Request (M/606)**: The Commission adopts an implementing decision establishing the work scope, list of deliverables, and delivery deadlines[^m606].
2. **Technical Drafting**: Joint Working Groups and Technical Committees draft European Standards (prEN / EN) aligned with CRA Annex I essential requirements.
3. **Public Enquiry / Open Consultation**: Drafts (e.g., EN 304 series enquiry drafts in ETSI Open Area) are released for public commenting by industry, open-source communities, civil society, and national standardisation bodies.
4. **ESO Formal Approval**: National standardisation delegations and ESO members vote on final draft text.
5. **Commission Assessment**: Harmonised Standard (HAS) consultants and the European Commission assess deliverable conformity with M/606 and CRA requirements.
6. **OJEU Citation**: The Commission publishes the reference of the harmonised standard in the Official Journal (C series), with or without restrictions. Presumption of conformity takes effect on the date of OJEU publication.

# Dates and transitions

- **2025-01-31**: Commission Implementing Decision C(2025) 618 adopting Standardisation Request M/606[^m606].
- **2026-08-21**: ETSI public enquiry baseline active for 17 vertical EN 304 series drafts.
- **2026-09-11**: CRA Article 14 vulnerability reporting obligations take effect.
- **2027-12-11**: Full application of Regulation (EU) 2024/2847 and complete entry into force of essential requirements.

# Related concepts

- `standards/committees/cen-clc-jtc-13`
- `standards/committees/etsi-tc-cyber-eusr`
- `standards/committees/cen-tc-224`
- `standards/committees/clc-tc-47x`
- `standards/committees/clc-tc-65x`
- `standards/m606/index`
- `standards/harmonised/index`

[^m606]: Commission Implementing Decision C(2025) 618 on standardisation request M/606. https://ec.europa.eu/transparency/documents-register/detail?ref=C(2025)618&lang=en
[^cra-art-27]: Regulation (EU) 2024/2847, Article 27. http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_27
[^reg-1025-2012]: Regulation (EU) No 1025/2012 on European standardisation. http://data.europa.eu/eli/reg/2012/1025/oj/eng
[^cyberstand-process]: CYBERSTAND.eu. How CRA Standards are built. https://cyberstand.eu/how-cra-standards-are-built
[^stan4cra-work]: STAN4CR. CRA Standardisation Technical Work. https://www.stan4cra.eu/technicalwork
