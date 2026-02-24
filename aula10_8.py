import os 
def clear():
    os.system("cls")
clear()

class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def lecionar(self):
        print(f"O professor {self.nome} leciona a disciplina de {self.disciplina}.")



prof1 = Professor("Carlos", "Matemática")
prof1.lecionar()