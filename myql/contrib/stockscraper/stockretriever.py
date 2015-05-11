import pdb
from myql.myql import MYQL

def get_current_info(symbolList, columns=None, format='json'):
    """
    """
    yql = MYQL(format=format, community=True)
    response = yql.select('yahoo.finance.quotes',columns).where(['symbol','in',symbolList])
    return response
