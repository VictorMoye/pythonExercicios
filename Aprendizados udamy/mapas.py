"""
Mapas -> Conhecidos em Python como Dicionarios
Dicionarios em Python são representado por Chaves {}
"""
print('Mapas -> Conhecidos em Python como Dicionarios')

resp = ''
while resp != 's':
    receita = {'jan': 100, 'fev': 260, 'mar': 400}
    print('1-Interar sobre dicionario')
    print('2-Imprimindo os valores')
    print('3-Imprimindo chave valor')
    print('4-Desempacotamento de Dicionairo')
    print('5-Somar, valor maximo\min e tamanho')
    escolha = int(input('Qual dado voce quer acessar : '))

    if escolha == 1:
        # Interar sobre dicionario
        print(receita)
        # Imprimindo as chaves
        for chave in receita:
            print(chave)

        # modo pythonico pois é recomendado que voce demostre que é a chave que voce ta trabalhando
        for chave in receita.keys():
                print('Modo pythonico mostrando a chave')
                print(receita[chave])

        # Imprimindo o dicionario de chaves
        print('Imprimindo o Dicionario de chaves')

    elif escolha == 2:
        for chave in receita:
            print(receita[chave])

    # Imprimindo chave valor
    elif escolha == 3:
        for chave in receita:
            print(f'{chave} : {receita[chave]}')

        for chave in receita:
            print(f'Em {chave} recebi R$: {receita[chave]}')

    #Desempacotamento de Dicionario
    elif escolha == 4:
        print(receita)
        print(receita.items())
        for chave,valor in receita.items():
            print(f'Chave = {chave} e valor = {valor}')

    #Somar, valor maximo\min e tamanho
    elif escolha == 5:
        #Se os valores forem todos inteiros ou reais
        print(sum(receita.values()))
        print(max(receita.values()))
        print(min(receita.values()))
        print(len(receita))

    resp = input('Quer sair do programa [S/N]? ')