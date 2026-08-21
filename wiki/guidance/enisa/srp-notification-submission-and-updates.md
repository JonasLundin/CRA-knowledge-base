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
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/notification-guidance
    title: Single Reporting Platform - Notification Submission and Lifecycle Management Guidance
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-07-08T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2026-03-12
  relevant_provisions:
    - Article 14
    - Article 15
    - Article 16
    - Article 71
  language: en
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

ENISA's *Notification Submission and Lifecycle Management Guidance* provides detailed procedural steps for submitting mandatory notifications through the Single Reporting Platform (SRP) under Article 14 of Regulation (EU) 2024/2847 [^enisa-srp-notification].

# Legal effect

This guidance is non-binding and operational [^enisa-srp-notification]. It assists reporting entities in adhering to the statutory timelines and mandatory data elements established by Article 14 of Regulation (EU) 2024/2847.

# Applicability

Applies to manufacturers, authorized representatives, product security incident response teams (PSIRTs), and designated CSIRTs managing the reporting lifecycle of actively exploited vulnerabilities and severe incidents.

# Key topics or guidance coverage

The guidance outlines the end-to-end reporting lifecycle across four core submission phases [^enisa-srp-notification]:

- **Stage 1: Early Warning (Within 24 Hours):**
  - Minimum initial indicators: identification of the affected product with digital elements, suspected nature of the active exploitation or severe incident, whether other Member States are likely affected, and initial mitigation measures.
- **Stage 2: Formal Notification (Within 72 Hours):**
  - Detailed technical assessment: vulnerability identifier (e.g., CVE / CWE), severity metrics (CVSS score), affected versions and configurations, indicators of compromise (IoCs), root cause analysis (if known), and containment/mitigation status.
- **Stage 3: Intermediate Progress Updates:**
  - Dynamic updates submitted when new critical information emerges (e.g., proof-of-concept release, wider exploitation) or in response to technical queries from the receiving national CSIRT.
- **Stage 4: Final Report (Within 14 Days of Patch or 1 Month for Incidents):**
  - Comprehensive closure report: permanent remediation / patch details, technical root cause, lessons learned, and evidence of user notification.
- **Sensitivity and Delayed Dissemination Flags:** Mechanisms for requesting temporary delay in broader CSIRT network dissemination pursuant to Delegated Regulation (EU) 2026/881 when immediate circulation poses severe risks before patch deployment.

# Dates and transitions

- **Mandatory Reporting Start Date:** 11 September 2026 (Article 71(2)).

# Related concepts

- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [SRP Interface Guidance](./srp-interface-guidance.md)
- [SRP Assigned Representative Registration](./srp-assigned-representative-registration.md)
- [European Commission Reporting Guidance](../european-commission/reporting-guidance.md)

[^enisa-srp-notification]: European Union Agency for Cybersecurity (ENISA), Single Reporting Platform - Notification Submission and Lifecycle Management Guidance, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/notification-guidance
