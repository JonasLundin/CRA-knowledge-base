---
type: Procedure
title: "Module B + C: EU-Type Examination and Conformity to Type"
description: Two-stage conformity assessment procedure combining third-party type examination and internal production control under Annex VI of Regulation (EU) 2024/2847.
category: procedure
tags: [cra, module-b, module-c, type-examination, notified-body, conformity-assessment]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: cra-annex-6
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_6
    title: Regulation (EU) 2024/2847, Annex VI
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
  - id: cra-art-32
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_32
    title: Regulation (EU) 2024/2847, Article 32
    author: European Parliament and Council
    last_modified: 2024-11-20T00:00:00Z
x-cra:
  jurisdiction: EU
  authority_level: binding
  instrument_status: in_force
  provision: Annex VI Modules B and C, Article 32
  applies_from: 2027-12-11
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

The Module B + Module C conformity assessment route set out in Annex VI of Regulation (EU) 2024/2847 combines an independent EU-Type Examination by a notified body (Module B) with internal production control by the manufacturer (Module C).[^cra-annex-6]

# Legal effect

Permits product release based on an EU-Type Examination Certificate issued by a notified body confirming that a representative specimen (or software build) meets all Annex I essential requirements.[^cra-annex-6]

# Applicability

- Permitted route for **Important Products with Digital Elements — Class I** (Article 32(2));
- Permitted route for **Important Products with Digital Elements — Class II** (Article 32(3)).[^cra-art-32]

# Requirements or coverage

### Stage 1: Module B (EU-Type Examination)
1. **Application:** The manufacturer submits technical documentation, risk assessment, SBOM, and a representative specimen/build to a single notified body;
2. **Examination & Testing:** The notified body examines the technical documentation, verifies standards implementation, and performs technical security tests and code audits;
3. **Certificate issuance:** If compliant, the notified body issues an EU-Type Examination Certificate containing product details, conclusions, and validity conditions.[^cra-annex-6]

### Stage 2: Module C (Conformity to Type based on Internal Production Control)
1. **Production conformity:** The manufacturer implements production and build controls ensuring every manufactured/distributed unit conforms to the approved type described in the certificate;
2. **DoC & CE marking:** The manufacturer issues the EU declaration of conformity and affixes the CE marking (accompanied by the notified body ID number where required by the procedure).[^cra-annex-6]

# Dates and transitions

- Applies from 11 December 2027.

# Related concepts

- [Conformity Assessment Routes](conformity-routes.md)
- [Module H: Full Quality Assurance](module-h-full-quality-assurance.md)
- [Notified Bodies](notified-bodies.md)

[^cra-annex-6]: Regulation (EU) 2024/2847, Annex VI, http://data.europa.eu/eli/reg/2024/2847/oj/eng#ann_6
[^cra-art-32]: Regulation (EU) 2024/2847, Article 32, http://data.europa.eu/eli/reg/2024/2847/oj/eng#art_32
