---
type: Product Category
title: Personal Wearables with Health and Location Tracking
description: Smartwatches and wearable devices tracking health metrics or geolocation under Annex III Class I point 17 of Regulation (EU) 2024/2847.
category: product
tags: [cra, product-category, important-class-i, wearables, smartwatches, health-tracking, iot]
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
  provision: Annex III Class I point 17, Article 32(2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Point 17 of Annex III Class I designates personal wearable products with health monitoring (e.g. pulse, ECG, sleep, vital signs) or geolocation tracking (e.g. GPS fitness trackers, smartwatches) as Important Products (Class I).[^cra-annex-3] [^reg-2025-2392]

# Legal effect

Wearables outside medical device scope (MDR) must undergo Class I conformity assessment under Article 32(2) to safeguard biometric telemetry, location data, and BLE/cellular connectivity.[^cra-art-32]

# Applicability

Applies to:
- Smartwatches and connected fitness bands;
- Wearable GPS trackers and smart rings;
- Wearable biosensors for general wellness not qualifying as medical devices under Regulation (EU) 2017/745.[^reg-2025-2392]

# Requirements or coverage

- **Conformity assessment route:** Module A (with full application of cited harmonised standards) or third-party Module B+C / Module H (Article 32(2));[^cra-art-32]
- **Relevant vertical standards:** M/606 line 34 (ETSI EN 304-634);
- **Data protection & interface security:** Encrypted local storage for biometric data, secure Bluetooth LE bonding, anti-tracking protection (MAC address randomization), and secure companion cloud backends.

# Dates and transitions

- Article 14 reporting applies from 11 September 2026.
- Full product conformity applies from 11 December 2027.

# Related concepts

- [Sectoral Exclusions (Medical Devices)](../../obligations/scope/exclusions.md)
- [Internet-Connected Toys](internet-connected-toys.md)
- [Conformity Assessment Routes](../../obligations/conformity-assessment/conformity-routes.md)

[^cra-annex-3]: Regulation (EU) 2024/2847, Annex III, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_3
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
[^reg-2025-2392]: Commission Implementing Regulation (EU) 2025/2392, http://data.europa.eu/eli/reg_impl/2025/2392/oj/eng
