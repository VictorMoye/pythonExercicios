"""
Filter

Filter()-> Serve para filtrar dados de uma determinadad coleção


valores = 1,2,3,4,5,6
media = (sum(valores) / len(valores))
print(media)
print(type(media))
"""

#Biblioteca para dados estatisticos
import statistics

#dados coletados te algum sensor
dados = [1.3,2.7,3,8,8.0,3.8,4,1,4.1,0.1,-1.6]

# calculando media dos dados ultilizando a funçao mean()
meida = statistics.mean(dados)
print(f'media: {round(meida,2) }')
print(type(meida))

# Assim como a funçao map() , a filter() recebe dois parametros sendo
# uma funçao e um interavel

res = filter(lambda  valor_dados : valor_dados  >= round(meida,2), dados )
print(f'res: {list(res)}')
print(f'res: {res}')
print(f'res: {type(res)}')


"""
resp =''
while resp != 'S':
    #biblioteca pra trabalhar com dados estatistico
    import  statistics
    dados = [1.3,4.4,7,45.89,6,6.52]

    #calculando as medias dos dados
    
    resp = input('sair do programa [S/N] -> ').upper()
"""