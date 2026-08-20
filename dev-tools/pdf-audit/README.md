# MM 2024 PDF terminology audit

This directory contains the reproducible checks used to compare the Foundry
translation with the official Spanish Monster Manual PDFs.

The local PDFs are scanned page images. The audit records this condition but
does not copy book text into Git. OCR output, when generated, must remain under
an ignored `_data` directory.

Run from the repository root:

```powershell
python dev-tools/pdf-audit/audit_mm_translation.py `
  --json dev-tools/pdf-audit/reports/mm-pdf-audit.json `
  --markdown dev-tools/pdf-audit/reports/mm-pdf-audit.md
```

The audit verifies top-level entry coverage, internal Monster Manual
references, protected Foundry commands, official terminology, deprecated
Spanish variants, and probable untranslated fields.
