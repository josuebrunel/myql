if [ ! -z $1 ]; then 
    method=".$1"
else
    method=''
fi

python -m unittest tests.TestTable$method
if [ -f credentials.json ]; then
    python -m unittest tests.TestOAuth
fi
