`mYQL <http://myql.readthedocs.org/en/latest/>`__
=================================================

|Build Status| |Documentation Status| |Code Health| |PyPI| |PyPI| |PyPI|
|PyPI| |PyPI| |Coverage Status| |PyPI|

mYQL is a Python wrapper of the Yahoo Query Language.

Yahoo! Query Language Documentation and Support
===============================================

-  Yahoo! Query Language - http://developer.yahoo.com/yql/
-  Yahoo! Developer Network: http://developer.yahoo.com
-  Yahoo! Application Platform - http://developer.yahoo.com/yap/
-  Yahoo! Social APIs - http://developer.yahoo.com/social/
-  Yahoo! QUery Language Console
   https://developer.yahoo.com/yql/console/

Features
~~~~~~~~

-  Simple YQL Query
-  Authenticated YQL Query ( OAuth )
-  StockScraper
-  YQL Open Table (Classes and Metaclasses) Generator
-  Response prettyfier

Installation
============

.. code:: shell

    $ pip install myql

Quick Start
===========

It's important to know that **response** is a just
**requests.models.Response** object. Yes indeed, ***mYQL*** uses
***requests*** :smile:

By default, you have access to the **community tables**. If for
whatsoever reason you would like to not have access to those tables

.. code:: python

    >>> import myql
    >>> yql = myql.MYQL(community=False)

Changing response format (xml or json)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The response format is by default ***json***.

.. code:: python

    >>> import myql
    >>> from myql.utils import pretty_json, pretty_xml
    >>> yql = myql.MYQL(format='xml', community=True)
    >>> resp = yql.raw_query('select name, woeid from geo.states where place="Congo"')
    >>> print(pretty_xml(resp.content))
    <?xml version="1.0" encoding="utf-8"?>
    <query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="11" yahoo:created="2015-06-07T11:56:11Z" yahoo:lang="en-US">
        <results>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Cuvette-Ouest Department</name>
                <woeid>55998384</woeid>
            </place>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Cuvette Department</name>
                <woeid>2344968</woeid>
            </place>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Plateaux District</name>
                <woeid>2344973</woeid>
            </place>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Sangha</name>
                <woeid>2344974</woeid>
            </place>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Lekoumou</name>
                <woeid>2344970</woeid>
            </place>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Pool Department</name>
                <woeid>2344975</woeid>
            </place>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Likouala Department</name>
                <woeid>2344971</woeid>
            </place>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Niari Department</name>
                <woeid>2344972</woeid>
            </place>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Brazzaville</name>
                <woeid>2344976</woeid>
            </place>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Bouenza Department</name>
                <woeid>2344967</woeid>
            </place>
            <place xmlns="http://where.yahooapis.com/v1/schema.rng">
                <name>Kouilou</name>
                <woeid>2344969</woeid>
            </place>
        </results>
    </query>
    <!-- total: 33 -->
    <!-- pprd1-node1003-lh3.manhattan.bf1.yahoo.com -->

    >>> resp = yql.raw_query('select name, woeid from geo.states where place="Congo"', format='json')
    >>> print(pretty_json(resp.content))
    {
        "query": {
            "count": 11, 
            "created": "2015-06-07T11:58:20Z", 
            "lang": "en-US", 
            "results": {
                "place": [
                    {
                        "name": "Cuvette-Ouest Department", 
                        "woeid": "55998384"
                    }, 
                    {
                        "name": "Cuvette Department", 
                        "woeid": "2344968"
                    }, 
                    {
                        "name": "Plateaux District", 
                        "woeid": "2344973"
                    }, 
                    {
                        "name": "Sangha", 
                        "woeid": "2344974"
                    }, 
                    {
                        "name": "Lekoumou", 
                        "woeid": "2344970"
                    }, 
                    {
                        "name": "Pool Department", 
                        "woeid": "2344975"
                    }, 
                    {
                        "name": "Likouala Department", 
                        "woeid": "2344971"
                    }, 
                    {
                        "name": "Niari Department", 
                        "woeid": "2344972"
                    }, 
                    {
                        "name": "Brazzaville", 
                        "woeid": "2344976"
                    }, 
                    {
                        "name": "Bouenza Department", 
                        "woeid": "2344967"
                    }, 
                    {
                        "name": "Kouilou", 
                        "woeid": "2344969"
                    }
                ]
            }
        }
    }

    >>>

Methods
-------

use(yql\_table\_url,name=yql\_table\_name)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Maps a table name to the URL of an Open Data Table.

.. code:: python

    >>> yql.use('http://www.josuebrunel.org//users.xml', name='myusers') 

desc(tablename)
^^^^^^^^^^^^^^^

Returns table description

