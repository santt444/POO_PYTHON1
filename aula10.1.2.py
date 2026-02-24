import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Pessoa:
    def __init__(self, nome, idade, cidade, profissao):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.profissao = profissao 
    
    def aniversario(self):
        self.idade += 1 
        
    def mensagem(self):
        print(f"{self.nome} é uma pessoa que tem {self.idade} anos de idade.")

    def apresentar(self):
        print(f"Nome: {self.nome} \nidade após fazer aniversário: {self.idade} anos \ncidade: {self.cidade}\nprofissão: {self.profissao}")
    

ps = Pessoa("Santt", 17,"ES", "Dev")



ps.mensagem()
ps.aniversario()
ps.apresentar()






