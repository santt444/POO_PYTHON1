import os 
def clear():
    os.system("cls")
clear()
from time import sleep 

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media 
    
    def situacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado Burro"
        
aluno1 = Aluno("joao", 5, 5)
print(f"Aluno: {aluno1.nome}")
print(f"Média: {aluno1.calcular_media()}")
print(f"Situação: {aluno1.situacao()}")

sleep(2)
clear()

aluno2 = Aluno("santt", 10, 7)
print(f"Aluno: {aluno2.nome}")
print(f"Média: {aluno2.calcular_media()}")
print(f"Situação: {aluno2.situacao()}")