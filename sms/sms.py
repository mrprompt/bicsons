"""
Envio de SMS
"""
from random import randint
from datetime import datetime
from .driver import nexmo, totalvoice

def sms(numeros, mensagem):
    """
    Envia o sms com o driver escolhido aleatoriamente
    """
    for numero in numeros:
        now = datetime.now().strftime("%H:%M")

        if now in numero['horarios']:
            driver = randint(1, 2)

            if driver == 1:
                result = totalvoice.send(numero['telefone'], mensagem)
            elif driver == 2:
                result = nexmo.send(numero['telefone'], mensagem)
            else:
                result = {'sucesso' : False}

            print("Envio para " + numero['telefone'] + " : " + str(result['sucesso']))
