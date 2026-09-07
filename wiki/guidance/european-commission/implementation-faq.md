---
type: Official Guidance
title: European Commission CRA Implementation FAQ
description: Official frequently asked questions and answers published by the European Commission clarifying practical aspects of Cyber Resilience Act compliance.
category: guidance
tags: [cra, guidance, european-commission, faq, implementation, scope, conformity]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: ec-cra-faq
    resource: https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
    title: Cyber Resilience Act Implementation - Frequently Asked Questions
    author: European Commission
    last_modified: 2026-09-04T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: European Commission - DG CNECT
  authority_level: non_binding
  document_status: published
  publication_date: 2025-12-01
  relevant_provisions:
    - Article 2
    - Article 3
    - Article 11
    - Article 12
    - Article 13
    - Article 14
    - Article 24
    - Article 27
    - Article 32
    - Annex III
    - Annex IV
  language: en
  checked_at: 2026-09-07T00:00:00Z
---

# Summary

The European Commission's *Cyber Resilience Act Implementation - Frequently Asked Questions* is a dynamic reference document addressing practical questions raised by manufacturers, developers, open-source communities, and national authorities [^ec-cra-faq]. Updated to **Version 1.4 on 4 September 2026**, the FAQ provides official clarifications on scope thresholds, economic operator roles, interaction with other EU legislation, conformity assessment pathways, and reporting obligations.

# Legal effect

The answers provided in the FAQ are non-binding and intended solely for informational purposes [^ec-cra-faq]. They do not substitute for or modify the legal provisions of Regulation (EU) 2024/2847.

# Applicability

Applicable to developers, manufacturers, importers, distributors, open-source software stewards, and notified bodies navigating the implementation phase of the CRA.

# Key topics or guidance coverage

Version 1.4 structures official clarifications across seven thematic chapters [^ec-cra-faq]:

1. **Chapter 1: Scope:**
   - Stand-alone software/firmware and products with direct or indirect logical/physical data connections to devices or networks.
   - Products placed on the market before 11 December 2027 (grandfathering boundary under Article 69).
   - Exemptions for products developed exclusively for own internal use without commercial supply.
   - Pre-market test/prototype versions, software archives preserving older releases, and exclusions for national security, defence, and military purposes.
2. **Chapter 2: Interplay with Other Legislation:**
   - Specific sector legislation: Civil Aviation Regulation (EU) 2018/1139 and Marine Equipment Directive 2014/90/EU.
   - New product safety and liability frameworks: Product Liability Directive (EU) 2024/2853, Machinery Regulation (EU) 2023/1230, and General Product Safety Regulation (EU) 2023/988.
   - Radio Equipment Directive (RED) 2014/53/EU and Delegated Regulation (EU) 2022/30 transition.
   - Data and health frameworks: European Health Data Space (EHDS) Regulation (EU) 2025/327, GDPR (EU) 2016/679, and Data Act (EU) 2023/2854.
3. **Chapter 3: Important and Critical Products:**
   - Classification principles based on core cybersecurity functionalities (Annex III & IV).
   - Impact of integration into higher-risk environments and manufacturer risk assessments.
4. **Chapter 4: Manufacturer Obligations:**
   - Cybersecurity risk assessment methodology and documentation throughout the product lifecycle.
   - Essential cybersecurity requirements under Annex I Part I (security-by-default, access control, integrity, minimization).
   - Vulnerability handling requirements under Annex I Part II, coordinated vulnerability disclosure policies, and contact endpoints.
   - Due diligence obligations when integrating third-party components (commercial and open source) without CE markings.
   - Objective criteria for determining support period duration based on user expectations and product nature.
5. **Chapter 5: Reporting Obligations:**
   - Awareness thresholds and internal telemetry triggering the 24-hour early warning under Article 14.
   - Clarifications on reporting zero-day vulnerabilities and exploitation indicators.
   - Reporting duties for products placed on the market prior to CRA general applicability that remain in use and maintained.
   - Handling actively exploited vulnerabilities discovered in integrated third-party components.
   - Reporting timeline for open-source software stewards under Article 24(3), which applies from 11 December 2027 (unlike manufacturer Article 14 reporting applying 11 September 2026).
6. **Chapter 6: Conformity Assessment:**
   - Permissible conformity assessment modules: Internal control (Module A), EU-type examination (Module B+C), and Full quality assurance (Module H).
   - Technical documentation file requirements, EU Declaration of Conformity drafting, and CE marking rules.
   - Role of notified bodies, accreditation timelines, and the interim use of harmonised standards and common specifications.
7. **Chapter 7: Transition Period:**
   - Application calendar: Article 14 reporting applying 11 September 2026; general CRA provisions applying 11 December 2027.
   - Continued production of existing types and component integration without CE marking during transition.
   - Verification duties incumbent on distributors and importers during the transition window.

# Dates and transitions

- **Initial Publication:** December 2025.
- **Latest Document Update:** 4 September 2026 (Version 1.4).
- **Official Formats:** Published by the Commission in web format, Markdown document redirection, and PDF.
- **Maintenance Model:** The Commission updates and expands the FAQ on an ongoing basis as new implementing acts and standards progress.

# Related concepts

- [Commission Guidance C(2026) 5252](./c-2026-5252-cra-guidance.md)
- [Implementation Hub](./implementation-hub.md)
- [Open Source Guidance](./open-source-guidance.md)
- [Article 14 Reporting Overview](../../obligations/reporting/article-14-reporting.md)

[^ec-cra-faq]: European Commission, Cyber Resilience Act Implementation - Frequently Asked Questions, https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions
