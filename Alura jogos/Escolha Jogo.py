import  adivinhacao
import  Forca

print('Escolha seu jogo ')
print('(1)Jogo da forca (2) Adivinhação')

jogo = int(input('Qual Jogo você quer jogar ? '))

if(jogo == 1):
    Forca.Jogar_Forca()
elif(jogo == 2):
    adivinhacao.Jogar_Adivinhacao()