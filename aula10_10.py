import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def mostrar_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")

    def calcular_idade(self):
        idade = 2026 - self.ano
        print(f"Idade do carro: {idade} anos")



carro1 = Carro("bmw", 2018)
carro1.mostrar_dados()
carro1.calcular_idade()