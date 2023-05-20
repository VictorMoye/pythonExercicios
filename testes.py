import math, random
class Aux:
    def __init__(self, linha, numero):
        self.linha = linha
        self.numero = numero

    def Crialinha(self):
        print("==" * int(random.randint(10,20))) # retorna um none problema na programção
    def Long(self,linhas,caracter):
        linhas = linha.numero + int(random.randint(10,15))
        caracter = input("qual caracter deseja: ")
        return caracter * linhas

linha = Aux('=',int(random.randint(1,10)))
# classe produto
class Produto:
    # atributo de classe
    imposto = 1.35
    contador = 0

    def __init__(self,nome,tamanho,tipo,preco):
        self.id = Produto.contador + 1
        self.nome = nome
        self.tamanho = f"{tamanho} Metros"
        self.tipo = tipo
        self.preco = preco * Produto.imposto
        Produto.contador = self.id
    def Ligar(self):
        return "Ligar"
    def Desligar(self):
        return ("Desligar")

ps4 = Produto("play station",10, "gamers",4000)
produto = Produto("Produto",5,"Produto medido em metros",10)

# deletando atributos
print(dir(ps4))
print(dir(produto))
# ou
print(ps4.__dict__)
print(produto.__dict__)

del produto.tamanho


print(ps4.__dict__)
print(produto.__dict__)

