"""
Envio de SMS
"""
from random import randint
from datetime import datetime
from .driver import nexmo, totalvoice

def sms(numeros, exchange, mensagem):
    """
    Envia o sms com o driver escolhido aleatoriamente
    """
    for numero in numeros:
        now = datetime.now().strftime("%H:%M")

        if now in numero['horarios'] and exchange in numero['exchanges']:
            driver = randint(1, 2)
            newmessage = exchange + ": " + mensagem

            if driver == 1:
                result = totalvoice.send(numero['telefone'], newmessage)
            elif driver == 2:
                result = nexmo.send(numero['telefone'], newmessage)
            else:
                result = {'sucesso' : False}

            print("Envio para " + numero['telefone'] + " : " + str(result['sucesso']))
