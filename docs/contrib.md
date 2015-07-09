##How to contribute

It's easy to contribute to ***MYQL***. 

1. Fork the repository
2. Develop your patches/fixes/features
3. Test your changes ( > py2.6 )
4. Submit a pull request

That's all

###Tips

If you want to add a new feature to the library, you better put it in ***myql/contrib/my_awesome_feature/***

Let's say i want to add a **weather** module.

```shell
$ mkdir myql/contrib/weather/
$ vim myql/contrib/__init__.py
```

```python
...
import weather
```

```shell
$ vim myql/contrib/weather/__init__.py
from weather import my_stuff
$ vim myql/contrib/weather/weather.py
```

```python
from myql.myql import MYQL # If ever you want to use the module
# Your code
```
