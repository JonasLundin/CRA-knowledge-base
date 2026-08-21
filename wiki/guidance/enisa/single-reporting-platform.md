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
    last_modified: 2026-07-01T00:00:00Z
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
  checked_at: 2026-08-21T00:00:00Z
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
- **Simultaneous Dissemination (Article 16(2)):** Upon submission, notifications are automatically routed simultaneously to the designated CSIRT of the Member State where the manufacturer has its main establishment (or representative) and to ENISA.
- **End-to-End Confidentiality & Encryption:** Technical security safeguards ensuring end-to-end cryptographic protection of sensitive vulnerability details, restricted role-based access, and audited access logs.
- **Support for Multi-Stage Workflows:** Structured submission workflows supporting 24-hour early warnings, 72-hour formal notifications, sensitive progress updates, and final closure reports.
- **Voluntary Reporting Integration (Article 14(8)):** Dedicated channels for voluntary submissions by open-source stewards, security researchers, and non-commercial entities.

# Dates and transitions

- **Platform Launch:** Operational deployment ahead of the statutory reporting deadline of **11 September 2026** (Article 71(2)).

# Related concepts

- [SRP FAQ](./srp-faq.md)
- [SRP Notification Submission and Updates](./srp-notification-submission-and-updates.md)
- [SRP Interface Guidance](./srp-interface-guidance.md)
- [European Commission Reporting Guidance](../european-commission/reporting-guidance.md)

[^enisa-srp-hub]: European Union Agency for Cybersecurity (ENISA), Single Reporting Platform (SRP) for the Cyber Resilience Act, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
