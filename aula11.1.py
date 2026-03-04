import os 
def clear():
    os.system("cls")
clear()
from time import sleep  

# Analise o código:

class Pessoa: 
    def __init__(self, nome, idade):
         self.nome = nome 
         self._idade = idade 
         self.__cpf = "123.456.789-00"

#Responda:

print("(A) Qual atributo é público?" )
sleep(2)
print("Atributo self.nome")

sleep(2)
clear()

print("(b) Qual é protegido?")
print("Atributo self.idade")

sleep(2)
clear()

print("(c) Qual é privado? ")
print("Atributo self.cpf")
sleep(2)
clear()

print("(d) Qual deles pode ser acessado diretamente sem erro?")
print("Atributo self.nome")

sleep(2)
clear()