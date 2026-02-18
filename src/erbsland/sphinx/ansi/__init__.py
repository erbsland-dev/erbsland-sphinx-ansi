#  Copyright (c) 2026 Tobias Erbsland - https://erbsland.dev
#  SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
from typing import Any

from sphinx.util.fileutil import copy_asset


def _resolve_version() -> str:
    try:
        from ._version import __version__
    except ImportError:
        return "0.1.0"
    return __version__


ASSERT_SUBDIR = "erbsland-ansi"
STATIC_DIR = Path(__file__).parent / "static"
CSS_FILES = ["ansi.css"]


def _copy_static_files(app):
    if not getattr(app.builder, "supports", set()) & {"html"} and app.builder.name != "html":
        return  # ignore for non-HTML builders
    dest = Path(app.outdir) / "_static"
    dest.mkdir(parents=True, exist_ok=True)
    copy_asset(str(STATIC_DIR), str(dest))


def setup(app) -> dict[str, Any]:
    from erbsland.sphinx.ansi.parser import ANSIBlockDirective, ANSICodeParser

    app.require_sphinx("8.0")
    app.connect("builder-inited", _copy_static_files)
    for css_file in CSS_FILES:
        app.add_css_file(f"{ASSERT_SUBDIR}/{css_file}")
    app.add_directive("erbsland-ansi", ANSIBlockDirective)
    app.connect("doctree-resolved", ANSICodeParser())
    return {"version": _resolve_version(), "parallel_read_safe": True, "parallel_write_safe": True}
