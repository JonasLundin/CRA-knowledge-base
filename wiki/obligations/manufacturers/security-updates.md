---
type: Requirement
title: Security Updates and Patch Management under the CRA
description: Mandatory provision of free security updates, automatic update mechanisms, and disaggregation from feature updates under Article 13(9), (14) and Annex I Part II.
category: requirement
tags: [cra, security-updates, patching, vulnerability-handling, lifecycle]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-13
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
    title: Regulation (EU) 2024/2847, Article 13
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-annex-1
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_1
    title: Regulation (EU) 2024/2847, Annex I
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 13(9), (14), Annex I Part II point (2)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) 2024/2847 establishes binding requirements on manufacturers to develop, provide, and distribute security updates free of charge for the entire duration of the declared support period.[^cra-art-13]

# Legal effect

Manufacturers are legally obligated to remediate vulnerabilities through security updates or patches without cost to users. Security updates must not bundle unwanted functional changes that degrade performance or force paid upgrades.[^cra-art-13]

# Applicability

Applies to all products with digital elements made available on the EU market throughout their active support period.[^cra-art-13]

# Requirements or coverage

1. **Free of charge:** Security updates must be supplied at no cost to users throughout the support period (Article 13(9));
2. **Disaggregation from feature updates:** Security updates must be clearly distinguished and provided separately from new functionality updates, ensuring users can apply security fixes without accepting feature modifications (Article 13(14));
3. **Automatic update capability:** Where technically feasible, products must support automatic security updates, enabled by default or easily configured, with clear options for users to deactivate, postpone, or schedule updates (Annex I Part II point (2));
4. **Advisories and transparency:** Every security update must be accompanied by an advisory explaining the vulnerabilities addressed, severity levels, and any user actions required (Article 13(10), (14));
5. **Post-support update transparency:** If a manufacturer provides a security update after the support period has expired, it must not introduce discriminatory terms.[^cra-art-13] [^cra-annex-1]

# Dates and transitions

- Applies from 11 December 2027.

# Related concepts

- [Manufacturer Role & Duties](manufacturer.md)
- [Support Period Determination](support-period.md)
- [Vulnerability Handling Requirements](../vulnerability-handling/vulnerability-handling-requirements.md)
- [Coordinated Vulnerability Disclosure](../vulnerability-handling/coordinated-vulnerability-disclosure.md)

[^cra-art-13]: Regulation (EU) 2024/2847, Article 13, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
[^cra-annex-1]: Regulation (EU) 2024/2847, Annex I, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_1
