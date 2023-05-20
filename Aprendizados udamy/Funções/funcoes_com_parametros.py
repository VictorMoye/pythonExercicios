"""
Funções com parametro (de entrada)
- Funções que recebem dados para serem processados dentro da mesma;
Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saida

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saida;
- Possuem entrada mas não possuem saida
- Não possuem entrada mas possuem saida
- Possuem entrada e saida

"""

resp = ''
while resp != 's':
    print('1- Refatorando uma fução ')
    print('2- Refatorando 2 parametros ')
    print('3- Nomeando parametros ')
    print('4- Erros comum na ultiilização do return')
    escolha = int(input('Qual exercicio voce quer ver -> '))
    # Refatorando uma fução
    if escolha == 1:
        def quadrado(numero):
            return  numero ** 2

        def cubo(numero):
            return numero ** 3
        print(quadrado(7))
        print(cubo(7))
        print(quadrado(2))
        print(cubo(2))
        print(quadrado(5))
        print(cubo(5))

        #Refatorando outra função
        def cantar(aniversariante):
            print('parabens')
            print('pra')
            print(f'Voce {aniversariante}')
        cantar('Victor')
        print(f'parametro {cantar("Moye")}')# resp None

    elif escolha == 2:
        def soma(a,b):
            return a + b
        def multiplicar(a, b):
            return a * b
        def outra(num, b, msg):
            return (num + b) * msg

        print(soma(5, 2))
        print(multiplicar(4, 5))
        print(outra(45,85, 56))
        #OBS: se a gente informa 3 parametros o programa espera receber 3 argumentos se ele nao receber
        #Acontece o type erro
        # ou seja se a função espera receber N parametros deve se enviar os mesmos N argumetnos pra ela
        #print(soma(a))
        #print(multiplicar(b)) # tudo aqui da type erro
        #print(outra(a, b ,f,g))

    elif escolha ==3:
        #Modo errado
        print('Modo errado de fazer')
        def nome_completo(string1, string2):
            return f'Seu nome completo é {string1} {string2}'
        print(nome_completo('Angelina',' Jolie'))
        print('Modo Certo de fazer')
        #Modo certo
        def nome_completo2(nome,sobrenome):
            return f'Seu nome completo agora é {nome} {sobrenome}'
        print(nome_completo2('Victor', 'Wayne'))
        #Parametros deve se ter nome definido que sejam bem claros para que a pessoa possa entender
        #Argumentos sao dados passados para o parametro
        #Parametros sao dados recebidos pelo argumento sao passadas na definição da função

        #A ordem dos parametros importa
        #Exemplo
        nome = 'felicity'
        sobrenome = 'Smoke'
        print(nome_completo2(sobrenome, nome))

        #Argumentos nomeados (Keyword Arguments)
        #Caso especificamos os argumentos podemos ultilizalos de qualquer ordem
        #Neste caso especifico a ordem não importa nada
        #Exemplo
        print(nome_completo2(nome= 'Felicity',sobrenome='Smoke'))
        print(nome_completo(string1='Victor',string2='Moye'))
        print(nome_completo2(sobrenome='Wayne',nome='Bruce'))

    #Erros comum na ultiilização do return
    elif escolha == 4:

        def soma_impares(numeros):
            total = 0
            for num in numeros:
                if num % 2 != 0:
                    total = total + num
                    # O return finaliza a função se ele estivesse aqui por mais que a função tivesse outras coisas pra se fazer
                    # ela simplesmente saia aqui e terminaria tudo
                    # ou seja tome cuidado com a função return pois ela sai da função mesmo nao estando terminada
            return total
        lista = [1,2,3,4,5,6,7]
        print(soma_impares(lista))
        tuple = 1,2,3,4,5,6,7
        print(soma_impares(tuple))

    resp = input('Quer sair do programa [S/N] ? ')