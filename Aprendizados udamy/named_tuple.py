"""
Módulo Colletions - Named Tuple

# recap tupla
tupla = (1,2,3)

Named Tupla -> são tuplas diferenciadaas onde especificamos um nome para a mesma e parametros

"""

# import
from collections import namedtuple

# percisamos definir o nome e parametro

# forma 1 declaração named tuple
cachorro = namedtuple('cahorro', 'idade raca nome')

# forma 2 declaração named tuple

cachorro = namedtuple('cahorro','idade, raca, nome')

# foma 3 declaração named tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# usando

ray = cachorro(idade=2, raca='chow chow', nome='ray')
print(ray)
#Acesando dados
#Forma 1
print(ray[0]) #idade
print(ray[1])#raça
print(ray[2])#nome

#forma 2

print(ray.nome)
print(ray.idade)
print(ray.idade)

print(ray.index('chow chow'))# retorna o numero do indice
print(ray.count('chow chow'))# retorna quantas vezes foi chow chow foi visto ou existe
