MYQL
====

### **Definition**

#### *MYQL(community=True, fromat='json', jsonCompact=False, crossProduct=None, debug=False, oauth=None)*

### **Methods**

#### *MYQL.payloadBuilder(query, format='json')*

Return a dictionary of parameters

* ***query*** : the YQL Query
* ***format*** : xml or json

#### *MQYL.executeQuery(payload)*

Execute the query and returns and response

* ***payload*** : Dict of parameters


#### *MYQL.rawQuery(query, format=None, pretty=False)*

Call *payloadBuilder* to build paramaters and *executeQuery* to execute que *query* then return a response.

* ***query*** : the YQL Query
* ***format*** : xml or json

#### *MYQL.clauseFormatter(condition)*

Formats conditions. 

*  ***condition*** : list of ['column', 'operator', 'value']
```python
cond = ['yid', '=', 'josue_brunel']
```


#### *MQYL.buildResponse(response)*

#### *MQYL.use(url)*

 Change the service provider

* ***url*** : url of the service provider


#### *MQYL.desc(table=None)*

Get the description of a table.
If no table name is provided, the **self.table** will be used.

* ***table*** : Table name

#### *MQYL.get(table=None, items=[], limit=None)*

Get **items** from **table**.

* ***table*** : Table name
* ***items*** : Element/columns to get from the table
* ***limit*** : limit of element to fetch


#### *MQYL.select(table=None, items=[], limit=None)*

* ***table*** : Table name
* ***items*** : Element/columns to get from the table
* ***limit*** : limit of element to fetch

```python
>>> yql.select('social.profile', ['guid', 'givenName', 'gender'])
```

#### *MQYL.where(\*args)*

* ***\*args*** : List of conditions

```python
>>> yql.select('mytable.friends').where(['name', '=', 'alain'], ['location', '!=', 'paris'])
```

#### *MQYL.showTables()*

List all tables 

#### *MQYL.getGUID(username)*

Return a user *guid* 

* ***username*** : yahoo id i.e 'josue_brunel'