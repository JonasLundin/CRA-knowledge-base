---
type: Product Category
title: Operating Systems (Class I)
description: Operating systems not covered by Class II (such as specialized, embedded, or appliance OSs) under Annex III Class I point 11 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-i, operating-systems, embedded-os, rtos]
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
  provision: Annex III Class I point 11, Article 32(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 11 of Annex III Class I covers operating systems not covered by Class II, including specialized, real-time (RTOS), and embedded operating systems.[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Operating systems in Class I must satisfy Article 32(2) conformity assessment requirements, implementing core kernel isolation, memory protection, and secure update capabilities.[^cra-art-32]

# Applicability

Applies to:
- Real-Time Operating Systems (RTOS) used in consumer and commercial appliances;
- Embedded Linux and specialized microkernel operating systems not classified under Class II (general-purpose server/desktop/mobile OSs belong in Class II);
- Hypervisors and container base OS distributions.[^reg-2025-2392]

# Requirements or coverage

- **Conformity assessment route:** Module A (with full application of cited harmonised standards) or third-party Module B+C / Module H (Article 32(2));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 26 (ETSI EN 304-626);
- **Security architecture:** Address Space Layout Randomization (ASLR), kernel memory isolation, privilege separation, and signed kernel modules.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Operating Systems (Class II)](../important-class-ii/operating-systems-class-ii.md)
- [Boot Managers](boot-managers.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
