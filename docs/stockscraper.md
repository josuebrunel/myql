StockScraper
============

***[StockScraper](https://github.com/gurch101/StockScraper)*** is a module written by **[Gurchet Rai](https://github.com/gurch101/)** and has just been imported into *mYQL*.

Full [Documentation](http://www.gurchet-rai.net/dev/yahoo-finance-yql)

### **Definition**

#### *StockRetriever(format='json', debug=False, oauth=None)*

* ***format*** : xml or json
* ***debug*** : True or False
* ***oauth*** : YOAuth object

```python
from myql.contrib.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
```

### **Methods**

#### *StockRetriever.get_current_info(symbolList, columns=None)*

* ***symbolList*** : List of symbol to retrieve
* ***columns*** : List of column to fetch

```python
from myql.contrib.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_current_info(["YHOO","AAPL","GOOG"])
```

#### *StockRetriever.get_news_feed(symbol)*

* ***symbol*** : Symbol news to retrieve

```python
from myql.contrib.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_news_feed('YHOO')
```

#### *StockRetriever.get_historical_info(symbol)*

* ***symbol*** : Symbol news to retrieve

```python
from myql.contrib.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_historical_info('YHOO')
```

#### *StockRetriever.get_options_info(symbol, items=[], expiration=None)*

* ***symbol*** : Symbol news to retrieve
* ***items*** : list of attributes to retrieve
* ***expiration*** : Date of expiration (type : str)

```python
from myql.contrib.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_options_info('YHOO')
```

#### *StockRetriever.get_index_summary(symbol, items=[])*

* ***symbol*** : Symbol news to retrieve
* ***items*** : list of attributes to retrieve

```python
from myql.contrib.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_index_summary('GOOG',('Volume','Change'))
```

#### *StockRetriever.get_industry_index(index_id,items=[])*

* ***index_id*** : index id
* ***items*** : list of attributes to retrieve

```python
from myql.contrib.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_industry_index(112)
```

