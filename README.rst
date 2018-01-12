===============================
pytest-doctest-ellipsis-markers
===============================

.. image:: https://travis-ci.org/wooyek/pytest-doctest-ellipsis-markers.svg?branch=master
    :target: https://travis-ci.org/wooyek/pytest-doctest-ellipsis-markers
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/wooyek/pytest-doctest-ellipsis-markers?branch=master
    :target: https://ci.appveyor.com/project/wooyek/pytest-doctest-ellipsis-markers/branch/master
    :alt: See Build Status on AppVeyor

Setup additional values for ELLIPSIS_MARKER for doctests

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


Features
--------


Doctest has problems with matching default ELLIPSIS_MARKER at the begging of line and
interprets them as line continuation characters and not as ellipsis for the output.
The easy way was to use `# doctest: +SKIP`::

    >>> u'Tanie dranie niesłychanie' # doctest: +SKIP
    ...

Without `SKIP` it would not work. But then the statement is not tested :(

This plugin cant extend `ELLIPSIS_MARKER` mathing a little
without actually changing the default `ELLIPSIS_MARKER` value::

    >>> u'Adios pomidory'
    '...'


Installation
------------

You can install "pytest-doctest-ellipsis-markers" via `pip`_ from `PyPI`_::

    $ pip install pytest-doctest-ellipsis-markers


Usage
-----

* TODO

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-doctest-ellipsis-markers" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/wooyek/pytest-doctest-ellipsis-markers/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
