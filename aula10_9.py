import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Jogo:
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1 

    def subir_nivel(self):
        self.nivel += 1 
        print(f"No jogo {self.nome}, você subiu para o nível {self.nivel}!")



meu_jogo = Jogo("Hytale")
meu_jogo.subir_nivel()
sleep(2)
clear()
meu_jogo.subir_nivel()