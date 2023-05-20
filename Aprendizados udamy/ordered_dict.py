""""
Módulo Collections: Orderes Dict

"""
resp = ''
while resp !='s':
    print('2-percorrendo um dicionario')
    print('1-Ordenando um dicionario')
    print('3-Entendendo a diferença de Dict e ordered dict')

    escolha = int(input('Qual programa vc quer usar? '))
    if escolha == 1:
        # Em um dicionario a ordem de inserção dos elementos não é garantida
        dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

        print(dicionario)

        for chave, valor in dicionario.items():
            print(f'Chave = {chave} : Valor= {valor}')
    elif escolha == 2:
        #Fazendo o import
        #OrderedDict ele garante a ordem de inserção dos elementos
        from _collections import  OrderedDict
        dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
        print(dicionario)

        for chave, valor in dicionario.items():
            print(f'Chave = {chave} : Valor= {valor}')

    #Entendendo a diferença de Dict e ordered dict
    elif escolha == 3:
        #dicionario comum
        dict1= {'a':1, 'b': 2}
        dict2 = {'b':2, 'a': 1}

        print(dict1 == dict2) # true ja que a ordem dos elementos não importa para os dicionairos
        from collections import OrderedDict
        # ordered dict
        odic1 = OrderedDict({'a':1, 'b':2})
        odic2 = OrderedDict({'a':2, 'b':1})
        print(odic1 == odic2) # false, ja que as ordens dos elementos importa para o ordered dict


    resp = input('Quer sair do programa [S/N]? ')
