import unittest

from lokingyql import LokingYQL
from lokingyql.errors import NoTableSelectedError
from lokingyql.contrib import YahooOAuth

from test_config import consumer_key, consumer_secret

class LokingYqlTest(unittest.TestCase):
  
  def setUp(self,):
    self.yql = LokingYQL()
    self.yoauth = YahooOAuth(consumer_key, consumer_secret)

  def tearUp(self,):
    pass

  def test_use(self, url= 'http://myserver.com/mytables.xml'):
    '''Tests use method
    '''
    self.yql.use(url)
    self.assertEquals(self.yql.url, url)

 # def test_select_where(self, table='geo.states', items=[''])

  def test_config(self,):
    '''Tests test config file
    '''
    conf = self.yql.loadConfig('tests.test_config')

    self.assertEquals('josue', conf.consumer_key)
    self.assertEquals('brunel', conf.consumer_secret)

  def test_desc_with_no_table(self,):
    #self.yql.desc()
    #self.assertEqual('No table selected', self.yql.desc())
    self.assertRaises(NoTableSelectedError, self.yql.desc())
    
  def test_oauth(self,):
    #Step 1: Getting the request token
    self.yoauth.get_request_token()
    #Step 2: Getting the user authorization
    self.yoauth.get_user_authorization()
    #Step 3: Getting access token
    self.yoauth.get_access_token()

    
if __name__ == "__main__":
  unittest.main()
