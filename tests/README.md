How to test the Library (if cloned the rep)
=======================

Get to the root directory of the module

* Config file test

```shell
python -m unittest tests.LokingyqlTestCase.test_config
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
``` 

* OAuth Config : Don't forget to put your credentials in the test_config.py

```shell
(lokingYQL)josue@LokingMac:~/Dropbox/Workspace/lokingYQL$ python -m unittest tests.LokingyqlTestCase
Please input the verifier : pc25wf
.
----------------------------------------------------------------------
Ran 1 test in 18.488s

OK
(lokingYQL)josue@LokingMac:~/Dropbox/Workspace/lokingYQL$
```



