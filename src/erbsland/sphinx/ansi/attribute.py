#  Copyright (c) 2026 Tobias Erbsland - https://erbsland.dev
#  SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import enum


class ANSIAttribute(enum.Enum):
    BOLD = enum.auto()
    DIM = enum.auto()
    ITALIC = enum.auto()
    UNDERLINE = enum.auto()
    BLINK = enum.auto()
    REVERSE = enum.auto()
    HIDDEN = enum.auto()
    STRIKE = enum.auto()
    FOREGROUND = enum.auto()
    BACKGROUND = enum.auto()

    def to_class_name(self, value: str) -> str:
        if self == ANSIAttribute.BACKGROUND:
            return f"background-{value}"
        return value
