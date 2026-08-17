#!/usr/bin/env python3
"""
Merge incremental Babele actors patches into dnd-monster-manual.actors.json.

Usage:
  python merge_actors_patch.py dnd-monster-manual.actors.json dnd-monster-manual.actors.es.v17-erinyes-to-flumph.patch.json dnd-monster-manual.actors.es.v17-erinyes-to-flumph.json
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any


def deep_merge(base: Any, patch: Any) -> Any:
    """Recursively merge dictionaries; patch wins for scalars/lists."""
    if isinstance(base, dict) and isinstance(patch, dict):
        out = copy.deepcopy(base)
        for key, value in patch.items():
            if key in out:
                out[key] = deep_merge(out[key], value)
            else:
                out[key] = copy.deepcopy(value)
        return out
    return copy.deepcopy(patch)


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__.strip(), file=sys.stderr)
        return 2

    base_path = Path(sys.argv[1])
    patch_path = Path(sys.argv[2])
    out_path = Path(sys.argv[3])

    with base_path.open("r", encoding="utf-8") as f:
        base = json.load(f)

    with patch_path.open("r", encoding="utf-8") as f:
        patch = json.load(f)

    merged = deep_merge(base, patch)

    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Merged {len(patch.get('entries', {}))} actor entries into {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
