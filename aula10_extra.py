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

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def apresentar(self):
        print(f"Professor: {self.nome} | Disciplina: {self.disciplina}")


class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Aluno: {aluno.nome} | Média: {aluno.media():.1f} | Situação: {aluno.situacao()}")




#professor
prof = Professor("Leo", "Matemática")
prof.apresentar()

#alunos
aluno1 = Aluno("joao", 8.0, 7.5)
aluno2 = Aluno("yuri", 5.0, 6.0)

#adicionar alunos
turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)

#média e situação
print("\nAlunos da turma:")
turma.listar_alunos()
