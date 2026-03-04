import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Aluno:
    def __init__(self, nota):
        self.__nota = nota 

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        self.__nota = valor
        if 0 <= valor <= 10:
            print(f"nota definida para {valor}")
        else:
            print(f"valor invalido: {valor} \nA nota deve ser entre 0 e 10")

aln1 = Aluno(8)   # válido
aln2 = Aluno(12)  # inválido

aln1.nota = 10    # válido
aln2.nota = - 3    # inválido