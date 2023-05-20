"""
çLista de exercicios 7 parte 2

"""
import math
from  random import randint
resp = ''
while resp != 'S':
    print('1- Escreva uma matriz 4X4 e mostre quantos numeros maiores que 10 ela possui')
    escolha = int(input('\nQual exercicios você quer fazer -> '))

    if escolha == 1:
        matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        maiores = 0
        for linha in range(0, 4):
            for coluna in range(0, 4):
                matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}], [{coluna}]-> '))
                if matriz[linha][coluna] >= 10:
                    maiores += 1
        print('-=' * 30)
        for linha in range(0, 4):
            for coluna in range(0, 4):
                print(f'[{matriz[linha][coluna]:^5}]',end='')  # ^5 <- significa centralizado com 5 casas decimais pra ficar bonitinho
            print()  # pra quebrar a linha quando sair do ultimo laço ou seja da primeira coluna
            # vai ficar quebrando de coluna em coluna

        print(f'Existe {maiores} valores maiores que 10')

    #matriz 5 por 5  com a diagonal pintada do elemento que voce quiser
    elif escolha == 2:
        matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        elemento = int(input('Qual elemento voce quer na diagonal da sua lista '))
        for coluna in range(0, 5):
            for linha in range(0, 5):
                matriz[linha][coluna] = 1
                if coluna == linha:
                    matriz[coluna][linha] = elemento

        print('-=' * 30)
        for coluna in range(0, 5):
            for linha in range(0, 5):
                print(f'[{matriz[coluna][linha]:^3}]', end='')
            print()

    elif escolha == 3:
        matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for coluna in range(0, 4):
            for linha in range(0, 4):
                matriz[coluna][linha] = coluna + linha
        for coluna in range(0, 4):
            for linha in range(0, 4):
                print(f'[{matriz[coluna][linha]:^5}]', end='')
            print()

    elif escolha == 4:
        matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        maior = None
        posição = [0, 0]
        for coluna in range(0, 4):
            for linha in range(0, 4):
                matriz[coluna][linha] = num = int(input(f'Digite o valor na [{coluna}],[{linha}] -> '))
                if maior is None or num > maior:
                    maior = num
                    posição = [coluna, linha]
        for coluna in range(0, 4):
            for linha in range(0, 4):
                print(f'[{matriz[coluna][linha] : ^5}]', end='')
            print()
        print(f'O maior numero é {maior} na posição {posição}')
    elif escolha == 5:
        matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        maior = None
        posição = [0, 0]
        for coluna in range(0, 4):
            for linha in range(0, 4):
                matriz[coluna][linha] = coluna + linha
        for coluna in range(0, 4):
            for linha in range(0, 4):
                print(f'[{matriz[coluna][linha] : ^5}]', end='')
            print()
        num = int(input(f'Informe o valor que voce quer encontrar -> '))
        for coluna in range(0, 4):
            for linha in range(0, 4):
                if num == matriz[coluna][linha]:
                    posição = [coluna, linha]
                else:
                    posição = 'Valor não encontrado'
        print(f'Valor encontrado na linha {posição}')

    elif escolha == 6:
        matriz1 = matriz2 = matriz3 = [[0, 0], [0, 0]]
        num = 0
        lista = []
        print('Dando forma a primeira matriz')
        for coluna in range(0, 2):
            for linha in range(0, 2):
                matriz1[coluna][linha] = num = randint(5, 10)
                lista.append(num)
        for coluna in range(0, 2):
            for linha in range(0, 2):
                print(f'[{matriz1[coluna][linha]: ^5}]', end='')
            print()

        print(lista)
        print('Dando forma a matriz 2')
        for coluna in range(0, 2):
            for linha in range(0, 2):
                matriz2[coluna][linha] = num = randint(5, 10)
                lista.append(num)
        for coluna in range(0, 2):
            for linha in range(0, 2):
                print(f'[{matriz2[coluna][linha]: ^5}]', end='')
            print()
        media = sum(lista) / len(lista)
        print(f'Lista Completa = {lista}')
        print(f'Media total = {media}')
        for cont in range(0, len(lista)):
            if lista[cont] > media:
                matriz3.append(lista[cont])

        for coluna in range(0, 2):
            for linha in range(0, 2):
                print(f'[{matriz3[coluna][linha]: ^5}]', end='')
            print()

    elif escolha == 7:
        matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for coluna in range(0, 10):
            for linha in range(0, 10):
                if coluna < linha:
                    matriz[coluna][linha] = (2 * coluna) + (7 * linha)
                elif coluna == linha:
                    matriz[coluna][linha] = (3 * coluna ^ 2) - 1
                else:
                    matriz[coluna][linha] = (4 * coluna ^ 3) - (5 * linha ^ 2) + 1
        for coluna in range(0, 10):
            for linha in range(0, 10):
                print(f'[{matriz[coluna][linha] : ^ 5}]', end='')
            print()

    elif escolha == 8:
        matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        soma = 0
        lista = list()
        for coluna in range(0, 3):
            for linha in range(0, 3):
                matriz[coluna][linha] = randint(1, 20)
                print(f'coluna [{coluna}] linha [{linha}] = {matriz[coluna][linha]}')
                if coluna < linha:
                    soma += matriz[coluna][linha]
                    lista.append(matriz[coluna][linha])
        for coluna in range(0, 3):
            for linha in range(0, 3):
                print(f'[{matriz[coluna][linha] : ^ 5}]', end='')
            print()
        print(f'Os numeros que estao acima da diagonal principal são \n{lista}')
        print(f'A soma dos numeros que estao acima da diagonal principal é {soma}')

    elif escolha == 9:
        matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        soma = abaixo = diagonal = 0
        lista = list()
        lista2 = []
        lista3 = []
        for coluna in range(0, 3):
            for linha in range(0, 3):
                matriz[coluna][linha] = randint(1, 20)
                print(f'coluna [{coluna}] linha [{linha}] = {matriz[coluna][linha]}')
                if coluna < linha:
                    soma += matriz[coluna][linha]
                    lista.append(matriz[coluna][linha])
                elif coluna == linha:
                    diagonal += matriz[coluna][linha]
                    lista2.append(matriz[coluna][linha])
                else:
                    abaixo += matriz[coluna][linha]
                    lista3.append(matriz[coluna][linha])
        for coluna in range(0, 3):
            for linha in range(0, 3):
                print(f'[{matriz[coluna][linha] : ^ 5}]', end='')
            print()
        print(f'Os numeros que estao acima da diagonal principal são \n{lista}')
        print(f'A soma dos numeros que estao acima da diagonal principal é {soma}')
        print(f'Os numeros que estao abaixo da diagonal principal são \n{lista3}')
        print(f'A soma dos numeros que estao abaixo da diagonal principal é {abaixo}')
        print(f'Os numeros que estaona diagonal principal são \n{lista2}')
        print(f'A soma dos numeros que estao na diagonal principal é {diagonal}')

    elif escolha == 10:
        matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for coluna in range(0, 4):
            for linha in range(0, 4):
                matriz[coluna][linha] = randint(0, 20)
        print('Matriz Original')
        for coluna in range(0, 4):
            for linha in range(0, 4):
                print(f'[{matriz[coluna][linha] : ^ 5}]', end='')
            print()
        print('Matriz transformada')
        for coluna in range(0, 4):
            for linha in range(0, 4):
                matriz[coluna][linha] = randint(0, 20)
                if coluna < linha:
                    matriz[coluna][linha] = 0
        for coluna in range(0, 4):
            for linha in range(0, 4):
                print(f'[{matriz[coluna][linha] : ^ 5}]', end='')
            print()

    elif escolha == 11:
        matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        lista = []
        lista2 = []
        while len(lista2) <= 25:
            for coluna in range(0, 5):
                for linha in range(0, 5):
                    num = randint(0, 99)
                    lista.append(num)
                    if num not in lista2:
                        lista2.append(num)
                        matriz[coluna][linha] = num

        for coluna in range(0, 5):
            for linha in range(0, 5):
                print(f'[{matriz[coluna][linha] : ^ 5}]', end='')
            print()

    resp = input('Você quer sair da lista de exercicios [S/N]? ').upper()