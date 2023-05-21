""""
Reduce
OBS: Aparti do python 3+ não pertence a função integrada do python

Para entender o reduce()

filter

36

17

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

E você tem uma função que recebe dois parámetros:

def funcao(x, y): return x = y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce (funcao, dados)

A função reduce(), funciona da seguinte forma: Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado. Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passol mais o terceiro elemento e guarda o res.

Isso é repetido até o final. Passo 3: res3 = f(res2, a4)

Passon: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final, reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

funcao (funcao (funcao (a1, a2), a3), a4), ...), an)
"""
# ultilicando Reduce para multiplicar os numeros da lista
# importando reduce
from functools import reduce
dados = [1,1,2,3,5,5,6,4]
# para usar precisamos de uma função que receba dois parametros
multi = lambda parametroMulti , parametroDados : parametroMulti * parametroDados
res = reduce(multi,dados)
print(res)
# fazendo o mesmo ultilzando um loop normal
resp = 1
for contadora in dados:
    resp =  resp * contadora
print(resp)



