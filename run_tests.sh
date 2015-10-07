if [ ! -z $1 ]; then
    TestCase="::${1}"
else
    TestCase=''
fi 

if [ ! -z $2 ]; then
    Test="::${2}"
else
    Test=''
fi

coverage run --source=myql -m pytest -vs tests/tests.py$TestCase$Test
coverage report
coverage html
