---
type: Official Guidance
title: ENISA Guidance on SRP Notification Submission and Updates
description: Detailed operational guidance on drafting, submitting, and updating early warnings, 72-hour notifications, and final reports on the Single Reporting Platform.
category: guidance
tags: [cra, guidance, enisa, srp, notifications, article-14, early-warning, incident-reporting]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: enisa-srp-notification
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/cra-srp-guidance-ar-notification-submission-and-update
    title: CRA SRP guidance - AR Notification submission and update
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
    - Article 71
  language: en
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

ENISA's *CRA SRP guidance - AR Notification submission and update* provides step-by-step procedural instructions for submitting mandatory notifications of actively exploited vulnerabilities and severe incidents via the Single Reporting Platform (SRP) under Article 14 of Regulation (EU) 2024/2847 [^enisa-srp-notification].

# Legal effect

This guidance is non-binding and operational [^enisa-srp-notification]. It assists reporting entities in adhering to the statutory timelines, required data fields, and submission mechanics established by Article 14 of Regulation (EU) 2024/2847.

# Applicability

Applies to manufacturers, authorized representatives, product security incident response teams (PSIRTs), and Assigned Representatives submitting notifications under Article 14.

# Key topics or guidance coverage

The guidance details the submission workflow structured across three sequential platform stages [^enisa-srp-notification]:

- **Stage 1: Early Warning (Within 24 Hours):**
  - Minimum initial submission indicating whether the report concerns an Actively Exploited Vulnerability (AEV) or a Severe Incident (SI).
  - Captures high-level product details, suspected vulnerability or incident nature, whether other Member States are likely affected, and initial mitigation steps taken.
- **Stage 2: Formal Notification (Within 72 Hours):**
  - Detailed technical submission submitted via the platform's second tab.
  - The SRP countdown timer displays a 48-hour deadline from the timestamp of the early warning submission.
  - Includes vulnerability metrics (CVE/CWE IDs, CVSS score), affected product versions, exploitation evidence, root cause analysis (if known), and mitigation actions.
  - *Particular Exceptional Circumstances (PEC):* Submitters may invoke Article 16(2) grounds delaying broader dissemination. When selected, ENISA receives only partial notification data until the lead CSIRT approves wider distribution.
- **Stage 3: Intermediate Updates and Requests:**
  - Submitters provide dynamic updates via notes and follow-up submissions attached to the active notification record (e.g., when new exploit telemetry emerges or upon inquiry from the lead CSIRT).
- **Stage 4: Final Report:**
  - Submitted via the third tab to conclude the reporting lifecycle.
  - *Severe Incidents:* The platform timer displays a deadline of 1 month after the 72-hour notification submission.
  - *Actively Exploited Vulnerabilities:* No automatic timer is displayed; statutory submission is required within 14 days after a corrective or mitigating measure becomes available.
- **Draft Functionality:** Submitters can save in-progress forms as drafts prior to formal submission. Drafts remain visible only to the manufacturer's Assigned Representatives until formally transmitted.
- **Simultaneous Routing & Lead CSIRT Dissemination:** Upon formal submission, the platform routes the notification to the selected lead CSIRT designated as coordinator (CDaC) and to ENISA. The lead CDaC reviews and manually disseminates the notification to other concerned Member State CSIRTs via the SRP.

# Dates and transitions

- **First Published:** 3 August 2026.
- **Mandatory Reporting Start Date:** 11 September 2026 (Article 71(2)(a)).

# Related concepts

- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [SRP FAQ](./srp-faq.md)
- [SRP Interface Guidance](./srp-interface-guidance.md)
- [SRP User Registration](./srp-assigned-representative-registration.md)
- [SRP Glossary](./srp-glossary.md)
- [CSIRTs Designated as Coordinators](./srp-csirt-coordinators.md)
- [Article 14 Reporting Overview](../../obligations/reporting/article-14-reporting.md)

[^enisa-srp-notification]: European Union Agency for Cybersecurity (ENISA), CRA SRP guidance - AR Notification submission and update, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/cra-srp-guidance-ar-notification-submission-and-update
