import os 
def clear():
    os.system("cls")
clear()

class veiculo:
    def mover(self):
        print("O veiculo está se movendo")

class moto(veiculo):
    pass

m = moto()
m.mover()

#1 ela herdou o metodo

