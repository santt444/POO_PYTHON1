import os 
def clear():
    os.system("cls")
clear()
from time import sleep

 # Versão 1
class CarroPublico:
     def __init__(self, velocidade):
         self.velocidade = velocidade

print("Questão 1")
carro1 = CarroPublico(100) # velocidade atual
print(f"{carro1.velocidade} kmh velocidade atual")  # ler
carro1.velocidade = 120   # Modificação
print(f"{carro1.velocidade} kmh velocidade modificada")
print("-" * 40)

 # Versão 2
class CarroProtegido:
     def __init__(self, velocidade):
         self._velocidade = velocidade  # protegido

print("Questão 2")
carro2 = CarroProtegido(50)
print(f"{carro2._velocidade} kmh Velocidade atual ")  # velocidade atual 

carro2._velocidade = 100   # alterado 
print(f"{carro2._velocidade} kmh Velocidade modificada")

# Versão 3 
class CarroPrivado:
    def __init__(self, velocidade):
        self.__velocidade = velocidade # privado

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self,valor):
        if valor < 0:
           return "Velocidade não pode ser negativa"
        self.__velocidade = valor
print("-" * 40)

print("Questão 3")
carro3 = CarroPrivado(50)
print(f"{carro3.velocidade} kmh velocidade atual")  # atual
carro3.velocidade = 110
print(f"{carro3.velocidade} kmh velocidade modificada")  # modificada

print("(A) versão 1 oferece maior controle ")
sleep(2)
print("(B) versão 2 é mais adequada ")
sleep(2)
print("(C) porque usa property e setter, assim deixando o codigo mais profissional")