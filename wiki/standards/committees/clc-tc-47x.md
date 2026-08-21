---
type: Authority
title: CLC/TC 47X
description: CENELEC Technical Committee 47X Semiconductors and Trusted Chips Implementation developing CRA standards for microprocessors, MCUs, ASICs, and secure element platforms.
category: standard
tags: [cra, cenelec, clc-tc47x, semiconductors, microcontrollers, trusted-chips, secure-elements, m606]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
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
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

CENELEC Technical Committee 47X (Semiconductor devices and trusted chips)[^clc-tc47x][^stan4cra-clc47x] develops harmonised standards for microprocessors, microcontrollers, embedded security components, and semiconductor platforms under Standardisation Request M/606[^m606].

# Legal effect

Deliverables and technical drafts developed by CLC/TC 47X do not confer presumption of conformity under CRA Article 27 until formal European Standard (EN) adoption and citation in the Official Journal of the European Union (OJEU).

# Working group responsibilities

## WG 1: Microprocessors and microcontrollers with security-related functionalities
Defines standards enabling third-party assessment for microcontrollers (MCUs) and microprocessors (MPUs) claiming tamper resistance (JIL basic/enhanced basic potential of attack). Integrates with evaluation methodologies such as SESIP.

## WG 2: Tamper-resistant Microprocessors and Microcontrollers
Focuses on standards enabling conformity assessment for MCUs/MPUs providing security functions without tamper-resistance claims, establishing baseline hardware security requirements.

## WG 3: SmartCards and Secure Element Platforms
Focuses on the harmonisation of Common Criteria Protection Profiles (PPs) (e.g. Eurosmart Secure IC PP 0084, Java Card PP 0099, TCG TPM PP 0101) with CRA Annex I essential requirements and incident reporting duties, supporting EUCC-certified platforms.

# M/606 work allocation

- **Lines 28 & 29**: Microprocessors, microcontrollers, ASICs, and FPGAs with security-related functionalities (CRA Annex III Class I points 13 & 14).
- **Lines 37 & 38**: Tamper-resistant microprocessors and microcontrollers (CRA Annex III Class II points 3 & 4).
- **Line 41**: Cyber resilience of EUCC-certified platforms of smartcards and secure elements (CRA Annex III Class II point 6 / Annex IV).

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
