"""
Construa um Algoritmo que, para um grupo de 50 valores inteiros, determine:
a) A soma dos números positivos;
b) A quantidade de valores negativos;

"""
#importando uma biblioteca para gerar numeros aleatorios
import random

#criando as variaveis contadoras
contadora_Negativo = contadora_Positiva = contadora_neutro = 0
for contadora in range(0,50):
    auxiliar = random.randint(-10,10)
    if(auxiliar < 0):
        contadora_Negativo += 1
    elif(auxiliar >0):
        contadora_Positiva += 1
    else:
        contadora_neutro += 1
print(f"O numero de positivos foi {contadora_Positiva}")
print(f"O numero de positivos foi {contadora_Negativo}")
print(f"Contadora neutro: {contadora_neutro}")

# fazendo com listas
import random
lista = []
lista_positiva = []
lista_negativa = []

for cont in range(1,10):
    auxiliar = random.randint(-10,10)
    lista.append(auxiliar)
    if(auxiliar <= 0):
        lista_negativa.append(auxiliar)
    elif(auxiliar >= 0):
        lista_positiva.append(auxiliar)
    else:
        print()

print(f"Lista completa: {lista}")
print(f"lista positiva: {lista_positiva}")
print(f"lista negativa: {lista_negativa}")
