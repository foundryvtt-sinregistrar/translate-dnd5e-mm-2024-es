#!/usr/bin/env python3
"""Restore translated Monster Manual UUID and Embed targets from English sources."""

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
REFERENCE = re.compile(
    r"(?P<prefix>@(?:UUID|Embed)\[Compendium\.dnd-monster-manual\.)"
    r"(?P<target>[^\]]+)(?P<suffix>\])"
)
MISMATCHES: list[str] = []


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def source_path(pack: str) -> Path:
    base = f"dnd-monster-manual.{pack}"
    return ENGLISH / base / "en" / f"{base}.en-source.json"


def repair_string(spanish: str, english: str, location: str) -> tuple[str, int]:
    translated = list(REFERENCE.finditer(spanish))
    original = list(REFERENCE.finditer(english))
    if not translated or all(a.group("target") == b.group("target") for a, b in zip(translated, original)):
        return spanish, 0
    if len(translated) != len(original):
        MISMATCHES.append(f"{location}: ES={len(translated)}, EN={len(original)}")
        return spanish, 0
    output: list[str] = []
    cursor = 0
    changes = 0
    for current, source in zip(translated, original):
        output.append(spanish[cursor:current.start()])
        target = source.group("target")
        output.append(current.group("prefix") + target + current.group("suffix"))
        changes += current.group("target") != target
        cursor = current.end()
    output.append(spanish[cursor:])
    return "".join(output), changes


def repair_value(spanish: Any, english: Any, path: str) -> tuple[Any, int]:
    if isinstance(spanish, dict) and isinstance(english, dict):
        changes = 0
        result = dict(spanish)
        for key, value in spanish.items():
            if key not in english:
                continue
            child_path = f"{path}.{key}" if path else key
            result[key], count = repair_value(value, english[key], child_path)
            changes += count
        return result, changes
    if isinstance(spanish, list) and isinstance(english, list):
        changes = 0
        result = list(spanish)
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
    total = 0
    outputs: list[tuple[Path, dict[str, Any]]] = []
    for pack in PACKS:
        path = COMPENDIUM / f"dnd-monster-manual.{pack}.json"
        spanish = load(path)
        english = load(source_path(pack))
        repaired, changes = repair_value(spanish, english, pack)
        outputs.append((path, repaired))
        total += changes
        print(f"{pack}: {changes} reference target(s) restored")
    if MISMATCHES:
        print("Ambiguous fields left unchanged:")
        for row in MISMATCHES:
            print(f"- {row}")
    if args.write:
        for path, data in outputs:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
