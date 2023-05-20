"""
çLista de exercicios 7 parte 1

"""
import glob
import  math, random
def CriarLinha():
    return print("=" * 30)
def PerguntasExercicios():
    print('1- Faça uma veotr demonimado A que armazene 6 numeros inteiro e tenque dar os seguintes passos: \n'
          '\tA- atribua os seguintes valores a esse vetor: 1,0,5,-2,-5,7\n'
          '\tb- armazene uma variavel interia simples e some entre os valores das posiçoes A[0]A[1]..A[5] do vetor  \te mostre sa soma na tela \n'
          '\tc- modifique o vetor na posição 4 atribuindo a esta posição o valor 100 \n'
          '\td- mostre na tela cada valor do vetor A um em cada linha')

    print('2- Programa que ler 6 valores e mostre eles lidos na tela')

    print('3- Ler um conjunto de numeros reais armazenado armazenando em um vetor\n'
          '\te calculando os quadrados de cada numero armazenando dentro de outro vetor e imprima todos os resultados')

    print('4- Leia um conjunto de 8 posições e tambem dois valores X & Y que deveram apontar pra qualquer index \n'
          '\te no final some os numeros contidos nas posições X & Y ')

    print('5- Conta um vetor e escreve nele quantos numeros pares ele possui e impares \n'
          '\t O menor e o maior mostra ele tambem de forma inversa e \n'
          '\tmostra tambem qual posição esta o menor e o maior todas as listas')

    print('6- Retirando os numeros pares e impares da lista de forma bem diferente')
s
    print('7- Programa que ler uma list e mostra o menor e maior valor e a media dele')

    print('8- Programa que verifica se existe numeros repetidos dentro da lista ')

    print('9- Programa que impede que numeros repetidos entre na lista ')

    print('10-Programa que gera uma responsta diferente dependendo da escolha da pessoa uma opção entre \n'
          '\t0 - O processo é incerrado'
          '\t1 - O processo retorna a lista na ordem normal'
          '\t2 - O processo retorna a lista de forma inversa'
          '\tQualquer outro codigo entrara como um erro !!')

    print('11-Atribui valor 0 para todos os valores que tiverem negativos dentro da lista')

    print('12-Programa que ler os numeros da lista e você escolhe um valor qualquer \n'
          '\tDentro da lista X e ele te dira os muultiplos desse valor inteiros')

    print('13-ler um vetor de 50 com o seguinte valor: (I + 5 * I ) % (I +1) I= Tamanho')

    print('14-Subtração de lista')
def somandoOsNumerosNaLista_SubstintuindoUmValorNaLista():
    vetor = []

    # Adc elemento ao vetor e somando os elementos
    for cont in range(0, 6):
        vetor.append(int(input('Digite um valor inteiro : ')))
    print(vetor)

    print(f'A soma de todos os numero é = {sum(vetor)}')

    posicao = int(input(f'Qual posição voce quer alterar o valor: [0] e [5]'))
    num = int(input(f'Qual numero voce quer troca na posição [{posicao}] = '))

    vetor.insert(posicao, num)
    print(vetor)

    print(f'A nova soma agora é = {sum(vetor)}')
def Mostra6NumerosLidos():
    lista = []
    tamanho = int(input('Digite o tamanho de sua lista: '))
    for cont in range(0, tamanho):
        lista.append(int(input('Digite qualquer elemento pra por na lista -> ')))

    print(lista)
    res = [(numeros * 10) for numeros in lista]  # Compreension
    print(res)
def CalculandoQudradoDentroDaLista(vetor_inteiro):
    vetor_quadrado = []
    vetor_RaizQuadrado = []
    vetor_universo = []
    for cont in range(0, tamanho):
        # Achando a raiz quadrada dos numeros
        vetor_RaizQuadrado.append(round(math.sqrt(vetor_inteiro[cont]), 2))

        # Achando os quadrados dos numeros inteiros
        vetor_quadrado.append(vetor_inteiro[cont] * vetor_inteiro[cont])

    vetor_universo.append(vetor_inteiro)
    vetor_universo.append(vetor_quadrado)
    vetor_universo.append(vetor_RaizQuadrado)
    universo = {"lista_inteira " : vetor_inteiro ,
                "lista_quadrada" : vetor_quadrado,
                "lista_raiz" : vetor_RaizQuadrado}
    return print(f"{universo}")
