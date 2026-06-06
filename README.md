# ANSI-Colored Terminal Output for Sphinx

`erbsland-sphinx-ansi` is a lightweight Sphinx extension that renders ANSI-colored and formatted terminal output directly in your documentation.

It is useful for command-line tools, build logs, and terminal sessions where ANSI colors improve readability.

## Features

- Render ANSI-colored terminal output in Sphinx documentation.
- Support for standard ANSI text styles and colors.
- Optional `escape-char` parameter for readable source files.
- Optional `theme` parameter for custom CSS styling.
- Works with both HTML and non-HTML output formats.

## Installation

```shell
pip install erbsland-sphinx-ansi
```

## Quick Start

Enable the extension in `conf.py`:

```python
extensions = [
    # ...
    "erbsland.sphinx.ansi",
]
```

Use the `erbsland-ansi` directive:

```rst
.. erbsland-ansi::
    :escape-char: ␛

    ␛[32m[sphinx-autobuild] ␛[36mStarting initial build␛[0m
    ␛[32m[sphinx-autobuild] ␛[34m> python -m sphinx build doc _build␛[0m
    ␛[32m[sphinx-autobuild] ␛[36mServing on http://127.0.0.1:9000␛[0m
    ␛[32m[sphinx-autobuild] ␛[36mWaiting to detect changes...␛[0m
```

`escape-char` is optional. If set, this character is replaced with the ANSI escape character (`\x1b`) when parsing the directive content. If omitted, provide real ANSI escape sequences directly.

## Output Formats

- HTML output: ANSI sequences are converted into styled output.
- Non-HTML output: ANSI formatting is stripped, leaving plain text.

## Limitations

`erbsland-sphinx-ansi` renders ANSI text formatting but is **not a terminal emulator**.

The extension supports ANSI colors and text styles, but does not emulate terminal behavior such as:

- Cursor movement
- Screen clearing
- Alternate screen buffers
- Character-set switching
- Interactive terminal updates

Output that relies on terminal emulation may not render as expected.

For such cases, preprocess the captured output with `erbsland-ansi-convert`:

```shell
pip install erbsland-ansi-convert

erbsland-ansi-convert input.ansi -o output.ansi
```

This tool emulates a terminal and writes the final screen contents as ANSI-formatted text that can be rendered correctly by `erbsland-sphinx-ansi`.

## Requirements

- Python 3.10+
- Sphinx 8.0+ (required by the extension at runtime)

## Development

- Python 3.13+

Install development dependencies:

```shell
pip install -r requirements-dev.txt
```

Run tests:

```shell
pytest
```

## Documentation

Project documentation is available at:

<https://sphinx-ansi.erbsland.dev>

## License

Copyright (c) 2026 Tobias Erbsland / Erbsland DEV (<https://erbsland.dev>)

Licensed under the Apache License, Version 2.0.
See `LICENSE` for details.
