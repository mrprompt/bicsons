"""
Envio de SMS
"""
from random import randint
from .driver import nexmo, totalvoice

def sms(numeros, mensagem):
    """
    Envia o sms com o driver escolhido aleatoriamente
    """
    for numero in numeros:
        driver = randint(1, 2)

        if driver == 1:
            result = totalvoice.send(numero, mensagem)
        elif driver == 2:
            result = nexmo.send(numero, mensagem)
        else:
            result = {'sucesso' : False}

        print("Envio para " + numero + " : " + str(result['sucesso']))
