#!/usr/bin/env python3
"""Restore functional Foundry inline commands from aligned English fields."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
COMPENDIUM = ROOT / "compendium"
ENGLISH = ROOT / "dev-tools" / "export" / "data"
PACKS = ("actors", "content", "features", "tables")
COMMAND = re.compile(r"\[\[(?:lookup|/)[^\]]+\]\]")
MISMATCHES: list[str] = []


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def source_path(pack: str) -> Path:
    base = f"dnd-monster-manual.{pack}"
    return ENGLISH / base / "en" / f"{base}.en-source.json"


def preserve_roll_label(source: str, translated: str) -> str:
    if not source.startswith("[[/r ") or "#" not in translated:
        return source
    label = translated.rsplit("#", 1)[1][:-2]
    base = source.split("#", 1)[0]
    return f"{base}#{label}]]"


def repair_string(spanish: str, english: str, location: str) -> tuple[str, int]:
    translated = list(COMMAND.finditer(spanish))
    original = list(COMMAND.finditer(english))
    if not translated or len(translated) != len(original):
        if translated or original:
            MISMATCHES.append(f"{location}: ES={len(translated)}, EN={len(original)}")
        return spanish, 0
    output: list[str] = []
    cursor = 0
    changes = 0
    for current, source in zip(translated, original):
        output.append(spanish[cursor:current.start()])
        replacement = preserve_roll_label(source.group(0), current.group(0))
        output.append(replacement)
        changes += replacement != current.group(0)
        cursor = current.end()
    output.append(spanish[cursor:])
    return "".join(output), changes


def repair_value(spanish: Any, english: Any, path: str) -> tuple[Any, int]:
    if isinstance(spanish, dict) and isinstance(english, dict):
        result = dict(spanish)
        changes = 0
        for key, value in spanish.items():
            if key in english:
                result[key], count = repair_value(
                    value, english[key], f"{path}.{key}" if path else key
                )
                changes += count
        return result, changes
    if isinstance(spanish, list) and isinstance(english, list):
        result = list(spanish)
        changes = 0
        for index, value in enumerate(spanish[: len(english)]):
            result[index], count = repair_value(value, english[index], f"{path}[{index}]")
            changes += count
        return result, changes
    if isinstance(spanish, str) and isinstance(english, str):
        return repair_string(spanish, english, path)
    return spanish, 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    outputs: list[tuple[Path, dict[str, Any], int]] = []
    for pack in PACKS:
        path = COMPENDIUM / f"dnd-monster-manual.{pack}.json"
        repaired, changes = repair_value(load(path), load(source_path(pack)), pack)
        outputs.append((path, repaired, changes))
        print(f"{pack}: {changes} command(s) restored")
    if MISMATCHES:
        print(f"Ambiguous fields left unchanged: {len(MISMATCHES)}")
        for row in MISMATCHES[:20]:
            print(f"- {row}")
    if args.write:
        for path, data, changes in outputs:
            if changes:
                path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
