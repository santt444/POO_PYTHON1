import os 
def clear():
    os.system("cls")
clear()

class Item:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço
    
    def exibir(self):
        print(f"Item: {self.nome} \nPreço: R${self.preço:.2f}")

i1 = Item("Caderno", 45.90)
i1.exibir()
