"""
Cotação dos Bitcoins da Foxbit
"""
from json import loads, dumps
from requests import get

def load(exchange):
    """
    Recupera a cotação para a Foxbit
    """
    response = get('https://api.bitvalor.com/v1/ticker.json')
    result = loads(response.text)

    return dumps(result['ticker_1h']['exchanges'][exchange])
