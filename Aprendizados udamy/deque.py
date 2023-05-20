"""
Módulo Colletions - Deque
Podemos dizer que o deque é uma lista de alta perfomace

"""

#import
from  _collections import deque
#criando deques
deq = deque('Victor')
print(deq)

#adicionando elementos no deque
deq.append('Moye') # a mesma coisa que lista inclusiver dar pra se usar o for normalmente
print(deq)

deq.appendleft('wayne')# adiciona no começo / tambem podemos usar no final
print(deq)

#remover elemento
print(deq.pop()) # remove e retorna o ultimo elemento mas tambem da pra fazer com o elemento iinicla
print(deq)
print(deq.popleft())# remove o primeiro elemento
print(deq)