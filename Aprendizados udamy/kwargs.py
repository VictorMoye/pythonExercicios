"""
**Kwargs

Poderiamos chamar esse parametro de **qualquer coisa, mas por convençao
chamamos de **Kwargs
Este é mais um parametro que transforma os valores extras em tupla, mas diferente do ARGS
ele exige que ultilizamos parametros nomeados e transforma esses parametros em dicionarios

Quando for fazer uma função podemos ter varias coisas porem todas elas é impresendivel que estejam nesta oredem

1º- Parametros obrigatorios
2º- *Args
3º- Parametros defaul (não obrigatorios)
4º- **Kwargs

"""

resp = ''
while resp != 's':
    print('1- Exemplo 1')
    print('2- Exemplo mais complexo')
    print('3- Ordens de parametros obrigatoriedade ')
    print('4- Entendendo o porque é importante manter essa ordem')
    print('5- Desempacotamento Kwargs')

    escolha = int(input('Qual programa voce quer ver em funcionamento -> '))

    #exemplo 1
    if escolha == 1:
        def cores_favoritas(**kwargs):
            print(kwargs)
        cores_favoritas(marcos ='verde', julia ='branco',fernanda = 'amarelo', victor ='Azul')
        # podemos fazer tambem
        def cores_favoritas2(**kwargs):
            for pessoa, cor in kwargs.items(): # chave em pessoa o valor em cor
                print(f'A cor favorita de {pessoa.title()} é {cor}') # tittle tranformando a primeira letra em maisculo

        cores_favoritas2(marcos='verde', julia='branco', fernanda='amarelo', victor='Azul')
        #OBS: os parametros ARGS e KWARGS não são obrigatorios

    #Exemplo mais complexo
    elif escolha == 2:
        def comprimento_especial(**kwargs):
            #se eu tenho a chave geek dentro do meu dicionairo e se sim, se o valor da chave geek é igual a Python
            if 'geek' in kwargs and kwargs['geek'] == 'Python': # chave e valor kwags
                return 'Você recebeu um cumprimento meu camarada Geek!'

            elif 'geek' in kwargs:
                return f'{kwargs["geek"]} Geek !!'

            else:
                'Não tenho certeza quem voce é'

        print(comprimento_especial())
        print(comprimento_especial(geek='Python'))
        print(comprimento_especial(geek='Oi'))
        print(comprimento_especial(geek='Especial'))
                                                                                                                                                                                                                                       
    elif escolha == 3:
        def minha_funcao(idade,nome, *args,soleiro=False,**kwargs):
            print(f'{nome} tem {idade} anos')
            print(args)
            if soleiro:
                print('Solteiro')
            else:
                print('Casado')
            print(kwargs)
        minha_funcao(8,'Julia')
        minha_funcao(18,'Felicity',4,5,3,solteiro=True)
        minha_funcao(28,'Carolina',eu='Não',voce='Vai')
        minha_funcao(19,'Carla',9,4,3,java=False,python = True)

    #Entendo o porque é importante manter essa ordem dos parametros
    elif escolha == 4:
        #Jeito certo !!
        def mostra_indo(obrigatorio1,obrigatorio2,*args, instrutor ='Geek', **kwargs):
            return [obrigatorio1, obrigatorio2, args, instrutor, kwargs]
        #[1, 2, (3,), 'Geek', {'sobrenome': 'University', 'cargo': 'Instrutor'}] <- saida
        print(mostra_indo(1,2,3, sobrenome='University', cargo='Instrutor'))

        #Jeito errado note a diferença e as ordens dos parametros
        def mostra_indo2(obrigatorio1,obrigatorio2, instrutor ='Geek', *args,**kwargs):
            return [obrigatorio1, obrigatorio2, args, instrutor, kwargs]
        #[1, 2, (), 3, {'sobrenome': 'University', 'cargo': 'Instrutor'}] <- Saida
        print(mostra_indo2(1, 2, 3, sobrenome='University', cargo='Instrutor'))

    #Desempacotamento Kwargs
    elif escolha == 5:
        def mostra_nomes(**kwargs):
            return f"{kwargs['nome']} {kwargs['sobrenome']}"

        nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

        print(mostra_nomes(**nomes))#Note os dois asteristicos pra desempacotar o dicionario

        #outro exemplo
        def soma_multi_numeros(a,b,c):
            return a + b + c
        lista = [ 1,2,3]
        tupla = ( 1,2,3)
        conjunto = {1, 2, 3}
        print(soma_multi_numeros(*tupla))
        print(soma_multi_numeros(*lista))
        print(soma_multi_numeros(*conjunto))

        dicionario = {'a' : 1, 'b' : 2, 'c' : 3} #OBS os nomes das chaves do dicionarios precisam ser extritamente igual aos parametros passados
        print(soma_multi_numeros(**dicionario))

    resp = input('Quer sair do programa [S/N]? ')