MYQL
====

| |Build Status| |Documentation Status|
| |Latest Version|
| |Downloads|
| |Status|
| |Status|
| |Join the chat at https://gitter.im/josuebrunel/myql| |Code Issues|

MYQL is a Python wrapper of the Yahoo Query Language.

Yahoo! Query Language Documentation and Support
===============================================

-  Yahoo! Query Language - http://developer.yahoo.com/yql/
-  Yahoo! Developer Network: http://developer.yahoo.com
-  Yahoo! Application Platform - http://developer.yahoo.com/yap/
-  Yahoo! Social APIs - http://developer.yahoo.com/social/
-  Yahoo! QUery Language Console
   https://developer.yahoo.com/yql/console/

Release Notes
=============

v 1.2.2 ( development )
-----------------------

-  Fixed issue with **IN** condition in **where** clause
-  Fixed issue when passing an empty list/tuple (**[]/()**) in a
   **where** clause
-  Import of StockParser from Gurchet Rai
   https://github.com/gurch101/StockScraper OK `#68`_
-  Insert, Update, Delete methods added `#67`_
-  Dummy *try/except* removed from main module
-  Fixed **Invalid OAuth Signature** when using a refreshed token `#64`_
-  Fixed misused of ***MYQL.use(…)*** `#76`_

v 1.2.1
-------

-  Multiple requests while using OAuth fixed

v 1.2.0
-------

-  OpenTable classes
-  Access to resources requiring authentication

v 0.5.6
-------

-  fetch data
-  access to community data
-  select data format (xml/json)
-  change data source
-  filter data
-  fix handling of default and on the fly response format
-  fix limit on ***select(…).where(…)*** when no limit value is passed
-  fix limit on ***get(…)***

installation
============

.. code:: shell

    $ pip install myql

how to use
==========

.. code:: python

    >>> import myql
    >>> yql = myql.MYQL()
    >>> yql.diagnostics = True # To turn diagnostics on

access to community tables
^^^^^^^^^^^^^^^^^^^^^^^^^^

\`\`\`python

            | yql = myql.MYQL()
            | rep = yql.rawQuery(‘desc yahoo.finance.quotes’)
            | rep.json()
            | {u’error’: {u’lang’: u’en-US’, u’description’: u’No
              definition found for Table yahoo.finance.quotes’}}

.. _#68: https://github.com/josuebrunel/myql/issues/68
.. _#67: https://github.com/josuebrunel/myql/issues/67
.. _#64: https://github.com/josuebrunel/myql/issues/64
.. _#76: https://github.com/josuebrunel/myql/issues/76

.. |Build Status| image:: https://travis-ci.org/josuebrunel/myql.svg?branch=master
   :target: https://travis-ci.org/josuebrunel/myql
.. |Documentation Status| image:: https://readthedocs.org/projects/myql/badge/?version=latest
   :target: https://myql.readthedocs.org
.. |Latest Version| image:: https://pypip.in/version/myql/badge.svg
   :target: https://pypi.python.org/pypi/myql/
.. |Downloads| image:: https://pypip.in/download/myql/badge.svg
   :target: https://pypi.python.org/pypi/myql
.. |Status| image:: https://pypip.in/py_versions/myql/badge.svg
   :target: https://pypi.python.org/pypi/myql
.. |Status| image:: https://pypip.in/implementation/myql/badge.svg
   :target: https://pypi.python.org/pypi/myql
.. |Join the chat at https://gitter.im/josuebrunel/myql| image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://gitter.im/josuebrunel/myql?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |Code Issues| image:: https://www.quantifiedcode.com/project/gh:josuebrunel:myql/badge.svg
   :target: https://www.quantifiedcode.com/app/project/gh:josuebrunel:myql
