---
type: Procedure
title: Severe Incident Notification (72-Hour Report)
description: Second-stage detailed report on severe incidents impacting product security submitted within 72 hours under Article 14(4)(b) of Regulation (EU) 2024/2847.
category: procedure
tags: [cra, reporting, incident, 72h, article-14, procedure]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-14
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
    title: Regulation (EU) 2024/2847, Article 14
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: enisa-srp-docs
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
    title: ENISA Single Reporting Platform Documentation
    author: ENISA
    last_modified: 2026-03-01T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 14(4)(b)
  applies_from: 2026-09-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Within 72 hours of becoming aware of a severe incident impacting the security of a product with digital elements, the manufacturer must submit an incident notification updating the initial 24-hour early warning.[^cra-art-14] [^enisa-srp-docs]

# Legal effect

Fulfilling the 72-hour severe incident notification enables national CSIRTs and ENISA to coordinate cross-border incident containment and assess impact on critical infrastructure and supply chains.[^cra-art-14]

# Applicability

Applies to manufacturers of products with digital elements experiencing an incident that:
- Has caused or is capable of causing severe operational disruption to the product or its users;
- Affects the provision of services by essential entities under NIS2; or
- Has caused or is capable of causing material or non-material damage to users.[^cra-art-14]

# Requirements or coverage

Under Article 14(4)(b), the 72-hour severe incident notification must contain:

1. **Initial assessment:** Severity, operational consequences, and root cause analysis where known;
2. **Impact assessment:** Estimated number of affected users, devices, or downstream integrations;
3. **Indicators of compromise (IoCs):** Technical indicators, signatures, or attacker behavior patterns;
4. **Mitigation actions:** Corrective measures implemented, containment steps taken, and advice issued to users.[^cra-art-14] [^enisa-srp-docs]

# Dates and transitions

- Applies from 11 September 2026.

# Related concepts

- [Article 14 Reporting Overview](article-14-reporting.md)
- [Early Warning (24h)](early-warning-24h.md)
- [Final Report (1 Month)](final-report-one-month.md)
- [User Notifications](user-notifications.md)

[^cra-art-14]: Regulation (EU) 2024/2847, Article 14, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
[^enisa-srp-docs]: ENISA, Single Reporting Platform Documentation, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
