import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    # Questão 5
    def get__saldo(self):
        return self.__saldo
    
    # Questão 6
    def set__saldo(self, valor):
        if valor < 0:
            print("saldo não pode ser negativo ")
        else:
            self.__saldo = valor
            print("saldo atualizado ")



conta = Conta(1000)
print(conta.get__saldo()) # acessa de forma controlada
conta.set__saldo(500) # Atualizado 
conta.set__saldo(-100) # Negativo


# Questão 4

# print(conta.__saldo) errado 
# print(conta._Conta__saldo) certo
# A) dar erro type object 'Conta' has no attribute
# B) porque é privado e esta protegido 