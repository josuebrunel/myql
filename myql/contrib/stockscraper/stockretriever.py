"""This module isn't mine, it's at 99% inspired from https://github.com/gurch101/StockScraper written by Gurchet Rai.
So all rigts reserved to Gurchet Rai.
Documentation http://www.gurchet-rai.net/dev/yahoo-finance-yql
"""

import pdb
from myql.myql import MYQL

def get_current_info(symbolList, columns=None, format='json'):
    """get_current_info() uses the yahoo.finance.quotes datatable to get all of the stock information presented in the main table on a typical stock page 
    and a bunch of data from the key statistics page.
    """
    yql = MYQL(format=format, community=True)
    response = yql.select('yahoo.finance.quotes',columns).where(['symbol','in',symbolList])
    return response

def get_news_feed(symbol,format='json'):
    """get_news_feed() uses the rss data table to get rss feeds under the Headlines and Financial Blogs headings on a typical stock page.
    """
    yql = MYQL(format=format, community=True)
    rss_url='http://finance.yahoo.com/rss/headline?s={0}'.format(symbol)
    response = yql.select('rss',['title','link','description'],limit=2).where(['url','=',rss_url])
    return response

def get_historical_info(symbol,limit=5, format='json'):
    """get_historical_info() uses the csv datatable to retrieve all available historical data on a typical historical prices page
    """
    yql = MYQL(format=format)
    historical_url = 'http://ichart.finance.yahoo.com/table.csv?s={0}'.format(symbol)
    response = yql.select('csv',limit=limit).where(['url','=',historical_url],['columns','=','Date,Open,High,Low,Close,Volume,AdjClose'])
    return response

def get_options_info(symbol, items=[], expiration='', format=format):
    """get_options_data() uses the yahoo.finance.options table to retrieve call and put options from the options page.
    """
    yql = MYQL(format=format,community=True)
    response = yql.select('yahoo.finance.options',items).where(['symbol','=',symbol],[] if not expiration else ['expiration','=',expiration])
    return response

def get_index_summary(symbol, items=[],format='json'):
    """
    """
    yql = MYQL(format=format, community=True)
    response = yql.select('yahoo.finance.quoteslist',items).where(['symbol','=',symbol])
    return response
