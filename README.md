# Bicsons

Cotação dos Bitcoins por SMS

## ATENÇÃO

Este projeto foi criado para fins pessoais e didáticos apenas, **sem garantias**  e distribuído **como está**, use por sua própria conta e risco.

## Instalação

** Necessário Python 3 **

```
pip install < requirements.txt
``` 

Crie um arquivo _.env_ na raiz do projeto e com seguintes campos:

```
API_KEY=<TOTALVOICE-API-KEY>
NUMEROS="DDD+NUMERO"
```

* A api key, você pode conseguir [aqui](http://www.totalvoice.com.br/).
* Os números devem seguir o formato DDD+NÚMERO, você pode inserir quantos números quiser, basta separá-los por vírgula. Mais detalhes, consulte a [documentação da API](https://api.totalvoice.com.br/doc/) da [TotalVoice](http://www.totalvoice.com.br/).

## Uso

```
python script.py
```

## Licença

MIT