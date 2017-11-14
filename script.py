#/usr/bin/env python3.6
# -*- utf-8 -*-
from totalvoice.cliente import Cliente
from requests import get
from dotenv import load_dotenv, find_dotenv
import json
import os

load_dotenv(find_dotenv(), override=True)

def bicsons():
    response = get('https://api.bitvalor.com/v1/ticker.json')
    result = json.loads(response.tecp ..xt)

    return json.dumps(result['ticker_1h']['exchanges']['FOX'])

def sms(mensagem):
    cliente = Cliente(os.environ.get("API_KEY"), 'api.totalvoice.com.br')
    numeros = os.environ.get("NUMEROS").split(",")
    envios = 0;

    for numero_destino in numeros:
        response = cliente.sms.enviar(numero_destino, mensagem)
        result = json.loads(response.decode())

        print("Envio para " + numero_destino + " : " + str(result['sucesso']))

        if result['sucesso']:
            envios += 1
    
    return envios

def main():
    sms(bicsons())

main()