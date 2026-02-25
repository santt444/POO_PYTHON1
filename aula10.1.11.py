import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class celular:
    def  __init__(self, marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        print(f"Celuar marca: {self.marca}\nmodelo: {self.modelo}")

c = celular("Iphone", "8 plus")
c.descricao()