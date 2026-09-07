---
type: Requirement
title: Article 14 Reporting Obligations Overview
description: Mandatory notification framework for actively exploited vulnerabilities and severe incidents under Article 14 of Regulation (EU) 2024/2847.
category: requirement
tags: [cra, reporting, article-14, vulnerability, incident, csirt, enisa, srp]
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
  provision: Article 14
  applies_from: 2026-09-11
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

Article 14 of Regulation (EU) 2024/2847 requires manufacturers of products with digital elements to report any actively exploited vulnerability contained in the product and any severe incident having an impact on the security of the product to the designated CSIRT and ENISA via the Single Reporting Platform (SRP).[^cra-art-14] [^enisa-srp-docs]

# Legal effect

Compliance with Article 14 is a mandatory legal obligation enforceable from 11 September 2026 (15 months before general CRA application). Failure to notify within the prescribed statutory timeframes constitutes an infringement subject to administrative fines under Article 64.[^cra-art-14]

# Applicability

Applies to all manufacturers placing products with digital elements on the EU market, including legacy products placed on the market before 11 September 2026 that are actively maintained or available.[^cra-art-14]

# Requirements or coverage

Manufacturers must report via a multi-stage timeline:

### 1. Actively Exploited Vulnerabilities (Article 14(1)–(2))
- **Early Warning:** Within **24 hours** of becoming aware (indicating whether other Member States are likely affected);
- **Vulnerability Notification:** Within **72 hours** of becoming aware (technical details, severity, corrective measures);
- **Intermediate Status Update:** Upon request of the lead CSIRT or ENISA, or voluntarily via follow-up notes;
- **Final Report:** No later than **14 days** after a corrective or mitigating measure is in place (or 14 days after closure if no measure is available).

### 2. Severe Incidents (Article 14(3)–(4))
- **Early Warning:** Within **24 hours** of becoming aware (indicating whether other Member States are likely affected);
- **Incident Notification:** Within **72 hours** of becoming aware (incident description, severity, impact assessment);
- **Final Report:** Within **1 month** after submission of the 72-hour incident notification (comprehensive report on root causes and mitigation).

### 3. Centralised Routing
All notifications are submitted electronically via the ENISA-operated Single Reporting Platform (SRP) web portal, which simultaneously transmits them to the designated lead CSIRT and ENISA, subject to delayed dissemination where Particular Exceptional Circumstances apply.[^cra-art-14] [^enisa-srp-docs]

# Dates and transitions

- **11 September 2026:** Article 14 applies across the EU (Article 71(2)(a)).

# Related concepts

- [Early Warning (24h)](early-warning-24h.md)
- [Vulnerability Notification (72h)](vulnerability-notification-72h.md)
- [Severe Incident Notification (72h)](severe-incident-notification-72h.md)
- [Final Report (1 Month)](final-report-one-month.md)
- [SRP Routing & Dissemination](srp-routing-and-dissemination.md)
- [User Notifications](user-notifications.md)

[^cra-art-14]: Regulation (EU) 2024/2847, Article 14, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
[^enisa-srp-docs]: ENISA, Single Reporting Platform Documentation, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
