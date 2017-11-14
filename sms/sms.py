import random
from .driver import nexmo, totalvoice

"""
Envia o sms com o driver escolhido aleatoriamente
"""
def sms(numeros, mensagem):
    for numero in numeros:
        driver = random.randint(1, 2)
        
        if driver == 1:
            result = totalvoice.send(numero, mensagem)
        elif driver == 2:
            result = nexmo.send(numero, mensagem)
        else:
            result = { 'sucesso' : False }

        print("Envio para " + numero + " : " + str(result['sucesso']))