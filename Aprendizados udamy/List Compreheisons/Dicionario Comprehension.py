"""
Dicionario Comprehension

Pense no seguinte
 Se quiser crair uma lista ou uma tupla basta fazer

 Lista = [1,2,2]
 Tupla = (1,2,3)
 Conjunto = {1,2,3}
 Dicionario = {'a' : 1, 'b':2 , "c":3}
# para pular de tupla to dicionario to conjunto é so mudar do () to {} ou []
e por isso a sintaxe é a mesma para poder usar o Compreehesion basta fazer a mesma coisa
#sintaxy
{chave : valor for valor in interavel}
"""

#Exemplos
numeros = {'a' : 1, 'b':2 , "c":3, 'D' : 5}#Pode ser feito isso com uma tupla conjuto ou lista
print(numeros)
                    #ta multiplicando apenas a chave okay
quadrado = {chave : valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

chaves = 'abcde'
valores = [1,2,3,4,5]

mistura = {chaves[cont] : valores[cont] for cont in range(0,len(chaves))}
print(mistura)

num = [1,2,3,4,5]
res = {num : ('Numero Par' if num % 2 == 0 else "Não Par ")}