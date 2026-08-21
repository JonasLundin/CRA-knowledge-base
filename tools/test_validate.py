import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


VALID_CONCEPT = """---
type: Requirement
title: Test requirement
description: A validation fixture.
category: requirement
tags: [cra]
status: draft
generated: { by: process:test, at: 2026-08-21T00:00:00Z }
stale_after: 2026-11-21T00:00:00Z
sources:
  - id: test-source
    resource: https://example.eu/source
    title: Test source
x-cra:
  jurisdiction: EU
  checked_at: 2026-08-21T00:00:00Z
---

# Summary

Test claim.[^test-source]

[^test-source]: Test source.
"""


class ValidatorTest(unittest.TestCase):
    def run_validator(self, concept: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "wiki"
            root.mkdir()
            (root / "index.md").write_text(
                '---\nokf_version: "0.2"\n---\n\n# Test bundle\n', encoding="utf-8"
            )
            (root / "test.md").write_text(concept, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(Path(__file__).with_name("validate.py")), str(root)],
                check=False,
                capture_output=True,
                text=True,
            )

    def test_accepts_valid_and_rejects_missing_type(self) -> None:
        valid = self.run_validator(VALID_CONCEPT)
        self.assertEqual(valid.returncode, 0, valid.stdout + valid.stderr)
        invalid = VALID_CONCEPT.replace("type: Requirement\n", "")
        result = self.run_validator(invalid)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required fields: type", result.stdout)


if __name__ == "__main__":
    unittest.main()
