import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        return f"{self.nome} disse auau e tem {self.idade} anos"



cachorro1 = Cachorro("Bonicio", 3)
cachorro2 = Cachorro("Bidu", 5)


print(cachorro1.latir())
print(cachorro2.nome)