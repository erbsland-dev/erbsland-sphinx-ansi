ANSI-Colored Terminal Output for Sphinx
========================================

``erbsland-sphinx-ansi`` is a lightweight Sphinx extension that renders
ANSI-colored and formatted terminal output directly in your documentation.

It is especially useful when documenting command-line tools, build logs,
or interactive sessions where color improves readability and realism.

Features
========

*   Optional ``escape-char`` parameter that allows you to replace the ANSI escape character (``\x1b``) with a visible placeholder character inside reStructuredText sources.
*   Optional ``theme`` parameter that allows you to customize the CSS class prefix used for styling.
*   Works with both HTML and non-HTML output formats.

Quick Start
===========

Installation
------------

Install the package from PyPI:

.. code-block:: shell

    pip install erbsland-sphinx-ansi

Configuration
-------------

Enable the extension in your ``conf.py``:

.. code-block:: python

    extensions = [
        # ...
        "erbsland.sphinx.ansi",
    ]

No additional configuration is required.

Usage
=====

To render ANSI-colored output, use the ``erbsland-ansi`` directive:

.. code-block:: rst

    .. erbsland-ansi::
        :escape-char: ␛

        ␛[32m[sphinx-autobuild] ␛[36mStarting initial build␛[0m
        ␛[32m[sphinx-autobuild] ␛[34m> python -m sphinx build doc _build␛[0m
        ␛[32m[sphinx-autobuild] ␛[36mServing on http://127.0.0.1:9000␛[0m
        ␛[32m[sphinx-autobuild] ␛[36mWaiting to detect changes...␛[0m

The ``:escape-char:`` option defines which character in the source file
represents the ANSI escape character. This makes the escape sequences
visible and editable in your documentation sources.

If the option is omitted, the directive expects real ANSI escape sequences.

Rendered Example
================

The following block demonstrates the rendered output:

.. erbsland-ansi::
    :escape-char: ␛

    ␛[32m[sphinx-autobuild] ␛[36mStarting initial build␛[0m
    ␛[32m[sphinx-autobuild] ␛[34m> python -m sphinx build doc _build␛[0m
    ␛[32m[sphinx-autobuild] ␛[36mServing on http://127.0.0.1:9000␛[0m
    ␛[32m[sphinx-autobuild] ␛[36mWaiting to detect changes...␛[0m

When building HTML documentation, the ANSI color codes are converted into
styled output that closely resembles the original terminal appearance.

Custom Theming
==============

Use the parameter ``theme`` to customize the CSS class prefix used for styling:

.. code-block:: rst

    .. erbsland-ansi::
        :escape-char: ␛
        :theme: my-theme

        ␛[32m[sphinx-autobuild] ␛[36mStarting initial build␛[0m
        ␛[32m[sphinx-autobuild] ␛[34m> python -m sphinx build doc _build␛[0m
        ␛[32m[sphinx-autobuild] ␛[36mServing on http://127.0.0.1:9000␛[0m
        ␛[32m[sphinx-autobuild] ␛[36mWaiting to detect changes...␛[0m

Create a CSS file ``static/my-theme.css`` with the following content:

.. literalinclude:: _static/custom-theme.css
   :language: css

Output with the custom theme:

.. erbsland-ansi::
    :escape-char: ␛
    :theme: my-theme

    ␛[32m[sphinx-autobuild] ␛[36mStarting initial build␛[0m
    ␛[32m[sphinx-autobuild] ␛[34m> python -m sphinx build doc _build␛[0m
    ␛[32m[sphinx-autobuild] ␛[36mServing on http://127.0.0.1:9000␛[0m
    ␛[32m[sphinx-autobuild] ␛[36mWaiting to detect changes...␛[0m


Contents
========

.. toctree::
    :maxdepth: 2

    license
    requirements
    contribute/index
    credits

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
