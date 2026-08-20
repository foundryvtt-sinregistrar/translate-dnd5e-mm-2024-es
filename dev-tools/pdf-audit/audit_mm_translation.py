#!/usr/bin/env python3
"""Audit the MM 2024 Spanish translation without changing compendium data."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parents[2]
COMPENDIUM = ROOT / "compendium"
ENGLISH = ROOT / "dev-tools" / "export" / "data"
PDF_DIR = ROOT / "dev-tools" / "export" / "_data" / "pdf"
TERMS_FILE = Path(__file__).with_name("official-terms.es.json")
PACKS = ("actors", "content", "features", "tables")

PROTECTED = re.compile(
    r"(?:@(?:UUID|Embed|Check|Damage|Template|Prompt)\[[^\]]*\](?:\{[^}]*\})?)"
    r"|(?:&(?:amp;)?(?:Reference|Trait|Activity)\[[^\]]*\](?:\{[^}]*\})?)"
    r"|(?:\[\[[^\]]*\]\])"
)
MM_REFERENCE = re.compile(
    r"@(?:UUID|Embed)\[Compendium\.dnd-monster-manual\.([^\.\]]+)\."
    r"(?:Item|Actor|JournalEntry|RollTable)\.([^\.#\]\s]+)"
)
ENGLISH_MARKERS = {
    "all", "and", "any", "are", "attack", "before", "can", "creature",
    "creatures", "damage", "during", "each", "effect", "feet", "from", "has",
    "have", "hit", "in", "is", "it", "its", "make", "must", "of", "on", "or",
    "saving", "spell", "target", "than", "that", "the", "their", "then", "they",
    "this", "throw", "to", "turn", "until", "use", "when", "while", "with",
    "within", "you", "your",
}


def walk(value: Any, path: str = "") -> Iterator[tuple[str, str]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")
    elif isinstance(value, str):
        yield path, value


def visible_text(value: str) -> str:
    value = PROTECTED.sub(" ", value)
    return html.unescape(re.sub(r"<[^>]+>", " ", value))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def source_path(pack: str) -> Path:
    base = f"dnd-monster-manual.{pack}"
    return ENGLISH / base / "en" / f"{base}.en-source.json"


def load_packs() -> tuple[dict[str, dict], dict[str, dict]]:
    spanish = {
        pack: load_json(COMPENDIUM / f"dnd-monster-manual.{pack}.json") for pack in PACKS
    }
    english = {pack: load_json(source_path(pack)) for pack in PACKS}
    return spanish, english


def pdf_statistics() -> dict[str, Any]:
    paths = sorted(PDF_DIR.glob("*.pdf"))
    result: dict[str, Any] = {"files": len(paths), "characters": None, "blankFiles": None}
    if not paths:
        return result
    try:
        from pypdf import PdfReader
    except ImportError:
        result["warning"] = "Install pypdf to inspect the local PDF files."
        return result
    characters = 0
    blank = 0
    for path in paths:
        text = "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages)
        characters += len(text)
        blank += not bool(text.strip())
    result.update(characters=characters, blankFiles=blank)
    if blank == len(paths):
        result["warning"] = "All PDF pages are scanned images; OCR is required for corpus searches."
    return result


def run_audit() -> dict[str, Any]:
    spanish, english = load_packs()
    terms = load_json(TERMS_FILE)
    canonical = {**terms["actions"], **terms["conditions"], **terms["rules"]}
    identifiers = {pack: set(data.get("entries", {})) for pack, data in spanish.items()}
    structure: dict[str, Any] = {}
    references = 0
    invalid_references: list[dict[str, str]] = []
    macro_mutations: list[dict[str, str]] = []
    residues: list[dict[str, str]] = []
    deprecated_hits: list[dict[str, str]] = []
    probable_english: list[dict[str, Any]] = []

    for pack in PACKS:
        data = spanish[pack]
        source = english[pack]
        es_ids = identifiers[pack]
        en_ids = set(source.get("entries", {}))
        structure[pack] = {
            "englishEntries": len(en_ids),
            "spanishEntries": len(es_ids),
            "missing": sorted(en_ids - es_ids),
            "extra": sorted(es_ids - en_ids),
        }
        source_fields = dict(walk(source))
        for path, value in walk(data):
            for target_pack, entry_id in MM_REFERENCE.findall(value):
                references += 1
                if target_pack not in identifiers or entry_id not in identifiers[target_pack]:
                    invalid_references.append({
                        "pack": pack, "path": path, "targetPack": target_pack, "entryId": entry_id
                    })
            for lookup in re.findall(r"\[\[lookup\s+([^\]]+)\]\]", value):
                tokens = lookup.split()
                unexpected = [
                    token for token in tokens[1:]
                    if token not in {"capitalize", "lowercase"}
                    and not re.match(r"(?:activity|format|fallback)=", token)
                ]
                if unexpected:
                    macro_mutations.append({
                        "pack": pack,
                        "path": path,
                        "kind": "lookup-key",
                        "command": lookup,
                    })
            visible = visible_text(value)
            for old, new in canonical.items():
                if old.casefold() != new.casefold() and re.search(
                    rf"\b{re.escape(old)}\b", visible, re.IGNORECASE
                ):
                    residues.append({"pack": pack, "path": path, "found": old, "expected": new})
            for old, new in terms["deprecatedSpanish"].items():
                if re.search(rf"\b{re.escape(old)}\b", visible, re.IGNORECASE):
                    deprecated_hits.append(
                        {"pack": pack, "path": path, "found": old, "expected": new}
                    )
            words = re.findall(r"[A-Za-z']+", visible.casefold())
            markers = sum(word in ENGLISH_MARKERS for word in words)
            if markers >= 4 and markers / max(1, len(words)) > 0.18:
                probable_english.append(
                    {"pack": pack, "path": path, "markers": markers, "words": len(words)}
                )
            source_value = source_fields.get(path)
            if source_value and value != source_value:
                source_commands = Counter(re.findall(r"\[\[(?:lookup|/)[^\]]+\]\]", source_value))
                translated_commands = Counter(re.findall(r"\[\[(?:lookup|/)[^\]]+\]\]", value))
                removed = source_commands - translated_commands
                added = translated_commands - source_commands
                if removed or added:
                    macro_mutations.append({
                        "pack": pack,
                        "path": path,
                        "kind": "command-difference",
                        "removed": list(removed.elements()),
                        "added": list(added.elements()),
                    })

    return {
        "pdf": pdf_statistics(),
        "structure": structure,
        "references": {"checked": references, "invalid": invalid_references},
        "macroMutations": macro_mutations,
        "englishResidues": residues,
        "deprecatedSpanish": deprecated_hits,
        "probableEnglishFields": probable_english,
        "summary": {
            "missingEntries": sum(len(row["missing"]) for row in structure.values()),
            "extraEntries": sum(len(row["extra"]) for row in structure.values()),
            "invalidReferences": len(invalid_references),
            "macroMutations": len(macro_mutations),
            "englishResidues": len(residues),
            "deprecatedSpanish": len(deprecated_hits),
            "probableEnglishFields": len(probable_english),
            "probableEnglishByPack": dict(Counter(row["pack"] for row in probable_english)),
        },
    }


def markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# MM 2024 PDF terminology audit", "", "## Summary", "",
        f"- Missing Spanish entries: {summary['missingEntries']}",
        f"- Extra Spanish entries: {summary['extraEntries']}",
        f"- Invalid internal references: {summary['invalidReferences']}",
        f"- Macro mutation candidates: {summary['macroMutations']}",
        f"- Visible English terminology residues: {summary['englishResidues']}",
        f"- Deprecated Spanish terminology occurrences: {summary['deprecatedSpanish']}",
        f"- Probable untranslated English fields: {summary['probableEnglishFields']}",
        "", "## Pack structure", "",
        "| Pack | English | Spanish | Missing | Extra |",
        "|---|---:|---:|---:|---:|",
    ]
    for pack, row in report["structure"].items():
        lines.append(
            f"| {pack} | {row['englishEntries']} | {row['spanishEntries']} | "
            f"{len(row['missing'])} | {len(row['extra'])} |"
        )
    sections = (
        ("Invalid internal references", report["references"]["invalid"]),
        ("Macro mutation candidates", report["macroMutations"]),
        ("Visible English terminology findings", report["englishResidues"]),
        ("Deprecated Spanish terminology", report["deprecatedSpanish"]),
        ("Probable untranslated English fields", report["probableEnglishFields"]),
    )
    for title, rows in sections:
        lines.extend(["", f"## {title}", ""])
        for row in rows:
            details = ", ".join(f"{key}={value}" for key, value in row.items() if key not in {"pack", "path"})
            lines.append(f"- `{row['pack']}:{row['path']}`: {details}")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--markdown", type=Path)
    args = parser.parse_args()
    report = run_audit()
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown(report), encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
