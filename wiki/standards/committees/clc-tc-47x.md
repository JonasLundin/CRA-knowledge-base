---
type: Authority
title: CLC/TC 47X
description: CENELEC Technical Committee 47X Semiconductors and Trusted Chips Implementation developing CRA standards for microprocessors, MCUs, ASICs, and secure element platforms.
category: standard
tags: [cra, cenelec, clc-tc47x, semiconductors, microcontrollers, trusted-chips, secure-elements, m606]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-05-18T00:00:00Z
sources:
  - id: clc-tc47x
    resource: https://www.cenelec.eu/dyn/www/f?p=104:7:0::::FSP_ORG_ID:2417743
    title: CLC/TC 47X Semiconductor devices and trusted chips
    author: CENELEC
    last_modified: 2026-06-01T00:00:00Z
  - id: stan4cra-clc47x
    resource: https://www.stan4cra.eu/clctc47x
    title: CLC TC 47X Technical Work
    author: STAN4CR
    last_modified: 2026-06-01T00:00:00Z
  - id: m606
    resource: https://ec.europa.eu/transparency/documents-register/detail?ref=C(2025)618&lang=en
    title: Commission Implementing Decision C(2025) 618 (Mandate M/606)
    author: European Commission
    last_modified: 2025-01-31T00:00:00Z
x-cra:
  committee_name: CLC/TC 47X
  standards_body: CENELEC
  mandate_lines: [28, 29, 37, 38, 41]
  working_groups:
    - WG 1: MCUs/MPUs with security functionalities (tamper resistance / third-party assessment)
    - WG 2: MCUs/MPUs without tamper-resistance claims (self-assessment / SESIP)
    - WG 3: SmartCards and Secure Element Platforms (EUCC / Protection Profiles)
  checked_at: 2026-11-18T00:00:00Z
---

# Summary

CENELEC Technical Committee 47X (Semiconductor devices and trusted chips)[^clc-tc47x][^stan4cra-clc47x] develops harmonised standards for microprocessors, microcontrollers, embedded security components, and semiconductor platforms under Standardisation Request M/606[^m606].

# Legal effect

Deliverables and technical drafts developed by CLC/TC 47X do not confer presumption of conformity under CRA Article 27 until formal European Standard (EN) adoption and citation in the Official Journal of the European Union (OJEU).

# Working group responsibilities

## WG 1 & WG 2: Microprocessors and microcontrollers with security-related functionalities and tamper resistance
Defines vertical European Standards enabling conformity assessment for general-purpose security-enabled microcontrollers (MCUs), microprocessors (MPUs), ASICs, and FPGAs (`prEN 50765:2026`, initially drafted as `prEN 40001-3:2026`) as well as tamper-resistant microprocessors and microcontrollers (`prEN 50766:2026`, initially drafted as `prEN 40002-3:2026`, integrating JIL attack-potential resistance and SESIP/Common Criteria evaluation methodologies).

## WG 3: SmartCards and Secure Element Platforms
Develops `prEN 50764:2026` (*Cybersecurity requirements for platforms of smartcards and similar devices including secure elements*, initially drafted as `prEN 40003-3:2026`), focusing on the harmonisation of Common Criteria Protection Profiles (e.g. Eurosmart Secure IC PP-0084, Java Card PP-0099, TCG TPM PP-0101) with CRA Annex I essential requirements and vulnerability handling duties to support EUCC-certified platforms.

# M/606 work allocation and 2026 deliverables

- **Lines 28 & 29 (`prEN 50765:2026`)**: *Cybersecurity requirements for microprocessors and microcontrollers with security-related functionalities* — covering microprocessors, microcontrollers, ASICs, and FPGAs with security-related functionalities (CRA Annex III Class I points 13 & 14).
- **Lines 37 & 38 (`prEN 50766:2026`)**: *Cybersecurity requirements for tamper-resistant microprocessors and microcontrollers* — covering tamper-resistant microprocessors and microcontrollers (CRA Annex III Class II points 3 & 4).
- **Line 41 (`prEN 50764:2026`)**: *Cybersecurity requirements for platforms of smartcards and similar devices including secure elements* — covering cyber resilience of platforms of smartcards and secure elements (CRA Annex III Class II point 6 / Annex IV point 1, complementing CEN/TC 224 application-layer draft `prEN 18330`).

# Related concepts

- `standards/process/how-cra-standards-are-built`
- `standards/committees/cen-tc-224`
- `standards/certification-schemes/eucc`
- `standards/m606/line-28`
- `standards/m606/line-29`
- `standards/m606/line-37`
- `standards/m606/line-38`
- `standards/m606/line-41`

[^clc-tc47x]: CENELEC TC 47X. https://www.cenelec.eu/dyn/www/f?p=104:7:0::::FSP_ORG_ID:2417743
[^stan4cra-clc47x]: STAN4CR. CLC TC 47X Technical Work. https://www.stan4cra.eu/clctc47x
[^m606]: Commission Implementing Decision C(2025) 618. https://ec.europa.eu/transparency/documents-register/detail?ref=C(2025)618&lang=en
