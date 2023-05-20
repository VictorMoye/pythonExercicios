"""
Entendendo o * args
- O *args é um parametro como outro qualquer, isso significa que voce podera chamar com qualquer coisas
desde que começe com o *

Exemplo
Mas por convenção ultilzamos *args para defini-lo

Mas o que é o *args?

O parametro *args ultilizado em uma função coloca valores extras informados como
entrada em uma tupla, então desde já lembre-se que tuplas são imutaveis.

"""

#Exemplo
def soma_todos(num1,num2,num3):
    return num1 + num2 + num3
print(soma_todos(5,2,6))

#Entendo o *ARGS

def soma_todos_numeros(*args):
    print(args)

soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(1,2,3,4)
soma_todos_numeros(1,5)

def soma_numeros(*args):
    return sum(args) #as duas tem a mesma função no entanto como args retorna uma tupla é preferivel que voce economize cod e faça o mais simples
    """total = 0
    for numeros in args:
        total += numeros
    return total"""

print(soma_numeros())
print(soma_numeros(1,2,3))
print(soma_numeros(2,3))
print(soma_numeros(2,2,5,6,5))

#Outro exemplo de usar args
def verificar_info(*args):
    if 'Geek' in args and 'University' in args:
        return f'Bem vindo Geek {args}'
    return f'Eu não lhes conheço {args}'
print(verificar_info('Geek','University'))
print(verificar_info(1,True,'University','Geek'))
print(verificar_info(1,'University',3,14,3.145))

def soma_numero(*args):
    totsl = 0
    for cont in args:
        totsl += cont
    return totsl
print(soma_numeros())
print(soma_numeros(1))
print(soma_numeros(1,3))
print(soma_numeros(1,2,3))
print(soma_numeros(4,25,6.16,4.4,3.154236))
# o mesmo exemplo so que em baixo e bem mais curto pra comparação

def soma_numeros2(*args):
    return sum(args)
print(soma_numeros2())
print(soma_numeros2(1))
print(soma_numeros2(1,3))
print(soma_numeros2(1,2,3))
print(soma_numeros2(4,25,6.16,4.4,3.154236))

numeross = [1,2,3,5,6]
#print(soma_numeros2(numeross))
#Não  da certo pois a lista se torna uma tupla e ele entende que todos os numeros são apenas um elemento e nao uma lista de elementos
#A menos que voce desempacotar os numetos
#Desempacotando os numetos
print(soma_numeros2(*numeross))# pra desempacotar basta usar o *



