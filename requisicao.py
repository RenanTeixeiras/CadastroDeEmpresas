import requests
import json


def consulta_cnpj(cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    querystring = {'token':'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX','cnpj':'06990590000123','plugin':'RF'}
    response = requests.request('GET', url, params=querystring)

    resp = json.loads(response.text)
    listaChaves = ['nome', 'logradouro','numero','complemento','bairro','municipio','uf','cep','telefone','email']
    listaValores = []
    for chave in listaChaves:
        listaValores.append(resp[chave])
    return listaValores

# numero = consulta_cnpj(cnpj)['numero']
# bairro = consulta_cnpj(cnpj)['bairro']
# municipio = consulta_cnpj(cnpj)['municipio']
# uf = consulta_cnpj(cnpj)['uf']
# cep = consulta_cnpj(cnpj)['cep']
# telefone = consulta_cnpj(cnpj)['telefone']
# email = consulta_cnpj(cnpj)['email']