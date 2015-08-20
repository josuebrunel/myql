MYQL
====

### **Definition**

#### *MYQL(community=True, format='json', jsonCompact=False, crossProduct=None, debug=False, oauth=None)*

### **Methods**

#### *MYQL.payload_builder(query, format='json')*

Return a dictionary of parameters

* ***query*** : the YQL Query
* ***format*** : xml or json

#### *MQYL.execute_query(payload)*

Execute the query and returns and response

* ***payload*** : Dict of parameters


#### *MYQL.raw_query(query, format=None, pretty=False)*

Call *payloadBuilder* to build paramaters and *executeQuery* to execute que *query* then return a response.

* ***query*** : the YQL Query
* ***format*** : xml or json

#### *MQYL.use(yql_table_url, name=yql_table_name)*

 Change the service provider

* ***url*** : url of the service provider

```python
>>> from myql import YQL
>>> yql = YQL(format='json')
>>> yql.use('http://www.josuebrunel.org/users.xml',name='users')
>>> response = self.yql.raw_query('select * from users', format='xml')
```

#### *MYQL.set({key:value, ..., keyN:valueN})*

Set variable to use in your YQL statement

```python
>>> from myql import YQL
>>> yql = YQL()
>>> yql.set({'home':'Congo'})
>>> states = yql.select('geo.states', remote_filter=(5,)).where(['place', '=', '@home'])
```

#### *MQYL.desc(table)*

Get the description of a table.

* ***table*** : Table name

#### *MQYL.get(table, items=[], limit=None, **kwargs)*

Get **items** from **table**.

* ***table*** : Table name
* ***items*** : Element/columns to get from the table
* ***limit*** : limit of element to fetch


#### *MQYL.select(table, items=[], limit=None, **kwargs)*
This method is always followed by a **where**. It doesn't return a response if called alone.

* ***table*** : Table name
* ***items*** : Element/columns to get from the table
* ***limit*** : limit of element to fetch

```python
>>> yql.select('social.profile', ['guid', 'givenName', 'gender'])
```

#### *MYQL.insert(table,[field1, field2, ..., fieldN],[value1, value2, ..., valueN])*
* ***table***: Table name
* ***fields***: List or Tuple of fields
* ***values***: List or Tuple of values

```python
>>> response = yql.insert('yql.storage.admin',('value',),('http://josuebrunel.org',))
```

#### *MYQL.update(table,[field1, field2, ..., fieldN],[value1, value2, ..., valueN])*
This method is always followed by a **where**. It doesn't return a response if called alone.

* ***table***: Table name
* ***fields***: List or Tuple of fields to update
* ***values***: List or Tuple of new values

```python
>>> response = yql.update('yql.storage',('value',),('https://josuebrunel.org',)).where(['name','=',"store://Rqb5fbQyDvrfHJiClWnZ6q"])
```

#### *MYQL.delete(table)*
This method is always followed by a **where**. It doesn t return a response if called alone.

* ***table***: Table name

```python
>>> response = self.yql.delete('yql.storage').where(['name','=',"store://Rqb5fbQyDvrfHJiClWnZ6q"])
```

#### *MQYL.where(\*args)*

* ***\*args*** : List of conditions

```python
>>> yql.select('mytable.friends').where(['name', '=', 'alain'], ['location', '!=', 'paris'])
```

#### *MQYL.show_tables()*

List all tables 

#### *MQYL.get_guid(username)*

Return a user *guid* 

* ***username*** : yahoo id i.e 'josue_brunel'


### **Filters**

mYQL implements 2 types of filters :

* Remote filters
* Post Query Filters

##### **Remote Filters**
***Remote filters*** are defined as **tuple**, such as ***(<count\>)*** or ***(<start\>, <count\>)***.

- *Python Code* : 
```python
from myql import YQL
yql = YQL()
data = self.yql.get('geo.countries', remote_filter=(10,))
```

- *YQL Statement* :
```sql
> SELECT * FROM geo.countries(10) ;
```

- *Python Code* :

```python
data = self.yql.get('geo.countries', remote_filter=(10,20))
```

- *YQL Statement* :
```sql
> SELECT * FROM geo.countries(10,20) ;
```


##### **Post Query Filters**

**Filters** or **Function** applied to the result of the ***Query***.

- ***reverse***
```python
func_filters = ['reverse']
data = yql.select('geo.states', func_filters=func_filters).where(['place', '=', 'Congo'])
```

- ***tail***
```python
func_filters = [('tail', 2)]
data = yql.select('geo.states', func_filters=func_filters).where(['place', '=', 'Congo'])
```

- ***truncate***
```python
func_filters = [('truncate', 2)]
data = yql.select('geo.states', func_filters=func_filters).where(['place', '=', 'Congo'])
```

- ***unique***
```python
func_filters = [
    {'unique': [
        ('field','content'),
        ('hideRepeatCount','false')
    ]},
    ('truncate', 5)
]
data = yql.get('yql.table.list', func_filters=func_filters)
```

- ***sort***
```python
func_filters = [
    {'sort': [
        ('field','name'),
        ('descending','true')
    ]},
    ('tail', 10),
    #('reverse')
]
data = yql.select('geo.counties', func_filters=func_filters).where(['place', '=', 'CA'])
```
