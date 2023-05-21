"""
Any All

all()-> Te retorna verdadeiro se todos os elementos do interavel são verdadeiros
"""
print(all([0,1,2,3,4])) # False por conta do 0 zero
print(all([1,2,3,4])) # Lista começando com 1 True
print(all([])) # lista vazia True
print(all(["Instringue de qualquer coisa"])) # False
print(all((1,2,3,4))) # Set True
print(all({1,2,3,4})) # Dicionario True

nomes = ['carlos', 'Camila', 'Carla']
print(all(nome[0] == 'c' for nome in nomes)) # falce pois reconhe os nomes maiusculos e minusculos
print(all(nome[0] == 'c' or 'C' for nome in nomes)) # retorna verdadeiro pois todos os nomes começa com C OU c

print(all([letra for letra in 'eio' if letra in 'eiouf']))

print(all([num for num in [1,2,3,4] if num %2 == 0]))

print('---------------Ultilizando ANY AGORA -------------------')
 # ANY()-> RETORNA True se qualquer elemento do interavel for verdadeiro so retorna false se todos forem false quase um OU
print(any([0,1,2,3,4])) # True por conta do 0 zero
print(any([1,2,3,4])) # Lista começando com 1 True
print(any([])) # lista vazia False
print(any(["Instringue de qualquer coisa"])) # True
print(any((1,2,3,4))) # Set True
print(any({1,2,3,4})) # Dicionario True

nomes = ['carlos', 'Camila', 'Carla','vitoria']
print(any(nome[0] == 'c' for nome in nomes)) # True
print(any(nome[0] == 'c' or 'C' for nome in nomes)) # retorna verdadeiro possuem todos os nomes  C OU c

print(all([letra for letra in 'eio' if letra in 'eiouf']))

print(all([num for num in [1,2,3,4] if num %2 == 0]))