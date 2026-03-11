import os 
def clear():
    os.system("cls")
clear()

class Animal:
    def __init__(self, nome):
        self.nome = nome 

class cachorro(Animal):
    def falar(self):
        return(f" Nome do cachorro é {self.nome}")

class gato(Animal):
    def falar(self):
        return(f" Nome do gato é {self.nome}")

dog = cachorro("rossi")
print(dog.falar())

cat = gato("reginaldo")
print(cat.falar())
        