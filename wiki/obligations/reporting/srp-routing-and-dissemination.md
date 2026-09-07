---
type: Requirement
title: Single Reporting Platform Routing and Dissemination Rules
description: Architecture of ENISA's Single Reporting Platform (SRP) and rules for delaying dissemination under Delegated Regulation (EU) 2026/881.
category: requirement
tags: [cra, srp, enisa, csirt, dissemination-delay, delegated-regulation-2026-881]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-14
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
    title: Regulation (EU) 2024/2847, Article 14
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: reg-2026-881
    resource: http://data.europa.eu/eli/reg_del/2026/881/oj/eng
    title: Commission Delegated Regulation (EU) 2026/881
    author: European Commission
    last_modified: 2026-04-15T00:00:00Z
  - id: enisa-srp-docs
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
    title: ENISA Single Reporting Platform Documentation
    author: ENISA
    last_modified: 2026-03-01T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 14(5)–(7), Delegated Regulation (EU) 2026/881
  applies_from: 2026-09-11
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

Article 14 and Article 16 of Regulation (EU) 2024/2847 mandate that all notifications of actively exploited vulnerabilities and severe incidents be submitted via the Single Reporting Platform (SRP) established and maintained by ENISA.[^cra-art-14] [^enisa-srp-docs]

# Legal effect

The SRP serves as the single electronic entry point for all CRA Article 14 reporting. Simultaneous transmission to the competent CSIRTs and ENISA occurs automatically via end-to-end encrypted channels.[^cra-art-14]

# Applicability

Applies to all manufacturers submitting Article 14 notifications and all designated national CSIRTs and market surveillance authorities receiving notifications.[^cra-art-14]

# Requirements or coverage

1. **Simultaneous routing:** When a report is submitted, the SRP transmits it simultaneously to:
   - The designated lead CSIRT of the Member State where the manufacturer has its main establishment (or, for non-EU manufacturers, determined via the statutory hierarchy: Authorized Representative > importer > distributor > largest user base);
   - ENISA (Article 16(2)).[^cra-art-14]
2. **Dissemination delay rules & Particular Exceptional Circumstances (PEC):** Under Article 16(2) and Commission Delegated Regulation (EU) 2026/881, dissemination to other Member State CSIRTs or market surveillance authorities may be delayed where immediate circulation poses heightened cybersecurity risks prior to patch availability.[^reg-2026-881] When PEC is marked at the 72-hour notification stage, ENISA receives only restricted information (common fields and delayed dissemination justification) until the lead CSIRT approves wider distribution.
3. **CSIRT coordinator powers:** The lead CSIRT reviews the notification, validates Assigned Representatives, manages dissemination to CSIRTs of other Member States where the product is marketed, and coordinates technical remediation;
4. **Confidentiality:** All reports are treated as strictly confidential commercial and security information.[^cra-art-14] [^enisa-srp-docs]

# Dates and transitions

- SRP operational and Article 14 reporting applicable from 11 September 2026.

# Related concepts

- [Article 14 Reporting Overview](article-14-reporting.md)
- [Early Warning (24h)](early-warning-24h.md)
- [Vulnerability Notification (72h)](vulnerability-notification-72h.md)
- [CSIRTs Designated as Coordinators](../../guidance/enisa/srp-csirt-coordinators.md)
- [SRP FAQ](../../guidance/enisa/srp-faq.md)
- [SRP Glossary](../../guidance/enisa/srp-glossary.md)

[^cra-art-14]: Regulation (EU) 2024/2847, Article 14, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
[^reg-2026-881]: Commission Delegated Regulation (EU) 2026/881, http://data.europa.eu/eli/reg_del/2026/881/oj/eng
[^enisa-srp-docs]: ENISA, Single Reporting Platform Documentation, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
