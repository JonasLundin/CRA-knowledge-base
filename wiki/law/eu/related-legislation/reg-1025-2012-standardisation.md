---
type: Legal Instrument
title: Regulation (EU) No 1025/2012 (European Standardisation Framework)
description: Legal framework governing standardisation requests, harmonised European standards development, and presumption of conformity under the Cyber Resilience Act.
category: law
tags: [cra, standardisation, harmonised-standards, m606, presumption-of-conformity]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-08-21T00:00:00Z
sources:
  - id: reg-1025-2012
    resource: http://data.europa.eu/eli/reg/2012/1025/oj/eng
    title: Regulation (EU) No 1025/2012 on European standardisation
    author: European Parliament and Council
    last_modified: 2012-11-14T00:00:00Z
  - id: cra-art-27
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_27
    title: Regulation (EU) 2024/2847, Article 27
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: m606-decision
    resource: https://ec.europa.eu/transparency/documents-register/detail?ref=C(2025)618&lang=en
    title: Commission Implementing Decision C(2025) 618 (Standardisation Request M/606)
    author: European Commission
    last_modified: 2025-02-14T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  celex: 32012R1025
  eli: http://data.europa.eu/eli/reg/2012/1025/oj/eng
  relevant_cra_provisions:
    - Article 27
    - Recital 54
    - Recital 55
    - Recital 56
    - Recital 57
  applicability: procedural_enabling_framework
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) No 1025/2012 establishes the horizontal legal framework for European standardisation, governing how the European Commission requests European Standardisation Organisations (ESOs: CEN, CENELEC, ETSI) to draft harmonised European standards and how references to such standards are evaluated and published in the Official Journal of the European Union (OJEU).[^reg-1025-2012] Under the Cyber Resilience Act (CRA), this framework provides the legal mechanism for creating harmonised standards that confer a presumption of conformity with CRA Annex I essential requirements.[^cra-art-27]

# Interaction and scope relationship

The relationship between Regulation (EU) No 1025/2012 and Regulation (EU) 2024/2847 is procedural and complementary. Regulation (EU) No 1025/2012 does not impose direct cybersecurity technical requirements on products; rather, it regulates the institutional procedure through which voluntary technical specifications become harmonised standards with legal effect under Union harmonisation law.[^reg-1025-2012]

# When the instrument applies

Regulation (EU) No 1025/2012 applies across the Union whenever:
- The Commission issues a formal standardisation request (mandate) to CEN, CENELEC, or ETSI pursuant to Article 10;[^reg-1025-2012]
- ESOs draft, consult on, and adopt European standards (EN) or European standardisation deliverables;[^reg-1025-2012]
- The Commission assesses whether ESO deliverables comply with the initial standardisation request and decides on publication or restriction of citations in the OJEU pursuant to Article 10(6);[^reg-1025-2012]
- Formal objections to harmonised standards are raised by Member States or the European Parliament pursuant to Article 11.[^reg-1025-2012]

# Exclusion or concurrency with CRA

The two instruments operate concurrently. Regulation (EU) No 1025/2012 does not exclude or limit the scope of the CRA, nor does CRA exclude Regulation (EU) No 1025/2012. Instead, CRA Article 27 explicitly invokes Regulation (EU) No 1025/2012 as the statutory procedure for developing and citing CRA harmonised standards.[^cra-art-27]

# Technical or procedural satisfaction of CRA elements

Under CRA Article 27(1), products with digital elements and vulnerability handling processes that conform to harmonised standards (or parts thereof) whose references have been published in the OJEU in accordance with Regulation (EU) No 1025/2012 are presumed to conform to the essential requirements set out in CRA Annex I covered by those standards.[^cra-art-27]

Key operational connections:
1. **Standardisation Request M/606:** The Commission adopted Implementing Decision C(2025) 618 under Article 10 of Regulation (EU) No 1025/2012, formally requesting CEN, CENELEC, and ETSI to develop horizontal and product-specific harmonised standards supporting CRA Annex I.[^m606-decision]
2. **Presumption of conformity boundary:** Presumption of conformity arises strictly from OJEU citation under Regulation (EU) No 1025/2012. Draft standards, un-cited published standards, or proprietary specifications do not confer presumption of conformity under Article 27.[^cra-art-27]
3. **Formal objection mechanism:** If a cited standard is deemed technically inadequate or incomplete in covering CRA essential requirements, Member States or the European Parliament may trigger the objection procedure under Article 11 of Regulation (EU) No 1025/2012, leading to withdrawal or limitation of the OJEU citation.[^reg-1025-2012]

# Relevant provisions

- **Regulation (EU) No 1025/2012:** Article 10 (Standardisation requests to European standardisation organisations), Article 11 (Formal objections to harmonised standards).[^reg-1025-2012]
- **Regulation (EU) 2024/2847:** Article 27(1)–(4) (Presumption of conformity via harmonised standards), Recitals 54–57 (Standardisation process and common specifications fallback).[^cra-art-27]
- **Commission Implementing Decision C(2025) 618:** Standardisation Request M/606 to CEN, CENELEC, and ETSI.[^m606-decision]

# Dates and transition

- Regulation (EU) No 1025/2012 entered into force on 1 January 2013 and is fully in force.[^reg-1025-2012]
- Standardisation Request M/606 sets delivery milestones for ESOs between 2025 and 2027 to ensure harmonised standards are available ahead of full CRA application on 11 December 2027.[^m606-decision]

# Related concepts

- [How CRA Standards Are Built](../../../standards/process/how-cra-standards-are-built.md)
- [CRA Article 27: Presumption of Conformity](../cra/articles/article-27.md)

[^reg-1025-2012]: Regulation (EU) No 1025/2012, http://data.europa.eu/eli/reg/2012/1025/oj/eng
[^cra-art-27]: Regulation (EU) 2024/2847, Article 27, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_27
[^m606-decision]: Commission Implementing Decision C(2025) 618, https://ec.europa.eu/transparency/documents-register/detail?ref=C(2025)618&lang=en
