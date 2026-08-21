---
type: Authority
title: Cyber Resilience Act Implementation in Sweden
description: Designated national authorities, market surveillance, CSIRT reporting routing, and enforcement measures for the Cyber Resilience Act in Sweden.
category: authority
tags: [cra, jurisdiction, eu-member-state, sweden, authorities, market-surveillance, csirt]
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
  - id: se-sfs
    resource: https://www.svenskforfattningssamling.se/
    title: Swedish Code of Statutes (Svensk författningssamling - SFS)
    author: Government of Sweden / Riksdagen
    last_modified: 2026-08-21T00:00:00Z
  - id: se-certse
    resource: https://www.cert.se/
    title: CERT-SE - Sweden's National CSIRT (MSB)
    author: Myndigheten för samhällsskydd och beredskap (MSB)
    last_modified: 2026-08-21T00:00:00Z
x-cra:
  jurisdiction_code: SE
  jurisdiction_name: Sweden
  eu_eea_status: eu_member_state
  notifying_authority: Ministry of Climate and Enterprise (Klimat- och näringslivsdepartementet) / Swedac (Styrelsen för ackreditering och teknisk kontroll)
  market_surveillance_authority: Swedish Post and Telecom Authority (Post- och telestyrelsen - PTS) and Swedish Civil Contingencies Agency (Myndigheten för samhällsskydd och beredskap - MSB) / Swedish Consumer Agency (Konsumentverket)
  legislation_status: pending
  csirt_routing: CERT-SE (Myndigheten för samhällsskydd och beredskap - MSB / National Cyber Security Centre - NCSC-SE)
  source_language: sv
  language_review_gap: false
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Implementation, market surveillance structure, and incident notification routing for Regulation (EU) 2024/2847 (Cyber Resilience Act)[^cra-regulation] in Sweden.

# Competent authorities

## Notifying authority
Under CRA Article 35, Sweden designates its notifying authority responsible for setting up and carrying out assessment and notification procedures for conformity assessment bodies (notified bodies):
- Designated authority: Ministry of Climate and Enterprise (Klimat- och näringslivsdepartementet) / Swedac (Styrelsen för ackreditering och teknisk kontroll)[^ec-nando-cra].

## Market surveillance authority
Under CRA Article 52 and Regulation (EU) 2019/1020, market surveillance of products with digital elements placed on the Sweden market is conducted by:
- Designated market surveillance authority: Swedish Post and Telecom Authority (Post- och telestyrelsen - PTS) and Swedish Civil Contingencies Agency (Myndigheten för samhällsskydd och beredskap - MSB) / Swedish Consumer Agency (Konsumentverket)[^ec-cra-ms].

## CSIRT and reporting routing
Under CRA Article 14 and Directive (EU) 2022/2555 (NIS2), notifications of actively exploited vulnerabilities and severe incidents affecting products with digital elements route through the ENISA Single Reporting Platform (SRP) to the national CSIRT coordinator:
- Designated CSIRT / reporting recipient: CERT-SE (Myndigheten för samhällsskydd och beredskap - MSB / National Cyber Security Centre - NCSC-SE)[^se-certse].

# National legislation and penalties

Under CRA Article 64, Member States must establish rules on penalties applicable to infringements of the CRA by 11 December 2027:
- Legislation status: Pending national legislative enactment.
- Official legal gazette / registry: Swedish Code of Statutes (Svensk författningssamling - SFS)[^se-sfs].
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
[^se-sfs]: Government of Sweden / Riksdagen, Swedish Code of Statutes (Svensk författningssamling - SFS), https://www.svenskforfattningssamling.se/
[^se-certse]: Myndigheten för samhällsskydd och beredskap (MSB), CERT-SE - Sweden's National CSIRT (MSB), https://www.cert.se/
