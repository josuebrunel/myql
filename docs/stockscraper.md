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
from myql.contrib.stockscraper import StockRetriever
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

#### *StockRetriever.get_historical_info(symbol)*

* ***symbol*** : Symbol news to retrieve

```python
from myql.contrib.stockscraper import StockRetriever
stocks = StockRetriever(format='json')
data = stocks.get_historical_info('YHOO')
```

```json

    "query": {
        "count": 5,
        "created": "2015-05-20T13:07:29Z",
        "lang": "en-US",
        "results": {
            "row": [
                {
                    "AdjClose": "Adj Close",
                    "Close": "Close",
                    "Date": "Date",
                    "High": "High",
                    "Low": "Low",
                    "Open": "Open",
                    "Volume": "Volume"
                },
                {
                    "AdjClose": "40.98",
                    "Close": "40.98",
                    "Date": "2015-05-19",
                    "High": "44.66",
                    "Low": "39.12",
                    "Open": "44.38",
                    "Volume": "41283000"
                },
                {
                    "AdjClose": "44.36",
                    "Close": "44.36",
                    "Date": "2015-05-18",
                    "High": "44.57",
                    "Low": "44.04",
                    "Open": "44.52",
                    "Volume": "8278800"
                },
                {
                    "AdjClose": "44.75",
                    "Close": "44.75",
                    "Date": "2015-05-15",
                    "High": "45.07",
                    "Low": "44.69",
                    "Open": "45.00",
                    "Volume": "7751900"
                },
                {
                    "AdjClose": "44.95",
                    "Close": "44.95",
                    "Date": "2015-05-14",
                    "High": "44.99",
                    "Low": "44.45",
                    "Open": "44.53",
                    "Volume": "10098100"
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
from myql.contrib.stockscraper import StockRetriever
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
from myql.contrib.stockscraper import StockRetriever
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
from myql.contrib.stockscraper import StockRetriever
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

