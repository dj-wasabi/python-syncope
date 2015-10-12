.. python-syncope documentation master file, created by
   sphinx-quickstart on Sat Oct  3 15:55:21 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-syncope's documentation!
==========================================

.. image:: https://readthedocs.org/projects/python-syncope/badge/?version=latest
    :target: http://python-syncope.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status


Overview
========

This is an python wrapper for the Syncope REST API. You'll be able to get, create and update User, roles and a lot more via the API. You'll need basic understanding of JSON to use this module properly.
I tried to add a lot of example on how to use the functions in this module. If you do however find something that might be documented better, please let me know. Also check the 'examples' directory on github for examples.


Installation
============

Installation can be done with:

.. code-block:: bash

    pip install python-syncope


.. include:: test_results.rst


API doc
=======

Overview of the python-syncope api functions that can be used on your script(s).

.. automodule:: syncope

.. autoclass:: Syncope
    :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

