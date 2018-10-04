SERAPIDE - Core
===============

.. image:: http://2013.foss4g.org/wp-content/uploads/2013/01/logo_GeoSolutions_quadrato.png
   :target: https://www.geo-solutions.it/
   :alt: GeoSolutions
   :width: 50

*Django GraphQL APIs / SERAPIDE - Core*

.. image:: https://badge.fury.io/py/serapide-core.svg?service=github
   :target: http://badge.fury.io/py/serapide-core

.. image:: https://travis-ci.org/geosolutions-it/serapide-core.svg?service=github
   :alt: Build Status
   :target: https://travis-ci.org/geosolutions-it/serapide-core

.. image:: https://coveralls.io/repos/github/geosolutions-it/serapide-core/badge.svg?branch=master&service=github
   :alt: Coverage Status
   :target: https://coveralls.io/github/geosolutions-it/serapide-core?branch=master

If you are facing one or more of the following:
 * TODO,
 * TODO,

TODO

Contributing
------------

We love contributions, so please feel free to fix bugs, improve things, provide documentation. Just `follow the
guidelines <https://serapide-core.readthedocs.io/en/latest/contributing.html>`_ and submit a PR.

Requirements
------------

* Python 3.4, 3.5, 3.6
* Django 2.0

Installation
------------

Install with pip::

    pip install serapide-core

Add `serapide_core` to your `INSTALLED_APPS`

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'serapide_core',
    )


If you need an OAuth2 provider you'll want to add the following to your urls.py.
Notice that `serapide_core` namespace is mandatory.

.. code-block:: python

    urlpatterns = [
        ...
        url(r'^o/', include('serapide_core.urls', namespace='serapide_core')),
    ]


Changelog
---------

See `CHANGELOG.md <https://github.com/geosolutions-it/serapide-core/blob/master/CHANGELOG.md>`_.


Documentation
--------------

The `full documentation <https://serapide-core.readthedocs.io/>`_ is on *Read the Docs*.

License
-------

serapide-core is released under the terms of the **Simplified BSD license**. Full details in ``LICENSE`` file.
