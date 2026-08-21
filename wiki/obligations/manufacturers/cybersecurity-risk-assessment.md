---
type: Requirement
title: Cybersecurity Risk Assessment under the Cyber Resilience Act
description: Manufacturer duty to assess cybersecurity risks, threats, and operational environments under Article 13(2) and Annex I of Regulation (EU) 2024/2847.
category: requirement
tags: [cra, risk-assessment, threat-modelling, essential-requirements, design]
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
  provision: Article 13(2), Annex I Part I
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Article 13(2) mandates that manufacturers carry out a comprehensive cybersecurity risk assessment during the planning, design, development, production, delivery, and maintenance phases of a product with digital elements.[^cra-art-13]

# Legal effect

The risk assessment serves as the foundation for product compliance. It dictates how Annex I Part I essential cybersecurity requirements are applied, justifies any trade-offs or design decisions, and forms an indispensable component of the technical documentation under Annex VII.[^cra-art-13] [^cra-annex-1]

# Applicability

Applies to all manufacturers placing products with digital elements on the EU market, irrespective of whether the product is a default, important, or critical product.[^cra-art-13]

# Requirements or coverage

The cybersecurity risk assessment must:

1. **Cover the entire lifecycle:** Address risks from initial architecture through deployment and the declared support period;
2. **Consider intended purpose and foreseeable use:** Evaluate operational contexts, intended user environments, and foreseeable misconfigurations or abuse;
3. **Assess remote data processing:** Include any cloud backends or companion processing endpoints under the manufacturer's control;
4. **Evaluate component risks:** Analyze risks originating from integrated third-party hardware and software components;
5. **Dynamic updates:** Be updated whenever new vulnerabilities, threat vectors, or architectural changes occur during the product support period.[^cra-art-13] [^cra-annex-1]

# Dates and transitions

- Applies from 11 December 2027.

# Related concepts

- [Manufacturer Role & Duties](manufacturer.md)
- [Third-Party Components Due Diligence](third-party-components.md)
- [Technical Documentation](technical-documentation.md)
- [Remote Data Processing Solutions](../scope/remote-data-processing.md)

[^cra-art-13]: Regulation (EU) 2024/2847, Article 13, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
[^cra-annex-1]: Regulation (EU) 2024/2847, Annex I, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_1
