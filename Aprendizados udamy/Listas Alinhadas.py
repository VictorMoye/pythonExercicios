"""
Listas Aninhadas (Nested Lists)
 - Algunsas linguagens de programação possuem essa estrutura de dados chamados arrays
 - Unidimensional Array ou vetores
 - Multidimensional Matrizes

 Em Python temos a lista
 numeros = [1,'b',True , entre outros na mesma lista coisa que as  outra linguagens nao comportam

"""
#Exenplo

listas = [[1,2,3],[4,5,6],[7,8,9]] # matriz

#Interando com as listas
print('exempllo 1')
for lista in listas:
    for num in lista:
        print(num)

#List comprehension
print('exempllo 2')
[[print(valor) for valor in lista] for lista in listas]

#gerando um tabuleiro 3x3
print('tabuleiro 3x3')
tabuleiro = [[numero for numero in range(0,4)] for valor in range(0,4)]
print(tabuleiro)

#gerando jogadas pra jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1,4)]for valor in range(1,4)]
print(velha)

#gerando valores iniciais
print([["*" for i in range(1,4)] for j in range(1,4)])