"""
Ultilizando Lambdas

Elas são funções sem nomes ou seja funções anonimas

"""
resp = ''
while resp != 'S':

    print('1-Difeença de uma função normal e um lambda ')
    print('2-Expressões lambdas com muiltiplas entradas ')
    print('3-Nenhuma ou mais entrada em lambdas')
    print('4-Ordenando nomes e sobrenomes com labda')
    print('5- Matematica em labda ou função quadratica ')
    escolha = int(input('Qual programa voce quer executar -> '))


    if(escolha == 1):
        #função normal
        def funcao(parametro):
            return  3 * parametro + 1
        print(funcao(4))
        print(funcao(7))

        #Parte Lambda
        lambda  parametro : 3 * parametro + 1

        calc = lambda  parametro : 3 * parametro + 1
        print(calc(4))
        print(calc(7))

    #Expressoes lambdas com multiplas entradas
    elif(escolha == 2):
        nome = input('Informe seu nome-> ')
        sobrenome = input('Informe seu sobrenome-> ')
        nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title() # primeira letra copleta e o outro tirar o espaço
        print(nome_completo(nome,sobrenome))
        print(nome_completo('Felicity    ', 'smock '))
        print(nome_completo('      bruce ', 'WaynE'))

    #Nenhuma ou mais entradas em labdas
    elif(escolha == 3):
        amar = lambda : 'Como não amar python'
        uma = lambda x: 3 * x * 3
        duas = lambda x, y: (x * y) ** 0.5
        tres = lambda  x,y,z: 3/(1 / x * 1 / y * 1 /z)
        #n = lambda  x1,x2, ...xn: <expressões>
        print(amar())
        print(uma(9))
        print(duas(23,46))
        print(tres(9,23,46))
        # se pasarmos mais ou menos parametros que o esperado como em qualquer função vai dar erro

    # ordenando nomes e sobrenomes
    elif escolha == 4:
        # outro errro
        autores = ['Victor Moye', 'Bruce qayne', 'tony stark ', 'steven roger', 'diana', 'bruce moye wayne',
                   'R. Carlos']
        print(autores)
        # transformando tdos os nomes em lista separado os sobrenomes por um espaço e invertendo pegando apenas o ultimo nome e o lower tranforma tudo em minusculo
        autores.sort(key = lambda sobrenome : sobrenome.split(' ')[-1].lower())
        # a proposito esse é o jeito certo de usar a função lambda
        print(autores)

    # função quadratica e matematica
    elif escolha == 5:
        # funçao quadratica
        # quadraditica = f(x) = a * x ** 2 (+-) b * x + c
         # definindo a função

        def gerafora_quadratica(a,b,c):
            """ f(x) = a * x ** 2 (+-) b * x + c"""
            return lambda x: a * x ** 2 + b * x + c

        teste = gerafora_quadratica(2,3,-5)
        print(teste(0))
        print(teste(1))
        print(teste(2))
        print(teste(3))
        print(gerafora_quadratica(23,46,94)(9))#primerio ja estou passando so parametros fixos e depois tou passando a funçao e X pra executar no lambda


    resp = input('voce quer sair do programa [S/N]? ').upper()