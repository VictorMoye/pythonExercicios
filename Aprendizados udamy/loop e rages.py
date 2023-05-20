"""
Loop FOR
 Loop -> estrutura de repetiçao
 For -> Uma dessas estruturas

Ultilizamos loop para interar sobre sequentcia ou sobre valores interaveis

Exemplos de intereaveis
- String
    nome - "nome"

 - lista
    lista = [1,3,5,7,9]

 - Range
    numeros = range[1,10]


"""
# Exemplo de for 1
nome = 'victor hugo'
lista = [1,3,5,7,9]
teste = range(1,10) # temos que tranforma em uma lista


for letra in nome: # interando em string
    print(letra)

for numero in lista: # inteirando em lista
    print(numero)

for teste in range(1,10):
    print(teste)

print('outros testes \n')

for Indice, letra in enumerate(nome):
    print(nome[Indice])

for letras in enumerate(nome):
    print(letras)


qtd = int(input('Digite o valor do Loop: '))

for cont in range(1,qtd):
    print(cont)

# fazendo emoji // da para se fazer qualquer tipo de emoji pegando o cod dele na internet e disponobilizando em uma variavle atribuida

for num in range(1,10):
    print('\U0001F60D' * num)
"""
Ranges

- Precisamos conhecer os ranges para ultilizar os loops

FORMAS GERAIS

    range(_valoe de parada_)
OBS: valor de parada nao inclusive(inicio padrao 0 e passo de 1 em 1)

"""