"""
Escreva um algoritmo que calcule os quadrados e cubos dos números de 0 a 10
e imprima os valores resultantes no formato de tabela, como segue:
e imprima os valores resultantes no formato de tabela, como segue:
Número Quadrado Cubo
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
10 100 1000
"""
import  math
for contadora in range(1,11):
    print(f"contadora: {contadora} quadrado: {contadora * contadora} cubo: {(contadora * contadora) * contadora}")