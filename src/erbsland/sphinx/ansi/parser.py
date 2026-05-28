#  Copyright (c) 2026 Tobias Erbsland - https://erbsland.dev
#  SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import re

from docutils import nodes
from docutils.parsers import rst
from docutils.parsers.rst.directives import single_char_or_unicode

from erbsland.sphinx.ansi.attribute import ANSIAttribute
from erbsland.sphinx.ansi.definition import definition_from_ansi_code

DEFAULT_THEME = "erbsland-ansi"


class ANSILiteralBlock(nodes.container):
    """The literal_block node, for ANSI color codes."""

    def __init__(self, rawsource: str = "", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)


class ANSICodeParser(object):
    """Either remove ANSI formatting from a block, or colorize it for HTML output."""

    RE_ANSI_CSI_SEQUENCE: re.Pattern[str] = re.compile(r"\x1b\[([0-?]*)([ -/]*)([@-~])")

    def __call__(self, app, doctree, docname):
        if app.builder.name != "html":
            for ansi_block in doctree.traverse(ANSILiteralBlock):
                self._remove_ansi_formatting(ansi_block)
        else:
            for ansi_block in doctree.traverse(ANSILiteralBlock):
                self._colorize_block_contents(ansi_block)

    def _remove_ansi_formatting(self, block: ANSILiteralBlock):
        cleaned_text = self.RE_ANSI_CSI_SEQUENCE.sub("", block.rawsource)
        block.replace_self(nodes.literal_block(cleaned_text, cleaned_text))

    def _colorize_block_contents(self, block: ANSILiteralBlock):
        theme = block.get("ansi_theme", DEFAULT_THEME)
        block["classes"].extend([f"{theme}-block", "nohighlight"])
        block.clear()
        pre_block = nodes.literal_block("", "", classes=[f"{theme}-block", "nohighlight"])
        block += pre_block
        current_attributes: dict[ANSIAttribute, str] = {}
        last_end = 0
        for match in self.RE_ANSI_CSI_SEQUENCE.finditer(block.rawsource):
            head = block.rawsource[last_end : match.start()]
            if head:
                pre_block += self._create_formatting_node(head, current_attributes, theme)
            self._apply_csi_sequence(match.group(1), match.group(3), current_attributes)
            last_end = match.end()
        tail = block.rawsource[last_end:]
        if tail:
            pre_block += self._create_formatting_node(tail, current_attributes, theme)

    def _create_formatting_node(
        self,
        text: str,
        current_attributes: dict[ANSIAttribute, str],
        theme: str,
    ):
        classes = [f"{theme}-{attr.to_class_name(value)}" for attr, value in current_attributes.items()]
        return nodes.inline("", text, classes=classes)

    def _update_attributes(self, code: int, attributes: dict[ANSIAttribute, str]):
        definition = definition_from_ansi_code(code)
        if definition is None:
            return
        attributes_to_set = []
        if isinstance(definition.attribute, ANSIAttribute):
            attributes_to_set = [definition.attribute]
        elif isinstance(definition.attribute, list):
            attributes_to_set = definition.attribute
        for attr in attributes_to_set:
            if definition.value:
                attributes[attr] = definition.value
            elif attr in attributes:
                del attributes[attr]

    def _apply_csi_sequence(self, parameters: str, final_byte: str, attributes: dict[ANSIAttribute, str]):
        if final_byte != "m":
            return
        for code in self._parse_sgr_parameters(parameters):
            self._update_attributes(code, attributes)

    @staticmethod
    def _parse_sgr_parameters(parameters: str) -> list[int]:
        if not parameters:
            return [0]
        codes = []
        for parameter in parameters.split(";"):
            if not parameter:
                codes.append(0)
                continue
            if not parameter.isdigit():
                return []
            codes.append(int(parameter))
        return codes


class ANSIBlockDirective(rst.Directive):
    """
    A directive to include ANSI formatted output as a literal block

    The parameter ``escape-char`` can be used to replace the escape character with a different character.
    The parameter ``theme`` can be used to replace the CSS class prefix.
    """

    has_content = True
    option_spec = {
        "escape-char": single_char_or_unicode,
        "theme": rst.directives.unchanged,
    }

    def run(self):
        text = "\n".join(self.content)
        if "escape-char" in self.options:
            text = text.replace(self.options["escape-char"], "\x1b")
        block = ANSILiteralBlock(text)
        if "theme" in self.options:
            block["ansi_theme"] = self.options["theme"]
        return [block]
