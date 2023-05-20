"""

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
        """RETORNA O VALOR DO PRODUTO COM DESCONTOS"""
        return (self.__valor * (100 - porcentagem))/ 100
"""
pd1 = Produto("play1","gamer", 1200)
descontoProduto = int(input("qual o valor do desconto: "))
print(pd1.desconto(descontoProduto))

print(Produto.desconto(pd1, 40))# passando o objeto como parametro
"""
from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:
    def __init__(self,nome,sobrenome,email,senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds= 100, salt_size = 8)# emparalha a senha, tamanho ou comprimento da função
    # self.__senha = cryp.encrypt(senha, rounds= 2000, salt_size = 16) vai dar um erro sugerindo hash

    def nome_completo(self):
        return f"{self.__nome}  {self.__sobrenome}"
    def verifica_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
"""
usuario = Usuario("Bruce","Wayne", "@gmail", 1234)
usuario2 = Usuario("Felicity", "Smoke","@gmail.com","1235")
print(usuario.nome_completo())
print(usuario2.nome_completo())

# acessando atributo de forma errada
print(f"senha usuario 1: {usuario._Usuario__senha}")
print(f"senha usuario 2: {usuario2._Usuario__senha}")
"""
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

# herança
class Pessoa:
    def __init__(self, nome, idade):
        self.nome =nome
        self.idade = idade
        self.nome_da_classe = self.__class__.__name__
    def falar(self):
        return f"{self.nome_da_classe} Falando..."
class Cliente(Pessoa):
    pass
class Aluno(Pessoa):
    pass
c1 = Cliente("maria",42)
a1 = Aluno("jurandi",56)
print(a1.falar())
class Pessoa:
    def __init__(self, nome, idade):
        self.nome =nome
        self.idade = idade
        self.nome_da_classe = self.__class__.__name__
    def falar(self):
        return f"{self.nome_da_classe} Falando..."

class Cliente(Pessoa):
    def compra(self):
        print(f"{self.nome_da_classe} Comprando...")

class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome_da_classe} Estudando...")

c2 = Cliente("fb",15)
print(c2.compra())