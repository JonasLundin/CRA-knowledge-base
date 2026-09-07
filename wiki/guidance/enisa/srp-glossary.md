---
type: Official Guidance
title: ENISA CRA Single Reporting Platform (SRP) Glossary
description: Standardized taxonomy, terminology, and 43 operational data fields required for notifications under the CRA Single Reporting Platform.
category: guidance
tags: [cra, guidance, enisa, srp, glossary, fields, taxonomy, reporting-data]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-09-07T00:00:00Z }
stale_after: 2026-12-07T00:00:00Z
sources:
  - id: enisa-srp-glossary
    resource: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/cra-srp-glossary
    title: CRA SRP Glossary
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2026-09-05T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2026-09-05
  relevant_provisions:
    - Article 14
    - Article 16
  language: en
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

ENISA's *CRA SRP Glossary* establishes the official terminology, data dictionary, and technical field definitions governing notifications of actively exploited vulnerabilities and severe incidents submitted through the Single Reporting Platform (SRP) [^enisa-srp-glossary].

# Legal effect

This guidance is non-binding and operational [^enisa-srp-glossary]. It defines the specific data structure and field validations required to satisfy the notification obligations under Article 14 of Regulation (EU) 2024/2847.

# Applicability

Applies to manufacturers, Assigned Representatives, CSIRTs designated as coordinators, and security researchers preparing submissions for the Single Reporting Platform.

# Key topics or guidance coverage

The glossary (Version 1.1, 5 September 2026) specifies **43 standardized data fields** divided into three groups across the Early Warning (24h), Notification (72h), and Final Report stages [^enisa-srp-glossary]:

### 1. Common Notification Fields (Fields 1 to 23)
Mandatory or conditional fields shared across both vulnerability and incident reporting:
- **Notification Type (Field 1):** Specifies whether the submission relates to an Actively Exploited Vulnerability (AEV) or a Severe Incident (SI).
- **Notification Level (Field 2):** Current stage (`24h Early Warning`, `72h Notification`, or `Final Report`).
- **Reporting Times & Timestamps (Fields 3–5):** Automated system timestamps recording the submission time for the 24h, 72h, and Final stages.
- **Reporter Details (Field 6):** Automated metadata identifying the submitting Assigned Representative and user EU Login ID.
- **Title & Summary (Fields 7–8):** High-level descriptive heading and human-readable factual abstract of the vulnerability or incident.
- **Manufacturer Identification (Field 9):** Legal entity name, registration identifier, and contact credentials.
- **Member States Concerned (Field 10):** Selection of EU Member States where the affected product is known to be made available on the market.
- **Product Identification (Fields 11–14):** Commercial product name, version/model/family, general product description, and standardized identifiers (Common Platform Enumeration - CPE, Package URL - PURL, hardware part numbers, or serial numbers).
- **Third-Party Components (Field 15):** Details on whether the vulnerability resides in an upstream open-source or commercial integrated component.
- **Lead CSIRT Determination (Fields 16–18):** Specification of the lead CSIRT designated as coordinator (CDaC) based on establishment within the Union or the non-EU hierarchy.
- **Particular Exceptional Circumstances (PEC) & Dissemination Delay (Field 19):** Checkbox and written justification invoking grounds under Article 16(2) and Delegated Regulation (EU) 2026/881. When flagged, access by ENISA and non-lead CSIRTs is restricted.
- **Contact & Coordination Channels (Fields 20–23):** Technical contact points, secondary coordinators, and external reference tickets.

### 2. Actively Exploited Vulnerability Specific Fields (Fields v24 to v34)
Required for AEV submissions to characterize exploitation and remediation:
- **Vulnerability Identifiers (Fields v24–v25):** Common Vulnerabilities and Exposures (CVE) ID or Common Weakness Enumeration (CWE) identifier.
- **Severity Scoring (Field v26):** CVSS vector string and base numerical score.
- **Exploitation Telemetry (Fields v27–v28):** Description of observed exploitation activity, indicators of compromise (IoCs), and threat actor attribution where available.
- **Corrective & Mitigating Measures (Fields v29–v31):** Workarounds, temporary configuration guidance, patch availability date, release versions, and download verification hashes.
- **Remediation Timeline (Fields v32–v34):** Expected date of patch availability and confirmation of user security advisory publication.

### 3. Severe Incident Specific Fields (Fields i35 to i43)
Required for incident submissions to evaluate operational and societal impact:
- **Incident Categorisation (Field i35):** Classification according to incident type (e.g., denial of service, unauthorized access, integrity violation).
- **Operational Impact (Field i36):** Nature and scale of operational disruption caused to the product or its connected ecosystems.
- **Damage Assessment (Fields i37–i38):** Material or non-material damages incurred by users, and impact on essential services under NIS2 (Directive (EU) 2022/2555).
- **Attack Vector & Root Cause (Fields i39–i40):** Probable trigger mechanism, exploited vulnerability, or supply chain vector.
- **Mitigation & Containment (Fields i41–i43):** Containment measures taken, user guidance issued, and final incident resolution status.

# Dates and transitions

- **First Published:** 5 September 2026 (Version 1.1).
- **Operational Application:** Enforced as standard validation schema on the SRP from 11 September 2026.

# Related concepts

- [Single Reporting Platform (SRP)](./single-reporting-platform.md)
- [SRP FAQ](./srp-faq.md)
- [SRP Notification Submission and Updates](./srp-notification-submission-and-updates.md)
- [SRP Interface Guidance](./srp-interface-guidance.md)
- [CSIRTs Designated as Coordinators](./srp-csirt-coordinators.md)
- [Article 14 Reporting Overview](../../obligations/reporting/article-14-reporting.md)

[^enisa-srp-glossary]: European Union Agency for Cybersecurity (ENISA), CRA SRP Glossary, https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/cra-srp-glossary
