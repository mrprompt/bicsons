"""
Envia SMS da cotação do Bitcoin pela FoxBit
"""
import json
import time
import os
from dotenv import load_dotenv, find_dotenv
from cotacao import bitcoin
from sms import sms
from daemons import daemonizer
from os.path import abspath, exists

load_dotenv(find_dotenv(), override=True)

@daemonizer.run(pidfile="/tmp/bicsons.pid")
def main():
    """
    Função principal
    """
    while True:
        base  = os.path.dirname(os.path.realpath(__file__))
        numeros = json.load(open(base + "/numeros.json"))

        sms.sms(numeros, bitcoin.load('FOX'))

        time.sleep(60)

if __name__ == "__main__":
    main()
