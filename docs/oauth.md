Yahoo-OAuth
=====================

The ***YOAuth*** module is not supported anymore. mYQL comes with
 ***[Yahoo-OAuth](http://yahoo-oauth.readthedocs.org/en/master/)***. 
 From now on, this will be the library to use to when you want to use **OAuth**. 
 Nothing has really changed anyway, since *yahoo-oauth* is based on *YOAuth*.

You can read the full documentation [here](http://yahoo-oauth.readthedocs.org/en/master/)

```python
>>> import myql
>>> from yahoo_oauth import OAuth1
>>> oauth = OAuth1(None, None, from_file='credentials.json')
>>> yql = myql.MYQL(format='xml',oauth=oauth)
>>> response = yql.get_guid('josue_brunel')
...
```

