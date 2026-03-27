*****************************
ErbslandDEV Python Code Style
*****************************

This guide defines the core Python style conventions used across all ErbslandDEV codebases.  
It ensures that our projects remain consistent, easy to read, and maintainable for everyone.

Code Format with Black
======================

We use the `Black Formatter`_ to format all Python code in a consistent way.  
Code should always be formatted automatically instead of manually adjusted. This saves time, prevents bikeshedding, and helps everyone focus on the actual logic.

Run Black with the following command:

.. code-block:: shell

    $ black --line-length 120 src tests

We intentionally set the line length to **120 characters** to allow for slightly longer, yet still readable, lines of code.  
This helps reduce unnecessary line breaks, especially in test cases and function signatures.

API Documentation
=================

For API documentation, we use the `Sphinx`_ documentation generator.  
Parts of the documentation is built directly from docstrings in the code, so keeping those clear and accurate is essential.

Docstrings
----------

All public interfaces should be documented using *Sphinx/reST-style* docstrings.  

* If the function signature already makes the parameters and return type clear, a **single-line docstring** is sufficient.  
* If the function has more complex behavior, provide a **multi-line docstring** including parameters, return values, and raised exceptions.

Examples:

.. code-block:: python

    def method1() -> None:
        """Perform a simple one-line task."""

    def method2(path: str, count: int) -> str:
        """
        Perform an operation based on ``path`` and ``count``.

        :param path: The file system path to process.
        :param count: The number of iterations to run.
        :returns: A string containing the processed result.
        :raises ValueError: If the provided path is invalid.
        """

When writing docstrings, always describe the **why** and **what**, not just the **how**.  
This helps future developers (including yourself!) understand the intent behind your code.

Type Hints
----------

We consistently use **type hints** throughout the codebase.  
They serve three purposes:

* Documenting the API directly in the function signature.  
* Providing better IDE support (auto-completion and error detection).  
* Enabling static analysis tools such as ``mypy`` or ``pyright``.  

Using type hints is not optional — it’s an integral part of how we write Python at ErbslandDEV.  

File Size Limits
================

We prefer many **small, focused files** over a few very large ones.
Smaller files are easier to read, review, and maintain, and they naturally encourage a clean project structure.

As a rule of thumb:

* Each file *should* stay **under 500 lines**.
* Each file *must* stay **under 1000 lines**.

If a file grows too large, consider breaking it into smaller parts:

* Move related functionality into a dedicated **subpackage** with multiple modules.
* If you are dealing with a large class, **refactor it using composition or delegation**. This not only reduces file size but also improves readability and testability.

Keeping files concise makes it easier for new contributors to understand the project and helps avoid the “god module” or “god class” anti-patterns.


.. _Black Formatter: https://black.readthedocs.io/
.. _Sphinx: https://www.sphinx-doc.org/