---
type: Requirement
title: Product Scope of the Cyber Resilience Act
description: Scope of application covering products with digital elements made available on the EU market under Article 2(1) of Regulation (EU) 2024/2847.
category: requirement
tags: [cra, scope, applicability, products]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-2
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
    title: Regulation (EU) 2024/2847, Article 2
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
  provision: Article 2(1)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Regulation (EU) 2024/2847 applies to all products with digital elements made available on the European Union market whose intended purpose or reasonably foreseeable use includes a direct or indirect logical or physical data connection to a device or network.[^cra-art-2]

# Legal effect

Article 2(1) establishes the general horizontal scope of the Cyber Resilience Act. Products within scope must satisfy the essential cybersecurity requirements set out in Annex I before they are placed on the market or made available in the EU.[^cra-art-2]

# Applicability

The scope covers both hardware and software products:

- Standalone software applications, firmware, and operating systems;
- Hardware devices with embedded digital components (smart devices, IoT, network equipment, computing systems);
- Remote data processing solutions designed and developed by or on behalf of the manufacturer, without which the product cannot perform one of its primary functions;
- Components placed on the market separately as individual products intended for integration into other products with digital elements.[^cra-art-2] [^ec-cra-faq]

# Requirements or coverage

To be in scope, a product must meet three cumulative criteria:

1. It is a product with digital elements (software or hardware and its remote data processing solutions);
2. It has or can have a direct or indirect data connection to a device or network;
3. It is made available on the EU market in the course of a commercial activity.[^cra-art-2]

Products are classified into default products, important products (Class I and Class II), or critical products, which determines the required conformity assessment procedure.

# Dates and transitions

- Entry into force: 10 December 2024
- General application date: 11 December 2027 (Article 71(2))
- Transitional provisions for legacy products apply under Article 69.[^cra-art-2]

# Related concepts

- [Sectoral Exclusions](exclusions.md)
- [Remote Data Processing Solutions](remote-data-processing.md)
- [Commercial Activity Test](commercial-activity.md)
- [Default Products with Digital Elements](../../products/default/default-products.md)
- [General Application Date](../../timeline/main-application-date.md)

[^cra-art-2]: Regulation (EU) 2024/2847, Article 2, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_2
[^ec-cra-faq]: European Commission, Cyber Resilience Act Implementation Frequently Asked Questions, https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
