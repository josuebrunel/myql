import requests

class LokingYQL(object):

  def __init__(self, table=None, format='json'):
    self.url = 'https://query.yahooapis.com/v1/public/yql'	  
    self.table = table
    self.format = format

  def __repr__(self):
    pass


  def queryBuilder(self, table):
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

  def runQuery(self, payload):
    '''Execute the query'''
    response = requests.get(self.url, params= payload)

    return response

  #
  # Actions
  #

  def showTables(self, format='json'):
    '''Return list of all avaible tables'''

    query = 'SHOW TABLES'
    payload = self.payloadBuilder(query, format) 	

    response = self.runQuery(payload) 

    return response
