Changes
=======

2.0.0 (2026-02-03)
------------------

- Refactor package layout to use ``pyproject.toml`` and implicit namespace packages.
  [rnix]

- Extend JS by ``chosen_on_array_add`` and ``register_array_subscribers``
  functions to enable usage in ``yafowil.widget.array``.
  [lenadax]

- Prevent initialize of widget if part of array template.
  [lenadax]

- Rewrite JavaScript using ES6.
  [rnix]


1.4 (2025-11-03)
----------------

- Pin upper versions of dependencies.
  [lenadax]


1.3 (2018-07-16)
----------------

- Python 3 compatibility.
  [rnix]

- Convert doctests to unittests.
  [rnix]


1.2 (2017-03-01)
----------------

- Use ``yafowil.utils.entry_point`` decorator.
  [rnix, 2016-06-28]


1.1 (2015-01-23)
----------------

- Upgrade to Chosen 1.1.
  [rnix]

- Add Bootstrap 3.2 compatible styles
  [rnix]


1.0
---

- For data-attributes, don't use wrapper element but define them on the field
  tag directly.
  [thet]

- Make it work.
  [thet]
