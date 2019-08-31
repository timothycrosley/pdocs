
[![Build Status](https://travis-ci.org/mitmproxy/pdocs.svg?branch=master)](https://travis-ci.org/mitmproxy/pdocs)
[![PyPI Version](https://shields.mitmproxy.org/pypi/v/pdocs.svg)](https://pypi.org/project/pdocs/)

`pdocs` is a library and a command line program to discover the public
interface of a Python module or package. The `pdocs` script can be used to
generate plain text or HTML of a module's public interface, or it can be used
to run an HTTP server that serves generated HTML for installed modules.


Installation
------------

    pip install pdocs


Features
--------

* Support for documenting data representation by traversing the abstract syntax
  to find docstrings for module, class and instance variables.
* For cases where docstrings aren't appropriate (like a
  [namedtuple](http://docs.python.org/2.7/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields)),
  the special variable `__pdocs__` can be used in your module to
  document any identifier in your public interface.
* Usage is simple. Just write your documentation as Markdown. There are no
  added special syntax rules.
* `pdocs` respects your `__all__` variable when present.
* `pdocs` will automatically link identifiers in your docstrings to its
  corresponding documentation.
* When `pdocs` is run as an HTTP server, external linking is supported between
  packages.
* The `pdocs` HTTP server will cache generated documentation and automatically
  regenerate it if the source code has been updated.
* When available, source code for modules, functions and classes can be viewed
  in the HTML documentation.
* Inheritance is used when possible to infer docstrings for class members.

The above features are explained in more detail in pdocs's documentation.

`pdocs` is compatible with Python 3.5 and newer.


Example usage
-------------
`pdocs` will accept a Python module file, package directory or an import path.
For example, to view the documentation for the `csv` module in the console:

    pdocs csv

Or, you could view it by pointing at the file directly:

    pdocs /usr/lib/python3.7/csv.py

Submodules are fine too:

    pdocs multiprocessing.pool

You can also filter the documentation with a keyword:

    pdocs csv reader

Generate HTML with the `--html` switch:

    pdocs --html csv

A file called `csv.m.html` will be written to the current directory.

Or start an HTTP server that shows documentation for any installed module:

    pdocs --http

Then open your web browser to `http://localhost:8080`.

There are many other options to explore. You can see them all by running:

    pdocs --help


Submodule loading
-----------------

`pdocs` uses idiomatic Python when loading your modules. Therefore, for `pdocs` to
find any submodules of the input module you specify on the command line, those
modules must be available through Python's ordinary module loading process.

This is not a problem for globally installed modules like `sys`, but can be a
problem for your own sub-modules depending on how you have installed them.

To ensure that `pdocs` can load any submodules imported by the modules you are
generating documentation for, you should add the appropriate directories to your
`PYTHONPATH` environment variable.

For example, if a local module `a.py` imports `b.py` that is installed as
`/home/jsmith/pylib/b.py`, then you should make sure that your `PYTHONPATH`
includes `/home/jsmith/pylib`.

If `pdocs` cannot load any modules imported by the input module, it will exit
with an error message indicating which module could not be loaded.
