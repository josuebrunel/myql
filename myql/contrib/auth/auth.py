import pdb
import json
import time
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import webbrowser
import credentials

BASE_URL = "http://query.yahooapis.com/v1/yql"
REQUEST_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/get_request_token"
ACCESS_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/get_token"
AUTHORIZE_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/request_auth?oauth_token="
CALLBACK_URI = 'oob'

class OAuth(object):

    
    def __init__(self, ck=None, cs=None):
        """
        """
        self.ck = credentials.ck
        self.cs = credentials.cs
        self.oauth = OAuth1(self.ck, client_secret=self.cs, callback_uri=CALLBACK_URI)
        
    def fetch_tokens(self, content):
        """Parse content to fetch request/access token/token-secret
        """
        stuff = parse_qs(content)
        return stuff.get('oauth_token')[0], stuff.get('oauth_token_secret')[0]

    def json_get_data(self, filename):
        """Returns content of a json file
        """
        with open(filename) as f:
            json_data = json.load(filename)

        return json_data

    def json_wirte_data(self, json_data, filename):
        """Write data into a json file
        """
        with open(filename, 'w') as f:
            json.dump(json_data, f)
            return True

        return False

    def request_token(self,):
        """Get request token
        """
        response = requests.post(url=REQUEST_TOKEN_URL, auth=self.oauth)
        self.request_token, self.request_token_secret = self.fetch_tokens(response.content)
        print(self.request_token, self.request_token_secret) 
        return self.request_token, self.request_token_secret
        
    def get_user_authorization(self,):
        """Get authorization
        """
        authorization_url = AUTHORIZE_TOKEN_URL+self.request_token
        print(authorization_url)
        webbrowser.open(authorization_url)
        self.verifier = raw_input("Please input a verifier: ")
        print(self.verifier)
    

    def get_access_token(self):
        """Get access token
        """
        self.oauth = OAuth1(self.ck, client_secret=self.cs, resource_owner_key=self.request_token, resource_owner_secret=self.request_token_secret,verifier=self.verifier)
        response = requests.post(url=ACCESS_TOKEN_URL, auth=self.oauth)
        self.access_token, self.access_token_secret = self.fetch_tokens(response.content)
        print(self.access_token, self.access_token_secret)
        return self.access_token, self.access_token_secret

if '__main__' == __name__:

    auth = OAuth()
    auth.request_token()
    auth.get_user_authorization()
    auth.get_access_token()

