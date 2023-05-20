"""
Set Comprehension

Lista = [1,2,3,4,5,6]
Set = {1,2,3,4,5,6}
"""

#Exemplo
numeros = {num for num in range(1,7)}
print(numeros)

#outro exemplo
numeros2 = {x ** 2 for x in range(10)}
print(numeros2)

Dicionario = {x : x ** 2 for x in range(1,len(numeros))}
print(Dicionario)

# com letras
letras = {letra for letra in 'Geek University'}
print(letras)