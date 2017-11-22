"""
Cotação dos Bitcoins
"""
from json import loads, dumps
from requests import get

def load():
    """
    Recupera a cotação das exchanges
    """
    response = get('https://api.bitvalor.com/v1/ticker.json')
    result = loads(response.text)

    return result['ticker_1h']['exchanges']
