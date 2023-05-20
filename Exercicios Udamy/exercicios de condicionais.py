resp = ''
while resp != 'S':
    print('1- se for positivo informa a raiz quadrada e se for negativo dizer que é invalido')
    print('2- mostrando o maior numero entre eles')
    print('3- receba a altura e o sexo de uma pessoa e calcule o peso ideal e usando a seguinte formula \n'
          '\thomens = (72.7 * h) - 58 \n'
          '\tmulheres = (62.1 * h) - 44, 7 h == altura')
    print("4- Voce deseja receber sua velocidade em \nM/S, metros por segundo: Digite 1 \nOU \nK/M kilometros por hora: Digite 2 ")
    print('5- leia uma distancia em milhas e converta em quillometros e vise versa EXERCICIO 12 ')

    escolha = int(input('qual programa voce deseja fazer -> '))
    if(escolha == 1):
        import  math
        num1 = int(input('Informe um numero: '))
        num2 = num1
        raiz = f'O Número é {num1} e a raiz quadrada dele é {round(pow(num1, 1 / 2), 2)}'if num1 >= 1 else 'O Número é {num1} negativo e invalido'
        print(raiz)
        #List Compreenhesion
        print([f'O Número é {num2} e a raiz quadrada dele é {round(math.sqrt(num2), 2)}' if num2 >= 1 else f'O Número é {num2} negativo e invalido'])

    elif(escolha ==2):
        import math

        num1 = int(input('Informe um numero: '))
        num2 = int(input('Informe um segundo numero: '))

        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        else:
            print(f'{num2} é maior que {num1}')

        print('Fazendo a mesma coisa com List Comprehension -> ')
        exercicio2 = f'{num1} é maior que {num2} ' if num1 > num2 else f'{num2} é maior que {num1}'
        print(exercicio2)

    elif(escolha == 3):
        peso = float(input('Digite o peso da pessoa: '))
        altura = float(input('Digite a altura da pessoa: '))
        print('\nFAVOR RESPONDER APENAS COM [H/M]')
        sexo = input(' \nDetermine o sexo da pessoa: [H = HOMENS / M = MULHERES]').upper()
        mulher = (62.1 * altura) - 44.7
        homem = (72.7 * altura) - 58
        nome = input(f"Digite o nome do(a) pessoa: ")
        print('Fazendo a mesma coisa com List Comprehension -> ')
        print(f"O peso ideal da {nome} \nÉ {mulher} \nporém hoje é {peso}" if (sexo == 'M')
                else f"O peso idela de {nome} \nÉ {homem} \nporém hoje é {peso} ")

    elif(escolha == 4):
        print("Voce deseja receber sua velocidade em \nM/S, metros por segundo: Digite 1 \nOU \nK/M kilometros por hora: Digite 2 ")
        resp = int(input('Digite sua resposta: '))
        if resp == 1:
            velocidade = float(input('Digite sua velocidade em KM: '))
            velocidade2 = velocidade / 3, 6
        elif resp == 2:
            velocidade = float(input('Digite sua velocidade em M/S: '))
            velocidade2 = velocidade * 3, 6

        print(f'Sua velocidade é {velocidade}K/M  e conertidad  é {velocidade2} M/S' if resp == 1 else f'Sua velocidade é {velocidade}m/s e conertida é {velocidade2} K/M')
        print('fim!!')

    elif(escolha == 5):
        print('Voce quer sua distancia convertida em \nMILHAS \nDigite 1 \nOU\nQUILOMETROS\n Digite 2 ')
        resp11 = int(input('Digite sua resposta: '))

        if resp11 == 1:
            distancia = float(input('Convertendo de quilometros para milhas \n\n Informe sua distancia em quilometros: '))
            diatancia2 = distancia / 1.61
        elif resp11 == 2:
            distancia = float(input('Convertendo de Milhas para Quilometros \n\n Informe sua distancia em milhas: '))
            diatancia2 = distancia * 1.61
        print(f'Sua distancia em Milhas é {distancia} milhas e convertida é {distancia / 1.61} Quilometros' if resp11 == 1 else f'Sua distancia em Milhas é {distancia} milhas e convertida é {distancia * 1.61} Quilometros')


    resp = input('quer sair do programa [S/N]- > ').upper()