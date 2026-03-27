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

Demo
====

The following demo includes additional control sequences that are ignored during rendering.

.. erbsland-ansi::
    :escape-char: ␛

    ␛[?25l␛[92mcommand-line-help␛[37m [␛[35m<options>␛[37m]

    ␛[97mSummary
    ␛[37mThis demo prints a fictive command-line help page that adapts to the terminal width. On wider terminals it uses␛[97m  ␛[39m
    ␛[97mTerminal::printParagraph()␛[37m to keep descriptions aligned, wrapped, and easy to scan. Below 40 columns it␛[97m          ␛[39m
    ␛[37mintentionally falls back to plain line-oriented output so you can compare both styles.␛[97m                           ␛[39m

    ␛[97mPreview Paragraph
    ␛[93;44mPreview ␛[97mThis paragraph keeps a visible background so options like background mode, wrap markers, word breaks,␛[49m    ␛[39m
    ␛[97;44mellipsis handling, and alignment become easier to inspect while you adjust the rendering settings.␛[49m               ␛[39m

    ␛[97mOptions
    ␛[96m--help␛[37m/␛[93m-h␛[97m                               ␛[37mRender this formatted help output. The flag is mostly here so the demo␛[97m   ␛[39m
    ␛[97m                                        ␛[37mbehaves like a familiar command-line tool.␛[97m                               ␛[39m
    ␛[96m--terminal-width␛[37m/␛[93m-t␛[37m=␛[35m<columns>␛[39m           ␛[37mDisable automatic width detection and simulate a terminal width between␛[39m
                                            ␛[37m20 and 200 cells for deterministic wrapping.␛[39m
    ␛[96m--description-column␛[37m/␛[93m-c␛[37m=␛[35m<column>␛[39m        ␛[37mOverride the description tab stop for the options list. Valid values are␛[39m
                                            ␛[37m12 to 60.␛[39m
    ␛[96m--alignment␛[37m/␛[93m-a␛[37m=␛[35m<left|center|right>␛[39m      ␛[37mChoose the horizontal alignment used for the wrapped preview paragraphs.␛[39m
    ␛[96m--line-indent␛[37m/␛[93m-l␛[37m=␛[35m<columns>␛[39m              ␛[37mIndent the preview paragraphs by 0 to 10 columns before any wrapping␛[39m
                                            ␛[37mtakes place.␛[39m
    ␛[96m--first-line-indent␛[37m/␛[93m-f␛[37m=␛[35m<columns>␛[39m        ␛[37mOverride the first-line indent for preview paragraphs. Valid values are 0␛[39m
                                            ␛[37mto 12.␛[39m
    ␛[96m--wrapped-line-indent␛[37m/␛[93m-w␛[37m=␛[35m<columns>␛[39m      ␛[37mOverride the indentation of wrapped lines. Values between 0 and 30 make␛[39m
                                            ␛[37mthe effect easy to inspect.␛[39m
    ␛[96m--background-mode␛[37m/␛[93m-b␛[37m=␛[35m<mode>␛[39m             ␛[37mSet the background fill strategy: default, wrapped-left, wrapped-right,␛[39m
                                            ␛[37mwrapped-both, full-right, or full-both.␛[39m
    ␛[96m--line-break-start-mark␛[37m/␛[93m-s␛[37m=␛[35m<text>␛[39m       ␛[37mInsert a one- or two-character marker at the start of each wrapped␛[39m
                                            ␛[37mcontinuation line.␛[39m
    ␛[96m--line-break-end-mark␛[37m/␛[93m-m␛[37m=␛[35m<text>␛[39m         ␛[37mAppend a one- or two-character marker at the right edge when a line␛[39m
                                            ␛[37mwraps.␛[39m
    ␛[96m--paragraph-spacing␛[37m/␛[93m-p␛[37m=␛[35m<single|double>␛[39m  ␛[37mSwitch between compact paragraphs or double-spaced output with one empty␛[39m
                                            ␛[37mrow in between.␛[39m
    ␛[96m--word-separators␛[37m/␛[93m-i␛[37m=␛[35m<tokens>␛[39m           ␛[37mUse comma-separated separator tokens such as space,tab,slash or␛[39m
                                            ␛[37mone-character literals like ; and |.␛[39m
    ␛[96m--word-break-mark␛[37m/␛[93m-k␛[37m=␛[35m<char>␛[39m             ␛[37mSet the single character inserted when a word is split because it does␛[39m
                                            ␛[37mnot fit on the current line.␛[39m
    ␛[96m--maximum-line-wraps␛[37m/␛[93m-r␛[37m=␛[35m<count>␛[39m         ␛[37mLimit the number of automatic wraps per paragraph. Use 0 for unlimited or␛[39m
                                            ␛[37mvalues up to 8 to trigger ellipsis behaviour.␛[39m
    ␛[96m--paragraph-ellipsis-mark␛[37m/␛[93m-x␛[37m=␛[35m<text>␛[39m     ␛[37mChoose the marker that signals clipped paragraphs after the configured␛[39m
                                            ␛[37mwrap limit has been reached.␛[39m
    ␛[96m--tab-stops␛[37m/␛[93m-u␛[37m=␛[35m<list>␛[39m                   ␛[37mProvide comma-separated tab stops like 1,24,40 or use wrapped to align a␛[39m
                                            ␛[37mstop with the wrapped-line indent.␛[39m
    ␛[96m--on-error␛[37m/␛[93m-o␛[37m=␛[35m<plain|empty>␛[39m             ␛[37mChoose the fallback when the paragraph cannot be laid out: plain output␛[39m
                                            ␛[37mor empty output.␛[39m

    ␛[?25h␛[0m␛[?25h
    ␛[0m␛[?25h

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
