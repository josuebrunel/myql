YQL Open Table
==============

## Table
This class represents the **root** element of a YQL Table Definition File. You can read about the full documentation [here](https://developer.yahoo.com/yql/guide/yql-opentables-reference.html#yql-opentables-tables-element)

### **Definition**

#### *Table(name, author, apiKeyURL, documentationURL, sampleQuery=[], description=None, table_attr=None, bindings=[])*

```python
>>> from myql.contrib.table import Table
>>> mytable = Table('mytable', 'Josue Kouka', 'http://josuerunel.org/mytable/','http://josuerunel.org/mytable/docs.html',sampleQuery = ['SELECT * FROM mytable', 'SELECT name FROM mytable WHERE id = 77'], description='Just a simple tabe', table_attr={'xmlns':'http://query.yahooapis.com/v1/schema/table.xsd', 'securityLevel':'any', 'https':'false'})
```

### **Methods**

#### *Table.addBinder(binder_object)*
Add a binder to the table 
```python
>>> mytable.addBinder(select_binder)
```
#### *Table.removeBinder(binder_object)*
Remove a binder from the table
```python
>>> mytable.removeBinder(select_binder)
```
#### *Table.save(name=None, path=None)*
Save the table as a *xml file* with Table Object name if *name* is not provided. If *path*, saves the *xml file* to the specified location
```python
>>> mytable.save(name='test',path='/var/www/josuebrunel.org/mytable/')
```

## Inputs
There are 3 kind of *inputs* as described in the [documentation](https://developer.yahoo.com/yql/guide/yql-opentables-reference.html#yql-opentables-key) :

* ***key***  
* ***map*** 
* ***value***  

### **Definitions**

* #### *InputKey(id, type, paramType, like='', required=False, default='', private=False, const=False, batchable=False, maxBatchItems=0)*

* #### *InputValue(id, type, paramType, like='', required=False, default='', private=False, const=False, batchable=False, maxBatchItems=0)*

* #### *InputMap(id, type, paramType, like='', required=False, default='', private=False, const=False, batchable=False, maxBatchItems=0)*

All of those objects are based on ***BaseInput***.

### **Methods**
No methods defined

## Paging
This class describe a ***paging*** element. A ***paging*** is deifined by the 3 classes below :

* ***PagingPage***
* ***PagingUrl***
* ***PagingOffset***

### **Definitions**

* #### *PagingPage(start={}, pageSize={}, total={})*
```python
>>> mypage = PagingPage({'id': 'ItemPage', 'default': '1'}, {'id':'Count' ,'max':'25'},{'default': '10'})
```
* #### *PagingUrl(nextpage)*
```python
>>> mypage = PagingUrl("ysearchresponse.nextpage")
```
* #### *PagingOffset(matrix, start={}, pageSize={}, total={})*
```python
>>> mypage = PagingOffset({'id': 'ItemPage', 'default': '1'}, {'id':'Count' ,'max':'25'},{'default': '10'})
```

### **Methods**
No methods defined

## Binder
This class represents an element under **<bindings>**. Which means :

* select
* insert
* update
* delete

You can read about the full documentation [here](https://developer.yahoo.com/yql/guide/yql-opentables-reference.html#yql-opentables-select)

### **Definition**

#### *Binder(name, itemPath, produces, pollingFrequencySeconds=0, urls=[], inputs=[], paging=None)*

```python
>>> select = Binder('select', 'products.product', 'xml')
```

### **Methods**

#### *Binder.addInput(input_object)* : 
Add a input object to the binder
#### *Binder.removeInput(input_id, input_type)*
Remove an input object from the binder. ***input_type*** may be ***key, value or map***
#### *Binder.addUrl(url)*
#### *Binder.removeUrl(url)*
#### *Binder.addPaging(paging_instance)*
#### *Binder.removePaging(paging_instance)*

## MetaClasses
 
### **Definition**

### **Methods**


