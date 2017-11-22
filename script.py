"""
Envia SMS da cotação do Bitcoin pela FoxBit
"""
import time
import sys
from json import load, loads, dumps
from dotenv import load_dotenv, find_dotenv
from cotacao import bitcoin
from sms import sms

load_dotenv(find_dotenv(), override=True)

def main(agenda):
    numeros = load(open(agenda))
    
    """
    Função principal
    """
    while True:
        exchanges = bitcoin.load()

        for exchange in exchanges:
            sms.sms(numeros, exchange, dumps(exchanges[exchange]))
            
        time.sleep(60)

if __name__ == "__main__":
    numeros = sys.argv[1]

    main(numeros)
