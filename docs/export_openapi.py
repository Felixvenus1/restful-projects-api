"""Export the generated OpenAPI schema to docs/openapi.json.

Run from the project root:

    python docs/export_openapi.py

This produces a concrete, version-controllable artefact of the API contract that
backs the live Swagger UI at /docs (ARTEFACT 02-D companion).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.app.main import app  # noqa: E402


def main() -> None:
    schema = app.openapi()
    out = Path(__file__).resolve().parent / "openapi.json"
    out.write_text(json.dumps(schema, indent=2), encoding="utf-8")
    paths = sorted(schema.get("paths", {}))
    print(f"Wrote {out} ({len(paths)} paths)")
    for p in paths:
        print(f"  {p}")


if __name__ == "__main__":
    main()
