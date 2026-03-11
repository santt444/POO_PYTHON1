import os 
def clear():
    os.system("cls")
clear()

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
class aluno(pessoa):
    def estudar(self):
        return (f"Eu me chamo {self.nome} estou aprendendo e tenho {self.idade} anos")
class professor(pessoa):
    def ensinar(self):
        return (f"Eu me chamo {self.nome} estou ensinando e tenho {self.idade} anos ")

aln = aluno("santt", 17)
print(aln.estudar())

prof = professor("leo", 30)
print(prof.ensinar())
