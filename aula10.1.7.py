import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo 
        self.cor = cor

    def descrever(self):
        print(f"Carro {self.modelo} na cor {self.cor}")

c = carro("BMW","azul")
c.descrever()