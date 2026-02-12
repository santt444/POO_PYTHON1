import os 
def clear():
    os.system("cls")
clear()

class Produto:

    def __init__(self, nome, preco):

        self.nome = nome

        self.preco = preco

    def exibir_informacoes(self): 
        print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}")

produto1 = Produto("Notebook", 3500.00)

produto1.exibir_informacoes()