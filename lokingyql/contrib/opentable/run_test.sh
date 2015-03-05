if [ ! -z $1 ]; then 
    method=".$1"
else
    method=''
fi

python -m unittest test.TestYqlTable$method
