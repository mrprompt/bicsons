# Bicsons

Cotação dos Bitcoins por SMS

## ATENÇÃO

Este projeto foi criado para fins pessoais e didáticos apenas, **sem garantias**  e distribuído **como está**, use por sua própria conta e risco.

## Instalação

```console
pip install -r requirements.txt
```

Crie um arquivo _.env_ na raiz do projeto e com seguintes campos:

```console
TOTALVOICE_API_KEY=<TOTALVOICE-API-KEY-VALUE>
NEXMO_API_KEY=<NEXMO-API-KEY-VALUE>
NEXMO_API_SECRET=<NEXMO-API-SECRET-VALUE>
```

Crie um arquivo _numeros.json_ na raiz do projeto com a seguinte estrutura:

```json
[
    {
        "nome": "Thiago",
        "telefone": "48123456789",
        "horarios": ["09:00", "11:00", "15:00", "18:00", "21:00"]
    }
]
```

* A api key da TotalVoice, você pode conseguir [aqui](http://www.totalvoice.com.br/).
* A api key da Nexmo, você pode conseguir [aqui](https://www.nexmo.com/products/sms).
* Os números devem seguir o formato DDDNÚMERO, você pode inserir quantos números quiser.
* Os horários devem seguir o formato HH:MM.

## Uso

```console
python script.py
```

## Exemplo de crontab

```console
* 8-21 * * * echo 'cd /srv/app/bicsons; source venv/bin/activate; python script.py; deactivate' | /bin/bash >/dev/null 2>&1
```

## Licença

MIT