---
type: Standard
title: "EUCC: European Cybersecurity Certification Scheme on Common Criteria"
description: Official European cybersecurity certification scheme adopted under Regulation (EU) 2019/881 relevant for CRA conformity of high-assurance products.
category: standard
tags: [cra, standard, certification-scheme, eucc, common-criteria, csa]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: reg-2024-482
    resource: http://data.europa.eu/eli/reg_impl/2024/482/oj/eng
    title: Commission Implementing Regulation (EU) 2024/482 adopting EUCC scheme
    author: European Commission
    last_modified: 2024-01-31T00:00:00Z
  - id: cra-art-27-8
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_27
    title: Regulation (EU) 2024/2847, Article 27(8) (Presumption from European cybersecurity schemes)
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
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

The European Common Criteria-based cybersecurity certification scheme (EUCC) was established under the Cybersecurity Act (Regulation (EU) 2019/881) by Commission Implementing Regulation (EU) 2024/482[^reg-2024-482]. Under CRA Article 27(8)[^cra-art-27-8], the Commission is empowered to specify by implementing act when EUCC certificates confer presumption of conformity with CRA Annex I essential requirements.

# Legal effect

At present, an EUCC certificate does **not** automatically confer presumption of conformity with Regulation (EU) 2024/2847 until the European Commission adopts an implementing act under Article 27(8) explicitly recognizing EUCC certificates or European cybersecurity statements of conformity.

# Applicability

Applies to ICT products requiring substantial or high evaluation assurance levels (AVA_VAN.1 to AVA_VAN.5), including:
- Smartcards, secure elements, and cryptographic embedded chips (M/606 Line 41);
- Hardware security modules (HSMs) and secure execution environments (M/606 Line 39);
- Network appliances and smart meter gateways (M/606 Line 40).

# Related concepts

- `standards/committees/clc-tc-47x`
- `standards/committees/cen-tc-224`
- `standards/m606/line-41`
- `standards/process/how-cra-standards-are-built`

[^reg-2024-482]: Commission Implementing Regulation (EU) 2024/482. http://data.europa.eu/eli/reg_impl/2024/482/oj/eng
[^cra-art-27-8]: Regulation (EU) 2024/2847, Article 27(8). http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_27
