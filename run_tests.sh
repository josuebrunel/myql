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
    python -m unittest tests.TestMYQL
    python -m unittest tests.TestStockParser.{get_current_info,get_news_feed,get_historical_info,get_options_info,get_index_summary,get_industry_index}
    python -m unittest tests.TestTable

    if [ -f credentials.json ]; then
         python -m unittest tests.TestOAuth
    fi
fi
