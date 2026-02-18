
# ANSI-Colored Terminal Output for Sphinx

`erbsland-sphinx-ansi` is a lightweight Sphinx extension that renders ANSI-colored and formatted terminal output directly in your documentation.

It is useful for command-line tools, build logs, and interactive sessions where terminal colors improve readability.

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

## Output Behavior

- HTML output: ANSI sequences are converted into styled output.
- Non-HTML output: ANSI formatting is stripped, leaving plain text.

## Requirements

- Python 3.10+
- Sphinx 8.0+ (required by the extension at runtime)

## Development

Install development dependencies:

```shell
pip install -r requirements-dev.txt
```

Run tests:

```shell
pytest
```

## Documentation

Project documentation is here: [https://sphinx-ansi.erbsland.dev](https://sphinx-ansi.erbsland.dev).

## License

Copyright (c) 2026 Tobias Erbsland / Erbsland DEV (<https://erbsland.dev>)

Licensed under the Apache License, Version 2.0.
See `LICENSE` for details.
