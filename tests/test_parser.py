import pytest

pytest.importorskip("docutils")

from docutils import nodes

import erbsland.sphinx.ansi as ansi_extension
from erbsland.sphinx.ansi.attribute import ANSIAttribute
from erbsland.sphinx.ansi.parser import ANSIBlockDirective, ANSICodeParser, ANSILiteralBlock


class _Builder:
    def __init__(self, name: str):
        self.name = name


class _App:
    def __init__(self, builder_name: str):
        self.builder = _Builder(builder_name)


class _DirectiveApp:
    def __init__(self):
        self.static_dirs = []
        self.css_files = []
        self.required_sphinx = []
        self.directives = []
        self.connections = []

    def add_static_dir(self, path):
        self.static_dirs.append(path)

    def add_css_file(self, path):
        self.css_files.append(path)

    def require_sphinx(self, version):
        self.required_sphinx.append(version)

    def add_directive(self, name, directive):
        self.directives.append((name, directive))

    def connect(self, event_name, callback):
        self.connections.append((event_name, callback))


class _DocTree:
    def __init__(self, ansi_block: ANSILiteralBlock):
        self.container = nodes.section()
        self.container += ansi_block

    def traverse(self, node_type):
        if node_type is ANSILiteralBlock:
            return [n for n in self.container.children if isinstance(n, ANSILiteralBlock)]
        return []


def test_remove_ansi_formatting_replaces_literal_block_with_plain_text():
    parser = ANSICodeParser()
    block = ANSILiteralBlock("Hello \x1b[31mRed\x1b[0m", "Hello \x1b[31mRed\x1b[0m")
    container = nodes.section()
    container += block

    parser._remove_ansi_formatting(block)

    replaced = container.children[0]
    assert isinstance(replaced, nodes.literal_block)
    assert replaced.rawsource == "Hello Red"
    assert replaced.astext() == "Hello Red"


def test_update_attributes_sets_and_clears_attribute_state():
    parser = ANSICodeParser()
    attributes = {}

    parser._update_attributes(31, attributes)
    assert attributes == {ANSIAttribute.FOREGROUND: "red"}

    parser._update_attributes(0, attributes)
    assert attributes == {}


def test_colorize_block_contents_splits_text_and_applies_css_classes():
    parser = ANSICodeParser()
    block = ANSILiteralBlock("A\x1b[31mB\x1b[44mC\x1b[0mD", "A\x1b[31mB\x1b[44mC\x1b[0mD")
    block["ansi_theme"] = "custom-theme"
    container = nodes.section()
    container += block

    parser._colorize_block_contents(block)

    replaced = container.children[0]
    assert "custom-theme-block" in replaced["classes"]
    children = list(replaced.children)
    assert len(children) == 4

    assert isinstance(children[0], nodes.Text)
    assert children[0].astext() == "A"

    assert isinstance(children[1], nodes.inline)
    assert children[1].astext() == "B"
    assert children[1]["classes"] == ["custom-theme-red"]

    assert isinstance(children[2], nodes.inline)
    assert children[2].astext() == "C"
    assert sorted(children[2]["classes"]) == ["custom-theme-background-blue", "custom-theme-red"]

    assert isinstance(children[3], nodes.Text)
    assert children[3].astext() == "D"


def test_call_switches_behavior_for_non_html_and_html_builders():
    parser = ANSICodeParser()

    text = "A\x1b[31mB\x1b[0m"
    non_html_block = ANSILiteralBlock(text, text)
    non_html_tree = _DocTree(non_html_block)
    parser(_App("latex"), non_html_tree, "index")
    assert non_html_tree.container.children[0].astext() == "AB"

    html_block = ANSILiteralBlock(text, text)
    html_tree = _DocTree(html_block)
    parser(_App("html"), html_tree, "index")
    assert "erbsland-ansi-block" in html_tree.container.children[0]["classes"]


def test_ansi_block_directive_run_replaces_escape_character():
    directive = ANSIBlockDirective.__new__(ANSIBlockDirective)
    directive.content = ["X#[31mY#[0m"]
    directive.options = {"escape-char": "#", "theme": "custom-theme"}

    result = directive.run()

    assert len(result) == 1
    assert isinstance(result[0], ANSILiteralBlock)
    assert result[0].rawsource == "X\x1b[31mY\x1b[0m"
    assert result[0]["ansi_theme"] == "custom-theme"


def test_setup_registers_static_assets_directive_and_callback():
    app = _DirectiveApp()

    result = ansi_extension.setup(app)

    assert app.css_files == ["erbsland-ansi/ansi.css"]
    assert app.required_sphinx == ["8.0"]
    assert app.directives == [("erbsland-ansi", ANSIBlockDirective)]
    assert len(app.connections) == 2
    assert app.connections[0][0] == "builder-inited"
    assert app.connections[1][0] == "doctree-resolved"
    assert isinstance(app.connections[1][1], ANSICodeParser)
    assert result["parallel_read_safe"] is True
    assert result["parallel_write_safe"] is True
