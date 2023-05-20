"""
LISTAS
 Listas em python funcionam como vetores ou matrizes (ARRAYS)
 Eles sao dinamicos e podem colocar QUALQUER tipo de dados.

 Linguagemns C/JAVA: ARRAYS
  - Eles nestas linguagem possui tipo e linguagem fixa.

  Python:

 -Dinâmino: não possui tamanho fixo, podemos criando listas e sair tacando elementos enquanto tiver tamanho na memoria.
 -Qualquer tipo de dados: nao possui um tipo de dado fixo pode ser usar qualquer tipo de dado dentro dela.

 As listas em Python sao representadas por cohcetes []

type([])
listaNum = [1,2,3,4,5,6,7,8,9,10,'/']
lista = [1,1,99,56,94,556,46,9,10,11,23]
lista2 = ['V','i','c','t','o','r','','M','o','y','e']
lista3 = []
lista4 = list(range(23))
list5 = list('Victor Moye da Silva')
lista6 = ['python','csharp','java']

#podemos colocar qualquer tipo de dado dentro de uma lista inclusive misturando esses tipos de dados
lista7 = [1,2.34,True,'Victor','m',[1,2,3],9999999,8*9,listaNum *2,lista2,'\n', list5 + lista6]
print(lista7)



# Podemos checar se determinado valor esta contindo na lista

num = int(input('qual numero que voce quer encontrar?'))
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

# podemos facilmente ordena uma lista

lista.sort() # primeiro voce ordena a lista  "EVITANDO O ERRO NONE"
print(lista) # depois voce imprimi ela pronta

# Ordenando a lista de string

lista2.sort() # Primeiro voce ordena
print(lista2) # depois voce imprimi

# contando facilmente a ocorrencia que ocorre dentro de uma lista

print(lista.count(1))# dentro do cont eu tou contando quantos numeros 1 eu tenho ou o numero que eu bootar dentro dos ()
print(list5.count('i')) # aqui tou vendo quantas letras eu tenho poderia botar outras dentro do cont acrescentando dentro do ()


# adicionando elementos em listas  usando a funçao append

Usando a funçao append so conseguimos adicionar um elemento por vez
caso voce queira adicionar mais elementos tera que ultilizar um laço de repetiçao 

print(f'os elementos da lista 1 {lista}')
lista.append(46)
print(f'elemento 46 adicionado: \n{lista}')

# adicionando uma lista dentro de outra


print(f'Lista antes de ter uma lista dentro \n{lista}')
lista.append([9,16,18,19,20,23,46,943,563,46,94,100]) # coloca apenas um elemento na lista e ser for colocar mais, ira colocar como uma lista dentro de outra SUBLISTA
print(f'Lista apos por outra lista dentro \n{lista}')

if [1, 1] in lista: # ele nao vai encontrar qualque numero avulso
    print('Encontrei os numeros!!')
else:
    print('Não encontrei nada!!')
 
 
isso só é possivel graças a teoria de que uma lista pode ser er qualquer tipo de dados de qualque tipo 
encontrada la no topo


# fazendo o tesste de uma lista com dois tipos de dados

listaTeste = [1,2,3,6] # fazendo a lista de numeros

listaTeste.append('v') # tem como voce por uma string em uma lista de de numeros

print(listaTeste) # incrementando uma string a essa lista de numero.


listaTeste.extend([1,2,3,4,5,'v','i','c','t','o,','r']) # colocar varios elementos dentro da lista sem criar uma SUBLISTA.

print(f'lista apos o extend {listaTeste} \n diferente de {lista}')


print('Dados invertidos: ')
lista.reverse()# usando a função reverse para inverte os dados dentro da lista
lista2.reverse()# usando a função reverse para inverte os dados dentro da lista
print(lista)
print(lista2)
print(list5[:: -1])# usando a função slice para inverte os dados [:: -1]" começando do zero indo ate o final inverte"
print(lista4[:: - 1])  # usando a função slice para inverte os dados [:: -1]"començando do zedo indo ate o final inverte"


A funçao reverse ela inverte definitivamente a funçao
caso voce use a metodologia slice ela ira inverte o invertido e voltara ao normal, Pórem caso voce use a funçao de novo 
ela estara invertida pela funçao 
Pois a função slice inverte ela na hora do print temporariamente 

# copiando dados de uma lista em outra

print('Lista original')
print(list5)
print('Lista inversa com a funçao REVERSE')
list5.reverse()
print(list5)
print('Lista invertida com a funçao slice')
print(list5[:: -1])
print('Copiando uma lista na outra:')
listaCop = list5.copy()
print(listaCop)

# podemos contar quantos elementos temos dentro de uma lista usando a funçao LEN

print('Usando a funçao LEN para saber quantos elementos temos dentro da lista')
print(f'Lista {lista}')
print(len(lista))
print(f'Lista 2: {lista2}')
print(len(lista2))
print(f'lista3: {lista3}')
print(len(lista3))
print(f'lista4: {lista4}')
print(len(lista4))
print(f'lista5: {list5}')
print(len(list5))

# podemos excluir ou remover o ultimo elemento dentro de uma lista usando a funão pop

print('Lista 5 antes da função pop')
print(list5)
list5.pop()
print('Lista 5 depois da função pop')
print(list5)

# podemos tambem usar escolher qual elemento tirar atraves desta mesma funçao basta indicar qual posiçao voce quer tira por meio de numeros

print('lista num antes de indicara a posiçao 5')
print(listaNum)
print('lista num depois de indicar a posiçao 5')
print(f'O numero que esta na posiçao 5: {listaNum.pop(5)} \nConfere:')
print(listaNum)

print('lista de palavras')
print(lista6)
lista6.pop(1) # o elemento que a funçao tira sao os que estao entre as aspas ou separados por virgula,
print('apos usar para tira um elemento que esteja dentro das aspas')# uma palavra que esteja entre aspas ele vai tirar a palavra inteira pois considera um so elemento
print(lista6)

# podemos zera a lista e todos os elementos contidos nela
print('lista 5 e todos os seus elementos')
print(list5)
print('apos usar a funçao clear para limpa a lista 5')
list5.clear()
print(list5)

# usando em lista com videversos elementos
print('lista cheia 1')
print(listaNum)
listaNum.clear()
print('lista apos clear')
print(listaNum)


# podemos repetir elementos em dentro de uma lista

print('Lista nova de teste:')
listaNova = [1,2,3,'/']
print(f'Lista nova: {listaNova} do tipo :{type(listaNova)}')
listaNova = listaNova * 3
print(f'Lista nova de teste triplicada: {listaNova} do tipo: {type(listaNova)}')

print(f'Invertendo a variavel convertida: {curso[:: -1]}')
print(f'Contando quantos elementos existe dentro da nova lista: {len(curso)}')
print(f'Excluindo {curso.pop(2)} da lista: \n {curso}')
print(f'Excluindo todos os elementos dentro da lista: \n Lista antes {curso}')
curso.clear()
print(f'Lista depois: {curso}')
print(f'Colocando um elemento dentro da lista: {curso.append(input("Digite um dado: "))}')
print(f'Imprimindo Nova lista: {curso}')
print(f'Adicionando varios elementos de diversos tipos na nova lista: {curso}')# na verdade acho que deveria usar no laço for

c = int(input('Informe quantos elementos voce quer na lista: ')) # quantos elementos voce quer na lista
for i in range(1,c + 1): # contadora para ir ate o numero desejado (+1)p/alcançar o numero desejado
    curso.append((input('Informe um tipo de elemento'))) # adicionando um elemento de cada vez

print(curso) # imprimindo a lista com todos os elementos prontos

print(f'Colocando uma nova lista determinada {lista2} dentro da antiga lista {curso}: ')
print(f'{curso + lista2}')

print(f'Colocando uma subLista dentro de outra lista: ')
curso.append(listaNum) # a funçao append pega um argumento ou variavel e adiciona em forma de sub lista , ja extend adiciona dentro da lista
print(curso)

print(f'Multiplicando os elementos dentro de uma lista: ')
print(listaNum)
print(listaNum * 2)

print(f'Pegando uma frase qualquer é trasnformando em uma lista: ')
frase  = input('Digite sua frase: ')
frase = frase.split()
print(frase)
print(f'copiando os dados de uma lista em outra:')
print(f'o que tinha antes {lista}')
lista = listaNum.copy()
print(f' depois {lista}')

# Convertendo strings frases textos ou dados em Listas

curso = 'Programaçao em python avançada '
print(f'Imprimindo a variavel curso em string: {curso}')
curso = curso.split() # usando a funçao split para converte o dado em Lista
print(f'Variavel convertida: {curso}')
OBS: SPLIT(,) // colocando uma viirgula ou qualquer dado dentro dos parenteses a funçao ira entender que o separador padrao
e a virgula ou o elemento que estiver dentro dos parenteses



# convertendo uma lista em string

print(f'Lista de numeros antes da conversão: {lista6}')
lista9 = ''.join(lista6)
print(f'Lista num depois da conversão: {lista9}')
print(lista2)
lista9 = '  '.join(lista2) #funciona primeiro um objeto recebe a lista desejada e o join converte, porem antes da conversao
# abresse uma aspas e tudo que tiver dentro das aspas ira ser o separador da string e dentro do JOIN vai a lista que sera convertida em string
print(lista9)

print(f'Lista 6 usando o separador sifrao de dinheiro \n Atualmente: {lista6}')
lista9 = '$'.join(lista6)
print(f'DEPOIS: {lista9}')

# Exemplo FOR
soma = 0

for elemento in lista4: # elemento valendo 0 indo ate o final da lista
    print(f'Elemento: {elemento}') # cuspindo o elemento
    soma = soma + elemento # somando todos os elementos e somando tudo em soma
print(f'A soma de todos os elementos foi = {soma}') # cuspindo a soma total fora do loop

# exemplo 2 usando o while
carrinho = []
produto = ''

while produto != 'sair': # quando a condiçao for diferente de sair ou seja verdadeira ela entra no loop
    print('Adicione um produto qualquer a lista: ')
    produto = input() # inserindo um elemento em produto
    if produto != 'sair': # entrando no laço caso a condiçao seja verdadeira se for falsa ela nao entra e sai do loop
            carrinho.append(produto) # quando eu digitar uma sair a condiçao la em cima sera falsa O produto deixara de ser diferente de sair e ai sairia do llop
for produto in carrinho: # varrendo a lista carrrinho toda ate o final e cuspindo o resultado fora
    print(produto)

# ultilizando valores fixos e variaveis dentro da lista

numeros = [1,2,3,5]

print(numeros)

num = 1
num2 = 2
num3 = 3
num4 = 5
numer = [num,num2,num3,num4]
print(numer)


# fazendo acesso aos elementos de formas indexada

#          0       1        2       3
cores = ['verde','azul','branco','amarelo']

print(cores[0]) # verde
print(cores[1]) # azul
print(cores[2]) # branco
print(cores[3]) # amarelo

# fazendo acesso de forma indexada e inversa

imagina alista como uma roda, se voce vai pelo caminho inverso voce pega
o ultimo elemento de tras para frente
se for por negativo a lista ira percorre de tras para frente ate o primeiro numero que seria o ultimo
"""

