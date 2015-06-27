StockScraper
============

***[StockScraper](https://github.com/gurch101/StockScraper)*** is a module written by **[Gurchet Rai](https://github.com/gurch101/)** and has just been imported into *mYQL*.

Full [Documentation](http://www.gurchet-rai.net/dev/yahoo-finance-yql)

### **Definition**

#### *StockRetriever(format='json', debug=False, oauth=None)*

* ***format*** : xml or json
* ***debug*** : True or False
* ***oauth*** : yahoo_oauth (OAuth1)

```python
from myql.contrib.finance.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
```

### **Methods**

#### *StockRetriever.get_current_info(symbolList, columns=None)*

* ***symbolList*** : List of symbol to retrieve
* ***columns*** : List of column to fetch

```python
from myql.contrib.finance.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_current_info(["YHOO","AAPL","GOOG"])
```

```json
{
    "query": {
        "count": 3,
        "created": "2015-05-20T12:56:27Z",
        "lang": "en-US",
        "results": {
            "quote": [
                {
                    "AfterHoursChangeRealtime": null,
                    "AnnualizedGain": null,
                    "Ask": "42.22",
                    "AskRealtime": null,
                    "AverageDailyVolume": "13763800",
                    "Bid": "42.20",
                    "BidRealtime": null,
                    "BookValue": "35.91",
                    "Change": "-3.38",
                    "ChangeFromFiftydayMovingAverage": "-3.03",
                    "ChangeFromTwoHundreddayMovingAverage": "-5.46",
                    "ChangeFromYearHigh": "-11.64",
                    "ChangeFromYearLow": "8.05",
                    "ChangePercentRealtime": null,
                    "ChangeRealtime": null,
                    "Change_PercentChange": "-3.38 - -7.62%",
                    "ChangeinPercent": "-7.62%",
                    "Commission": null,
                    "Currency": "USD",
                    "DaysHigh": "44.66",
                    "DaysLow": "39.12",
                    "DaysRange": "39.12 - 44.66",
                    "DaysRangeRealtime": null,
                    "DaysValueChange": null,
                    "DaysValueChangeRealtime": null,
                    "DividendPayDate": null,
                    "DividendShare": null,
                    "DividendYield": null,
                    "EBITDA": "598.70M",
                    "EPSEstimateCurrentYear": "0.78",
                    "EPSEstimateNextQuarter": "0.21",
                    "EPSEstimateNextYear": "0.79",
                    "EarningsShare": "7.32",
                    "ErrorIndicationreturnedforsymbolchangedinvalid": null,
                    "ExDividendDate": null,
                    "FiftydayMovingAverage": "44.01",
                    "HighLimit": null,
                    "HoldingsGain": null,
                    "HoldingsGainPercent": null,
                    "HoldingsGainPercentRealtime": null,
                    "HoldingsGainRealtime": null,
                    "HoldingsValue": null,
                    "HoldingsValueRealtime": null,
                    "LastTradeDate": "5/19/2015",
                    "LastTradePriceOnly": "40.98",
                    "LastTradeRealtimeWithTime": null,
                    "LastTradeTime": "4:00pm",
                    "LastTradeWithTime": "4:00pm - <b>40.98</b>",
                    "LowLimit": null,
                    "MarketCapRealtime": null,
                    "MarketCapitalization": "38.46B",
                    "MoreInfo": null,
                    "Name": "Yahoo! Inc.",
                    "Notes": null,
                    "OneyrTargetPrice": "54.45",
                    "Open": "44.48",
                    "OrderBookRealtime": null,
                    "PEGRatio": "-4.24",
                    "PERatio": "5.60",
                    "PERatioRealtime": null,
                    "PercebtChangeFromYearHigh": "-22.12%",
                    "PercentChange": "-7.62%",
                    "PercentChangeFromFiftydayMovingAverage": "-6.89%",
                    "PercentChangeFromTwoHundreddayMovingAverage": "-11.75%",
                    "PercentChangeFromYearLow": "+24.45%",
                    "PreviousClose": "44.36",
                    "PriceBook": "1.24",
                    "PriceEPSEstimateCurrentYear": "52.54",
                    "PriceEPSEstimateNextYear": "51.22",
                    "PricePaid": null,
                    "PriceSales": "8.84",
                    "SharesOwned": null,
                    "ShortRatio": "2.10",
                    "StockExchange": "NMS",
                    "Symbol": "YHOO",
                    "TickerTrend": null,
                    "TradeDate": null,
                    "TwoHundreddayMovingAverage": "46.44",
                    "Volume": "48892169",
                    "YearHigh": "52.62",
                    "YearLow": "32.93",
                    "YearRange": "32.93 - 52.62",
                    "symbol": "YHOO"
                },
                ...
            ]
        }
    }
}
```

#### *StockRetriever.get_news_feed(symbol)*

* ***symbol*** : Symbol news to retrieve

```python
from myql.contrib.finance.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_news_feed('YHOO')
```

```json
{
    "query": {
        "count": 2,
        "created": "2015-05-20T13:05:27Z",
        "lang": "en-US",
        "results": {
            "item": [
                {
                    "description": null,
                    "link": "http://us.rd.yahoo.com/finance/news/rss/story/*http://finance.yahoo.com/news/video-may-20-premarket-briefing-110800770.html",
                    "title": "May 20 Premarket Briefing: 10 Things You Should Know"
                },
                {
                    "description": "[at MarketWatch] - How alarmed should be about a former Fed\u2019s warning on a taper tantrum and volatility, from China to Yahoo.",
                    "link": "http://us.rd.yahoo.com/finance/external/cbsm/rss/SIG=11iiumket/*http://www.marketwatch.com/News/Story/Story.aspx?guid=F8AC52CC-FEAB-11E4-8608-290076337AAF&siteid=yhoof2",
                    "title": "Why it might pay to listen to a Fed old timer\u2019s tantrum warning"
                }
            ]
        }
    }
}
```

#### *StockRetriever.get_historical_info(symbol, items=None, startDate=None, endDate=None, limit=None)*

* ***symbol*** : Symbol news to retrieve
* ***items*** : columns to retrieve
* ***startDate*** : starting date
* ***endDate*** : ending date
* ***limit*** : number of results to return

```python
from myql.contrib.finance.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_historical_info('YHOO',items=['Open','Close','High','Low'], limit=5,startDate='2014-09-11',endDate='2015-02-10')
```

```json
{
    "query": {
        "count": 5, 
        "created": "2015-05-24T05:12:21Z", 
        "lang": "en-US", 
        "results": {
            "quote": [
                {
                    "Close": "43.07", 
                    "High": "43.18", 
                    "Low": "42.66", 
                    "Open": "42.90"
                }, 
                {
                    "Close": "42.57", 
                    "High": "43.15", 
                    "Low": "42.54", 
                    "Open": "42.61"
                }, 
                {
                    "Close": "42.94", 
                    "High": "43.66", 
                    "Low": "42.67", 
                    "Open": "43.57"
                }, 
                {
                    "Close": "43.55", 
                    "High": "44.26", 
                    "Low": "43.03", 
                    "Open": "44.08"
                }, 
                {
                    "Close": "44.05", 
                    "High": "44.98", 
                    "Low": "43.88", 
                    "Open": "44.80"
                }
            ]
        }
    }
}

```

#### *StockRetriever.get_options_info(symbol, items=[], expiration=None)*

* ***symbol*** : Symbol news to retrieve
* ***items*** : list of attributes to retrieve
* ***expiration*** : Date of expiration (type : str)

```python
from myql.contrib.finance.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_options_info('YHOO')
```

```json
{
    "query": {
        "count": 1,
        "created": "2015-05-20T13:09:02Z",
        "lang": "en-US",
        "results": {
            "optionsChain": {
                "symbol": "YHOO"
            }
        }
    }
}
```

#### *StockRetriever.get_index_summary(symbol, items=[])*

* ***symbol*** : Symbol news to retrieve
* ***items*** : list of attributes to retrieve

```python
from myql.contrib.finance.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_index_summary('GOOG',('Volume','Change'))
```

```json
{
    "query": {
        "count": 1,
        "created": "2015-05-20T13:09:48Z",
        "lang": "en-US",
        "results": {
            "quote": {
                "Change": null,
                "Volume": "16"
            }
        }
    }
}
```

#### *StockRetriever.get_industry_index(index_id,items=[])*

* ***index_id*** : index id
* ***items*** : list of attributes to retrieve

```python
from myql.contrib.finance.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_industry_index(112)
```

```json
{
    "query": {
        "count": 1,
        "created": "2015-05-20T13:10:55Z",
        "lang": "en-US",
        "results": {
            "industry": {
                "company": [
                    {
                        "name": "Adarsh\nPlant Protect Ltd",
                        "symbol": "ADARSHPL.BO"
                    },
                    {
                        "name": "African\nPotash Ltd",
                        "symbol": "AFPO.L"
                    },
                    {
                        "name": "Agrium\nInc",
                        "symbol": "AGU.DE"
                    },
                    {
                        "name": "Agrium\nInc",
                        "symbol": "AGU.TO"
                    },
                    ...
                    {
                        "name": "Zuari\nAgro Chemicals Ltd",
                        "symbol": "ZUARI.NS"
                    },
                    {
                        "name": "Zuari\nGlobal Ltd",
                        "symbol": "ZUARIAGRO.NS"
                    },
                    {
                        "name": "Zuari\nGlobal Ltd",
                        "symbol": "ZUARIIND.BO"
                    }
                ],
                "id": "112",
                "name": ""
            }
        }
    }
}
```

#### *StockRetriever.get_xchange_rate(pairs, items=None)*

```python
from myql.contrib.finance.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_xchange_rate(['EURUSD','GBPUSD'])
```

```json
{
    "query": {
        "count": 2, 
        "created": "2015-06-27T13:48:51Z", 
        "lang": "en-US", 
        "results": {
            "rate": [
                {
                    "Ask": "1.1174", 
                    "Bid": "1.1162", 
                    "Date": "6/27/2015", 
                    "Name": "EUR/USD", 
                    "Rate": "1.1168", 
                    "Time": "12:53pm", 
                    "id": "EURUSD"
                }, 
                {
                    "Ask": "1.5756", 
                    "Bid": "1.5738", 
                    "Date": "6/27/2015", 
                    "Name": "GBP/USD", 
                    "Rate": "1.5747", 
                    "Time": "12:53pm", 
                    "id": "GBPUSD"
                }
            ]
        }
    }
}

```

#### *StockRetriever.get_dividendhistory(symbol, startDate, endDate)*

```python
from myql.contrib.finance.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_dividendhistory('AAPL',"2008-01-01", "2015-06-15")
```

```json
{
    "query": {
        "count": 12, 
        "created": "2015-06-27T13:42:27Z", 
        "lang": "en-US", 
        "results": {
            "quote": [
                {
                    "Date": "2015-05-07", 
                    "Dividends": "0.520000", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2015-02-05", 
                    "Dividends": "0.470000", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2014-11-06", 
                    "Dividends": "0.470000", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2014-08-07", 
                    "Dividends": "0.470000", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2014-05-08", 
                    "Dividends": "0.470000", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2014-02-06", 
                    "Dividends": "0.435710", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2013-11-06", 
                    "Dividends": "0.435710", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2013-08-08", 
                    "Dividends": "0.435710", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2013-05-09", 
                    "Dividends": "0.435710", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2013-02-07", 
                    "Dividends": "0.378570", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2012-11-07", 
                    "Dividends": "0.378570", 
                    "Symbol": "AAPL"
                }, 
                {
                    "Date": "2012-08-09", 
                    "Dividends": "0.378570", 
                    "Symbol": "AAPL"
                }
            ]
        }
    }
}

```

#### *StockRetriever.get_symbols(company_name)*

&nbsp;&nbsp;&nbsp;&nbsp; **Always returns data as JSON**

```python
from myql.contrib.finance.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_symbols('Google')
```

```json
{
    "ResultSet": {
        "Query": "google",
        "Result": [
            {
                "exch": "NMS",
                "exchDisp": "NASDAQ",
                "name": "Google Inc.",
                "symbol": "GOOG",
                "type": "S",
                "typeDisp": "Equity"
            },
            {
                "exch": "NMS",
                "exchDisp": "NASDAQ",
                "name": "Google Inc.",
                "symbol": "GOOGL",
                "type": "S",
                "typeDisp": "Equity"
            },
            {
                "exch": "GER",
                "exchDisp": "XETRA",
                "name": "Google Inc.",
                "symbol": "GGQ7.DE",
                "type": "S",
                "typeDisp": "Equity"
            },
            {
                "exch": "MEX",
                "exchDisp": "Mexico",
                "name": "Google Inc.",
                "symbol": "GOOG.MX",
                "type": "S",
                "typeDisp": "Equity"
            },
            {
                "exch": "MEX",
                "exchDisp": "Mexico",
                "name": "GOOGLE-A",
                "symbol": "GOOGL.MX",
                "type": "S",
                "typeDisp": "Equity"
            },
            {
                "exch": "BUE",
                "exchDisp": "Buenos Aires",
                "name": "Google Inc.",
                "symbol": "GOOGL.BA",
                "type": "S",
                "typeDisp": "Equity"
            },
            {
                "exch": "FRA",
                "exchDisp": "Frankfurt",
                "name": "GOOGLE-A",
                "symbol": "GGQ1.F",
                "type": "S",
                "typeDisp": "Equity"
            },
            {
                "exch": "MUN",
                "exchDisp": "Munich",
                "name": "GOOGLE-A",
                "symbol": "GGQ1.MU",
                "type": "S",
                "typeDisp": "Equity"
            },
            {
                "exch": "EBS",
                "exchDisp": "Swiss",
                "name": "GOOGLE-A",
                "symbol": "GOOGL.SW",
                "type": "S",
                "typeDisp": "Equity"
            },
            {
                "exch": "MUN",
                "exchDisp": "Munich",
                "name": "GOOGLE-C",
                "symbol": "GGQ7.MU",
                "type": "S",
                "typeDisp": "Equity"
            }
        ]
    }
}

```
