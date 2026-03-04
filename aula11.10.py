import os 
def clear():
    os.system("cls")
clear()
from time import sleep

class Produto:
    def __init__(self, nome_produto, categoria, quantidade):
        self.nome_produto = nome_produto # publico
        self._categoria = categoria      # protegido
        self.__quantidade = 0            # privado
        self.quantidade = quantidade     # usa setter para validar

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor < 0:
            return "Valor inválido"
        else:
            self.__quantidade = valor


    def adicionar(self, valor):
        if valor > 0:
            self.__quantidade += valor
            print(f"{valor} Produto adicionado ")
        else:
            print("Produto não adicionado")


    def remover(self, valor):
        if valor <= 0:
            print("Valor invalido")
        elif valor > self.__quantidade:
            print("Estoque insuficiente! ")
        else:
            self.__quantidade -= valor
            print(f"{valor} produto removido")


p1 = Produto("Notebook", "Eletrônicos", 10)
print(f"Quantidade atual: {p1.quantidade}")  # 10
sleep(2)


p1.adicionar(5)   # adiciona 5
print(f"Quantidade atual: {p1.quantidade}")  # 15
sleep(2)
clear()

p1.remover(8)     # remove 8 
print(f"Quantidade atual: {p1.quantidade}")  # 7
sleep(2)
clear()
p1.remover(8)    # estoque insuficiente
    
    # DESAFIO

# 1) para proteger que nenhum valor invalido seja colocado no atributo
# 2) permitir alterar valores, transformar metodos em atributos 
# 3) bloquear entradas invalidas
# 4) todos poderiam alterar, quebraria a logica de estoque 
# 5) estoque negativo, calculos errados e manipular os dados
    