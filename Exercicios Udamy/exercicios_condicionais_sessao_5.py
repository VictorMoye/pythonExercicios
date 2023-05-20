from cmath import log
import math
print('Seja bem vindo aos exercicios da sessão 5')

resp = ''
while resp != 's':
    print('Escolha com os numeros qual deles voce quer ver')
    print('1-Mostrando o maior numero entre eles')
    print('2-se for positivo informa a raiz quadrada e se for negativo dizer que é invalido')
    print('3-Receba a altura e o sexo da pessoa e calcule o peso ideal dela formula homens = (72.7 * h) - 58 mulheres = (62.1 * h) - 44, 7 h == altura')
    print('4-Faça o numero ser somado pelos seus logaritimos e caso seja menor que 0 seja invalido ex: 852,8+5+2')
    print('5- Escolha um numero se for positivo calcule o logaritmo desse numero caso seja negativo escreva invalido')
    escolha = int(input("Qual exercicio voce quer fazer: "))

    if escolha ==1:
        num1 = int(input('Informe um numero: '))
        num2 = int(input('Informe um segundo numero: '))
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        else:
            print(f'{num2} é maior que {num1}')

    elif escolha == 2:
        num1 = int(input('Informe um numero: '))

        if num1 >= 1:
            print(f'Número é {num1} e a raiz quadrada dele é {num1 * num1}')

        else:
            print(f'Número é {num1} negativo e invalido')

    elif escolha == 3:
        peso = float(input('Digite o peso da pessoa: '))
        altura = float(input('Digite a altura da pessoa: '))
        print('\nFAVOR RESPONDER APENAS COM [H/M]')
        sexo = input(' \nDetermine o sexo da pessoa: [H = HOMENS / M = MULHERES]')
        if sexo == 'm':
            mulher = (62.1 * altura) - 44.7
            nome = input("Digite o nome da mulher: ")
            print(f'O peso ideal da {nome} \nÉ {mulher} \nporém hoje é {peso}')
        elif sexo == 'H' or 'h':
            homem = (72.7 * altura) - 58
            nome = input("Digite o nome do homem: ")
        print(f'O peso idela de {nome} \nÉ {homem} \nporém hoje é {peso}')

    elif escolha == 4:
        numero = int(input('Digite seu numero: '))
        soma = 0
        if numero > 0:
            while numero > 0:
                soma+= int(numero % 10)
                numero /= 10
            print(f'A soma dos algarismos do numero {numero} é {soma}')
        else:
            print('Número menor que 0')

    elif escolha == 5:

        questao_5 = int(input('Informe um numero: '))
        x = int(input('Informe o valor da base desejada: '))
        if questao_5 < 0:
            print(f'O nmero {questao_5} é menor que 0 por tanto ele é invalido')
        else:
            log2 = math.log(questao_5, 2.0)
            print(f'Log({questao_5}) na base ^ {x} é {log2}')
            log3 = math.log(questao_5)
            print(log3)

    resp = input('quer sair dos exercicios [S/N]? ')