.. code:: python

    >>> response = yql.desc('weather.forecast')
    >>> print(pretty_json(response.content))
    {
        "query": {
            "count": 1, 
            "created": "2015-06-07T12:00:27Z", 
            "lang": "en-US", 
            "results": {
                "table": {
                    "hash": "aae78b1462a6a8fbc748aec4cf292767", 
                    "meta": {
                        "author": "Yahoo! Inc", 
                        "description": "Weather forecast table", 
                        "documentationURL": "http://developer.yahoo.com/weather/", 
                        "sampleQuery": "select * from weather.forecast where woeid=2502265"
                    }, 
                    "name": "weather.forecast", 
                    "request": {
                        "select": [
                            {
                                "key": [
                                    {
                                        "name": "location", 
                                        "required": "true", 
                                        "type": "xs:string"
                                    }, 
                                    {
                                        "name": "u", 
                                        "type": "xs:string"
                                    }
                                ]
                            }, 
                            {
                                "key": [
                                    {
                                        "name": "woeid", 
                                        "required": "true", 
                                        "type": "xs:string"
                                    }, 
                                    {
                                        "name": "u", 
                                        "type": "xs:string"
                                    }
                                ]
                            }
                        ]
                    }, 
                    "security": "ANY"
                }
            }
        }
    }

    >>>

raw\_query(query)
^^^^^^^^^^^^^^^^^

Allows you to directly type your query

.. code:: python

    >>> response = yql.raw_query("select * from geo.countries where place='North America'")
    >>> # deal with the response

select(table, fields, limit).where(filters, ...)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

***NB*** : A simple select doesn't return any data. Use ***GET***
instead.

.. code:: python

    >>> response = yql.select('geo.countries', ['name', 'code', 'woeid']).where(['name', '=', 'Canada'])
    >>> print(pretty_json(response.content))
    {
        "query": {
            "count": 1, 
            "created": "2015-06-07T12:10:39Z", 
            "lang": "en-US", 
            "results": {
                "place": {
                    "name": "Canada", 
                    "woeid": "23424775"
                }
            }
        }
    }

    >>> ...
    >>> response = yql.select('geo.countries', ['name', 'woeid'], 2).where(['place', 'in', ('Africa', 'Europe')])
    >>> from myql.utils import dump
    >>> dump(response)
    {
        "query": {
            "count": 2, 
            "created": "2015-06-07T12:27:04Z", 
            "lang": "en-US", 
            "results": {
                "place": [
                    {
                        "name": "Algeria", 
                        "woeid": "23424740"
                    }, 
                    {
                        "name": "Angola", 
                        "woeid": "23424745"
                    }
                ]
            }
        }
    }

    >>>

get(table, fields, limit)
^^^^^^^^^^^^^^^^^^^^^^^^^

Same as ***SELECT***, but instead returns data.

**REMINDER** : Some tables require a **where clause**, therefore
***GET*** won't work on those tables, use *select(...).where(...)*
instead .

.. code:: python

    >>> from myql.utils import dump
    >>> response = yql.get('geo.countries', ['name', 'woeid'], 1)
    >>> dump(response)
    {
        "query": {
            "count": 1, 
            "created": "2015-06-07T12:29:01Z", 
            "lang": "en-US", 
            "results": {
                "place": {
                    "name": "Sao Tome and Principe", 
                    "woeid": "23424966"
                }
            }
        }
    }

    >>>

insert(table, (field1, field2, ..., fieldN),(value1, value2, ..., valueN))
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Insert values into a table. Arguments 2 and 3 may be **tuples** or
**list**.

.. code:: python

    >>> from myql.utils import pretty_json
    >>> response = yql.insert('yql.storage.admin',('value',),('http://josuebrunel.org',))
    >>> print(pretty_json(response.content))
    {
        "query": {
            "count": 1,
            "created": "2015-05-14T13:25:56Z",
            "lang": "en-US",
            "results": {
                "inserted": {
                    "execute": "store://KkkC5xDw4v32IcWWSQ4YRe",
                    "select": "store://Zc5LHXcmYM7XBfSbo9tzFL",
                    "update": "store://Rqb5fbQyDvrfHJiClWnZ6q"
                }
            }
        }
    }

update(table,[field1, ..., fieldN],[value1, ..., ...valueN]).where(filters, ...)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update fields values. This method **is always followed by
***where()*****. Arguments 2 and 3 may be **tuples** or **list**.

.. code:: python

    >>> from myql.utils import pretty_json
    >>> response = yql.update('yql.storage',('value',),('https://josuebrunel.org',)).where(['name','=','store://Rqb5fbQyDvrfHJiClWnZ6q'])
    >>> print(pretty_json(response.content))
    {
        "query": {
            "count": 1,
            "created": "2015-05-14T13:32:52Z",
            "lang": "en-US",
            "results": {
                "success": "Updated store://KkkC5xDw4v32IcWWSQ4YRe"
            }
        }
    }

delete(table).where(filters, ...)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete records

.. code:: python

    >>> from myql.utils import pretty_json
    >>> response = self.yql.delete('yql.storage').where(['name','=','store://Rqb5fbQyDvrfHJiClWnZ6q'])
    >>> print(pretty_json(response.content))
    {
        "query": {
            "count": 1,
            "created": "2015-05-14T13:38:28Z",
            "lang": "en-US",
            "results": {
                "success": "store://Rqb5fbQyDvrfHJiClWnZ6q deleted"
            }
        }
    }

