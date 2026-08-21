---
type: Legal Provision
title: "CRA Annex I Part I: Security Requirements Relating to the Properties of Products with Digital Elements"
description: "Defines mandatory product-level security capabilities including default security, access control, data protection, and update mechanisms."
category: law
tags: ['cra', 'law', 'annex', 'annex-i', 'part-i', 'security-properties', 'security-by-design']
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-12-11T00:00:00Z
sources:
  - id: cra-annex-i-part-1
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_i_part_1
    title: Regulation (EU) 2024/2847, Annex I Part I
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Annex I Part I
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Annex I Part I establishes mandatory product-level design and engineering requirements ensuring hardware and software products are secure by design and default.

# Legal effect

Imposes mandatory design and architecture requirements verified through conformity assessment before CE marking.

# Applicability

Applies to all products with digital elements placed on the Union market.

# Requirements or coverage

Key requirements under Annex I Part I include:
1. **Absence of known exploitable vulnerabilities**: Products must be placed on the market without known exploitable flaws.
2. **Secure default configuration**: Secure out-of-the-box configuration, mandatory password changes, and ability to reset to a secure state.
3. **Access control and authentication**: Robust mechanisms preventing unauthorised access to functions, data, and interfaces.
4. **Data confidentiality and integrity**: Strong encryption for sensitive data in transit and at rest; protection against tampering and corrupt states.
5. **Data minimisation**: Processing only data strictly necessary for product functionality.
6. **Attack surface limitation**: Limiting interfaces to those necessary for operation and disabling unused services by default.
7. **Resilience**: Protection against denial-of-service and degradation of essential functions.
8. **Security logging**: Recording security events, access attempts, and audit trails with tamper protection.
9. **Updateability**: Ensuring secure installation of updates, separated from functional updates, with automated installation options where appropriate.

# Dates and transitions

Applies from 11 December 2027.

# Related concepts

- [Annex I: Overview](annex-i.md)
- [Annex I Part II: Vulnerability handling](annex-i-part-2.md)
- [Article 6: Requirements for products](../articles/article-6.md)
- [Article 13: Obligations of manufacturers](../articles/article-13.md)

[^cra-annex-i-part-1]: Regulation (EU) 2024/2847, Annex I Part I, [ELI: http://data.europa.eu/eli/reg/2024/2847/oj/eng](http://data.europa.eu/eli/reg/2024/2847/oj/eng).
