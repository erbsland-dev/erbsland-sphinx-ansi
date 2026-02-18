from erbsland.sphinx.ansi.attribute import ANSIAttribute


def test_to_class_name_returns_background_prefix_for_background_color():
    assert ANSIAttribute.BACKGROUND.to_class_name("red") == "background-red"


def test_to_class_name_returns_plain_value_for_non_background_attribute():
    assert ANSIAttribute.FOREGROUND.to_class_name("bright-green") == "bright-green"
