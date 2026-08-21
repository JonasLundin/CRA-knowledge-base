---
type: Requirement
title: User Notification Obligations under CRA Article 14(8)
description: Duties to inform users of actively exploited vulnerabilities, severe incidents, and user-deployable corrective measures under Article 14(8).
category: requirement
tags: [cra, user-notifications, incident-response, consumer-protection, security-advisory]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-14
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
    title: Regulation (EU) 2024/2847, Article 14
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: ec-cra-faq
    resource: https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
    title: Cyber Resilience Act Implementation Frequently Asked Questions
    author: European Commission
    last_modified: 2026-01-15T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 14(8)
  applies_from: 2026-09-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Under Article 14(8) of Regulation (EU) 2024/2847, manufacturers must inform affected users of actively exploited vulnerabilities or severe incidents and provide actionable guidance on corrective measures and mitigations that users can deploy.[^cra-art-14]

# Legal effect

Direct statutory obligation owed to product users and consumers. Market surveillance authorities and CSIRTs may instruct manufacturers to issue emergency user warnings if the manufacturer fails to act proactively.[^cra-art-14]

# Applicability

Applies to manufacturers of products with digital elements whenever an active exploitation or severe incident presents a direct security risk to users or their data.[^cra-art-14]

# Requirements or coverage

Manufacturers must:

1. **Direct user communication:** Inform users without undue delay through appropriate communication channels (e.g. in-app alerts, registered email, public security advisories);
2. **Actionable guidance:** Detail any necessary actions users must take, such as applying configuration changes, updating software, isolating network interfaces, or rotating credentials;
3. **Emergency mitigations:** Provide temporary workarounds if a full software patch is not yet available;
4. **Transparency without exploitation risk:** Formulate notices clearly without providing detailed exploit code or information that enables attackers to target unpatched instances.[^cra-art-14] [^ec-cra-faq]

# Dates and transitions

- Applies from 11 September 2026.

# Related concepts

- [Article 14 Reporting Overview](article-14-reporting.md)
- [Severe Incident Notification (72h)](severe-incident-notification-72h.md)
- [Security Updates](../manufacturers/security-updates.md)

[^cra-art-14]: Regulation (EU) 2024/2847, Article 14, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
[^ec-cra-faq]: European Commission, Cyber Resilience Act Implementation Frequently Asked Questions, https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
