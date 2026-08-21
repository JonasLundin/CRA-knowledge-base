---
type: Authority
title: Cyber Resilience Act Implementation in Poland
description: Designated national authorities, market surveillance, CSIRT reporting routing, and enforcement measures for the Cyber Resilience Act in Poland.
category: authority
tags: [cra, jurisdiction, eu-member-state, poland, authorities, market-surveillance, csirt]
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
  - id: pl-dziennikustaw
    resource: https://dziennikustaw.gov.pl/
    title: Journal of Laws of the Republic of Poland (Dziennik Ustaw)
    author: Government Legislation Centre (Rządowe Centrum Legislacji)
    last_modified: 2026-08-21T00:00:00Z
  - id: pl-cert
    resource: https://cert.pl/
    title: CSIRT NASK (CERT Polska)
    author: NASK - National Research Institute
    last_modified: 2026-08-21T00:00:00Z
x-cra:
  jurisdiction_code: PL
  jurisdiction_name: Poland
  eu_eea_status: eu_member_state
  notifying_authority: Ministry of Digital Affairs (Ministerstwo Cyfryzacji) / Ministry of Economic Development and Technology (Ministerstwo Rozwoju i Technologii)
  market_surveillance_authority: Office of Electronic Communications (Urząd Komunikacji Elektronicznej - UKE) and Office of Competition and Consumer Protection (UOKiK)
  legislation_status: pending
  csirt_routing: CSIRT NASK (NASK-PIB), CSIRT GOV (Internal Security Agency - ABW), and CSIRT MON
  source_language: pl
  language_review_gap: true
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Implementation, market surveillance structure, and incident notification routing for Regulation (EU) 2024/2847 (Cyber Resilience Act)[^cra-regulation] in Poland.

# Competent authorities

## Notifying authority
Under CRA Article 35, Poland designates its notifying authority responsible for setting up and carrying out assessment and notification procedures for conformity assessment bodies (notified bodies):
- Designated authority: Ministry of Digital Affairs (Ministerstwo Cyfryzacji) / Ministry of Economic Development and Technology (Ministerstwo Rozwoju i Technologii)[^ec-nando-cra].

## Market surveillance authority
Under CRA Article 52 and Regulation (EU) 2019/1020, market surveillance of products with digital elements placed on the Poland market is conducted by:
- Designated market surveillance authority: Office of Electronic Communications (Urząd Komunikacji Elektronicznej - UKE) and Office of Competition and Consumer Protection (UOKiK)[^ec-cra-ms].

## CSIRT and reporting routing
Under CRA Article 14 and Directive (EU) 2022/2555 (NIS2), notifications of actively exploited vulnerabilities and severe incidents affecting products with digital elements route through the ENISA Single Reporting Platform (SRP) to the national CSIRT coordinator:
- Designated CSIRT / reporting recipient: CSIRT NASK (NASK-PIB), CSIRT GOV (Internal Security Agency - ABW), and CSIRT MON[^pl-cert].

# National legislation and penalties

Under CRA Article 64, Member States must establish rules on penalties applicable to infringements of the CRA by 11 December 2027:
- Legislation status: Pending national legislative enactment.
- Official legal gazette / registry: Journal of Laws of the Republic of Poland (Dziennik Ustaw)[^pl-dziennikustaw].
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
[^pl-dziennikustaw]: Government Legislation Centre (Rządowe Centrum Legislacji), Journal of Laws of the Republic of Poland (Dziennik Ustaw), https://dziennikustaw.gov.pl/
[^pl-cert]: NASK - National Research Institute, CSIRT NASK (CERT Polska), https://cert.pl/
