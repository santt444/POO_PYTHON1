import os 
def clear():
    os.system("cls")
clear()

class animal:
    def falar(self):
        print("O animal fez um som")
    
class cachorro(animal):
    def falar(self):
        print("Auau")

class fala(animal):
    def falar(self):
        print("O cachorro fala ")

dog = fala()
dog.falar()
dog = cachorro()
dog.falar()