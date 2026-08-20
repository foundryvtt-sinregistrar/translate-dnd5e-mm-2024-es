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

Restore translated identifiers and anchors inside Monster Manual `UUID` and
`Embed` targets while preserving their Spanish visible labels:

```powershell
python dev-tools/pdf-audit/repair_internal_references.py --write
```

Restore functional `lookup`, item, roll, attack, and damage commands from the
aligned English fields. Visible Spanish roll labels after `#` are preserved:

```powershell
python dev-tools/pdf-audit/repair_foundry_commands.py --write
```

Reuse reviewed PHB translations when an identical English spell or effect is
embedded in a Monster Manual actor:

```powershell
python dev-tools/pdf-audit/sync_phb_embedded_text.py --write
```

Apply the curated translations for MM-only residual fields and official terms:

```powershell
python dev-tools/pdf-audit/normalize_mm_residuals.py --write
```