"""
# revisão de slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]


print(cores[-1]) # amarelo
print(cores[-2]) # branco
print(cores[-3]) # azul
print(cores[-4]) # verde



for cor in cores:
    print(f'Lista: {cores}') # cuidado com o que voce declara aqui voce ta pedindo para prunta a lista
    print(f'Elementos: {cor}')# aqui voce ta printando a variavel que esta na posiçao 0 e ira ate o fim da lista mostrando os elementos

print('------------------------')
contadora = 0
while contadora < len(cores):
    print(f'Elemento: {cores[contadora]}')
    contadora = contadora + 1

# gerando indice em um for

for cont, cor in enumerate(cores): # gerando um numero no cont para indentificar qual posiçao pertence a posiçao cor dentro da lista cores
    print(cont, cor)# sem a contadora iria tudo para uma lista
    
    
cores = ['verde','azul','branco','amarelo']
numeros = [1,2,3,4,5,6,7,8,9,10]
#em qual indice ou posiçao da lista esta o valor/ elemento 6
print(numeros.index(6))

# escolhendo um elemento para pesquisar a posiçao na lista de 1 à 10

resp = int(input('Escolha um elemento na lista para saber a posição de 1..10: '))
print(f'O elemento {resp} esta na posição: {numeros.index(resp)}')




# trabalhando com slice de lista  com o parametro no inicio
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[1:]) # iniciando da primeira posição e imprimindo o da segunda posiçao em diante

# trabalhando com slice da lista com o parametro no final
print(lista[::-1]) # so pega um valor determinado

# trabalhando com lista com parametro fim
print(lista[:2])# so pega ate a segunda posição

# trabalhando com lista e o parametro restante
print(lista[1:])# so pega o segundo elemento para cima

# trabalhando com lista pegando de um elemento definido e indo ate o outro definido
print(lista[1:3]) # indo de 0 ate 2

# trabalhando com elementos de 2 em 2
print(lista[1::2])# começa de 1 e vai ate o final em 2 em 2

# trabalhando com lista indo do 0 ate o final em 2 em 2
print(lista[::2])

# invertendo valores em um lista
nome = ['Victor ', 'Moye']
print(nome)
nome[0], nome[1] = nome[1] , nome[0]# presta atençao o elemento 0 esta recebendo o elemento 1, e o elemento 1 esta recebendo o elemento 0
print(nome)

# Soma, valor maximo, valor minimo,tamanho
# somente se os valores forem todos inteiros ou reias

lista = [ 1,2,3,4,5,6,7,8,9]

print(f'Somando todos os valores da lista {sum(lista)}') # soma
print(f'Achando o valor maximo da lista {max(lista)}') # maximo valor
print(f'Achando o valor minimo da lista {min(lista)}') # minimo valor
print(f'Mostrando o tamanho da lista {len(lista)}') # retorna o tamanho da lista


# transformando uma lista em tupla
lista = [ 1,2,3,4,5,6,7,8,9]

print(f'Lista: {lista}')
print(f'Tipo da lista: {type(lista)}')

tupla = tuple(lista)
print(f'Imprimindo a tupla: {tupla}')
print(f'Confirmando o tipo da tupla: {type(tupla)}')


"""
type([])

