************
Requirements
************

Runtime Requirements
====================

To use this extension, you only need **Python 3.10 or newer**.
There are no external dependencies required at runtime.

Development Requirements
========================

If you want to work on this extension, all required dependencies
are listed in the ``requirements-dev.txt`` file.

You can install them with:

.. code-block:: shell

    pip install -r requirements-dev.txt

The development dependencies include:

* **pytest**  
  Used to run the unit tests.

* **pytest-xdist**  
  The project contains more than 10,000 tests. ``xdist`` is used to run them in parallel for faster feedback.

* **pytest-cov**  
  Adds test coverage reporting to ``pytest``.

* **coverage**  
  Provides detailed coverage checks and reports.

* **black**  
  Automatically formats the code to ensure consistent style.

* **hatch**  
  Tool for building, managing, and publishing the package.

* **hatch-vcs**  
  Hatch extension that integrates version control metadata into builds.
