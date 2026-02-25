import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
     
    
    def exibir(self):
        print(f"Cliente: {self.titular}\nSaldo em conta após saque: R$ {self.saldo:.2f}")

    def sacar(self,valor):
        print(f"Saldo em conta: {self.saldo}")
        if valor > self.saldo:
            return "Saldo insuficiente"
        else:
            self.saldo -= valor
            return (f"Saque de R$ {valor:.2f} realizado")

minha_conta = ContaBancaria("Dani", 1000)
minha_conta.depositar(50)
print(minha_conta.sacar(500))
minha_conta.exibir()