def Recebe2IndexESoma_naLista(tamanho):
    lista = []
    soma = []
    for cont in range(0, tamanho):
        lista.append(int(input('Digite o valor aqui: ')))
    print(lista)

    x = int(input(f'Informe a posição do X entre {0} e {tamanho - 1} -> '))
    y = int(input(f'Informe a posição do y entre {0} e {tamanho - 1} -> '))

    if x & y <= tamanho - 1:
        soma = lista[x] + lista[y]
        return print(f'{lista[x]} + {lista[y]} = {soma}')
    else:
        while True:
            print('Valor superior ao tamanho da lista ou invalido')
            x = int(input(f'Informe a posição do X entre {0} e {tamanho - 1} -> '))
            y = int(input(f'Informe a posição do y entre {0} e {tamanho - 1} -> '))
            if x & y <= tamanho - 1:
                soma = lista[x] + lista[y]
                return print(f'{lista[x]} + {lista[y]} = {soma}')
            else:
                print('Valor invalido')
def Ler_numeros_paresImpares_dentroLista():
    vetor = list()
    resp = dict()
    contPar = contImpar = 0
    tamanho = int(random.randint(1,100))
    # Inserindo os valores a lista
    for cont in range(0,tamanho):
        vetor.append(random.randint(1,tamanho))
    #Descobrindo quantos numeros pares e impares existem na lista
    for cont in vetor:
        if vetor[cont] % 2 == 0:
            contPar += 1
        else:
            contImpar += 1
    resp = {'Vetor ' : vetor, "qtdPar ": contPar, "qtdImpar" : contImpar}
    return resp
def Ler_numeros_paresImpares_dentroLista(tamanho):
    vetor = list()
    # Inserindo os valores a lista
    for cont in range(0, tamanho):
        vetor.append(random.randint(1, 40))
    print(vetor)


    par = [cont for cont in vetor if cont % 2 == 0]
    impar = [contadora for contadora in vetor if contadora % 2 == 1]
    resp = dict()
    resp = {"Lista completa" : vetor ,"par" : par,"impar": impar}
    return resp
def Ler_numeros_paresImpares_dentroLista2():
    num1 = int(input('Informe o tamanho do vetor  -> '))
    num = [[], []]
    vetor = list()

    for cont in range(1, num1 + 1):
        vetor.append(int(input('Digite o valor aqui: ')))

    num[0] = [cont for cont in vetor if cont % 2 == 0]
    num[1] = [cont for cont in vetor if cont % 2 == 1]

    print(num)
    print(f'Os numeros pares dentro da lista são -> {num[0]}')
    print(f'A soma de todos os numeros pares é -> {sum(num[0])}')
    print(f'O maior numero par é -> {max(num[0])}')
    print(f'O menor numero par é -> {min(num[0])}')
    print(f'Os numeros impares dentro da lista são -> {num[1]}')
    print(f'A soma de todos os numeros impares da lista é -> {sum(num[1])}')
    print(f'O maior numero impar é -> {max(num[1])}')
    print(f'O menor numero impar é -> {min(num[0])}')
    print(f'Lista completa \n{vetor}')
    print(f'A posição do menor numero dentro da lista é -> [{vetor.index(min(vetor))}] o numero é {min(vetor)}')
    print(f'A posição do maior numero dentro da lista é -> [{vetor.index(max(vetor))}] o numero é {max(vetor)}')
    print(f'Lista invertida porem completa \n{vetor[:: -1]}')
