import os 
def clear():
    os.system("cls")
clear()
from time import sleep 

class Produto:
    def __init__(self, nome, preco,):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto

    def mostrar(self):
        print(f"Produto: {self.nome}")
        print(f"Preço atualizado: R$ {self.preco:.2f}")


#teste
produto1 = Produto("Camisa", 100.0)

produto1.aplicar_desconto(20)  #20% de desconto
produto1.mostrar()