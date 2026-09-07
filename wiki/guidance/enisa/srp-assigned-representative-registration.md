---
type: Official Guidance
title: ENISA Guidance on SRP User Registration and Assigned Representatives
description: Operational instructions for entity onboarding, EU Login authentication, designating Assigned Representatives, and parallel CSIRT validation on the SRP.
category: guidance
tags: [cra, guidance, enisa, srp, registration, assigned-representatives, identity-verification, onboarding]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: enisa-srp-registration
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/cra-srp-guidance-ar-user-registration
    title: CRA SRP guidance - AR User registration
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-08-03T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2026-08-03
  relevant_provisions:
    - Article 14
    - Article 15
    - Article 16
    - Article 17
    - Article 20
  language: en
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

ENISA's *CRA SRP guidance - AR User registration* provides procedural instructions for manufacturers and authorized representatives to establish accounts, designate Assigned Representatives (ARs), and complete entity onboarding on the Single Reporting Platform (SRP) [^enisa-srp-registration].

# Legal effect

This guidance is non-binding and operational [^enisa-srp-registration]. It defines the account registration protocols required to access and submit notifications through the SRP infrastructure under Article 16 of Regulation (EU) 2024/2847.

# Applicability

Applies to manufacturers (EU and non-EU), authorized representatives appointed under Article 20, reporting teams, and individual users registering as Assigned Representatives.

# Key topics or guidance coverage

The guidance outlines the account setup lifecycle, authentication, and validation model [^enisa-srp-registration]:

- **Personal Authentication via EU Login:**
  - Individual users access the SRP using their personal EU Login account secured by multi-factor authentication (MFA).
  - Corporate certificates or federated enterprise SSO are not utilized for user onboarding.
- **Assigned Representative Designation:**
  - *Primary Assigned Representative (Primary AR):* The individual who initially registers the manufacturer entity on the platform. The Primary AR provides the manufacturer's legal name, registration number (e.g., VAT, EORI, or national commercial registry code), contact details, and country of establishment.
  - *Secondary Assigned Representatives (Secondary ARs):* Up to 20 additional users whom the Primary AR can invite to collaborate and submit reports.
- **Invitation Workflow:**
  - Primary ARs invite Secondary ARs by generating unique invitation links in the platform interface.
  - Invitation links remain valid for **7 days**.
- **Parallel CSIRT Validation Process:**
  - After registration, the relevant CSIRT designated as coordinator (CDaC) validates the manufacturer profile and the legitimacy of the Assigned Representative association.
  - Validation occurs in parallel with operational reporting to avoid blocking urgent incident submissions.
- **Unvalidated AR Notification Quota:**
  - While national CSIRT validation is pending, an unvalidated Assigned Representative is permitted to submit up to **20 notifications**.
- **Advisory Against Pre-emptive Registration:**
  - ENISA and national CSIRTs explicitly advise manufacturers **NOT** to register proactively on the platform in advance of experiencing an actively exploited vulnerability or severe incident.
  - Completing registration concurrently with the first required submission prevents administrative bottlenecks across Member State CSIRTs.

# Dates and transitions

- **First Published:** 3 August 2026.
- **Operational Availability:** Ahead of the 11 September 2026 reporting deadline.

# Related concepts

- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [SRP FAQ](./srp-faq.md)
- [SRP Interface Guidance](./srp-interface-guidance.md)
- [SRP Notification Submission and Updates](./srp-notification-submission-and-updates.md)
- [CSIRTs Designated as Coordinators](./srp-csirt-coordinators.md)

[^enisa-srp-registration]: European Union Agency for Cybersecurity (ENISA), CRA SRP guidance - AR User registration, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/cra-srp-guidance-ar-user-registration
