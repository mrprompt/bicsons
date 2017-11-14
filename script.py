# -*- utf-8 -*-
from totalvoice.cliente import Cliente
from requests import get
from dotenv import load_dotenv, find_dotenv
import json
import os
import nexmo
import random

load_dotenv(find_dotenv(), override=True)

numeros = os.environ.get("NUMEROS").split(",")

"""
Recupera a cotação para a Foxbit
"""
def bicsons():
    response = get('https://api.bitvalor.com/v1/ticker.json')
    result = json.loads(response.text)

    return json.dumps(result['ticker_1h']['exchanges']['FOX'])

"""
Envia o sms via TotalVoice
"""
def sms_totalvoice(numero, mensagem):
    cliente = Cliente(os.environ.get("TOTALVOICE_API_KEY"), 'api.totalvoice.com.br')
    response = cliente.sms.enviar(numero, mensagem)
    result = json.loads(response.decode())    

    return result

"""
Envia o sms via Nexmo
"""
def sms_nexmo(numero, mensagem):
    cliente = nexmo.Client()
    response = cliente.send_message({ 'from': 'Bicsons', 'to': '55' + numero, 'text': mensagem })

    return { 'sucesso': bool(response['messages'][0]['status']) }

"""
Envia o sms com o driver escolhido aleatoriamente
"""
def sms(mensagem):
    for numero in numeros:
        driver = random.randint(1, 2)
        
        if driver == 1:
            result = sms_totalvoice(numero, mensagem)
        elif driver == 2:
            result = sms_nexmo(numero, mensagem)
        else:
            result = { 'sucesso' : False }

        print("Envio para " + numero + " : " + str(result['sucesso']))

"""
Função principal
"""
def main():
    sms(bicsons())

main()