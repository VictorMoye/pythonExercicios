"""
Módulo Collections - Counter(contador)
Collections -> High-performace Container Datatypes

Conter -> Recebe um interalvel com parametro e ria um objeto do tipo collection conuter que é parecido
com um dicionari, contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento.

"""

resp = ''
while resp != 's':
    print('1-Ultilizando o counter')

    escolha = int(input('Digite a sua escolha?'))
    #Ultilizando o counter
    if escolha == 1:
        from collections import  Counter
        #Podemos ultlilizar qualquer interavel aqui usamos uma lista
        lista = [1,1,2,2,3,3,3,2,2,1,2,3,22,5,5,6,9,9,23,23,46,646,46,94,9]
        #ultilizando o counter
        res = Counter(lista)
        print(type(res))
        print(res)
        #Counter({2: 5, 3: 4, 1: 3, 9: 3, 5: 2, 23: 2, 46: 2, 22: 1, 6: 1, 646: 1, 94: 1})
        #para cada elemento ele criou uma chave e colocou o numero de ocorrencias que os numeros se repetem

        #Exemplo 2
        print(Counter('Victor moye wayne')) # inclusive caractere ele faz a mesma coisa

        #Exemplo 3
        texto = """
        O que é Lorem Ipsum?
        Lorem Ipsum é simplesmente um texto fictício da indústria tipográfica e de impressão. 
        Lorem Ipsum é o texto fictício padrão do setor desde os anos 1500, quando uma impressora 
        desconhecida pegou uma galera do tipo e a mexeu para fazer um livro de amostras do tipo.
        Ele sobreviveu não apenas cinco séculos, mas também o salto para a composição eletrônica, 
        permanecendo essencialmente inalterado. Foi popularizado na década de 1960 com o lançamento 
        de folhas de Letraset contendo passagens de Lorem Ipsum e, mais recentemente, com software de 
        editoração eletrônica como o Aldus PageMaker, incluindo versões do Lorem Ipsum.
        """
        palavras = texto.split()

        print(palavras)

        res = Counter(palavras)
        print(res)

        #econtrando as 5 palavras mais ocorrencias do texto
        print(f'As palavras com mais ocorrencias \n{res.most_common(5)}')
    resp = input('Quer sair do programa [S/N]? ')