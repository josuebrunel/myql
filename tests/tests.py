import unittest

from lokingyql import LokingYQL
from lokingyql import YahooOAuth

from test_config import consumer_key, consumer_secret

class LokingyqlTestCase(unittest.TestCase):
  
  def setUp(self,):
    self.yql = LokingYQL()
    self.yoauth = YahooOAuth(consumer_key, consumer_secret)

  def tearUp(self,):
    pass


  def test_config(self,):
    '''Tests test config file
    '''
    conf = self.yql.loadConfig('tests.test_config')

    self.assertEquals('josue', conf.consumer_key)
    self.assertEquals('brunel', conf.consumer_secret)
    
  def test_oauth(self,):
    #Step 1: Getting the request token
    self.yoauth.get_request_token()
    #Step 2: Getting the user authorization
    self.yoauth.get_user_authorization()
    #Step 3: Getting access token
    self.yoauth.get_access_token()

    
if __name__ == "__main__":
  unittest.main()
