"""
Funções com retorno

OBS:
Return -> ela finaliza a funçao ou seja ela sai da execução da função
podemos ter em uma função diferentes returns
podemos em uma função retorna qualquer tipo de dado e ate mesmo multiplicar valores
"""
resp = ''
while resp != 's':
    print('1- Fazendo o basico e mostrando uma funççao')
    print('2- Refatorando uma função')
    print('3-Diferentes returns dentro da mesma função')
    print('4-Função cara ou coroa')
    print('5-Função impar par em uma linha de cod')
    escolha = int(input('Qual exercicio voce quer ver -> '))
    if escolha == 1:
        numeros = [1, 2, 3]
        ret_pop = numeros.pop()
        print(f'Retorno de pop {ret_pop}')

        ret_pr = print(numeros)

        print(
            f'retorno de print : {ret_pr}')  # nao retorna nada ele no maximo mostra na tela mas nao retorna valor nenhum


        def quadrado_de_7():
            print(7 * 7)


        ret = quadrado_de_7()
        print(f'retorno {ret}')  # mais uma vez mostra na tela mas nao retorna nada dado nenhum
        """
        OBS: Em python quando uma função nao retorna nenhuum valor o retorno é None 
        """

    # refatorando a função pra retorna o valor
    elif escolha == 2:
        def quadrado_de_7():
            return 7 * 7
        ret = quadrado_de_7()
        print(f'Retorno {ret}')
        #nao precisamos necessariamente crair uma variavel para recever o retorno de uma funçao
        #podemos apenas rexecutar a função
        #exemplo
        def quadrado_de_9():
            return 9 * 9
        print(f'Retorno {quadrado_de_9()}')

        def diz_oi():
            return 'Oi!!'
        eu = 'Victor'
        print(diz_oi() + eu )

    #diferentes returns dentro da mesma função
    elif escolha == 3:
        def diz_oi():
            print('estou sendo executado antes do retorno')
            return 'Oi'
            print('estou sendo exutdo depois do return')# o return funaliza a funão ou seja isso nunca sera executado
        print(diz_oi())

        #Exemplo 2
        def nova_funcao():
            variavel = None
            if variavel:
                return 4
            elif variavel is None:
                return  3.2
            return  'b'
        print(nova_funcao())

        #exemplo 3
        def outra_funcao():
            return 1,2,3,4,5
        num1, num2,num3,num4, num5 = outra_funcao()
        print(num1,num2,num3,num4,num5)
        print(type(outra_funcao()))
        print(outra_funcao())

    elif escolha == 4:
        from random import random
        def joga_moeda():
           # valor = random()# radom tras um numero entre 0 e 1 com varios valores decimais
            if random() > 0.5:# valor > 0.5: <- decodificação desnessesaria o radom retorna valor logo ele pode ser usado como expressao de condicionais
                return 'cara'
            else:
                return 'coroa'
        print(joga_moeda())

    elif escolha == 5:
        from random import randint
        def impar_par():
            numero = randint(1,99)
            if numero % 2 != 0:
                return 'Impar'
            return 'Par'
        print(impar_par())


    resp = input('Quer sair do programa [S/N] ? ')