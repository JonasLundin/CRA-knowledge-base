---
type: Authority
title: Cyber Resilience Act Implementation in Germany
description: Designated national authorities, market surveillance, CSIRT reporting routing, and enforcement measures for the Cyber Resilience Act in Germany.
category: authority
tags: [cra, jurisdiction, eu-member-state, germany, authorities, market-surveillance, csirt]
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
  - id: de-bgbl
    resource: https://www.recht.bund.de/
    title: Federal Law Gazette (Bundesgesetzblatt - BGBl.)
    author: Federal Ministry of Justice (Bundesministerium der Justiz)
    last_modified: 2026-08-21T00:00:00Z
  - id: de-bsi
    resource: https://www.bsi.bund.de/
    title: Federal Office for Information Security (BSI / CERT-Bund)
    author: Bundesamt für Sicherheit in der Informationstechnik
    last_modified: 2026-08-21T00:00:00Z
x-cra:
  jurisdiction_code: DE
  jurisdiction_name: Germany
  eu_eea_status: eu_member_state
  notifying_authority: Federal Ministry for Economic Affairs and Climate Action (Bundesministerium für Wirtschaft und Klimaschutz - BMWK) / Federal Ministry of the Interior and Community (BMI) / Federal Network Agency (Bundesnetzagentur - BNetzA)
  market_surveillance_authority: Federal Office for Information Security (Bundesamt für Sicherheit in der Informationstechnik - BSI) and Federal Network Agency (Bundesnetzagentur - BNetzA)
  legislation_status: pending
  csirt_routing: CERT-Bund / Federal Office for Information Security (BSI)
  source_language: de
  language_review_gap: true
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Implementation, market surveillance structure, and incident notification routing for Regulation (EU) 2024/2847 (Cyber Resilience Act)[^cra-regulation] in Germany.

# Competent authorities

## Notifying authority
Under CRA Article 35, Germany designates its notifying authority responsible for setting up and carrying out assessment and notification procedures for conformity assessment bodies (notified bodies):
- Designated authority: Federal Ministry for Economic Affairs and Climate Action (Bundesministerium für Wirtschaft und Klimaschutz - BMWK) / Federal Ministry of the Interior and Community (BMI) / Federal Network Agency (Bundesnetzagentur - BNetzA)[^ec-nando-cra].

## Market surveillance authority
Under CRA Article 52 and Regulation (EU) 2019/1020, market surveillance of products with digital elements placed on the Germany market is conducted by:
- Designated market surveillance authority: Federal Office for Information Security (Bundesamt für Sicherheit in der Informationstechnik - BSI) and Federal Network Agency (Bundesnetzagentur - BNetzA)[^ec-cra-ms].

## CSIRT and reporting routing
Under CRA Article 14 and Directive (EU) 2022/2555 (NIS2), notifications of actively exploited vulnerabilities and severe incidents affecting products with digital elements route through the ENISA Single Reporting Platform (SRP) to the national CSIRT coordinator:
- Designated CSIRT / reporting recipient: CERT-Bund / Federal Office for Information Security (BSI)[^de-bsi].

# National legislation and penalties

Under CRA Article 64, Member States must establish rules on penalties applicable to infringements of the CRA by 11 December 2027:
- Legislation status: Pending national legislative enactment.
- Official legal gazette / registry: Federal Law Gazette (Bundesgesetzblatt - BGBl.)[^de-bgbl].
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
[^de-bgbl]: Federal Ministry of Justice (Bundesministerium der Justiz), Federal Law Gazette (Bundesgesetzblatt - BGBl.), https://www.recht.bund.de/
[^de-bsi]: Bundesamt für Sicherheit in der Informationstechnik, Federal Office for Information Security (BSI / CERT-Bund), https://www.bsi.bund.de/
