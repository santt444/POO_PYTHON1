import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def resumo(self):
        print(f"O livro {self.titulo} foi escrito por {self.autor}")

L = livro("Blue lock", "Muneyuki kaneshiro")
L.resumo()