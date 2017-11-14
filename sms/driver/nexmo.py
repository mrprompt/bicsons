import nexmo

"""
Envia o sms via Nexmo
"""
def send(numero, mensagem):
    cliente = nexmo.Client()
    payload = { 'from': 'Bicsons', 'to': '55' + numero, 'text': mensagem }
    response = cliente.send_message(payload)

    return { 'sucesso': bool(response['messages'][0]['status']) }