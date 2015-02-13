import time
import hmac
import hashlib
from uuid import uuid4

URI_REQUEST_TOKEN ='https://api.login.yahoo.com/oauth/v2/get_request_token'

oauth_params = {
  'oauth_consumer_key' : 'dj0yJmk9aVRSd3ZabElmTzJNJmQ9WVdrOWEyNW1VRmRGTnpZbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1hMg--',
  'oauth_nonce' : uuid4().hex,
  'oauth_timestamp': time.time(),
  'oauth_signature_method' : 'plaintext',
  'oauth_signature' : '98407bfba41094aacd571e971fe82c9c7c1cfe60%26',
  'oauth_version' : 1.0,
  'oauth_callback' : 'oob' 
}

consumer_key = 'dj0yJmk9aVRSd3ZabElmTzJNJmQ9WVdrOWEyNW1VRmRGTnpZbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1hMg--'

consumer_secret = '98407bfba41094aacd571e971fe82c9c7c1cfe60'