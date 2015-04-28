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
```python
song = InputKey(id='song', type='xs:string', paramType='path', required=True)
```
* #### *InputValue(id, type, paramType, like='', required=False, default='', private=False, const=False, batchable=False, maxBatchItems=0)*
```python
song = InputValue(id='song', type='xs:string', paramType='path', required=True, const='12' )
```
* #### *InputMap(id, type, paramType, like='', required=False, default='', private=False, const=False, batchable=False, maxBatchItems=0)*

All of those classes are based on ***BaseInput***.

***like*** is a replacement for ***as*** which is a python keyword. In the *xml* file, ***as*** will be displayed.



### **Methods**
No methods defined

## Paging
This class describe a ***paging*** element. A ***paging*** is deifined by one of the 3 classes below :

* ***PagingPage***
* ***PagingUrl***
* ***PagingOffset***

Check out the full [documentation](https://developer.yahoo.com/yql/guide/yql-opentables-reference.html#yql-opentables-paging)
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

All these classes above subclass ***BasePaging*** .

### **Methods**
No methods defined

## Binder
This class represents an element under **<bindings>**. Which means :

* select
* insert
* update
* delete
* function (stored function)

You can read about the full documentation [here](https://developer.yahoo.com/yql/guide/yql-opentables-reference.html#yql-opentables-select)

### **Definition**

#### *Binder(name, itemPath, produces, pollingFrequencySeconds=0, urls=[], inputs=[], paging=None)*

```python
>>> select = Binder('select', 'products.product', 'xml')
```

### **Methods**

#### *Binder.addInput(input_object)* : 
Add an input object to the binder
#### *Binder.removeInput(input_id, input_type)*
Remove an input object from the binder. ***input_type*** may be ***key, value or map***
#### *Binder.addUrl(url)*
Add an url to the binder
#### *Binder.removeUrl(url)*
Remove an url from the binder
#### *Binder.addPaging(paging_instance)*
Add a paging to the binder
#### *Binder.removePaging(paging_instance)*
Remove a paging from the binder

## MetaClasses

They say *"A picture is worth a thousand of word"* and I say *"A code snippet 
is worth ..."* . You got it (^_^).  
***BinderModel*** and ***TableModel*** are the only classes to use here.

Copy and past the code snippet below in a *example.py*

```python
from binder import BinderModel, InputKey, PagingPage, PagingUrl, InputValue, BinderFunction
from table import TableModel, BinderFrom

class SelectBinder(BinderModel):
    name = 'select'
    itemPath = 'products.product'
    produces = 'xml'
    pollingFrequencySeconds = 30
    urls = ['http://lol.com/services?artist={artis}','http://lol.com/services/song={song}']
    paging = PagingPage({'id': 'ItemPage', 'default': '1'}, {'id':'Count' ,'max':'25'},{'default': '10'})
    artist = InputKey(id='artist', type='xs:string', paramType='path')
    song = InputKey(id='song', type='xs:string', paramType='path', required=True)

class InsertBinder(BinderModel):
    name = 'insert'
    itemPath = 'products.product'
    produces = 'xml'
    pollingFrequencySeconds = 30
    urls = ['http://lol.com/services?artist={artis}','http://lol.com/services/song={song}']
    paging = PagingUrl(nextpage={'path':'yqlsearch.nextpage'})
    artist = InputKey(id='artist', type='xs:string', paramType='path')
    song = InputValue(id='song', type='xs:string', paramType='path', required=True)
    

class TestTable(TableModel):
    name = 'Test'
    author = 'Josue Kouka'
    apiKeyURL = 'http://josuebrunel.org/api'
    documentationURL = 'http://josuebrunel.org/doc.html'
    description = "Just a test table"
    sampleQuery = ['SELECT * FROM mytable','SELECT name FROM mytable WHERE id=4656', "SELECT * FROM mytable WHERE name='Josh'"]
    select = BinderFrom(SelectBinder)
    insert = BinderFrom(InsertBinder)
    func1 = BinderFunction('concat', func_code="console.log('Hello Josh!!!')")

TestTable.table.save(name='Example')
```

Run 

```shell
$ python example.py
$ cat Example.xml
```

```xml
<?xml version="1.0" ?>
<table https="false" securityLevel="any" xmlns="http://query.yahooapis.com/v1/schema/table.xsd">
    <meta>
        <apiKey>http://josuebrunel.org/api</apiKey>
        <author>Josue Kouka</author>
        <description>Just a test table</description>
        <documentationURL>http://josuebrunel.org/doc.html</documentationURL>
        <sampleQuery>SELECT * FROM mytable</sampleQuery>
        <sampleQuery>SELECT name FROM mytable WHERE id=4656</sampleQuery>
        <sampleQuery>SELECT * FROM mytable WHERE name='Josh'</sampleQuery>
    </meta>
    <bindings>
        <function name="concat">
            <execute>
    ![CDATA]console.log('Hello Josh!!!')]]
    </execute>
        </function>
        <insert itemPath="products.product" produces="xml">
            <urls>
                <url>http://lol.com/services?artist={artis}</url>
                <url>http://lol.com/services/song={song}</url>
            </urls>
            <inputs>
                <value id="song" required="true" type="xs:string"/>
                <key id="artist" type="xs:string"/>
            </inputs>
            <paging model="url">
                <nextpage path="yqlsearch.nextpage"/>
            </paging>
        </insert>
        <select itemPath="products.product" produces="xml">
            <urls>
                <url>http://lol.com/services?artist={artis}</url>
                <url>http://lol.com/services/song={song}</url>
            </urls>
            <inputs>
                <key id="song" required="true" type="xs:string"/>
                <key id="artist" type="xs:string"/>
            </inputs>
            <paging model="page">
                <start default="1" id="ItemPage"/>
                <total default="10"/>
                <pageSize id="Count" max="25"/>
            </paging>
        </select>
    </bindings>
</table>

```

Voila, i think we're done here
