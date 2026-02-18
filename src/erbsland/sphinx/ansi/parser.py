#  Copyright (c) 2026 Tobias Erbsland - https://erbsland.dev
#  SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import re

from docutils import nodes
from docutils.parsers import rst
from docutils.parsers.rst.directives import single_char_or_unicode

from erbsland.sphinx.ansi.attribute import ANSIAttribute
from erbsland.sphinx.ansi.definition import definition_from_ansi_code


class ANSILiteralBlock(nodes.literal_block):
    """The literal_block node, for ANSI color codes."""

    pass


class ANSICodeParser(object):
    """Either remove ANSI formatting from a block, or colorize it for HTML output."""

    RE_ANSI_FORMAT_SEQUENCE: re.Pattern[str] = re.compile(r"\x1b\[([^m]+)m")

    def __call__(self, app, doctree, docname):
        if app.builder.name != "html":
            for ansi_block in doctree.traverse(ANSILiteralBlock):
                self._remove_ansi_formatting(ansi_block)
        else:
            for ansi_block in doctree.traverse(ANSILiteralBlock):
                self._colorize_block_contents(ansi_block)

    def _remove_ansi_formatting(self, block: ANSILiteralBlock):
        cleaned_text = self.RE_ANSI_FORMAT_SEQUENCE.sub("", block.rawsource)
        block.replace_self(nodes.literal_block(cleaned_text, cleaned_text))

    def _colorize_block_contents(self, block: ANSILiteralBlock):
        new_literal = nodes.literal_block(block.rawsource, classes=["erbsland-ansi-block"])
        block.replace_self(new_literal)

        current_attributes: dict[ANSIAttribute, str] = {}
        last_end = 0
        nodes_with_formatting = []
        for match in self.RE_ANSI_FORMAT_SEQUENCE.finditer(block.rawsource):
            head = block.rawsource[last_end : match.start()]
            if head:
                nodes_with_formatting.append(self._create_formatting_node(head, current_attributes))
            for code in [int(c) for c in match.group(1).split(";")]:
                self._update_attributes(code, current_attributes)
            last_end = match.end()
        tail = block.rawsource[last_end:]

        nodes_with_formatting.append(self._create_formatting_node(tail, current_attributes))
        new_literal.extend(nodes_with_formatting)

    def _create_formatting_node(self, text: str, current_attributes: dict[ANSIAttribute, str]):
        if current_attributes:
            classes = list([f"erbsland-ansi-{attr.to_class_name(value)}" for attr, value in current_attributes.items()])
            return nodes.inline(text=text, classes=classes)
        return nodes.Text(text)

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


class ANSIBlockDirective(rst.Directive):
    """
    A directive to include ANSI formatted output as a literal block

    The parameter ``escape-char`` can be used to replace the escape character with a different character.
    """

    has_content = True
    option_spec = {
        "escape-char": single_char_or_unicode,
    }

    def run(self):
        text = "\n".join(self.content)
        if "escape-char" in self.options:
            text = text.replace(self.options["escape-char"], "\x1b")
        return [ANSILiteralBlock(text, text)]
