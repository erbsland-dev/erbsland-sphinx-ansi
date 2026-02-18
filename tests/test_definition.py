from erbsland.sphinx.ansi.attribute import ANSIAttribute
from erbsland.sphinx.ansi.definition import definition_from_ansi_code


def test_definition_from_ansi_code_returns_mapped_attribute_for_basic_style_code():
    definition = definition_from_ansi_code(1)

    assert definition is not None
    assert definition.attribute == ANSIAttribute.BOLD
    assert definition.value == "bold"


def test_definition_from_ansi_code_returns_foreground_color_for_standard_color_code():
    definition = definition_from_ansi_code(34)

    assert definition is not None
    assert definition.attribute == ANSIAttribute.FOREGROUND
    assert definition.value == "blue"


def test_definition_from_ansi_code_returns_background_color_for_standard_color_code():
    definition = definition_from_ansi_code(43)

    assert definition is not None
    assert definition.attribute == ANSIAttribute.BACKGROUND
    assert definition.value == "yellow"


def test_definition_from_ansi_code_returns_bright_colors_for_high_intensity_codes():
    foreground = definition_from_ansi_code(92)
    background = definition_from_ansi_code(104)

    assert foreground is not None
    assert foreground.attribute == ANSIAttribute.FOREGROUND
    assert foreground.value == "bright-green"

    assert background is not None
    assert background.attribute == ANSIAttribute.BACKGROUND
    assert background.value == "bright-blue"


def test_definition_from_ansi_code_returns_reset_definition_for_code_zero():
    definition = definition_from_ansi_code(0)

    assert definition is not None
    assert isinstance(definition.attribute, list)
    assert ANSIAttribute.FOREGROUND in definition.attribute
    assert ANSIAttribute.BACKGROUND in definition.attribute
    assert definition.value == ""


def test_definition_from_ansi_code_returns_none_for_unknown_code():
    assert definition_from_ansi_code(999) is None
