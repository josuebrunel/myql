import time
import webbrowser
from uuid import uuid4
from rauth import OAuth1Service

class YahooOAuth(object):
  '''OAuth for yahoo api
  '''

  default_base_url = 'http://query.yahooapis.com/v1/yql'

  def __init__(self, consumer_key= None, consumer_secret= None, base_url= default_base_url):
    '''
    '''
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret
    self.base_url = base_url
    self.service = OAuth1Service(
      consumer_key = consumer_key,
      consumer_secret = consumer_secret,
      name = 'yahoo',
      request_token_url = "https://api.login.yahoo.com/oauth/v2/get_request_token",
      access_token_url = "https://api.login.yahoo.com/oauth/v2/get_token",
      authorize_url = "https://api.login.yahoo.com/oauth/v2/request_auth",
      base_url = base_url
    )

    self.params = {
      'oauth_version' : 1.0,
      'oauth_callback' : 'oob'
    }


  def get_request_token(self,):
    '''Requests access_token and access secrets
    '''

    self.request_token, self.request_token_secret = self.service.get_request_token(params= self.params)

    return self.request_token, self.request_token_secret

  def get_user_authorization(self,):
    '''Redirects to the authorization url
    '''

    url = self.service.get_authorize_url(self.request_token)

    webbrowser.open(str(url))

    self.verifier = raw_input('Please input the verifier : ')

    return self.verifier

  def get_access_token(self,):
    '''Get oauth_token
    '''

    self.access_token, self.access_token_secret = self.service.get_access_token(self.request_token, self.request_token_secret, params={'oauth_verifier': self.verifier})

    return self.access_token, self.access_token_secret

  #Left to be done
  def refresh_token(self):
    '''Refresh the access_token
    '''
    pass

  #Not finsished yet
  def authenticate(self,):
    '''Handles the authentication process
    '''
    self.get_request_token()
    self.get_user_authorization()
    self.get_access_token()

    self.payload = {
      'realm': "yahoo.apis.com",
    }