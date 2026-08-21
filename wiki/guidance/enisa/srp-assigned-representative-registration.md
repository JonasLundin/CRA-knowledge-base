---
type: Official Guidance
title: ENISA Guidance on SRP User Registration and Assigned Representatives
description: Operational instructions for entity onboarding, user account management, identity verification, and designating assigned representatives within the Single Reporting Platform.
category: guidance
tags: [cra, guidance, enisa, srp, registration, assigned-representatives, identity-verification, onboarding]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: enisa-srp-registration
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/user-registration-guidance
    title: Single Reporting Platform - Entity Onboarding and User Registration Guidance
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-06-20T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2026-03-05
  relevant_provisions:
    - Article 14
    - Article 15
    - Article 16
    - Article 17
    - Article 20
  language: en
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

ENISA's *Entity Onboarding and User Registration Guidance* provides step-by-step instructions for manufacturers and their authorized or assigned representatives to establish organizational accounts on the Single Reporting Platform (SRP) [^enisa-srp-registration].

# Legal effect

This guidance is non-binding and procedural [^enisa-srp-registration]. It defines the operational registration protocols required to access and submit notifications through the SRP infrastructure under Article 16 of Regulation (EU) 2024/2847.

# Applicability

Applies to manufacturers (EU and non-EU), authorized representatives appointed under Article 20, assigned reporting agents (such as external incident response or legal teams), and administrative managers.

# Key topics or guidance coverage

The guidance outlines the account setup lifecycle and access hierarchy [^enisa-srp-registration]:

- **Entity Account Creation:** Registering the legal entity using its official company identifier (EORI, VAT, or national trade registry number) and validating corporate domain ownership.
- **Identity Proofing & EU Login Integration:** Authenticating administrative users via qualified electronic signatures (eIDAS) or high-assurance EU Login credentials.
- **Role-Based Access Control (RBAC):**
  - *Entity Administrator:* Manages company profile, delegates user permissions, and configures notification webhooks.
  - *Reporting Officer / Security Lead:* Submits, updates, and reviews technical vulnerability and incident notifications.
  - *Read-Only Auditor:* Observes submission logs without editing or submission rights.
- **Assigning External Representatives (Article 20):** Formal verification protocols for non-EU manufacturers mandating an authorized representative within the Union to handle reporting responsibilities.
- **Key Management & Cryptographic Setup:** Uploading public PGP/GPG keys or x.509 certificates used to decrypt secure communications and verify the authenticity of automated API submissions.

# Dates and transitions

- **Early Registration Window:** Available in advance of the 11 September 2026 reporting deadline to ensure organizations are verified and pre-configured.

# Related concepts

- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [SRP Notification Submission and Updates](./srp-notification-submission-and-updates.md)
- [SRP Interface Guidance](./srp-interface-guidance.md)

[^enisa-srp-registration]: European Union Agency for Cybersecurity (ENISA), Single Reporting Platform - Entity Onboarding and User Registration Guidance, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/user-registration-guidance
