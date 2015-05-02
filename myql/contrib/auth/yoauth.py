"""
YOAuth is inspired from Darren Kempiners YahooAPI https://github.com/josuebrunel/python-yahooapi/blob/master/yahooapi.py
"""
import rauth
from rauth.utils import parse_utf8_qsl

BASE_URL = "http://query.yahooapis.com/v1/yql"
REQUEST_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/get_request_token"
ACCESS_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/get_token"
AUTHORIZE_TOKEN_URL = "https://api.login.yahoo.com/oauth/v2/request_auth?oauth_token="
CALLBACK_URI = 'oob'


class YOAuth(object):
    """
    """

    #def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None, from_file=None):
    def __init__(**kwargs):
        """
        consumer_key : client key
        consumer_secret : client secret
        access_token : access token
        access_token_secret : access token secret
        from_file : file containing the credentials
        """

        pass



