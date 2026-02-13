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
        print(f"A marca do carro é {self.marca}")
        sleep(1.5)
        clear()
        print(f"O ano do carro é {self.ano}")
        sleep(1.5)
        clear()


    def calcular_idade(self):
        atual = 2026
        idade_carro = atual - self.ano
        return idade_carro


c1 = Carro("Mustang", 2000)
c2 = Carro("BMW", 2018)

c1.mostrar_dados()
c2.mostrar_dados()

idade = c1.calcular_idade()
print(f"Idade do carro Mustang: {idade} anos")

idade1 = c2.calcular_idade()
print(f"Idade do carro BMW: {idade1} anos")
