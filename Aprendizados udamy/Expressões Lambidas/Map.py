"""
Map

Com Maps fazemos mapeamento de valores para uma função
"""

resp = ' '
while resp != 'S':
    print('1- Aprendendo a suar o MAP')
    print('2- Outro exemplo')
    escolha = int(input('Quer ultilizar qual programa'))
    if(escolha == 1):
        import math


        def area(r):
            # Calcular a area de um circulo com raio R
            return round(math.pi * (r ** 2), 3)


        print(area(2))
        print(area(5.3))

        raios = [2, 5, 7.1, 0.3, 10, 44]
        areas = []
        for r in raios:
            areas.append((area(r)))

        print('Forma 1')
        print(areas)

        # Forma 2 - Map
        # Map é uma função que recebe dois parametros: o primeiro a função, o segundo um interavel Retorna um Map Object
        print('Forma 2')
        areas2 = map(area, raios)
        print(areas2)
        print(type(areas2))
        print(list(areas2))  # convertendo pra lista

        # Forma 3 - Map com Lambda
        print('Forma 3')
        print(list(map(lambda r: math.pi * (r ** 2), raios)))

        # OBS: Após ultilizar o map object depois da primeia  ultilização o MAP Zeera

    # Outro exemplo
    elif(escolha == 2):
        #Para fixar o MAP
        """
        Temos dados interaveis:
        daos: a1,a2,...an
        temos uma função: 
        Função: f(x)
        Ultilizamos a função ma(f,dados) onde map ira "Mapear" cada elemento dos dados e aplicar a função 
        O Map Object: f(a1), f(a2), f(...),f(an)
        """
        #Mais um exemplo
        cidades = [('Rio de janeiro', 41),('São paulo',29),('Rio grande do sul', 14),("petropolis",20)]

        print('Cidades e temperatura sem conversão')
        print(cidades)
        #F : 9/5 * c + 32
        Cecius_para_Feretchi = lambda dados: (dados[0],(9/5) * dados[1] + 32)

        print('Dados convertidos pra outra temperatura Farecht')
        print(list(map(Cecius_para_Feretchi,cidades)))
    resp = input('Quer sair do programa [S/N]-> ').upper()