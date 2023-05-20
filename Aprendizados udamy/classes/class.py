class Computador:
    def __init__(self, marca, memoria, placa):
        self.marca = marca
        self.memoria = memoria
        self.placa = placa

computador1 = Computador('azus', '12gb', 'nvidia 4gb')
print(computador1.marca)
class Produtos:
    def __init__(self, nome, produtos , valor):
        self.nome = nome
        self.produtos = produtos
        self.valor = valor

ps4= Produtos('paystation','gamer','1200 dolar')
print(ps4.nome, ps4.produtos, ps4.valor)

def retornaDois():
    return 2
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha # transformando a senha como privada
    def MostraSenha(self):
        print(self.__senha)
    def MostraEmail(self):
        print(self.email)
        retornaDois()


user = Acesso('email','senha')
print(user.email)
#print(user.__senha) # atributo erro, dis nao ter esse atributo
print(dir(Acesso))
print(user._Acesso__senha) # acessando o atributo privado (nome da classe + __ +  atributo) Name Mangling (junção da claase com o atributo) os nomes

user1 = Acesso("@GMAIL.COM.BR","12345")
user2 = Acesso("@gmail.com","123")

print(user1.MostraSenha() , user2.MostraSenha())

# Atributo de Classe
# atributos de classe,sao atributos que são declarados diferente da classe
# ou seja fora do metodo construtor, Geralmente já inicializamos um valor e este valor é compartilhado
# entre todas as intancias de uma classe. Ou seja ao inves de cada atributo ter seus proprios valores
# todas as intancias da classe terão o mesmo valor para este atributo#

class Produtos:
    # Atributos de Classe
    imposto = 1.50
    def __init__(self, nome, produtos , valor):
        self.nome = nome
        self.produtos = produtos
        self.valor = valor
p1 = Produtos("pLAY", "VIDEO GAMER", 1852)
p2 = Produtos("xbos","video gamer", 2562)
print(p1.imposto)
print(p2.imposto)

print(f"valor com imposto {p1.valor} de {p1.imposto} "
      f"valor sem imposto {p1.valor - p1.imposto}")
