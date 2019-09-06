[![pdocs - Documentation Powered by Your Python Code.](https://raw.github.com/timothycrosley/pdocs/master/art/logo_large.png)](https://timothycrosley.github.io/pdocs/)
_________________

[![PyPI version](https://badge.fury.io/py/pdocs.svg)](http://badge.fury.io/py/pdocs)
[![Build Status](https://travis-ci.org/timothycrosley/pdocs.svg?branch=master)](https://travis-ci.org/timothycrosley/pdocs)
[![codecov](https://codecov.io/gh/timothycrosley/pdocs/branch/master/graph/badge.svg)](https://codecov.io/gh/timothycrosley/pdocs)
[![Join the chat at https://gitter.im/pdocs/community](https://badges.gitter.im/pdocs/community.svg)](https://gitter.im/pdocs/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/pdocs/)
[![Downloads](https://pepy.tech/badge/pdocs)](https://pepy.tech/project/pdocs)
_________________

[Read Latest Documentation](https://timothycrosley.github.io/pdocs/) - [Browse GitHub Code Repository](https://github.com/timothycrosley/pdocs/)
_________________


`pdocs` is a library and a command line program to discover the public
interface of a Python module or package. The `pdocs` script can be used to
generate Markdown or HTML of a module's public interface, or it can be used
to run an HTTP server that serves generated HTML for installed modules.

`pdocs` is an MIT Licensed fork of [pdoc](https://github.com/mitmproxy/pdoc)'s original implementation by Andrew Gallant (@BurntSushi).
 with the goal of staying true to the original vision layed out by the project's creator.

NOTE: For most projects, the best way to use `pdocs` is using [portray](https://timothycrosley.github.io/portray/).

[![asciicast](https://asciinema.org/a/265744.svg)](https://asciinema.org/a/265744)

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

`pdocs` is compatible with Python 3.6 and newer.

## Quick Start

The following guides should get you up using pdocs in no time:

1. [Installation](https://timothycrosley.github.io/pdocs/docs/quick_start/1.-installation/) - TL;DR: Run `pip3 install pdocs` within your projects virtual environment.
2. [Command Line Usage](https://timothycrosley.github.io/pdocs/docs/quick_start/2.-cli/) - TL;DR: Run `pdocs server YOUR_MODULES` to test and `pdocs as_html YOUR_MODULES` to generate HTML.
3. [API Usage](https://timothycrosley.github.io/pdocs/docs/quick_start/3.-api/) - TL;DR: Everything available via the CLI is also easily available programmatically from within Python.

## Differences Between pdocs and pdoc

Below is a running list of intentional differences between [pdoc](https://github.com/mitmproxy/pdoc) and [pdocs](https://github.com/timothycrosley/pdocs):

- pdocs has built-in support for Markdown documentation generation (as needed by [portray](https://timothycrosley.github.io/portray/)).
- pdocs has built-in support for the inclusion of Type Annotation information in reference documentation.
- pdocs requires Python 3.6+; pdoc maintains Python2 compatibility as of the latest public release.
- pdocs uses the most recent development tools to ensure long-term maintainability (mypy, black, isort, flake8, bandit, ...)
- pdocs generates project documentation to a temporary folder when serving locally, instead of including a live server. An intentional trade-off between simplicity and performance.
- pdocs provides a simplified Python API in addition to CLI API.
- pdocs is actively maintained.
- pdocs uses [hug CLI and sub-commands](https://github.com/timothycrosley/pdocs/blob/master/pdocs/cli.py#L1), pdoc uses [argparse and a single command](https://github.com/mitmproxy/pdoc/blob/master/pdoc/cli.py#L1).
- pdoc provides textual documentation from the command-line, pdocs removed this feature for API simplicity.

## Notes on Licensing and Fork

The original pdoc followed the [Unlicense license](https://unlicense.org/), and as such so does the initial commit to this fork [here](https://github.com/timothycrosley/pdocs/commit/7cf925101e4ffc5690f2952ac9ad0b7b0410b4f8).
Unlicense is fully compatible with MIT, and the reason for the switch going forward is because MIT is a more standard and well-known license.

As seen by that commit, I chose to fork with fresh history, as the project is very old (2013) and I felt many of the commits that happened in the past might, instead of helping to debug issues, lead to red herrings due to the many changes that have happened
in the Python eco-system since that time. If you desire to see the complete history for any reason, it remains available on the original [pdoc repository](https://github.com/mitmproxy/pdoc).

## Why Create `pdocs`?

I created `pdocs` to help power [portray](https://timothycrosley.github.io/portray/) while staying true to the original vision of `pdoc` and maintain
MIT license compatibility. In the end I created it to help power better documentation websites for Python projects.

I hope you, too, find `pdocs` useful!

~Timothy Crosley
