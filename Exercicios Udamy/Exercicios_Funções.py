"""
Exercicios de Funções em Python

"""
def CriarLinha():
    print('=-' * 30)
resp = ''
while resp != 's':
    print('1- Crie uma função que receba um parametro e retorne seu dobro')
    print('2- Faça uma função que receba a data atual (dia/mes/ano e exiba na tela \n'
          '\t no formato textual poe extenso ')
    print('3- Função pra saber se o numero é positivo ou negativo \n'
          '\t Se o numero for positivo retorna 1 negativo ou igual a 0 retorna 0')
    print('4- Informa se o nmero é um quadrado perfeito ')
    print('5- Quantos quadrados perfeitos você quer descobrir')
    print('6- Calcula o volume de uma esfera sendo que o raio é passado por parametro')
    print('7- Converso de horas e minutos pra segundos do dia')
    print('8- Conversão de Celcius pra farenhid e vise versa')
    print('9- Calcula o valor da hipotenusa')
    print('10-Recebe a altura e o raio de um cilindro e calcula o seu volume')
    print('11-Função que recebe um numero e soma todos os seus algoritmos EX: 257 = 2+5+7')
    print('12-Operação matematica pelo caractere que o usuario entrar = / * - + ')
    print('13-Calcula a distancia do carro de acordo com o combustivel dentro dele')
    print('14-Calcule um triangulo diz se é triangulo e qual tipo de triangulo ele é ')
    print('15-Soma todos os numeros que estão entre NUM1 e NUM2')
    print('16-Mostra se é numero primo e o numero primo mais proximos e a lista de todos os numeros primos anteriores a ele')
    print('17-Calcula a fatorial de um numero')
    print('30- Conferir todos os exercicios e tirar a prova real online pra ver se ta certo o resultado')
    print('26- Refazer todos os exercicios existentes loops condições e aplicar as funções')
    escolha = int(input('Qual Exercicio você quer ver em ação -> '))
    print(CriarLinha())
    #Crie uma função que receba um parametro e retorne seu dobro
    if escolha == 1:
        numero_1 = int(input('Informe um numero -> '))
        def Dobro(num1):
            return  num1 * 2
        print(f'O dobro de {numero_1} é {Dobro(numero_1)}')

    #Pega uma data qualquer e retorna por extenso em texto
    elif escolha == 2:
        from datetime import date
        hj = date.today()
        dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
        print("Hoje é", dias[hj.weekday()])

    #Indentifica se o numero é positivo ou negativo
    elif escolha == 3:
        numero_1 = int(input('Infome um numero qualquer -> '))
        def Indentificador_Positivo_Negativo(num1):
            if num1 >= 1:
                return  f'Numero Positivo 1'
            else:
                return f'Numero negativo ou igual a 0 '
        print(Indentificador_Positivo_Negativo(numero_1))

    #Informa se o numero é um quadrado perfeito
    elif escolha == 4:
        numero = int(input('Informe um numero -> '))
        def Quadrado_Perfeito(quadrado):
            raizQ = int(quadrado ** (1/2))

            if (raizQ ** 2) == quadrado:
                return f'O numero {quadrado} é um quadrado perfeito!!'
            else:
                return f'O numero {quadrado} não é um quadrado perfeito!!'
        print(Quadrado_Perfeito(numero))

    #Mostra quantos quadrados perfeitos voce quer saber
    elif escolha == 5:
        aux =1
        qtd = int(input('Quantos quadrados perfeitos você que saber -> '))
        while aux <= qtd:
            print(f'{aux} ^ {2} = {aux, 2,(aux **2)}')
            aux = aux  + 1

    #Calcula o volume de uma esfera sendo que o raio é passado por parametro
    elif escolha == 6:
        import  math

        pi = math.pi
        raio = int(input('Informe o raio da esfera -> '))
        def Raio_Esfera(raio):
            Volume = 4 / 3 * pi * raio ** 3
            return  Volume
        print(f'O voume da esfera é = {Raio_Esfera(raio)}')

    #Converso pegar a HORA MINUTOS SEGUNDOS e converte tudo pra segundos
    elif escolha == 7:
        def Converso_Segundos(hora,minuto):
            hora += hora * 3600
            minuto += minuto * 60
            total = hora + minuto + segundo
            return f'Seu tempo convertido pra segundos é = {total}'
        #print('Informe o seu a sua hora minuto e segundo -> ')
        hora = int(input('Infome uma hora qualquer ->'))
        minuto = int(input('Infome um minuto qualquer ->'))
        segundo = int(input('Infome um segundo qualquer ->'))
        if hora <= 23 and minuto <= 59 and segundo <= 59:
            print(Converso_Segundos(hora,minuto))
            #print(f' {Converso_Segundos(hora,minuto)}')
        else:
            print('Informação errada')
            print('Tente novamente')
            hora = int(input('Infome uma hora qualquer ->'))
            minuto = int(input('Infome um minuto qualquer ->'))
            segundo = int(input('Infome um segundo qualquer ->'))
            if hora <= 23 and minuto <= 59 and segundo <= 59:
                print(Converso_Segundos(hora, minuto))
            else:
                print('Informação errada')

    # Conversão de Celcius pra farenhid e vise versa
    elif escolha == 8:
        temp = int(input(('Informe a temperatura pra conversão -> ')))
        def Converso_De_Temperatura(temperatura):
            print('Você quer converte a temperatura \n'
                  '\t [1] Celcius pra Fahrenheit \n'
                  'ou \n'
                  '[2] Fahrenheit pra Celcius')
            escolha = int(input('Qual sua decisão? '))
            if escolha == 1:
                C = 5/9 * temperatura - 32
                return  f'A Temperatura Fahrenheit convertida pra Celcius é {C} '
            else:
                F = temperatura * (9.0/5.0) + 32.0
                return f'A Temperatura Celcius convertida pra Fahrenheit  é {F} '
        print(Converso_De_Temperatura(temp))

    # Calcula o valor da hipotenusa
    elif escolha == 9:
        a = int(input('Infome o cateto A -> '))
        b = int(input('Infome o cateto B -> '))
        def Hipotenusa(a,b):
            import  math
            hipotenusa = math.sqrt(a**2 + b**2)
            return  f'A hipotenusa é {round(hipotenusa , 2)}'
        print(Hipotenusa(a,b))

    #Recebe a altura e o raio de um cilindro e calcula o seu volume
    elif escolha == 10:
        alt = int(input('Informe a altura do cilindrico -> '))
        rai = int(input('Informe o raio do cilindrico -> '))
        def Celindro(altura,raio):
            pi = math.pi
            volume = pi * (raio ** 2) * altura
            return f'O Volume do Cilindro é {round(volume,2)}'
        print(Celindro(alt,rai))

    # função que recebe um numero e soma todos os seus algoritmos
    # 257 = 2 + 5 +7
    elif escolha == 11:
        numero = int(input('Informe um numero -> '))
        if numero >= 1:
            def Soma_Algoritma(algoritmo):
                soma = 0
                while algoritmo > 0:
                    soma += (int)(algoritmo % 10)
                    algoritmo /= 10
                return f'A soma de todos so algoritmos de {numero} é {soma}'
            print(Soma_Algoritma(numero))
        else:
            print('Numero negativo ou igual a 0 ')

    # operação matematica pelo caractere que o usuario entrar = / * - +
    elif escolha == 12:
        num1 = int(input('Informe o primerio numero -> '))
        num2 = int(input('Informe o primerio numero -> '))


        def Operação_Guiada(num1, num2):
            cont = 0
            while cont <= 2:
                resp = input('Qual operação você deseja fazer \n'
                             '/ = Divisão\n'
                             '* = Multiplicação\n'
                             '- = Subtração\n'
                             '+ = Adição \n'
                             '->')
                if resp == '/':
                    return f'A divisão de {num1} / {num2} é = {round(num1 / num2)} com resto {num1 % num2}'
                elif resp == '+':
                    return f'A Soma de {num1} + {num2} = {num1 + num2}'
                elif resp == '-':
                    return f'A Subtração de {num1} - {num2} = {num1 - num2}'
                elif resp == '*':
                    return f'A Multiplicação de {num1} * {num2} = {num1 * num2}'
                else:
                    print('Operação não reconhecida \n'
                          'Favor dentar de novo ')
                    cont += 1


        print(Operação_Guiada(num1, num2))

    #Calcula a distancia do carro de acordo com o combustivel dentro dele
    elif escolha == 13:
        combustivel = int(input('Informe quantos litros de combustivel voce botou no carro -> '))
        Distancia = int(input('Informe quanto de distancia o seu carro consegue fazer com os litros posto  -> '))
        def Calcula_Distancia_Litro(num1, num2):
            tot = num1 / num2
            if tot < 8:
                return f'Venda seu carro !! \n' \
                       f'Pois ele faz {tot} por Litro'
            elif tot >= 8 and tot <= 14:
                return f'Economico \n' \
                       f'Pois ele faz {tot} por Litro'
            else:
                return f'Super economico \n' \
                       f'Pois ele faz {tot} por Litro'
        print(Calcula_Distancia_Litro(combustivel, Distancia))

    #Calcule um triangulo diz se é triangulo e qual tipo de triangulo ele é
    elif escolha == 14:
        num1 = int(input('Informe o tamanho do lado -> '))
        num2 = int(input('Informe o tamanho do lado -> '))
        num3 = int(input('Informe o tamanho do lado -> '))


        def Qual_Tipo_de_Triangulo(lado1, lado2, lado3):
            if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
                return f'O triangulo é equilatero pois tem as tres medidas iguais {lado1} ={lado2} = {lado3} ou se preferir um triangulo perfeito'
            elif lado1 == lado2 or lado3 == lado2 or lado1 == lado3:
                return f'O triagulo é isósceles pois tem os comprimentos de dois lados iguais {lado3} = {lado1} = {lado2}'
            else:
                return f'O triangulo chamase escaleno pois os tres lados são diferentes {lado1} =  {lado3} = {lado2}'


        def Confirmando_Triangulo(lado1, ladoo2, lado3):

            if lado1 < (ladoo2 + lado3) and ladoo2 < (lado1 + lado3) and lado3 < (lado1 + ladoo2):
                print(Qual_Tipo_de_Triangulo(lado1, ladoo2, lado3))
            else:
                return 'Não é um triangulo!!'
        print(Confirmando_Triangulo(num1, num2, num3))

    # Soma todos os numeros que estao entre o NUM1 e NUM2
    elif escolha == 15:
        num1 = int(input('Informe um numero -> '))
        num2 = int(input('Informe um numero -> '))


        def Soma_Os_Numeros_Entre_Eles(num1, num2):
            if num1 != num2:
                cont = soma = 0
                if num1 > num2:
                    while num1 > num2:
                        num2 += 1
                        soma += num2
                        print(f'n1 {num1} > n2 {num2} == soma {soma}')
                    return f'A soma entre os numeros  é igual a {soma - num1}'
                else:
                    while num2 > num1:
                        num1 += 1
                        soma += num1
                        print(f'n1 {num2} > n2 {num1} == soma {soma}')
                    return f'A soma entre os numeros é igual a {soma - 1}'
            else:
                return f'A soma entre os numeros {num1} e {num2} é igual a {num1 - num2}'
            return


        print(Soma_Os_Numeros_Entre_Eles(num1, num2))

    # Mostra se é numero primo e o numero primo mais proximos e a lista de todos os numeros primos anteriores a ele
    elif escolha == 16:
        num1 = int(input('Informe um numero -> '))
        num_primos = list()


        def ehPrimo(n):
            if n == 2:
                return False
            elif (n % 2 == 0):
                return False
            else:
                i = 3
                while (i <= (n / i)):
                    if ((n % i) == 0):
                        return False
                    i += 2
                num_primos.append(n)
                return True

            return False


        def n_primos(n):

            if (n < 2):
                return 0
            elif (n == 2):
                return 1
            else:
                contador = 1
                while (n > 2):
                    if (ehPrimo(n)):
                        contador += 1

                    n -= 1
                return contador

            return 0


        # funcao para retornar o maior numero primo
        def maior_primo(num):

            if (num < 2):
                return 0
            elif (num == 2):
                return 2
            else:

                while (num > 2):
                    if (ehPrimo(num)):
                        return f'O maior primo de {num1} é {num}'
                    num -= 1
                return num

        #


            return 0


        print(f'{ehPrimo(num1)} p/Número primo!!')
        print(maior_primo(num1))
        print(f'Existe {n_primos(num1)} primos até {num1}')
        print(f'As sequencias dos numeros primos até {num1}\n'
              f'{num_primos[:: -1]}')


    # Calcula a fatorial de um numero
    elif escolha == 17:
        num1 = int(input('Informe um numero -> '))


        def Fatorial(numero):
            if (numero <= 0):
                return f'{numero} Invalido !!'
            elif (numero == 1):
                return f'{numero}!'
            else:
                cont = numero
                fatorial = 1
                while cont > 0:
                    fatorial *= cont
                    cont -= 1
                return fatorial


        print(Fatorial(num1))

    # Retorna quantos numeros primos você quer achar
    elif escolha == 18:
        num1 = int(input('Informe quantos numeros primos você quer achar -> '))
        primo = []


        def Primo(numero):

            import math
            raiz = int(math.sqrt(numero))

            for d in range(2, numero // 2 + 1):
                if (numero % d == 0):
                    return False
            return True


        # Primo(num1)
        # passar uma contadora ate chegar ao nmero num1
        # print(Primo(num1))
        cont = 0
        while len(primo) < num1:  # LEN USAR O KISTA EM LISTA PRA IR ATE O TAMANAHO DO NUMEROB
            cont += 1
            if Primo(cont):
                primo.append(cont)

        print(primo)


        #trianculo de floyd
    elif escolha == 19:
        num1 = int(input('Informe qualquer coisa pra aparecer um triangulo -> '))


        def TrianguloFloyd(num):
            k = 0
            lista = [cont + 1 for cont in range(int((num ** 2 + num) / 2))]
            aux = ''
            for i in range(num):
                for l in lista[k:k + i + 1]:
                    if i > 3:
                        aux += str(l) + ' '
                    else:
                        aux += str(l) + '  '
                print(aux)
                aux = ''
                k += i + 1


        TrianguloFloyd(num1)

    resp = input('Quer sair do programa[S/N]?')
