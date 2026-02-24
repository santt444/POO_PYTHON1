import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def informacao(self):
        print(f"{self.nome} é um {self.especie}")

esp = Animal("elefante", "mamífero")
esp1 = Animal("camarão pistola", "Alpheidae")

esp.informacao()
sleep(1)
esp1.informacao()