"""
. Faça um algoritmo que imprima os múltiplos positivos de 7, inferiores a 1000.
"""

for contadora in range(0,1000):
    if contadora % 7 == 0:
        print(f"{contadora} é multiplo de 7")

#colocando em uma lista
multiplo_sete = []
for contadora in range(0,1000):
    if contadora % 7 == 0:
        multiplo_sete.append(contadora)
print(multiplo_sete)