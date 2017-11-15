"""
Envia SMS da cotação do Bitcoin pela FoxBit
"""
import json
from dotenv import load_dotenv, find_dotenv
from cotacao import bitcoin
from sms import sms

load_dotenv(find_dotenv(), override=True)

def main():
    """
    Função principal
    """
    numeros = json.load(open("numeros.json"))

    sms.sms(numeros, bitcoin.load('FOX'))

main()
