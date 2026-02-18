#  Copyright (c) 2026 Tobias Erbsland - https://erbsland.dev
#  SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
from typing import Any


def resolve_version() -> str:
    try:
        from ._version import __version__
    except ImportError:
        return "0.1.0"
    return __version__


def setup(app) -> dict[str, Any]:
    from erbsland.sphinx.ansi.parser import ANSIBlockDirective, ANSICodeParser

    app.add_static_dir(Path(__file__).parent / "static")
    app.add_css_file("erbsland-ansi/ansi.css")
    app.require_sphinx("8.0")
    app.add_directive("erbsland-ansi", ANSIBlockDirective)
    app.connect("doctree-resolved", ANSICodeParser())
    return {"version": resolve_version(), "parallel_read_safe": True, "parallel_write_safe": True}
