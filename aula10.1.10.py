import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def tocar(self):
        print(f"tocando música: {self.titulo} \nde: {self.artista}")
    
m = musica("Te amar demais", "Sodré")
m.tocar()