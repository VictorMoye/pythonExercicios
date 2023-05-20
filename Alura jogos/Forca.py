def Jogar_Forca():
    print('Bem vindo ao jogo da forca')
    palavra_secreta = 'Banana'
    enforcou = False
    acertou = False

    #Enquanto não acerta e nao enforcou
    while(not enforcou and not acertou):
        print('Jogando')
        chute = input('Qual a letra ? ')
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print(f'Encontrei a letra {letra} na posição {index}')
                index = index + 1
    print('Fim de jogo')