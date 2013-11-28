bitcoin-python3 is a set of Python libraries that allows easy access to the
bitcoin peer-to-peer cryptocurrency client API. For Python 3 only.
To get Python 2 version - go to https://github.com/laanwj/bitcoin-python

Documentation
===========================

Documentation can be found here, or in the source archive. It is built
using Sphinx:

http://laanwj.github.com/bitcoin-python/doc/

Installation instructions
===========================

bitcoin-python3 uses setuptools for the install script. There are no dependencies apart from Python itself.

::

  $ python setup.py build
  $ python setup.py install

Pypi / Cheeseshop
==================

It is possible to install the package through Pypi (cheeseshop), see http://pypi.python.org/pypi?:action=display&name=bitcoin-python3

::

  $ pip install bitcoin-python3

TODO
======
These things still have to be added:

- SSL support (including certificate verification) for managing remote bitcoin daemons.

