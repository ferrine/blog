:orphan:

.. _test_css_layout:

Test CSS Layout
===============


This page demonstrates the basic directives for testing CSS layout in Sphinx reStructuredText.




Headings
--------

* # with overline, for parts
* * with overline, for chapters
* =, for sections
* -, for subsections
* ^, for subsubsections
* “, for paragraphs

Example
^^^^^^^

Example
"""""""

Paragraphs
----------

This is an example of a paragraph. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Lists
-----

- This is an example of an unordered list item.
- Another unordered list item.

1. This is an example of an ordered list item.
2. Another ordered list item.

Code Blocks
-----------

Here's a code block with Python syntax highlighting:

.. code-block:: python

   def hello_world():
       print("Hello, World!")

   hello_world()

Admonitions
-----------

.. note::

   This is a note admonition. It should appear with a special styling to draw attention.

.. warning::

   This is a warning admonition. It should appear with a distinct styling to indicate caution.

Images
------

.. image:: https://via.placeholder.com/200x100
   :alt: Placeholder image
   :width: 200
   :height: 100
   :align: center

Tables
------

.. list-table:: Example Table
   :header-rows: 1
   :widths: 20 20 20

   * - Header 1
     - Header 2
     - Header 3
   * - Row 1, Cell 1
     - Row 1, Cell 2
     - Row 1, Cell 3
   * - Row 2, Cell 1
     - Row 2, Cell 2
     - Row 2, Cell 3

Links
-----

This is an example of an `external link <https://www.example.com>`_.

This is an example of an :ref:`internal link <test_css_layout>`.

.. card-carousel:: 1

   .. card:: Is your problem **white box**?

      If your problem is not white box it makes little sense to use Bayesian methods.
      The approach relies on clear understanding and reasoning about the problem.

   .. card:: How much do you know about the problem?

      The more you understand about the model and process it describes the better is the solution.
      No traditional approach takes this to the absolute and translates expert opinions to rigor definition.

   .. card:: Do you understand causal relations of your problem?

      Understanding relations is a half-way to build a Bayesian model.
      Ignoring these relations leads to biased estimates and decisions.