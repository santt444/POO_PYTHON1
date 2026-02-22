import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, saldo):
        self.saldo += saldo
    
    def exibir(self):
        print(f"Cliente: {self.titular}\nSaldo em conta: R$ {self.saldo:.2f}")


minha_conta = ContaBancaria("Dani", 1000)
minha_conta.depositar(50)
minha_conta.exibir()