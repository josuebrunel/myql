YahooOAuth
==========

***YahooOAuth*** is 3 legged *OAuth* module dedicated to the *Yahoo! OAuth Provider*. It uses [rauth](http://rauth.readthedocs.org/en/latest/) as *oauth* library.

You only need **2** parameters to make it work :
- Your ***consumer key***
- Your ***consumer secret***

I tried to make it as painless as possible for me (and you too ;) ). Thus **3 legged OAuth** , **3 methods** and **3 steps** ( in order ) :
* YahooOAuth.get_request_token()
* YahooOAuth.get_user_authorization()
* YahooOAuth.get_access_token()

Quick start
-----------

```python
>>> from lokingyql import YahooOAuth
>>> from lokingyql.config import consumer_key, consumer_secret # config file where you have your consumer_key and consumer_secret
>>> consumer_key
'dj0yJmk9aVRSd3ZabElmTzJNJmQ9WVdrOWEyNW1VRmRGTnpZbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1hMg--'
>>> consumer_secret
'***************************' # Sorry guys it's kinda personal
>>> auth = YahooOAuth(consumer_key, consumer_secret)
>>> #Step 1:Getting request token
...
>>> auth.get_request_token()
(u'hjmbdag', u'cdb5688ed78a54e4e87f8456580f8197b2069270')
>>> #Step 2: Getting User Authorization
...
>>> auth.get_user_authorization() 
```

* Granting access

![Alt grant](../../../static/img/grant.png)

* Getting code 

![Alt code](../../../static/img/code.png)

```python
Please input the verifier : 2k8akm
'2k8akm'
>>> #Step 3:Getting access token
...
>>> auth.get_access_token()
(u'A=pxautZv7kC.gB_I7UvbIv9GN1XB2Ky7Ql1EOie0KTzvjKTZfd5OpqlKF3WLRhEz1qxyUfbtQsCELg5NqrHHcnA8n8CytqMfZsTLLJLFi4mKZX6L3R4xbt1jbTY_dW6wM5ffz18SJOHLQVhFXjC2U826fndT.eBpVh5hJ8QGcxKYaEiqhwue7LqXtFEUnSEzDsCebR5ZsUsi_T7dKHZ9DL4tNfpi81Il0o9xkakkJt9i2raXrC49J7Ds8tUpjkhSbuay_HcDLeZwXOW4WN1TXIP_6ZofAP9dzdD3mOm.u9wONzontMraUjE6wSic8k0UfOHvcIJTV5JITpYjjw7BX3r.NU119rZqo_VGpIDecZmPXkRKy6w.4g9xfBize0hgh8118j5qXMbSW50bOwhTDyF2k3wVfhBc9qYwUTgsFE1GJeJCx0jU2Y6re6OuOp4NDmTZsaCm1pG7D180nvGq_5j3Tf0OSYRo6noffhbMZ.KnnkBRdu9a0.a5GCBC4RKKBUtd4EW7zNF5sODlVLjisa4RZ5XwzfKSafmNrAeSibVc.WRDhleMziKcf3jPmafHx09xbCfDWUg8FOMOKWaJzr_ocjUIqPXQUG6ryzRw61IkajCvQ_LGLa_q3eBwT3WCxTOBm2x9hb6Hw1CVTvV_CbeevE7jGrcyJH6UH69YgdpG0A1vGFhLSRh.bpiyTuxYCxFByZKxR8onSblcY6wG5NDq_kbcmtyYFmIVLoPqPk9SCuBeRQYpMoyumv0U8FfJVvijE8b41PCzEKexCrfLdmbKYDmsFaeS_oghC0WjkGCZVQX7nmt.XJYntr8dzdVBqJcU6YG0NGpYGQp_r9B_0vlqmjfj61fXkFIxGsNTMArOShw--', u'795a47a1e1dc2385130ec1e738177dd9694d970a')
>>>
```

As you noticed, all we needed were a *consumer_key* and *consumer_secret* .

Access to some attributes (it's just python)
---------------------------------------------

```python
>>> auth.request_token
u'hjmbdag'
>>> auth.request_token_secret
u'cdb5688ed78a54e4e87f8456580f8197b2069270'
>>> auth.verifier
'2k8akm'
>>> auth.access_token
u'A=pxautZv7kC.gB_I7UvbIv9GN1XB2Ky7Ql1EOie0KTzvjKTZfd5OpqlKF3WLRhEz1qxyUfbtQsCELg5NqrHHcnA8n8CytqMfZsTLLJLFi4mKZX6L3R4xbt1jbTY_dW6wM5ffz18SJOHLQVhFXjC2U826fndT.eBpVh5hJ8QGcxKYaEiqhwue7LqXtFEUnSEzDsCebR5ZsUsi_T7dKHZ9DL4tNfpi81Il0o9xkakkJt9i2raXrC49J7Ds8tUpjkhSbuay_HcDLeZwXOW4WN1TXIP_6ZofAP9dzdD3mOm.u9wONzontMraUjE6wSic8k0UfOHvcIJTV5JITpYjjw7BX3r.NU119rZqo_VGpIDecZmPXkRKy6w.4g9xfBize0hgh8118j5qXMbSW50bOwhTDyF2k3wVfhBc9qYwUTgsFE1GJeJCx0jU2Y6re6OuOp4NDmTZsaCm1pG7D180nvGq_5j3Tf0OSYRo6noffhbMZ.KnnkBRdu9a0.a5GCBC4RKKBUtd4EW7zNF5sODlVLjisa4RZ5XwzfKSafmNrAeSibVc.WRDhleMziKcf3jPmafHx09xbCfDWUg8FOMOKWaJzr_ocjUIqPXQUG6ryzRw61IkajCvQ_LGLa_q3eBwT3WCxTOBm2x9hb6Hw1CVTvV_CbeevE7jGrcyJH6UH69YgdpG0A1vGFhLSRh.bpiyTuxYCxFByZKxR8onSblcY6wG5NDq_kbcmtyYFmIVLoPqPk9SCuBeRQYpMoyumv0U8FfJVvijE8b41PCzEKexCrfLdmbKYDmsFaeS_oghC0WjkGCZVQX7nmt.XJYntr8dzdVBqJcU6YG0NGpYGQp_r9B_0vlqmjfj61fXkFIxGsNTMArOShw--'
>>> auth.access_token_secret
u'795a47a1e1dc2385130ec1e738177dd9694d970a'
>>>
```

2 Legged OAuth (Coming pretty soon)
-----------------------------------

In *2 legged OAuth* the **User Authorization** isn't required anymore ...

Voila ...