Using OAuth
^^^^^^^^^^^

***mYQL*** comes with
***`yahoo\_oauth <http://yahoo-oauth.readthedocs.org/en/master/>`__***,
which is an OAuth library for Yahoo! APIs.

.. code:: python

    >>> from yahoo_oauth import OAuth1
    >>> oauth = OAuth1(None, None, from_file='credentials.json') # only consumer_key and consumer_secret are required.
    >>> from myql import MYQL
    >>> yql = MYQL(format='xml', oauth=oauth)
    >>> response = yql.get_guid('josue_brunel') # Deal with the response

Stocks Scraper
^^^^^^^^^^^^^^

The full documentation on ***StockScraper*** is
`here <https://myql.readthedocs.org/en/latest/stockscraper/>`__

Release Notes
^^^^^^^^^^^^^

##### 1.2.6
-----------

-  Fixed `#148 <https://github.com/josuebrunel/myql/issues/148>`__

##### 1.2.5
-----------

-  camelCase dropped for underscore
-  Support for substitution variable i.e @myvar
-  Support of Remote Filters
-  Support of Post Query Filters

##### 1.2.4
-----------

-  Weather module added
-  StockScraper now under Finance namespace

##### 1.2.3
-----------

-  Fixed issue related to date in StockRetriver.get\_historical\_info
   `#107 <https://github.com/josuebrunel/myql/issues/107>`__
-  Fixed issue with **IN** condition in **where** clause
   `#106 <https://github.com/josuebrunel/myql/issues/107>`__
-  Fix definition of raw\_input for python3
   `#105 <https://github.com/josuebrunel/myql/issues/105>`__
-  Yahoo-OAuth included as main oauth library
   `#112 <https://github.com/josuebrunel/myql/issues/112>`__

##### 1.2.2
-----------

-  **Python3** support OK
   `#71 <https://github.com/josuebrunel/myql/issues/71>`__
-  **PyPy/PyPy3** support OK
-  Fixed issue with **IN** condition in **where** clause
-  Fixed issue when passing an empty list/tuple (**[]/()**) in a
   **where** clause besides first argument
-  Import of
   ***`StockParser <https://github.com/gurch101/StockScraper>`__*** from
   Gurchet Rai OK
   `#68 <https://github.com/josuebrunel/myql/issues/68>`__
-  Insert, Update, Delete methods added
   `#67 <https://github.com/josuebrunel/myql/issues/67>`__
-  Dummy *try/except* removed from main module
-  Fixed **Invalid OAuth Signature** when using a refreshed token
   `#64 <https://github.com/josuebrunel/myql/issues/64>`__
-  Fixed misused of ***MYQL.use(...)***
   `#76 <https://github.com/josuebrunel/myql/issues/76>`__
-  Fixed format issue
   `#82 <https://github.com/josuebrunel/myql/issues/82>`__
-  Added useful functions in utils
   `#81 <https://github.com/josuebrunel/myql/issues/81>`__
-  Default access to community tables
-  Response prettyfier : *pretty\_json, pretty\_xml*

##### v 1.2.1
-------------

-  Multiple requests while using OAuth fixed

##### 1.2.0
-----------

-  OpenTable classes
-  Access to resources requiring authentication

##### 0.5.6
-----------

-  fetch data
-  access to community data
-  select data format (xml/json)
-  change data source
-  filter data
-  fix handling of default response format on the fly
-  fix limit on ***select(...).where(...)*** when no limit value is
   passed
-  fix limit on ***get(...)***

.. |Build Status| image:: https://travis-ci.org/josuebrunel/myql.svg?branch=master
   :target: https://travis-ci.org/josuebrunel/myql
.. |Documentation Status| image:: https://readthedocs.org/projects/myql/badge/?version=latest
   :target: https://myql.readthedocs.org
.. |Code Health| image:: https://landscape.io/github/josuebrunel/myql/master/landscape.svg?style=flat
   :target: https://landscape.io/github/josuebrunel/myql/master
.. |PyPI| image:: https://img.shields.io/pypi/status/myql.svg?style=flat
   :target: https://pypi.python.org/pypi/myql
.. |PyPI| image:: https://img.shields.io/pypi/v/myql.svg?style=flat
   :target: https://pypi.python.org/pypi/myql
.. |PyPI| image:: https://img.shields.io/pypi/dm/myql.svg?style=flat
   :target: https://pypi.python.org/pypi/myql
.. |PyPI| image:: https://img.shields.io/pypi/pyversions/myql.svg
   :target: https://pypi.python.org/pypi/myql
.. |PyPI| image:: https://img.shields.io/pypi/implementation/myql.svg?style=flat
   :target: https://pypi.python.org/pypi/myql
.. |Coverage Status| image:: https://coveralls.io/repos/josuebrunel/myql/badge.svg?branch=testing
   :target: https://coveralls.io/r/josuebrunel/myql?branch=master
.. |PyPI| image:: https://img.shields.io/pypi/l/myql.svg?style=flat
   :target: https://pypi.python.org/pypi/myql
