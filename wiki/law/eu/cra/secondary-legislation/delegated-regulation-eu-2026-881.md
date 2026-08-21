---
type: Legal Instrument
title: "Commission Delegated Regulation (EU) 2026/881: Delaying Dissemination of Notifications via Single Reporting Platform"
description: "Specifies terms and cybersecurity-related grounds permitting designated CSIRTs to delay notification dissemination across the Single Reporting Platform."
category: law
tags: [cra, law, delegated-regulation, secondary-legislation, reporting, srp, csirt, dissemination-delay]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-12-11T00:00:00Z
sources:
  - id: cra-del-reg-2026-881
    resource: http://data.europa.eu/eli/reg_del/2026/881/oj
    title: Commission Delegated Regulation (EU) 2026/881
    author: European Commission
    last_modified: 2026-04-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  instrument_type: delegated_regulation
  empowerment: "Regulation (EU) 2024/2847, Article 16(2)"
  adoption_date: 2025-12-11
  publication_date: 2026-04-20
  in_force_date: 2026-05-10
  applies_from: 2026-09-11
  celex: 32026R0881
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Commission Delegated Regulation (EU) 2026/881 specifies the terms, conditions, and strict cybersecurity-related grounds under which a designated CSIRT coordinator initially receiving a CRA Article 14 notification may delay disseminating it to other CSIRTs via the Single Reporting Platform.

# Legal effect

Establishes exhaustive statutory criteria and procedures permitting temporary withholding of vulnerability notifications across the EU CSIRTs network to prevent premature disclosure, weaponisation, or operational disruption.

# Applicability

Applies to designated CSIRT coordinators, ENISA, the CSIRTs Network, and notifying manufacturers.

# Requirements or coverage

- **Article 1 (Subject matter)**: Specifies conditions enabling CSIRT coordinators to delay dissemination of notifications under Articles 14(1), 14(3), 15(1), and 15(2).
- **Article 2 (Definitions)**: Defines 'CSIRT initially receiving the notification' and 'relevant CSIRT'.
- **Article 3 (Grounds stemming from information nature)**: Authorises temporary delay where risks of dissemination outweigh security benefits and cannot be mitigated by traffic protocols (TLP/PAP), meeting at least one condition:
  - (a) Manufacturer confirms effective mitigation (patch/guidance) is expected within **72 hours**;
  - (b) Notification enables direct creation of an exploit technique with low barrier to entry;
  - (c) Sufficient mitigation information can be shared without disclosing the full technical vulnerability;
  - (d) Vulnerability is part of an ongoing Coordinated Vulnerability Disclosure (CVD) process where the CSIRT acts as trusted intermediary.
- **Article 4 (Grounds relating to specific CSIRTs)**: Delays dissemination to a specific CSIRT affected by an active cybersecurity incident or lacking adequate confidentiality capabilities.
- **Article 5 (Grounds relating to Single Reporting Platform)**: Delays dissemination via the SRP if ENISA reports an active security compromise affecting SRP confidentiality.
- **Article 6**: Enters into force on 10 May 2026 and applies from 11 September 2026.

# Dates and transitions

- Adopted by the Commission on 11 December 2025.
- Published in the Official Journal (OJ L, 2026/881) on 20 April 2026.
- Enters into force on 10 May 2026; applies from 11 September 2026 (synchronised with Article 14).

# Related concepts

- [CRA Article 14: Reporting obligations of manufacturers](../articles/article-14.md)
- [CRA Article 16: Single reporting platform](../articles/article-16.md)
- [Secondary Legislation Register](register.md)

[^cra-del-reg-2026-881]: Commission Delegated Regulation (EU) 2026/881, OJ L, 2026/881, 20.04.2026, [ELI: http://data.europa.eu/eli/reg_del/2026/881/oj](http://data.europa.eu/eli/reg_del/2026/881/oj).
