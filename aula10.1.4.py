import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

ret = Retangulo(5, 3)

print("Área do retângulo:", ret.calcular_area())