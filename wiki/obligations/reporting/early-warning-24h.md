---
type: Procedure
title: Early Warning (24-Hour Notification)
description: First-stage mandatory notification submitted to the Single Reporting Platform within 24 hours of becoming aware under Article 14(2)(a) and (4)(a) of Regulation (EU) 2024/2847.
category: procedure
tags: [cra, reporting, early-warning, 24h, article-14, procedure, awareness, triggers, telemetry]
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
  - id: ec-c-2026-5252
    resource: https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
    title: Commission Communication C(2026) 5252 final - Guidelines on the application of Regulation (EU) 2024/2847
    author: European Commission
    last_modified: 2026-07-27T00:00:00Z
  - id: ec-cra-faq
    resource: https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
    title: Cyber Resilience Act Implementation - Frequently Asked Questions (v1.4)
    author: European Commission
    last_modified: 2026-09-04T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 14(2)(a), Article 14(4)(a)
  applies_from: 2026-09-11
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

The early warning is the first mandatory step in the Article 14 reporting procedure. Manufacturers must submit an early warning through the Single Reporting Platform (SRP) within **24 hours of becoming aware** of an actively exploited vulnerability or a severe incident [^cra-art-14] [^enisa-srp-docs].

# Legal effect

Failing to submit the early warning within the 24-hour statutory window constitutes a direct breach of reporting obligations under Article 14, enforceable from 11 September 2026 and subject to administrative fines under Article 64 [^cra-art-14].

# Applicability and Awareness Thresholds

The 24-hour clock begins the moment the manufacturer achieves a **"sufficient degree of certainty" (verified knowledge)** that an actively exploited vulnerability or severe incident affects its product, rather than at the completion of root-cause investigation or patch development [^ec-c-2026-5252] [^ec-cra-faq].

### 1. Actively Exploited Vulnerabilities (Articles 3(42) & 14(1))
The statutory reporting trigger requires **reliable evidence** that execution of malicious code was performed by an actor on a system without permission of the system owner [^cra-art-14]:
- **Positive Awareness Triggers:**
  - *Internal Telemetry & Monitoring:* Production telemetry, SIEM alerts, or EDR detections confirming unauthorized exploitation of the product in the wild.
  - *Verified External Reports:* Substantiated notifications from users, CSIRTs, security researchers, or threat intelligence feeds providing proof of real-world exploitation, active threat-actor campaigns, or indicators of compromise (IoCs).
  - *Third-Party Components:* For integrated open-source or commercial libraries, awareness is triggered **only if** the vulnerability is *reachable and exploitable* within the manufacturer's product and actively exploited in that operational context [^ec-c-2026-5252].
- **Negative Exclusions (What Does NOT Trigger Awareness):**
  - *Good-Faith Testing / CVD (Recital 68):* Vulnerabilities discovered without malicious intent for testing, investigation, correction, or coordinated vulnerability disclosure (CVD) do not trigger reporting. Ethical hacking demonstrations and laboratory proof-of-concept (PoC) exploits are excluded [^cra-art-14].
  - *Static Scanners & CVE Bulletins:* Unverified automated vulnerability scan results, generic CVE publications, or theoretical bug bounty submissions without evidence of active exploitation.
  - *Triage Window:* The 24-hour clock starts upon completion of initial triage confirming credibility and product impact, not upon initial arrival of an unverified message in a generic mailbox [^ec-cra-faq]. Once verified, the clock runs continuously, including weekends and public holidays.

### 2. Severe Incidents (Articles 14(3) & 14(5))
The reporting trigger applies when the manufacturer has reason to believe that a security incident has occurred that meets **either** of the two statutory severity thresholds under Article 14(5) [^cra-art-14]:
- **Criterion (a) — Impact on Core Security Properties:** Negatively affects (or is capable of negatively affecting) the product's ability to protect the **availability, authenticity, integrity, or confidentiality** of sensitive or important data or functions; **or**
- **Criterion (b) — Malicious Code Propagation:** Has led (or is capable of leading) to the **introduction or execution of malicious code** in the product itself or in the network and information systems of a user.

# Requirements or coverage

The early warning is designed as a preliminary alert and must contain [^cra-art-14]:

1. **Notification Type:** Specification of whether the submission concerns an Actively Exploited Vulnerability (AEV) or a Severe Incident (SI);
2. **Product Identification:** Commercial name, version/model, and category of the affected product;
3. **Suspected Malicious Action:** Indication of whether the exploitation or incident is suspected of being caused by unlawful or malicious action;
4. **Cross-Border Impact:** Preliminary assessment of whether the exploitation or incident has caused or could cause significant cross-border impact across EU Member States;
5. **Immediate Mitigation:** Any emergency corrective measures or interim workarounds already deployed or recommended to users.

Root-cause analysis, complete technical disclosures, and vulnerability severity scores (CVSS) are **not** required at the 24-hour stage and are provided in the subsequent 72-hour notification.

# Dates and transitions

- **11 September 2026:** Article 14 reporting obligations apply across the Union (Article 71(2)(a)).

# Related concepts

- [Article 14 Reporting Overview](article-14-reporting.md)
- [Vulnerability Notification (72h)](vulnerability-notification-72h.md)
- [Severe Incident Notification (72h)](severe-incident-notification-72h.md)
- [Final Report (1 Month)](final-report-one-month.md)
- [SRP Routing & Dissemination](srp-routing-and-dissemination.md)
- [Actively Exploited Vulnerability](../../glossary/actively-exploited-vulnerability.md)
- [SRP Glossary](../../guidance/enisa/srp-glossary.md)

[^cra-art-14]: Regulation (EU) 2024/2847, Article 14, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_14
[^enisa-srp-docs]: ENISA, Single Reporting Platform Documentation, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp
[^ec-c-2026-5252]: European Commission, Guidelines on the application of Regulation (EU) 2024/2847 (C(2026) 5252 final), https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
[^ec-cra-faq]: European Commission, Cyber Resilience Act Implementation - Frequently Asked Questions, https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
