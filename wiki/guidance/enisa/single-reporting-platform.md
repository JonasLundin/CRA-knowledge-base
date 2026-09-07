---
type: Official Guidance
title: ENISA Single Reporting Platform (SRP) Overview
description: Operational overview and architecture of the ENISA Single Reporting Platform established under CRA Article 16 for mandatory vulnerability and incident notifications.
category: guidance
tags: [cra, guidance, enisa, srp, reporting, article-16, vulnerabilities, incidents]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: enisa-srp-hub
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
    title: Single Reporting Platform (SRP) for the Cyber Resilience Act
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-09-04T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2025-11-15
  relevant_provisions:
    - Article 14
    - Article 15
    - Article 16
    - Article 71
  language: en
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

The *Single Reporting Platform (SRP)* documentation published by ENISA outlines the functional architecture, operational workflows, and security design of the centralized EU platform for reporting actively exploited vulnerabilities and severe incidents under Article 16 of Regulation (EU) 2024/2847 [^enisa-srp-hub].

# Legal effect

This operational guidance is non-binding [^enisa-srp-hub]. It describes the technical implementation and user interfaces of the platform established pursuant to Article 16 of Regulation (EU) 2024/2847.

# Applicability

Applies to all manufacturers placing products with digital elements on the EU market, authorized representatives, designated national Computer Security Incident Response Teams (CSIRTs), and ENISA operational staff.

# Key topics or guidance coverage

The overview details the operational mechanism of the platform [^enisa-srp-hub]:

- **Centralized Single-Entry Architecture (Article 16(1)):** The SRP provides a single digital entry point for manufacturers, preventing duplicate reporting to individual Member States.
- **Web Portal Access via EU Login:** Users authenticate using personal EU Login accounts secured with multi-factor authentication (MFA). Corporate certificates or custom PKI onboarding are not used for portal access.
- **Assigned Representative (AR) Roles:** Organizations operate through Assigned Representatives, comprising a Primary AR (who registers the manufacturer and manages delegations) and up to 20 Secondary ARs.
- **Simultaneous Dissemination (Article 16(2)):** Upon submission, notifications are made simultaneously available to the relevant CSIRT designated as coordinator (CDaC) and to ENISA, subject to delayed dissemination rules under Particular Exceptional Circumstances (PEC).
- **Initial Release Scope (No M2M API):** The SRP is deployed exclusively as an interactive web portal for its initial release on 11 September 2026. No machine-to-machine (REST API) interface is available at launch; API functionality is planned for a subsequent phase.
- **Mandatory Reporting First:** Voluntary reporting under Article 15 is not implemented in the initial release; the initial version strictly supports mandatory reporting under Article 14 (and Article 24(3) for open-source software stewards from December 2027).
- **End-to-End Confidentiality & Encryption:** Safeguards ensure cryptographic protection of sensitive vulnerability notifications, role-based isolation, and complete audit logging.

# Dates and transitions

- **Platform Launch:** Operational deployment for mandatory reporting on **11 September 2026** (Article 71(2)(a)).

# Related concepts

- [SRP FAQ](./srp-faq.md)
- [SRP Notification Submission and Updates](./srp-notification-submission-and-updates.md)
- [SRP Interface Guidance](./srp-interface-guidance.md)
- [SRP User Registration](./srp-assigned-representative-registration.md)
- [SRP Glossary](./srp-glossary.md)
- [CSIRTs Designated as Coordinators](./srp-csirt-coordinators.md)
- [European Commission Reporting Guidance](../european-commission/reporting-guidance.md)

[^enisa-srp-hub]: European Union Agency for Cybersecurity (ENISA), Single Reporting Platform (SRP) for the Cyber Resilience Act, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
