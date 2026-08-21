---
type: Glossary Term
title: Software Bill of Materials (SBOM)
description: Legal definition of a Software Bill of Materials under Article 3(40) of Regulation (EU) 2024/2847.
category: glossary
tags: [cra, glossary, definition, sbom, supply-chain, dependencies]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-art-3
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
    title: Regulation (EU) 2024/2847, Article 3
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Article 3(40)
  applies_from: 2024-12-10
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Under Article 3(40) of Regulation (EU) 2024/2847, a **Software Bill of Materials (SBOM)** means a formal record containing details and supply chain relationships of components included in the software elements of a product with digital elements.[^cra-art-3]

# Legal effect

Mandatory component of the technical documentation under Annex VII and a core requirement for vulnerability handling under Annex I Part II point (1).[^cra-art-3]

# Requirements or coverage

Must be compiled in a machine-readable format covering top-level and relevant transitive dependencies, versions, and cryptographic identities.[^cra-art-3]

# Related concepts

- [Software Bill of Materials Requirements](../obligations/vulnerability-handling/software-bill-of-materials.md)
- [Third-Party Components Due Diligence](../obligations/manufacturers/third-party-components.md)
- [Technical Documentation](../obligations/manufacturers/technical-documentation.md)

[^cra-art-3]: Regulation (EU) 2024/2847, Article 3, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_3
