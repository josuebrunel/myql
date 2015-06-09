[mYQL](http://myql.readthedocs.org/en/latest/)
=========

[![Build Status](https://travis-ci.org/josuebrunel/myql.svg?branch=master)](https://travis-ci.org/josuebrunel/myql) [![Documentation Status](https://readthedocs.org/projects/myql/badge/?version=latest)](https://myql.readthedocs.org)
[![PyPI](https://img.shields.io/pypi/status/myql.svg?style=flat)](https://pypi.python.org/pypi/myql)
[![PyPI](https://img.shields.io/pypi/v/myql.svg?style=flat)](https://pypi.python.org/pypi/myql)
[![PyPI](https://img.shields.io/pypi/dm/myql.svg?style=flat)](https://pypi.python.org/pypi/myql)
[![PyPI](https://img.shields.io/pypi/pyversions/myql.svg)](https://pypi.python.org/pypi/myql)
[![PyPI](https://img.shields.io/pypi/implementation/myql.svg?style=flat)](https://pypi.python.org/pypi/myql)
[![Coverage Status](https://coveralls.io/repos/josuebrunel/myql/badge.svg?branch=testing)](https://coveralls.io/r/josuebrunel/myql?branch=testing)
[![PyPI](https://img.shields.io/pypi/l/myql.svg?style=flat)](https://pypi.python.org/pypi/myql)


mYQL is a Python wrapper of the Yahoo Query Language. **[Full Documentation](http://myql.readthedocs.org/en/latest/)**

Yahoo! Query Language Documentation and Support
===============================================

* Yahoo! Query Language - http://developer.yahoo.com/yql/
* Yahoo! Developer Network: http://developer.yahoo.com
* Yahoo! Application Platform - http://developer.yahoo.com/yap/
* Yahoo! Social APIs - http://developer.yahoo.com/social/
* Yahoo! QUery Language Console https://developer.yahoo.com/yql/console/

### Features

* Simple YQL Query 
* Authenticated YQL Query ( OAuth )
* StockScraper
* YQL Open Table (Classes and Metaclasses) Generator 
* Response prettyfier

Installation
============

```shell
$ pip install myql
```

Quick Start
===========

It's important to know that **response** is a just **requests.models.Response** object. 
Yes indeed, ***mYQL*** uses ***requests*** :smile:

By default, you have access to the **community tables**. If for whatsoever reason you would like to not have access to those tables

```python
>>> import myql
>>> yql = myql.MYQL(community=False)
```

####Changing response format (xml or json)

The response format is by default ***json***.

```python
>>> import myql
>>> from myql.utils import pretty_json, pretty_xml
>>> yql = myql.MYQL(format='xml', community=True)
>>> resp = yql.rawQuery('select name, woeid from geo.states where place="Congo"')
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

>>> resp = yql.rawQuery('select name, woeid from geo.states where place="Congo"', format='json')
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
```


Methods
-------

####use(yql_table_url,name=yql_table_name)
Maps a table name to the URL of an Open Data Table.

```python
>>> yql.use('http://www.josuebrunel.org//users.xml', name='myusers') 
```

####desc(tablename)
Returns table description
 
```python
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
```

####rawQuery(query)

Allows you to directly type your query

```python
>>> response = yql.rawQuery("select * from geo.countries where place='North America'")
>>> # deal with the response
```


####select(table, fields, limit).where(filters, ...)

***NB*** : A simple select doesn't return any data. Use ***GET*** instead.

```python
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
```

####get(table, fields, limit)
Same as ***SELECT***, but instead returns data.

**REMINDER** : Some tables require a **where clause**, therefore ***GET*** won't work on those tables, use *select(...).where(...)* instead .

```python
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
```

####insert(table, (field1, field2, ..., fieldN),(value1, value2, ..., valueN))
Insert values into a table. Arguments 2 and 3 may be **tuples** or **list**.

```python
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
```

####update(table,[field1, ..., fieldN],[value1, ..., ...valueN]).where(filters, ...)
Update fields values. This method __is always followed by ***where()***__. Arguments 2 and 3 may be **tuples** or **list**.

```python
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
```

####delete(table).where(filters, ...)
Delete records
```python
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

```

####Using OAuth 

***mYQL*** comes with ***[yahoo_oauth](http://yahoo-oauth.readthedocs.org/en/master/)***, which is an OAuth library for Yahoo! APIs.

```python
>>> from yahoo_oauth import OAuth1
>>> oauth = OAuth1(None, None, from_file='credentials.json') # only consumer_key and consumer_secret are required.
>>> from myql import MYQL
>>> yql = MYQL(format='xml', oauth=oauth)
>>> response = yql.getGUID('josue_brunel') # Deal with the response
```


#### Release Notes

##### 1.2.3
-------

* Fixed issue related to date in StockRetriver.get_historical_info [#107](https://github.com/josuebrunel/myql/issues/107)
* Fixed issue with **IN** condition in **where** clause [#106](https://github.com/josuebrunel/myql/issues/107)
* Fix definition of raw_input for python3 [#105](https://github.com/josuebrunel/myql/issues/105)
* Yahoo-OAuth included as main oauth library [#112](https://github.com/josuebrunel/myql/issues/112)

##### 1.2.2
-------
* **Python3** support OK [#71](https://github.com/josuebrunel/myql/issues/71)
* **PyPy/PyPy3** support OK
* Fixed issue with **IN** condition in **where** clause
* Fixed issue when passing an empty list/tuple (**[]/()**) in a **where** clause besides first argument
* Import of ***[StockParser](https://github.com/gurch101/StockScraper)*** from Gurchet Rai  OK [#68](https://github.com/josuebrunel/myql/issues/68)
* Insert, Update, Delete methods added [#67](https://github.com/josuebrunel/myql/issues/67) 
* Dummy *try/except* removed from main module
* Fixed **Invalid OAuth Signature** when using a refreshed token [#64](https://github.com/josuebrunel/myql/issues/64)
* Fixed misused of ***MYQL.use(...)*** [#76](https://github.com/josuebrunel/myql/issues/76)
* Fixed format issue [#82](https://github.com/josuebrunel/myql/issues/82)
* Added useful functions in utils [#81](https://github.com/josuebrunel/myql/issues/81)
* Default access to community tables
* Response prettyfier : *pretty_json, pretty_xml*

##### v 1.2.1
------
* Multiple requests while using OAuth fixed 

##### 1.2.0
-------
* OpenTable classes
* Access to resources requiring authentication

##### 0.5.6
-------------
* fetch data
* access to community data
* select data format (xml/json)
* change data source
* filter data 
* fix handling of default response format on the fly 
* fix limit on ***select(...).where(...)*** when no limit value is passed
* fix limit on ***get(...)***



