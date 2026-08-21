---
type: Official Guidance
title: European Commission Guidance on CRA Reporting Obligations
description: Official policy guidance on Article 14 mandatory notification workflows for actively exploited vulnerabilities and severe incidents via the Single Reporting Platform.
category: guidance
tags: [cra, guidance, european-commission, reporting, article-14, vulnerabilities, incidents, srp, csirt]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-02-21T00:00:00Z
sources:
  - id: ec-cra-reporting
    resource: https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
    title: Cyber Resilience Act - Vulnerability and Incident Reporting Overview
    author: European Commission
    last_modified: 2026-06-25T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: European Commission - DG CNECT
  authority_level: non_binding
  document_status: published
  publication_date: 2025-05-12
  relevant_provisions:
    - Article 14
    - Article 15
    - Article 16
    - Article 71
  language: en
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

The European Commission's *Guidance on Vulnerability and Incident Reporting Overview* explains the statutory reporting regime under Article 14 of Regulation (EU) 2024/2847 [^ec-cra-reporting]. It clarifies triggers, multi-stage notification deadlines, recipient roles (designated CSIRTs and ENISA), and user notification duties.

# Legal effect

This guidance is non-binding and explanatory [^ec-cra-reporting]. It interprets the mandatory reporting procedures established in Articles 14 and 16 of Regulation (EU) 2024/2847.

# Applicability

Applies to all manufacturers placing products with digital elements on the EU market, designated national CSIRTs, ENISA, and market surveillance authorities.

# Key topics or guidance coverage

The guidance structures the reporting lifecycle and operational rules [^ec-cra-reporting]:

- **Reportable Triggers (Article 14(1)–(2)):**
  1. *Actively Exploited Vulnerabilities:* Any vulnerability in a product with digital elements for which reliable evidence exists that an adversary is executing malicious code without authorization.
  2. *Severe Incidents:* Any incident having a significant impact on the cybersecurity or availability of a product with digital elements.
- **Multi-Stage Reporting Deadlines:**
  - **Early Warning:** Submitted within **24 hours** of becoming aware of the actively exploited vulnerability or severe incident.
  - **Notification:** Submitted within **72 hours** of becoming aware, providing initial technical assessment, general information, and risk mitigation details.
  - **Intermediate Reporting:** Submitted upon request of the designated CSIRT or when substantial new information arises.
  - **Final Report:** Submitted within **14 days** after a corrective measure/patch is available (or within **1 month** of the 72-hour notification for incidents).
- **Single Reporting Platform (SRP) Architecture (Article 16):** Notifications submitted via the SRP are simultaneously disseminated to the designated CSIRT of the Member State where the manufacturer is established and to ENISA.
- **Delayed Dissemination (Delegated Regulation (EU) 2026/881):** Rules governing temporary delay in sharing vulnerability details across broader networks when premature disclosure would create severe cybersecurity risks before a patch is ready.
- **User Notification (Article 14(4)):** Manufacturer obligations to inform affected users of the vulnerability or incident, potential impact, and corrective mitigation measures.

# Dates and transitions

- **Early Application:** Article 14 reporting obligations apply earlier than the general act, becoming mandatory on **11 September 2026** (Article 71(2)).

# Related concepts

- [Commission Guidance C(2026) 5252](./c-2026-5252-cra-guidance.md)
- [Manufacturers Guidance](./manufacturers-guidance.md)
- [Member States Guidance](./member-states-guidance.md)

[^ec-cra-reporting]: European Commission, Cyber Resilience Act - Vulnerability and Incident Reporting Overview, https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
