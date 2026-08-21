---
type: Procedure
title: Early Warning (24-Hour Notification)
description: First-stage mandatory notification submitted to the Single Reporting Platform within 24 hours under Article 14(2)(a) and (4)(a) of Regulation (EU) 2024/2847.
category: procedure
tags: [cra, reporting, early-warning, 24h, article-14, procedure]
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
  provision: Article 14(2)(a), Article 14(4)(a)
  applies_from: 2026-09-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

The early warning is the first mandatory step in the Article 14 reporting procedure. Manufacturers must submit an early warning through the Single Reporting Platform within 24 hours of becoming aware of an actively exploited vulnerability or severe incident.[^cra-art-14] [^enisa-srp-docs]

# Legal effect

Failing to submit the early warning within the 24-hour window constitutes a direct breach of statutory reporting obligations under Article 14.[^cra-art-14]

# Applicability

Applies whenever a manufacturer obtains credible evidence that:
- A vulnerability in its product is being actively exploited in the wild (Article 14(1)); or
- A severe incident is impacting the cybersecurity of its product (Article 14(3)).[^cra-art-14]

# Requirements or coverage

The early warning must contain concise preliminary facts and specify:

1. **Vulnerability trigger:** Whether the report concerns an actively exploited vulnerability or a severe incident;
2. **Product identification:** Product name, affected versions, and category;
3. **Suspected cause / exploitation:** Whether the exploitation is suspected of being caused by unlawful or malicious action;
4. **Cross-border impact:** Indications of whether the exploitation or incident has or could have a significant cross-border impact across Member States;
5. **Preliminary mitigation:** Any immediate emergency mitigations advised or deployed.[^cra-art-14]

# Dates and transitions

- Applies from 11 September 2026.

# Related concepts

- [Article 14 Reporting Overview](article-14-reporting.md)
- [Vulnerability Notification (72h)](vulnerability-notification-72h.md)
- [Severe Incident Notification (72h)](severe-incident-notification-72h.md)
- [SRP Routing & Dissemination](srp-routing-and-dissemination.md)

[^cra-art-14]: Regulation (EU) 2024/2847, Article 14, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
[^enisa-srp-docs]: ENISA, Single Reporting Platform Documentation, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
