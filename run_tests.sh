if [ ! -z $1 ]; then
    suite=".$1"
else
    suite="all"
fi

if [ ! -z $2 ]; then 
    method=".$2"
else
    method=''
fi

if [ $suite != "all" ];then
    python -m unittest tests$suite$method
else
    python -m unittest tests.TestMYQL$method
    python -m unittest tests.TestStockParser
    python -m unittest tests.TestTable$method

    if [ -f credentials.json ]; then
         python -m unittest tests.TestOAuth
    fi
fi
