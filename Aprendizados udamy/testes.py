# Imprimi todos os numeros naturais de 0 a N em ordem crescente e decrescente

num = int(input('Escolha um numero: '))
qtd = num

# ordem crescente
for cont in range(0,qtd):
            print(cont)
            cont += 1
#ordem decrescente
for num in range(num,0, -1):
            print(num)
            num -= 1




"""
12- Fac¸a um programa que receba dois numeros. Calcule e mostre:" +
                                    "• a soma dos numeros pares desse intervalo de n ´ umeros, incluindo os n ´ umeros digi - ´tados;" +
                                    "• a multiplicac¸ao dos n ˜ umeros ´ ´ımpares desse intervalo, incluindo os digitados

idade = int(input("informe a idade"))
if idade >= 61:
    print("velha idade ")
elif (idade >= 18 and idade <= 60):
    print("nova idade")
else:
    print("menor idade ")

#num2 = int(input('Informe um numero -> '))
resp = ''
while resp != 'S':
    num1 = int(input('Informe um numero -> '))
    num2 = int(input('Informe um numero -> '))
    aux = 0
    mult = 1
    if num2 > num1 or num1 == num2:
        print(f'Invalido {num2} é maior ou igual a {num1} por tando a esposta é zero !!')
    else:
        while(num1 <= num2):
            if (num1 % 2 == 0):
                aux += num1
            if (num1 % 2 == 1):
                mult *= num1
            num1 += 1
        print(f'aux {aux} -> mult {mult}')
    resp = input('\nVoce quer sair do programa [S/N]? ').upper()


#Calcular o numero  H = 1+1/2!+1/3!+1/4!+1...N+1
    print('Primeiro calculando o fatorial ')
    num2 = int(input('Informe um numero -> '))
    mult = 1
    while num2 >= 1:
        mult *= num2
        num2 -=1
    print(mult)
    # irei transforma em uma função a parte de cima e embaixo irei usar o Lambda
    # aqui preciso fazer a junção da conta
    aux = 1
    soma = 0
    while aux:
        aux = int(input('Informe um numero -> '))
        if aux:
            i = 1
            while i < aux:
                soma += 1 / i
                i += 1
            print(f'O resultado da serie é {round(soma, 2)}')
        else:
            print('Entrada terminada pelo usuario')
"""