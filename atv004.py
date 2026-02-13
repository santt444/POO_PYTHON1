import os 
def clear():
    os.system("cls")
clear()

class Roupa:
    def __init__(self,nome, preço ):
        self.nome = nome 
        self.preço = preço 

    def exibir(self):
        print(f"Peça: {self.nome}\nPreço: R${self.preço:.2f}")

cmst = Roupa("Nike", 59.90) 
cmst.exibir()