:orphan:

.. _test_css_layout:

Test CSS Layout
===============

This page demonstrates the basic directives for testing CSS layout in Sphinx reStructuredText.

Headings
--------

.. code:: rst

   This is an example of a Heading.

      Subheading
      ----------

      This is an example of a subheading.

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

Badges
------

Inline badges can be used as a labelling component.
Badges are available in each semantic color, with filled and outline variants:

- :bdg:`plain badge`
- :bdg-primary:`primary`, :bdg-primary-line:`primary-line`
- :bdg-secondary:`secondary`, :bdg-secondary-line:`secondary-line`
- :bdg-success:`success`, :bdg-success-line:`success-line`
- :bdg-info:`info`, :bdg-info-line:`info-line`
- :bdg-warning:`warning`, :bdg-warning-line:`warning-line`
- :bdg-danger:`danger`, :bdg-danger-line:`danger-line`
- :bdg-light:`light`, :bdg-light-line:`light-line`
- :bdg-dark:`dark`, :bdg-dark-line:`dark-line`
