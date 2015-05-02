import pdb
import json
import time
import logging
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import webbrowser

BASE_URL = "http://query.yahooapis.com/v1/yql"
REQUEST_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/get_request_token"
ACCESS_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/get_token"
AUTHORIZE_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/request_auth?oauth_token="
CALLBACK_URI = 'oob'

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s %(levelname)s] [%(name)s.%(module)s.%(funcName)s] %(message)s \n")
logging.getLogger(__name__)

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

        if not vars(self).get('access_token') and not vars(self).get('access_token_secret'):
            self.get_request_token()
            self.verifier = self.get_user_authorization()
            self.get_access_token()
           # if not vars(self).get('request_token') and not vars(self).get('request_token_secret'):
           #     self.get_request_token()
           #     self.verifier = self.get_user_authorization()
           #     self.get_access_token()
           # elif not vars(self).get('verifier'):
           #     self.verifier = self.get_user_authorization()
           #     self.get_access_token() 
           # else:
           #     self.get_access_token()
        #else:
        self.oauth = OAuth1(self.consumer_key, client_secret=self.consumer_secret, resource_owner_key=self.access_token, resource_owner_secret=self.access_token_secret)
    
        json_data.update({
            #'request_token': self.request_token,
            #'request_token_secret': self.request_token_secret,
            #'verifier': self.verifier,
            'access_token': self.access_token,
            'access_token_secret': self.access_token_secret,
            'session_handle': self.session_handle,
            'token_time': time.time()
        })

        self.json_wirte_data(json_data, from_file)
    
    def isValid(self):
        """Check if the token hasn't expired
        """
        elapsed_time = time.time() - vars(self).get('token_time',0) 
        if elapsed_time > 3000 and elapsed_time < 3600:
            self.refresh_token()
            logging.debug("Token Refreshed")
            True
        elif elapsed_time > 3600:
            return False
        return True

    def refresh_token(self):
        """Refresh access token
        """
        #oauth = OAuth1(self.consumer_key, resource_owner_key=self.access_token,resource_owner_secret=self.access_token_secret)
        oauth = OAuth1(resource_owner_key=self.access_token,resource_owner_secret=self.access_token_secret)
        response = requests.post(ACCESS_TOKEN_URL, headers={'oauth_session_handle': self.session_handle}, auth=oauth)
        pdb.set_trace()
        tokens = self.fetch_tokens(response.content)
        return tokens
        
    def fetch_tokens(self, content):
        """Parse content to fetch request/access token/token-secret
        """
        stuff = parse_qs(content)
        stuff = {k:v[0] for (k,v) in stuff.items()}
        return stuff

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
        tokens = self.fetch_tokens(response.content)
        logging.debug(tokens)
        self.request_token, self.request_token_secret = tokens.get('oauth_token'), tokens.get('oauth_token_secret')
        logging.debug("{0}, {1}".format(self.request_token, self.request_token_secret)) 
        return tokens
        
    def get_user_authorization(self,):
        """Get authorization
        """
        authorization_url = AUTHORIZE_TOKEN_URL+self.request_token
        logging.debug(authorization_url)
        webbrowser.open(authorization_url)
        verifier = raw_input("Please input a verifier: ")
        logging.debug(verifier)
        return verifier

    def get_access_token(self):
        """Get access token
        """
        oauth = OAuth1(self.consumer_key, client_secret=self.consumer_secret, resource_owner_key=self.request_token, resource_owner_secret=self.request_token_secret,verifier=self.verifier)
        response = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
        tokens = self.fetch_tokens(response.content)
        logging.debug(tokens)
        self.access_token, self.access_token_secret, self.session_handle = tokens.get('oauth_token'), tokens.get('oauth_token_secret'), tokens.get('oauth_session_handle')
        logging.debug("{0} {1}".format(self.access_token, self.access_token_secret))
        return tokens

if '__main__' == __name__:
    auth = OAuth(None, None, from_file='credentials.json')
    auth.refresh_token()
