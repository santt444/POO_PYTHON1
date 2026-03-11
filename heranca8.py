import os 
def clear():
    os.system("cls")
clear()

class Veiculo:
    def __init__(self, marca):
        self.marca = marca 
        
    def mover(self):
        return "O veículo está se movendo"

class carro(Veiculo):
    def mover(self):
        return f"O carro da marca {self.marca} está se movendo a 90kmh "

class moto(Veiculo):
    def mover(self):
      return f"A moto da marca {self.marca} está se movendo a 100kmh"

car = carro("BMW")
print(car.mover())

mot = moto("MT03")
print(mot.mover())
