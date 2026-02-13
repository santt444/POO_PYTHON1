import os 
def clear():
    os.system("cls")
clear()

class Plano:
    def __init__(self,nome,valor_mensal):
        self.nome = nome
        self.valor_mensal = valor_mensal
    
    def exibir(self):
         print(f"Plano: {self.nome}\nMensalidade: R${self.valor_mensal:.2f}")

plan = Plano("Premium", 120.00)
plan.exibir()
    