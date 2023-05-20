"""
Defininfo Funções
- Funções sao pequenos trechos de codigo que realizam uma tarefa especificas:
- Pode ou nao receber entradas de dados e retornar uma saida de dados:
- Muito uteis para executar procedimentos similares por repetidas vezes:

OBS: Se você escrever uma função que realiza varias tarefas dentro dela:
é bom fazer uma vereficação para que a função seja simplificada.
Já ultilizamos várias funções  desde que iniciamos este curso:
-print()
-len()
-max()
-min()
-count()
- e muitas outras

"""

# Exemplo de ultilização de funções

#cores = ['verde','amarelo','azul','branco']

#ultilizamos a função integrada (Built-in) do python print()

#print(cores)

#curso = 'Programação em python : Essencial'
#print(curso)

#cores.append('Roxo')
#print(cores)

#curso.append('Mais dados...') #Attribute Error ou seja erros de atributos

#Principio DRY - Don't Repeat Yourself  - Não repita voce mesmo /não repita seu codigo

"""
Em python a forma geral de definir uma função é : 
def nome]_Da_funcao(parametros_de_entrada):
    bloco da função 
    
Onde: 
nome_da_função -> SEMPRE, Com letras minusculas, e se for nome composto, separado por underline (Snake Case)
parametros de entradas -> Opcionais,onde tendo mais de um cada um separados por virgula, podendo ser opcionais ou não:
bloco de função -> Tambem chado de corpo da função ou implementação, é onde o processamento da função acontece 
Neste bloco pode ter ou não um retorno da função. 

Obs: Veja que para definir uma função ultilizamos a palavra reservada 'def' informando ao python que estamos definindo 
uma função. Tambem abrimos o bloco de codigo com o já conhecido dois pontos: que é ultilizado em python para definir blocos 

"""

#Definindo a primeira função
def diz_oi():
    print('Olá Mundo Python !!')
    print('Oi!')
"""
OBS:
1- veja que dentro da nossa função podemos ultilizar outras funções
2- veja que nossa função so executa uma tarefa ou seja a unica coisa que ela faz é dizer OI 
3- Veja que essa função não recebe nenhum parametro de entrada
4- Veja que essa funçao nao retorna nada
"""

#Ultilizando a funçao OI
diz_oi() #chamada de execução

def cantar_parabens():
    print('Parabens pra você')
    print('...')

#exemplo 2
cantar_parabens()

"""for cont in range(0,4):
    diz_oi()
    cantar_parabens()"""
#Em python podemos criar uma variavel do tipo da nossa função e executar esta função atraves da variavel

#Exemplo
cantar = cantar_parabens
respeito = diz_oi
respeito()
cantar()