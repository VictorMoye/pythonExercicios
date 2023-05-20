"""
num1 = int(input("Infome um numero: "))
num3 = int(input("Infome um numero: "))
num2 = int(input("Infome um numero: "))

lista = [num1,num2,num3]
print(f' {sorted(lista)}')
"""


# recenbendo varios numeros e ordenando eles

contador = int(input("Informe quantos numeros quer colocar: "))
lista2 = [0,1]
print(lista2)
for cont in range(1,contador):
    import random
    aux = random.randint(1,100)
    lista2.append(aux)
print(lista2)