---
type: Procedure
title: Final Report (One-Month Technical Closure)
description: Final comprehensive post-remediation report submitted within one month under Article 14(2)(e) and (4)(e) of Regulation (EU) 2024/2847.
category: procedure
tags: [cra, reporting, final-report, one-month, article-14, procedure]
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
  provision: Article 14(2)(d), Article 14(4)(c)
  applies_from: 2026-09-11
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

The final report is the concluding submission of the Article 14 reporting procedure. Under Regulation (EU) 2024/2847, the statutory deadline depends on whether the submission concerns an actively exploited vulnerability or a severe incident:
- **Actively Exploited Vulnerabilities (Article 14(2)(d)):** Due no later than **14 days** after a corrective or mitigating measure is available (or upon closure of handling if no measure is available).
- **Severe Incidents (Article 14(4)(c)):** Due within **1 month** after submission of the 72-hour incident notification.[^cra-art-14] [^enisa-srp-docs]

# Legal effect

Concludes the mandatory notification lifecycle for the specific vulnerability or incident and provides final documentation for CSIRT and ENISA repository records.[^cra-art-14]

# Applicability

Mandatory for all reported actively exploited vulnerabilities and severe incidents under Article 14.[^cra-art-14]

# Requirements or coverage

Under Article 14(2)(d) and 14(4)(c), the final report must contain:

1. **Complete technical description:** Root cause, vulnerability mechanics (CVE/CWE IDs), affected components, and attack vectors;
2. **Exploitation data:** Confirmed severity rating, known real-world exploitation extent, and threat actor details if attributable;
3. **Corrective measures deployed:** Release versions containing security updates, download links, hashes, and deployment statistics;
4. **Impact summary:** Total assessed impact on users, cross-border effects, and downstream supply chains;
5. **Lessons learned & preventive measures:** Internal process or architectural changes implemented to prevent recurrence.[^cra-art-14] [^enisa-srp-docs]

# Dates and transitions

- Applies from 11 September 2026.

# Related concepts

- [Article 14 Reporting Overview](article-14-reporting.md)
- [Early Warning (24h)](early-warning-24h.md)
- [Vulnerability Notification (72h)](vulnerability-notification-72h.md)
- [SRP Routing & Dissemination](srp-routing-and-dissemination.md)

[^cra-art-14]: Regulation (EU) 2024/2847, Article 14, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
[^enisa-srp-docs]: ENISA, Single Reporting Platform Documentation, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
