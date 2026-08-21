# CRA Knowledge Base

An English-language [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) bundle covering the EU Cyber Resilience Act (CRA), its implementation, standards landscape, and related rules.

The bundle contains concise original summaries with provision-level citations to primary sources. It does not reproduce full legal instruments, guidance documents, or standards.

Current release: **v0.1.0**

> **Draft public preview:** the planned corpus has been populated, but every ingested concept remains `draft` and unverified pending human source review.

> **General orientation only:** do not rely on this knowledge base for decisions that determine, demonstrate, or materially affect legal or regulatory compliance. Verify the current primary sources and obtain qualified professional advice before making product-classification, conformity-assessment, market-access, reporting, remediation, or other compliance-impacting decisions.

## Use With Meerkat

[Meerkat](https://github.com/zegit-zoo/meerkat) can serve the bundle as CLI, MCP, or HTTP without conversion:

```sh
mk --kb-dir . search "support period"
mk --kb-dir . show law/eu/cra/articles/article-14
mk --kb-dir . list --category standard
mk --kb-dir . mcp serve
mk --kb-dir . http serve --port 4004
```

Run these commands from the repository root. The knowledge bundle itself is under `wiki/`; Meerkat's `--kb-dir` reads that content-repository layout.

The Markdown remains usable without Meerkat or any other tool.

## Coverage

The intended corpus includes:

- Regulation (EU) 2024/2847, its annexes, amendments, and secondary legislation;
- official European Commission and ENISA implementation guidance;
- economic-operator obligations, product categories, reporting, conformity assessment, and enforcement;
- M/606, its 41 requested standards lines, ESO work items, public drafts, and OJEU citations;
- supporting standards and certification schemes, without copied normative text;
- interacting EU legislation;
- EU Member State authorities and national measures, plus EEA status.

Coverage is measured in `coverage.yaml`. A missing official source is recorded as a research gap rather than filled by inference.

## Source And Publication Policy

- Binding claims cite OJEU, ELI, EUR-Lex, or an official national gazette.
- Official guidance is labelled non-binding.
- A standard provides CRA presumption of conformity only when its reference is cited in the OJEU for the requirements concerned.
- Publicly accessible standards drafts are linked, not copied.
- Agent-generated content stays `status: draft` until a human verifies it against the cited source.
- Superseded material is retained and marked rather than silently deleted.

Only the electronic Official Journal on EUR-Lex is authentic and produces legal effects. This repository is not legal advice, is not a conformity assessment, does not certify any product, and must not be used as the basis for compliance-impacting decisions.

## Validate

```sh
python3 -m pip install -r requirements-dev.txt
python3 tools/validate.py wiki
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Corrections with exact primary-source citations are welcome. Do not submit copied standards text, private compliance evidence, or confidential information.

## Licence

Original summaries, structure, and metadata are licensed under [CC BY 4.0](LICENSE). Source documents and standards retain their own terms; see [NOTICE](NOTICE).

This project is independent and is not affiliated with or endorsed by the European Commission, ENISA, CEN, CENELEC, ETSI, ISO, IEC, Google Cloud, or Meerkat.
