---
type: Standard
title: "EUCC: European Cybersecurity Certification Scheme on Common Criteria"
description: Official European cybersecurity certification scheme adopted under Regulation (EU) 2019/881 relevant for CRA conformity of high-assurance products.
category: standard
tags: [cra, standard, certification-scheme, eucc, common-criteria, csa]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-05-18T00:00:00Z
sources:
  - id: reg-2024-482
    resource: http://data.europa.eu/eli/reg_impl/2024/482/oj/eng
    title: Commission Implementing Regulation (EU) 2024/482 adopting EUCC scheme
    author: European Commission
    last_modified: 2024-01-31T00:00:00Z
  - id: reg-2024-3144
    resource: http://data.europa.eu/eli/reg_impl/2024/3144/oj/eng
    title: Commission Implementing Regulation (EU) 2024/3144 amending Implementing Regulation (EU) 2024/482 as regards applicable international standards and correcting that Implementing Regulation
    author: European Commission
    last_modified: 2024-12-18T00:00:00Z
  - id: reg-2025-2462
    resource: http://data.europa.eu/eli/reg_impl/2025/2462/oj/eng
    title: Commission Implementing Regulation (EU) 2025/2462 amending Implementing Regulation (EU) 2024/482 as regards the definition and rules for certification of a product series, the definitions of minor and major changes and the state-of-the-art documents in Annexes I, II and III
    author: European Commission
    last_modified: 2025-12-08T00:00:00Z
  - id: cra-art-27-8
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_27
    title: Regulation (EU) 2024/2847, Article 27(8)-(9) (Presumption from European cybersecurity schemes)
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  standard_number: EUCC (Regulation (EU) 2024/482)
  standards_body: ENISA / European Commission
  m606_entries: [41]
  standard_status: published
  ojeu_cited: false
  ojeu_reference: null
  presumption_of_conformity: false
  covers:
    - CRA Annex I
    - CRA Annex III Class II
    - CRA Annex IV
  access: open
  copyright: third-party
  checked_at: 2026-11-18T00:00:00Z
---

# Summary

The European Common Criteria-based cybersecurity certification scheme (EUCC) was established under the Cybersecurity Act (Regulation (EU) 2019/881) by Commission Implementing Regulation (EU) 2024/482[^reg-2024-482], and subsequently amended by Commission Implementing Regulation (EU) 2024/3144[^reg-2024-3144] (updating applicable international standards and transitional provisions) and Commission Implementing Regulation (EU) 2025/2462[^reg-2025-2462] (establishing rules for certification of a "product series", defining "minor and major changes" for assurance continuity, and updating state-of-the-art annexes). Under CRA Article 27(8) and (9)[^cra-art-27-8], the Commission is empowered to specify by **delegated act** (in accordance with Article 61) when EUCC certificates confer a presumption of conformity with CRA Annex I essential requirements.

# Legal effect

At present, an EUCC certificate does **not** automatically confer a blanket presumption of conformity with Regulation (EU) 2024/2847 until the European Commission adopts a **delegated act** under Article 27(9) explicitly specifying the coverage of EUCC certificates or European cybersecurity statements of conformity against Annex I. However, under CRA Article 32(3) and (4), where an EUCC certificate at assurance level 'substantial' or 'high' has been issued for an Important (Class I or Class II) or Critical product, it satisfies the third-party conformity assessment requirement for the covered essential requirements.

# Applicability

Applies to ICT products and product series requiring substantial or high evaluation assurance levels (AVA_VAN.1 to AVA_VAN.5), including:
- Smartcards, secure elements, and cryptographic embedded chips (M/606 Line 41);
- Hardware security modules (HSMs) and secure execution environments (M/606 Line 39);
- Network appliances and smart meter gateways (M/606 Line 40).

# Related concepts

- `standards/committees/clc-tc-47x`
- `standards/committees/cen-tc-224`
- `standards/m606/line-41`
- `standards/process/how-cra-standards-are-built`

[^reg-2024-482]: Commission Implementing Regulation (EU) 2024/482. http://data.europa.eu/eli/reg_impl/2024/482/oj/eng
[^reg-2024-3144]: Commission Implementing Regulation (EU) 2024/3144. http://data.europa.eu/eli/reg_impl/2024/3144/oj/eng
[^reg-2025-2462]: Commission Implementing Regulation (EU) 2025/2462. http://data.europa.eu/eli/reg_impl/2025/2462/oj/eng
[^cra-art-27-8]: Regulation (EU) 2024/2847, Article 27(8)-(9). http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_27
