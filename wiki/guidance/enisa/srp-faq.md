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
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions
    title: CRA Single Reporting Platform - Frequently Asked Questions
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-09-04T00:00:00Z
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
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

ENISA's *CRA Single Reporting Platform - Frequently Asked Questions* addresses practical, operational, and security queries from manufacturers, security officers, and CSIRTs regarding the day-to-day use of the SRP under the Cyber Resilience Act [^enisa-srp-faq].

# Legal effect

This document provides non-binding technical and operational guidance [^enisa-srp-faq]. It does not modify statutory reporting requirements under Article 14 of Regulation (EU) 2024/2847.

# Applicability

Applies to registered users, product security incident response teams (PSIRTs), compliance officers, and CSIRT operators interacting with the SRP.

# Key topics or guidance coverage

The FAQ (updated 4 September 2026) provides critical operational details [^enisa-srp-faq]:

- **No API at Initial Release (Q15):** ENISA explicitly clarifies that no machine-to-machine Application Programming Interface (API) is provided at the initial 11 September 2026 release of the SRP. All notifications must be submitted directly through the platform web interface. API functionality may be considered in a future phase.
- **User Authentication & Identity (Q9, Q10):** Assigned Representatives log in using personal EU Login accounts secured by multi-factor authentication (MFA). Corporate certificates or organizational federated SSO are not supported for individual access.
- **Pre-emptive Registration Discouraged (Q11):** Manufacturers are advised **NOT** to register proactively on the platform prior to needing to report an incident or vulnerability, to prevent overwhelming national CSIRTs with identity validations. Registration can be completed at the same time an initial notification is filed.
- **Parallel CSIRT Validation & Quotas (Q12):** National CSIRTs validate Assigned Representative associations in parallel with incoming reports. An unvalidated AR is permitted to submit up to 20 notifications while verification is pending.
- **Submission Deadlines & SRP Counters (Q7, Q26):**
  - *Early Warning:* Within 24 hours of becoming aware.
  - *72-Hour Notification:* The platform counter displays a deadline of 48 hours following the submission of the 24-hour early warning.
  - *Final Report:* For severe incidents, the SRP counter displays a deadline of 1 month after the 72-hour notification. For actively exploited vulnerabilities, no automated counter is displayed, as the statutory deadline is within 14 days after a corrective or mitigating measure becomes available.
- **Lead CSIRT Determination Hierarchy for Non-EU Manufacturers (Q18):**
  1. Member State where the Authorized Representative with the highest number of products placed on the EU market is established.
  2. Member State of the importer with the highest product volume.
  3. Member State of the distributor with the highest product volume.
  4. Member State with the largest user base.
- **Particular Exceptional Circumstances (PEC) & Delayed Dissemination (Q8, Q25):**
  - Invoked during the 72-hour notification stage under Article 16(2) and Delegated Regulation (EU) 2026/881.
  - When a manufacturer marks that PEC applies, ENISA receives only restricted information (common fields and delayed dissemination justification) until the lead CSIRT approves wider distribution.
- **Platform Unavailability Contingency (Q20):** If the SRP is temporarily unreachable, submitters must wait for service restoration and submit via the platform. Direct contact with national CSIRTs during an outage does not waive the obligation to file the formal record on the SRP once restored.
- **Voluntary Reporting Deferral (Q14):** Voluntary reporting under Article 15 is not supported in the initial SRP launch; only mandatory reporting under Article 14 and Article 24(3) is enabled.

# Dates and transitions

- **First Published:** January 2026.
- **Latest Document Update:** 4 September 2026.
- **Maintenance Model:** Updated periodically by ENISA to reflect platform iterations and operational lessons learned.

# Related concepts

- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [SRP Notification Submission and Updates](./srp-notification-submission-and-updates.md)
- [SRP Interface Guidance](./srp-interface-guidance.md)
- [SRP User Registration](./srp-assigned-representative-registration.md)
- [SRP Glossary](./srp-glossary.md)
- [CSIRTs Designated as Coordinators](./srp-csirt-coordinators.md)

[^enisa-srp-faq]: European Union Agency for Cybersecurity (ENISA), CRA Single Reporting Platform - Frequently Asked Questions, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions
