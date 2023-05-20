"""
 Some os números de 1 a 100 e imprima o valor
"""
#criando a variavel que vai receber a soma dos numeros

lista = []
num = 0
for cont in range(0,100):
    num += cont
    lista.append(cont)
    print(num)
print(lista)
print(sum(lista))