import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome 
        self.nota = nota 

    def mostrar_nota(self):
        print(f"O aluno {self.nome} tirou nota {self.nota}")

a = Aluno("Santt", 10)
a.mostrar_nota()