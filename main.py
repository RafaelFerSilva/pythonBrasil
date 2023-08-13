from acesso_cep import BuscaEndereco
import requests

cep = 13803096
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro)

