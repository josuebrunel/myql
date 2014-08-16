lokingYQL
=========

LokingYQL is a Yahoo Query Language Wrapper written in Python

version
=======

***0.5***

installation
============

Surely through ***pipe*** or something like

```shell
$ python setup.py install 
```

how to use
==========

```python
>>> import lokingyql
>>> yql = lokingyql.LokingYQL()
>>> yql.diagnostics = True # To turn diagnostics on
```
Methods
-------

- use(data_provider_url)
------------------------

Changes the data provider

```python
>>> yql.use('http://myserver.com/mytables.xml') 
```

- desc(tablename)
-----------------
 returns table description
```python
>>> response = yql.desc('weather.forecast')
>>> response.json()
{u'query': {u'count': 1, u'lang': u'en-US', u'results': {u'table': {u'request': {u'select': [{u'key': [{u'required': u'true', u'type': u'xs:string', u'name': u'location'}, {u'type': u'xs:string', u'name': u'u'}]}, {u'key': [{u'required': u'true', u'type': u'xs:string', u'name': u'woeid'}, {u'type': u'xs:string', u'name': u'u'}]}]}, u'security': u'ANY', u'meta': {u'documentationURL': u'http://developer.yahoo.com/weather/', u'sampleQuery': u'select * from weather.forecast where woeid=2502265', u'description': u'Weather forecast table', u'author': u'Yahoo! Inc'}, u'hash': u'aae78b1462a6a8fbc748aec4cf292767', u'name': u'weather.forecast'}}, u'created': u'2014-08-16T19:31:51Z'}}
>>>
```

- rawQuery(query)
-----------------

Allows you to directly type your query

```python
>>> response = yql.rawQuery("select * from geo.countries where place='North America'")
>>> # deal with the response
```

- select(table, fields).where(filters, ...)
-------------------------------------------

Select a table i.e *weather.forecast*.
If *table* not provided, it will use the default table. If there's no such thing as a default table, it will raise a *NoTableSelectedError*

```python
>>> response = yql.select('geo.countries', [name, code, woeid]).where(['name', '=', 'Canada'])
>>> response.json()
{u'query': {u'count': 1, u'lang': u'en-US', u'results': {u'place': {u'woeid': u'23424775', u'name': u'Canada'}}, u'created': u'2014-08-16T19:04:08Z'}}
>>> ...
```

- create()
----------

- insert()
----------

- update()
----------

* delete()
----------







