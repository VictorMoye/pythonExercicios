"""
List Comprehension

-Utilizando List Comprehension nos podemos gerar novas Listas
com dados processados aparti de outro interavel

# Sintaxe da list COM.
[ Dado for dado in interavel]

"""

resp = ''
while resp != 'S':

    print('1- Entendendo o basico')
    print('2-Usando função')
    print('3-List comprehension VS Loops')
    print('4-Usando com nomes ')
    print('5-Usando com Loops')
    print('6- Adicionando estrutura condicionais e logicas')
    escolha = int(input('Qual voce quer ver em ação -> '))

    if(escolha == 1):
        # exemplo 1
        numeros = [1, 2, 3, 4, 5, 6]
        res = [numeros * 10 for numeros in numeros]
        print(res)
        """
        -Para poder entender o que esta acontecendo precisamos dividir a expressão em duas partes 
        -A  primeira parte de: For de numeros in Numeros
        -A segunda parte: Numeros * 10
        """
        res = [numeros / 2 for numeros in numeros]
        print(res)

    #Usando junto de uma função
    elif(escolha == 2):
        numeros = [1, 2, 3, 4, 5, 6]
        def funcao(valor):
            return  valor * valor
        res = [funcao(numeros) for numeros in numeros]
        print(res)


        # 3
        def Caixa_Alta(amigo):
            amigo = amigo.replace(amigo[0], amigo[0].upper())
            return amigo


        amigos = ['maria', 'julia', 'ana', 'gabriella', 'rebeca']
        print([Caixa_Alta(amigo) for amigo in amigos])

    #List comprehension VS Loops
    elif(escolha == 3):
        # Loop
        numeros = [1, 2, 3, 4, 5]
        numeros_dobrados = []

        for numero in numeros:
            numeros_dobrados.append(numero * 2)
        print(numeros_dobrados)

        #Usando list comprehensinon
        print([numero * 2 for numero in numeros])

    #Usando com nomes
    elif(escolha == 4):
        #1
        nome = 'Geek University'
        print([letra.upper() for letra in nome])# Upper poem a primeira letra em caixa alta ai neste caso pra cada letra irá por em maiuscula tbm

        #2
        text = input('Informe uma frase qualquer -> ')
        print([letra.upper() for letra in text])
        print([letra.__add__('º') for letra in text]) # adicionando um caracterer a cada letra como texte

    #Usando com Loops
    elif (escolha == 5):
        num = [1,2,3,4,5,6]
        print([num * 3 for num in range(1,10)])

        print([bool(num) for num in [0,[],'',True,1,3.14]])

        print([str(num) for num in [1,2,3]])

    # condicionais e logicas em list adc
    elif(escolha == 6):
        #1
        numeros = [1,2,3,4,5,6,7,8,9]

        pares = [cont for cont in numeros if cont % 2 == 0]
        impar = [cont for cont in numeros if cont % 2 == 1]

        print(pares)
        print(impar)

        #Refatorando
        # qualquer modulo % 2 o resultado é 0 e 0 == False em python, por tanto not negando 0 vira verdadeiro por tanto 1
        pares2 = [numero for numero in numeros if not numero % 2]

        # qualquer modulo % 2 se o numero for impar é ==1 por tanto verdadeiro em python
        impar2 = [ numero for numero in numeros if numero % 2]

        # 3
        res = [ numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
        



    resp = input('qeur sair do programa [S/N]? ').upper()