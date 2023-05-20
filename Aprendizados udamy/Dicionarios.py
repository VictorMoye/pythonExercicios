"""
Dicionarios

OBS: Em algumas linguagems de programação, os dicionarios em python sao conhecidos por
mapas

Dicionarios sao coleções do tipo CHAVE/VALOR

dicionarios sao representados por chaves {}

print(type({}))

OBS: Sobre dicionarios
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

"""
print('Dicionarios')
resp =''
while resp != 's':
    print('1-Crianções de Dicionarios')
    print('2-Acessando elementos')
    print('3-Encontrando Chave dentro do dicionario')
    print('4-Ultilizando qualquer tipo de dado')
    print('5-Adicionando elemento a um dicionario')
    print('6-Como remover dados de um dicionario')
    print('7-Testando no ecomerce basico e a diferenciação de tuplas lista e dicionario')
    print('8-Métodos de dicionario')
    escolha = int(input('Qual sessão você quer ver ? '))

    #Criação de dicionario
    if escolha == 1:
        print('Criaçao de dicionarios')

        # Forma 1 (mais comum)

        paises = {'br': 'brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
                # elemento 1        elemento 2                  elemento 3
        print(paises)
        print(type(paises))

        # Forma 2 (Menos Comum)

        paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

        print(paises)
        print(type(paises))

    #Acessando elementos
    elif escolha == 2:
        print('Acessando elementos')
        # via chave da mesma forma que via tupla/lista
        paises = {'br': 'brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
        # elemento 1        elemento 2                  elemento 3
        print(paises['br']) # Dicionario não tem indice e por isso ultilizamos a chave
        print(paises['py']) # cheve vem antes dos ":" caso vc queira uma chave que nao existe da erro

        # Acessando via GET - Recomendado
        print(paises.get('br'))
        print(paises.get('ru')) # ele nao da erro ele da NONE é um tipo sem tipo um vazio neutro
        print('faze de teste ')

        #teste
        pais = paises.get("br")# pegue o valor da chave 1 caso nao encontre nada envia a mensagem depois da virgula
        if pais == 'brasil':
            print(f'encontrei o  {pais}')
        else:
            print(f'encontrei alguma coisa {pais}')

        # teste 2
        print('fase de teste 2')
        pais = paises.get('ru','Lian Yu')# pegue o valor da chave 1 caso nao encontre nada envia a mensagem depois da virgula
        print(f'Encontrei {pais}')

    #Encontrando chave dentro do dicionario
    elif escolha == 3:
        print('chave Valor dentro do dicionario')
        paises = {'br': 'brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
        #           chave : elemento
        print('br' in paises) # OBS: temos a cheve aqui
        print('ru' in paises)
        print('Paraguai' in paises) # OBS tamos preocurando a chave não elemento

        if 'ru' in paises:
            russia = paises['ru']
            print(russia)
        elif 'br' in paises:
            rj = paises['py'] # passei o valor pro chave
            print(rj)
        else:
            print(Nome)

    # ultilizando qualquer tipo de dados
    # qualquer tipo: float, tuple, string int...
    elif escolha == 4:
        print('Ultilizando qualquer tipo de dado')
        localidades = { # tuplas são bastante interessante de serem usadas como chave de um dicionario
            (35.6895, 39.6974): 'escritorio em tokio ',
            (40.7154, 53.8523): 'escritorio em Nova York ',
            (99.1211, 22.5522): 'escritorio em São paulo '
        }
        print(localidades)
        print(type(localidades))

    #Adicionando elementos ao dicionario
    elif escolha == 5:
        receita = {'jan': 100, 'fev': 120, 'mar':300}
        print(receita)
        print(type(receita))

        # Forma 1 - Mais comum
        receita['abr'] = 350
        print(receita)

        #Forma 2
        novo_dado = {'mai':500}
        receita.update(novo_dado) # receita_update({"mai":500}) Ambos são a mesma coisa
        print(receita)

        # forma 3 teste com variaveis
        chave = input('digite o mês: ')
        valor = int(input('Digite o valor do mês: '))
        novo_dado = {f'{chave}': valor}
        receita.update(novo_dado)
        print(receita)

        #Atualizando dados do dicionario
        # forma 1
        receita['mai'] = 550
        print(receita)

        #Forma 2
        receita.update({'mai': 620})
        print(receita)

        #forma 3
        chave = input('digite o mês pra ser atualizado: ')
        valor = int(input('Digite o valor do mês pra ser atualizado: '))
        novo_dado = {f'{chave}': valor}
        receita.update(novo_dado)
        print(receita)

        #Conclusão 1: a forma de adicionar novos elementos e atualizar dados é a mesma
        #Conclusão 2: Em dicionario NÃO podemos ter chaves repetidas

    #Como remover dados de um dicionario
    elif escolha == 6:
        #Remover dados de um dicionario
        receita = {'jan': 100, 'fev': 120, 'mar':300}
        print(receita)

        #Forma 1 - forma mais comum
        ret = receita.pop('mar')
        #OBS: aqui precisamos sempre informa a chave e se nao encontrar o elemento o key erro e acionado
        print(receita)
        print(ret) # ao removemos um objeto o valor desse objeto é sempre retornado

        #Fomra 2
        del receita['fev'] # del = deletar
        print(receita) # se a chave não existir gera um keyerro
        # Neste caso aqui o valor removido não sera retornado

    #Imagine que voce tem um e-comerce
    elif escolha == 7:
        """
        carrinho de compras: 
        produto 1: 
            - nome
            - quantidade 
            - preço
        produto 2:
            - nome
            - quantidade
            - preco:
        """
        # Poderiamos ultilizar uma lista pra isso? sim
        carrinho = []
        produto_1 = ['playstation 5',1,1200]
        produto_2 = ['god of war',4,500]

        carrinho.append(produto_1)
        carrinho.append(produto_2)

        print(carrinho)
        # Teriamos que saber qual é o indice de cada informão no produto

        # 2- Poderiamos ultilizar tuplas pra isso? sim
        produto_1 = ['playstation 5',1,1200]
        produto_2 = ['god of war',4,500]

        carrinho = (produto_1,produto_2)
        print(carrinho)
        # Teriamos o mesmo problema que a lista, precisariamos saber qual indice pertence a cada informação
        # No entanto tuplas ela é imutavel e isso é bom

        # 3- Poderiamos ultilizar um dicionario?sim
        carrinho = []
        produto_1 = {'nome':'playstation 5', 'quantidade': 1, 'preço' : 2300}
        produto_2 = {'nome' : 'god of war 1/2/3/4', 'quantidade': 4,'preço' : 520}

        carrinho.append(produto_1)
        carrinho.append(produto_2)
        print(carrinho)
        # Desta forma facilmente adicionamos ou removemos produtos do carrinho
        # podemos ter a certeza sobre cada informação

    # Métodos de dicionario
    elif escolha == 8:
        d = dict(a = 1, b = 2, c = 3)
        print(d)
        print(type(d))

        # Limpar o dicionario (zerar dados)
        d.clear()
        print(d)

        #Copiando um dicionario pra outro
        # Forma 1- Deep Copy
        print('Forma 1- Deep Copy')
        d = dict(a = 1, b = 2, c = 3)
        novo = d.copy()
        print(novo)
        novo ['d'] = 4
        print(d)
        print(novo)

        #Forma 2- Shallow Copy
        print('Forma 2- Shallow Copy')
        novo = d
        print(novo)
        novo['e'] = 4
        print(d)
        print(novo)
        novo['v'] = 9
        print(d)
        print(novo)

        #Forma não usual de criação de dicionarios
        outro = {}.fromkeys('a','b') # Criando um dicionario aonde o A é a CHAVE e o B é o VALOR
        print(outro)
        print(type(outro))

        #O metodo fromkeys recebe dois parametros: um interavel e um valor
        # ele vai gerar para cada valor do interario uma chave e ira atribuir a esta chave e o valor informado
        usuario = {}.fromkeys(['nome','pontos','email','profile'], 'desconhecido')
        #                       [cahves,chaves,...              ] , valor das chaves
        print(usuario)
        print(type(usuario))

        veja = {}.fromkeys('teste','valor') # ele vai gerar para cada valor do interario uma chave e ira atribuiir a esta chave o valor informdo
        print(veja) # cada letra sera separada e o valor sera adicionado a elas
        # a menos que voce proteja com cohetes
        veja = {}.fromkeys(['teste'],'valor')
        print(veja)

        # podemos ate usar o ranger
        veja_rage = {}.fromkeys(range(1,11), 'novo')
        print(veja_rage)


    resp = input('Você quer sair [S/N]? ')

