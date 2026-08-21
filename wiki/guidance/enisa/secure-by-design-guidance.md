---
type: Official Guidance
title: ENISA Guidance on Secure-by-Design and Secure-by-Default
description: Technical guidance on applying secure-by-design and secure-by-default engineering principles to satisfy CRA Annex I Part I essential requirements.
category: guidance
tags: [cra, guidance, enisa, secure-by-design, secure-by-default, annex-i, engineering, threat-modelling]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2027-02-21T00:00:00Z
sources:
  - id: enisa-sbd-guidance
    resource: https://www.enisa.europa.eu/publications/cybersecurity-by-design-in-cyber-resilience-act
    title: Engineering Cybersecurity by Design and by Default for the Cyber Resilience Act
    author: European Union Agency for Cybersecurity (ENISA)
    last_modified: 2025-10-28T00:00:00Z
x-cra:
  jurisdiction: EU
  issuing_authority: ENISA
  authority_level: non_binding
  document_status: published
  publication_date: 2025-10-28
  relevant_provisions:
    - Article 13
    - Annex I
    - Annex VII
  language: en
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

ENISA's *Engineering Cybersecurity by Design and by Default for the Cyber Resilience Act* provides engineering best practices and architectural patterns to help manufacturers design, develop, and deliver products that meet the essential cybersecurity requirements of CRA Annex I Part I [^enisa-sbd-guidance].

# Legal effect

This technical guide is non-binding [^enisa-sbd-guidance]. Adherence to the recommended engineering patterns does not automatically grant a legal presumption of conformity (which requires OJEU-cited harmonised standards), but serves as authoritative technical evidence in technical documentation files.

# Applicability

Applies to software architects, hardware designers, embedded systems engineers, DevSecOps practitioners, and product security teams developing products with digital elements.

# Key topics or guidance coverage

The guidance translates the legal requirements of Annex I Part I into actionable engineering disciplines [^enisa-sbd-guidance]:

- **Secure Default Configurations (Annex I Part I Point 2):** Delivering products in a hardened state by default, prohibiting default/universal passwords, disabling unnecessary network ports, services, and interfaces, and requiring user-prompted activation for exposed features.
- **Threat Modelling and Risk Assessment (Article 13(2)):** Performing systematic threat modelling (e.g., STRIDE) throughout the design lifecycle to identify potential attack vectors and select proportional mitigations.
- **Attack Surface Minimization & Principle of Least Privilege:** Restricting administrative access, enforcing memory safety, segregating critical execution domains, and isolating sensitive cryptographic material.
- **Data Protection and Cryptographic Safeguards:** Enforcing modern, state-of-the-art cryptographic algorithms for data at rest and data in transit, ensuring secure key generation and storage.
- **Secure Update Mechanisms (Annex I Part I Point 3):** Implementing authenticated, integrity-verified, and cryptographically signed update channels capable of automatic, rollback-resistant security patching.
- **Logging and Security Monitoring:** Providing tamper-resistant local logging of security-relevant events while avoiding the capture of sensitive personal data.

# Dates and transitions

- **Publication Date:** October 2025.
- **Implementation Target:** Supports manufacturer preparation ahead of the 11 December 2027 general application deadline.

# Related concepts

- [CRA Standards Mapping](./cra-standards-mapping.md)
- [European Commission Manufacturers Guidance](../european-commission/manufacturers-guidance.md)
- [European Commission Guidance C(2026) 5252](../european-commission/c-2026-5252-cra-guidance.md)

[^enisa-sbd-guidance]: European Union Agency for Cybersecurity (ENISA), Engineering Cybersecurity by Design and by Default for the Cyber Resilience Act, https://www.enisa.europa.eu/publications/cybersecurity-by-design-in-cyber-resilience-act
