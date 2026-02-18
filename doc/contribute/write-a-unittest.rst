****************************
How to Write a New Unit Test
****************************

This project uses `pytest`_ as its testing framework.
This short guide explains how to add new unit tests so that they are clear, consistent, and easy to maintain.

File Structure
==============

* Unit tests go in :file:`tests/<module>`, where ``<module>`` is the name of a **group of related classes or functions**.
  It does not have to match the exact module name, but it should be meaningful and consistent.
* Test data belongs in :file:`tests/<module>/data`.

Keeping tests organized by feature area makes it easier to navigate the test suite and quickly find related tests.

Guidelines
==========

* **Use parametrization** with ``pytest.mark.parametrize`` to cover multiple inputs and outputs in a single test function.
  This keeps tests concise, avoids repetition, and makes failures easier to interpret.

* **Ensure unique test names or IDs** when using parametrization.
  Pytest automatically generates names, but in some cases they may be too similar. If that happens, provide explicit IDs:

  .. code-block:: python

      import pytest

      @pytest.mark.parametrize(
          "value, expected",
          [
              pytest.param(1, "one", id="int-1"),
              pytest.param(2, "two", id="int-2"),
          ]
      )
      def test_number_to_string(value, expected):
          assert number_to_string(value) == expected

  Alternatively, you can pass an ``ids`` list directly:

  .. code-block:: python

      @pytest.mark.parametrize(
          "value",
          [1, 2, 3],
          ids=["case-1", "case-2", "case-3"]
      )
      def test_is_positive(value):
          assert is_positive(value)

* Test IDs do **not** need to be creative. In doubt, simply use a **sequential numbering scheme** like ``case-1``, ``case-2``, etc.

Readable test names make failures much easier to diagnose, especially when running large test suites.

.. _pytest: https://docs.pytest.org/
