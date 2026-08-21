---
type: Standard
title: M/606 Line 35 — Virtualisation and Container Systems
description: Standardisation request entry for vertical cybersecurity requirements on hypervisors, container runtime systems, and virtualisation platforms.
category: standard
tags: [cra, standard, m606, vertical, annex-iii-class-ii, hypervisors, containers, virtualisation, etsi-tc-cyber]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: m606
    resource: https://ec.europa.eu/transparency/documents-register/detail?ref=C(2025)618&lang=en
    title: Commission Implementing Decision C(2025) 618 (Mandate M/606)
    author: European Commission
    last_modified: 2025-01-31T00:00:00Z
  - id: stan4cra-etsi
    resource: https://www.stan4cra.eu/etsi-tc-cyber
    title: ETSI TC Cyber Technical Work (Topic 35)
    author: STAN4CR
    last_modified: 2026-07-01T00:00:00Z
  - id: etsi-wi-74858
    resource: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74858
    title: ETSI Work Item REN/CYBER-00126 (EN 304 635)
    author: ETSI
    last_modified: 2026-06-24T00:00:00Z
x-cra:
  standard_number: M/606 Line 35
  standard_status: requested
  standards_body: ETSI
  technical_committee: ETSI TC CYBER / WG EUSR
  m606_entries: [35]
  ojeu_cited: false
  ojeu_reference: null
  presumption_of_conformity: false
  covers:
    - CRA Annex III Class II point 1
  access: open
  copyright: third-party
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

M/606 Line 35 requests a vertical European Standard establishing essential cybersecurity requirements for virtualisation systems, hypervisors, and container runtimes under CRA Annex III Class II point 1[^m606].

# Legal effect

This request entry sets the standardisation mandate; presumption of conformity requires publication in the OJEU.

# Requested scope and mandate

- **Legal basis**: CRA Annex III, Class II, point 1 (Important products Class II).
- **Mandate objective**: Specify requirements for VM/container isolation, side-channel mitigation (e.g. Spectre/Meltdown defenses), host kernel attack surface reduction, container image signature verification, namespace security, and hypervisor privilege escalation protection.

# Responsible committee and deliverables

- **Technical Committee**: ETSI TC CYBER / WG EUSR (Rapporteur: Mohamad Hajj)[^stan4cra-etsi].
- **Deliverable**: `EN 304-635` (ETSI Work Item `REN/CYBER-00126`, WKI ID 74858)[^etsi-wi-74858].

# Related concepts

- `standards/committees/etsi-tc-cyber-eusr`
- `standards/harmonised/en-304-635`

[^m606]: Commission Implementing Decision C(2025) 618. https://ec.europa.eu/transparency/documents-register/detail?ref=C(2025)618&lang=en
[^stan4cra-etsi]: STAN4CR. ETSI TC Cyber Technical Work. https://www.stan4cra.eu/etsi-tc-cyber
[^etsi-wi-74858]: ETSI Work Item REN/CYBER-00126. https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74858
