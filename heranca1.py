import os 
def clear():
    os.system("cls")
clear()

class animal:
    def falar(self):
        print("O Animal faz um som")

class cachorro(animal):
    pass

class gato(animal):
    pass


g = gato()
g.falar()

dog = cachorro()
dog.falar()

#1 Classe animal
#2 Classe cahorro
#3 porque ele é uma subclasse e está herdando os atributos da classe pai
#4 foi herdado
