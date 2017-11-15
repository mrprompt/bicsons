"""
Envio de SMS via Nexmo
"""
import nexmo

def send(numero, mensagem):
    """
    Envia o sms via Nexmo
    """
    cliente = nexmo.Client()
    payload = {'from': 'Bicsons', 'to': '55' + numero, 'text': mensagem}
    response = cliente.send_message(payload)

    return {'sucesso': bool(response['messages'][0]['status'])}
