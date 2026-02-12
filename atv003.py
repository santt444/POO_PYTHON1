import os 
def clear():
    os.system("cls")
clear()

class Livro:
    def __init__(self, titulo, preço):
        self.titulo = titulo
        self.preço = preço

    def exibir(self):
        print(f"Livro: {self.titulo}\nPreço: R${self.preço:.2f}")

lv1 = Livro("Python para Iniciantes " , 89.90)
lv1.exibir()