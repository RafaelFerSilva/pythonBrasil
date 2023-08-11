import re
from TelefonesBr import TelefonesBR

# padrao = "[0-9][a-z]{2}[0-9]"
# texto = "123 1ac2 1cc aa1"
# resposta = re.search(padrao, texto)
# print(resposta.group())

# padrao = "\w{5,50}@[a-z]{3,10}.com.br"
# texto = "aaabbbccc rafael123@gmail.com.br dfsdfdfsd dfsdfsdfsd"
# resposta = re.search(padrao, texto)
# print(resposta.group())

# padrao_model = "(xx)aaaa-wwww"
# padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
# texto = "eu gosto do número 2126451234 e gosto também do 19999980631"
# resposta = re.findall(padrao, texto)
# print(resposta)

telefone = "551999980631"

telefone_objeto = TelefonesBR(telefone)
print(telefone_objeto)

# padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# resposta = re.search(padrao, telefone)
# print(resposta.group())
