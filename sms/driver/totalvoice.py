"""
Envio de SMS via TotalVoice
"""
import os
from json import loads
from totalvoice.cliente import Cliente

def send(numero, mensagem):
    """
    Envia o sms via TotalVoice
    """
    key = os.environ.get("TOTALVOICE_API_KEY")
    url = 'api.totalvoice.com.br'
    cliente = Cliente(key, url)
    response = cliente.sms.enviar(numero, mensagem)

    return loads(response.decode())
