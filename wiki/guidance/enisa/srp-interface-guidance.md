---
type: Official Guidance
title: ENISA Guidance on SRP Assigned Representative Interface Functions
description: Operational guidance on web portal interface functions, user settings, managing Secondary AR delegations, and multi-manufacturer associations on the SRP.
category: guidance
tags: [cra, guidance, enisa, srp, web-interface, assigned-representatives, user-functions]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: enisa-srp-api-guide
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/cra-srp-guidance-ar-interface-functions
    title: CRA SRP guidance - AR Interface functions
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-08-14T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2026-08-14
  relevant_provisions:
    - Article 14
    - Article 16
  language: en
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

ENISA's *CRA SRP guidance - AR Interface functions* defines the web portal navigation, account configuration options, delegation controls, and notification management features available to Assigned Representatives (ARs) on the Single Reporting Platform (SRP) [^enisa-srp-api-guide].

# Legal effect

This technical and operational guidance is non-binding [^enisa-srp-api-guide]. It describes the interface capabilities implemented for the platform's initial release pursuant to Article 16 of Regulation (EU) 2024/2847.

# Applicability

Applies to individual users registered as Assigned Representatives (both Primary and Secondary ARs) submitting or managing CRA Article 14 notifications on behalf of manufacturers.

# Key topics or guidance coverage

The interface guidance outlines the functional components of the web portal [^enisa-srp-api-guide]:

- **Interface Modality (No Machine-to-Machine API):** For the initial 11 September 2026 launch, the SRP operates exclusively via an interactive web interface. No machine-to-machine (REST API) interface is available at launch; programmatic integration (e.g., CSAF 2.0 endpoints) is deferred to a future platform iteration.
- **User Settings and Authentication:** Users manage profile data linked to their personal EU Login account. Multi-factor authentication (MFA) credentials and communication preferences are maintained directly.
- **Assigned Representative Hierarchy:**
  - *Primary Assigned Representative (Primary AR):* The initial user establishing the manufacturer association on the platform. Possesses administrative rights to configure manufacturer entity profiles and delegate access.
  - *Secondary Assigned Representatives (Secondary ARs):* Up to 20 additional users invited by the Primary AR to collaborate on submissions.
- **Invitation and Delegation Lifecycle:**
  - Primary ARs generate secure invitation links for Secondary ARs directly within the platform.
  - Invitation links remain valid for **7 days** from generation.
  - Primary ARs may revoke active delegations or re-issue expired invitations at any time.
- **Multi-Manufacturer Associations:**
  - A single individual user (using one EU Login identity) may be designated as an AR for multiple distinct manufacturers.
  - The interface provides a tenant switcher allowing users to toggle between represented manufacturer profiles without re-authenticating.
- **Notification Dashboard & Tracking:**
  - Centralized dashboard displaying all active, draft, and submitted notifications.
  - Real-time countdown timers for the 72-hour notification deadline and severe incident 1-month final report deadline.
  - Status indicators reflecting validation progress by the lead CSIRT designated as coordinator.

# Dates and transitions

- **First Published:** 14 August 2026.
- **Application:** Operational for portal access from 11 September 2026.

# Related concepts

- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [SRP FAQ](./srp-faq.md)
- [SRP User Registration](./srp-assigned-representative-registration.md)
- [SRP Notification Submission and Updates](./srp-notification-submission-and-updates.md)
- [SRP Glossary](./srp-glossary.md)

[^enisa-srp-api-guide]: European Union Agency for Cybersecurity (ENISA), CRA SRP guidance - AR Interface functions, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/cra-srp-guidance-ar-interface-functions
