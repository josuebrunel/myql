YQL Open Table
==============

## Table

This class represents the **root** element of a YQL Table Definition File. You can read about the full documentation [here](https://developer.yahoo.com/yql/guide/yql-opentables-reference.html#yql-opentables-tables-element)

```python
def __init__(self, name, author, apiKeyURL, documentationURL, sampleQuery=[], description=None, table_attr=None, bindings=[])
```

```python
>>> from myql.contrib.table import Table
>>> mytable = Table('mytable', 'Josue Kouka', 'http://josuerunel.org/mytable/','http://josuerunel.org/mytable/docs.html',sampleQuery = ['SELECT * FROM mytable', 'SELECT name FROM mytable WHERE id = 77'], description='Just a simple tabe', table_attr={'xmlns':'http://query.yahooapis.com/v1/schema/table.xsd', 'securityLevel':'any', 'https':'false'})
```

####Table.addBinder(binder_object)
Add a binder to the table 
```python
>>> mytable.addBinder(select_binder)
```
####Table.removeBinder(binder_object)
Remove a binder from the table
```python
>>> mytable.removeBinder(select_binder)
```
####Table.save(name=None, path=None)
Save the table as a *xml file* with Table Object name if *name* is not provided. If *path*, saves the *xml file* to the specified location
```python
>>> mytable.save(name='test',path='/var/www/josuebrunel.org/mytable/')
```

## Binder

## Inputs

## Paging
 



