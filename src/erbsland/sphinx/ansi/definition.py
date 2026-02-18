#  Copyright (c) 2026 Tobias Erbsland - https://erbsland.dev
#  SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from erbsland.sphinx.ansi.attribute import ANSIAttribute


@dataclass
class ANSIAttributeDefinition:
    attribute: Union[ANSIAttribute, list[ANSIAttribute]]
    value: str


ANSI_CODE_TO_COLOR_NAME: dict[int, str] = {
    0: "black",
    1: "red",
    2: "green",
    3: "yellow",
    4: "blue",
    5: "magenta",
    6: "cyan",
    7: "white",
}


CODE_ATTRIBUTE_MAP: dict[int, ANSIAttributeDefinition] = {
    0: ANSIAttributeDefinition(
        [
            ANSIAttribute.BOLD,
            ANSIAttribute.DIM,
            ANSIAttribute.ITALIC,
            ANSIAttribute.UNDERLINE,
            ANSIAttribute.BLINK,
            ANSIAttribute.REVERSE,
            ANSIAttribute.HIDDEN,
            ANSIAttribute.STRIKE,
            ANSIAttribute.FOREGROUND,
            ANSIAttribute.BACKGROUND,
        ],
        "",
    ),
    1: ANSIAttributeDefinition(ANSIAttribute.BOLD, "bold"),
    2: ANSIAttributeDefinition(ANSIAttribute.DIM, "dim"),
    3: ANSIAttributeDefinition(ANSIAttribute.ITALIC, "italic"),
    4: ANSIAttributeDefinition(ANSIAttribute.UNDERLINE, "underline"),
    5: ANSIAttributeDefinition(ANSIAttribute.BLINK, "blink"),
    6: ANSIAttributeDefinition(ANSIAttribute.REVERSE, "reverse"),
    7: ANSIAttributeDefinition(ANSIAttribute.HIDDEN, "hidden"),
    8: ANSIAttributeDefinition(ANSIAttribute.STRIKE, "strike"),
    22: ANSIAttributeDefinition([ANSIAttribute.BOLD, ANSIAttribute.DIM], ""),
    23: ANSIAttributeDefinition(ANSIAttribute.ITALIC, ""),
    24: ANSIAttributeDefinition(ANSIAttribute.UNDERLINE, ""),
    25: ANSIAttributeDefinition(ANSIAttribute.BLINK, ""),
    26: ANSIAttributeDefinition(ANSIAttribute.REVERSE, ""),
    27: ANSIAttributeDefinition(ANSIAttribute.HIDDEN, ""),
    28: ANSIAttributeDefinition(ANSIAttribute.STRIKE, ""),
}


def definition_from_ansi_code(code: int) -> ANSIAttributeDefinition | None:
    if code in CODE_ATTRIBUTE_MAP:
        return CODE_ATTRIBUTE_MAP[code]
    elif 20 <= code <= 29:
        return ANSIAttributeDefinition(ANSIAttribute.ITALIC, ANSI_CODE_TO_COLOR_NAME[code % 10])
    elif 30 <= code <= 37:
        return ANSIAttributeDefinition(ANSIAttribute.FOREGROUND, ANSI_CODE_TO_COLOR_NAME[code % 10])
    elif 40 <= code <= 47:
        return ANSIAttributeDefinition(ANSIAttribute.BACKGROUND, ANSI_CODE_TO_COLOR_NAME[code % 10])
    elif 90 <= code <= 97:
        return ANSIAttributeDefinition(ANSIAttribute.FOREGROUND, f"bright-{ANSI_CODE_TO_COLOR_NAME[code % 10]}")
    elif 100 <= code <= 107:
        return ANSIAttributeDefinition(ANSIAttribute.BACKGROUND, f"bright-{ANSI_CODE_TO_COLOR_NAME[code % 10]}")
    else:
        return None  # Ignore unknown codes.
