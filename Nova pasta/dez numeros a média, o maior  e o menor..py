"""
Crie um programa que peça 10 números inteiros e apresente: a média, o maior
e o menor.
"""
import random
import statistics
media = 0
maior =  aux =0

menor = 100
lista = []
for contadora in range(0,10):
    aux = int(random.randint(1,10))
    media += aux
    lista.append(aux)
    if(aux > maior):
        maior = aux
    if (aux < menor ):
        menor = aux

print(f"A media é {round((media / contadora),2)}")
print(f"O maior número foi: {maior}")
print(f"O menor numero foi: {menor}")
print(lista)

# fazendo om listas
for contadora in range(0,10):
    lista.append(random.randint(1,10))
print(f"Media: { round(sum(lista)/len(lista),2)}")
print(f"Maior numero: {max(lista)}")
print(f"Menor numero: {min(lista)}")
print(f"Linsta: \n {lista}")