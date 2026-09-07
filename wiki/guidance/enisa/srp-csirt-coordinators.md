---
type: Official Guidance
title: CSIRTs Designated as Coordinators under CRA Article 14 and 16
description: Directory, governance rules, and coordination roles of the designated Computer Security Incident Response Teams across EU Member States under the CRA.
category: guidance
tags: [cra, guidance, enisa, srp, csirts, coordinators, article-14, article-16]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-09-07T00:00:00Z }
stale_after: 2026-12-07T00:00:00Z
sources:
  - id: enisa-srp-csirts
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/list-of-csirts-designated-as-coordinators
    title: List of CSIRTs Designated as Coordinators
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-09-04T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2026-09-04
  relevant_provisions:
    - Article 14
    - Article 16
    - Article 33
  language: en
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

ENISA's *List of CSIRTs Designated as Coordinators* identifies the national Computer Security Incident Response Teams (CSIRTs) designated by Member States pursuant to Article 14(3) and Article 16 of Regulation (EU) 2024/2847 to act as coordinators for receiving, validating, and managing CRA notifications [^enisa-srp-csirts].

# Legal effect

This directory and operational guidance is non-binding [^enisa-srp-csirts]. The legal designation of national CSIRTs as coordinators is performed by Member States under Article 14(3) of Regulation (EU) 2024/2847 in accordance with Directive (EU) 2022/2555 (NIS2).

# Applicability

Applies to manufacturers, Authorized Representatives, Assigned Representatives, and national CSIRTs participating in coordinated vulnerability disclosure and incident management within the Union.

# Key topics or guidance coverage

The publication specifies the governance roles, lead CSIRT criteria, and coordination obligations across the Union [^enisa-srp-csirts]:

- **Statutory Mandate (Article 14(3) & 16(2)):**
  - Each Member State designates one CSIRT from among those established or designated under Article 10 of Directive (EU) 2022/2555 to act as coordinator (CDaC) for CRA notifications.
  - The designated CSIRT serves as the single national operational interlocutor on the Single Reporting Platform (SRP).
- **Core Responsibilities of the Lead CDaC:**
  - *Entity & AR Validation:* Validates the manufacturer profile and the legitimacy of registered Assigned Representatives on the SRP.
  - *Notification Triage & Review:* Conducts initial technical assessments of 24h early warnings and 72h notifications.
  - *Dissemination Management:* Disseminates received notifications via the SRP to the designated CSIRTs of other Member States where the product is made available on the market.
  - *Particular Exceptional Circumstances (PEC):* Evaluates and approves/denies requests for delayed dissemination under Article 16(2) and Delegated Regulation (EU) 2026/881.
  - *Information Requests:* May request intermediate follow-up reports from manufacturers under Article 14(2)(c).
  - *Technical Assistance:* Provides operational cybersecurity support to the reporting manufacturer upon request.
- **Lead CSIRT Determination Hierarchy:**
  - *EU Manufacturers:* The CSIRT designated as coordinator of the Member State where the manufacturer has its main establishment.
  - *Non-EU Manufacturers:* When no EU establishment exists, the lead CDaC is determined through the following strict statutory order:
    1. Member State of the Authorized Representative with the highest number of products placed on the EU market.
    2. Member State of the importer with the highest number of products placed on the market.
    3. Member State of the distributor with the highest number of products placed on the market.
    4. Member State with the largest user base.
- **Designated Coordinator Directory:**
  - Lists the 27 designated national coordinators across the Union, including CERT.at (Austria), CERT.be (Belgium), BSI / CERT-Bund (Germany), CCN-CERT / INCIBE-CERT (Spain), ANSSI / CERT-FR (France), CSIRT-ITA (Italy), CERT-SE (Sweden), and counterparts across all Member States.

# Dates and transitions

- **Publication Date:** 4 September 2026.
- **Operational Go-Live:** Active coordination on the SRP commences 11 September 2026.

# Related concepts

- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [SRP FAQ](./srp-faq.md)
- [SRP Notification Submission and Updates](./srp-notification-submission-and-updates.md)
- [SRP User Registration](./srp-assigned-representative-registration.md)
- [SRP Glossary](./srp-glossary.md)
- [SRP Routing and Dissemination](../../obligations/reporting/srp-routing-and-dissemination.md)

[^enisa-srp-csirts]: European Union Agency for Cybersecurity (ENISA), List of CSIRTs Designated as Coordinators, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/list-of-csirts-designated-as-coordinators
