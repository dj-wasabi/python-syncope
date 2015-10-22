.. python-syncope documentation master file, created by
   sphinx-quickstart on Sat Oct  3 15:55:21 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-syncope's documentation!
==========================================

.. image:: https://readthedocs.org/projects/python-syncope/badge/?version=latest
    :target: http://python-syncope.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status


Table of Content
================

.. toctree::
   :maxdepth: 2

   test_results.rst
   api_doc.rst


Overview
========

This is an python wrapper for the Syncope REST API. You'll be able to get, create and update User, roles and a lot more via the API. You'll need basic understanding of JSON to use this module properly.
I tried to add a lot of example on how to use the functions in this module. If you do however find something that might be documented better, please let me know. Also check the 'examples' directory on github for examples.


Syncope usage
-------------

An overview of the components on which Syncope version is working.

+-----------+---------------+---------------+
| component |  Syncope 1.1  |  Syncope 1.2  |
+===========+===============+===============+
| Users     |      v        |       x       |
+-----------+---------------+---------------+
| Roles     |      v        |       x       |
+-----------+---------------+---------------+
| Logger    |      v        |       x       |
+-----------+---------------+---------------+

This module is sill Work In Progress, so if you miss an specific action it will come.


Installation
============

Installation can be done with:

.. code-block:: bash

    pip install python-syncope



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

