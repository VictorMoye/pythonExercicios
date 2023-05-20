"""
Loop while
while expressãop booleana
    // execução do loop
será repetido enquanto a expressão for verdadeira


num = 1
#enquanto for falso ira executar
while num < 10:
    print(num)
    #Importante em um loop while cuidarmos do criterio de parada
    num = num + 1
# outro caso
resposta = ''
while resposta != 'sim':
    print('digite sim pra sair')
    resposta = input('Já acabou Jessica ? ')
"""
i = 1
while i <= 10:
    print(i)
    i = i +1

inicio = final = i = 0

inicio = int(input("Digite um numero inicial: "))
final = int(input("Digite um numero final: "))

for i in final:
    print(i)
    i  = i+ 1
    print(i)

