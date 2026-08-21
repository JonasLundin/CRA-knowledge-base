---
type: Authority
title: Cyber Resilience Act Implementation in Luxembourg
description: Designated national authorities, market surveillance, CSIRT reporting routing, and enforcement measures for the Cyber Resilience Act in Luxembourg.
category: authority
tags: [cra, jurisdiction, eu-member-state, luxembourg, authorities, market-surveillance, csirt]
status: draft
generated: { by: opencode/task-coder-smart, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: cra-regulation
    resource: http://data.europa.eu/eli/reg/2024/2847/oj/eng
    title: Regulation (EU) 2024/2847 (Cyber Resilience Act)
    author: European Parliament and Council of the European Union
    last_modified: 2024-11-20T00:00:00Z
  - id: ec-cra-ms
    resource: https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation
    title: Cyber Resilience Act Implementation
    author: European Commission
    last_modified: 2026-08-21T00:00:00Z
  - id: ec-nando-cra
    resource: https://ec.europa.eu/growth/tools-databases/nando/
    title: NANDO Information System - CRA Notifying Authorities
    author: European Commission
    last_modified: 2026-08-21T00:00:00Z
  - id: lu-legilux
    resource: https://legilux.public.lu/
    title: Official Journal of the Grand Duchy of Luxembourg (Legilux / Mémorial)
    author: Service central de législation
    last_modified: 2026-08-21T00:00:00Z
  - id: lu-circl
    resource: https://www.circl.lu/
    title: CIRCL - Computer Incident Response Center Luxembourg
    author: security made in Lëtzebuerg (SECURITYMADEIN.LU) / HCPN
    last_modified: 2026-08-21T00:00:00Z
x-cra:
  jurisdiction_code: LU
  jurisdiction_name: Luxembourg
  eu_eea_status: eu_member_state
  notifying_authority: Ministry of the Economy (Ministère de l'Économie) / ILNAS (Institut Luxembourgeois de la Normalisation, de l'Accréditation, de la Sécurité et qualité des produits et services)
  market_surveillance_authority: ILNAS (Department of Market Surveillance) and High Commission for National Protection (Haut-Commissariat à la Protection Nationale - HCPN)
  legislation_status: pending
  csirt_routing: Computer Incident Response Center Luxembourg (CIRCL) / GOVCERT.LU
  source_language: fr, de
  language_review_gap: true
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Implementation, market surveillance structure, and incident notification routing for Regulation (EU) 2024/2847 (Cyber Resilience Act)[^cra-regulation] in Luxembourg.

# Competent authorities

## Notifying authority
Under CRA Article 35, Luxembourg designates its notifying authority responsible for setting up and carrying out assessment and notification procedures for conformity assessment bodies (notified bodies):
- Designated authority: Ministry of the Economy (Ministère de l'Économie) / ILNAS (Institut Luxembourgeois de la Normalisation, de l'Accréditation, de la Sécurité et qualité des produits et services)[^ec-nando-cra].

## Market surveillance authority
Under CRA Article 52 and Regulation (EU) 2019/1020, market surveillance of products with digital elements placed on the Luxembourg market is conducted by:
- Designated market surveillance authority: ILNAS (Department of Market Surveillance) and High Commission for National Protection (Haut-Commissariat à la Protection Nationale - HCPN)[^ec-cra-ms].

## CSIRT and reporting routing
Under CRA Article 14 and Directive (EU) 2022/2555 (NIS2), notifications of actively exploited vulnerabilities and severe incidents affecting products with digital elements route through the ENISA Single Reporting Platform (SRP) to the national CSIRT coordinator:
- Designated CSIRT / reporting recipient: Computer Incident Response Center Luxembourg (CIRCL) / GOVCERT.LU[^lu-circl].

# National legislation and penalties

Under CRA Article 64, Member States must establish rules on penalties applicable to infringements of the CRA by 11 December 2027:
- Legislation status: Pending national legislative enactment.
- Official legal gazette / registry: Official Journal of the Grand Duchy of Luxembourg (Legilux / Mémorial)[^lu-legilux].
- National penalty rules: No verified official source located as of 2026-08-21 for adopted national CRA penalty legislation.

# Official guidance

- National authority CRA guidance: No verified official source located as of 2026-08-21.

# Dates and transitions

- 2024-12-10: CRA entered into force across the European Union.
- 2026-06-11: Application of Chapter IV (Notifying Authorities and Notified Bodies).
- 2026-09-11: Application of Article 14 reporting obligations (actively exploited vulnerabilities and severe incidents via SRP to national CSIRT).
- 2027-12-11: Full application of CRA essential requirements, conformity obligations, and national penalty regimes.

# Related concepts

- `law/eu/cra/articles/article-14`
- `law/eu/cra/articles/article-35`
- `law/eu/cra/articles/article-52`
- `law/eu/cra/articles/article-64`
- `jurisdictions/eu-member-states/index`

[^cra-regulation]: Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements (Cyber Resilience Act), OJ L 2024/2847, http://data.europa.eu/eli/reg/2024/2847/oj/eng
[^ec-cra-ms]: European Commission, Cyber Resilience Act Implementation, https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation
[^ec-nando-cra]: European Commission, NANDO (New Approach Notified and Designated Organisations) Information System, https://ec.europa.eu/growth/tools-databases/nando/
[^lu-legilux]: Service central de législation, Official Journal of the Grand Duchy of Luxembourg (Legilux / Mémorial), https://legilux.public.lu/
[^lu-circl]: security made in Lëtzebuerg (SECURITYMADEIN.LU) / HCPN, CIRCL - Computer Incident Response Center Luxembourg, https://www.circl.lu/
