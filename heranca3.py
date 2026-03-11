import os 
def clear():
    os.system("cls")
clear()

class animal:
    def falar(self):
        return "O animal fez um som"
    
class cachorro(animal):
    def falar(self):
        return "Auau"

class fala(animal):
    def falar(self):
        return "O cachorro late"

dog = fala()
print(dog.falar())

dog = cachorro()
print(dog.falar())