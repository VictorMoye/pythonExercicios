"""
Funções com parametros padrão (Default Paramters)
- Funções onde a passagem de parametros é opcional

"""

resp = ''
while resp != 's':

    print('1- Tornando uma o parametro opcional')
    print('2 - Exemplo mais complexo ')
    print('3- Funções como parametro')
    print('4- Variaveis globais e variaveis locais')
    print('5- Funções dentro de funções')
    escolha = int(input('Qual exercicio voce quer ver -> '))

    if escolha == 1:
        # Exemplo de função aonde a passagem de parametro é opcional
        print()
        print('geek')


        # Exemplo de função onde a passagem é obrigatoria
        def quadrado(numero):
            return numero ** 2


        print(quadrado(5))


        def exponencial(numero, potencia):
            return numero ** potencia


        print(exponencial(2, 3))  # 2 * 2 * 2
        print(exponencial(9, 9))


        # tranformando a função expotencial em opcional passar parametros
        def exponencial_2(numero, potencia=2):  # fazendo com que o parametro receba um valor ele se torna opcional
            return numero ** potencia


        print(exponencial_2(3))  # por padrão se passar apenas um argumento elevara a 2
        print(exponencial_2(3, 5))

        def exponencial_3(numero = 2, potencia = 2):
            return numero ** potencia
        print(exponencial_3())

        #OBS: Os parametros defout opcionais devem ser colocados sempre ao final da declaração
        #ERRO
        #def teste(num = 2, porencia): # note que isso é um erro a opção deve sempre ser o ultimo na ordem
         #   return num + porencia
        #print(teste(6))

    #Exemplo complexo
    elif escolha == 2:
        # Exemplo complexo
        def mostra_informação(nome='Geek', intrutor = False):
            if nome == 'Geek' and intrutor:
                return 'Bem vindo intrutor Geek'
            elif nome == 'Geek':
                return 'Eu pensei que voce era o instrutuor'
            return  f'Ola {nome}'
        print(mostra_informação())
        print(mostra_informação(intrutor=True))
        print(mostra_informação(True))
        print(mostra_informação('Bruce'))
        print(mostra_informação(nome='Wayne'))

    #FUNÇÕES COMO PARAMETRO
    elif escolha == 3:
        #Exemplos
        def soma(num1,num2):
            return num1 + num2

        def mat(num1,num2,fun=soma):
            return fun(num1, num2)

        def subtração(num1,num2):
            return num1 - num2
        print(mat(2,3))
        print(mat(3,5,subtração))

    #Variaveis locais e globais
    elif escolha == 4:
        #Variavel global
        instrutor  ='Geek' #Global pois esta fora do escopo da função / so é local comparada com o if e o resto da função
        def diz_oi():
            return f'Oi {instrutor}'
        print(diz_oi())

        #Variavel local
        intrutor = 'Python'
        def diz_oi2():
            instrutor = 'CSharp'
            return f'Oi {instrutor}'
        print(diz_oi2())
        #Obs: Variavel local se sobrepoem a uma variavel local
        #se tivemos uma variavel local com o mesmo nome da global a variavel local sera usada ao inves da global

        def diz_oi_3(nome):
            nome = 'bruce '
            return f'Oi {nome}'
        print(diz_oi_3('viCTOR'))
        #Atenção com variaveis globais(Se puder evitar evite as)

        total = 0
        def incrementa():
            #Avisando pro python que queremos usar a variavel global
            global total # Para acessar a variavel global necessita especificar ela antes caso contrario so ira conseguir acessa a variavel local
            total = total + 1
            return total
        print(incrementa())
        for cont in range(0,100):
            print(incrementa())

    #Funções dentro de funções
    elif escolha == 5:
        def fora():
            contador = 0

            def dentro():
                nonlocal contador #NonLocal ela nao é local e nem global ela é apenas a variavel que esta emcima ou seja ela ta numa função anterior
                contador = contador + 1
                return contador
            return dentro()
        print(fora())

    resp = input('Quer sair do programa [S/N] ? ')

