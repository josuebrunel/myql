[mYQL](http://myql.readthedocs.org/en/latest/)
=========

[![Build Status](https://travis-ci.org/josuebrunel/myql.svg?branch=master)](https://travis-ci.org/josuebrunel/myql) [![Documentation Status](https://readthedocs.org/projects/myql/badge/?version=latest)](https://myql.readthedocs.org)
[![Latest Version](https://pypip.in/version/myql/badge.svg)](https://pypi.python.org/pypi/myql/)
[![Downloads](https://pypip.in/download/myql/badge.svg)](https://pypi.python.org/pypi/myql) 
[![Py_Versions](https://pypip.in/py_versions/myql/badge.svg)](https://pypi.python.org/pypi/myql)
[![Implementations](https://pypip.in/implementation/myql/badge.svg)](https://pypi.python.org/pypi/myql)
[![Join the chat at https://gitter.im/josuebrunel/myql](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/josuebrunel/myql?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Code Issues](https://www.quantifiedcode.com/project/gh:josuebrunel:myql/badge.svg)](https://www.quantifiedcode.com/app/project/gh:josuebrunel:myql)


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

### Installation

```shell
$ pip install myql
```

#### Examples
--------------

* ___rawQuery___

```python
>>> import myql
>>> from myql.utils import pretty_json, pretty_xml
>>> yql = myql.MYQL(format='json')
>>> response = yql.rawQuery("select name, woeid from geo.states where place='Congo' limit 2")
>>> print(pretty_json(response.content))
{
    "query": {
        "count": 2, 
        "created": "2015-06-03T04:51:23Z", 
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
                }
            ]
        }
    }
}
>>> 

```

* ___get(tabke, item=[], limit=None)___

```python
>>> response = yql.get('geo.countries',['name,woeid'],3)
>>> print(pretty_json(response.content))
{
    "query": {
        "count": 3, 
        "created": "2015-06-03T05:07:47Z", 
        "lang": "en-US", 
        "results": {
            "place": [
                {
                    "name": "Sao Tome and Principe", 
                    "woeid": "23424966"
                }, 
                {
                    "name": "Ghana", 
                    "woeid": "23424824"
                }, 
                {
                    "name": "Togo", 
                    "woeid": "23424965"
                }
            ]
        }
    }
}
>>> 

```

*  ___select(table,item=[],limit=None).were(condition)___

```python
>>> yql.format = 'xml'
>>> response = yql.select('weather.forecast',['units','atmosphere']).where(['woeid','in','select woeid from geo.places(1) where text="Paris,Fr"'])
>>> print(pretty_xml(response.content))
<?xml version="1.0" encoding="utf-8"?>
<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="4" yahoo:created="2015-06-03T05:21:43Z" yahoo:lang="en-US">
    <results>
        <channel>
            <yweather:units distance="mi" pressure="in" speed="mph" temperature="F" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"/>
            <yweather:atmosphere humidity="82" pressure="30.22" rising="0" visibility="9" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"/>
        </channel>
        <channel>
            <yweather:units distance="mi" pressure="in" speed="mph" temperature="F" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"/>
            <yweather:atmosphere humidity="94" pressure="29.85" rising="0" visibility="6.21" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"/>
        </channel>
        <channel>
            <yweather:units distance="mi" pressure="in" speed="mph" temperature="F" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"/>
            <yweather:atmosphere humidity="93" pressure="30.26" rising="0" visibility="" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"/>
        </channel>
        <channel>
            <yweather:units distance="mi" pressure="in" speed="mph" temperature="F" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"/>
            <yweather:atmosphere humidity="100" pressure="30.23" rising="0" visibility="" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"/>
        </channel>
    </results>
</query>
<!-- total: 55 -->
<!-- pprd1-node1008-lh1.manhattan.bf1.yahoo.com -->
```

### Documentation

Full Documentation is [here](http://myql.readthedocs.org/en/latest/)

### Contribute

* Report issue
* Star and Fork the repository
* Submit pull requests
* Above all, have fun playing with data :wink:

#### Release Notes

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