# Desempacotamento de lista
lista = [1,2,3]

num1, num2, num3 = lista # desempacotamento cada variavel ira receber um elemento da lissta de acordo com a fila
# o desempacotamento so funciona quando tem o numero de variaveis o suficiente para cada elemento da lista

print(num1)
print(num2)
print(num3)




"""
criando uma lista com multiplos dados diferentes 
ordenando a lista usando a funçao SHORT()
checar se determinado valor esta contido dentro da lista 
contando quantos elementos repetidos eu tenho dentro da classe COUNT(O que eu quero pesquisar)
lendo uma lista de tras para frente (:: -1) ou reverse()
contando quantos elementos existe dentro da lista LEN(VARIAVEL)
excluir um elemento na lista e mostrando na tela o que foi excluido 
zerando todos os elementos de dentro da lista
colocando varios elementos dentro da lista 
colocando uma lissta dentro de outra lista
zerando a lista e todos os elementos contidos nela
multiplicando o elemento dentro da lista atraves de operaçao basica
converte uma string em uma lista 
copiando uma lista
convertendo uma lista em sttring 
cirando uma lista com multiplos dados diferentes 
interando uma lista com o while e for 
ultilizando variaveis em listas
fazendo acesso de forma indexada e indexada inversa
enumerando os elementos com enumerates 
pesquisando em qual posição esta o elemento
imprimindo elemento de 2 em 2 
começando de tras para frente 
pegando apenas um elemento em uma determinada posiçao 
pegando elemento ate uma determinada posiçao 
pegrando elemento da posiçao determinada ate o fim 
pegrando elemento de uma determinadad posiçao ate outra determinanda posição 
invertendo valor da lista com string o elemento 2 vai para a posição 1 e, 1 vai para a posição 2
pegando o valor maximo da lista 
pegando o valor minimo da lista 
somando todos os valores da lista 
pegando o tamanho da lista 
tem coisas relacionada a ista que da para pesquisar que nem no excel
transformando uma lista em tupla 


"""

