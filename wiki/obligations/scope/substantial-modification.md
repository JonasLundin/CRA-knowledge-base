---
type: Requirement
title: Substantial Modification under the Cyber Resilience Act
description: Criteria determining when a hardware or software change constitutes a substantial modification triggering manufacturer obligations under Article 3(32) and Article 18.
category: requirement
tags: [cra, substantial-modification, compliance, manufacturer-duties]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-3
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
    title: Regulation (EU) 2024/2847, Article 3
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-art-13
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
    title: Regulation (EU) 2024/2847, Article 13
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-art-18
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_18
    title: Regulation (EU) 2024/2847, Article 18
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: ec-guidance-5252
    resource: https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
    title: Commission Guidance C(2026) 5252 on CRA Implementation
    author: European Commission
    last_modified: 2026-06-30T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 3(32), Article 18
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Under Article 3(32) of Regulation (EU) 2024/2847, a substantial modification is a change made to a product with digital elements after its placing on the market that affects its compliance with Annex I essential cybersecurity requirements or alters its intended purpose.[^cra-art-3]

# Legal effect

Any natural or legal person (including a distributor, importer, integrator, or user) who carries out a substantial modification is deemed a manufacturer under Article 18 and becomes subject to all manufacturer obligations under Article 13 for the modified part or the entire product.[^cra-art-18]

# Applicability

A modification is deemed substantial when:
1. It alters the intended purpose or operating environment of the product in a way not foreseen in the original risk assessment; or
2. It introduces new cybersecurity risks or significantly increases existing risks affecting compliance with Annex I; and
3. The risk cannot be mitigated by measures already defined in the original technical documentation.[^cra-art-3] [^ec-guidance-5252]

### Changes that are NOT substantial modifications
- **Security updates:** Routine security patches and bug fixes intended to eliminate vulnerabilities without altering functionality or performance;[^cra-art-13]
- **Minor software updates:** Maintenance updates that remain within the assessed intended purpose and do not degrade cybersecurity properties;
- **User configurations:** Standard configuration options documented and provided by the original manufacturer.[^ec-guidance-5252]

# Requirements or coverage

When a substantial modification occurs, the person making the modification must:
1. Carry out a fresh cybersecurity risk assessment;
2. Update the technical documentation and Software Bill of Materials (SBOM);
3. Perform the applicable conformity assessment procedure;
4. Draw up a new EU declaration of conformity and affix the CE marking if necessary.[^cra-art-18]

# Dates and transitions

- Effective from 11 December 2027.
- Applies to legacy products placed on the market before 11 December 2027 if they undergo a substantial modification after that date (Article 69(2)).[^cra-art-18]

# Related concepts

- [Manufacturer Role & Obligations](../manufacturers/manufacturer.md)
- [Modification and Rebranding](../importers-and-distributors/modification-and-rebranding.md)
- [Transitional Rules](transitional-rules.md)
- [Security Updates](../manufacturers/security-updates.md)

[^cra-art-3]: Regulation (EU) 2024/2847, Article 3, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^cra-art-18]: Regulation (EU) 2024/2847, Article 18, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_18
[^ec-guidance-5252]: European Commission, Commission Guidance C(2026) 5252 on CRA Implementation, https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
