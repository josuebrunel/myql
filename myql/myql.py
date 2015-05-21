import logging
import requests
from contrib.auth import YOAuth
import errors

import importlib

__author__ = 'Josue Kouka'
__email__ = 'josuebrunel@gmail.com'

logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s %(levelname)s] [%(name)s.%(module)s.%(funcName)s] %(message)s \n")
logger = logging.getLogger(__name__)

logging.getLogger('requests').setLevel(logging.WARNING)

class MYQL(object):
  '''Yet another Python Yahoo! Query Language Wrapper
  Attributes:
  - url : data provider url
  - table : default table, so you won't have to specify a table later
  - format : default format of the responses
  - diagnostics : set to <True> to see diagnostics on queries
  - community : set to <True> to have access to community tables
  '''
  public_url = 'https://query.yahooapis.com/v1/public/yql'
  private_url = 'http://query.yahooapis.com/v1/yql'
  community_data  = "env 'store://datatables.org/alltableswithkeys'; " #Access to community table 
  
  def __init__(self, table=None, url=public_url, community=False, format='json', jsonCompact=False, crossProduct=None, debug=False, oauth=None):
    #self.url = url
    self.table = table
    self.format = format
    self._query = None # used to build query when using methods such as <select>, <insert>, ...
    self._payload = {} # Last payload
    self.diagnostics = False # Who knows, someone would like to turn it ON lol
    self.limit = ''
    self.community = community # True means access to community data
    self.crossProduct = crossProduct
    self.jsonCompact = jsonCompact
    self.debug = debug
    
    if oauth:
        self.oauth = oauth

  def __repr__(self):
    '''Returns information on the current instance
    '''
    return "<url>: '{0}' - <table>: '{1}' -  <format> : '{2}' ".format(self.url, self.table, self.format)

  def payloadBuilder(self, query, format=None):
    '''Build the payload'''
    if self.community :
      query = self.community_data + query # access to community data tables

    if vars(self).get('yql_table_url') : # Attribute only defined when MYQL.use has been called before
      query = "use '{0}' as {1}; ".format(self.yql_table_url, self.yql_table_name) + query

    self._query = query
    logger.debug(query)
    
    payload = {
	  'q' : query,
	  'callback' : '', #This is not javascript
	  'diagnostics' : self.diagnostics, 
	  'format' : format if format else self.format,
      'debug': self.debug,
      'jsonCompact': self.jsonCompact
    }
    if self.crossProduct:
        payload['crossProduct'] = self.crossProduct
    
    self._payload = payload
    logger.debug(payload) 

    return payload

  def rawQuery(self, query, format=None, pretty=False):
    '''Executes a YQL query and returns a response
       >>>...
       >>> resp = yql.rawQuery('select * from weather.forecast where woeid=2502265')
       >>> 
    '''
    if format:
      format = format
    else:
      format = self.format
    
    payload = self.payloadBuilder(query, format=format)
    response = self.executeQuery(payload)
    if pretty :
      response = self.buildResponse(response)

    return response

  def executeQuery(self, payload):
    '''Execute the query and returns and response'''
    if vars(self).get('oauth'): 
        #self.url = self.private_url
        if not self.oauth.token_is_valid(): # Refresh token if token has expired
            self.oauth.refresh_token()
        response = self.oauth.session.get(self.private_url, params= payload, header_auth=True)
    else:
        response = requests.get(self.public_url, params= payload)

    self._response = response # Saving last response object.
    return response

  def clauseFormatter(self, cond):
    '''Formats conditions
       args is a list of ['column', 'operator', 'value']
    '''
    if cond[1].lower() == 'in':
      cond[2] = "({0})".format(','.join(map(str,[ "'{0}'".format(e) for e in cond[2] ])))
      cond = ' '.join(cond)
    else:
      cond[2] = "'{0}'".format(cond[2])
      cond = ''.join(cond)

    return cond
    
  def buildResponse(self, response):
    '''Try to return a pretty formatted response object
    '''
    try:
      r = response.json()
      result = r['query']['results']
      response = {
        'num_result': r['query']['count'] ,
        'result': result
      }
    except (Exception,) as e:
      print(e)
      return response.content
    return response


  ######################################################
  #
  #                 MAIN METHODS
  #
  #####################################################

  ##USE
  def use(self, url, name='mytable'):
    '''Changes the data provider
    >>> yql.use('http://myserver.com/mytables.xml')
    '''
    self.yql_table_url = url
    self.yql_table_name = name
    return {'table url': url, 'table name': name}

  ##DESC
  def desc(self, table=None):
    '''Returns table description
    >>> yql.desc('geo.countries')
    >>>
    '''
    if not table:
      #query = "desc {0} ".format(self.table)
      raise errors.NoTableSelectedError('No table selected')
    query = "desc {0}".format(table)
    response = self.rawQuery(query)

    return response

  ##GET
  def get(self, table=None, items=[], limit=''):
    '''Just a select which returns a response
    >>> yql.get("geo.countries', ['name', 'woeid'], 5")
    '''
    self.table = table
    if not items:
        items = ['*'] 
    self._query = "SELECT {1} FROM {0} ".format(self.table, ','.join(items))
    if limit:
        self._query += "limit {0}".format(limit)

    if not self.table :
        raise errors.NoTableSelectedError('Please select a table')
    
    payload = self.payloadBuilder(self._query)
    response = self.executeQuery(payload)

    return response
      
    
  ## SELECT
  def select(self, table=None, items=[], limit=''):
    '''This method simulate a select on a table
    >>> yql.select('geo.countries', limit=5) 
    >>> yql.select('social.profile', ['guid', 'givenName', 'gender'])
    '''
    self.table = table
    if not items:
      items = ['*']
    self._query = "SELECT {1} FROM {0} ".format(self.table, ','.join(items))
    try: #Checking wether a limit is set or not
      self._limit = limit
    except (Exception,) as e:
      pass

    return self

  ## INSERT
  def insert(self, table,items, values):
      """This method allows to insert data into table
      >>> yql.insert('bi.ly.shorten',('login','apiKey','longUrl'),('YOUR LOGIN','YOUR API KEY','YOUR LONG URL'))
      """
      values = ["'{0}'".format(e) for e in values]
      self._query = "INSERT INTO {0} ({1}) VALUES ({2})".format(table,','.join(items),','.join(values))
      payload = self.payloadBuilder(self._query)
      response = self.executeQuery(payload)

      return response

  ## UPDATE
  def update(self, table, items, values):
      """Updates a YQL Table
      >>> yql.update('yql.storage',['value'],['https://josuebrunel.orkg']).where(['name','=','store://YEl70PraLLMSMuYAauqNc7']) 
      """
      self.table = table
      self._limit = None
      items_values = ','.join(["{0} = '{1}'".format(k,v) for k,v in zip(items,values)])
      self._query = "UPDATE {0} SET {1}".format(self.table, items_values)

      return self

  ## DELETE
  def delete(self, table):
      """Deletes record in table
      >>> yql.delete('yql.storage').where(['name','=','store://YEl70PraLLMSMuYAauqNc7'])
      """
      self.table = table
      self._limit = None
      self._query = "DELETE FROM {0}".format(self.table)

      return self

  ## WHERE
  def where(self, *args):
    ''' This method simulates a where condition. Use as follow:
    >>> yql.select('mytable').where(['name', '=', 'alain'], ['location', '!=', 'paris'])
    '''
    if not self.table:
      raise errors.NoTableSelectedError('No Table Selected')

    clause = []
    self._query += ' WHERE '
    for x in args:
      if x:
        x = self.clauseFormatter(x)
        clause.append(x)

    self._query += ' AND '.join(clause)

    if self._limit :
      self._query +=  " LIMIT {0}".format(self._limit)

    payload = self.payloadBuilder(self._query)
    response = self.executeQuery(payload)

    return response

  ######################################################
  #
  #                     HELPERS
  #
  #####################################################

  def getGUID(self, username):
    '''Returns the guid of the username provided
       >>> guid = self.getGUID('josue_brunel')
       >>> guid
    '''
    response = self.select('yahoo.identity').where(['yid', '=', username])
    
    return response
    
  def showTables(self, format='json'):
    '''Return list of all available tables'''

    query = 'SHOW TABLES'
    payload = self.payloadBuilder(query, format) 	

    response = self.executeQuery(payload) 

    return response

