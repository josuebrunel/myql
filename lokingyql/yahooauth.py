import webbrowser
from rauth import OAuth1Service

class YahooOAuth(object):
  '''OAuth for yahoo api
  '''

  def __init__(self, consumer_key= None, consumer_secret= None, base_url= None):
    '''
    '''
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret
    self.base_url = base_url

    self.oauth = OAuth1Service(
      consumer_key = consumer_key,
      consumer_secret = consumer_secret,
      name = 'yahoo',
      request_token_url = "https://api.login.yahoo.com/oauth/v2/get_request_token",
      access_token_url = "https://api.login.yahoo.com/oauth/v2/get_token",
      authorize_url = "https://api.login.yahoo.com/oauth/v2/request_auth",
      base_url = 'https://query.yahooapis.com/v1/public/yql'
    )

    self.oauth_params {
      # 'oauth_consumer_key' : 'dj0yJmk9aVRSd3ZabElmTzJNJmQ9WVdrOWEyNW1VRmRGTnpZbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1hMg--',
      'oauth_nonce' : uuid4().hex,
      'oauth_timestamp': time.time(),
      'oauth_signature_method' : 'plaintext',
      'oauth_signature' : '98407bfba41094aacd571e971fe82c9c7c1cfe60%26',
      'oauth_version' : 1.0,
      'oauth_callback' : 'oob'
    }


  def get_request_token(self,):
    '''Requests access_token and access secrets
    '''

    self.request_token, self.request_token_secret = self.oauth.get_request_token(params= self.oauth_params)

    return self.request_token, self.request_token_secret

  def authorize_url(self,):
    '''Redirects to the authorization url
    '''

    url = self.oauth.get_authorize_url(self.request_token)

    webbrowser.open(str(url))

    verifier = raw_input('Please input the verifier : ')

    return verifier

  