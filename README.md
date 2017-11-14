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
NUMEROS="DDDNUMERO,DDDNUMERO,DDDNUMERO,DDDNUMERO"
```

* A api key da TotalVoice, você pode conseguir [aqui](http://www.totalvoice.com.br/).
* A api key da Nexmo, você pode conseguir [aqui](https://www.nexmo.com/products/sms).
* Os números devem seguir o formato DDDNÚMERO, você pode inserir quantos números quiser, basta separá-los por vírgula.

## Uso

```console
python script.py
```

## Exemplo de crontab

```console
0 8,11,15,18,21 * * * echo 'cd /srv/app/bicsons; source venv/bin/activate; python script.py; deactivate' | /bin/bash >/dev/null 2>&1
```

## Licença

MIT