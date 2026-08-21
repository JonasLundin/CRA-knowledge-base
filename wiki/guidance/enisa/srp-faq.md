---
type: Official Guidance
title: ENISA Single Reporting Platform (SRP) FAQ
description: Frequently asked questions on the operational, security, and technical aspects of reporting via the ENISA Single Reporting Platform.
category: guidance
tags: [cra, guidance, enisa, srp, faq, reporting, authentication, security]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: enisa-srp-faq
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/faq
    title: Single Reporting Platform - Frequently Asked Questions
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-07-15T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2026-01-20
  relevant_provisions:
    - Article 14
    - Article 15
    - Article 16
  language: en
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

ENISA's *Single Reporting Platform - Frequently Asked Questions* addresses practical, operational, and security queries from manufacturers, security officers, and CSIRTs regarding the day-to-day use of the SRP under the Cyber Resilience Act [^enisa-srp-faq].

# Legal effect

This document provides non-binding technical and operational guidance [^enisa-srp-faq]. It does not modify statutory reporting requirements under Article 14 of Regulation (EU) 2024/2847.

# Applicability

Applies to registered users, product security incident response teams (PSIRTs), compliance officers, and CSIRT operators interacting with the SRP.

# Key topics or guidance coverage

The FAQ covers recurring technical and procedural questions [^enisa-srp-faq]:

- **User Authentication and Identity Verification:** Use of EU Login, eIDAS-compliant electronic identification, multi-factor authentication (MFA), and enterprise Single Sign-On (SSO) options.
- **Reporting Deadlines Calculation:** How to count the 24-hour and 72-hour deadlines (UTC timestamps, weekend and public holiday rules).
- **Drafting and Staging Reports:** Managing partial submissions, saving encrypted drafts, and attaching machine-readable Common Vulnerability Reporting Framework (CSAF / JSON) documents.
- **Confidentiality and Data Protection:** Cryptographic storage standards, zero-knowledge architecture components, and strict access boundaries preventing unauthorized staff or third parties from viewing unpatched vulnerability details.
- **Handling Multi-Party Vulnerabilities:** Coordinating reports when an actively exploited vulnerability resides in an upstream open-source or commercial third-party component used across multiple manufacturers.

# Dates and transitions

- **First Published:** January 2026.
- **Regular Refresh:** Updated dynamically as new platform features, API endpoints, and integration tools are released.

# Related concepts

- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [SRP Notification Submission and Updates](./srp-notification-submission-and-updates.md)
- [SRP Interface Guidance](./srp-interface-guidance.md)

[^enisa-srp-faq]: European Union Agency for Cybersecurity (ENISA), Single Reporting Platform - Frequently Asked Questions, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/faq