def Exercicio6OrganizandoLista():
    num = [[], []]
    valor = 0
    for cont in range(1, 8):
        valor = int(input(f'Digite o {cont}º valor -> '))
        if valor % 2 == 0:
            num[0].append(valor)
        else:
            num[1].append(valor)
    print('-' * 30)
    num[0].sort()
    num[1].sort()
    print(f'Os valores pares digitados forem: {num[0]}')
    print(f'Os valores impares digitados foram: {num[1]}')
def MostraMenorMaiorMediaDaLista():

        tamanho = int(input('Informe o tamanho da lista: '))
        lista = []
        maior = menor = 0
        for cont in range(0, tamanho):
            lista.append(int(input(f'Digite o {cont}º valor -> ')))
            if cont == 0:
                menor = maior = lista[cont]
            else:
                if lista[cont] >= maior:
                    maior = lista[cont]

                if lista[cont] <= menor:
                    menor = lista[cont]

        print(lista)
        print(f'O Menor numero da lista é {menor}')
        print(f'O Maior numero da lista é {maior}')
        media = sum(lista) / len(lista)
        print(f'A Média da lista é {media}')
def VerificaNumerosRpetido():

    tamanho = int(input("Informe o tamanho da lita"))
    lista = []
    listaBruta = list()
    duplicado = list()
    for cont in range(0, tamanho):
            num = int(input(f'Digite o {cont}º Valor -> '))
            listaBruta.append(num)
            if num not in lista:
                lista.append(num)
            else:
                duplicado.append(num)
    print(f'Os elementos dentro da lista com duplicação \n{listaBruta}')
    print(f'Os elementos dentro da lista são sem duplicação \n{lista}')
    print(f'Os elementos duplicados da lista são \n{duplicado}')
def ImperdeNumerosRepetidosListas(listas):

    listaTot = []
    listaSemRepeticao = []
    for cont in range(0,listas):
        aux = int(random.randint(1, 100))
        listaTot.append(aux)
        # tirando os numeros repetidos dentro da listas
        if aux not in listaSemRepeticao:
            listaSemRepeticao.append(aux)
    return  print(f"lista completa: {listaTot} \n"
                  f"lista sem repeticao: {listaSemRepeticao}")
def TamnhoLista(tamanho):
    tamanho = int(random.randint(1,50))
    return tamanho
def subtracaoListas(tamanho):
        list1 = []
        list2 = []
        for cont in range(0, tamanho):
            list1.append(random.randint(1, 50))
        for cont in range(0, TamnhoLista(tamanho)):
            list2.append((random.randint(1, 50)))
        return print(f" lista 1 : {list1} \n "
                     f"Soma de list1: {sum(list1)} \n"
                     f"Lista 2 : {list2} \n "
                     f"Soma de list2: {sum(list2)}\n "
                     f"Subtação entre listas: {sum(list1) - sum(list2)}")
