---
type: Requirement
title: Third-Party Components Due Diligence under the CRA
description: Manufacturer obligations to exercise due diligence when integrating third-party and open-source components under Article 13(5)–(6) of Regulation (EU) 2024/2847.
category: requirement
tags: [cra, supply-chain, third-party-components, sbom, open-source]
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
  provision: Article 13(5)–(6)
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Article 13(5) and (6) requires manufacturers to exercise due diligence when integrating components sourced from third parties—including proprietary software, hardware modules, and free and open-source software (FOSS)—into products with digital elements.[^cra-art-13]

# Legal effect

Integrating a third-party component does not transfer or reduce the manufacturer's legal responsibility. The manufacturer remains solely liable for ensuring that the final integrated product complies with Annex I essential requirements and remains secure throughout its support period.[^cra-art-13]

# Applicability

Applies whenever a manufacturer incorporates any third-party code, library, module, hardware element, firmware, or cloud dependency into a product with digital elements placed on the EU market.[^cra-art-13]

# Requirements or coverage

Manufacturers must:

1. **Exercise due diligence:** Verify that integrated components do not compromise the overall security of the product (Article 13(5));
2. **Document components in an SBOM:** Identify and track all direct and transitive third-party dependencies in a machine-readable Software Bill of Materials (Annex I Part II point 1);[^cra-annex-1]
3. **Monitor and patch vulnerabilities:** Continuously monitor third-party components for discovered vulnerabilities throughout the support period and deploy security patches without delay (Article 13(6));
4. **Upstream vulnerability coordination:** Share vulnerability information and patches with the maintainers of integrated open-source components where appropriate.[^cra-art-13]

# Dates and transitions

- Applies from 11 December 2027.

# Related concepts

- [Manufacturer Role & Duties](manufacturer.md)
- [Software Bill of Materials](../vulnerability-handling/software-bill-of-materials.md)
- [Commercial Activity Boundary](../scope/commercial-activity.md)
- [Open-Source Software Steward Role](../open-source/open-source-software-steward.md)

[^cra-art-13]: Regulation (EU) 2024/2847, Article 13, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_13
[^cra-annex-1]: Regulation (EU) 2024/2847, Annex I, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_1
