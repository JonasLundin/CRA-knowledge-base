---
type: Legal Instrument
title: Directive (EU) 2024/2853 (Product Liability Directive Recast)
description: Union strict civil liability regime for defective products including software, establishing civil liability consequences for CRA cybersecurity non-compliance and unpatched vulnerabilities.
category: law
tags: [cra, pld, product-liability, software-liability, defectiveness, civil-redress]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-08-21T00:00:00Z
sources:
  - id: dir-2024-2853
    resource: http://data.europa.eu/eli/dir/2024/2853/oj/eng
    title: Directive (EU) 2024/2853 on liability for defective products and repealing Council Directive 85/374/EEC
    author: European Parliament and Council
    last_modified: 2024-11-18T00:00:00Z
  - id: cra-art-13
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
    title: Regulation (EU) 2024/2847, Article 13
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-art-22
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_22
    title: Regulation (EU) 2024/2847, Article 22
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  celex: 32024L2853
  eli: http://data.europa.eu/eli/dir/2024/2853/oj/eng
  relevant_cra_provisions:
    - Article 13
    - Article 22
    - Annex I
    - Recital 17
    - Recital 40
  applicability: concurrent_civil_liability_regime
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Directive (EU) 2024/2853 recasts the Union's strict (no-fault) product liability regime, replacing Directive 85/374/EEC to explicitly incorporate software, digital services, and artificial intelligence into the definition of 'product' and covering modern digital harms such as the destruction or corruption of data.[^dir-2024-2853] While the Cyber Resilience Act sets ex-ante administrative and market access requirements, Directive (EU) 2024/2853 establishes ex-post civil compensation mechanisms where cybersecurity defects cause damage to natural persons.[^dir-2024-2853][^cra-art-13]

# Interaction and scope relationship

The relationship between the revised Product Liability Directive (PLD) and the CRA is complementary across the ex-ante / ex-post regulatory spectrum:
- **CRA:** Public administrative law setting baseline cybersecurity, technical documentation, CE marking, and vulnerability management duties enforced by market surveillance authorities.[^cra-art-13]
- **PLD Recast:** Private civil law setting strict no-fault liability for manufacturers where a defective digital product causes personal injury, property damage, or loss/corruption of data to individuals.[^dir-2024-2853]

# When the instrument applies

Directive (EU) 2024/2853 applies whenever:
- A defective product—explicitly including software (standalone, embedded, operating systems, apps) and digital files—causes harm to an individual within the Union;[^dir-2024-2853]
- Damage includes death, personal injury (including medically recognised psychological harm), destruction or corruption of personal data, or damage to property;[^dir-2024-2853]
- An injured party claims compensation from the manufacturer, importer, authorised representative, fulfilment service provider, or person who substantially modified the product.[^dir-2024-2853]

# Exclusion or concurrency with CRA

The two regimes apply concurrently. Compliance with the CRA does not automatically shield a manufacturer from civil liability under the PLD if a product is nevertheless proven defective in court; conversely, non-compliance with the CRA creates powerful evidentiary presumptions of defectiveness under the PLD.[^dir-2024-2853]

# Technical or procedural satisfaction of CRA elements

1. **Cybersecurity compliance as evidence in defect assessment:** Under PLD Article 7, courts determining whether a product is defective evaluate whether it provides the safety a person is entitled to expect, taking into account relevant safety and cybersecurity requirements under Union law (specifically including CRA Annex I essential requirements and manufacturer software update obligations under CRA Article 13).[^dir-2024-2853][^cra-art-13]
2. **Failure to supply security updates:** Under PLD Article 7(2)(e), a failure to provide cybersecurity software updates necessary to address emerging vulnerabilities during the product's expected lifetime/support period can constitute product defectiveness.[^dir-2024-2853]
3. **Rebuttable presumption of defectiveness:** Under PLD Article 9, where a plaintiff demonstrates that the manufacturer failed to comply with mandatory Union safety or cybersecurity requirements (such as CRA Annex I or CRA Article 13 update duties), the product is presumed defective unless the manufacturer proves otherwise.[^dir-2024-2853]
4. **Substantial modification liability alignment:** Both PLD Article 8 and CRA Article 22 align on the rule that any person who substantially modifies a product with digital elements after it has been placed on the market assumes the legal liabilities and obligations of a manufacturer.[^dir-2024-2853][^cra-art-22]

# Relevant provisions

- **Directive (EU) 2024/2853:** Article 4 (Definitions: product including software, damage including data loss), Article 6 (Defectiveness standard), Article 7 (Factors in assessing defectiveness), Article 8 (Liable economic operators), Article 9 (Disclosure of evidence and presumptions of defectiveness), Article 10 (Presumption of causal link).[^dir-2024-2853]
- **Regulation (EU) 2024/2847:** Article 13 (Obligations of manufacturers / support period and updates), Article 22 (Substantial modification), Annex I (Essential cybersecurity requirements), Recitals 17, 40.[^cra-art-13][^cra-art-22]

# Dates and transition

- Directive (EU) 2024/2853 entered into force on 8 December 2024; Member States must transpose it into national law by 9 December 2026.[^dir-2024-2853]
- Replaces Council Directive 85/374/EEC for products placed on the market after the transposition deadline, interacting with CRA obligations from day one.[^dir-2024-2853]

# Related concepts

- [Directive (EU) 2020/1828 (Representative Actions)](dir-2020-1828-representative-actions.md)
- [Manufacturer Obligations](../../../obligations/manufacturers/index.md)
- [CRA Article 13: Obligations of Manufacturers](../cra/articles/article-13.md)
- [CRA Article 22: Substantial Modification](../cra/articles/article-22.md)

[^dir-2024-2853]: Directive (EU) 2024/2853, http://data.europa.eu/eli/dir/2024/2853/oj/eng
[^cra-art-13]: Regulation (EU) 2024/2847, Article 13, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
[^cra-art-22]: Regulation (EU) 2024/2847, Article 22, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_22
