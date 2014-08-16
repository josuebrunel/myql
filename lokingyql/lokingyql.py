import requests

class LokingYQL(object):
  '''Yet another Python Yahoo! Query Language Wrapper
  '''
  default_url = 'https://query.yahooapis.com/v1/public/yql'	  
  
  def __init__(self, table=None, url=default_url, format='json'):
    self.url = url
    self.table = table
    self.format = format

  def __repr__(self):
    '''Returns information on the current instance
    '''
    return "<url>: '{0}' - <table>: '{1}' -  <format> : '{2}' ".format(self.url, self.table, self.format)

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
    #if pretty :
    #  response = self.buildResponse(response)

    return response

  def executeQuery(self, payload):
    '''Execute the query and returns and response'''
    response = requests.get(self.url, params= payload)

    return response

  def buildResponse(self, response):
    '''Try to return a pretty formatted response object
    '''
    try:
      r = response.json()
      result = r['query']['results']['table']
      response = {
        'num_result': len(result) if isinstance(result, list) else 0 ,
        'result': result
      }
    except Exception, e:
      print(e)
      return response.content
    return response

  def buildSelectQuery(conditions):
    '''Builds the query for the select method ''' 
    return query
  ######################################################
  #
  #                 ORM METHODS
  #
  #####################################################

  def use(self, url):
    '''Changes the data provider
    '''
    self.url = url
    return self.url

  def select(self, table=None):
    '''This method simulate a select on a table
       >>> yql.select('table')
    '''
    try:
      self.current_table = table
    except Exception, e:
      print(e)

    return self

  def where(self, *args):
     ''' This method simulates a where condition. Use as follow:
         >>>yql.select('mytable').where([('name', '=', 'alain'), ('location', '!=', 'paris')])
     '''
     return None

  def showTables(self, format='json'):
    '''Return list of all avaible tables'''

    query = 'SHOW TABLES'
    payload = self.payloadBuilder(query, format) 	

    response = self.executeQuery(payload) 

    return response
