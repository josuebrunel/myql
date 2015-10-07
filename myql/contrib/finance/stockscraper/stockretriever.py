"""This module isn't mine, it's at 99% inspired from https://github.com/gurch101/StockScraper written by Gurchet Rai.
So all rigts reserved to Gurchet Rai.
Documentation http://www.gurchet-rai.net/dev/yahoo-finance-yql
"""

from __future__ import absolute_import

import re
import json
from datetime import date, timedelta

import requests

from myql.myql import YQL

class StockRetriever(YQL):

    def __init__(self, format='json', debug=False, oauth=None):
        """Initialize the object
        """
        super(StockRetriever, self).__init__(community=True, format=format, debug=debug, oauth=oauth)
    
    def __get_time_range(self, startDate, endDate):
        """Return time range
        """
        today = date.today()
        start_date = today - timedelta(days=today.weekday(), weeks=1)
        end_date = start_date + timedelta(days=4)

        startDate = startDate if startDate else str(start_date)
        endDate = endDate if endDate else str(end_date)
        
        return startDate, endDate

    def get_current_info(self, symbolList, columns=None):
        """get_current_info() uses the yahoo.finance.quotes datatable to get all of the stock information presented in the main table on a typical stock page 
        and a bunch of data from the key statistics page.
        """
        response = self.select('yahoo.finance.quotes',columns).where(['symbol','in',symbolList])
        return response

    def get_news_feed(self, symbol):
        """get_news_feed() uses the rss data table to get rss feeds under the Headlines and Financial Blogs headings on a typical stock page.
        """
        rss_url='http://finance.yahoo.com/rss/headline?s={0}'.format(symbol)
        response = self.select('rss',['title','link','description'],limit=2).where(['url','=',rss_url])
        return response

    def get_historical_info(self, symbol,items=None, startDate=None, endDate=None, limit=None):
        """get_historical_info() uses the csv datatable to retrieve all available historical data on a typical historical prices page
        """
        startDate, endDate = self.__get_time_range(startDate, endDate)
        response = self.select('yahoo.finance.historicaldata',items,limit).where(['symbol','=',symbol],['startDate','=',startDate],['endDate','=',endDate])
        return response

    def get_options_info(self, symbol, items=None, expiration=''):
        """get_options_data() uses the yahoo.finance.options table to retrieve call and put options from the options page.
        """
        response = self.select('yahoo.finance.options',items).where(['symbol','=',symbol],[] if not expiration else ['expiration','=',expiration])
        return response

    def get_index_summary(self, symbol, items=None):
        """
        """
        response = self.select('yahoo.finance.quoteslist',items).where(['symbol','=',symbol])
        return response

    def get_industry_index(self, index_id,items=None):
        """retrieves all symbols that belong to an industry.
        """
        response = self.select('yahoo.finance.industry',items).where(['id','=',index_id])
        return response

    def get_xchange_rate(self, pairs, items=None):
        """Retrieves currency exchange rate data for given pair(s). 
        Accepts both where pair='eurusd, gbpusd' and where pair in ('eurusd', 'gpbusd, usdaud')
        """
        response = self.select('yahoo.finance.xchange', items).where(['pair', 'in', pairs])
        return response

    def get_dividendhistory(self, symbol, startDate, endDate, items=None):
        """Retrieves divident history
        """
        startDate, endDate = self.__get_time_range(startDate, endDate)
        response = self.select('yahoo.finance.dividendhistory', items).where(['symbol', '=', symbol], ['startDate', '=', startDate], ['endDate', '=', endDate])
        return response

    def get_balancesheet(self, symbol):
        """Retrieves balance sheet
        """
        response = self.select('yahoo.finance.balancesheet').where(['symbol', '=', symbol])
        return response

    def get_symbols(self, name):
        """Retrieves all symbols belonging to a company
        """
        url = "http://autoc.finance.yahoo.com/autoc?query={0}&callback=YAHOO.Finance.SymbolSuggest.ssCallback".format(name)

        response = requests.get(url)

        json_data = re.match("YAHOO\.Finance\.SymbolSuggest.ssCallback\((.*)\)", response.text)
        try:
            json_data = json_data.groups()[0]
        except (Exception,) as e:
            print(e)
            json_data = '{"results": "Webservice seems to be down"}'

        return type('response', (requests.Response,),{
            'text' : json_data,
            'content': json_data.encode(),
            'status_code': response.status_code,
            'reason': response.reason,
            'encoding': response.encoding,
            'apparent_encoding': response.apparent_encoding,
            'cookies': response.cookies,
            'headers': response.headers,
            'json': lambda : json.loads(json_data),
            'url': response.url
        })
