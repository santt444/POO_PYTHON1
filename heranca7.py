import os 
def clear():
    os.system("cls")
clear()

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Professor(Pessoa):
    def ensinar(self):
        return (self.nome, "está ensinando")

prof = Professor("Leo")
print(prof.ensinar())