resp = ''
while resp != 'S':

    escolha = int(input('\nQual exercicios você quer fazer -> '))
    #Exercicio 1
    if escolha == 1:
        somandoOsNumerosNaLista_SubstintuindoUmValorNaLista()
        CriarLinha()
    #Exercicio 2, mostra 6 valores lidos na tela
    elif escolha == 2:
        Mostra6NumerosLidos()
        CriarLinha()
    # 1 vetor contendo numeros outro vetor armazenando os numeros elevado ao quadrado
    # e mostrando todos os vetores dentro de apenas um
    elif escolha == 3:
        vetor_inteiro = []
        tamanho = int(input('Digite o tamanho do seu vetor: '))

        for cont in range(0, tamanho):
            # Adicionando elementos inteiros a lista
            vetor_inteiro.append(int(input('Digite um numero: ')))
        CalculandoQudradoDentroDaLista(vetor_inteiro)
    #Leia os elementos na posição X & Y e mostre a soma deles
    elif escolha == 4:
        tamanho = int(input('Informe o tamanho do seu vetor: '))
        print(Recebe2IndexESoma_naLista(tamanho))
    # Ler quantos numeros pares e impares tem e mais algumas coisas também
    elif escolha == 5:
        tamanho = random.randint(1, 20)
        print(Ler_numeros_paresImpares_dentroLista(tamanho))
        CriarLinha()
        print(Ler_numeros_paresImpares_dentroLista2())

    #Retirando os numeros impares e pares e jogando em uma lista dupla dentro de uma outra lista
    elif escolha == 6:
        print(Exercicio6OrganizandoLista())
        CriarLinha()
    #Mostra o menor maior e a media dentro da lista
    elif escolha == 7:
            MostraMenorMaiorMediaDaLista()
            CriarLinha()
    #Programa que verifica se existe numeros repetidos dentro da lista
    elif escolha == 8:
        VerificaNumerosRpetido()
        CriarLinha()
    #Programa que impede que numeros repetidos entre na lista
    elif escolha == 9:
        #UMA TUPLA RESOVERIA O CASO POIS TUPLA NAO RECEBEM VALORES REPETIDOS
        # Não repetindo valores na lista
        listas = int(input("Qual o tamanho da sua lista: "))
        ImperdeNumerosRepetidosListas(listas)
        CriarLinha()
    #Programa que faz uma ordem diferente cada vez que voce aperta qualquer valor
    elif escolha == 10:
        lista = list()
        tamanho = int(input('Informe o tamanho de seu vetor '))
        for cont in range(0, tamanho):
            lista.append(int(input(f'Informe o número na posição {cont}º -> ')))
        resp = 1
        while resp != 0:
            print('Escolha uma opção entre')
            print('0 - O processo é incerrado')
            print('1 - O processo retorna a lista na ordem normal')
            print('2 - O processo retorna a lista de forma inversa')
            print('Qualquer outro codigo entrara como um erro !!')

            resp = int(input('Informe o processo que você quer ver '))
            if resp == 1:
                print('1 - O processo retorna a lista na ordem normal')
                print(lista)
            elif resp == 2:
                print('2 - O processo retorna a lista de forma inversa')
                print(lista[:: -1])
            elif resp == 0:
                resp = 0

    #Atribui valor 0 para todos os valores que tiverem negativos dentro da lista
    elif escolha == 11:
        lista = list()
        tamanho = int(input('Informe o tamanho de seu vetor '))
        for cont in range(0, tamanho):

            lista.append(int(input(f'Informe o número na posição {cont}º -> ')))
            if lista[cont] <= 0:
                lista[cont] = 0
        print(lista)

    #Programa que voce escolhe qualquer valor dentro da lista e ele te mostra os multiplos dele
    elif escolha == 12:
        lista = list()
        tamanho = int(input('Informe o tamanho de seu vetor '))
        for cont in range(0, tamanho):
            lista.append(int(input(f'Informe o número na posição {cont}º -> ')))

        print(lista)
        print('Você quer acessa os multiplos das variaveis pelo indice [1] OU pelo numero do elemento [2]')
        escolha = int(input('Qual você prefere ? '))

        if escolha == 1:
            ind = int(input('Escolha qual desses número você quer saber os multiplos digite o numero do index -> '))
            resp = lista[ind]
            num = 0
            while num <= resp:
                print(f'{num} * {resp} = {num * resp}')
                num += 1

        elif escolha == 2:
            resp = int(input('Escolha qual desses número você quer saber os multiplos '))
            num = 0
            while num <= resp:
                print(f'{num} * {resp} = {num * resp}')
                num += 1

        else:
            print('Valor invalido')

    # ler um vetor de 50 com o seguinte valor: (I + 5 * I ) % (I +1)
    elif escolha == 13:
        tamanho = 25
        vetor = list()
        for cont in range(0, tamanho):
            vetor.append((tamanho + 5 * tamanho) % (tamanho + 1))
            print(vetor)

    #Subtração de lista
    elif escolha == 14:
        tamanho = 0
        tamanho = TamnhoLista(tamanho)
        subtracaoListas(tamanho)
        CriarLinha()

    resp = input('Você quer sair da lista de exercicios [S/N]? ').upper()


