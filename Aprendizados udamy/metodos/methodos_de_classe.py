

"""
class Lampada:
    def __init__(self,cor,voltagem,luminoziadade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminoziadade = luminoziadade

class ContaCorrente:
    # atributo de classe
    contador = 4999
    def __init__(self,limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    contador = 0
    def __init__(self,nome,descricao,valor):
        self.id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.id

    def desconto(self, porcentagem):
       #RETORNA O VALOR DO PRODUTO COM DESCONTOS
        return (self.__valor * (100 - porcentagem))/ 100

pd1 = Produto("play1","gamer", 1200)
descontoProduto = int(input("qual o valor do desconto: "))
print(pd1.desconto(descontoProduto))

print(Produto.desconto(pd1, 40))# passando o objeto como parametro


# methodos de classe
from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:
    # metodo de classe
    contador = 0
    @classmethod
    def conta_usuario(cls):
        print(f"{cls}")
        print(f'Temos {Usuario.contador} usuarios no sistema')
    def __init__(self,nome,sobrenome,email,senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds= 100, salt_size = 8)# emparalha a senha, tamanho ou comprimento da função
        Usuario.contador = self.__id

    def nome_completo(self):
        return f"{self.__nome}  {self.__sobrenome}"
    def verifica_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

usuario = Usuario("Bruce","Wayne", "@gmail", 1234)
usuario2 = Usuario("Felicity", "Smoke","@gmail.com","1235")
print(usuario.nome_completo())
print(usuario2.nome_completo())

# acessando atributo de forma errada
print(f"senha usuario 1: {usuario._Usuario__senha}")
print(f"senha usuario 2: {usuario2._Usuario__senha}")

# o ideal é que esteja criptografado
# pip install passlib
#from passlib.hash import pbkdf2_sha256


nome = 'filicity'
sobrenome = 'smoke'
email ='@gamail'
senha =input('senha: ')
confirmaSenha = input('confirmaSenha: ')
if senha == confirmaSenha:
    nome1 = Usuario(nome,sobrenome,email,senha)
else:
    print("errou a senha meu chapá")
    exit(42)
print('Senha criada com sucesso!!')
senha = input('senha: ')

if nome1.verifica_senha(senha):
    print('Acessi Permitido')
else:
    print('Acesso Negado')
    exit(1)
print(f'Senha Criptografada: {nome1._Usuario__senha}') # acesso errado !



usuario1 = Usuario('bruce','wayne','@batmail','1234')
usuario2 = Usuario('felicity','smoke','@TImail','12345')

Usuario.conta_usuario() # forma correta
usuario2.conta_usuario() # possivel mas forma errada
"""

"""
class Conta:
    contador = 400
    def __init__(self,titular, saldo,limite):
        self.__numero = Conta.contador + 1
        self.__titular =titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    def extrato(self):
        print(f"saldo de {self.__saldo} titluar: {self.__titular}")
    def depositar(self,valor):
        if valor >= 1:
            self.__saldo += valor
        else:
            print(f'O valor precisa ser positivo {valor}')
    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('saldo insuficiente')



"""

class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf =cpf
    def diz(self):
        print(f" o cliente: {self.__nome} diz  oi")
class ContaCorrente:

    contador =4999

    def __init__(self, limite, saldo, cliente):

        self.__numero = ContaCorrente.contador

        self.__limite = limite

        self.__saldo= saldo

        self.__cliente =cliente

        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'o cliente é {self.__cliente._Cliente__nome}')

class Usuario:

    def __init (self, nome, sobrenome, email, senha):
        self.nome =nome
        self. sobrenome =sobrenome
        self.email = email
        self. senha =senha



cli1 = Cliente('Angelina Jolie', 123456)
cc = ContaCorrente(500,100,cli1)

cc.mostra_cliente()

cc = ContaCorrente(5000, 10000, cli1)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz()