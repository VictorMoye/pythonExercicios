"""
print('programa que mostre os 5 primeiros multiplos de 3 considerando os maiores que 0')

num = int(input('informe um numero: '))
for num in range(1,20,num):
    print(num)


"""
print('Exercicios sessão 6 loops')

resp = ''
while resp != 's':
    print('1- Calcula os multiplos de qualquer numero')
    print('2- Imprimir os numeros de 1 a 100')
    print('3- Contagem de expoente ate o numero que voce quer ver')
    print('4- Contagem regressiva começando de onde voce quiser indo ate 0 zero')
    print('5- Digite 5 valores e some eles')
    print('6- Programa que ler 10 numeros e entrega a media e mediana e media harmonica dos numeros')
    print('7- Programa que mostra o maior e o menor numero lido')
    print('8- Programa que ler um numero N e imprimi os 4 primeiros numeros naturais impares')
    print('9- Programa que calcula os 50 primeiros numeros pares')
    print('10-Imprimi todos os numeros naturais de 0 a N em ordem crescente e decrescente')
    print('11-Algoitmo que mostra todos os numeros pares de 0 ate N e mostre eles em ordem crescente e decrescente')
    print('12-Analisando o numero e cuspindo de volta os algorismo que compoem esse numero')
    print('13-Leia uma certa quantidade de numero e mostre quantas vezes o maior numero se repeti')
    print('14-Mostra a soma de todos os pares digitados e a multiplicação de numeros impares e o inverso tambem')
    print('15-Programa que valida a indentidade da pessoa [solteira idade nome salario estado sexo]')
    print('16-Programa que mostra os divisores de um numero ')
    print('17-Programa que encontra os divisores de um numero ')
    print('18-Progrma que calcula a soma de todos os divisores de um numero')
    print('19-Programa que soma todos os numeros naturais abaixo de mil e que sejam multiplos de 3 e 5')
    print('20-Calcular o numero harmonico H = 1+1/2+1/3+1/4+1...N+1')
    print('21-Calcular o numero  H = 1+1/2!+1/3!+1/4!+1...N+1')
    print('22-Gerar varios dados D1,D2  e mostrando os resultados d1 > or < or == ate o fim do algoritmo')
    print('23-mostra os N primeiros multiplos de dois numeros diferentes')
    print('24-MDC de dois numeros ')
    print('25-Soma os numeros impares contindo nos intervalos de dois numeros diferentes')
    print('26-Separa os algoritmos de um numero em duas partes depois soma eles e eleva ao quadrado e mostra qual deles é igual ao numero digitado ')
    print('28-Pega dois numeros e informa a soma dos numeros pares contidos entre eles e ao mesmo tempo a multiplicação dos numeros impares')
    escolha = int(input('Qual programa você quer ver em ação? '))

    #calcula os multiplos de qualquer numero
    if escolha == 1:
        # calculando o multiplos de qualque numero
        mult = int(input('Qual multiplos você quer vêr? '))
        cont = num = int(input('Até qual numero? '))

        for num in range(0, num, mult):
            print(num)
        print(cont)

        print('Usando Maps')

    elif escolha == 2:
        num = 1
        for num in range(1,100):
            print(num)

    elif escolha == 3:
        num = int(input('escolha o numero de inicio: '))
        parada = int(input('informe o numero de parada: '))
        while num <= parada:
            print(num)
            num = num + num

    elif escolha == 4:
        num = int(input('informe um numero: '))
        while num > 0:
            print(f'{num - 1}')
            num = num - 1

    # some os 5 numeros que o usuario digitar
    elif escolha == 5:
        cont = 1
        soma = 0
        while cont <= 5:
            num = int(input('informe o numero: '))
            cont +=  1
            soma += num
        print(f'A soma de todos os valores foi = {soma}')

    #Media mediana e media harmonica
    elif escolha == 6:
        import statistics

        cont = 1
        media = mediaponderada = 0
        quant = int(input('Digite quantos numeros voce ira colocar na lista: '))
        lista = []
        for cont in range(0, quant):
            num = int(input('informe um numero: '))
            lista += [num]

        print(f'Valores digitados: {lista}')
        print(f'A mediana dos valores é {statistics.median_grouped(lista)}')
        print(f'A media dos valores é {statistics.median(lista)}')
        print(f'A media harmonica é {statistics.harmonic_mean(lista)}')

        print(type(lista))



    #Mostra o maior e o menor numero lido
    elif escolha == 7:
        resp = 's'
        soma = quant = maior = menor = 0
        while quant <= 10:

            num = int(input('Digite um numero: '))
            soma += num
            quant += 1
            if quant == 1:
                maior = menor = num
            else:
                if num > maior:
                    maior = num
                if num < menor:
                    menor = num

        print(f'O Seu maior numero foi = {maior}')
        print(f'O Seu menor numero foi = {menor}')

    #Programa que ler um numero N e imprimi os 3 primeiros numeros naturais impares
    elif escolha == 8:
        cont = 0
        num = int(input('Escolha um numero: '))
        print(f'O numero escolhido foi = {num}')
        print('e seus 3 proximos impares são: ')
        while cont <= 3:
            if num % 2 == 0:
                num += 1
                print(num)
            else:
                num += 2
                print(num)
            cont += 1

    #Programa que calcula os 50 primeiros numeros pares
    elif escolha == 9:
        num = int(input('Escolha um numero: '))
        soma = cont = 0
        while cont <= 50:
            if num % 2 == 0:
                num += 2
                print(f'{cont}º = {num}')
            else:
                num += 1
                print(f'{cont}º = {num}')

            soma += num
            cont +=1
        print(f'A soma de todos os numeros pares é = {soma}')

    # Imprimi todos os numeros naturais de 0 a N em ordem crescente e decrescente
    elif escolha == 10:
        num = int(input('Escolha um numero: '))
        qtd = num
        for num in range(num,0, -1):
            print(num)
            num -= 1

        for cont in range(0,qtd):
            print(cont)
            cont += 1

    #Algoitmo que mostra todos os numeros pares e impares de 0 ate N e mostre eles em ordem crescente e decrescente
    elif escolha == 11:
        num = int(input('Escolha um numero: '))
        lista_par = []
        lista_impar = []
        for cont in range(0,num):
            if cont % 2 == 0:
                lista_par += [cont]
            else:
                lista_impar += [cont]

        print(f'Mostrando todos os numeros pares de 0 a {num}')
        print(lista_par)
        print(f'Mostando todos os numeros impares de 0 a {num}')
        print(lista_impar)
        print(f'Mostrando todos os numeros pares invertidos de {num} a 0')
        print(lista_par[:: -1])
        print(f'Mostando todos os numeros impares invertidos de {num} a 0')
        print(lista_impar[:: -1])
        print(f'Mostrando a soma de todos os numeros pares')
        print(sum(lista_par))
        print(f'Mostrando a soma de todos os numeros impares')
        print(sum(lista_impar))

    #Analisando o numero e cuspindo de volta os algorismo que compoem esse numero
    elif escolha == 12:
        def soma_algoritmos(num):
            soma =0
            while(num > 0):
                soma += (num % 10)
                num /=10
            return soma
        num = int(input('Informe um numero -> '))
        if num <= 0:
            print(f'{num} Invalido !!')
        else:
            print(f'A soma dos algoritmos de {num} é {soma_algoritmos(num)}')

    #Leia uma certa quantidade de numero e mostre quantas vezes o maior numero se repeti
    elif escolha == 13:
        lista = []
        men = mai = cont_mai = cont_mei = 0
        tamanho = int(input('Digite o tamanho de sua lista: '))

        #Adicionando elementos a lista
        for c in range(0, tamanho):
            lista.append(int(input('Digite um numero: ')))

            #Colocando o maior e menor numeros em suas variaveis
            if c == 1:
                mai = men = lista[c]
            else:
                if lista[c] > mai:
                    mai = lista[c]
                if lista[c] < men:
                    men = lista[c]

        print('=' * 30)
        print(f'O tamanho da lista é {len(lista)}')
        print(f'{lista}')
        print(f' O maior valor foi {mai} nas posições ', end='')

        #Varrendo os indices pra achar o maior numero e iniciando um contador pra saber quantas vezes ele se repete
        for indice, valor in enumerate(lista):
            if valor == mai:
                print(f'[{indice}]', end="")
                cont_mai += 1
        print()
        print(f'O menor foi {men}  nas posições ', end='')

        #Varrendo os indices e iniciando um contador pra saber quantas vezes o menor se repete
        for indice, valor in enumerate(lista):
            if valor == men:
                print(f' [{indice}]', end='')
                cont_mei += 1
        print(f'O maior numero {mai} foi digitado {cont_mai} vezes')
        print(f'O menor numero {men} foi digitado {cont_mei} vezes')

    #Mostra a soma e a multiplicação de numeros pares e impares digitados de 0 ao numero que voce quer
    elif escolha == 14:
        # Mostra a soma e a multiplicação de numeros pares e impares digitados de 0 ao numero que voce quer
        from functools import reduce
        from operator import mul
        from operator import add

        num = int(input('Informe um numero? '))
        lista_par = []
        lista_impar = []

        for cont in range(0, num):
            if cont % 2 == 0:
                lista_par.append(cont)
            else:
                lista_impar.append(cont)
        if num % 2 == 0:
            lista_par.append(num)
        else:
            lista_impar.append(num)

        mutl_impar = reduce(mul, lista_impar)
        adc_impar = reduce(add, lista_impar) # ou {SUM(LISTA_IMPAR)}
        adc_par = reduce(add, lista_par) # ou {SUM(PAR)}
        print('Lista Impar')
        print(lista_impar)
        print(f'A multiplicação de todos os numeros impares é = {mutl_impar}')
        print(F'A soma de todos os elementos é = {adc_impar}')
        lista_par.pop(0)
        mult_par = reduce(mul, lista_par)
        print('Lista Par')
        print(lista_par)
        print(F'A soma de todos os elementos é = {adc_par}')
        print(f'A multiplicação de todos os numeros pares é = {mult_par}')

    #Mostra o nome idade salario sexo e estado civil
    elif escolha == 15:
        nome = input("Digite o seu nome: ")
        while len(nome) <= 3:
            nome = input("Digite o seu nome[MAIOR QUE 3 CARACTERES]: ")
        idade = int(input("Digite a sua idade: "))
        while idade < 0 or idade > 150:
            idade = int(input("Digite a sua idade[ENTRE 0 E 150]: "))
        salario = float(input("Digite o seu salário: "))
        while salario <= 0:
            salario = float(input("Digite o seu salário[MAIOR QUE 0]: "))
        sexo = input("Digite o seu sexo [f, m]: ")
        while sexo != 'f' and sexo != 'm':
            sexo = input("Digite o seu sexo[f OU m]: ")
        estado_civil = input("Digite o seu estado cívil [s, c, v, d]: ")
        while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
            estado_civil = input("Digite o seu estado civil[s, c, v, d]: ")

    #Programa que mostra os divisores de um numero e mostra a soma de seus divisores tambem
    elif escolha == 16:
        num = int(input('Escolha um numero: '))
        def divisores(num):
            for i in range(1, num // 2 + 1):
                if num % i == 0:
                    yield i
            yield num


        print(f'Lista com todos os divisores do numero {num}')
        print(list(divisores(num)))

    #Proggrama que leia um numero inteiro e mostre seus divisores
    elif escolha == 17:
        num = int(input('Informe um numero  -> '))

        def divisores(num):
            for i in range(1, num // 2 + 1):
                if num % i == 0:
                    yield i
            yield num


        print(list(divisores(num)))

    #Progrma que calcula a soma de todos os divisores de um numero
    elif escolha == 18:
        num = int(input('Informe um numero  -> '))


        def divisores(num):
            for i in range(1, num // 2 + 1):
                if num % i == 0:
                    yield i
            yield num


        print(list(divisores(num)))
        print(sum(divisores(num)))

    #Programa que soma todos os numeros naturais abaixo de mil e que sejam multiplos de 3 e 5
    elif escolha == 19:
        mult_3 = []
        mult_5 = []
        cont = 0
        while cont <= 1000:
            resultado_3 = cont * 3
            mult_3.append(resultado_3)
            if resultado_3 >= 999:
                break
            cont += 1
        print('Todos os numeros multiplos de 3 menores que MIL')
        print(mult_3)
        print(f'A soma de todos esses números é {sum(mult_3)}')
        cont = 0
        while cont <= 1000:
            resultado_5 = cont * 5
            mult_5.append(resultado_5)
            if resultado_5 >= 999:
                break
            cont += 1
        print('Todos os numeros multiplos de 5 menores que MIL')
        print(mult_5)
        print(f'A soma de todos esses números é {sum(mult_5)}')

    #Calcular o numero harmonico H = 1+1/2+1/3+1/4+1...N+1
    elif escolha == 20:
        aux = 1
        soma = 0
        while aux:
            aux = int(input('Informe um numero -> '))
            if aux:
                for i in range(1, aux):
                    soma += 1 / i
                print(f'O resultado da serie é {round(soma, 2)}')
            else:
                print('Entrada terminada pelo usuario')

    #Calcular o numero  H = 1+1/2!+1/3!+1/4!+1...N+1
    elif escolha == 21:
        num2 = int(input('Informe um numero -> '))
        resultado = 1
        num = 1
        while num <= num2:
            fat = 1
            for cont in range(1, num):
                fat = fat * cont
            resultado += (1 / fat)
            num += 1

        print(f'O resultado -> {resultado}')

    # Gerar varios dados D1,D2  e mostrando os resultados d1 > or < or == ate o fim do algoritmo
    elif(escolha == 22):
        import random

        num2 = int(input('Informe quantos numeros você quer testar -> '))
        for cont in range(1, num2 + 1):
            d1 = random.randint(1, 10)
            d2 = random.randint(1, 10)
            if (d1 > d2):
                print(d1, '>', d2)
            elif (d2 > d1):
                print(d1, '<', d2)
            else:
                print(d1, '=', d2)

    # mostra os N primeiros multiplos de dois numeros diferentes
    elif(escolha == 23):
        mult = int(input('Informe quantos multiplos vc quer saber de ambos os numeros-> '))
        num1 = int(input('Informe um numero -> '))
        num2 = int(input('Informe outro numero -> '))
        lista1 = [0]
        lista2 = [0]
        for cont in range(1, num1 // 2 + 1):
            if num1 % cont == 0:
                lista1.append(cont)

        for i in range(1, num2 // 2 + 1):
            if num2 % i == 0:
                lista2.append(i)

        print(lista1)
        print(lista2)
        print(f'Todos os {mult} multiplos de {num1} ')
        print([lista1[cont] for cont in range(0, mult)])
        print(f'Todos os {mult} multiplos de {num2} ')
        print([lista2[cont] for cont in range(0, mult)])

    #MDC de dois numeros
    elif(escolha == 24):
        num1 = int(input('Informe um numero -> '))
        num2 = int(input('Informe outro numero -> '))
        cont = ''
        mdc = []
        num = 1
        # primeiro vamos tirar o MDC de dois numeros
        while cont != 'S':
            if num1 % num == 0 and num2 % num == 0:
                mdc.append(num)
            num += 1
            if num >= num2:
                cont = 's'.upper()
        print(f'O mdc de {num1} e {num2} é = {mdc[-1]}')

        # Soma de numeros impares contidos no intervalo do numero 1 e numero 2
    elif(escolha == 25):
        num1 = int(input('Informe um numero -> '))
        num2 = int(input('Informe outro numero -> '))
        if num1 == num2 or num1 > num2:
            print('Intervalo invalido')
        else:
            lista = [0]
            cont = num1
            for cont in range(cont, num2 + 1):
                if cont % 2 == 1:
                    lista.append(cont)
            print(f'A soma de todos os numeros impares contido nos intervalos de {num1} até {num2} é = {sum(lista)}')
            print(lista)
    #A soma de seu algoritmo elevado ao quadrado é igual ao proprio numero
    elif(escolha == 26):

        import math

        num = int(input('Informe um numero -> '))
        num2 = int(input('Informe outro numero -> '))
        cont = num
        for cont in range(cont, num2 + 1):
            num1 = cont // 100
            num2 = cont // 1 % 100
            if (math.pow(num1 + num2, 2) == cont):
                print(f'O numero é {cont}')
                print(f'{num1} + {num2} ** 2 = {math.pow(num1 + num2, 2)}')

    # Calcula a area de um triangulo apenas com duas entradas de numeros base e altura e não pode permitir entrada de dados invalidos medidas menores ou iguais a 0
    elif escolha == 27:
        import math

        base = int(input('Informe a base  -> '))
        altura = int(input('Informe a altura -> '))
        if ((base <= 0) or (altura <= 0)):
            print('Dados invalidos')
        else:
            print(f'A area do triangulo é {base * altura}')

    elif escolha == 28:
        num1 = int(input('Informe um numero -> '))
        num2 = int(input('Informe um numero -> '))
        aux = 0
        mult = 1
        if num2 > num1 or num1 == num2:
            print(f'Invalido {num2} é maior ou igual a {num1} por tando a esposta é zero !!')
        else:
            while (num1 <= num2):
                if (num1 % 2 == 0):
                    aux += num1
                if (num1 % 2 == 1):
                    mult *= num1
                num1 += 1
            print(f'aux {aux} -> mult {mult}')


    resp = input('Você quer sair do programa [S/N]? ')

