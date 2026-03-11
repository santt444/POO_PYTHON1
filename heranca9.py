import os 
def clear():
    os.system("cls")
clear()

class Personagens:
    def __init__(self, nome):
        self.nome = nome 


    def atacar(self):
        return ("Está atacando ")
    
class Guerreiro(Personagens):
    def atacar(self):
        return (f"O personagem {self.nome} atacou com uma espada do khaos ")

class Mago(Personagens):
    def atacar(self):
        return (f"O personagem {self.nome} atacou com magia das sombras")

gue = Guerreiro("Kratos")
print(gue.atacar())

mag = Mago("Harry")
print(mag.atacar())