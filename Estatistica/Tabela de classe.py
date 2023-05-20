import random
num = random.randint(1,10)

#adicionando os dados dentro do rol
rol_da_postila = [14, 12, 11 ,13, 14, 13,
12 ,14, 13, 14, 11, 12,
12, 14, 10 ,13, 15, 11,
15, 13, 16, 17, 14 ,14,
15 ,16 ,13, 12 ,11 ,15]
#adicionando os dados dentro do rol

print(f'total de rol: {len(rol_da_postila)}')
for i in range(10,18):
    print(f' {i} tem {rol_da_postila.count(i)}')

#frequencia relativa
print('frequencia raltiva')
c=0
for i in range(10,18):
    print(f' {rol_da_postila.count(i)} relativa {((rol_da_postila.count(i) / len(rol_da_postila)) * 100):.0f} %')
    c +=((rol_da_postila.count(i) / len(rol_da_postila)) * 100)
print(f'{c:.0f}')

#frequencia relativa aculmulada
for i in range(10,18):
    c += ((rol_da_postila.count(i) / len(rol_da_postila)) * 100)
    print(f' {((rol_da_postila.count(i) / len(rol_da_postila)) * 100):.0f} % relativa aculmulada { round(c) - 100} %')
