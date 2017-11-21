"""
Envia SMS da cotação do Bitcoin pela FoxBit
"""
import json
import time
from dotenv import load_dotenv, find_dotenv
from cotacao import bitcoin
from sms import sms
from daemons import daemonizer

load_dotenv(find_dotenv(), override=True)

@daemonizer.run(pidfile="/tmp/bicsons.pid")
def main():
    """
    Função principal
    """
    while True:
        numeros = json.load(open("numeros.json"))

        sms.sms(numeros, bitcoin.load('FOX'))

        time.sleep(60)

if __name__ == "__main__":
    main()
