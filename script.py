"""
Envia SMS da cotação do Bitcoin pela FoxBit
"""
import json
import time
import sys
from dotenv import load_dotenv, find_dotenv
from cotacao import bitcoin
from sms import sms
from daemons import daemonizer

load_dotenv(find_dotenv(), override=True)

@daemonizer.run(pidfile="/tmp/bicsons.pid")
def main(agenda, exchange="FOX"):
    """
    Função principal
    """
    while True:
        numeros = json.load(open(agenda))

        sms.sms(numeros, bitcoin.load(exchange))

        time.sleep(60)

if __name__ == "__main__":
    numeros = sys.argv[1]
    exchange = sys.argv[2]
    
    main(numeros, exchange)
