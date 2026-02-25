import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_preco(self):
        print(f"O produto: {self.nome} \ncusta: R$ {self.preco}")

p = Produto("celular", 1400)
p.mostrar_preco()