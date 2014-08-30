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


  def request_token(self,):
    '''Requests access_token
    '''

    request_token, request_token_secret = self.oauth.get_request_token(params= {"oauth_callback": 'oob'})

    return request_token, request_token_secret
