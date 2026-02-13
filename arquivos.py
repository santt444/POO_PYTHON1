import os 
def clear():
    os.system("cls")
clear()
from time import sleep

# ATIVIDADE 1

class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_informacoes(self): 
        print(f"Produto: {self.nome}\nPreço: R${self.preco:.2f}")
print("ATIVIDADE 1")

produto1 = Produto("Notebook", 3500.00)
produto1.exibir_informacoes()
sleep(1.5)
clear()

# ATIVIDADE 2

class Item:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def exibir(self):
         print(f"Item: {self.nome}\nPreço: R${self.preço:.2f}")
print("ATIVIDADE 2")

Caderno= Item("Caderno", 45.90 )
Caderno.exibir()
sleep(1.5)
clear()

# ATIVIDADE 3

class Livro:
    def __init__(self, título, preço):
        self.título = título
        self.preço = preço

    def exibir(self):
         print(f"Livro: {self.título}\nPreço: R${self.preço:.2f}")
print("ATIVIDADE 3")

livro = Livro("Python para iniciantes", 89.90 )
livro.exibir()
sleep(1.5)
clear()

# ATIVIDADE 4

class Roupa:
    def __init__(self, Nome, Preço):
        self.Nome = Nome
        self.Preço = Preço


    def exibir(self):
        print(f"Peça: {self.Nome}\nPreço: R${self.preço:.2f}")
print("ATIVIDADE 4")

camisa = Livro("camiseta",59.90 )
camisa.exibir()
sleep(1.5)
clear()

# ATIVIDADE 5

class Plano:
    def __init__(self,nome, valor_mensal):
        self.nome = nome
        self.valor_mensal = valor_mensal


    def exibir(self):
        print(f"Plano: {self.nome}\nMensalidade: R${self.valor_mensal:.2f}")
print("ATIVIDADE 5")

Premium = Plano("Premium",120.00)
Premium.exibir()
sleep(1.5)
clear()

# ATIVIADE 6 

class Aparelho:
    def __init__(self, nome, preço):
        self.nome = nome 
        self.preço = preço

    def exibir(self):
         print(f"Aparelho: {self.nome}\nPreço: R${self.preço:.2f}")
print("ATIVIDADE 6")

celular = Aparelho("Smartphone",2500.00)
celular.exibir()
sleep(1.5)
clear()
