"""
Envia SMS da cotação do Bitcoin pela FoxBit
"""
import os
from dotenv import load_dotenv, find_dotenv
from cotacao import bitcoin
from sms import sms

load_dotenv(find_dotenv(), override=True)

def main():
    """
    Função principal
    """
    numeros = os.environ.get("NUMEROS").split(",")

    sms.sms(numeros, bitcoin.load('FOX'))

main()
