"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas porem existe diferenças basicas

1. as tuplas sao representada por parentes

2. as tuplas sao imutaveis: isso significa que ao ser criada
uma tupla ela nao muda.

3. e toda a operaçao com uma tupla ela gera outra tupla.



# as tuplas sao representadas por parenteses

tupla1 = (1,2,3,4,5,6,9)
print(tupla1)
print(type(tupla1))

tupla2 = 1,2,3,4,5
print(tupla2)
print(type(tupla2))

# tupla com 1 elementos

tupla3 = 4 # isto nao é uma tupla e considerado inteiro, pois nao tem virgula
print(tupla3)
print(f'isto não é uma tupla ({tupla3})e considerado um inteiro')
print(type(tupla3))

tupla3 = 4, # tuplas sao definidas por virgulas e nao por parentes ou o que seja
print(tupla3)
print(f"isto é uma tupla ({tupla3})")
print(type(tupla3))


# podemos definir que tuplas são definidas por virgulas e nao por uso dos parenteses

(variavel) - > nao é tuplas
(variavel,) -> é tupla
variavel, -> é tupla

"""
print('Aula de Tuplas')
resp =''
while resp != 's':
    print('1-Tupla com 1 elementos')
    print('2-Podemos definir que tuplas são definidas por virgulas e nao por uso dos parenteses')
    print('3-Desempacotamento de putlas')
    print('4-Somando os elementos das tuplas e fazendo alguns textes')
    print('5-Concatenação de tuplas')
    print('6-Pesquisando se determinado elemento esta contido na tupla')
    print('7- Interando sobre tupla')
    print('8-Contando elementos dentro de uma tupla')
    print('9-Dicas de ultilização de tuplas')
    print('10-Slicing')
    escolha = int(input('Qual tupla voce quer ver em ação: '))

    if escolha == 1:
        tupla3 = 4 # isto nao é uma tupla e considerado inteiro, pois nao tem virgula
        print(tupla3)
        print(f'isto não é uma tupla ({tupla3}) e considerado um inteiro')
        print(type(tupla3))
        tupla3 = 4,  # tuplas sao definidas por virgulas e nao por parentes ou o que seja
        print(tupla3)
        print(f"isto é uma tupla {tupla3},  tuplas sao definidas por virgulas e nao por parentes ou o que seja")
        print(type(tupla3))

    # podemos definir que tuplas são definidas por virgulas e nao por uso dos parenteses
    elif escolha == 2:
        print('podemos definir que tuplas são definidas por virgulas e nao por uso dos parenteses')
        variavel = 'variavel'
        print(f'{type(variavel)} - > nao é tuplas')
        variavel = ('variavel',)
        print(f'{type(variavel)} -> é tupla por causa da virgula e nao por causa dos parentenses')
        variavel = variavel,
        print(f'{variavel} -> é tupla apenas pela virgula ')

    #Desempacotamento de putlas
    elif escolha == 3:
        print('3-Desempacotamento de putlas')
        tupla = ('geek univeristy', 'programação em python: enssencial')
        escola, curso = tupla
        print(escola)
        print(curso)
        # gera erro se colocamos um numero diferentes de elementos para desempacotar
        print('Obs não existe metodo pra adição ou remoção de tuplas ')

    # Soma valor maximo e minimo e tamanho
    elif escolha ==4:
        print('Soma valor maximo e minimo e tamanho'
              'se os valores forem todos inteiros ou reais')
        tuplas = (1,2,3,4,5,6,9, 11.5)
        print(f'A soma das tuplas: {sum(tuplas)}')
        print(f'O valor maximo da tupla: {max(tuplas)}')
        print(f'O valo minimo da tupla: {min(tuplas)}')
        print(f'O tamanho da tupla: {len(tuplas)}')

    #concatenação de tuplas
    elif escolha == 5:
        print('Concatenação de tuplas')
        tupla1 = 1,2,3
        print(f'tupla 1: {tupla1}')
        tupla2 = 4,5,6,
        print(f'Tupla2: {tupla2}')
        print(f'Concatenação das tupplas: {tupla1 + tupla2}'
              '\nMas os dados não mudam de tuplas \n'
              f'tupla 1: {tupla1}'
              f'\nTupla 2: {tupla2}')
        print(f'Algumas coisas são permitidas desde que respeite a regra de não alterar as tuplas: Tamanho da tuplas unidas =  {len(tupla1 + tupla2)}')

    #Verificando se determinado elemento esta na tupla
    elif escolha == 6:
        print('Veroficando se determinado elemento esta contido na tupla')
        tupla_6 = 1,2,3
        print(f'Vericando se o elemento 3 esta na tupla {tupla_6}')
        print(3 in tupla_6)
        tupla_6 = 1,2,'victor'
        print(f'Vericando se a string VICTOR esta na tupla {tupla_6}')
        print('victor' in tupla_6)

    #Interando sobre tuplas
    elif escolha == 7:
        num = 852
        tupla_7 = 1,2,3,'victor', num
        for n in tupla_7:
            print(n)
        for indice, valor in enumerate(tupla_7):
            print(indice, valor)

        # Incrementando usando While
        i =0
        meses = 'janeiro', 'fevereiro', 'março', 'maio', 'abril', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
        while i < len(meses):
                print(meses[i])
                i = i + 1

    # Contando elementos dentro de uma tupla
    elif escolha == 8:
        print('Contando elementos dentro de uma tupla')
        tupla_8 = 'a','b','c','d','e','a','b'
        print(f'Tupla 8 '
              f'\n{tupla_8}')
        x = input('qual elemento voce quer pesquisar: ')
        print(f'Existe {tupla_8.count(x)} elementos dentro da tupla') # contanto quantos elementos iguais eu tenho ao qual eu digitei

        escola = tuple('Geek University e livros ilimitados')
        print(f'qual elemento voce quer pesquisar da tupla '
              f'\nEscola: {escola}')
        x = input()
        print(f'Existe {escola.count(x)} elementos dentro da tupla')

        # tambem da pra imprimir apenas usando o indice que voce quer
        indice = int(input(f'Escolha o indice que você quer acessar: '
                           f'\n{escola}'))
        print(escola[indice]) # vendo atraves do indice o que ta alocado dentro da tupla naquela posição

        # Verificando em qual elemento está na tupla
        meses = 'janeiro', 'fevereiro', 'março', 'maio', 'abril', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
        print('Ao contrario do exercicio anterior que eu busco o elemento pelo indice '
              '\n Aqui eu busco o indice pelo elemento ')
        i = input('Qual elemento da tabela mes voce quer busca: ')
        print(meses.index(i)) # OBS se o elemento não existir vai dar erro no cod value erro!!
    # Dicas de ultilização de tuplas
    elif escolha == 9:
        print('Dicas de ultilização de tuplas')
        print('Devemos usar sempre que não precisamos mecher ou modificar os dadods contidos'
              '\n contidos em uma coleção')
        meses = 'janeiro', 'fevereiro','março','maio','abril','junho','julho','agosto','setembro','outubro','novembro','dezembro'
        meses = ['janeiro', 'fevereiro', 'março', 'maio', 'abril', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        print(f'Tabela mes completa e certinha'
              f'\n{meses}')
        meses.append('plays') # adicionando um elemento a lista meses
        print(f'Não faz sendito adicionar o mês plays'
              f' \na tabela de meses que nem existe: \n{meses}')

    # SLICING
    elif escolha == 10:
         #Slicing
         #tupla[inicio:fim:passo]
        meses = 'janeiro', 'fevereiro','março','maio','abril','junho','julho','agosto','setembro','outubro','novembro','dezembro'
        print(meses[5:]) # vai imprimir aparti do incice 5 até o final
        print(meses[4:9])# vai imprimir aparti do indice 4 ate o 8


    # por que usar tuplas
    # tuplas são mais rapidas que listas muito bom pra B.I BIGDATA e essas coisas pois processam mais rapido
    # deixa seu cod mais seguro pois não pode mudar os elementos apenas sobre escrever eles
    # copiando uma tupla pra outra
    resp = input('Quer sair da aula de tuplas [S/N]? ')
