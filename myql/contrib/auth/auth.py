import pdb
import json
import time
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import webbrowser

BASE_URL = "http://query.yahooapis.com/v1/yql"
REQUEST_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/get_request_token"
ACCESS_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/get_token"
AUTHORIZE_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/request_auth?oauth_token="
CALLBACK_URI = 'oob'

class OAuth(object):
    """
    """
    def __init__(self, consumer_key, consumer_secret, **kwargs):
        """
        """
        if kwargs.get('from_file'):
            from_file = kwargs.get('from_file')
            json_data = self.json_get_data(from_file)
            vars(self).update(json_data)
        else:
            self.consumer_key = consumer_key
            self.consumer_secret = consumer_secret
            vars(self).update(kwargs)

        if not self.access_token and not self.access_token_secret:
           
            if not self.request_token and not self.request_token_secret:
                self.get_request_token()
                self.verifier = self.get_user_authorization()
                self.get_access_token()
            elif not self.verifier:
                self.verifier = self.get_user_authorization()
                self.get_access_token() 
            else:
                self.get_access_token()
        else:
            self.oauth = OAuth1(self.consumer_key, client_secret=self.consumer_secret, resource_owner_key=self.access_token, resource_owner_secret=self.access_token_secret)
    
        json_data.update({
            'request_token': self.request_token,
            'request_token_secret': self.request_token_secret,
            'verifier': self.verifier,
            'access_token': self.access_token,
            'access_token_secret': self.access_token_secret
        })

        self.json_wirte_data(json_data, from_file)

    def refresh_token(self):
        """Refresh access token
        """
        pass
        
    def fetch_tokens(self, content):
        """Parse content to fetch request/access token/token-secret
        """
        stuff = parse_qs(content)
        return stuff.get('oauth_token')[0], stuff.get('oauth_token_secret')[0]

    def json_get_data(self, filename):
        """Returns content of a json file
        """
        with open(filename) as fp:
            json_data = json.load(fp)

        return json_data

    def json_wirte_data(self, json_data, filename):
        """Write data into a json file
        """
        with open(filename, 'w') as fp:
            json.dump(json_data, fp, indent=4, encoding= 'utf-8', sort_keys=True)
            return True

        return False

    def get_request_token(self,):
        """Get request token
        """
        oauth = OAuth1(self.consumer_key, client_secret=self.consumer_secret, callback_uri=CALLBACK_URI)
        response = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
        self.request_token, self.request_token_secret = self.fetch_tokens(response.content)
        print(self.request_token, self.request_token_secret) 
        return self.request_token, self.request_token_secret
        
    def get_user_authorization(self,):
        """Get authorization
        """
        authorization_url = AUTHORIZE_TOKEN_URL+self.request_token
        print(authorization_url)
        webbrowser.open(authorization_url)
        verifier = raw_input("Please input a verifier: ")
        print(self.verifier)
        return verifier

    def get_access_token(self):
        """Get access token
        """
        oauth = OAuth1(self.consumer_key, client_secret=self.consumer_secret, resource_owner_key=self.request_token, resource_owner_secret=self.request_token_secret,verifier=self.verifier)
        response = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
        self.access_token, self.access_token_secret = self.fetch_tokens(response.content)
        print(self.access_token, self.access_token_secret)
        return self.access_token, self.access_token_secret

if '__main__' == __name__:
    auth = OAuth(None, None, from_file='credentials.json')
