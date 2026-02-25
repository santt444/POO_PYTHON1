import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Filme:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano 
    
    def detalhes(self):
        print(f"Filme {self.titulo} \nlançado em {self.ano}")

f = Filme("Vingadores", 2018)
f.detalhes()