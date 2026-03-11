import os 
def clear():
    os.system("cls")
clear()

class pessoa:
    def __init__(self, nome):
        self.nome = nome 
    
class aluno(pessoa):
    pass

a = aluno("santt")
print(a.nome)

#1 foi criado na classe pessoa 
#2 porque herdou os atributos
