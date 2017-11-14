from totalvoice.cliente import Cliente
import json
import os

"""
Envia o sms via TotalVoice
"""
def send(numero, mensagem):
    key = os.environ.get("TOTALVOICE_API_KEY")
    url = 'api.totalvoice.com.br'
    cliente = Cliente(key, url)
    response = cliente.sms.enviar(numero, mensagem)
    result = json.loads(response.decode())    

    return result