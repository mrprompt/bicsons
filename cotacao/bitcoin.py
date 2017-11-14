from requests import get
import json

"""
Recupera a cotação para a Foxbit
"""
def load(exchange):
    response = get('https://api.bitvalor.com/v1/ticker.json')
    result = json.loads(response.text)

    return json.dumps(result['ticker_1h']['exchanges'][exchange])