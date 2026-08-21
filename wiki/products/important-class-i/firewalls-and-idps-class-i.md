---
type: Product Category
title: Firewalls and Intrusion Detection Systems (Class I)
description: Consumer, SOHO, and host-based firewalls and intrusion detection/prevention systems not covered by Class II under Annex III Class I of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-i, firewalls, idps, intrusion-detection, network-security]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-annex-3
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
    title: Regulation (EU) 2024/2847, Annex III
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-art-32
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_32
    title: Regulation (EU) 2024/2847, Article 32
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: reg-2025-2392
    resource: http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
    title: Commission Implementing Regulation (EU) 2025/2392 on Technical Descriptions
    author: European Commission
    last_modified: 2025-11-15T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Annex III Class I, Article 32(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Annex III Class I covers firewalls, intrusion detection systems (IDS), and intrusion prevention systems (IPS) designed for consumer, small office, home office (SOHO), or general desktop use not meeting the industrial/critical criteria of Class II.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Subject to Class I conformity assessment under Article 32(2) to ensure packet inspection filters, rulesets, and signature update feeds do not introduce remote bypass vulnerabilities.[^cra-art-32]

# Applicability

Applies to:
- Host-based personal firewalls and desktop intrusion detection software;
- Consumer broadband router firewall sub-modules;
- SOHO firewall appliances without industrial certification.[^reg-2025-2392]

# Requirements or coverage

- **Conformity assessment route:** Module A (with full application of cited harmonised standards) or third-party Module B+C / Module H (Article 32(2));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 36 (ETSI EN 304-636);
- **Filtering integrity:** Secure rule distribution channels, fail-secure default behavior, and resilience against state exhaustion (DoS) attacks.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Firewalls & IDPS (Class II)](../important-class-ii/firewalls-and-idps.md)
- [Routers, Modems & Switches (Class I)](routers-modems-switches.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
