import os
from dotenv import load_dotenv, find_dotenv
from cotacao import bitcoin
from sms import sms

load_dotenv(find_dotenv(), override=True)

"""
Função principal
"""
def main():
    numeros = os.environ.get("NUMEROS").split(",")
    
    sms.sms(numeros, bitcoin.load('FOX'))

main()