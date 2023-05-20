"""
Módulo Colletions - Default Dict
#recap dicionarios
Ao criar um dicionairo ultilizando um valor default
podemos ultilizar um lambda para isso este valor sera ultilizado
sempre que não houver um valor definido caso tetemos acessar uma chave que
não existe essa chave será criadad e  o valor default sera atribuido


#diferenças
dicionario = {'curso': 'programação em python'}
print(dicionario)
print(dicionario['curso'])
# print(dicionario['outro']) keyErro

OBS: Lambdas são funçes se mnome que podem ou nao receber parametros de entrada
e retorna valores

"""

# fazendo a importação
from _collections import defaultdict
dicionario = defaultdict(lambda :0)

print(dicionario)

dicionario['curso'] = 'programação essencial'
print(dicionario)

print(dicionario['ooutro'])