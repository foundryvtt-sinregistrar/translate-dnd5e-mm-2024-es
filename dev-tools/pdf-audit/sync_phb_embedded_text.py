#!/usr/bin/env python3
"""Reuse canonical PHB translations for identical text embedded in MM actors."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parents[2]
MODULES = ROOT.parent
PHB = MODULES / "translate-dnd5e-phb-2024-es"
COMPENDIUM = ROOT / "compendium"
MM_ENGLISH = ROOT / "dev-tools" / "export" / "data"
MARKERS = {
    "all", "and", "any", "are", "attack", "before", "can", "creature", "damage",
    "during", "each", "effect", "feet", "from", "has", "have", "in", "is", "it",
    "its", "make", "must", "of", "on", "or", "saving", "spell", "target", "than",
    "that", "the", "their", "then", "they", "this", "throw", "to", "turn", "until",
    "use", "when", "while", "with", "within", "you", "your",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def walk(value: Any, path: tuple[str, ...] = ()) -> Iterator[tuple[tuple[str, ...], str]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, path + (str(index),))
    elif isinstance(value, str):
        yield path, value


def set_path(data: dict[str, Any], path: tuple[str, ...], value: str) -> None:
    target: Any = data
    for key in path[:-1]:
        target = target[int(key)] if isinstance(target, list) else target[key]
    if isinstance(target, list):
        target[int(path[-1])] = value
    else:
        target[path[-1]] = value


def probable_english(value: str) -> bool:
    visible = html.unescape(re.sub(r"<[^>]+>|@\w+\[[^\]]*\]|\[\[[^\]]*\]\]", " ", value))
    words = re.findall(r"[A-Za-z']+", visible.casefold())
    markers = sum(word in MARKERS for word in words)
    return markers >= 4 and markers / max(1, len(words)) > 0.18


def phb_dictionary() -> dict[str, str]:
    candidates: dict[str, Counter[str]] = defaultdict(Counter)
    for spanish_path in sorted((PHB / "compendium").glob("dnd-players-handbook.*.json")):
        pack = spanish_path.stem.rsplit(".", 1)[-1]
        english_path = (
            PHB / "dev-tools" / "export" / "data" / f"dnd-players-handbook.{pack}"
            / "en" / f"dnd-players-handbook.{pack}-en.json"
        )
        if not english_path.exists():
            continue
        english = dict(walk(load(english_path)))
        spanish = dict(walk(load(spanish_path)))
        for path, source in english.items():
            translated = spanish.get(path)
            if translated and translated != source:
                candidates[source][translated] += 1
    return {source: rows.most_common(1)[0][0] for source, rows in candidates.items()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    dictionary = phb_dictionary()
    total = 0
    for pack in ("actors", "features"):
        base = f"dnd-monster-manual.{pack}"
        spanish_path = COMPENDIUM / f"{base}.json"
        english_path = MM_ENGLISH / base / "en" / f"{base}.en-source.json"
        spanish = load(spanish_path)
        english = dict(walk(load(english_path)))
        changes = 0
        for path, current in list(walk(spanish)):
            source = english.get(path)
            replacement = dictionary.get(source or "")
            if replacement and current != replacement and probable_english(current):
                set_path(spanish, path, replacement)
                changes += 1
        if args.write and changes:
            spanish_path.write_text(
                json.dumps(spanish, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        total += changes
        print(f"{pack}: {changes} embedded PHB field(s) synchronized")
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
