import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class produto:
    def __init__(self, preco):
        self.preco = preco
    
pdt = produto(100)
pdt.preco = -200
print(pdt.preco) 

# é um problema porque ser público significa que pode alterar o valor livremente