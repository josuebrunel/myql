import pdb
import time
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import webbrowser

class OAuth(object):

    BASE_URL = "http://query.yahooapis.com/v1/yql"
    REQUEST_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/get_request_token"
    ACCESS_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/get_token"
    AUTHORIZE_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/request_auth?oauth_token="
    CALLBACK_URI = 'oob'

    def __init__(self, ck=None, cs=None):
        """
        """
        self.ck='dj0yJmk9eFJINERDYWk2M3NkJmQ9WVdrOWEyNW1VRmRGTnpZbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1iNQ--'
        self.cs='08802b459ab48eeaca765c119b0af6a4b75789f7'
        self.oauth = OAuth1(self.ck, client_secret=self.cs, callback_uri=self.CALLBACK_URI)
        
    def request_token(self,):
        """
        """
        response = requests.post(url=self.REQUEST_TOKEN_URL, auth=self.oauth)
        credentias = parse_qs(response.content)
        self.request_token = credentias.get('oauth_token')[0]
        self.request_token_secret = credentias.get('oauth_token_secret')[0]
        print(self.request_token, self.request_token_secret) 
        return self.request_token, self.request_token_secret
        
    def get_user_authorization(self,):
        """
        """
        webbrowser.open(self.AUTHORIZE_TOKEN_URL+self.request_token)
        self.verifier = raw_input("Please input a verifier: ")
        print(self.verifier)
    

if '__main__' == __name__:

    auth = OAuth()
    auth.request_token()
    auth.get_user_authorization()

