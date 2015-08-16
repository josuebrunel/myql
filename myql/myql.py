"""Simple Python Wrapper of the Yahoo! Query Language
"""

from __future__ import absolute_import

import re
import logging

import requests
from myql import errors 


logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s %(levelname)s] [%(name)s.%(module)s.%(funcName)s] %(message)s \n")
logger = logging.getLogger('mYQL')

logging.getLogger('requests').disabled = True # Disabling requests default logger


class YQL(object):
    '''Yet another Python Yahoo! Query Language Wrapper
    Attributes:
    - url : data provider url
    - table : default table, so you won't have to specify a table later
    - format : default format of the responses
    - diagnostics : set to <True> to see diagnostics on queries
    - community : set to <True> to have access to community tables
    '''
    PUBLIC_URL = 'https://query.yahooapis.com/v1/public/yql'
    PRIVATE_URL = 'https://query.yahooapis.com/v1/yql'
    COMMUNITY_DATA  = "env 'store://datatables.org/alltableswithkeys'; " #Access to community table 

    FUNC_FILTERS = ['sort', 'tail', 'truncate', 'reverse', 'unique', 'sanitize']
  
    def __init__(self, community=True, format='json', jsonCompact=False, crossProduct=None, debug=False, diagnostics=False, oauth=None):
        self.community = community # True means access to community data
        self.format = format
        self._table = None
        self._query = None # used to build query when using methods such as <select>, <insert>, ...
        self._payload = {} # Last payload
        self.diagnostics = diagnostics # Who knows, someone would like to turn it ON lol
        self._limit = None
        self._offset = None
        self.crossProduct = crossProduct
        self.jsonCompact = jsonCompact
        self.debug = debug
    
        if oauth:
            self.oauth = oauth

    def __repr__(self):
        '''Returns information on the current instance
        '''
        return "<Community>: {0} - <Format>: {1} ".format(self.community, self.format)

    def _payload_builder(self, query, format=None):
        '''Build the payload'''
        if self.community :
            query = self.COMMUNITY_DATA + query # access to community data tables

        if vars(self).get('yql_table_url') : # Attribute only defined when MYQL.use has been called before
            query = "use '{0}' as {1}; ".format(self.yql_table_url, self.yql_table_name) + query

        if vars(self).get('_func'): # if post query function filters
            query = '| '.join((query, self._func))

        self._query = query
        logger.info("QUERY = %s" %(query,))

        payload = {
            'q': query,
            'callback': '',#This is not javascript
            'diagnostics': self.diagnostics,
            'format': format if format else self.format,
            'debug': self.debug,
            'jsonCompact': self.jsonCompact
        }
        if self.crossProduct:
            payload['crossProduct'] = self.crossProduct

        self._payload = payload
        logger.info("PAYLOAD = %s " %(payload, ))

        return payload

    def raw_query(self, query, format=None, pretty=False):
        '''Executes a YQL query and returns a response
        >>>...
        >>> resp = yql.raw_query('select * from weather.forecast where woeid=2502265')
        >>>
        '''
        if format:
            format = format
        else:
            format = self.format

        payload = self._payload_builder(query, format=format)
        response = self.execute_query(payload)
        if pretty:
            response = self.buildResponse(response)

        return response

    def execute_query(self, payload):
        '''Execute the query and returns and response'''
        if vars(self).get('oauth'):
            if not self.oauth.token_is_valid(): # Refresh token if token has expired
                self.oauth.refresh_token()
            response = self.oauth.session.get(self.PRIVATE_URL, params= payload, header_auth=True)
        else:
            response = requests.get(self.PUBLIC_URL, params= payload)

        self._response = response # Saving last response object.
        return response

    def _clause_formatter(self, cond):
        '''Formats conditions
        args is a list of ['field', 'operator', 'value']
        '''
        
        if len(cond) == 2 :
            cond = ' '.join(cond)
            return cond

        if 'in' in cond[1].lower() :
            if not isinstance(cond[2], str) and 'select' not in cond[2][0].lower() :
                cond[2] = "({0})".format(','.join(map(str,["'{0}'".format(e) for e in cond[2]])))
            elif not isinstance(cond[2], str) and 'select' in cond[2][0].lower() :
                cond[2] = "({0})".format(','.join(map(str,["{0}".format(e) for e in cond[2]])))
            else:
                cond[2] = "({0})".format(','.join(map(str,["{0}".format(e) for e in cond[2]])))

            cond = " ".join(cond)
        else: 
            if isinstance(cond[2], str):
                var = re.match('^@(\w+)$', cond[2])
            else:
                var = None
            if var :
                cond[2] = "{0}".format(var.group(1))
            else :
                cond[2] = "'{0}'".format(cond[2])
            cond = ' '.join(cond)

        return cond
    
    def response_builder(self, response):
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

    def _func_filters(self, filters):
        '''Build post query filters
        '''
        if not isinstance(filters, list):
            raise TypeError('func_filters must be a List')

        for i, func in enumerate(filters) :
            if isinstance(func, str) and func == 'reverse':
                filters[i] = 'reverse()'
            elif isinstance(f, dict) and f in YQL.FUNC_FILTERS:
                pass
        return '| '.join(filters) 

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
            #query = "desc {0} ".format(self._table)
            raise errors.NoTableSelectedError('No table selected')
        query = "desc {0}".format(table)
        response = self.raw_query(query)

        return response

    ##GET
    def get(self, *args, **kwargs):
        '''Just a select which returns a response
        >>> yql.get("geo.countries', ['name', 'woeid'], 5")
        '''
        self = self.select(*args, **kwargs)

        payload = self._payload_builder(self._query)
        response = self.execute_query(payload)

        return response
    
    ## SELECT
    def select(self, table=None, items=None, limit=None, offset=None, remote_filter=None, func_filters=None):
        '''This method simulate a select on a table
        >>> yql.select('geo.countries', limit=5) 
        >>> yql.select('social.profile', ['guid', 'givenName', 'gender'])
        '''
        self._table = table

        if remote_filter:
            table = "%s(%s)" %(table, ','.join(map(str, remote_filter)))

        if not items:
            items = ['*']
        self._query = "SELECT {1} FROM {0} ".format(table, ','.join(items))

        if func_filters:
            self._func = self._func_filters(func_filters) 

        self._limit = limit
        self._offset = offset
            
        return self

    ## INSERT
    def insert(self, table,items, values):
        """This method allows to insert data into table
        >>> yql.insert('bi.ly.shorten',('login','apiKey','longUrl'),('YOUR LOGIN','YOUR API KEY','YOUR LONG URL'))
        """
        values = ["'{0}'".format(e) for e in values]
        self._query = "INSERT INTO {0} ({1}) VALUES ({2})".format(table,','.join(items),','.join(values))
        payload = self._payload_builder(self._query)
        response = self.execute_query(payload)

        return response

    ## UPDATE
    def update(self, table, items, values):
        """Updates a YQL Table
        >>> yql.update('yql.storage',['value'],['https://josuebrunel.orkg']).where(['name','=','store://YEl70PraLLMSMuYAauqNc7']) 
        """
        self._table = table
        self._limit = None
        items_values = ','.join(["{0} = '{1}'".format(k,v) for k,v in zip(items,values)])
        self._query = "UPDATE {0} SET {1}".format(self._table, items_values)

        return self

    ## DELETE
    def delete(self, table):
        """Deletes record in table
        >>> yql.delete('yql.storage').where(['name','=','store://YEl70PraLLMSMuYAauqNc7'])
        """
        self._table = table
        self._limit = None
        self._query = "DELETE FROM {0}".format(self._table)

        return self

    ## WHERE
    def where(self, *args):
        ''' This method simulates a where condition. Use as follow:
        >>> yql.select('mytable').where(['name', '=', 'alain'], ['location', '!=', 'paris'])
        '''
        if not self._table:
            raise errors.NoTableSelectedError('No Table Selected')

        clause = []
        self._query += ' WHERE '
        for x in args:
            if x:
                x = self._clause_formatter(x)
                clause.append(x)

        self._query += ' AND '.join(clause)

        if self._limit :
            self._query +=  " LIMIT {0} ".format(self._limit)

        if self._offset :
            self._query +=  " OFFSET {0} ".format(self._offset)


        payload = self._payload_builder(self._query)
        response = self.execute_query(payload)

        return response


class MYQL(YQL):

    def __init__(self, *args, **kwargs):

        super(MYQL, self).__init__(**kwargs) 


    ######################################################
    #
    #                     HELPERS
    #
    #####################################################

    def get_guid(self, username):
        '''Returns the guid of the username provided
        >>> guid = self.get_guid('josue_brunel')
        >>> guid
        '''
        response = self.select('yahoo.identity').where(['yid', '=', username])
    
        return response
    
    def show_tables(self, format='json'):
        '''Return list of all available tables'''

        query = 'SHOW TABLES'
        payload = self._payload_builder(query, format) 	

        response = self.execute_query(payload) 

        return response

