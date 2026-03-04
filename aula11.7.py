import os 
def clear():
    os.system("cls")
clear()
from time import sleep
 # Questão 7 
 
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("saldo não pode ser negativo ")
        else:
            self.__saldo = valor
            print("saldo atualizado ")



conta = Conta(1000)
print(conta.saldo) # acessa de forma controlada
conta.saldo = 500 # Atualizado 
conta.saldo = -100 # Negativo