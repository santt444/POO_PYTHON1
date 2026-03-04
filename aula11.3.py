import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Funcionario:
    def __init__(self, salario):
        self._salario = salario 
    
func = Funcionario(3000)
print(func._salario) #  A) fora da classe
# B) o python n impede 
# C) proteger o atributo 

