---
type: Procedure
title: Intermediate Report (14-Day Status Update)
description: Intermediate progress report submitted upon request or within 14 days of corrective measure availability under Article 14(2)(c) of Regulation (EU) 2024/2847.
category: procedure
tags: [cra, reporting, intermediate-report, 14d, article-14, procedure]
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
  provision: Article 14(2)(c)
  applies_from: 2026-09-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Under Article 14(2)(c) of Regulation (EU) 2024/2847, the manufacturer must provide an intermediate report detailing remediation progress upon request of the designated CSIRT, or as soon as a corrective or mitigating measure is made available, and no later than 14 days following such measure.[^cra-art-14] [^enisa-srp-docs]

# Legal effect

Ensures that authorities receive timely technical updates when long vulnerability remediation cycles exceed the initial 72-hour notification window.[^cra-art-14]

# Applicability

Applies to actively exploited vulnerability investigations where remediation is ongoing or when requested by the lead CSIRT coordinator.[^cra-art-14]

# Requirements or coverage

The intermediate report must provide:

1. **Remediation status:** Status of patch development, testing, and distribution;
2. **Mitigation details:** Full description of interim workarounds or mitigations made available to users;
3. **Exploitation evolution:** Updates on threat intelligence, active exploitation attempts, or newly identified affected versions;
4. **Target release date:** Estimated timeline for general patch release and final report submission.[^cra-art-14] [^enisa-srp-docs]

# Dates and transitions

- Applies from 11 September 2026.

# Related concepts

- [Article 14 Reporting Overview](article-14-reporting.md)
- [Vulnerability Notification (72h)](vulnerability-notification-72h.md)
- [Final Report (1 Month)](final-report-one-month.md)

[^cra-art-14]: Regulation (EU) 2024/2847, Article 14, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
[^enisa-srp-docs]: ENISA, Single Reporting Platform Documentation, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
