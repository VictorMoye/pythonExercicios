"""
Conjuntos
 - Conjuntos em qualquer linguagem de programação estamos fazendo referencia a teoria dos conjuntos da matematica
 - Aqui no python os conjuntos são chamados de Sets
 - Da mesma forma que na matemacia os Sets(conjuntos) não possuem valores duplicados
 - valores e elementos não são acessados via indice, ou seja, conjuntos não são indexados:
 - Sets(Conjuntos) não possuem valores ordenados

Conjuntos são bons para se ultilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados

Os Conjuntos (sets) são referenciados em python com chaves{}
Diferença entre Conjuntos(Sets) e Mapas(Dicionairo) em python
    - Um dicionario tem  chave/valor
    - um conjunto tem apenas valor
"""
print('Conjunto')
resp = ''
while resp != 's':
    print('1-Definindo um Conjunto')
    print('2-Verificando se determinado elemento esta contido no conjunto')
    print('3-Alocando dados e usando o for')
    print('4-Usos interessantes com SETs')
    print('5-Adicionando elementos a um conjunto e removendo ele ')
    print('6-Copiando um conjunto pra outro !! ')
    print('7-Metodos matematicos de conjuntos')

    escolha = int(input('Escolha qual ação você quer vê: '))

    # Definindo um conjunto:
    if escolha == 1:

        #Forma 1
        s= set({1,2,3,4,5,5,6,7,2,3})
        print(s)
        print(type(s)) # Note que não sera impresso os numeros repetidos
        # ao criar um conjunto com o valor ja existente ele sera ignorado e não dara erro

        #Forma 2 - Mais comum

        s= set({1,2,3,4,5,5})
        print(s)
        print(type(s))

        # A mesma coisa acontece com uma string
        texto = set({'Dicionario hells array', 'v','v','a','b'})
        print(texto)
        print(type(texto))

        # mesmo uma tupla ele nao se petete os valores
        tuple = {1,2,3,3,6,5,4,2,5,6}
        print(f'tuple {tuple}')
        print(type(tuple))
        s = set({tuple})
        print(s)
        print(type(s))

    elif escolha == 2:
        # verificando se determinado elemento esta contido no conjunto
        s = {1, 2, 3, 4, 5, 5}
        print(s)
        print(type(s))
        if 3 in s:
            print('tem 3')
        else:
            print('não tem 3')


        #Importante não tem ordem em conjunto que nem há em lista
        dados = 99, 2, 34 ,23, 23 ,9 ,9 ,46 ,46 ,12 ,1 ,44, 5
        #Lista aceita valores duplicados
        lista = list(dados)
        print(f'Lista: \n{lista} \nCom {len(lista)}')
        print(type(lista))
        #tuplas aceitam valores duplicados
        tupla = tuple(dados)
        print(f'Tupla: \n{tupla} \nCom {len(tupla)}')
        print(type(tupla))
        #dicionairo não aceitam chaves duplicadas
        dicionario = {}.fromkeys(dados, 'dict')
        print(f'dicionario: \n{dicionario} \nCom {len(dicionario)}')
        print(type(dicionario))
        # conjuntos não aceitam valores duplicados
        conjunto = set(dados) # conjunto nao tem ordenação ela é feita de forma auta e aleatoria
        print(f'Conjunto: \n{conjunto} \nCom {len(conjunto)}')
        print(type(conjunto))


    elif escolha == 3:
        #Assim como todo conjunto python podemos olocar tipos de dadso misturados
        s = {1, 'b', True, 3,9, 4,False, 5, 5}
        print(s)
        print(type(s))

        #Podemos interar em um set normalmente
        for valor in s:
            print(valor)

    #Usos interessantes com os sets
    elif escolha == 4:
    # Imagine que fizemos um formulario de cadastro de visitantes em um museu
    # os informantes informam manualmene a cidade de onde vieram
    # Nos adicioanmos os visiotantes  e uma lista python, ja que em uma lista podemos adicionar novos elementos
    # podemos ter repetição
        cidades = ['belo horizonte','são paulo', 'são paulo','campo grande','rio de janeiro', 'cuiaba','pombos','recife'] # detalhe que mesmo o ~ altera a variavel e ai por causa disso o valor e duplicado mesmo sem querer
        print(f'cidades: \n{cidades}  ')
        print(f'{len(cidades)} pessoas diferentes')
    #agora quantas cidades unicas e distintas temos ?
    # podemos ultlizar o set pra isso
        print(f'{len(set(cidades))} cidades diferente')
        print(f'Cada qual residente de \n{set(cidades)}')

    #Adicionando elemento a um conjunto e removendo ele
    elif escolha == 5:
        s = {1,2,3}
        print(s)
        s.add(4)
        s.add(4)
        s.add(6)
        print(s)
        for cont in range(0,5):
            s.add(input('Digite um novo elemento'))
        print(s)

        #remover
        #Forma 1
        s.remove(3) # não é indice, informamos valor a ser removido
        print(s) # conjunto não são indexados por isso nao funciona o indice
        # OBS caso o valor não seja encontrado sera gerado um valor keyErro

        #Forma 2
        s.discard(2) # se o valor não for encontrado nenhum erro é gerado
        print(s)

    #Copiando um conjunto pra outro conjunto
    elif escolha == 6:
        novo = {1,2,3}
        #Forma 1 - DEEP cOPY
        novo_conjunto = novo.copy()
        print(novo_conjunto)
        #nesta forma voce ler dois elementos totalmente separados
        
        print(f'Adicionando valor ao conjunto novo')
        for cont in range(0,5):
            novo.add(input('Digite um valor ao conjunto novo: '))
        novo_conjunto = novo.copy()
        print(f'Imprimindo o conjunto novo: \n{novo} \nE o conjunto novo conjunto \n{novo_conjunto}')
        print('Agora fazendo de forma inversa \n')
        while cont <= 2:
            novo_conjunto.add(input('Digite um valor ao conjunto novo'))
            cont += 1
        novo_conjunto = novo.copy()
        print(f'Imprimindo o conjunto novo: \n{novo} e o conjunto novo conjunto \n{novo_conjunto}')

        #Forma 2 - Shallow Copy
        s = novo
        s.add(4)
        print(novo)
        print(s)

        # Podemos remover todos os elementos de apenas uma unica vez
        print(novo.clear())
        print(novo)
        print(novo_conjunto)

    # Metodos matematicos de conjuntos
    elif escolha == 7:
    #imagine 2 conjuntos de python e java
        estudante_python = {'marcos','patricia','julia','victor','ellen','pedro', 'isabelle'}
        estudante_java = {'fernanda','victor','patricia','guilhermina','ana','dora'}

        #veja que alguns alunos estudam python tambem estuda jaba

        #gerando conjuntos de nomes unicos
        #Forma 1 -Union
        unicos1= estudante_python.union(estudante_java)
        print(unicos1)

        #Forma 2 - Ultilizando o caractere pipe |
        union2 = estudante_python | estudante_java
        print(union2)

        # gerando conjunto de estudandes que estao em ambos os curos
        #Forma 1 ultilizando intersection
        ambos1 = estudante_python.intersection(estudante_java)
        print(ambos1)
        #Forma 2 - Ultilizando o &
        ambos2 = estudante_python & estudante_java
        print(ambos2)

        #gerando um conjunto de estudantes que nao estao no outro
        so_python = estudante_python.difference(estudante_java)
        print(so_python)

        so_java = estudante_java.difference(estudante_python)
        print(so_java)

        #soam valor maximo valor mininno tamanho
        # se os valores forem sempre reias ou inteiros
        s= {1,2,3,4,5,6,7,8,9}
        print(sum(s))
        print(max(s))
        print(min(s))
        print(len(s))


    resp = input('Quer sair do programa [S/N]? ')