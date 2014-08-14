import requests

class LokingYQL(object):

  def __init__(self, table=None, format='json'):
    self.url = 'https://query.yahooapis.com/v1/public/yql'	  
    self.table = table
    self.format = format

  def __repr__(self):
    pass

  def payloadBuilder(self, query, format='json'):
    '''Build the payload'''
    payload = {
	'q' : query,
	'callback' : '', #This is not javascript
	'diagnostics' : 'true', # always true
	'format' : format
    }

    return payload

  def rawQuery(self, query, format='json', pretty=True):
    '''Executes a YQL query and returns a response
       >>>...
       >>> resp = yql.rawQuery('select * from weather.forecast where woeid=2502265')
       >>> 
    '''
    payload = self.payloadBuilder(query, format)
    response = self.executeQuery(payload)
    if pretty_response :
      response = self.buildResponse(response)

    return response

  def executeQuery(self, payload):
    '''Execute the query and returns and formatted response'''
    response = requests.get(self.url, params= payload)

    return response

  def buildResponse(self, response):
    
    try:
      r = response.json()
      result = r['query']['results']['table']
      response = {
        'num_result': len(result) if isintanceof(result, list) else 0 ,
        'result': result
      }
    except Exception, e:
      print(response.content)
    return response

  #
  # Actions
  #

  def select(self, table=None):
    '''This method simulate a select on a table'''
    try:
      self.current_table = table
    except Exception, e:
      print(e)

    return self

  def where(self, conditions):
     ''' This method simulates a where condition. Use as follow:
         yql.select('mytable').where(dict)
     '''
     pass

  def showTables(self, format='json'):
    '''Return list of all avaible tables'''

    query = 'SHOW TABLES'
    payload = self.payloadBuilder(query, format) 	

    response = self.executeQuery(payload) 

    return response
