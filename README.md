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

:8ball: use(data_provider_url)
------------------------------

Changes the data provider

```python
>>> yql.use('http://myserver.com/mytables.xml') 
```

:8ball: desc(tablename)
-----------------------
 returns table description
 
```python
>>> response = yql.desc('weather.forecast')
>>> response.json()
{u'query': {u'count': 1, u'lang': u'en-US', u'results': {u'table': {u'request': {u'select': [{u'key': [{u'required': u'true', u'type': u'xs:string', u'name': u'location'}, {u'type': u'xs:string', u'name': u'u'}]}, {u'key': [{u'required': u'true', u'type': u'xs:string', u'name': u'woeid'}, {u'type': u'xs:string', u'name': u'u'}]}]}, u'security': u'ANY', u'meta': {u'documentationURL': u'http://developer.yahoo.com/weather/', u'sampleQuery': u'select * from weather.forecast where woeid=2502265', u'description': u'Weather forecast table', u'author': u'Yahoo! Inc'}, u'hash': u'aae78b1462a6a8fbc748aec4cf292767', u'name': u'weather.forecast'}}, u'created': u'2014-08-16T19:31:51Z'}}
>>>
```

:8ball: rawQuery(query)
-----------------------

Allows you to directly type your query

```python
>>> response = yql.rawQuery("select * from geo.countries where place='North America'")
>>> # deal with the response
```

:8ball: select(table, fields, limit).where(filters, ...)
-------------------------------------------------

Select a table i.e *weather.forecast*.
If *table* not provided, it will use the default table. If there's no such thing as a default table, it will raise a *NoTableSelectedError*

***NB*** : A simple select doesn't return any data. Use ***GET*** instead.

```python
>>> response = yql.select('geo.countries', [name, code, woeid]).where(['name', '=', 'Canada'])
>>> response.json()
{u'query': {u'count': 1, u'lang': u'en-US', u'results': {u'place': {u'woeid': u'23424775', u'name': u'Canada'}}, u'created': u'2014-08-16T19:04:08Z'}}
>>> ...
```

:8ball: get(table, fields, limit)
----------------------------------

Same as ***SELECT***, but instead returns data.

```python
>>> yql.get("geo.countries', ['name', 'woeid'], 1")
>>> rep.json()
{u'query': {u'count': 1, u'lang': u'en-US', u'results': {u'place': {u'woeid': u'23424966', u'name': u'Sao Tome and Principe'}}, u'created': u'2014-08-17T10:32:25Z'}}
>>>
>>> rep = yql.select('geo.countries', ['name', 'woeid'], 2).where(['place', '=', 'Africa'])
>>> rep.json()
{u'query': {u'count': 2, u'lang': u'en-US', u'results': {u'place': [{u'woeid': u'23424740', u'name': u'Algeria'}, {u'woeid': u'23424745', u'name': u'Angola'}]}, u'created': u'2014-08-17T10:52:49Z'}}
>>>
```


:8ball: create()
----------------

:8ball: insert()
----------------

:8ball: update()
----------------

:8ball: delete()
----------------







