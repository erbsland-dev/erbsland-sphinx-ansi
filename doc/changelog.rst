*********
Changelog
*********

Version 1.2 — 2026-05-28
========================

This release focuses on improving compatibility with JavaScript-based syntax highlighters, strengthening the build infrastructure, and streamlining development workflows.

* Wrapped the ``<pre>`` output in an additional ``<div>`` container to improve compatibility with JavaScript-based Pygments formatters.
* Added the ``nohighlight`` CSS class to both the ``<pre>`` and ``<div>`` elements for the same compatibility reasons.
* Refactored the internal AST type into a dedicated container structure.
* Hardened the build process and improved the GitHub workflow configuration.
* Introduced additional build utilities, including a ``pre_commit`` action.
* Updated all project dependencies to their latest compatible versions.

