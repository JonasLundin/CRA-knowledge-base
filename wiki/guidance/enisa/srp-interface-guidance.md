---
type: Official Guidance
title: ENISA Guidance on SRP Technical Interfaces and Machine-to-Machine Integration
description: Technical specifications, REST API schemas, CSAF data formats, and cryptographic protocols for automated machine-to-machine reporting to the SRP.
category: guidance
tags: [cra, guidance, enisa, srp, api, m2m, csaf, technical-interface, schemas]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: enisa-srp-api-guide
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/interface-guidance
    title: Single Reporting Platform - Technical Interface and API Integration Specifications
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-07-22T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2026-04-15
  relevant_provisions:
    - Article 14
    - Article 16
  language: en
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

ENISA's *Technical Interface and API Integration Specifications* defines the machine-to-machine (M2M) interfaces, data models, and transport encryption protocols for automated vulnerability and incident reporting to the Single Reporting Platform (SRP) [^enisa-srp-api-guide].

# Legal effect

This technical specification is non-binding [^enisa-srp-api-guide]. Use of the automated API is optional; economic operators may alternately submit notifications via the SRP web portal interface.

# Applicability

Designed for software vendors, device manufacturers, enterprise Security Operations Centers (SOCs), Product Security Incident Response Teams (PSIRTs), and national CSIRTs implementing automated reporting pipelines.

# Key topics or guidance coverage

The interface guidance details the technical interoperability standards [^enisa-srp-api-guide]:

- **RESTful API Architecture:** Secure HTTPS REST endpoints supporting token-based mutual TLS (mTLS) and OAuth 2.0 / OpenID Connect client credentials.
- **Data Exchange Schemas:**
  - *CSAF 2.0 (Common Security Advisory Framework):* Standardized JSON document structure for describing vulnerabilities, affected product identification (PURL / CPE), and remediation status.
  - *OpenAPI 3.1 Specifications:* Fully specified schemas for early warnings, notifications, and incident milestone updates.
- **Payload Encryption & Integrity:** End-to-end payload signing and encryption using PGP/GPG or JSON Web Encryption (JWE) with ENISA and Member State CSIRT public keys.
- **Rate Limiting & Reliability:** Idempotent submission keys, retry backoff protocols, status polling endpoints, and automated receipt acknowledgments.
- **Test Sandbox Environment:** Dedicated staging API environment enabling manufacturers to validate payload compliance and automated dispatch without submitting live statutory notifications.

# Dates and transitions

- **API Sandbox Availability:** Open for developer testing prior to the 11 September 2026 statutory reporting date.

# Related concepts

- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [SRP Notification Submission and Updates](./srp-notification-submission-and-updates.md)
- [SRP Assigned Representative Registration](./srp-assigned-representative-registration.md)

[^enisa-srp-api-guide]: European Union Agency for Cybersecurity (ENISA), Single Reporting Platform - Technical Interface and API Integration Specifications, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/interface-guidance
